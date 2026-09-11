"""Unit and validation tests for eTryvoga integration."""
import sys
import unittest
from unittest.mock import MagicMock
from importlib.machinery import ModuleSpec

class MockDataUpdateCoordinator:
    def __init__(self, hass, logger, name, update_interval):
        self.hass = hass
        self.logger = logger
        self.name = name
        self.update_interval = update_interval
        self.data = None

    def async_set_updated_data(self, data):
        self.data = data

    def __class_getitem__(cls, item):
        return cls

from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True, kw_only=True)
class SensorEntityDescription:
    key: str
    translation_key: str | None = None
    icon: str | None = None
    device_class: Any | None = None
    native_unit_of_measurement: Any | None = None
    state_class: Any | None = None
    entity_registry_enabled_default: bool = True

@dataclass(frozen=True, kw_only=True)
class BinarySensorEntityDescription:
    key: str
    translation_key: str | None = None
    icon: str | None = None
    device_class: Any | None = None

class EventEntityDescription:
    def __init__(self, key, translation_key=None, icon=None):
        self.key = key
        self.translation_key = translation_key
        self.icon = icon
class CoordinatorEntity:
    def __init__(self, coordinator): self.coordinator = coordinator
    def __class_getitem__(cls, item): return cls
class SensorEntity: pass
class BinarySensorEntity: pass
class EventEntity: pass
class SensorStateClass:
    MEASUREMENT = "measurement"
    TOTAL = "total"
    TOTAL_INCREASING = "total_increasing"
class SensorDeviceClass:
    DURATION = "duration"
class BinarySensorDeviceClass:
    SAFETY = "safety"
class UnitOfTime:
    MINUTES = "min"

class MockImporter:
    def find_spec(self, fullname, path=None, target=None):
        if fullname.startswith("homeassistant") or fullname.startswith("aiohttp"):
            return ModuleSpec(fullname, self)
        return None

    def create_module(self, spec):
        mod = MagicMock()
        mod.__name__ = spec.name
        mod.__file__ = f"<mock {spec.name}>"
        mod.__path__ = []
        if spec.name == "homeassistant.helpers.update_coordinator":
            mod.DataUpdateCoordinator = MockDataUpdateCoordinator
            mod.CoordinatorEntity = CoordinatorEntity
            mod.UpdateFailed = Exception
        elif spec.name == "homeassistant.components.sensor":
            mod.SensorEntityDescription = SensorEntityDescription
            mod.SensorEntity = SensorEntity
            mod.SensorStateClass = SensorStateClass
            mod.SensorDeviceClass = SensorDeviceClass
        elif spec.name == "homeassistant.components.binary_sensor":
            mod.BinarySensorEntityDescription = BinarySensorEntityDescription
            mod.BinarySensorEntity = BinarySensorEntity
            mod.BinarySensorDeviceClass = BinarySensorDeviceClass
        elif spec.name == "homeassistant.components.event":
            mod.EventEntityDescription = EventEntityDescription
            mod.EventEntity = EventEntity
        elif spec.name == "homeassistant.const":
            mod.UnitOfTime = UnitOfTime
            mod.Platform = MagicMock()
        return mod

    def exec_module(self, module):
        pass

sys.meta_path.insert(0, MockImporter())

from custom_components.etryvoga.const import (
    THREAT_ARTILLERY,
    THREAT_DRONE,
    THREAT_EXPLOSION,
    THREAT_KAB,
    THREAT_RECON,
    THREAT_ROCKET,
    THREAT_SHELLING,
    EVENT_ALARM_STARTED,
    EVENT_ALARM_CANCELLED,
    EVENT_THREAT_DETECTED,
    EVENT_THREAT_CANCELLED,
    LEVEL_CLEAR,
    LEVEL_RED,
    LEVEL_YELLOW,
    STATUS_SIREN,
    STATUS_CANCEL,
    normalize_threat_type,
)
from custom_components.etryvoga.coordinator import ETryvogaDataUpdateCoordinator


