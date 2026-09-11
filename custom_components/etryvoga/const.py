"""Constants for the eTryvoga integration."""
from datetime import timedelta
import logging

DOMAIN = "etryvoga"
MANUFACTURER = "єТривога (eTryvoga)"
ATTRIBUTION = "Дані надано волонтерським проектом єТривога (map.etryvoga.com)"

_LOGGER = logging.getLogger(__package__)

# API Endpoints
API_BASE_URL = "https://map.etryvoga.com"
API_ALERTS_URL = f"{API_BASE_URL}/api/map/alerts"
API_CONFIRMED_URL = f"{API_BASE_URL}/api/map/confirmed"
API_NOTIFICATIONS_URL = f"{API_BASE_URL}/api/map/notifications"
API_LIVE_SSE_URL = f"{API_BASE_URL}/api/map/live"

# Headers
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HomeAssistant-eTryvoga/0.1.3"

# Timing
DEFAULT_SCAN_INTERVAL = timedelta(minutes=5)
SSE_RECONNECT_INITIAL_BACKOFF = 2
SSE_RECONNECT_MAX_BACKOFF = 60

# Configuration Keys
CONF_OBLAST = "oblast"
CONF_DISTRICT = "district"
CONF_DISTRICT_SLUG = "district_slug"
CONF_CITY = "city"
CONF_CITY_NAME = "city_name"
CONF_INCLUDE_NEIGHBORS = "include_neighbors"

# Alert Statuses and Levels
STATUS_SIREN = "siren"
STATUS_CANCEL = "cancel"

LEVEL_CLEAR = "clear"
LEVEL_YELLOW = "yellow"
LEVEL_RED = "red"

LEVEL_COLORS = {
    LEVEL_CLEAR: "#10B981",   # Зелений
    LEVEL_YELLOW: "#EAB308",  # Жовтий (БПЛА)
    LEVEL_RED: "#DC2626",     # Червоний (Ракети / КАБ / Сирена)
}

# Threat Types
THREAT_KAB = "kab"
THREAT_DRONE = "drone"
THREAT_ROCKET = "rocket"
THREAT_SHELLING = "shelling"
THREAT_RECON = "recon_drone"
THREAT_EXPLOSION = "explosion"

# Event Types for HA EventEntity
EVENT_ALARM_STARTED = "alarm_started"
EVENT_ALARM_CANCELLED = "alarm_cancelled"
EVENT_THREAT_DETECTED = "threat_detected"
EVENT_THREAT_CANCELLED = "threat_cancelled"
