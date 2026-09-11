"""Binary sensors for eTryvoga integration."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import ETryvogaConfigEntry
from .const import (
    ATTRIBUTION,
    DOMAIN,
    MANUFACTURER,
    THREAT_DRONE,
    THREAT_EXPLOSION,
    THREAT_KAB,
    THREAT_RECON,
    THREAT_ROCKET,
    THREAT_SHELLING,
)
from .coordinator import ETryvogaDataUpdateCoordinator


@dataclass(frozen=True, kw_only=True)
class ETryvogaBinarySensorDescription(BinarySensorEntityDescription):
    """Class describing eTryvoga binary sensor entities."""

    is_threat_key: str | None = None


BINARY_SENSOR_DESCRIPTIONS: tuple[ETryvogaBinarySensorDescription, ...] = (
    ETryvogaBinarySensorDescription(
        key="air_alert",
        translation_key="air_alert",
        device_class=BinarySensorDeviceClass.SAFETY,
        icon="mdi:shield-alert",
    ),
    ETryvogaBinarySensorDescription(
        key="kab_threat",
        translation_key="kab_threat",
        device_class=BinarySensorDeviceClass.SAFETY,
        icon="mdi:bomb",
        is_threat_key=THREAT_KAB,
    ),
    ETryvogaBinarySensorDescription(
        key="drone_threat",
        translation_key="drone_threat",
        device_class=BinarySensorDeviceClass.SAFETY,
        icon="mdi:drone",
        is_threat_key=THREAT_DRONE,
    ),
    ETryvogaBinarySensorDescription(
        key="missile_threat",
        translation_key="missile_threat",
        device_class=BinarySensorDeviceClass.SAFETY,
        icon="mdi:rocket",
        is_threat_key=THREAT_ROCKET,
    ),
    ETryvogaBinarySensorDescription(
        key="artillery_threat",
        translation_key="artillery_threat",
        device_class=BinarySensorDeviceClass.SAFETY,
        icon="mdi:tank",
        is_threat_key=THREAT_SHELLING,
    ),
    ETryvogaBinarySensorDescription(
        key="recon_threat",
        translation_key="recon_threat",
        device_class=BinarySensorDeviceClass.SAFETY,
        icon="mdi:eye-outline",
        is_threat_key=THREAT_RECON,
    ),
    ETryvogaBinarySensorDescription(
        key="explosion_threat",
        translation_key="explosion_threat",
        device_class=BinarySensorDeviceClass.SAFETY,
        icon="mdi:fire-alert",
        is_threat_key=THREAT_EXPLOSION,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ETryvogaConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up binary sensors for eTryvoga."""
    coordinator = entry.runtime_data

    async_add_entities(
        ETryvogaBinarySensor(
            coordinator=coordinator,
            description=description,
            entry=entry,
        )
        for description in BINARY_SENSOR_DESCRIPTIONS
    )


class ETryvogaBinarySensor(CoordinatorEntity[ETryvogaDataUpdateCoordinator], BinarySensorEntity):
    """Representation of an eTryvoga binary sensor."""

    entity_description: ETryvogaBinarySensorDescription
    _attr_has_entity_name = True
    _attr_attribution = ATTRIBUTION

    def __init__(
        self,
        coordinator: ETryvogaDataUpdateCoordinator,
        description: ETryvogaBinarySensorDescription,
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
    def is_on(self) -> bool:
        """Return true if the binary sensor is on."""
        data = self.coordinator.data or {}
        if self.entity_description.key == "air_alert":
            return bool(data.get("is_siren", False))

        threat_key = self.entity_description.is_threat_key
        if threat_key:
            return bool(data.get("threat_flags", {}).get(threat_key, False))

        return False

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return state attributes."""
        data = self.coordinator.data or {}
        attrs: dict[str, Any] = {
            "region": self.coordinator.district_title,
            "oblast": self.coordinator.oblast,
        }

        if self.entity_description.key == "air_alert":
            attrs.update({
                "alert_level": data.get("alert_level"),
                "status_at": data.get("status_at"),
                "duration_minutes": data.get("duration_minutes", 0),
            })
        else:
            threat_key = self.entity_description.is_threat_key
            matching_threats = [
                t for t in data.get("threats", [])
                if t.get("type") == threat_key
            ]
            attrs["active_count"] = len(matching_threats)
            if matching_threats:
                attrs["events"] = matching_threats
                attrs["origins"] = list(set(t.get("origin") for t in matching_threats if t.get("origin")))

        return attrs
