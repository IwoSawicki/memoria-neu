# CLAUDE.md — Tierbestattung Memoria Website

Diese Datei enthält die **verbindlichen Vorgaben** für den 1:1-Nachbau der
Memoria-Website in Astro. Grundlage ist der Claude-Design-Export in
`docs/design-reference/Designvorschlag_2.dc.html`. Alle Werte unten sind exakt
aus diesem Export übernommen. Bei Abweichungen gilt: **der Export ist die
Wahrheit**, diese Datei die Referenz.

---

## 1. Projekt & Ziel

- **Kunde:** Tierbestattung Memoria (Laudenbach) – Familienunternehmen für
  Tierkremierung (Einzel- & Gemeinschaftskremierung, Tierurnen).
- **Ziel:** Das Design 1:1 nachbauen – Farben, Fonts, Abstände, Größen,
  Verhalten. Technik: **Astro** (statisch), später um SEO-Inhalte erweiterbar.
- **Header und Footer sind auf allen Seiten identisch** (eigene Komponenten).
- **Sprache:** Deutsch (`lang="de"`).

### Getroffene Entscheidungen (mit dem Kunden abgestimmt)
1. **Bilder:**
   - **Hero:** `public/images/hero.webp` (aus dem vom Kunden hochgeladenen
     `memoria-herobild.png` optimiert, 1553×1013).
   - **Über uns:** `public/images/about.webp` (aus `pasted-1785311187667-0.png`
     optimiert, 994×1240, ~4:5). ✅ eingebunden.
   - **Kontakt-Parallax:** `public/images/contact.webp` (aus dem hochgeladenen
     `Memoria-Kontaktbild.png` optimiert, Waldpanorama). ✅ eingebunden.
   - Die hochgeladenen Original-PNGs bleiben im Repo; ausgeliefert werden die
     optimierten WebP-Dateien.
2. **Styling:** Umsetzung über **zentrale Design-Tokens** (CSS-Variablen) und
   saubere Komponenten – **exakt dieselben Werte** wie im Export, nur wartbar.
3. **Kontaktformular:** Versand über **Web3Forms** (AJAX, Bestätigung inline).
   Access Key in `src/data/site.ts` (`web3formsKey`) eintragen – bis dahin
   blockiert der Versand mit Hinweis. Honeypot gegen Spam aktiv.
4. **Unterseiten:** `impressum` und `datenschutz` werden als **eigene
   Astro-Seiten mit Header/Footer angelegt** (Struktur jetzt, Inhalt später).

---

## 2. Design-Tokens

### 2.1 Farben (exakt)
| Token | Hex | Verwendung |
|---|---|---|
| `--bg-page` | `#f3f8e5` | Seitenhintergrund (hell, salbeigrün) |
| `--bg-hero` | `#1c2413` | Hero-Sektion Hintergrund |
| `--bg-dark` | `#2b3a1e` | Ablauf, Footer, Mobile-Bar |
| `--bg-contact` | `#141a0e` | Kontakt-Sektion (dunkelste) |
| `--bg-card` | `#e6eecd` | Karten (Leistungen, Preise), Bild-Fallback |
| `--accent` | `#cfe36b` | Lime-Akzent (Buttons, Eyebrows, Zahlen) |
| `--accent-hover` | `#dcec84` | Lime Hover |
| `--text` | `#1f2d16` | Standard-Textfarbe / Links |
| `--text-link-hover` | `#0f1a08` | Link-Hover (global) |
| `--heading-dark` | `#16260c` | Überschriften auf hellem Grund |
| `--text-light` | `#eef3e0` | Text auf dunklem Grund (Kontakt/Footer) |
| `--text-lightest` | `#f7f9ee` | Logo & Headings auf dunkel (Hero) |
| `--about-lead` | `#22331a` | Über-uns-Lead-Absatz |
| `--muted-1` | `#3d4a30` | Fließtext gedämpft (Leistungen-Intro, Preis-dt) |
| `--muted-2` | `#4a5940` | Kartentext |
| `--muted-3` | `#5c6b4c` | Kursive Notizen, Preis-Hinweise |
| `--icon-stroke` | `#3f5325` | Icon-Stroke Leistungskarten |
| `--chevron` | `#9bb06a` | Chevron-Trenner unter Hero |
| `--rule-price` | `#d5deba` | Trennlinien Preistabelle |
| `--btn-text` | `#1b2610` | Textfarbe auf Lime-Buttons |

