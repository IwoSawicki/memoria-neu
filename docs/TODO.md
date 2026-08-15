# Go-Live-Checkliste – Tierbestattung Memoria

**Stand:** Website ist fertig. Startseite (inkl. FAQ), Tierurnen & Andenken,
Impressum, Datenschutz, 404. Kontaktformular über FormSubmit ✅ funktioniert,
Fonts selbst gehostet, Umami + Google Analytics (nur mit Einwilligung),
301-Weiterleitungen der alten URLs, SEO (Sitemap/robots/OG/Schema.org),
Docker/nginx für Dokploy (Port 80).

**Domains:** Entwicklung `memoria.stolz-marketing.de` · Live
`tierbestattung-memoria.de` (ohne www; www als Backup per Redirect).

---

## 🔴 VOR dem Livegang

### 1. Inhalte freigeben (mit dem Kunden)
- [ ] **E-Mail-Adresse:** Ich habe überall auf `info@tierbestattung-memoria.de`
      vereinheitlicht (in der alten Datenschutzerklärung stand
      `memoria.tierbestattung@gmail.com`). Bitte bestätigen lassen.
- [ ] **Tierurnen-Seite gegenlesen:** Sind der **Mevisto-Link** und die
      **Online-Terminbuchung (Acuity)** noch aktuell? Stimmen Größentabelle und
      Materialien mit dem Katalog überein?
- [ ] **FAQ gegenlesen:** 8 Fragen auf der Startseite, alle aus bestehenden
      Inhalten abgeleitet. Falls etwas nicht stimmt (z. B. Preise), sagen –
      ist schnell geändert.
- [ ] **Katalog-PDF:** aktuell „Urnenkatalog Juni 2026". Austausch jederzeit
      über `public/downloads/tierurnen-katalog.pdf` (siehe README dort).

### 2. Rechtliches
- [ ] **Impressum – „MDStV":** veraltete Rechtsnorm (heute § 18 Abs. 2 MStV) und
      nur für journalistische Inhalte nötig. Modernisieren oder streichen?
      Sag Bescheid – 1 Minute Arbeit.
- [ ] **Rechtstexte anwaltlich gegenlesen lassen** (Impressum, AGB, Datenschutz).
      Besonders: FormSubmit und Google Analytics als Auftragsverarbeiter.

### 3. Technisch (am Tag des Livegangs)
- [ ] **Backup der alten Seite** ziehen.
- [ ] **Live-Domain in Dokploy** eintragen: `tierbestattung-memoria.de`, HTTPS
      aktivieren (Traefik/Let's Encrypt).
- [ ] **www anlegen** und per Redirect auf die Domain ohne www zeigen lassen.
- [ ] **DNS umstellen.**
- [ ] Prüfen, dass Dokploy vom richtigen Branch deployt
      (`claude/memoria-website-astro-s4tyzy`) – oder vorher nach `main` mergen.

---

## 🟢 NACH dem Livegang

### 1. Sofort prüfen (15 Min)
- [ ] **Weiterleitungen:** `/leistungen`, `/preise`, `/pferdekremierung`,
      `/kontakt` → Startseite · `/anfahrt` → `/impressum`.
      `/tierurnen-andenken` muss die **echte Seite** zeigen (kein Redirect).
- [ ] **Kontaktformular** auf der Live-Domain testen – kommt die Mail an?
      (Auch Spam-Ordner prüfen.)
- [ ] **Katalog-PDF** öffnen: Desktop (Vorschau) und Handy (Button).
- [ ] **Telefon-Links** auf dem Handy antippen (`tel:`).
- [ ] **Cookie-Banner:** „Akzeptieren" → Google Analytics lädt;
      „Ablehnen" → lädt nicht. Widerruf über „Cookie-Einstellungen" im Footer.
- [ ] **Umami-Dashboard** und **GA Realtime**: kommen Zugriffe an?
- [ ] HTTPS + Weiterleitung von www → ohne www prüfen.

### 2. Google Search Console (wichtig für SEO)
- [ ] Property für `tierbestattung-memoria.de` anlegen bzw. Domain bestätigen.
- [ ] **Sitemap einreichen:** `https://tierbestattung-memoria.de/sitemap-index.xml`
- [ ] Startseite + Tierurnen-Seite zur Indexierung einreichen.
- [ ] **Rich Results Test** für FAQ und LocalBusiness laufen lassen
      (search.google.com/test/rich-results).

### 3. In den ersten Wochen beobachten
- [ ] **404-Fehler** in der Search Console: Falls alte URLs auftauchen, die wir
      nicht kennen → melde sie mir, ich ergänze die Weiterleitung.
- [ ] **Rankings/Indexierung** der alten Seiten beobachten (Weiterleitungen
      sorgen dafür, dass die Stärke auf die neue Seite übergeht).
- [ ] **Lighthouse-Check** (Performance/SEO/Accessibility).
- [ ] Google-Unternehmensprofil: Website-Link prüfen (falls vorhanden).

---

## 🟢 Bereits erledigt

**Inhalt**
- [x] Startseite 1:1 nach Design (Hero, Leistungen, Über uns, Ablauf +
      Zitat-Slider, Preise, **FAQ**, Kontakt, Footer, Mobile-Anrufleiste)
- [x] **Tierurnen & Andenken** als eigene Seite mit Galerie, Größentabelle,
      Materialien, Katalog-PDF, Individualisierung und Beratungs-Abschnitt
- [x] Impressum & Datenschutz mit echten Inhalten · 404-Seite
- [x] Navigation aufgeräumt: Leistungen · Preise · Tierurnen · Über uns · Kontakt

**Funktion**
- [x] Kontaktformular über FormSubmit (mit Fallback ohne JavaScript) ✅ läuft
- [x] Umami (cookielos) + Google Analytics (nur nach Einwilligung)
- [x] Cookie-Banner mit Widerruf über den Footer
- [x] Instagram im Footer · Copyright mit automatischer Jahreszahl

**SEO**
- [x] 301-Weiterleitungen der alten URLs (mit echtem nginx getestet)
- [x] Sitemap + robots.txt · OG-Bild + Twitter-Cards
- [x] Schema.org **LocalBusiness** + **FAQPage**
- [x] Canonical-URLs · Meta-Descriptions · saubere Überschriften-Struktur

**Technik**
- [x] Google Fonts selbst gehostet (DSGVO)
- [x] Mobile: weißes Menü mit Animation, Header wird beim Öffnen weiß,
      Hero rechtsbündig, kein horizontaler Überlauf
- [x] Sicherheits-Header in nginx · Hero-Preload · optimierte WebP-Bilder
- [x] Barrierefreiheit: Alt-Texte, Bildmaße, aria-Labels, Accordion ohne JS

---

## 🟡 Optional / später

- [ ] **Dev-Domain schützen:** `memoria.stolz-marketing.de` per Basic-Auth in
      Dokploy sperren, damit sie nicht indexiert wird (Canonicals zeigen ohnehin
      auf die Live-Domain).
- [ ] **Cookie-Banner loswerden:** Wenn Umami als Statistik reicht, kann Google
      Analytics entfernt werden (`googleAnalyticsId` leeren) – dann entfällt der
      Banner komplett, weil Umami cookielos ist.
- [ ] Weitere SEO-Unterseiten (Leistungen, Preise, Pferdekremierung).
- [ ] Echte Kundenbewertungen statt der 3 Design-Zitate.
- [ ] Favicon final abstimmen.
