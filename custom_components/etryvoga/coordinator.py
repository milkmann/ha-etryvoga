"""DataUpdateCoordinator for eTryvoga integration."""
import asyncio
from datetime import datetime, timezone
import json
import logging
from typing import Any
import aiohttp

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import (
    API_ALERTS_URL,
    API_CONFIRMED_URL,
    API_LIVE_SSE_URL,
    CONF_CITY_NAME,
    CONF_DISTRICT_SLUG,
    CONF_OBLAST,
    DEFAULT_SCAN_INTERVAL,
    DOMAIN,
    EVENT_ALARM_CANCELLED,
    EVENT_ALARM_STARTED,
    EVENT_THREAT_CANCELLED,
    EVENT_THREAT_DETECTED,
    LEVEL_CLEAR,
    LEVEL_RED,
    LEVEL_YELLOW,
    STATUS_CANCEL,
    STATUS_SIREN,
    THREAT_ARTILLERY,
    THREAT_DRONE,
    THREAT_EXPLOSION,
    THREAT_KAB,
    THREAT_RECON,
    THREAT_ROCKET,
    THREAT_SHELLING,
    USER_AGENT,
    normalize_threat_type,
    BIT_AIR,
    BIT_ARTILLERY,
    BIT_BALLISTIC,
    BIT_CHEMICAL,
    BIT_DRONE,
    BIT_EXPLOSION,
    BIT_KAB,
    BIT_NUCLEAR,
    BIT_OBLAST_ALERT,
    BIT_RECON,
    BIT_ROCKET,
    BIT_URBAN_FIGHTS,
)
from .geo_data import DISTRICTS_BY_SLUG, OBLAST_REGIONS, OBLAST_TO_DISTRICTS

_LOGGER = logging.getLogger(__name__)


class ETryvogaDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Coordinator handling REST bootstrap and background real-time SSE stream."""

    def __init__(
        self,
        hass: HomeAssistant,
        session: aiohttp.ClientSession,
        oblast: str,
        district_slug: str,
        city_name: str | None = None,
        include_neighbors: bool = True,
    ) -> None:
        """Initialize the coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN}_{district_slug}",
            update_interval=DEFAULT_SCAN_INTERVAL,
        )
        self.session = session
        self.oblast = oblast
        self.district_slug = district_slug
        if district_slug == "_OBLAST_":
            self.district_title = oblast
        else:
            self.district_title = DISTRICTS_BY_SLUG.get(district_slug, {}).get("title", district_slug)
        self.city_name = city_name
        self.include_neighbors = include_neighbors

        self._sse_task: asyncio.Task | None = None
        self._is_stopped = False
        self._is_sse_active = False
        self._sse_last_received = 0.0
        self._raw_alerts_cache: dict[str, Any] = {}
        self._raw_confirmed_cache: list[dict[str, Any]] = []
        self._has_bootstrap_confirmed = False

    async def async_start_sse(self) -> None:
        """Spawn background SSE consumer task."""
        if self._sse_task and not self._sse_task.done():
            return
        self._is_stopped = False
        self._sse_task = self.hass.async_create_background_task(
            self._sse_consumer_loop(),
            name=f"etryvoga_sse_{self.district_slug}",
        )

    async def _sse_consumer_loop(self) -> None:
        """Listen to /api/map/live with auto-reconnect and exponential backoff."""
        backoff = 2
        headers = {
            "Accept": "text/event-stream",
            "User-Agent": USER_AGENT,
            "Referer": "https://map.etryvoga.com/",
        }

        while not self._is_stopped:
            try:
                _LOGGER.debug("Connecting to eTryvoga SSE stream: %s", API_LIVE_SSE_URL)
                timeout = aiohttp.ClientTimeout(total=None, sock_read=90)
                async with self.session.get(API_LIVE_SSE_URL, headers=headers, timeout=timeout) as resp:
                    if resp.status != 200:
                        self._is_sse_active = False
                        _LOGGER.warning("eTryvoga SSE stream returned status %s, retrying in %ss", resp.status, backoff)
                        await asyncio.sleep(backoff)
                        backoff = min(backoff * 2, 60)
                        continue

                    backoff = 2  # Reset backoff on successful handshake
                    self._is_sse_active = True
                    _LOGGER.info("Connected to eTryvoga live SSE eventstream successfully")

                    current_event: str | None = None

                    async for line in resp.content:
                        if self._is_stopped:
                            break
                        decoded = line.decode("utf-8", errors="ignore").strip()
                        if not decoded:
                            current_event = None
                            continue

                        # Handle SSE event type headers
                        if decoded.startswith("event:"):
                            current_event = decoded[6:].strip().lower()
                            continue

                        # Update liveness timestamp on any non-empty SSE line
                        self._is_sse_active = True
                        self._sse_last_received = asyncio.get_running_loop().time()

                        # Ignore health / ping events to avoid unnecessary entity updates
                        if current_event in ("health", "ping"):
                            continue

                        # SSE payload lines start with 'data:' or raw JSON in some proxies
                        payload_str = decoded[5:].strip() if decoded.startswith("data:") else decoded
                        if payload_str.startswith("{") and payload_str.endswith("}"):
                            try:
                                payload = json.loads(payload_str)
                                # Ignore health/ping payload dicts
                                if ("districtsReady" in payload and "storiesReady" in payload) or (
                                    "health" in payload and len(payload) == 1
                                ):
                                    continue
                                self._is_sse_active = True
                                self._sse_last_received = asyncio.get_running_loop().time()
                                self._handle_live_payload(payload)
                            except Exception as err:
                                _LOGGER.debug("Could not parse SSE JSON line: %s (%s)", decoded, err)

            except asyncio.CancelledError:
                self._is_sse_active = False
                break
            except Exception as err:
                self._is_sse_active = False
                if not self._is_stopped:
                    err_str = str(err).lower()
                    if isinstance(err, (TimeoutError, asyncio.TimeoutError)) or "timeout" in err_str:
                        _LOGGER.debug("eTryvoga SSE stream socket timeout (keepalive cycle), reconnecting in %ss...", backoff)
                    else:
                        _LOGGER.warning("eTryvoga SSE stream error: %s. Reconnecting in %ss...", err, backoff)
                    await asyncio.sleep(backoff)
                    backoff = min(backoff * 2, 60)

    def _handle_live_payload(self, live_data: dict[str, Any]) -> None:
        """Merge live SSE stories and district alerts into state and push updates to entities."""
        # 1. Update districts cache if present in live SSE snapshot
        new_districts = live_data.get("districts")
        if isinstance(new_districts, list) and new_districts:
            self._raw_alerts_cache["districts"] = new_districts

        # 2. Collect stories from live stream categories
        categorized_keys = (
            "uavStories",
            "droneStories",
            "kabStories",
            "rocketStories",
            "shellingStories",
            "reconStories",
            "explosionStories",
        )
        cat_type_map = {
            "uavStories": THREAT_DRONE,
            "droneStories": THREAT_DRONE,
            "kabStories": THREAT_KAB,
            "rocketStories": THREAT_ROCKET,
            "shellingStories": THREAT_ARTILLERY,
            "reconStories": THREAT_RECON,
            "explosionStories": THREAT_EXPLOSION,
        }

        has_categorized_keys = any(k in live_data for k in categorized_keys)
        has_story_keys = has_categorized_keys or ("stories" in live_data)

        new_confirmed: list[dict[str, Any]] = []
        seen_ids: set[Any] = set()

        if has_categorized_keys:
            # Modern categorized payload: extract from each category list
            for key in categorized_keys:
                stories = live_data.get(key, [])
                if isinstance(stories, list):
                    default_type = cat_type_map.get(key, "unknown")
                    for st in stories:
                        sid = st.get("id")
                        if sid is not None and sid in seen_ids:
                            continue
                        if sid is not None:
                            seen_ids.add(sid)
                        if not st.get("type"):
                            st["type"] = default_type
                        new_confirmed.append(st)
        elif "stories" in live_data:
            # Fallback ONLY if categorized lists were absent from payload
            general_stories = live_data.get("stories", [])
            if isinstance(general_stories, list):
                for st in general_stories:
                    st_type = st.get("type", "")
                    if st_type not in ("siren", "cancel"):
                        sid = st.get("id")
                        if sid is not None and sid in seen_ids:
                            continue
                        if sid is not None:
                            seen_ids.add(sid)
                        new_confirmed.append(st)

        # Update confirmed cache whenever threat lists are present in payload
        # (clears cache when 0 threats, preventing stuck old threats)
        if has_story_keys:
            self._raw_confirmed_cache = new_confirmed
            self._has_bootstrap_confirmed = True

        # 3. Re-aggregate state immediately with live data
        new_state = self._aggregate_state(self._raw_alerts_cache, self._raw_confirmed_cache)
        self.async_set_updated_data(new_state)

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch REST snapshot of alerts and confirmed threats."""
        headers = {
            "Accept": "application/json",
            "User-Agent": USER_AGENT,
            "Referer": "https://map.etryvoga.com/",
        }

        try:
            async with self.session.get(API_ALERTS_URL, headers=headers, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                if resp.status != 200:
                    raise UpdateFailed(f"Failed to fetch alerts: HTTP {resp.status}")
                alerts_data = await resp.json()

            # Protect confirmed cache: do NOT overwrite with partial REST data if SSE stream is healthy
            sse_healthy = (
                self._is_sse_active
                and (asyncio.get_running_loop().time() - self._sse_last_received < 120)
            )
            if not sse_healthy or not self._has_bootstrap_confirmed:
                async with self.session.get(API_CONFIRMED_URL, headers=headers, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                    if resp.status == 200:
                        confirmed_data = await resp.json()
                        if isinstance(confirmed_data, list):
                            self._raw_confirmed_cache = confirmed_data
                            self._has_bootstrap_confirmed = True

            self._raw_alerts_cache = alerts_data

            # Ensure background SSE stream is active
            await self.async_start_sse()

            return self._aggregate_state(self._raw_alerts_cache, self._raw_confirmed_cache)

        except Exception as err:
            raise UpdateFailed(f"eTryvoga connection error: {err}") from err

    def _aggregate_state(self, alerts_payload: dict[str, Any], confirmed_items: list[dict[str, Any]]) -> dict[str, Any]:
        """Aggregate raw data for the configured district and city."""
        now = datetime.now(timezone.utc)
        districts = alerts_payload.get("districts", [])

        # Status & Level
        if self.district_slug == "_OBLAST_":
            oblast_slugs = OBLAST_TO_DISTRICTS.get(self.oblast, [])
            oblast_districts = [d for d in districts if d.get("slug") in oblast_slugs]
            active_districts = [d for d in oblast_districts if d.get("status") == STATUS_SIREN]
            is_siren = len(active_districts) > 0
            if is_siren:
                is_all_red = any(d.get("alertLevel") == "red" for d in active_districts)
                alert_level = LEVEL_RED if is_all_red else LEVEL_YELLOW
                status_at = min((d.get("statusAt") for d in active_districts if d.get("statusAt")), default=None)
            else:
                alert_level = LEVEL_CLEAR
                status_at = None
        else:
            # Find our district object
            our_district = next((d for d in districts if d.get("slug") == self.district_slug), None)
            if not our_district:
                # Fallback by title match
                our_district = next((d for d in districts if d.get("title") == self.district_title), {})

            raw_status = our_district.get("status", STATUS_CANCEL)
            raw_level = our_district.get("alertLevel")
            status_at = our_district.get("statusAt")

            is_siren = (raw_status == STATUS_SIREN)
            if is_siren:
                alert_level = LEVEL_YELLOW if raw_level == "yellow" else LEVEL_RED
            else:
                alert_level = LEVEL_CLEAR

        # Duration calculation
        duration_minutes = 0
        if is_siren and status_at:
            try:
                # Handle ISO 8601 format
                clean_ts = status_at.replace("Z", "+00:00")
                start_dt = datetime.fromisoformat(clean_ts)
                duration_minutes = max(0, int((now - start_dt).total_seconds() // 60))
            except Exception:
                pass

        # Filter confirmed threats relevant to our location
        relevant_threats = []
        stopwords = {
            "область", "області", "областю", "областях",
            "район", "району", "районі", "районом", "районах",
            "місто", "міста", "місті", "містом",
            "громада", "громади", "громаді", "громадою",
            "селище", "село", "села", "селі", "смт",
        }

        def _get_stems(text: str) -> list[str]:
            words = [w.lower().strip("()[]\",.") for w in text.split() if len(w) > 2]
            filtered = [w for w in words if w not in stopwords]
            stems: set[str] = set()
            for w in filtered:
                stems.add(w)
                stem = w
                for ending in (
                    "івського", "івському", "івська", "івське", "івський", "івських", "івської",
                    "ського", "ському", "ська", "ське", "ський", "ських", "ської",
                    "цького", "цькому", "цька", "цьке", "цький", "цьких", "цької",
                    "зького", "зькому", "зька", "зьке", "зький", "зьких", "зької",
                    "жжя", "щина", "щини", "щині", "щиною",
                ):
                    if stem.endswith(ending):
                        stem = stem[:-len(ending)]
                        break
                if len(stem) >= 3:
                    stems.add(stem)
                # Suffixes with -цьк- (e.g. Луцький -> луць, Вінницька -> вінниць/вінни, Чернівецька -> чернів)
                if w.endswith(("цький", "цьке", "цька", "цькому", "цького", "цьких", "цької")):
                    for suf in ("кий", "ка", "ке", "кому", "кого", "ких", "кої"):
                        if w.endswith(suf):
                            s2 = w[:-len(suf)]
                            if len(s2) >= 3:
                                stems.add(s2)
                                if s2.endswith("к"):
                                    stems.add(s2[:-1])
                                if s2.endswith("ець"):
                                    stems.add(s2[:-3])
                            break
                # Base noun inflection declensions for Ukrainian settlements
                for n_end in (
                    "ами", "ями", "ах", "ях", "ом", "ем", "ям", "ам", "ів", "ей",
                    "а", "я", "е", "є", "и", "і", "о", "у", "ю"
                ):
                    if w.endswith(n_end) and len(w) - len(n_end) >= 3:
                        stems.add(w[:-len(n_end)])
                        break
                # Ukrainian vowel alternations and root reductions (Львів -> львов, Харків -> харков, etc.)
                if w.endswith("ів") and len(w) > 3:
                    stems.add(w[:-2] + "ов")
                elif w.endswith("їв") and len(w) > 3:
                    stems.add(w[:-2] + "єв")
                elif w.endswith("піль") and len(w) > 4:
                    stems.add(w[:-4] + "пол")
                    stems.add(w[:-4])
                if w.endswith("цьк") and len(w) - 1 >= 3:
                    stems.add(w[:-1])
                if w.endswith("ськ") and len(w) - 2 >= 3:
                    stems.add(w[:-2])
            return list(stems)

        oblast_stems = _get_stems(self.oblast)
        district_stems = _get_stems(self.district_title)
        city_stems = _get_stems(self.city_name) if self.city_name else []

        for item in confirmed_items:
            title = item.get("title") or ""
            body = item.get("body") or ""
            region = item.get("region") or ""
            title_lower = title.lower()
            body_lower = body.lower()
            region_lower = region.lower()
            text_to_search = f"{title_lower} {body_lower} {region_lower}"

            # Check if threat affects our city, district, or oblast
            is_city_match = bool(city_stems and any(cs in text_to_search for cs in city_stems))
            is_district_match = bool(district_stems and any(ds in text_to_search for ds in district_stems))
            is_oblast_match = bool(self.include_neighbors and oblast_stems and any(os in text_to_search for os in oblast_stems))

            if is_city_match or is_district_match or is_oblast_match:
                raw_type = item.get("type", "unknown")
                norm_type = normalize_threat_type(raw_type)
                approach = item.get("approach") or {}
                origin = (
                    approach.get("origin_title")
                    or approach.get("heading")
                    or approach.get("area_sector")
                    or approach.get("cardinal")
                    or "Не вказано"
                )
                relevant_threats.append({
                    "id": item.get("id"),
                    "type": norm_type,
                    "raw_type": raw_type,
                    "title": title,
                    "body": body,
                    "origin": origin,
                    "time": item.get("createdAtParsed", ""),
                    "is_direct": bool(is_city_match or is_district_match),
                })

        # Calculate threat boolean flags
        threat_flags = {
            THREAT_KAB: any(t["type"] == THREAT_KAB for t in relevant_threats),
            THREAT_DRONE: any(t["type"] == THREAT_DRONE for t in relevant_threats),
            THREAT_ROCKET: any(t["type"] == THREAT_ROCKET for t in relevant_threats),
            THREAT_ARTILLERY: any(t["type"] == THREAT_ARTILLERY for t in relevant_threats),
            THREAT_RECON: any(t["type"] == THREAT_RECON for t in relevant_threats),
            THREAT_EXPLOSION: any(t["type"] == THREAT_EXPLOSION for t in relevant_threats),
        }

        # Human-readable tactical summary
        tactical_summary = self._build_tactical_summary(is_siren, alert_level, relevant_threats)

        # Detect state transitions for event generation (collect all transitions, not just the first)
        previous_data = self.data or {}
        prev_siren = previous_data.get("is_siren", False)
        prev_threats = previous_data.get("threats", [])
        events_to_trigger: list[dict[str, Any]] = []

        if is_siren and not prev_siren:
            events_to_trigger.append({
                "event_type": EVENT_ALARM_STARTED,
                "payload": {"district": self.district_title, "level": alert_level, "summary": tactical_summary},
                "ts": now.isoformat(),
            })
        elif not is_siren and prev_siren:
            events_to_trigger.append({
                "event_type": EVENT_ALARM_CANCELLED,
                "payload": {"district": self.district_title, "duration_minutes": duration_minutes},
                "ts": now.isoformat(),
            })

        if relevant_threats and relevant_threats != prev_threats:
            events_to_trigger.append({
                "event_type": EVENT_THREAT_DETECTED,
                "payload": {"district": self.district_title, "threats": relevant_threats, "summary": tactical_summary},
                "ts": now.isoformat(),
            })
        elif not relevant_threats and prev_threats:
            events_to_trigger.append({
                "event_type": EVENT_THREAT_CANCELLED,
                "payload": {"district": self.district_title, "summary": tactical_summary},
                "ts": now.isoformat(),
            })

        event_trigger = events_to_trigger[-1] if events_to_trigger else None

        country_overview = self._build_country_overview(alerts_payload, confirmed_items)

        return {
            "is_siren": is_siren,
            "alert_level": alert_level,
            "status_at": status_at,
            "duration_minutes": duration_minutes,
            "threats": relevant_threats,
            "threat_flags": threat_flags,
            "tactical_summary": tactical_summary,
            "country_overview": country_overview,
            "country_overview_summary": country_overview["summary"],
            "last_event": event_trigger,
            "last_events": events_to_trigger,
            "updated_at": now.isoformat(),
        }

    def _build_country_overview(
        self, alerts_payload: dict[str, Any], confirmed_items: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """Aggregate country-wide status for LED matrices (AWTRIX/Ulanzi) and custom maps."""
        districts = alerts_payload.get("districts", [])
        districts_by_slug = {d.get("slug"): d for d in districts if d.get("slug")}

        # Stem lookup for matching tactical threats to oblasts
        oblast_keywords: dict[str, list[str]] = {
            "Вінницька область": ["вінниц", "вінниччин"],
            "Волинська область": ["волин", "луцьк", "луць", "ковель", "володимир"],
            "Дніпропетровська область": ["дніпро", "дніпр", "крив", "нікопол", "марганець", "покров", "павлоград", "самарів", "кам'янськ"],
            "Донецька область": ["донецьк", "донец", "донеч", "краматорськ", "слов'янськ", "покровськ", "бахмут", "маріупол"],
            "Житомирська область": ["житомир", "коростен", "звягель", "бердичів"],
            "Закарпатська область": ["закарпат", "ужгород", "мукачев"],
            "Запорізька область": ["запоріз", "запоріж", "оріхів", "гуляйпол", "полог", "василівк", "бердянськ", "мелітопол"],
            "Івано-Франківська область": ["івано-франків", "івано-франков", "коломий", "калуш"],
            "Київська область": ["київськ", "біла церква", "бровар", "бориспіл", "вишгород", "буча", "ірпінь", "фастів", "славутич"],
            "м. Київ": ["м. київ", "столиц", "(київ)", "-cds", "(kyiv)"],
            "Кіровоградська область": ["кіровоград", "кропивниц", "олександрій"],
            "Луганська область": ["луганськ", "луган", "сіверськодонецьк", "лисичанськ"],
            "Львівська область": ["львів", "львов", "дрогобич", "стрий", "червоноград", "шептицьк"],
            "Миколаївська область": ["миколаїв", "миколаєв", "вознесенськ", "очаків", "первомайськ"],
            "Одеська область": ["одес", "ізмаїл", "чорноморськ", "білгород"],
            "Полтавська область": ["полтав", "кременчук", "миргород", "лубни"],
            "Рівненська область": ["рівнен", "рівн", "сарни", "дубно", "вараш"],
            "Сумська область": ["суми", "сум", "сумськ", "сумщин", "конотоп", "шостк", "охтирк", "ромен", "ромн"],
            "Тернопільська область": ["терноп", "кременець", "чортків"],
            "Харківська область": ["харків", "харков", "куп'янськ", "ізюм", "чугуїв", "лозов", "богодухів"],
            "Херсонська область": ["херсон", "берислав", "каховк", "скадовськ", "генічеськ"],
            "Хмельницька область": ["хмельниц", "кам'янець", "шепетівк"],
            "Черкаська область": ["черкас", "умань", "уман", "сміла", "сміл", "золотонош"],
            "Чернівецька область": ["чернів", "буковин"],
            "Чернігівська область": ["чернігів", "чернігов", "ніжин", "прилук", "корюківк", "новгород-сіверськ"],
            "АР Крим": ["крим", "севастопол", "сімферопол", "керч", "ялт", "євпатор"],
        }

        # Index threats by oblast
        threats_by_oblast: dict[str, list[dict[str, Any]]] = {obl: [] for obl in OBLAST_REGIONS}
        for t in confirmed_items:
            t_title = t.get("title") or ""
            t_body = t.get("body") or ""
            t_region = t.get("region") or ""
            text = f"{t_title} {t_body} {t_region}".lower()
            for obl, kws in oblast_keywords.items():
                is_match = False
                for kw in kws:
                    if kw in text:
                        # Prevent Dnipropetrovsk 'покров' matching Donetsk 'покровськ'
                        if kw == "покров" and "покровськ" in text:
                            continue
                        is_match = True
                        break
                if is_match:
                    threats_by_oblast[obl].append(t)

        regions_status: dict[str, str] = {}
        oblasts_data: dict[str, Any] = {}
        states_data: dict[str, Any] = {}
        threat_flags_data: dict[str, int] = {}
        active_regions: list[str] = []

        sirens_districts_count = 0
        sirens_oblasts_count = 0

        for obl in OBLAST_REGIONS:
            slugs = OBLAST_TO_DISTRICTS.get(obl, [])
            obl_districts = [districts_by_slug[s] for s in slugs if s in districts_by_slug]

            active_dstrs = [d for d in obl_districts if d.get("status") == STATUS_SIREN]
            sirens_districts_count += len(active_dstrs)
            is_siren = len(active_dstrs) > 0

            # Bitmask calculation for LED maps
            flags = 0
            if is_siren:
                sirens_oblasts_count += 1
                flags |= BIT_AIR
                if len(active_dstrs) == len(obl_districts) and len(obl_districts) > 0:
                    flags |= BIT_OBLAST_ALERT

            obl_threats = threats_by_oblast.get(obl, [])
            has_kab = False
            has_drone = False
            has_missile = False
            has_artillery = False
            has_explosion = False
            has_recon = False

            for t in obl_threats:
                raw_t = t.get("type", "")
                norm_t = normalize_threat_type(raw_t)
                if norm_t == THREAT_KAB:
                    flags |= BIT_KAB
                    has_kab = True
                elif norm_t == THREAT_DRONE:
                    flags |= BIT_DRONE
                    has_drone = True
                elif norm_t == THREAT_ROCKET:
                    flags |= BIT_ROCKET
                    if (raw_t or "").lower().strip() == "ballistic":
                        flags |= BIT_BALLISTIC
                    has_missile = True
                elif norm_t == THREAT_RECON:
                    flags |= BIT_RECON
                    has_recon = True
                elif norm_t == THREAT_ARTILLERY:
                    flags |= BIT_ARTILLERY
                    has_artillery = True
                elif norm_t == THREAT_EXPLOSION:
                    flags |= BIT_EXPLOSION
                    has_explosion = True

            # Determine level & LED display color (red / yellow / blue)
            if is_siren:
                is_red = any(d.get("alertLevel") == "red" for d in active_dstrs) or has_kab or has_missile
                obl_level = LEVEL_RED if is_red else LEVEL_YELLOW
                obl_color = "red" if is_red else "yellow"
                obl_status = STATUS_SIREN
            elif flags > 0:
                obl_level = LEVEL_YELLOW
                obl_color = "yellow"
                obl_status = LEVEL_CLEAR
            else:
                obl_level = LEVEL_CLEAR
                obl_color = "blue"
                obl_status = LEVEL_CLEAR

            is_enabled = is_siren or (flags > 0)
            if is_enabled:
                active_regions.append(obl)

            oblasts_data[obl] = {
                "status": obl_status,
                "level": obl_level,
                "color": obl_color,
                "threat_flags": flags,
                "active_districts": len(active_dstrs),
                "total_districts": len(obl_districts),
                "siren_districts": [d.get("title") for d in active_dstrs if d.get("title")],
            }

            region_state = {
                "enabled": is_enabled,
                "level": obl_level,
                "color": obl_color,
                "threat_flags": flags,
                "siren": is_siren,
                "air": is_siren,
                "kab": has_kab,
                "drone": has_drone,
                "missile": has_missile,
                "artillery": has_artillery,
                "explosion": has_explosion,
                "recon": has_recon,
                "active_districts": len(active_dstrs),
                "total_districts": len(obl_districts),
                "siren_districts": [d.get("title") for d in active_dstrs if d.get("title")],
            }
            states_data[obl] = region_state
            threat_flags_data[obl] = flags

            # Map multiple key variants for flexible Jinja2 / AWTRIX / Ulanzi templates
            regions_status[obl] = obl_level
            short = obl.replace(" область", "")
            regions_status[short] = obl_level
            if short == "м. Київ":
                regions_status["Київ"] = obl_level
            elif short == "АР Крим":
                regions_status["Крим"] = obl_level

        # Add popular aliases for instant template access (e.g. states['Київ'])
        if "м. Київ" in states_data:
            states_data["Київ"] = states_data["м. Київ"]
            threat_flags_data["Київ"] = threat_flags_data["м. Київ"]
        if "АР Крим" in states_data:
            states_data["Крим"] = states_data["АР Крим"]
            threat_flags_data["Крим"] = threat_flags_data["АР Крим"]

        # Extra city units like Sevastopol
        if "SEVASTOPOL-CITY" in districts_by_slug:
            sev = districts_by_slug["SEVASTOPOL-CITY"]
            sev_siren = sev.get("status") == STATUS_SIREN
            sev_flags = (BIT_AIR | BIT_OBLAST_ALERT) if sev_siren else 0
            sev_lvl = LEVEL_RED if sev_siren else LEVEL_CLEAR
            sev_color = "red" if sev_siren else "blue"
            regions_status["м. Севастополь"] = sev_lvl
            regions_status["Севастополь"] = sev_lvl
            sev_state = {
                "enabled": sev_siren,
                "level": sev_lvl,
                "color": sev_color,
                "threat_flags": sev_flags,
                "siren": sev_siren,
                "air": sev_siren,
                "kab": False,
                "drone": False,
                "missile": False,
                "artillery": False,
                "explosion": False,
                "recon": False,
                "active_districts": 1 if sev_siren else 0,
                "total_districts": 1,
                "siren_districts": ["Севастополь"] if sev_siren else [],
            }
            states_data["м. Севастополь"] = sev_state
            states_data["Севастополь"] = sev_state
            threat_flags_data["м. Севастополь"] = sev_flags
            threat_flags_data["Севастополь"] = sev_flags

        # Format tactical threats
        tactical_threats = []
        drones_cnt = 0
        kabs_cnt = 0
        missiles_cnt = 0
        recon_cnt = 0
        shelling_cnt = 0
        explosions_cnt = 0

        for t in confirmed_items:
            raw_t = t.get("type", "")
            norm_t = normalize_threat_type(raw_t)
            if norm_t == THREAT_DRONE:
                drones_cnt += 1
            elif norm_t == THREAT_KAB:
                kabs_cnt += 1
            elif norm_t == THREAT_ROCKET:
                missiles_cnt += 1
            elif norm_t == THREAT_RECON:
                recon_cnt += 1
            elif norm_t == THREAT_ARTILLERY:
                shelling_cnt += 1
            elif norm_t == THREAT_EXPLOSION:
                explosions_cnt += 1

            appr = t.get("approach") or {}
            origin = appr.get("origin_title") or appr.get("heading") or appr.get("area_sector") or ""
            direction = appr.get("heading") or appr.get("area_sector") or appr.get("cardinal", "")

            tactical_threats.append({
                "type": norm_t,
                "raw_type": raw_t,
                "title": t.get("title") or "",
                "region": t.get("region") or "",
                "origin": origin,
                "direction": direction,
                "time": t.get("createdAtParsed") or "",
                "body": t.get("body") or "",
            })

        counts = {
            "total_threats": len(confirmed_items),
            "drones": drones_cnt,
            "kabs": kabs_cnt,
            "missiles": missiles_cnt,
            "recon": recon_cnt,
            "shelling": shelling_cnt,
            "explosions": explosions_cnt,
            "sirens_districts": sirens_districts_count,
            "sirens_oblasts": sirens_oblasts_count,
        }

        # Build readable state string
        parts = []
        if len(confirmed_items) > 0:
            threat_parts = []
            if drones_cnt > 0:
                threat_parts.append(f"{drones_cnt} БПЛА")
            if kabs_cnt > 0:
                threat_parts.append(f"{kabs_cnt} КАБ")
            if missiles_cnt > 0:
                threat_parts.append(f"{missiles_cnt} ракет")
            if recon_cnt > 0:
                threat_parts.append(f"{recon_cnt} розвід. БПЛА")
            if shelling_cnt > 0:
                threat_parts.append(f"{shelling_cnt} обстрілів")
            if explosions_cnt > 0:
                threat_parts.append(f"{explosions_cnt} вибухів")
            parts.append(f"{len(confirmed_items)} загроз ({', '.join(threat_parts)})")
        else:
            parts.append("Загроз немає")

        if sirens_districts_count > 0:
            parts.append(f"{sirens_districts_count} тривог ({sirens_oblasts_count} обл.)")
        else:
            parts.append("Тривог немає")

        summary = " | ".join(parts)

        # Build districts dictionary (slug -> {title, status, level, status_at})
        districts_dict = {}
        for d in districts:
            slug = d.get("slug")
            if slug:
                districts_dict[slug] = {
                    "title": d.get("title", ""),
                    "status": d.get("status", "clear"),
                    "level": d.get("alertLevel") or ("red" if d.get("status") == STATUS_SIREN else "clear"),
                    "status_at": d.get("statusAt"),
                }

        return {
            "summary": summary,
            "states": states_data,
            "active_regions": active_regions,
            "threat_flags": threat_flags_data,
            "regions_status": regions_status,
            "oblasts": oblasts_data,
            "districts": districts_dict,
            "tactical_threats": tactical_threats,
            "counts": counts,
        }

    def _build_tactical_summary(self, is_siren: bool, alert_level: str, threats: list[dict[str, Any]]) -> str:
        """Create a human-friendly Ukrainian summary string."""
        if not is_siren and not threats:
            return "Обстановка спокійна. Тривоги немає."

        parts = []
        if is_siren:
            level_str = "Жовтий рівень (дрони)" if alert_level == LEVEL_YELLOW else "Повітряна тривога"
            parts.append(f"🚨 {level_str}")

        kabs = [t for t in threats if t["type"] == THREAT_KAB]
        drones = [t for t in threats if t["type"] == THREAT_DRONE]
        rockets = [t for t in threats if t["type"] == THREAT_ROCKET]
        artillery = [t for t in threats if t["type"] == THREAT_ARTILLERY]
        recon = [t for t in threats if t["type"] == THREAT_RECON]
        explosions = [t for t in threats if t["type"] == THREAT_EXPLOSION]

        if kabs:
            origins = ", ".join(set(k["origin"] for k in kabs if k.get("origin") and k["origin"] != "Не вказано"))
            if origins:
                parts.append(f"💣 Загроза КАБ (напрямок: {origins})")
            else:
                parts.append(f"💣 Загроза КАБ ({len(kabs)} подій)")
        if drones:
            parts.append(f"🛸 Ударні БПЛА в зоні контролю ({len(drones)} подій)")
        if rockets:
            parts.append("🚀 Ракетна небезпека!")
        if artillery:
            parts.append("💥 Загроза артобстрілу")
        if recon:
            parts.append(f"👁️ Розвідувальний БПЛА ({len(recon)} подій)")
        if explosions:
            parts.append(f"⚠️ Повідомлення про вибух ({len(explosions)} подій)")

        if parts:
            return "; ".join(parts)
        if is_siren:
            return "Повітряна тривога активна"
        return "Обстановка спокійна. Тривоги немає."

    async def async_close(self) -> None:
        """Cancel and clean up the background SSE stream."""
        self._is_stopped = True
        if self._sse_task and not self._sse_task.done():
            self._sse_task.cancel()
            try:
                await self._sse_task
            except asyncio.CancelledError:
                pass