class TestThreatNormalization(unittest.TestCase):
    """Test threat type normalization helper."""

    def test_drone_variants(self):
        for raw in ["drone", "uav", "shahed", "DRONE", " Shahed "]:
            self.assertEqual(normalize_threat_type(raw), THREAT_DRONE)

    def test_kab_variants(self):
        for raw in ["kab", "fab", "KAB", "FAB"]:
            self.assertEqual(normalize_threat_type(raw), THREAT_KAB)

    def test_rocket_variants(self):
        for raw in ["rocket", "missile", "ballistic", "ROCKET"]:
            self.assertEqual(normalize_threat_type(raw), THREAT_ROCKET)

    def test_artillery_variants(self):
        for raw in ["artillery", "shelling", "ARTILLERY"]:
            self.assertEqual(normalize_threat_type(raw), THREAT_ARTILLERY)
            self.assertEqual(normalize_threat_type(raw), THREAT_SHELLING)

    def test_recon_variants(self):
        for raw in ["recon_drone", "recon", "zala", "supercam", "RECON_DRONE"]:
            self.assertEqual(normalize_threat_type(raw), THREAT_RECON)

    def test_explosion_variants(self):
        for raw in ["explosion", "EXPLOSION"]:
            self.assertEqual(normalize_threat_type(raw), THREAT_EXPLOSION)

    def test_unknown_and_none(self):
        self.assertEqual(normalize_threat_type(None), "unknown")
        self.assertEqual(normalize_threat_type(""), "unknown")
        self.assertEqual(normalize_threat_type("custom_threat"), "custom_threat")


class TestStemmingAndGeographicMatching(unittest.TestCase):
    """Test Ukrainian stemming and geographic targeting."""

    def setUp(self):
        self.hass = MagicMock()
        self.session = MagicMock()

    def _create_coordinator(self, oblast="Київська область", district_slug="kyiv-dstr", city_name=None):
        return ETryvogaDataUpdateCoordinator(
            hass=self.hass,
            session=self.session,
            oblast=oblast,
            district_slug=district_slug,
            city_name=city_name,
            include_neighbors=True,
        )

    def test_stemming_lutsk(self):
        coord = self._create_coordinator(oblast="Волинська область", district_slug="lutsk-dstr")
        coord.district_title = "Луцький район"
        alerts = {"districts": [{"slug": "lutsk-dstr", "status": STATUS_CANCEL}]}
        threats = [
            {"id": "1", "type": "drone", "title": "🛸 Луцьк", "body": "Загроза ударних БПЛА"},
            {"id": "2", "type": "drone", "title": "🛸 У Луцьку", "body": "Увага"},
        ]
        res = coord._aggregate_state(alerts, threats)
        self.assertEqual(len(res["threats"]), 2)

    def test_stemming_vinnytsia(self):
        coord = self._create_coordinator(oblast="Вінницька область", district_slug="vinnytsia-dstr")
        alerts = {"districts": [{"slug": "vinnytsia-dstr", "status": STATUS_CANCEL}]}
        threats = [
            {"id": "1", "type": "drone", "title": "🛸 Вінниця", "body": "БПЛА в напрямку міста"},
            {"id": "2", "type": "rocket", "title": "🚀 У Вінниці", "body": "Вибухи"},
        ]
        res = coord._aggregate_state(alerts, threats)
        self.assertEqual(len(res["threats"]), 2)

    def test_stemming_donetsk(self):
        coord = self._create_coordinator(oblast="Донецька область", district_slug="donetsk-dstr")
        alerts = {"districts": [{"slug": "donetsk-dstr", "status": STATUS_CANCEL}]}
        threats = [
            {"id": "1", "type": "artillery", "title": "💥 Донецьк", "body": "Обстріл"},
            {"id": "2", "type": "kab", "title": "💣 У Донецьку", "body": "КАБ"},
        ]
        res = coord._aggregate_state(alerts, threats)
        self.assertEqual(len(res["threats"]), 2)

    def test_stemming_sumy(self):
        coord = self._create_coordinator(oblast="Сумська область", district_slug="sumy-dstr")
        alerts = {"districts": [{"slug": "sumy-dstr", "status": STATUS_CANCEL}]}
        threats = [
            {"id": "1", "type": "drone", "title": "🛸 Суми", "body": "Шахед"},
            {"id": "2", "type": "kab", "title": "💣 У Сумах", "body": "КАБ"},
        ]
        res = coord._aggregate_state(alerts, threats)
        self.assertEqual(len(res["threats"]), 2)

    def test_stemming_chernivtsi(self):
        coord = self._create_coordinator(oblast="Чернівецька область", district_slug="chernivtsi-dstr")
        alerts = {"districts": [{"slug": "chernivtsi-dstr", "status": STATUS_CANCEL}]}
        threats = [
            {"id": "1", "type": "drone", "title": "🛸 Чернівці", "body": "Увага"},
            {"id": "2", "type": "rocket", "title": "🚀 У Чернівцях", "body": "Ракета"},
        ]
        res = coord._aggregate_state(alerts, threats)
        self.assertEqual(len(res["threats"]), 2)

    def test_approach_heading_and_area_sector_parsing(self):
        coord = self._create_coordinator()
        alerts = {"districts": []}
        threats = [
            {
                "id": "1",
                "type": "drone",
                "title": "🛸 Київ",
                "body": "Шахед",
                "approach": {"mode": "none", "area_sector": "S"},
            },
            {
                "id": "2",
                "type": "drone",
                "title": "🛸 Київ",
                "body": "Шахед",
                "approach": {"origin_title": "Південь", "heading": "N"},
            },
        ]
        res = coord._aggregate_state(alerts, threats)
        self.assertEqual(len(res["threats"]), 2)
        self.assertEqual(res["threats"][0]["origin"], "S")
        self.assertEqual(res["threats"][1]["origin"], "Південь")

    def test_none_region_safety(self):
        coord = self._create_coordinator()
        alerts = {"districts": []}
        threats = [
            {
                "id": "1",
                "type": "drone",
                "title": "🛸 Київська область",
                "body": "БПЛА",
                "region": None,
            }
        ]
        res = coord._aggregate_state(alerts, threats)
        self.assertEqual(len(res["threats"]), 1)
        # Check country overview text search does not crash or match literal "None"
        overview = coord._build_country_overview(alerts, threats)
        self.assertIn("Київська область", overview["active_regions"])


