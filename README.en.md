# eTryvoga (єТривога) — Home Assistant Integration

<p align="center">
  <img src="https://raw.githubusercontent.com/milkmann/ha-etryvoga/main/icon.png" width="128" height="128" alt="eTryvoga Logo" />
</p>

<p align="center">
  <b>Modern, real-time, high-precision air raid alert and tactical threat monitoring system (KAB, UAVs, Missiles) for Home Assistant, powered by the <a href="https://map.etryvoga.com">eTryvoga</a> project.</b>
</p>

<p align="center">
  <a href="README.md">🇺🇦 Українська</a> &nbsp;|&nbsp; <b>🇬🇧 English</b>
</p>

<p align="center">
  <a href="https://github.com/hacs/default"><img src="https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge" alt="HACS Custom" /></a>
  <a href="https://github.com/milkmann/ha-etryvoga/releases"><img src="https://img.shields.io/github/v/release/milkmann/ha-etryvoga?style=for-the-badge&color=blue" alt="Latest Release" /></a>
  <a href="https://github.com/home-assistant/core"><img src="https://img.shields.io/badge/Home%20Assistant-2024.1%2B-blue?style=for-the-badge&logo=home-assistant" alt="Home Assistant" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/milkmann/ha-etryvoga?style=for-the-badge" alt="License" /></a>
</p>

---

## 🚀 Why This Integration?

The built-in `ukraine_alarm` core integration only provides basic on/off siren state at the district level. **eTryvoga elevates home safety and tactical awareness to an entirely new level:**

- ⚡ **Instant Real-Time Push (SSE):** Connected via a persistent stream to `api/map/live`. Events arrive with sub-second latency (< 1 sec) without polling or straining servers.
- 🎯 **Tactical Threat Intelligence:** Know not only that a siren is sounding, but **what is approaching, flight vectors, and target directions** (e.g., *“💣 Guided bomb (KAB) launched from south-east”*, *“🛸 UAV heading toward city suburbs”*, *“🚀 Ballistic missile warning for sector”*).
- 🟡 **Threat Severity Levels:** Distinguishes between **yellow** (drone/UAV activity) and **red** (missiles, KABs, general sirens) threat levels.
- 🏢 **Intuitive 3-Tier Setup Wizard (UI):** Choose your Region (Oblast) ➔ District / City ➔ Community / Town.
- ⚡ **Home Assistant Event Entity:** Modern discrete events (`alarm_started`, `alarm_cancelled`, `threat_detected`) for easy and robust automation triggers without template parsing.
- 📦 **Ready-to-use Blueprints:** Out-of-the-box templates for Telegram notifications, smart RGB light sirens, and voice warnings (TTS).

---

## 📊 Entities Created in Home Assistant

After adding your location, a virtual device **«eTryvoga: <Your District/City>»** is created with a complete set of sensors:

### 🔴 Binary Sensors (`binary_sensor`) — `BinarySensorDeviceClass.SAFETY`

All threat binary sensors use the `safety` device class, displaying **Safe** (`off`) when clear and **Unsafe** (`on`) during an alert:

| Entity | Name | Device Class | Description & Attributes |
| :--- | :--- | :--- | :--- |
| `binary_sensor.<id>_air_alert` | **Air Alert** | `safety` | `on` (Unsafe) during an active siren, `off` (Safe). Attributes: `alert_level` (yellow/red), `duration_minutes`. |
| `binary_sensor.<id>_kab_threat` | **KAB Threat** | `safety` | `on` (Unsafe) when guided aerial bombs are detected. Attributes: `origins` (launch direction), `events`. |
| `binary_sensor.<id>_drone_threat` | **Drone Threat** | `safety` | `on` (Unsafe) when attack UAVs (Shahed/Geran) are tracked in the sector. |
| `binary_sensor.<id>_missile_threat` | **Missile Threat** | `safety` | `on` (Unsafe) during cruise or ballistic missile dangers. |
| `binary_sensor.<id>_artillery_threat` | **Artillery Shelling** | `safety` | `on` (Unsafe) for frontline and border areas subject to artillery fire. |
| `binary_sensor.<id>_recon_threat` | **Recon Drone** | `safety` | `on` (Unsafe) during reconnaissance UAV activity (Zala, Supercam, Orlan). |
| `binary_sensor.<id>_explosion_threat` | **Explosion Reported** | `safety` | `on` (Unsafe) when verified explosion reports / air defense activity occur. |

### 🟡 State Sensors (`sensor`)

| Entity | Name | State | Description & Usage |
| :--- | :--- | :--- | :--- |
| `sensor.<id>_alert_level` | **Alert Level** | `clear` / `yellow` / `red` | Perfect for smart lighting automations. Attributes include exact hex colors: `#10B981`, `#EAB308`, `#DC2626`. |
| `sensor.<id>_tactical_summary` | **Tactical Summary** | Text | Structured human-readable threat summary suitable for dashboards or Text-to-Speech (TTS). |
| `sensor.<id>_alert_duration` | **Alert Duration** | Number (minutes) | Elapsed duration of the current active alert. |
| `sensor.<id>_active_threats_count` | **Active Threats Count** | Number | Total count of active tactical threats in your monitored area. |
| `sensor.<id>_ukraine_overview` | **All Ukraine (Threat Map)** | Text | *Disabled by default.* Comprehensive real-time breakdown of all oblasts (`states`, `regions_status`), 16-bit integer threat bitmasks for microcontrollers (`threat_flags`), all 144 districts (`districts`), and airborne targets (`tactical_threats`) across Ukraine for AWTRIX displays, ESP32, and maps. |

