# SEO-Plan – Tierbestattung Memoria

> Vorschlag zur Abstimmung. **Noch nichts davon ist umgesetzt.**
> Stand: nach Fertigstellung der Seite, vor dem Livegang.

---

## Ausgangslage (gemessen, nicht geschätzt)

| Prüfpunkt | Befund |
|---|---|
| Lighthouse SEO | 100 / 100 |
| Startseite Textmenge | 909 Wörter |
| Tierurnen-Seite | 492 Wörter |
| Titles / Descriptions | vorhanden, gute Länge (76 / 155 Zeichen) |
| Strukturierte Daten | LocalBusiness + FAQPage vorhanden |
| **H1 mit Keyword** | ❌ „Ein würdevoller Abschied für Ihr Tier" – kein Suchbegriff |
| **Eigene Seiten für Geld-Keywords** | ❌ /leistungen, /preise, /pferdekremierung sind nur Weiterleitungen |
| **404-Seite** | ❌ kein `noindex`, Canonical zeigt auf `/404/` |
| **Sitemap `lastmod`** | ❌ fehlt |
| **Interne Links** | ⚠️ `/tierurnen-andenken` ohne Slash → jeder Klick ein 301-Umweg |
| **Geo-Daten im Schema** | ❌ keine Koordinaten, `areaServed` nur als Fließtext |

Die Technik ist sehr gut. Die Lücken liegen bei **Inhalt, Seitenstruktur und
lokalen Signalen** – also genau dort, wo bei einem lokalen Dienstleister die
Rankings entstehen.

---

## Priorität 1 – Technische Quick Wins
*Kein Eingriff ins Design, geringes Risiko, ca. 1–2 Stunden*

1. **404-Seite auf `noindex`** setzen und Canonical entfernen.
   Sonst kann Google die Fehlerseite indexieren.
2. **Interne Links auf die kanonische Form** (`/tierurnen-andenken/` mit Slash).
   Spart bei jedem Klick eine Weiterleitung – gut für Crawling und Tempo.
3. **`lastmod` in die Sitemap** aufnehmen. Signalisiert Google Aktualität.
4. **Schema erweitern** (rein additiv, unsichtbar für Besucher):
   - `geo` mit Koordinaten + `hasMap` → **wichtig für die lokale Suche**
   - `areaServed` als echte Orte statt Fließtext
   - `Service`-Einträge für Einzel-/Gemeinschaftskremierung und Pferde,
     jeweils mit Preis ab-Angabe → Chance auf erweiterte Suchergebnisse
   - `BreadcrumbList` auf den Unterseiten
   - `foundingDate`, `paymentAccepted`, `currenciesAccepted`
5. **Dev-Domain vor Indexierung schützen** (`noindex` bzw. Basic-Auth), sonst
   konkurriert `memoria.stolz-marketing.de` mit der Live-Domain.
6. **Bild-Dateinamen**: `hero-1553.webp` → sprechender Name wie
   `tierbestattung-memoria-wald.webp`. Kleiner Faktor, aber kostenlos.

> ⚠️ Für die Koordinaten brauche ich die exakte Position des Standorts
> (Konrad-Zuse-Str. 3). Bitte aus Google Maps kopieren – ich rate sie nicht.

---

## Priorität 2 – Seitenstruktur *(größter Hebel)*
*Braucht deine Entscheidung*

### Das Kernproblem
Die alte Seite hatte eigene Seiten für `/leistungen`, `/preise` und
`/pferdekremierung`. Diese URLs waren bei Google indexiert. Wir leiten sie
aktuell **alle auf die Startseite** um.

Das ist für den Umzug korrekt (nichts läuft ins Leere), aber langfristig
schwach: Google kann eine Startseite nur für **ein** Hauptthema ranken. Für
„Tierkremierung Preise" oder „Pferdekremierung" fehlt dann die passende Seite.

### Vorschlag: 3 eigene Landingpages

| Neue Seite | Ziel-Suchbegriffe | Inhalt |
|---|---|---|
| `/leistungen` | Tierkremierung, Einzelkremierung Hund/Katze | Ablauf, Unterschied Einzel/Gemeinschaft, Abholung, Urkunde |
| `/preise` | Tierkremierung Preise, Kosten Einäscherung Hund | Preistabellen + was enthalten ist + Größenlogik |
| `/pferdekremierung` | Pferdekremierung, Pferd einäschern | eigener Ablauf, Abholung großer Tiere, Preis auf Anfrage |

**Wichtig:** Die Startseite behält alle Abschnitte – die neuen Seiten gehen
jeweils **in die Tiefe**. Die Weiterleitungen werden dann entfernt, sodass die
alten URLs wieder echte Seiten sind. Das ist der sauberste Fall für Google:
gleiche URL, besserer Inhalt.

