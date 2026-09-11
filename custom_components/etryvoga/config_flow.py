"""Config flow for eTryvoga integration."""
from __future__ import annotations

import logging
from typing import Any
import voluptuous as vol

from homeassistant.config_entries import (
    ConfigEntry,
    ConfigFlow,
    ConfigFlowResult,
    OptionsFlow,
)
from homeassistant.core import callback

from .const import (
    CONF_CITY_NAME,
    CONF_DISTRICT_SLUG,
    CONF_INCLUDE_NEIGHBORS,
    CONF_OBLAST,
    DOMAIN,
)
from .geo_data import (
    CITY_POINTS,
    DISTRICTS_BY_SLUG,
    DISTRICT_TO_CITIES,
    OBLAST_REGIONS,
    OBLAST_TO_DISTRICTS,
)

_LOGGER = logging.getLogger(__name__)


class ETryvogaConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for eTryvoga."""

    VERSION = 1

    def __init__(self) -> None:
        """Initialize the flow."""
        self.selected_oblast: str | None = None
        self.selected_district_slug: str | None = None
        self.selected_district_title: str | None = None

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Step 1: Choose Oblast."""
        if user_input is not None:
            self.selected_oblast = user_input[CONF_OBLAST]
            return await self.async_step_district()

        schema = vol.Schema({
            vol.Required(CONF_OBLAST): vol.In(OBLAST_REGIONS),
        })

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
        )

    async def async_step_district(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Step 2: Choose District within selected Oblast."""
        district_slugs = OBLAST_TO_DISTRICTS.get(self.selected_oblast, [])
        district_options = {
            slug: DISTRICTS_BY_SLUG.get(slug, {}).get("title", slug)
            for slug in district_slugs
        }

        # If oblast has only 1 district (e.g. Kyiv city)
        if len(district_options) == 1:
            slug = list(district_options.keys())[0]
            self.selected_district_slug = slug
            self.selected_district_title = district_options[slug]
            return await self.async_step_city()

        if user_input is not None:
            self.selected_district_slug = user_input[CONF_DISTRICT_SLUG]
            self.selected_district_title = district_options.get(
                self.selected_district_slug, self.selected_district_slug
            )
            return await self.async_step_city()

        schema = vol.Schema({
            vol.Required(CONF_DISTRICT_SLUG): vol.In(district_options),
        })

        return self.async_show_form(
            step_id="district",
            data_schema=schema,
        )

    async def async_step_city(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Step 3: Choose specific city/settlement or entire district."""
        district_info = DISTRICTS_BY_SLUG.get(self.selected_district_slug, {})
        is_city_entry = district_info.get("isCity", False)
        raw_title = district_info.get("rawTitle", self.selected_district_title)

        cities_options: dict[str, str] = {}
        if is_city_entry:
            cities_options["_ALL_"] = f"{raw_title} (все місто)"
        else:
            cities_options["_ALL_"] = "Весь район цілком (всі населені пункти)"

        # Populate available cities in this district
        district_cities = DISTRICT_TO_CITIES.get(self.selected_district_slug, [])
        for c in district_cities:
            cities_options[c] = c

        if user_input is not None:
            chosen_city = user_input.get(CONF_CITY_NAME)
            city_name = None if chosen_city == "_ALL_" else chosen_city

            if is_city_entry and city_name is None:
                city_name = raw_title

            # Ensure unique entry
            unique_id = f"{self.selected_district_slug}_{city_name or 'district'}"
            await self.async_set_unique_id(unique_id)
            self._abort_if_unique_id_configured()

            if is_city_entry:
                title = raw_title if raw_title.startswith("м. ") else f"м. {raw_title}"
            else:
                title = f"{self.selected_district_title}"
                if city_name:
                    title += f" ({city_name})"

            return self.async_create_entry(
                title=title,
                data={
                    CONF_OBLAST: self.selected_oblast,
                    CONF_DISTRICT_SLUG: self.selected_district_slug,
                    CONF_CITY_NAME: city_name,
                    CONF_INCLUDE_NEIGHBORS: user_input.get(CONF_INCLUDE_NEIGHBORS, True),
                },
            )

        schema = vol.Schema({
            vol.Required(CONF_CITY_NAME, default="_ALL_"): vol.In(cities_options),
            vol.Optional(CONF_INCLUDE_NEIGHBORS, default=True): bool,
        })

        return self.async_show_form(
            step_id="city",
            data_schema=schema,
        )

    async def async_step_reconfigure(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle reconfiguration."""
        entry = self._get_reconfigure_entry()
        self.selected_oblast = entry.data.get(CONF_OBLAST)
        return await self.async_step_district()

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow:
        """Get the options flow for this handler."""
        return ETryvogaOptionsFlow(config_entry)


class ETryvogaOptionsFlow(OptionsFlow):
    """Handle options for eTryvoga."""

    def __init__(self, config_entry: ConfigEntry) -> None:
        """Initialize."""
        self.config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        schema = vol.Schema({
            vol.Optional(
                CONF_INCLUDE_NEIGHBORS,
                default=self.config_entry.options.get(
                    CONF_INCLUDE_NEIGHBORS,
                    self.config_entry.data.get(CONF_INCLUDE_NEIGHBORS, True),
                ),
            ): bool,
        })

        return self.async_show_form(step_id="init", data_schema=schema)