**Text auf dunkel mit Deckkraft (rgba, exakt beibehalten):**
- Nav-Links Hero: `rgba(247,249,238,0.88)` (Hover `#ffffff`)
- Hero-Subzitat: `rgba(255,255,255,0.92)`
- Ablauf-Kartentext: `rgba(238,243,224,0.74)`
- Ablauf-Trennlinien: `rgba(238,243,224,0.28)` (unten `0.2`)
- Eyebrow auf dunkel: `rgba(207,227,107,0.85)`
- Footer-Links: `rgba(238,243,224,0.72)` (Hover `#ffffff`)
- Footer-Adresse: `rgba(238,243,224,0.5)` / `0.45`
- Kontakt-Fließtext: `rgba(255,255,255,0.82)` / `0.7` / `0.6`
- Mobile-Menü-Trennlinien: `rgba(247,249,238,0.22)`

**Verläufe (exakt):**
- Hero-Overlay: `linear-gradient(180deg, rgba(20,26,14,0.5) 0%, rgba(20,26,14,0.3) 45%, rgba(20,26,14,0.6) 100%)`
- Kontakt-Overlay: `linear-gradient(180deg, rgba(16,21,11,0.82) 0%, rgba(16,21,11,0.7) 50%, rgba(16,21,11,0.86) 100%)`

### 2.2 Fonts
- **Fraunces** (Serif) – Headings, Logo, Zitate. Variable Font, `opsz`.
  Gewichte: **300** (leichte Headings), **400** (H3, Logo), **500** verfügbar.
  Kursiv verwendet. Fallback: `Georgia, serif`.
- **Figtree** (Sans) – Fließtext. Gewichte **400/500/600**.
  Fallback: `'Helvetica Neue', Arial, sans-serif`.
- **Selbst gehostet** (DSGVO): Variable Fonts via `@fontsource-variable/fraunces`
  (`opsz` + `opsz-italic`) und `@fontsource-variable/figtree` (`wght`), importiert
  im `BaseLayout`. Family-Namen: `'Fraunces Variable'` / `'Figtree Variable'`.
  Kein Aufruf von Google-Servern mehr. (Ursprung: Google-Fonts-Export
  `Fraunces:ital,opsz,wght@0,9..144,300..500;1,…` + `Figtree:wght@400;500;600`.)
- **Basis:** `font-size:16px`, `line-height:1.7`, `color:#1f2d16`,
  Font-Familie Body = Figtree-Stack. `-webkit-font-smoothing:antialiased`.

### 2.3 Layout-Grundwerte
- **Max. Inhaltsbreite:** `1240px` (zentriert, `margin:0 auto`).
- **Border-Radius:** Karten `18px`; Bilder `22px`; abgerundete Sektionsoberkante
  `clamp(20px,2.6vw,34px)`; Buttons/Pills `999px`; Inputs `10px`.
- **Mobile-Breakpoint:** `< 1000px` (JS-gesteuert: Nav→Hamburger,
  Trust-Row→Spalte).
- **Body:** `overflow-x:hidden`; `html{scroll-behavior:smooth}`;
  `section[id]{scroll-margin-top:20px}`.

---

## 3. Seitenstruktur (DOM-Reihenfolge) & exakte Werte

Reihenfolge im DOM: **Hero → Leistungen → Über uns → Ablauf (inkl. Zitate) →
Preise → Kontakt → Footer → Mobile-Sticky-Bar**.
Nav-Reihenfolge (Anker): Ablauf · Leistungen · Über uns · Kontakt · Preise.

### 3.1 Hero `#top`
- Sektion: `background:#1c2413; min-height:100svh; display:flex; flex-direction:column`.
- Hero-Bild: `public/images/hero.webp`, `position:absolute; inset:0;
  object-fit:cover; object-position:50% 50%`, **Ken-Burns-Animation** (`kenburns 30s ease-out forwards`). Alt: „Frau geht mit ihrem Hund durch einen sonnigen Wald".
