# Auftrag an Claude Cowork — Datenbeschaffung SEO Memoria

> **Zweck:** Alles zusammentragen, was für die SEO-Entscheidungen im Oktober
> fehlt. Die Ergebnisse gehen zurück in die Entwicklungs-Session, die daraus
> die Seiten baut.
>
> **Wichtig:** Keine Empfehlungen ausarbeiten und keine Texte schreiben — das
> passiert in der anderen Session. Hier geht es ausschließlich um **Daten und
> Antworten**, sauber exportiert.

---

## Hintergrund in drei Sätzen

Tierbestattung Memoria (Laudenbach an der Bergstraße) ist seit dem 24.08.2026
mit einer neuen Website online. Im September wurden elf Unterseiten gebaut,
darunter Ortsseiten für Laudenbach, Einhausen, Weinheim, Bergstraße und
Odenwald. Jetzt muss entschieden werden, **für welche weiteren Orte und Themen
sich eigene Seiten lohnen** — und dafür reichen die Search-Console-Daten nicht
aus.

**Warum nicht:** Die Search Console zeigt nur Impressionen, also Fälle, in
denen die Seite tatsächlich angezeigt wurde. Steht eine Seite auf Position 20,
entstehen kaum Impressionen — unabhängig davon, wie oft gesucht wird. Das
tatsächliche Suchvolumen kommt nur aus dem Keyword Planner.

---

## Aufgabe 1 — Google Keyword Planner (höchste Priorität)

### Einstellungen

| Einstellung | Wert |
|---|---|
| Werkzeug | Keyword-Planer → **„Neue Keywords entdecken"** |
| Standort | **Deutschland** (nicht die Region — die Ortsnamen stecken schon im Suchbegriff) |
| Sprache | Deutsch |
| Zeitraum | **Letzte 12 Monate** |
| Suchnetzwerk | Google (ohne Suchnetzwerk-Partner) |

### Durchgang A — Orte

Diese Begriffe als Startkeywords eingeben. Bitte **alle** Kombinationen
abfragen, auch die, die unwahrscheinlich wirken:

```
tierbestattung mannheim
tierkrematorium mannheim
tierbestattung heidelberg
tierkrematorium heidelberg
tierbestattung ludwigshafen
tierbestattung worms
tierbestattung darmstadt
tierbestattung speyer
tierbestattung schwetzingen
tierbestattung hockenheim
tierbestattung wiesloch
tierbestattung frankenthal
tierbestattung viernheim
tierbestattung lampertheim
tierbestattung bürstadt
tierbestattung lorsch
tierbestattung bensheim
tierbestattung heppenheim
tierbestattung hemsbach
tierbestattung birkenau
tierbestattung schriesheim
tierbestattung ladenburg
tierbestattung michelstadt
tierbestattung erbach odenwald
```

### Durchgang B — Leistungen ohne Ort

```
tierbestattung
tierkrematorium
tier einäschern
hund einäschern
katze einäschern
kaninchen einäschern
tierkremierung
haustierbestattung
tierbestatter
hundebestatter
einzelkremierung
gemeinschaftskremierung
tierurne
tierfriedhof
pferdekremierung
pferd einäschern
```

### Durchgang C — Kosten

```
was kostet tierbestattung
tierbestattung kosten
hund einäschern kosten
katze einäschern kosten
tierkremierung preise
einäscherung hund preis
```

### Was ich zurückbekommen möchte

