# Digitale Wasserwaage für das Wohnmobil – Home Assistant

🇩🇪 Deutsch · [🇬🇧 English](README_EN.md)

Eigene Lovelace-Karte für Home Assistant, die zeigt, wie schief das Wohnmobil steht
und **wie viele Zentimeter Keil unter welches Rad** gehören.

Fahrzeug: Benimar Tessoro 488 (Ford Transit, Radstand 395 cm) – alle Werte sind für jedes Wohnmobil einstellbar.

| Rück- & Seitenansicht | Draufsicht |
|---|---|
| ![](docs/vorschau-rueck-seite.png) | ![](docs/vorschau-draufsicht.png) |

## Funktionen

- **Rückansicht** (Querneigung) und **Seitenansicht** (Längsneigung): Boden kippt mit, Zentimeter und Pfeil an der tiefen Seite
- **Draufsicht**: Keilhöhe für jedes der vier Räder plus Libellen-Blase
- Liste „Keile unterlegen“, sortiert nach Höhe
- Farben: grün = waagerecht, orange = Keile nötig, rot = höher als die Keile reichen
- Nur „anheben“ (Nivellieren mit Keilen)
- **Konfiguration der Fahrzeugwerte** direkt im Karten-Editor von Home Assistant
- **[Simulator-Webseite](https://tbr-brd.github.io/digitale-wasserwaage-wohnmobil-homeassistant/simulator/)** zum Ausprobieren ohne Hardware

## Simulator

👉 **[Simulator online testen](https://tbr-brd.github.io/digitale-wasserwaage-wohnmobil-homeassistant/simulator/)**

Läuft komplett im Browser, auch offline: [`simulator/index.html`](simulator/index.html) herunterladen und öffnen.

- Neigung per Regler simulieren, inkl. „Leute laufen im Womo“ (Wackeln)
- Wohnmobil konfigurieren: Radstand, Spurbreite, höchste Keilstufe, Toleranz, Darstellung
- Vorlage „Benimar Tessoro 488“ oder eigene Werte, wird im Browser gespeichert
- erzeugt den fertigen **YAML-Code** für die Karte zum Kopieren

![Simulator](docs/simulator.png)

## Konfiguration

Die Karte hat einen grafischen Editor (Dashboard bearbeiten → Karte → Bearbeiten).
Alternativ per YAML:

```yaml
type: custom:womo-level-card
title: Benimar Tessoro 488
pitch_entity: sensor.womo_level_neigung_laengs   # + = Front höher
roll_entity: sensor.womo_level_neigung_quer      # + = rechte Seite höher
wheelbase: 395      # cm, Radstand
track: 170          # cm, Spurbreite – noch nachmessen
max_wedge: 10       # cm, höchste Keilstufe
min_lift: 0.5       # cm, kleinere Werte ignorieren
tolerance: 0.3      # Grad, gilt als waagerecht
default_view: overview   # overview | top
exaggerate: 4       # Neigung im Bild übertreiben
bubble_range: 3     # Grad bis Blase am Rand
invert_pitch: false
invert_roll: false
```

| Wert | Bedeutung | Standard |
|---|---|---|
| `wheelbase` | Abstand Vorder- zu Hinterachse | 395 cm |
| `track` | Spurbreite, Reifenmitte links bis rechts | 170 cm |
| `max_wedge` | höchste Stufe der eigenen Keile – darüber wird es rot | 10 cm |
| `min_lift` | kleinere Keilhöhen werden als 0 angezeigt | 0,5 cm |
| `tolerance` | bis zu diesem Winkel gilt das Womo als waagerecht | 0,3° |
| `default_view` | Startansicht | overview |
| `exaggerate` | wie stark die Neigung im Bild übertrieben wird | 4x |
| `bubble_range` | Winkel, bei dem die Blase am Rand ist | 3° |
| `invert_pitch` / `invert_roll` | Vorzeichen umdrehen, falls der Sensor anders herum eingebaut ist | aus |

## Entwicklung

`womo-level-card.js` ist die Karte. Nach Änderungen den Simulator neu bauen:

```bash
python3 build_simulator.py
```

## Status

- [x] Dashboard-Karte mit Einstellungs-Editor
- [x] Simulator-Webseite mit Fahrzeug-Konfiguration
- [ ] Sensor: Integration des **Xparkle RVS01** über das Bluetooth des Raspberry Pi 4 – siehe [Plan](docs/xparkle-integration.md)
- [ ] Alternative ohne Kaufgerät: ESPHome-Konfiguration (ESP32 + MPU6050, Kalibrier-Taste)
- [ ] Installationsanleitung

## Weitere Projekte

🌐 Übersicht aller Projekte: **[lets-make.de](https://www.lets-make.de)**

### 🚐 Wohnmobil & Home Assistant
| Projekt | Was es macht |
|---|---|
| [wohnmobil-touren-homeassistant](https://github.com/TBR-BRD/wohnmobil-touren-homeassistant) | Wohnmobil-Touren aus GPS-Daten auf der Karte |
| [gewitterwarner-gw1-shelly-uni-homeassistant](https://github.com/TBR-BRD/gewitterwarner-gw1-shelly-uni-homeassistant) | Gewitterwarner über Shelly UNI |
| [ha-action-32x32-led](https://github.com/TBR-BRD/ha-action-32x32-led) | 32x32-BLE-LED-Panel als Info-Anzeige |

### 📟 ESP32-Displays
| Projekt | Was es macht |
|---|---|
| [ha-round-pv-weather-display](https://github.com/TBR-BRD/ha-round-pv-weather-display) | Rundes ESP32-Display für PV, Akku und Wetter |
| [esp32-cyd-wetterdisplay](https://github.com/TBR-BRD/esp32-cyd-wetterdisplay) | Wetteranzeige mit Vorhersage auf dem ESP32 „Cheap Yellow Display“ |

### ☀️ Solar & Energie
| Projekt | Was es macht |
|---|---|
| [bkw-effizienz-steigern](https://github.com/TBR-BRD/bkw-effizienz-steigern) | Balkonkraftwerk effizienter mit Akku und zwei Wechselrichtern |
| [homeassistant-stromzaehler](https://github.com/TBR-BRD/homeassistant-stromzaehler) | Netzbezug, Einspeisung und PV-Erzeugung per Tasmota-Zähleradapter |
| [pv-bitcoin-miner](https://github.com/TBR-BRD/pv-bitcoin-miner) | Bitcoin-Mining mit PV-Überschuss, gesteuert per Shelly Pro 3EM |

Alle Projekte: [github.com/TBR-BRD](https://github.com/TBR-BRD)

<br>
<a href="https://www.buymeacoffee.com/thoralf.brandt" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174">
</a>
