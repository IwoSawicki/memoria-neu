# Go-Live-Checkliste – Tierbestattung Memoria

Stand der Website: One-Pager + Impressum + Datenschutz sind gebaut, alle Bilder
eingebunden, Kontaktformular auf Web3Forms vorbereitet, Docker/nginx für Dokploy
(Port 80) vorhanden.

---

## 🔴 Muss vor Go-Live

- [ ] **Web3Forms Access Key eintragen.** Auf <https://web3forms.com> mit
  `info@tierbestattung-memoria.de` einen kostenlosen Access Key erzeugen und in
  `src/data/site.ts` bei `web3formsKey` einsetzen. Ohne echten Key wird der
  Versand blockiert und ein Hinweis angezeigt. Danach eine Testnachricht senden.
- [ ] **Domain + HTTPS in Dokploy.** Echte Domain eintragen; Traefik/Let's
  Encrypt stellt das Zertifikat automatisch aus.
- [ ] **`site`-URL setzen.** In `astro.config.mjs` `site` auf die finale Domain
  ändern (aktuell Platzhalter `https://www.tierbestattung-memoria.de`) – wichtig
  für Canonical-URLs und spätere Sitemap.
- [ ] **Deploy-Branch prüfen.** Dokploy auf den richtigen Branch zeigen lassen
  (`claude/memoria-website-astro-s4tyzy`) oder vorher nach `main` mergen.
- [ ] **Google Fonts selbst hosten (DSGVO).** Aktuell werden Fraunces + Figtree
  von `fonts.googleapis.com` geladen → IP-Übertragung an Google (USA). Für
  Rechtssicherheit + Tempo lokal einbinden (z. B. `@fontsource-variable/fraunces`
  und `@fontsource-variable/figtree`). Danach kann der Google-Fonts-Abschnitt und
  der USA-Hinweis in der Datenschutzerklärung entfallen.
- [ ] **Einwilligungs-Checkbox im Kontaktformular (DSGVO).** Checkbox „Ich habe
  die Datenschutzerklärung gelesen und stimme der Verarbeitung meiner Daten zu"
  mit Link auf `/datenschutz` ergänzen (bewusst noch nicht im 1:1-Design – bitte
  freigeben, dann baue ich sie ein).
- [ ] **Datenschutz: Web3Forms als Auftragsverarbeiter präzisieren.**
  Anbieter-Adresse + AVV ergänzen; Rechtstexte insgesamt anwaltlich prüfen lassen.
- [ ] **E-Mail-Adresse vereinheitlichen.** Impressum nennt
  `info@tierbestattung-memoria.de`, die „verantwortliche Stelle" in der
  Datenschutzerklärung nennt `memoria.tierbestattung@gmail.com` (aus der alten
  Seite übernommen). Bitte final festlegen.

## 🟡 Sollte / empfohlen

- [ ] **404-Seite** (`src/pages/404.astro`) im Markendesign gestalten.
- [ ] **Sitemap + robots.txt** für SEO (`@astrojs/sitemap`, braucht `site`).
- [ ] **Open-Graph-Bild** (`og:image`) für schöne Vorschau beim Teilen.
- [ ] **Strukturierte Daten** (Schema.org `LocalBusiness`) für lokale SEO
  (Name, Adresse, Telefon, Öffnungszeiten/„24 h").
- [ ] **Favicon final** – aktuell schlichtes „M" auf Dunkelgrün.
- [ ] **Lighthouse/Performance-Check** nach dem ersten Deploy.

## 🟢 Optional / später

- [ ] **Unbenutzte Original-PNGs entfernen.** `memoria-herobild.png`,
  `pasted-1785311187667-0.png`, `Memoria-Kontaktbild.png` liegen als Quelle in
  `public/images/`, ausgeliefert werden nur die optimierten `.webp`. Können raus,
  um den Deploy schlank zu halten (auf Wunsch mache ich das).
- [ ] **Weitere Unterseiten** (Leistungen, Preise, Tierurnen, Pferdekremierung)
  als eigene SEO-Seiten – wie in der alten Navigation.
- [ ] **Analytics** (falls gewünscht, DSGVO-konform, z. B. Plausible).
- [ ] **Echte Testimonials/Bewertungen** ergänzen.

---

### Schnell startklar
Das absolute Minimum für einen sinnvollen Live-Gang: **Web3Forms-Key**, **Domain
+ HTTPS**, **`site`-URL** und die **DSGVO-Punkte (Fonts selbst hosten +
Einwilligungs-Checkbox)**. Der Rest kann iterativ folgen.