- Overlay-Div mit Hero-Gradient (s.o.).
- **Header** (relativ, über dem Bild): `padding:clamp(18px,2.2vw,30px) clamp(20px,3vw,42px)`, Flex space-between.
  - Logo „Memoria": Fraunces 400, `clamp(26px,2.4vw,34px)`, `#f7f9ee`, Link `#top`.
  - Nav (Desktop): Links 15px/500, `rgba(247,249,238,0.88)`, gap `clamp(16px,2vw,30px)`.
  - Telefon-Button: bg `#cfe36b`, text `#1b2610`, `border-radius:999px; padding:11px 22px`, 15px/600, `font-variant-numeric:tabular-nums`. Text „06201 7303041", `href="tel:+4962017303041"`.
  - Hamburger-Button (mobil): zwei Balken `30x2px #f7f9ee`, `min-height:44px`.
- **Mobile-Menü-Panel** (mobil): Links Fraunces 26px, `#f7f9ee`, je `border-top:1px solid rgba(247,249,238,0.22)` (letzter zusätzlich border-bottom).
- **Hero-Center** (`data-reveal`): zentriert.
  - Eyebrow: „TIERBESTATTUNG MEMORIA", `clamp(12px,1.05vw,14px)`, 600, `letter-spacing:0.3em`, uppercase, `#cfe36b`.
  - H1: „Ein würdevoller Abschied für Ihr Tier", Fraunces **300**, `clamp(42px,6.6vw,92px)`, `line-height:1.02; letter-spacing:-0.02em; color:#ffffff; max-width:15ch; text-wrap:balance`.
  - Subzitat: „„Wir können Ihnen nicht die Trauer nehmen, …"", `clamp(16px,1.35vw,19px)`, `line-height:1.6; color:rgba(255,255,255,0.92); max-width:46ch; text-wrap:pretty`.
  - CTA (`data-herocta`): „Jetzt anrufen · 06201 7303041", bg `#cfe36b`, text `#1b2610`, `border-radius:999px; padding:19px 38px; font-size:17px; font-weight:600; min-height:58px`. `href="tel:+4962017303041"`.
- **Trust-Row** (`data-reveal`, `data-trustrow`): 3 Einträge mit Kreis-Häkchen-SVG (`#cfe36b`), Text 16px `#ffffff`:
  „Abholung rund um die Uhr" · „Einzelkremierung mit Ascherückgabe" · „Kleines Familienunternehmen". Mobil: Spalte.

### 3.2 Leistungen `#leistungen`
- Sektion überlappt Hero: `background:#f3f8e5; border-radius:clamp(20px,2.6vw,34px) clamp(20px,2.6vw,34px) 0 0; margin-top:clamp(-34px,-2.6vw,-20px); position:relative; z-index:2`.
- Chevron-Trenner-SVG oben (`#9bb06a`).
- H2 (Fraunces 300, `clamp(34px,5vw,64px)`, `#16260c`, `max-width:19ch`, `text-wrap:balance`): „Sie müssen jetzt nichts allein regeln. Wir übernehmen den **ganzen Weg.**" – „ganzen Weg." mit **handgezeichneter Unterstreichung** (3 SVG-Pfade, `#cfe36b`).
- Intro-Absatz: `clamp(16px,1.3vw,18px)`, `line-height:1.75; color:#3d4a30; max-width:58ch`.
- **3 Karten** (Grid `repeat(auto-fit, minmax(260px,1fr))`, gap `clamp(16px,1.8vw,26px)`):
  jede `background:#e6eecd; border-radius:18px; padding:clamp(28px,2.8vw,38px)`, Icon-SVG (`#3f5325`, `margin-bottom:clamp(48px,6vw,86px)`), H3 19px/600 `#16260c`, Text 16px `#4a5940`.
  1. **Einzelkremierung** – „Ihr Tier wird allein kremiert. …"
  2. **Gemeinschaftskremierung** – „Ein würdiger Abschied ohne Ascherückgabe. …"
  3. **Tierurnen und Andenken** – „Urnen aus Holz, Stein und Keramik, …"
- Kursive Notiz (Fraunces italic, 15px, `#5c6b4c`): „Auch Pferde und große Tiere · Abholung zu Hause oder in der Tierklinik".

