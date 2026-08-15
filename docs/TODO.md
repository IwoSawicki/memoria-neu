# Go-Live-Checkliste – Tierbestattung Memoria

**Stand:** Website ist fertig gebaut und getestet. One-Pager + Impressum +
Datenschutz + 404, alle Bilder eingebunden, Kontaktformular über FormSubmit.co,
Fonts selbst gehostet, Umami-Analytics aktiv, 301-Weiterleitungen der alten URLs,
SEO (Sitemap/robots/OG/Schema.org), Docker/nginx für Dokploy (Port 80).

**Domains:** Entwicklung `memoria.stolz-marketing.de` · Live
`tierbestattung-memoria.de` (ohne www; www als Backup per Redirect).

---

## 🔴 Was DU noch machen musst

### 1. Kontaktformular aktivieren (5 Min) ⚠️ WICHTIG
Das Formular meldete zuletzt einen Fehler – Ursache: **FormSubmit muss einmalig
aktiviert werden**, und die Aktivierungs-Mail wird nur beim *klassischen*
Versand verschickt (nicht über den AJAX-Weg). Ich habe das Formular deshalb so
umgebaut, dass es bei einem Fehler automatisch klassisch absendet.

**So aktivierst du es:**
1. Auf der Website das Formular ausfüllen und absenden.
2. Du landest kurz auf einer FormSubmit-Seite → dort wird die Aktivierung
   angestoßen.
3. In `info@tierbestattung-memoria.de` die **Aktivierungs-Mail** öffnen und den
   Link anklicken (auch Spam-Ordner prüfen!).
4. Danach noch einmal testen – ab jetzt läuft der Versand direkt auf der Seite,
   ohne Weiterleitung.

- *Optional gegen Spam:* FormSubmit erzeugt einen **Hash** für deine Adresse.
  Diesen statt der Klartext-Adresse in `src/data/site.ts` → `formsubmitTarget`
  eintragen (dann steht die E-Mail nicht im Quelltext).

### 2. Domain live schalten
- Live-Domain `tierbestattung-memoria.de` in Dokploy eintragen, HTTPS aktivieren
  (Traefik/Let's Encrypt macht das Zertifikat automatisch).
- `www.tierbestattung-memoria.de` anlegen und **per Redirect** auf die
  Hauptdomain ohne www zeigen lassen.
- DNS umstellen. **Vorher ein Backup der alten Seite ziehen.**

### 3. Nach dem Livegang prüfen (10 Min)
- [ ] Weiterleitungen testen: `/leistungen`, `/preise`, `/pferdekremierung`,
      `/kontakt` → Startseite · `/anfahrt` → `/impressum` (als 301 eingerichtet
      und lokal getestet). **`/tierurnen-andenken` ist jetzt eine echte
      Unterseite** und bleibt unter derselben URL wie bisher erhalten.
- [ ] Katalog-PDF öffnen und Anzeige prüfen (Desktop + Handy).
- [ ] Formular abschicken und Mail-Zustellung prüfen.
- [ ] Telefon-Links auf dem Handy testen (`tel:`-Links).
- [ ] Umami-Dashboard: Kommen Zugriffe an?

### 4. Google Search Console
- [ ] Property für `tierbestattung-memoria.de` anlegen (falls noch nicht da).
- [ ] **Sitemap einreichen:** `https://tierbestattung-memoria.de/sitemap-index.xml`
- [ ] Startseite zur neuen Indexierung einreichen.
- [ ] In den Folgewochen auf 404-Fehler schauen (falls alte URLs fehlen, die wir
      nicht kennen – dann melde sie mir, ich ergänze die Weiterleitung).

### 5. Inhaltliche Entscheidungen
- [ ] **E-Mail bestätigen:** Ich habe überall auf `info@tierbestattung-memoria.de`
      vereinheitlicht (vorher stand in der alten Datenschutzerklärung
      `memoria.tierbestattung@gmail.com`). Bitte beim Kunden gegenprüfen.
- [ ] **Impressum – „MDStV":** veraltete Rechtsnorm (heute § 18 Abs. 2 MStV) und
      nur für journalistische Inhalte nötig. Soll ich das modernisieren oder
      streichen? Sag Bescheid, ist in 1 Minute geändert.
- [ ] **Rechtstexte anwaltlich gegenlesen lassen** (Impressum/AGB/Datenschutz).
- [ ] **Tierurnen-Seite gegenlesen:** Inhalte wurden von der alten Seite
      übernommen (Katalog-Hinweise, Pfotenabdruck-Hinweis, Folienbeschriftung,
      Mevisto-Partner, Online-Terminbuchung). Bitte prüfen, ob alles noch aktuell
      ist – besonders der Mevisto-Link und die Terminbuchung.

---

## 🟢 Bereits erledigt (von mir)

**Inhalt & Funktion**
- [x] Komplette Startseite 1:1 nach Design (Hero, Leistungen, Über uns, Ablauf +
      Zitat-Slider, Preise, Kontakt, Footer, Mobile-Anrufleiste)
- [x] Impressum & Datenschutz mit echten Inhalten · 404-Seite im Markendesign
- [x] Kontaktformular über **FormSubmit.co** (AJAX, Bestätigung inline, Honeypot)
- [x] **Umami**-Analytics eingebunden (cookielos → **kein Cookie-Banner nötig**)
- [x] Cookie-Banner liegt bereit, falls du später Google Analytics willst
      (erscheint automatisch, sobald `googleAnalyticsId` gesetzt ist; GA lädt nur
      nach Einwilligung)
- [x] Instagram im Footer · Copyright mit automatischer Jahreszahl

**SEO**
- [x] **301-Weiterleitungen** aller alten URLs (real mit nginx getestet)
- [x] Sitemap + robots.txt · OG-Bild (Frau + Hund) + Twitter-Cards
- [x] Schema.org LocalBusiness (Adresse, Telefon, 24/7, Inhaber, Instagram)
- [x] Canonical-URLs · Meta-Description · saubere Überschriften-Struktur (1× h1)

**Technik & Qualität**
- [x] Google Fonts **selbst gehostet** (DSGVO – keine Verbindung zu Google)
- [x] Mobile-Fixes: weißes Menü mit Animation, Header wird beim Öffnen weiß,
      Hero rechtsbündig, kein horizontaler Überlauf
- [x] Weißer Header auf Unterseiten
- [x] Sicherheits-Header in nginx (nosniff, Frame-Options, Referrer-Policy)
- [x] Auslieferungsgröße von 6,2 MB auf **1,1 MB** reduziert (Original-PNGs nach
      `assets/originals/` verschoben, nur optimierte WebP werden ausgeliefert)
- [x] Hero-Bild-Preload für schnelleren Bildaufbau (LCP)
- [x] Barrierefreiheit: Alt-Texte, Bildmaße, aria-Labels im Formular

---

## 🟡 Später / optional

- [ ] Weitere SEO-Unterseiten (Leistungen, Preise, Pferdekremierung als eigene
      Seiten – aktuell alles auf der Startseite + Weiterleitungen).
- [ ] Dev-Domain `memoria.stolz-marketing.de` vor Indexierung schützen
      (Basic-Auth in Dokploy) – die Canonicals zeigen ohnehin auf die Live-Domain.
- [ ] Echte Kundenbewertungen ergänzen (aktuell die 3 Zitate aus dem Design).
- [ ] Favicon final abstimmen (aktuell schlichtes „M" auf Dunkelgrün).
- [ ] Lighthouse-Check nach dem Deploy.
