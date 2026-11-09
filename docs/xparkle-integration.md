# Xparkle RVS01 in Home Assistant einbinden (Plan)

Statt eines selbst gebauten Sensors (ESP32 + MPU6050) soll der fertige
**Xparkle RVS01** (Bluetooth, 2× AA) die Neigung liefern.

- Produkt: [Xparkle RVS01 bei hobbydirekt](https://www.hobbydirekt.de/Neuheiten/Neuheiten-2025/Minicars/Xparkle-RVS01-Smart-RV-Nivellierungsnavigator-XPARKLE-XP-990008-01-XP990008-01::410112.html)
- Home Assistant im Womo: **Raspberry Pi 4** mit eingebautem Bluetooth – kein ESP32 nötig

Es gibt keine fertige Integration, das Bluetooth-Protokoll muss erst ausgelesen werden.

## Ziel

Eigene Integration `custom_components/xparkle_level`:

- Verbindung über die Bluetooth-Integration von Home Assistant (Adapter des Pi 4)
- Sensoren `sensor.womo_level_neigung_laengs` und `sensor.womo_level_neigung_quer`
  → passen ohne Änderung zur `womo-level-card`
- Schalter **„Nivellieren“**: Verbindung nur bei Bedarf, schont die Batterien;
  optional automatische Abschaltung nach 15 Minuten
- Batteriestand als Sensor, falls das Gerät ihn liefert

## Schritte

1. **Bluetooth in HA prüfen**
   *Einstellungen → Geräte & Dienste → Bluetooth* – eingebauter Adapter des Pi 4 vorhanden?
2. **Rundsendungen ansehen**
   Batterien einlegen, *Bluetooth → Werbungsmonitor* öffnen, Xparkle suchen, Screenshot.
   Stecken die Winkel schon in den Rundsendungen, reicht passives Mithören (sparsamer, keine Verbindung).
3. **Bluetooth-Dienste auslesen**
   iPhone-App *nRF Connect* → mit Xparkle verbinden → Dienste und Merkmale notieren,
   Benachrichtigungen einschalten, Gerät in bekannte Richtungen kippen und Werte
   zusammen mit der Anzeige der Xparkle-App festhalten.
4. **Protokoll entschlüsseln**
   Rohdaten den Winkeln zuordnen (Byte-Position, Datentyp, Skalierung, Vorzeichen).
   Falls das Gerät erst nach einem Startbefehl sendet: Mitschnitt der App nötig.
5. **Integration schreiben und testen**
6. **Dokumentation** in der README ergänzen

## Zu beachten

- Meist ist **nur eine Verbindung gleichzeitig** möglich: Solange HA verbunden ist,
  kann sich die Xparkle-App nicht verbinden.
- Eine dauerhafte Verbindung leert die AA-Batterien schneller → Schalter „Nivellieren“.

## Status

- [ ] Xparkle bestellt / angekommen
- [ ] Schritt 1–2: Bluetooth & Rundsendungen
- [ ] Schritt 3–4: Protokoll
- [ ] Schritt 5: Integration
