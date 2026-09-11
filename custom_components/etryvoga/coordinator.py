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
    EVENT_THREAT_DETECTED,
    LEVEL_CLEAR,
    LEVEL_RED,
    LEVEL_YELLOW,
    STATUS_CANCEL,
    STATUS_SIREN,
    THREAT_DRONE,
    THREAT_EXPLOSION,
    THREAT_KAB,
    THREAT_RECON,
    THREAT_ROCKET,
    THREAT_SHELLING,
    USER_AGENT,
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
        self._raw_alerts_cache: dict[str, Any] = {}
        self._raw_confirmed_cache: list[dict[str, Any]] = []

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
                        _LOGGER.warning("eTryvoga SSE stream returned status %s, retrying in %ss", resp.status, backoff)
                        await asyncio.sleep(backoff)
                        backoff = min(backoff * 2, 60)
                        continue

                    backoff = 2  # Reset backoff on successful handshake
                    _LOGGER.info("Connected to eTryvoga live SSE eventstream successfully")

                    async for line in resp.content:
                        if self._is_stopped:
                            break
                        decoded = line.decode("utf-8", errors="ignore").strip()
                        if not decoded:
                            continue

                        # SSE payload lines start with 'data:' or raw JSON in some proxies
                        payload_str = decoded[5:].strip() if decoded.startswith("data:") else decoded
                        if payload_str.startswith("{") and payload_str.endswith("}"):
                            try:
                                payload = json.loads(payload_str)
                                self._handle_live_payload(payload)
                            except Exception as err:
                                _LOGGER.debug("Could not parse SSE JSON line: %s (%s)", decoded, err)

            except asyncio.CancelledError:
                break
            except Exception as err:
                if not self._is_stopped:
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
        new_confirmed: list[dict[str, Any]] = []
        for key in ("uavStories", "droneStories", "kabStories", "rocketStories", "shellingStories", "reconStories", "explosionStories"):
            stories = live_data.get(key, [])
            if isinstance(stories, list):
                new_confirmed.extend(stories)

        # Fallback to top-level stories if categorized lists were empty
        if not new_confirmed:
            general_stories = live_data.get("stories", [])
            if isinstance(general_stories, list):
                new_confirmed.extend(general_stories)

        if new_confirmed:
            self._raw_confirmed_cache = new_confirmed

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

            async with self.session.get(API_CONFIRMED_URL, headers=headers, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                if resp.status == 200:
                    confirmed_data = await resp.json()
                else:
                    confirmed_data = self._raw_confirmed_cache

            self._raw_alerts_cache = alerts_data
            self._raw_confirmed_cache = confirmed_data if isinstance(confirmed_data, list) else []

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
                for ending in ("ського", "ському", "ська", "ське", "ський", "ських", "ської", "івський", "івська", "івське", "зький", "зька", "зьке", "жжя"):
                    if stem.endswith(ending):
                        stem = stem[:-len(ending)]
                        break
                if len(stem) >= 4:
                    stems.add(stem)
            return list(stems)

        oblast_stems = _get_stems(self.oblast)
        district_stems = _get_stems(self.district_title)
        city_stems = _get_stems(self.city_name) if self.city_name else []

        for item in confirmed_items:
            title = item.get("title", "")
            title_lower = title.lower()
            body_lower = item.get("body", "").lower()
            text_to_search = f"{title_lower} {body_lower}"

            # Check if threat affects our city, district, or oblast
            is_city_match = bool(city_stems and any(cs in text_to_search for cs in city_stems))
            is_district_match = bool(district_stems and any(ds in text_to_search for ds in district_stems))
            is_oblast_match = bool(self.include_neighbors and oblast_stems and any(os in text_to_search for os in oblast_stems))

            if is_city_match or is_district_match or is_oblast_match:
                approach = item.get("approach") or {}
                origin = approach.get("origin_title") or approach.get("cardinal") or "Не вказано"
                relevant_threats.append({
                    "id": item.get("id"),
                    "type": item.get("type", "unknown"),
                    "title": title,
                    "body": item.get("body", ""),
                    "origin": origin,
                    "time": item.get("createdAtParsed", ""),
                    "is_direct": bool(is_city_match or is_district_match),
                })

        # Calculate threat boolean flags
        threat_flags = {
            THREAT_KAB: any(t["type"] == THREAT_KAB for t in relevant_threats),
            THREAT_DRONE: any(t["type"] == THREAT_DRONE for t in relevant_threats),
            THREAT_ROCKET: any(t["type"] == THREAT_ROCKET for t in relevant_threats),
            THREAT_SHELLING: any(t["type"] == THREAT_SHELLING for t in relevant_threats),
            THREAT_RECON: any(t["type"] == THREAT_RECON for t in relevant_threats),
            THREAT_EXPLOSION: any(t["type"] == THREAT_EXPLOSION for t in relevant_threats),
        }

        # Human-readable tactical summary
        tactical_summary = self._build_tactical_summary(is_siren, alert_level, relevant_threats)

        # Detect state transitions for event generation
        previous_data = self.data or {}
        prev_siren = previous_data.get("is_siren", False)
        event_trigger = None

        if is_siren and not prev_siren:
            event_trigger = {
                "event_type": EVENT_ALARM_STARTED,
                "payload": {"district": self.district_title, "level": alert_level, "summary": tactical_summary},
            }
        elif not is_siren and prev_siren:
            event_trigger = {
                "event_type": EVENT_ALARM_CANCELLED,
                "payload": {"district": self.district_title, "duration_minutes": duration_minutes},
            }
        elif relevant_threats and relevant_threats != previous_data.get("threats", []):
            event_trigger = {
                "event_type": EVENT_THREAT_DETECTED,
                "payload": {"district": self.district_title, "threats": relevant_threats, "summary": tactical_summary},
            }

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
            "Вінницька область": ["вінниц"],
            "Волинська область": ["волин", "луцьк"],
            "Дніпропетровська область": ["дніпро", "крив", "нікопол", "марганець", "покров", "павлоград", "самарів"],
            "Донецька область": ["донецьк", "краматорськ", "слов'янськ", "покровськ", "бахмут", "маріупол"],
            "Житомирська область": ["житомир", "коростен", "звягель", "бердичів"],
            "Закарпатська область": ["закарпат", "ужгород", "мукачев"],
            "Запорізька область": ["запоріз", "оріхів", "гуляйпол", "полог", "василівк", "бердянськ", "мелітопол"],
            "Івано-Франківська область": ["івано-франків", "коломий", "калуш"],
            "Київська область": ["київськ", "біла церква", "бровар", "бориспіл", "вишгород", "буча", "ірпінь", "фастів", "славутич"],
            "м. Київ": ["м. київ", "столиц"],
            "Кіровоградська область": ["кіровоград", "кропивниц", "олександрій"],
            "Луганська область": ["луганськ", "сіверськодонецьк", "лисичанськ"],
            "Львівська область": ["львів", "дрогобич", "стрий", "червоноград", "шептицьк"],
            "Миколаївська область": ["миколаїв", "вознесенськ", "очаків", "первомайськ"],
            "Одеська область": ["одес", "ізмаїл", "чорноморськ", "білгород"],
            "Полтавська область": ["полтав", "кременчук", "миргород", "лубни"],
            "Рівненська область": ["рівнен", "сарни", "дубно", "варош"],
            "Сумська область": ["сумськ", "конотоп", "шостк", "охтирк", "ромен"],
            "Тернопільська область": ["тернопіль", "кременець", "чортків"],
            "Харківська область": ["харків", "куп'янськ", "ізюм", "чугуїв", "лозов", "богодухів"],
            "Херсонська область": ["херсон", "берислав", "каховк", "скадовськ", "генічеськ"],
            "Хмельницька область": ["хмельниц", "кам'янець", "шепетівк"],
            "Черкаська область": ["черкас", "умань", "сміла", "золотонош"],
            "Чернівецька область": ["чернівець", "буковин"],
            "Чернігівська область": ["чернігів", "ніжин", "прилук", "корюківк", "новгород-сіверськ"],
            "АР Крим": ["крим", "севастопол", "сімферопол", "керч", "ялт", "євпатор"],
        }

        # Index threats by oblast
        threats_by_oblast: dict[str, list[dict[str, Any]]] = {obl: [] for obl in OBLAST_REGIONS}
        for t in confirmed_items:
            text = f"{t.get('title', '')} {t.get('body', '')} {t.get('region', '')}".lower()
            for obl, kws in oblast_keywords.items():
                if any(kw in text for kw in kws):
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
                ttype = t.get("type", "")
                if ttype in ("kab", "fab"):
                    flags |= BIT_KAB
                    has_kab = True
                elif ttype in ("drone", "uav", "shahed"):
                    flags |= BIT_DRONE
                    has_drone = True
                elif ttype in ("rocket", "missile"):
                    flags |= BIT_ROCKET
                    has_missile = True
                elif ttype in ("ballistic",):
                    flags |= BIT_BALLISTIC
                    has_missile = True
                elif ttype in ("recon", "zala", "supercam"):
                    flags |= BIT_RECON
                    has_recon = True
                elif ttype in ("artillery", "shelling"):
                    flags |= BIT_ARTILLERY
                    has_artillery = True
                elif ttype in ("explosion",):
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
            ttype = t.get("type", "")
            if ttype in ("drone", "uav", "shahed"):
                drones_cnt += 1
            elif ttype in ("kab", "fab"):
                kabs_cnt += 1
            elif ttype in ("rocket", "missile", "ballistic"):
                missiles_cnt += 1
            elif ttype in ("recon", "zala", "supercam"):
                recon_cnt += 1
            elif ttype in ("artillery", "shelling"):
                shelling_cnt += 1
            elif ttype in ("explosion",):
                explosions_cnt += 1

            appr = t.get("approach") or {}
            origin = appr.get("origin_title", "")
            direction = appr.get("cardinal", "")

            tactical_threats.append({
                "type": ttype,
                "title": t.get("title", ""),
                "region": t.get("region", ""),
                "origin": origin,
                "direction": direction,
                "time": t.get("createdAtParsed", ""),
                "body": t.get("body", ""),
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
        shelling = [t for t in threats if t["type"] == THREAT_SHELLING]

        if kabs:
            origins = ", ".join(set(k["origin"] for k in kabs if k.get("origin")))
            parts.append(f"💣 Загроза КАБ (напрямок: {origins})")
        if drones:
            parts.append(f"🛸 Ударні БПЛА в зоні контролю ({len(drones)} подій)")
        if rockets:
            parts.append("🚀 Ракетна небезпека!")
        if shelling:
            parts.append("💥 Загроза артобстрілу")

        return "; ".join(parts) if parts else "Повітряна тривога активна"

    async def async_close(self) -> None:
        """Cancel and clean up the background SSE stream."""
        self._is_stopped = True
        if self._sse_task and not self._sse_task.done():
            self._sse_task.cancel()
            try:
                await self._sse_task
            except asyncio.CancelledError:
                pass