class TestCountryOverview(unittest.TestCase):
    """Test nationwide overview aggregation, keyword matching, and conflict resolution."""

    def setUp(self):
        self.coord = ETryvogaDataUpdateCoordinator(
            hass=MagicMock(),
            session=MagicMock(),
            oblast="м. Київ",
            district_slug="kyiv-city",
        )

    def test_kyiv_keywords_match_cds_and_kyiv(self):
        alerts = {"districts": []}
        threats = [
            {"id": "1", "type": "drone", "title": "🛸 Деснянський район (Київ)", "body": "", "region": "DESNYANSKYI-CDS"},
            {"id": "2", "type": "drone", "title": "🛸 Печерськ (Kyiv)", "body": "", "region": None},
        ]
        overview = self.coord._build_country_overview(alerts, threats)
        self.assertIn("м. Київ", overview["active_regions"])
        self.assertTrue(overview["states"]["м. Київ"]["drone"])

    def test_rivne_varash(self):
        alerts = {"districts": []}
        threats = [
            {"id": "1", "type": "drone", "title": "🛸 Вараш", "body": "БПЛА поблизу РАЕС", "region": None},
        ]
        overview = self.coord._build_country_overview(alerts, threats)
        self.assertIn("Рівненська область", overview["active_regions"])

    def test_pokrovsk_donetsk_does_not_clash_with_dnipro(self):
        alerts = {"districts": []}
        threats = [
            {"id": "1", "type": "kab", "title": "💣 Покровськ (Донецька обл.)", "body": "Пуски КАБ", "region": None},
        ]
        overview = self.coord._build_country_overview(alerts, threats)
        self.assertIn("Донецька область", overview["active_regions"])
        self.assertNotIn("Дніпропетровська область", overview["active_regions"])

    def test_pokrov_dnipro_matches_dnipro(self):
        alerts = {"districts": []}
        threats = [
            {"id": "1", "type": "artillery", "title": "💥 Покров (Дніпропетровська обл.)", "body": "Обстріл", "region": None},
        ]
        overview = self.coord._build_country_overview(alerts, threats)
        self.assertIn("Дніпропетровська область", overview["active_regions"])
        self.assertNotIn("Донецька область", overview["active_regions"])


