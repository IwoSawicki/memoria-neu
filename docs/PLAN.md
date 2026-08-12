# Bauplan – Memoria Website (Astro)

Ziel: Das Design aus `docs/design-reference/Designvorschlag_2.dc.html` **1:1** in
Astro nachbauen. Alle exakten Werte stehen in `CLAUDE.md`. Dieser Plan beschreibt
**wie** wir bauen. Nach deinem **„Go"** wird alles unten in einem Durchgang
umgesetzt, committet und gepusht.

---

## Phase 0 – Vorbereitung (bereits erledigt ✅)
- [x] Design-Export analysiert (alle Sektionen, Farben, Fonts, Verhalten).
- [x] Offene Punkte mit Kunde geklärt (Bilder, Styling, Formular, Unterseiten).
- [x] Hero-Bild extrahiert → `public/images/hero.webp`.
- [x] Original-Export als Referenz gesichert → `docs/design-reference/`.
- [x] `CLAUDE.md` mit allen exakten Vorgaben erstellt.

## Phase 1 – Projekt-Setup
- [ ] Astro-Projekt initialisieren (`npm create astro` minimal, statisch).
- [ ] `astro.config.mjs` (`output:'static'`, `site`-URL Platzhalter).
- [ ] `tsconfig.json`, `.gitignore` (node_modules, dist, .astro).
- [ ] `package.json` Scripts: `dev`, `build`, `preview`.
- [ ] Ordnerstruktur anlegen (siehe unten).

## Phase 2 – Fundament (Tokens, Fonts, Layout)
- [ ] `src/styles/global.css`: Reset, Body-Basis, **alle Farb-/Font-Tokens als
      CSS-Variablen**, `@keyframes kenburns`, `[data-reveal]`-Regeln,
      `prefers-reduced-motion`, `scroll-behavior`, Link-Farben.
- [ ] Google Fonts (Fraunces + Figtree) mit `preconnect` + exakter URL.
- [ ] `src/layouts/BaseLayout.astro`: `<html lang="de">`, `<head>` (Meta/SEO als
      Props), Font-Links, global.css, `<slot/>`, Header (Variante wählbar),
      Footer, Mobile-Sticky-Bar. Lädt das UI-Script.
- [ ] `src/data/site.ts`: Kontaktdaten, Nav-Links, Preistabellen, Zitate,
      Trust-Punkte, Ablauf-Schritte, Leistungen – als typisierte Datenquelle.

## Phase 3 – Gemeinsame Komponenten (auf allen Seiten gleich)
- [ ] `Header.astro` – Logo, Desktop-Nav, Telefon-Button, Hamburger, Mobil-Panel.
      Prop `variant: 'overlay' | 'solid'`.
- [ ] `Footer.astro` – kompletter Footer inkl. großer Telefon-/E-Mail-Zeile,
      3-Spalten-Block, untere Leiste (Impressum/Datenschutz verlinkt).
- [ ] `MobileStickyBar.astro` – fixe Anruf-Leiste (mobil, scroll-abhängig).

## Phase 4 – Startseiten-Sektionen (`src/pages/index.astro`)
Jede Sektion als eigene Komponente, exakte Werte aus `CLAUDE.md §3`:
- [ ] `Hero.astro` (`#top`) – Bild + Overlay + Eyebrow/H1/Zitat/CTA + Trust-Row.
- [ ] `Leistungen.astro` (`#leistungen`) – Chevron, H2 mit Scribble-Underline,
      Intro, 3 Karten, Kursiv-Notiz.
- [ ] `UeberUns.astro` (`#ueber-uns`) – Bild-Platzhalter + Text + Outline-Button.
- [ ] `Ablauf.astro` (`#ablauf`) – 4 Schritte + `TestimonialSlider`.
- [ ] `TestimonialSlider.astro` – Markup für Zitat-Slider (Logik im UI-Script).
- [ ] `Preise.astro` (`#preise`) – 2 Preistabellen + Hinweise (Toggle-fähig).
- [ ] `Kontakt.astro` (`#kontakt`) – Parallax-Platzhalter + Overlay + Formular.
- [ ] `index.astro` – setzt die Sektionen in DOM-Reihenfolge zusammen,
      Header-Variante `overlay`, SEO-Meta aus `CLAUDE.md §5`.

## Phase 5 – Interaktivität (`src/scripts/ui.ts`)
Vanilla-JS, ein Modul, als `<script>` eingebunden:
- [ ] Reveal-on-Scroll (IntersectionObserver, exakte Parameter).
- [ ] Mobile-Menü Toggle + Responsive-Umschaltung `< 1000px`.
- [ ] Zitat-Slider (Auto 8 s, Prev/Next, Fade 0.9 s / Swap 500 ms).
- [ ] Parallax Kontakt-Bild.
- [ ] Sticky-Bar-Logik (abhängig von Hero-CTA-Sichtbarkeit).
- [ ] Formular-Submit → visuelle Bestätigung.
- [ ] `html.om-nojs`-Fallback entfernen bei aktivem JS.

## Phase 6 – Unterseiten (Struktur, Inhalt später)
- [ ] `src/pages/impressum.astro` – BaseLayout, Header `solid`, Platzhalter-Inhalt.
- [ ] `src/pages/datenschutz.astro` – analog.
- [ ] Footer-Links auf `/impressum` und `/datenschutz` verweisen.

## Phase 7 – Platzhalterbilder
- [ ] `about-placeholder` (Seitenverhältnis 4:5) und `contact-placeholder`
      (Full-Bleed) als dezente, stilkonforme Platzhalter erzeugen
      (Farbfläche `#e6eecd`/`#141a0e` + Hinweislabel). Später 1:1 austauschbar.

## Phase 8 – Qualitätssicherung
- [ ] `npm run build` fehlerfrei.
- [ ] Visueller Abgleich gegen den Original-Export (Desktop + Mobil):
      Farben, Fonts, Abstände, Rundungen, Breakpoints, Animationen.
- [ ] Reduced-Motion prüfen. Links/`tel:`/`mailto:` prüfen.
- [ ] Commit(s) mit klaren Messages, Push auf `claude/memoria-website-astro-s4tyzy`.

---

## Zielstruktur
```
memoria-neu/
├─ CLAUDE.md
├─ astro.config.mjs · package.json · tsconfig.json · .gitignore
├─ docs/
│  ├─ PLAN.md
│  └─ design-reference/Designvorschlag_2.dc.html
├─ public/images/  (hero.webp, *-placeholder.*)
└─ src/
   ├─ styles/global.css
   ├─ layouts/BaseLayout.astro
   ├─ data/site.ts
   ├─ scripts/ui.ts
   ├─ components/ Header · Footer · MobileStickyBar · Hero · Leistungen ·
   │              UeberUns · Ablauf · TestimonialSlider · Preise · Kontakt
   └─ pages/ index.astro · impressum.astro · datenschutz.astro
```

## Prinzipien
1. **Exaktheit vor Bequemlichkeit** – nie „ungefähr", immer die Werte aus `CLAUDE.md`.
2. **Header/Footer identisch** auf allen Seiten (eine Quelle).
3. **Wartbar & SEO-bereit** – Tokens, zentrale Daten, semantisches HTML.
4. **Unklarheiten → nachfragen**, nicht raten.

---

## Nächster Schritt
👉 Sobald du **„Go"** gibst, setze ich Phase 1–8 in einem Durchgang um,
committe sauber und pushe auf `claude/memoria-website-astro-s4tyzy`.
```