1. **Den CSV-Export** aus dem Keyword Planner, je Durchgang eine Datei
   („Keyword-Ideen herunterladen" → CSV). Bitte **nicht** abtippen oder
   zusammenfassen — die Rohdatei ist genau das, was gebraucht wird.
2. Die Spalten **Durchschnittliche monatliche Suchanfragen**, **Wettbewerb**
   und **Gebot für oberste Positionen (Bereich)** müssen enthalten sein.
3. Zusätzlich zu den eingegebenen Begriffen auch die **Keyword-Ideen**, die
   Google selbst vorschlägt — dort stecken oft Begriffe, an die niemand denkt.

### Wenn nur Spannen statt Zahlen erscheinen

Ohne laufende Kampagne zeigt der Keyword Planner oft Bereiche wie „100–1.000"
statt genauer Zahlen. **Das ist in Ordnung** — die Spannen bitte genauso
übernehmen. Die Größenordnung reicht für die Entscheidung völlig aus.

---

## Aufgabe 2 — Google Unternehmensprofil

Die Search Console zeigt ausschließlich die normale Google-Suche. Alles, was
über Google Maps und das Unternehmensprofil läuft, fehlt darin komplett — und
genau dort landen vermutlich die vielen „in der Nähe"-Suchen.

Im Google-Unternehmensprofil unter **Statistiken / Leistung**, Zeitraum
**letzte 6 Monate**, bitte Folgendes abgreifen (Screenshot genügt, Export ist
besser):

- Aufrufe gesamt, aufgeteilt nach **Google Suche** und **Google Maps**
- **Anrufe** über das Profil
- **Routenanfragen**
- **Websiteaufrufe** über das Profil
- Die Liste **„Suchbegriffe, über die Nutzer Sie gefunden haben"** — das ist
  der wertvollste Teil
- Anzahl und Durchschnitt der **Bewertungen** (zur Gegenprüfung: wir arbeiten
  mit 4,9 aus 186)

Außerdem bitte prüfen und notieren:

- Sind die **Öffnungszeiten als 24 Stunden / 7 Tage** hinterlegt?
- Ist die **Website-URL** auf `https://www.tierbestattung-memoria.de`
  aktualisiert (nicht mehr die alte Wix-Adresse)?
- Welche **Kategorien** sind gesetzt (Haupt- und Nebenkategorien)?
- Wie viele **Fotos** sind hinterlegt, und wann wurde zuletzt eines
  hochgeladen?
- Ist das **Einzugsgebiet** im Profil eingetragen?

---

## Aufgabe 3 — Antworten von Franz (Inhaber) einholen

Diese Fragen blockieren konkrete Stellen auf der Website. Überall dort steht
aktuell bewusst nichts oder nur ein Verweis aufs Telefon, weil wir nichts
erfinden. Bitte als **Gesprächsleitfaden für ein Telefonat** aufbereiten, nicht
als E-Mail-Fragebogen — am Telefon ist das in zehn Minuten geklärt.

| # | Frage | Wofür |
|---|---|---|
| 1 | Kostet die Abholung extra? Pauschale, Kilometerpreis oder im Preis enthalten? | FAQ auf `/preise` |
| 2 | Wann und wie wird bezahlt? (Zeitpunkt, Zahlungsarten) | FAQ auf `/preise` |
| 3 | Wie lange dauert es realistisch, bis die Urne zurück ist? | FAQ auf `/preise` |
| 4 | Was sollen Tierhalter tun, bis jemand vor Ort ist? **Fachliche Angabe, bitte wörtlich mitschreiben** | `/tier-nachts-gestorben` |
| 5 | Bietet Memoria eine Beisetzung oder einen Tierfriedhof an — oder ausschließlich Kremierung? | Wird häufig gesucht |
| 6 | Wofür genau steht die Abholadresse Einhausen? Können Kunden dort etwas abgeben oder die Urne holen? | `/anfahrt`, `/tierbestattung-einhausen` |
| 7 | Gibt es feste Zeiten, zu denen jemand in Laudenbach vor Ort ist? Parkplätze? | `/anfahrt` |
| 8 | Gibt es einen maximalen Radius oder Fahrtkosten ab einer Entfernung? | Einzugsgebiet |
| 9 | Wie schnell ist in Laudenbach und Umgebung üblicherweise jemand da? | Ortsseiten |
| 10 | Wird die Pferdekremierung aktiv angeboten oder über einen Partner vermittelt? | Entscheidung über eine eigene Seite |

### Zusätzlich von Franz besorgen

- **Vier bis sechs Google-Bewertungen im Wortlaut**, die auf der Website
  gezeigt werden dürfen. Je Bewertung: Text, Vorname oder Initialen, Monat.
  *(Die Website zeigt aktuell drei erfundene Platzhalter-Zitate aus dem
  Design-Entwurf — die müssen ersetzt werden.)*
- Den **Link zum Google-Profil** (Google Maps → Teilen → Link kopieren).

---

## Aufgabe 4 — Eine offene Frage aus der Search Console

In der Search Console unter **Indexierung → Seiten** gibt es den Eintrag
**„Durch ‚noindex'-Tag ausgeschlossen: 1"**. Bitte die Zeile anklicken und die
betroffene URL notieren.

- Ist es `/404` → alles in Ordnung, so gewollt.
- Ist es eine **echte Inhaltsseite** → bitte sofort melden, das wäre ein
  Fehler, der die Seite aus dem Index hält.

---

## Format der Rückgabe

Bitte in dieser Reihenfolge, als eine zusammenhängende Antwort:

1. **Keyword-Planner-CSVs** als Dateien (Durchgang A, B, C getrennt)
2. **Unternehmensprofil-Zahlen** als Tabelle oder Screenshot, plus die
   Antworten auf die fünf Prüffragen
3. **Antworten von Franz** zu den zehn Fragen, so wörtlich wie möglich —
   besonders bei Frage 4
4. **Bewertungstexte** und Profil-Link
5. **Die URL** aus Aufgabe 4

Wo etwas nicht beschafft werden konnte: bitte ausdrücklich hinschreiben, dass
es fehlt, statt die Lücke zu überspringen. Eine bekannte Lücke ist besser als
eine stille.