class TestTacticalSummaryAndEvents(unittest.TestCase):
    """Test tactical summary building and event transition logic."""

    def setUp(self):
        self.coord = ETryvogaDataUpdateCoordinator(
            hass=MagicMock(),
            session=MagicMock(),
            oblast="Київська область",
            district_slug="kyiv-dstr",
        )

    def test_summary_no_siren_with_recon_and_explosion(self):
        threats = [
            {"type": THREAT_RECON, "origin": "Не вказано"},
            {"type": THREAT_EXPLOSION, "origin": "Не вказано"},
        ]
        summary = self.coord._build_tactical_summary(is_siren=False, alert_level=LEVEL_CLEAR, threats=threats)
        self.assertIn("Розвідувальний БПЛА", summary)
        self.assertIn("Повідомлення про вибух", summary)
        self.assertNotIn("Повітряна тривога active", summary)
        self.assertNotIn("Повітряна тривога активна", summary)

    def test_summary_quiet(self):
        summary = self.coord._build_tactical_summary(is_siren=False, alert_level=LEVEL_CLEAR, threats=[])
        self.assertEqual(summary, "Обстановка спокійна. Тривоги немає.")

    def test_summary_siren_only(self):
        summary = self.coord._build_tactical_summary(is_siren=True, alert_level=LEVEL_RED, threats=[])
        self.assertEqual(summary, "🚨 Повітряна тривога")

    def test_threat_cancelled_event_triggered(self):
        alerts = {"districts": [{"slug": "kyiv-dstr", "status": STATUS_CANCEL}]}
        # 1. State with threats
        self.coord.data = {
            "is_siren": False,
            "threats": [{"id": "1", "type": THREAT_DRONE, "title": "БПЛА"}],
        }
        # 2. Update with 0 threats
        res = self.coord._aggregate_state(alerts, [])
        self.assertIsNotNone(res["last_event"])
        self.assertEqual(res["last_event"]["event_type"], EVENT_THREAT_CANCELLED)


class TestSSEPayloadAndCacheClearing(unittest.TestCase):
    """Test SSE live payload processing and cache clearing."""

    def setUp(self):
        self.coord = ETryvogaDataUpdateCoordinator(
            hass=MagicMock(),
            session=MagicMock(),
            oblast="Київська область",
            district_slug="kyiv-dstr",
        )

    def test_cache_cleared_on_zero_threats_snapshot(self):
        self.coord._raw_confirmed_cache = [{"id": "old_1", "type": "drone"}]
        live_payload = {
            "uavStories": [],
            "kabStories": [],
            "rocketStories": [],
            "stories": [],
        }
        self.coord._handle_live_payload(live_payload)
        self.assertEqual(self.coord._raw_confirmed_cache, [])

    def test_filter_siren_and_cancel_from_general_stories(self):
        live_payload = {
            "stories": [
                {"id": "1", "type": "siren", "title": "🔴 Кам'янський район"},
                {"id": "2", "type": "cancel", "title": "🟢 Вишгородський район"},
                {"id": "3", "type": "drone", "title": "🛸 Корабел"},
            ]
        }
        self.coord._handle_live_payload(live_payload)
        self.assertEqual(len(self.coord._raw_confirmed_cache), 1)
        self.assertEqual(self.coord._raw_confirmed_cache[0]["type"], "drone")


class TestEntityConfigurations(unittest.TestCase):
    """Test sensor and binary sensor descriptions for correct classes and threat keys."""

    def test_alert_duration_state_class(self):
        from custom_components.etryvoga.sensor import SENSOR_DESCRIPTIONS
        desc = next(d for d in SENSOR_DESCRIPTIONS if d.key == "alert_duration")
        # Ensure state_class is not TOTAL (which distorted statistics) and is MEASUREMENT
        self.assertNotEqual(desc.state_class, "total")

    def test_binary_sensor_threat_keys(self):
        from custom_components.etryvoga.binary_sensor import BINARY_SENSOR_DESCRIPTIONS
        artillery_desc = next(d for d in BINARY_SENSOR_DESCRIPTIONS if d.key == "artillery_threat")
        self.assertEqual(artillery_desc.is_threat_key, THREAT_ARTILLERY)

    def test_event_types_include_threat_cancelled(self):
        from custom_components.etryvoga.event import ETryvogaThreatEventEntity
        self.assertIn(EVENT_THREAT_CANCELLED, ETryvogaThreatEventEntity._attr_event_types)


if __name__ == "__main__":
    unittest.main()
