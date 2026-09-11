"""The eTryvoga integration."""
from __future__ import annotations

import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import (
    CONF_CITY_NAME,
    CONF_DISTRICT_SLUG,
    CONF_INCLUDE_NEIGHBORS,
    CONF_OBLAST,
    DOMAIN,
)
from .coordinator import ETryvogaDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [
    Platform.BINARY_SENSOR,
    Platform.SENSOR,
    Platform.EVENT,
]

type ETryvogaConfigEntry = ConfigEntry[ETryvogaDataUpdateCoordinator]


async def async_setup_entry(hass: HomeAssistant, entry: ETryvogaConfigEntry) -> bool:
    """Set up eTryvoga from a config entry."""
    session = async_get_clientsession(hass)
    oblast = entry.data[CONF_OBLAST]
    district_slug = entry.data[CONF_DISTRICT_SLUG]
    city_name = entry.data.get(CONF_CITY_NAME)
    include_neighbors = entry.options.get(
        CONF_INCLUDE_NEIGHBORS, entry.data.get(CONF_INCLUDE_NEIGHBORS, True)
    )

    coordinator = ETryvogaDataUpdateCoordinator(
        hass=hass,
        session=session,
        oblast=oblast,
        district_slug=district_slug,
        city_name=city_name,
        include_neighbors=include_neighbors,
    )

    await coordinator.async_config_entry_first_refresh()
    entry.runtime_data = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    entry.async_on_unload(entry.add_update_listener(async_reload_entry))

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ETryvogaConfigEntry) -> bool:
    """Unload a config entry."""
    coordinator = entry.runtime_data
    await coordinator.async_close()

    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)


async def async_reload_entry(hass: HomeAssistant, entry: ETryvogaConfigEntry) -> None:
    """Reload config entry when options change."""
    await hass.config_entries.async_reload(entry.entry_id)
