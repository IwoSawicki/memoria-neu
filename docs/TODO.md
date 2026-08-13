# Go-Live-Checkliste – Tierbestattung Memoria

Website-Stand: One-Pager + Impressum + Datenschutz + 404, alle Bilder
eingebunden, Kontaktformular über FormSubmit.co, Fonts selbst gehostet,
Cookie-Banner + Google-Analytics-Vorbereitung, SEO (Sitemap/robots/OG/Schema.org),
Docker/nginx für Dokploy (Port 80).

**Domains:** Entwicklung `memoria.stolz-marketing.de` · Live `tierbestattung-memoria.de`
(ohne www; www als Backup per Redirect).

---

## 🔴 Was DU noch tun musst (bis live)

- [ ] **Kontaktformular aktivieren (FormSubmit).** Einmalig eine Testnachricht
  über das Formular senden → FormSubmit schickt eine **Aktivierungs-Mail** an
  `info@tierbestattung-memoria.de` → Link darin bestätigen. Fertig, kein Key.
  (Optional gegen Spam: den von FormSubmit erzeugten **Hash** statt der
  Klartext-Adresse in `src/data/site.ts` → `formsubmitTarget` eintragen.)
- [ ] **Google Analytics aktivieren (optional).** GA4-Mess-ID (`G-XXXXXXXXXX`) in
  `src/data/site.ts` → `googleAnalyticsId` eintragen. Erst dann erscheinen
  Cookie-Banner + Analytics (Analytics lädt nur nach „Akzeptieren").
- [ ] **Live-Domain + HTTPS in Dokploy** eintragen (`tierbestattung-memoria.de`);
  www-Domain als Redirect auf die Hauptdomain.
- [ ] **E-Mail final bestätigen.** Ich habe überall auf
  `info@tierbestattung-memoria.de` vereinheitlicht – bitte beim Kunden gegenprüfen.
- [ ] **Rechtstexte final freigeben** (siehe Prüf-Notizen unten), idealerweise
  anwaltlich gegenlesen.

## 📋 Rechtstext-Prüfung (Notizen)

- **Impressum:** vollständig für § 5 DDG (Firma, GF, Anschrift, Kontakt,
  Registergericht/HRB, USt-IdNr, Zulassungsnummer). Ergänzt:
  Verbraucherstreitbeilegungs-Hinweis.
  - Hinweis: „Inhaltlich Verantwortlicher gemäß **MDStV**" ist eine veraltete
    Rechtsnorm (heute § 18 Abs. 2 **MStV**) und nur für journalistische Inhalte
    nötig – kann modernisiert oder entfernt werden. Bitte entscheiden.
  - Die **EU-OS-Plattform** (Online-Streitbeilegung) wurde 2025 eingestellt –
    daher **kein** Link darauf mehr (bewusst weggelassen).
- **Datenschutz:** an die neue Seite angepasst (Hetzner-Hosting, FormSubmit,
  Google Analytics einwilligungsbasiert, Fonts lokal, KI-Telefonassistent).
  - Offen: **FormSubmit** und **Google Analytics** als Auftragsverarbeiter ggf.
    mit Anbieter-Anschrift / AVV präzisieren (juristisch prüfen).
- **AGB:** bewusst knapp (§1–§4 wie geliefert) – inhaltlich Sache des Kunden.

## 🟢 Erledigt

- [x] Kontaktformular auf **FormSubmit.co** umgestellt (AJAX, Bestätigung inline,
  Honeypot).
- [x] **Cookie-Banner** (dezent, unten links) + **Google-Analytics-Einbindung**
  nur nach Einwilligung; Widerruf über „Cookie-Einstellungen" im Footer.
- [x] **E-Mail** überall auf `info@` vereinheitlicht.
- [x] Google Fonts selbst gehostet · 404-Seite · Sitemap/robots · OG-Bild ·
  Schema.org LocalBusiness · `site`-URL (Live-Domain, Dev per `SITE_URL`-Env).

## 🟡 Optional / später

- [ ] Dev-Domain nicht indexieren (Basic-Auth in Dokploy oder
  `SITE_URL=https://memoria.stolz-marketing.de` setzen).
- [ ] Unbenutzte Original-PNGs entfernen (nur die `.webp` werden ausgeliefert).
- [ ] Weitere SEO-Unterseiten (Leistungen, Preise, Tierurnen, Pferdekremierung).
- [ ] Favicon final · Lighthouse-Check nach Deploy.