### 3.3 Über uns `#ueber-uns`
- `background:#f3f8e5`, Grid `repeat(auto-fit, minmax(300px,1fr))`, gap `clamp(32px,5vw,80px)`, `align-items:center` (`data-reveal`).
- Bild links: `border-radius:22px; overflow:hidden; background:#e6eecd; aspect-ratio:4/5`. **Platzhalter** (Original: „Kind streichelt einen liegenden Hund im Wald").
- Rechts:
  - H2 (Fraunces 300, `clamp(30px,3.9vw,50px)`, `#16260c`): „Ein Abschied, den man *in guter Erinnerung* behält." (Teil kursiv).
  - Lead (Fraunces, `clamp(19px,1.8vw,23px)`, `#22331a`, `max-width:42ch`): „„Als kleines Familienunternehmen …"".
  - Absatz (16px, `#4a5940`, `max-width:52ch`): „Sarina Göck-König und Dr. Klaus Göck …".
  - Kursiv-Zitat (Fraunces italic, 17px, `#4a5940`): „„Mit Tieren aufgewachsen …" — Sarina Göck-König".
  - Button „Lernen Sie uns kennen" (Outline `1.5px solid #16260c`, `border-radius:999px; padding:15px 30px`, `#16260c`, Hover bg `#e6eecd`), `href="#kontakt"`.

### 3.4 Ablauf `#ablauf`
- `background:#2b3a1e; color:#eef3e0; border-radius:clamp(20px,2.6vw,34px)`.
- H2 (Fraunces 300, `clamp(32px,4.6vw,58px)`, `#f7f9ee`, `max-width:16ch`): „Was nach Ihrem Anruf geschieht".
- **4 Schritte** (Grid `repeat(auto-fit, minmax(230px,1fr))`, gap `clamp(28px,3vw,44px)`), jeder `border-top:1px solid rgba(238,243,224,0.28); padding-top:22px`:
  Nummer (14px/600, `#cfe36b`, tabular-nums) · H3 (Fraunces 400, 25px, `#f7f9ee`) · Text (16px, `rgba(238,243,224,0.74)`).
  1. **01 Sie rufen an** · 2. **02 Wir holen ab** · 3. **03 Die Kremierung** · 4. **04 Die Urne**.
- **Testimonial-Slider** (gleiche Sektion, `border-top:1px solid rgba(238,243,224,0.2)`):
  - Eyebrow: „Freundliche Worte von Tierhaltern", 13px/600, `letter-spacing:0.28em`, uppercase, `rgba(207,227,107,0.85)`.
  - Prev/Next-Buttons: `46x46px`, `border-radius:999px; border:1px solid rgba(238,243,224,0.35)`, Pfeil-SVG, Hover `#cfe36b`.
  - Zitattext (Fraunces 300, `clamp(24px,3.2vw,42px)`, `#f7f9ee`, `max-width:22ch`) + Autor (15px, `rgba(238,243,224,0.6)`).
  - **Verhalten:** 3 Zitate, Auto-Rotation alle **8s**, Fade (`opacity` transition `0.9s`, Swap nach `500ms`).

  Zitate:
  1. „„Wir haben nachts angerufen und sofort einen ruhigen Menschen am Telefon gehabt. Das hat uns sehr geholfen."" — **M. K.**
  2. „„Unser Hund wurde mit einer Achtsamkeit abgeholt, die wir nicht erwartet hatten. Danke dafür."" — **A. B.**
  3. „„Alles wurde uns in Ruhe erklärt, nichts musste schnell entschieden werden. Die Urne ist wunderschön."" — **S. R.**

### 3.5 Preise `#preise`  (nur wenn `showPrices` – Standard: an)
- `background:#f3f8e5`.
- H2 (Fraunces 300, `clamp(32px,4.6vw,58px)`, `#16260c`): „Transparent und ohne Zusätze".
- Hinweis (16px, `#5c6b4c`): „Alle Preise inkl. Urkunde, Überführung, Energie-, CO₂-Zuschlag und 19 % MwSt."
- **2 Preistabellen** (Grid `repeat(auto-fit, minmax(300px,1fr))`, gap `clamp(16px,1.8vw,26px)`),
  je Karte `background:#e6eecd; border-radius:18px; padding:clamp(28px,3vw,40px)`.
  H3 (Fraunces 400, 25px, `#16260c`) + Badge (15px, `#5c6b4c`). `<dl>` Grid `1fr auto`, 16px,
  Zeilen `border-bottom:1px solid #d5deba`, `dt` `#3d4a30`, `dd` `#16260c` tabular-nums rechtsbündig.

  **Einzelkremierung mit Ascherückgabe** *(inkl. Urnengutschrift)*:
  Vögel & Kleintiere **115 €** · Kaninchen **135 €** · Katzen & Hunde bis 5 kg **195 €** ·
  5–20 kg **235 €** · 20–40 kg **315 €** · 40–60 kg **370 €** · über 60 kg **430 €**.

  **Gemeinschaftskremierung** *(ohne Ascherückgabe)*:
  Vögel & Kleintiere **60 €** · Kaninchen **70 €** · Katzen & Hunde bis 5 kg **120 €** ·
  5–20 kg **160 €** · 20–40 kg **210 €** · 40–60 kg **260 €** · über 60 kg **320 €**.
- Fußnote (16px, `#5c6b4c`): „Preise für die Pferdekremierung nennen wir Ihnen gern persönlich am Telefon."

### 3.6 Kontakt `#kontakt`
- `background:#141a0e; color:#eef3e0; position:relative; overflow:hidden`.
- **Parallax-Bild** (`data-parallax`, `aria-hidden`): **Platzhalter**, `position:absolute; top:-14%; height:128%; object-fit:cover`. Verhalten: leichter vertikaler Parallax beim Scrollen.
- Kontakt-Overlay-Gradient (s.o.).
- Grid `repeat(auto-fit, minmax(300px,1fr))`, gap `clamp(36px,5vw,80px)`, `align-items:center` (`data-reveal`).
- Links: Eyebrow „Kontakt"; H2 (Fraunces 300, `clamp(34px,4.6vw,60px)`, `#ffffff`): „Schreiben Sie uns in Ruhe"; Absatz (`rgba(255,255,255,0.82)`); „Lieber direkt sprechen? **06201 7303041**" (Link `#cfe36b`).
- **Formular** (`display:grid; gap:14px`): Inputs `name`, `email`(email), `phone`(tel), `textarea`(message, rows 4). Alle `background:#ffffff; border:none; border-radius:10px; padding:18px 20px; font-size:16px; color:#16260c; min-height:58px`. Submit-Button „Nachricht senden" (bg `#cfe36b`, text `#1b2610`, pill). Hinweistext darunter.
  - **Verhalten:** Submit → `preventDefault`, Hinweis wechselt zu „Danke – wir melden uns so schnell wie möglich bei Ihnen." (kein echter Versand, s. Entscheidung 3).

### 3.7 Footer  (auf allen Seiten identisch)
- `background:#2b3a1e; color:#eef3e0`.
- Eyebrow: „Rund um die Uhr erreichbar" (13px/600, ls 0.28em, `rgba(207,227,107,0.85)`).
- H2 (Fraunces 300, `clamp(38px,7vw,104px)`, `line-height:1`, `#f7f9ee`, `max-width:14ch`): „Sie erreichen uns jederzeit".
- Telefon-Link (Fraunces 300, `clamp(34px,6vw,84px)`, `#cfe36b`, `border-bottom:1px solid rgba(207,227,107,0.4)`): „06201 7303041", `tel:+4962017303041`.
- E-Mail: „info@tierbestattung-memoria.de" (`mailto:`), `#eef3e0` mit Unterstrich.
- Untere Grid-Zeile (3 Spalten, `border-top:1px solid rgba(238,243,224,0.2)`):
  1. „Memoria" (Fraunces 30px) + „Sarina Göck-König / Dr. Klaus Göck".
  2. Nav: Leistungen · Ablauf · Über uns · Preise (`rgba(238,243,224,0.72)`).
  3. Adresse: „Konrad-Zuse-Str. 3, 69514 Laudenbach" · „Abholadresse: Carl-Benz-Str. 1, 64683 Einhausen".
- Untere Leiste: „Tierbestattung Memoria · Abholung 365 Tage im Jahr" | „Impressum · Datenschutz".

### 3.8 Mobile-Sticky-Bar  (nur wenn `showStickyBar` – Standard: an)
- `position:fixed; bottom:0; z-index:50; background:#2b3a1e; padding` inkl. `env(safe-area-inset-bottom)`.
- Button „Anrufen · rund um die Uhr" (bg `#cfe36b`, Pill, `min-height:54px`), `tel:+4962017303041`.
- **Verhalten:** nur mobil (`< 1000px`) sichtbar, und **nur wenn der Hero-CTA aus dem Viewport gescrollt** ist.

---

## 4. Interaktives Verhalten (JS – in Vanilla nachzubauen)

1. **Ken-Burns** Hero-Bild: `@keyframes kenburns { from{transform:scale(1.02)} to{transform:scale(1.12) translate3d(0,-1.5%,0)} }`, `30s ease-out forwards`.
2. **Reveal-on-Scroll** (`[data-reveal]`): Start `opacity:0; transform:translateY(12px)`, Ziel `.om-in` → `opacity:1; transform:none`, `transition:opacity 1.1s ease, transform 1.1s ease`. IntersectionObserver `rootMargin:'0px 0px -6% 0px'`, `threshold:0.05`. Above-the-fold nach 60 ms sofort einblenden. Ohne JS (`html.om-nojs`) direkt sichtbar.
3. **prefers-reduced-motion:** Reveals & Animationen deaktivieren.
4. **Zitat-Slider:** Auto-Rotation 8 s, Prev/Next, Fade wie oben.
5. **Mobile-Menü:** Hamburger togglet Panel (`< 1000px`).
6. **Responsive-Umschaltung** bei `< 1000px`: Desktop-Nav aus, Hamburger an, Trust-Row als Spalte.
7. **Parallax:** Kontakt-Bild vertikal je nach Scrollposition (dezent, wie Original ≈ ±7 %).
8. **Sticky-Bar-Logik:** wie 3.8.
9. **Formular:** Submit → visuelle Bestätigung.

> Hinweis: Die Original-`onClick="{{ … }}"`/`{{ … }}`-Platzhalter und `<sc-if>`
> stammen aus der Claude-Design-Runtime und werden **nicht** übernommen, sondern
> durch echtes Astro-Markup + kleines Vanilla-JS ersetzt.

---

## 5. Inhaltsdaten (Single Source of Truth)

- **Telefon:** `06201 7303041` → `tel:+4962017303041`
- **E-Mail:** `info@tierbestattung-memoria.de`
- **Firma:** Tierbestattung Memoria
- **Inhaber:** Sarina Göck-König · Dr. Klaus Göck
- **Sitz:** Konrad-Zuse-Str. 3, 69514 Laudenbach
- **Abholadresse:** Carl-Benz-Str. 1, 64683 Einhausen

**SEO-Meta (Startseite):**
- Title: `Tierbestattung Memoria – Einzelkremierung mit Ascherückgabe in Laudenbach`
- Description: `Tierbestattung Memoria in Laudenbach: Abholung rund um die Uhr, Einzel- und Gemeinschaftskremierung, Tierurnen. Familienunternehmen. Telefon 06201 7303041.`

---

## 6. Technische Konventionen (Astro)

- **Astro statisch** (`output: 'static'`), keine SSR nötig.
- **Header/Footer/Mobile-Bar** als wiederverwendbare Komponenten in einem
  `BaseLayout`, damit sie auf **allen Seiten identisch** sind.
- Header unterstützt zwei Varianten: `overlay` (transparent über Hero, helle
  Schrift, **absolut positioniert** – Startseite) und `solid` (**weißer Balken**,
  dunkle Schrift – Unterseiten).
- **Mobiles Menü:** weißes Sheet mit Slide-Animation (max-height/opacity),
  Burger animiert zu X. Hero-Bild mobil rechtsbündig (`object-position:80% 50%`).
- Design-Tokens als CSS-Variablen in `src/styles/global.css`.
- Inhalte (Kontaktdaten, Nav, Preise, Zitate) zentral in `src/data/site.ts`.
- **Werte niemals „ungefähr" – immer die exakten `clamp()`/px/Farb-Werte oben.**
- Bilder in `public/images/`; Platzhalter klar benannt (`about-placeholder.*`,
  `contact-placeholder.*`) für späteren 1:1-Austausch.

Der detaillierte Umsetzungsplan steht in `docs/PLAN.md`.
