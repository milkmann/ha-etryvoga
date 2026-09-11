"""Event entity for eTryvoga integration."""
from __future__ import annotations

from typing import Any

from homeassistant.components.event import EventEntity, EventEntityDescription
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import ETryvogaConfigEntry
from .const import (
    ATTRIBUTION,
    DOMAIN,
    EVENT_ALARM_CANCELLED,
    EVENT_ALARM_STARTED,
    EVENT_THREAT_CANCELLED,
    EVENT_THREAT_DETECTED,
    MANUFACTURER,
)
from .coordinator import ETryvogaDataUpdateCoordinator


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ETryvogaConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up event entity for eTryvoga."""
    coordinator = entry.runtime_data
    async_add_entities([ETryvogaThreatEventEntity(coordinator, entry)])


class ETryvogaThreatEventEntity(CoordinatorEntity[ETryvogaDataUpdateCoordinator], EventEntity):
    """Representation of an eTryvoga tactical event entity."""

    _attr_has_entity_name = True
    _attr_attribution = ATTRIBUTION
    _attr_event_types = [
        EVENT_ALARM_STARTED,
        EVENT_ALARM_CANCELLED,
        EVENT_THREAT_DETECTED,
        EVENT_THREAT_CANCELLED,
    ]

    def __init__(
        self,
        coordinator: ETryvogaDataUpdateCoordinator,
        entry: ETryvogaConfigEntry,
    ) -> None:
        """Initialize the event entity."""
        super().__init__(coordinator)
        self.entity_description = EventEntityDescription(
            key="threat_event",
            translation_key="threat_event",
            icon="mdi:bell-badge-outline",
        )
        self._attr_unique_id = f"{entry.unique_id}_threat_event".lower()
        self._attr_device_info = DeviceInfo(
            entry_type=DeviceEntryType.SERVICE,
            identifiers={(DOMAIN, entry.entry_id)},
            manufacturer=MANUFACTURER,
            name=entry.title,
            configuration_url="https://map.etryvoga.com",
        )
        self._last_processed_event_ts: str | None = None
        self._processed_events: set[tuple[str, str]] = set()

    def _handle_coordinator_update(self) -> None:
        """Handle coordinator update and fire event if a new transition occurred."""
        data = self.coordinator.data or {}
        events = data.get("last_events")
        if events is None:
            single = data.get("last_event")
            events = [single] if single else []

        for event_info in events:
            if not isinstance(event_info, dict):
                continue
            event_type = event_info.get("event_type")
            ts = event_info.get("ts", "")
            event_key = (event_type, ts)
            if event_key not in self._processed_events:
                payload = event_info.get("payload", {})
                if event_type in self._attr_event_types:
                    self._trigger_event(event_type, payload)
                    self._processed_events.add(event_key)
                    self._last_processed_event_ts = event_info

        if len(self._processed_events) > 50:
            self._processed_events = set(list(self._processed_events)[-25:])

        self.async_write_ha_state()
