"""Sensors for eTryvoga integration."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import UnitOfTime
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import ETryvogaConfigEntry
from .const import (
    ATTRIBUTION,
    DOMAIN,
    LEVEL_CLEAR,
    LEVEL_COLORS,
    MANUFACTURER,
)
from .coordinator import ETryvogaDataUpdateCoordinator


import logging

_LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True, kw_only=True)
class ETryvogaSensorDescription(SensorEntityDescription):
    """Class describing eTryvoga sensor entities."""

    value_key: str


SENSOR_DESCRIPTIONS: tuple[ETryvogaSensorDescription, ...] = (
    ETryvogaSensorDescription(
        key="alert_level",
        translation_key="alert_level",
        icon="mdi:alert-decagram",
        value_key="alert_level",
    ),
    ETryvogaSensorDescription(
        key="tactical_summary",
        translation_key="tactical_summary",
        icon="mdi:information-outline",
        value_key="tactical_summary",
    ),
    ETryvogaSensorDescription(
        key="alert_duration",
        translation_key="alert_duration",
        icon="mdi:timer-outline",
        device_class=SensorDeviceClass.DURATION,
        native_unit_of_measurement=UnitOfTime.MINUTES,
        state_class=SensorStateClass.MEASUREMENT,
        value_key="duration_minutes",
    ),
    ETryvogaSensorDescription(
        key="active_threats_count",
        translation_key="active_threats_count",
        icon="mdi:counter",
        state_class=SensorStateClass.MEASUREMENT,
        value_key="active_threats_count",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ETryvogaConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up sensors for eTryvoga."""
    coordinator = entry.runtime_data

    entities: list[SensorEntity] = [
        ETryvogaSensor(
            coordinator=coordinator,
            description=description,
            entry=entry,
        )
        for description in SENSOR_DESCRIPTIONS
    ]
    try:
        overview_sensor = ETryvogaUkraineOverviewSensor(coordinator, entry)
        entities.append(overview_sensor)
        _LOGGER.debug(
            "ETRYVOGA SENSOR SETUP: Added %d entities, overview entity unique_id: %s",
            len(entities),
            overview_sensor.unique_id,
        )
    except Exception as err:
        _LOGGER.exception("ETRYVOGA SENSOR SETUP ERROR creating overview sensor: %s", err)

    async_add_entities(entities)


class ETryvogaSensor(CoordinatorEntity[ETryvogaDataUpdateCoordinator], SensorEntity):
    """Representation of an eTryvoga local city/district sensor."""

    entity_description: ETryvogaSensorDescription
    _attr_has_entity_name = True
    _attr_attribution = ATTRIBUTION

    def __init__(
        self,
        coordinator: ETryvogaDataUpdateCoordinator,
        description: ETryvogaSensorDescription,
        entry: ETryvogaConfigEntry,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{entry.unique_id}_{description.key}".lower()
        self._attr_device_info = DeviceInfo(
            entry_type=DeviceEntryType.SERVICE,
            identifiers={(DOMAIN, entry.entry_id)},
            manufacturer=MANUFACTURER,
            name=entry.title,
            configuration_url="https://map.etryvoga.com",
        )

    @property
    def native_value(self) -> Any:
        """Return the state of the sensor."""
        data = self.coordinator.data or {}
        key = self.entity_description.value_key

        if key == "active_threats_count":
            return len(data.get("threats", []))

        return data.get(key)

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return state attributes."""
        data = self.coordinator.data or {}
        attrs: dict[str, Any] = {
            "region": self.coordinator.district_title,
            "oblast": self.coordinator.oblast,
        }

        if self.entity_description.key == "alert_level":
            level = data.get("alert_level", LEVEL_CLEAR)
            attrs["color"] = LEVEL_COLORS.get(level, "#10B981")
            attrs["is_siren"] = data.get("is_siren", False)

        elif self.entity_description.key == "active_threats_count":
            attrs["threats"] = data.get("threats", [])

        return attrs


class ETryvogaUkraineOverviewSensor(CoordinatorEntity[ETryvogaDataUpdateCoordinator], SensorEntity):
    """Nationwide tactical overview sensor for LED matrices (AWTRIX) and maps."""

    _attr_has_entity_name = True
    _attr_translation_key = "ukraine_overview"
    _attr_attribution = ATTRIBUTION
    _attr_icon = "mdi:map-legend"
    _attr_entity_registry_enabled_default = False

    def __init__(
        self,
        coordinator: ETryvogaDataUpdateCoordinator,
        entry: ETryvogaConfigEntry,
    ) -> None:
        """Initialize the nationwide overview sensor."""
        super().__init__(coordinator)
        self.entity_description = SensorEntityDescription(
            key="ukraine_overview",
            translation_key="ukraine_overview",
            icon="mdi:map-legend",
            entity_registry_enabled_default=False,
        )
        self._attr_unique_id = f"{entry.unique_id}_ukraine_overview".lower()
        self._attr_device_info = DeviceInfo(
            entry_type=DeviceEntryType.SERVICE,
            identifiers={(DOMAIN, entry.entry_id)},
            manufacturer=MANUFACTURER,
            name=entry.title,
            configuration_url="https://map.etryvoga.com",
        )

    @property
    def suggested_object_id(self) -> str | None:
        """Return clean entity ID object name."""
        return "etryvoga_ukraine_overview"

    @property
    def native_value(self) -> Any:
        """Return the nationwide summary state."""
        data = self.coordinator.data or {}
        return data.get("country_overview_summary", "Спокійно")

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return nationwide tactical attributes."""
        data = self.coordinator.data or {}
        country = data.get("country_overview") or {}
        return {
            "states": country.get("states", {}),
            "active_regions": country.get("active_regions", []),
            "threat_flags": country.get("threat_flags", {}),
            "regions_status": country.get("regions_status", {}),
            "oblasts": country.get("oblasts", {}),
            "districts": country.get("districts", {}),
            "tactical_threats": country.get("tactical_threats", []),
            "counts": country.get("counts", {}),
        }