**Aufwand:** ca. 1 Tag inkl. Texten. **Ich brauche dafür Input vom Kunden**
(Details zur Pferdekremierung, Ablauf, ggf. Preisrahmen).

### Einzugsgebiet sichtbar machen
Ein Abschnitt „Wir sind für Sie da in …" mit den umliegenden Orten
(Weinheim, Hemsbach, Heppenheim, Bensheim, Viernheim, Lampertheim, Bürstadt,
Einhausen, Mannheim, Heidelberg). Das ist der klassische Hebel, um über den
eigenen Ort hinaus gefunden zu werden.

> ⚠️ Nur Orte nennen, die wirklich bedient werden – bitte vom Kunden bestätigen
> lassen.

---

## Priorität 3 – Texte & Keywords
*Braucht deine Entscheidung, weil es das Design berührt*

Die Überschriften sind emotional stark, enthalten aber **keinen einzigen
Suchbegriff**. Google gewichtet H1/H2 weiterhin.

**Drei Optionen – abgestuft nach Eingriff ins Design:**

- **A (mein Vorschlag): Nur die Zwischenüberschriften erweitern.**
  Die große H1 bleibt exakt wie im Design. Beispiel:
  „Was nach Ihrem Anruf geschieht" → „Ablauf der Tierkremierung – was nach
  Ihrem Anruf geschieht". Wirkung solide, Design bleibt praktisch unberührt.
- **B: H1 ergänzen** – „Ein würdevoller Abschied für Ihr Tier" bleibt, darunter
  eine sichtbare Zeile „Tierbestattung & Tierkrematorium in Laudenbach".
  (Die Eyebrow-Zeile sagt heute nur „TIERBESTATTUNG MEMORIA".)
- **C: Nichts ändern.** Design bleibt 100 % wie freigegeben, dafür bleibt hier
  Potenzial liegen.

Zusätzlich, unabhängig von der Wahl:
- **FAQ intern verlinken** (z. B. Urnengrößen-Antwort → Tierurnen-Seite).
- **Bild-Alt-Texte** leicht anreichern („Tierurne Verona Weiß aus Keramik").

---

## Priorität 4 – Was außerhalb der Website passieren muss
*Das kann ich nicht umsetzen – hat aber lokal oft die größte Wirkung*

1. **Google Unternehmensprofil** pflegen: Öffnungszeiten (24/7), Fotos,
   Leistungen, Website-Link auf die neue Domain. Für den „Local Pack"
   (Kartenergebnisse) ist das der wichtigste Faktor überhaupt – meist wichtiger
   als alles auf der Website.
2. **Bewertungen** aktiv einsammeln. Nach dem Livegang können echte Bewertungen
   die Design-Zitate auf der Startseite ersetzen.
3. **Branchenverzeichnisse** mit identischen Daten (Name, Adresse, Telefon):
   Gelbe Seiten, Das Örtliche, Bing Places.
4. **Tierarztpraxen der Region** – Verlinkungen von deren Seiten sind
   thematisch perfekt passende und dadurch besonders wertvolle Empfehlungen.

---

## Was ich bewusst *nicht* empfehle

- **Keyword-Stuffing** in den Fließtexten. Das Thema ist emotional; ein Text,
  der nach SEO klingt, kostet hier mehr Vertrauen als er an Ranking bringt.
- **`aggregateRating` im Schema** ohne echte, nachweisbare Bewertungen. Das
  verstößt gegen Googles Richtlinien und kann abgestraft werden.
- **Blog** „für SEO", solange niemand ihn regelmäßig pflegt. Verwaiste Blogs
  schaden dem Gesamteindruck mehr, als sie nützen.

---

## Vorschlag zur Reihenfolge

| Wann | Was |
|---|---|
| **Vor dem Livegang** | Priorität 1 komplett (technische Quick Wins) |
| **Zum Livegang** | Google Unternehmensprofil auf neue Domain, Search Console |
| **1–2 Wochen danach** | Priorität 2 (die drei Landingpages) – dann sieht man in der Search Console auch, wonach wirklich gesucht wird |
| **Laufend** | Bewertungen, Verzeichnisse, Verlinkungen |

### Ehrliche Einordnung
Priorität 1 ist gute Handwerksarbeit – sie verhindert Verluste und legt die
Basis, bringt aber allein selten große Sprünge. Die eigentliche Bewegung
entsteht durch **Priorität 2 (eigene Seiten)** und **Priorität 4 (Google
Unternehmensprofil + Bewertungen)**. Rankings brauchen erfahrungsgemäß
mehrere Wochen bis Monate, besonders direkt nach einem Domain-/Seitenwechsel –
kurzfristige Schwankungen nach dem Umzug sind normal.