### ⚡ Event Entity (`event`)

* `event.<id>_threat_event` — fires discrete event states:
  * `alarm_started` — alert started (provides level, timestamp, summary);
  * `alarm_cancelled` — all-clear / alert ended (provides duration in minutes);
  * `threat_detected` — new specific threat detected (provides threat type, direction, origin);
  * `threat_cancelled` — tactical threat cleared.

### 🗺️ AWTRIX / Ulanzi TC001 & Map Cards Usage
The `sensor.<id>_ukraine_overview` sensor is specifically designed for rendering live Ukraine alert maps (such as on AWTRIX Light LED matrix clocks or SVG dashboard maps):
* **How to enable:** Go to *Settings* ➔ *Devices & Services* ➔ *eTryvoga* ➔ click on the disabled *«All Ukraine (Threat Map)»* sensor ➔ toggle *«Enable»*.
* **Database Optimization (RAM-only):** We strongly recommend adding this entity to your `recorder.exclude` in `configuration.yaml` so frequent nationwide updates stay in memory without bloating your database:
  ```yaml
  recorder:
    exclude:
      entity_globs:
        - sensor.*_ukraine_overview*
  ```
* **Jinja2 Template Examples for AWTRIX / ESPHome:**
  ```jinja2
  {# 1. Check alert status for an oblast (compatible with LED map mappings) #}
  {{ state_attr('sensor.etryvoga_ukraine_overview', 'states')['Запорізька область'].enabled }}

  {# 2. Check for guided bomb (KAB) danger #}
  {{ state_attr('sensor.etryvoga_ukraine_overview', 'states')['Запорізька область'].kab }}

  {# 3. Get ready-to-use LED color ('red', 'yellow', or 'clear') #}
  {{ state_attr('sensor.etryvoga_ukraine_overview', 'states')['Запорізька область'].color }}

  {# 4. Numeric threat bitmask for ESP32 / ESPHome #}
  {{ state_attr('sensor.etryvoga_ukraine_overview', 'threat_flags')['Запорізька область'] }}
  ```

---

## 🛠️ Installation via HACS

### Step 1. Add Repository to HACS
1. Open Home Assistant ➔ navigate to **HACS**.
2. Click the top-right menu (three dots) ➔ **Custom repositories**.
3. Enter the repository URL:
   ```text
   https://github.com/milkmann/ha-etryvoga
   ```
4. Select **Integration** under Category.
5. Click **Add**.

### Step 2. Download & Configure
1. Search for **eTryvoga (єТривога)** in HACS and click **Download**.
2. Restart Home Assistant.
3. Go to **Settings** ➔ **Devices & Services** ➔ **Add Integration**.
4. Search for **eTryvoga (єТривога)**:
   * **Step 1 (Region / Oblast):** Select your Oblast (all 26 regions of Ukraine supported).
   * **Step 2 (Monitoring Level):** Choose your target:
     - *«{Oblast} (entire region)»* — general regional monitoring;
     - *«City of {City} (city)»* — direct selection of major cities (Kyiv, Kharkiv, Odesa, Dnipro, Zaporizhzhia, Lviv, etc.);
     - *Territorial District* of the region.
   * **Step 3 (Community / Settlement):** If a district was selected, you can monitor the entire district or choose a specific town/community for pinpoint threat tracking.
   * Toggle *«Include threats within the region»* if you want notifications when missiles or UAVs travel through neighboring districts toward yours.

---

## 💡 Ready-to-Use Blueprints

The integration includes pre-built automation blueprints (`blueprints/automation/etryvoga/`):

1. **Telegram Notifications (`telegram_alerts.yaml`):**
   * Instant alert message with location and threat details.
   * Real-time tactical updates when KABs or UAVs change course.
   * All-clear notification with total alert duration.
2. **RGB Smart Light Alert (`rgb_lights_alert.yaml`):**
   * Turns **Yellow** on UAV / drone threats.
   * Pulses **Red** on high-risk missile or KAB threats.
   * Illuminates **Green** for 15 seconds on all-clear, then restores previous state.
3. **Voice TTS Siren (`voice_warning_tts.yaml`):**
   * Speaks voice warnings over smart speakers (Google Cast / HomePod / AirPlay) when high-priority threats (KAB/Missile) are detected.

---

## 🤝 Acknowledgements

This integration utilizes public data and event streams provided by the volunteer civil defense project **[eTryvoga (єТривога)](https://map.etryvoga.com)**.
Sincere gratitude to the volunteer team behind eTryvoga for their tireless 24/7 efforts keeping citizens informed and safe.

> [!IMPORTANT]
> This integration is an auxiliary home notification tool. Always pay attention to official civil defense warnings, the Air Force of Ukraine telegram channel, and outdoor sirens.

---

## 📄 License
This project is released under the open-source [MIT License](LICENSE).
