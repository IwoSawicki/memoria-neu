# Go-Live-Checkliste – Tierbestattung Memoria

Website-Stand: One-Pager + Impressum + Datenschutz + 404, alle Bilder
eingebunden, Kontaktformular über Web3Forms, Fonts selbst gehostet, SEO
(Sitemap/robots/OG/Schema.org), Docker/nginx für Dokploy (Port 80).

**Domains:** Entwicklung `memoria.stolz-marketing.de` · Live später
`tierbestattung-memoria.de`.

---

## 🔴 Muss vor Go-Live

- [ ] **Web3Forms Access Key eintragen.** Auf <https://web3forms.com> die
  E-Mail `info@tierbestattung-memoria.de` eingeben → Key kommt per Mail → in
  `src/data/site.ts` bei `web3formsKey` einsetzen. Danach Testnachricht senden.
- [ ] **Domain + HTTPS in Dokploy.** Für die Live-Domain
  `tierbestattung-memoria.de` eintragen; Traefik/Let's Encrypt macht das
  Zertifikat automatisch.
- [ ] **www vs. ohne www festlegen.** Aktuell ist die Live-Domain **ohne www**
  gesetzt (`tierbestattung-memoria.de`). Eine Variante als Hauptdomain wählen und
  die andere per Redirect darauf weiterleiten (in Dokploy/DNS). Die alte Seite
  lief auf `www.` – bitte final entscheiden.
- [ ] **E-Mail-Adresse vereinheitlichen.** Impressum nennt
  `info@tierbestattung-memoria.de`, die „verantwortliche Stelle" in der
  Datenschutzerklärung nennt `memoria.tierbestattung@gmail.com` (aus der alten
  Seite). Bitte final festlegen.
- [ ] **Rechtstexte prüfen (lassen).** Impressum/AGB/Datenschutz inhaltlich
  gegenlesen; Web3Forms als Auftragsverarbeiter ggf. mit Anbieteradresse/AVV
  präzisieren.

## 🟢 Erledigt

- [x] **Google Fonts selbst hosten** (Fraunces + Figtree via `@fontsource-variable`,
  keine Verbindung zu Google mehr; Datenschutzerklärung entsprechend angepasst).
- [x] **Datenschutz-Hinweis am Kontaktformular** (mit Link statt harter Checkbox –
  auf Wunsch in 1 Zeile auf Pflicht-Checkbox umstellbar).
- [x] **404-Seite** im Markendesign (`src/pages/404.astro`, nginx `error_page`).
- [x] **Sitemap + robots.txt** (`@astrojs/sitemap`, `/`, `/impressum/`,
  `/datenschutz/`).
- [x] **Open-Graph-Bild** (Frau + Hund, 1200×630, `public/images/og.jpg`) inkl.
  OG-/Twitter-Meta-Tags.
- [x] **Schema.org LocalBusiness** (JSON-LD auf der Startseite: Adresse, Telefon,
  Öffnungszeiten 24/7, Inhaber, Instagram).
- [x] **`site`-URL gesetzt** (Live-Domain als Standard; Dev-Domain per
  `SITE_URL`-Env in Dokploy überschreibbar).

## 🟡 Optional / später

- [ ] **Dev-Domain nicht indexieren.** Für `memoria.stolz-marketing.de` in Dokploy
  optional Basic-Auth aktivieren oder `SITE_URL=https://memoria.stolz-marketing.de`
  setzen (dann zeigen Canonicals auf die Dev-Domain). Standard: Canonicals zeigen
  auf die Live-Domain – Suchmaschinen konsolidieren dorthin.
- [ ] **Unbenutzte Original-PNGs entfernen** (`memoria-herobild.png`,
  `pasted-1785311187667-0.png`, `Memoria-Kontaktbild.png`) – ausgeliefert werden
  nur die `.webp`.
- [ ] **Weitere SEO-Unterseiten** (Leistungen, Preise, Tierurnen, Pferdekremierung).
- [ ] **Analytics** (falls gewünscht, DSGVO-konform, z. B. Plausible).
- [ ] **Favicon final** abstimmen · **Lighthouse-Check** nach dem Deploy.

---

### Kürzester Weg live
Nur noch: **Web3Forms-Key** + **Live-Domain in Dokploy** (mit HTTPS) + **www-Frage
+ E-Mail final** + **Rechtstext-Gegenlesen**. Der Rest ist optional.
