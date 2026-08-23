# Go-Live: DNS-Umstellung ohne E-Mail-Ausfall

> Die Werte unten habe ich am Tag der Erstellung **live per DNS-Abfrage
> ausgelesen** – das ist der echte Ist-Zustand, keine Vermutung.

---

## Ist-Zustand

| Eintrag | Aktueller Wert | Wer? |
|---|---|---|
| **Nameserver** | `ns14.wixdns.net`, `ns15.wixdns.net` | **Wix verwaltet die komplette DNS-Zone** |
| **A** `@` | `185.230.63.107`, `185.230.63.186`, `185.230.63.171` | Wix-Webserver |
| **CNAME** `www` | `cdn3.wixdns.net` | Wix-CDN |
| **MX** `@` | `5 smtpin.rzone.de` | **Strato** (dort liegen die E-Mails) |
| **TXT / SPF** | *nicht vorhanden* | – |
| **DMARC** | *nicht vorhanden* | – |

---

## ⚠️ Die eine Gefahr, die du kennen musst

**Die E-Mails liegen bei Strato – aber der MX-Eintrag, der dorthin zeigt, liegt
in der DNS-Zone von Wix.**

Das heißt:

> Sobald die Wix-Zone verschwindet (Kündigung) oder die Nameserver umgestellt
> werden, **ohne dass der MX-Eintrag vorher woanders neu angelegt wurde**,
> ist der Mailempfang sofort tot. Die Postfächer bei Strato bleiben zwar
> bestehen, aber niemand findet sie mehr.

Daraus folgt die wichtigste Regel:

> ### 🚫 Wix NIEMALS kündigen, solange die Nameserver noch auf `wixdns.net` zeigen.

---

## Empfohlenes Vorgehen: in zwei Schritten

Ich rate ausdrücklich davon ab, Livegang und DNS-Umzug gleichzeitig zu machen.
Getrennt ist jeder Schritt einzeln rückgängig zu machen.

### Schritt 1 – Livegang (heute): nur A- und www-Eintrag ändern

DNS **bleibt vorerst bei Wix**. Du fasst nur die zwei Website-Einträge an,
alles rund um E-Mail bleibt unberührt.

- [ ] **IP-Adresse des Dokploy-Servers notieren** (die brauchst du gleich).
- [ ] **Alles dokumentieren:** In der Wix-DNS-Verwaltung von *jedem* Eintrag
      einen Screenshot machen. Auch von denen, die du nicht anfasst.
- [ ] *(Optional)* TTL auf 300 Sekunden senken und 1–2 Stunden warten –
      dann greift ein eventueller Rollback schneller.
- [ ] **Domain in Wix von der Website „trennen"** (nicht löschen!), damit Wix
      die A-Einträge nicht wieder überschreibt.
- [ ] **A-Eintrag `@`** ändern: die drei `185.230.63.*` löschen,
      stattdessen die **Dokploy-IP** eintragen.
- [ ] **`www`**: den CNAME `cdn3.wixdns.net` entfernen und stattdessen
      `www` ebenfalls auf die **Dokploy-IP** zeigen lassen (A-Eintrag).
      → In Dokploy ist `www` bereits als Weiterleitung auf die Domain ohne
      `www` eingerichtet. **Das ist wichtig:** Alle bei Google indexierten
      URLs laufen auf `www.`.
- [ ] **MX-Eintrag `5 smtpin.rzone.de` NICHT anfassen.**
- [ ] Warten (meist 15–60 Min, laut TTL bis zu 1 Std.)

### Schritt 2 – DNS zu Strato umziehen (später, in Ruhe)

Erst wenn die Website stabil läuft. **Voraussetzung für die Wix-Kündigung.**

- [ ] **Zuerst klären: Wo ist die Domain registriert?**
      Bei Strato im Kundenbereich unter „Domainverwaltung" nachsehen.
      - *Steht sie dort* → super, du kannst die Nameserver direkt ändern.
      - *Steht sie dort nicht* → sie liegt bei Wix und muss **zuerst zu Strato
        transferiert** werden (Auth-Code bei Wix anfordern). Das dauert einige
        Tage – **vor** der Kündigung erledigen.
- [ ] **Bei Strato die DNS-Zone vorbereiten**, bevor die Nameserver wechseln:
      | Typ | Name | Wert |
      |---|---|---|
      | A | `@` | Dokploy-IP |
      | A | `www` | Dokploy-IP |
      | **MX** | `@` | **`smtpin.rzone.de`, Priorität 5** |
- [ ] **Nameserver auf Strato umstellen.**
- [ ] 24–48 Std. warten und prüfen (siehe unten).
- [ ] **Erst danach Wix kündigen.**

---

## Nach jedem Schritt prüfen

Im Terminal (Mac) bzw. der Eingabeaufforderung:

```bash
# Zeigt die Domain auf den neuen Server?
dig +short tierbestattung-memoria.de A
dig +short www.tierbestattung-memoria.de

# ← DAS IST DER WICHTIGE: muss IMMER "5 smtpin.rzone.de" liefern
dig +short tierbestattung-memoria.de MX

# Wer verwaltet die Zone gerade?
dig +short tierbestattung-memoria.de NS
```

Zusätzlich:
- [ ] **Test-E-Mail von außen** an `info@tierbestattung-memoria.de` schicken
      (z. B. von einer privaten Gmail-Adresse) – **kommt sie an?**
- [ ] **Test-E-Mail nach außen** senden.
- [ ] Website über `https://tierbestattung-memoria.de` **und**
      `https://www.tierbestattung-memoria.de` aufrufen.
- [ ] HTTPS-Zertifikat gültig (Schloss im Browser)?
- [ ] Alte URLs testen: `/leistungen`, `/preise`, `/kontakt`,
      `/pferdekremierung` → Startseite; `/anfahrt` → Impressum.
- [ ] Kontaktformular absenden – kommt die Mail an?

---

## Notfall-Rollback

Solange DNS bei Wix liegt (Schritt 1), ist der Rückweg einfach:
A-Einträge wieder auf `185.230.63.107`, `185.230.63.186`, `185.230.63.171`
setzen und `www` zurück auf `cdn3.wixdns.net`. Deshalb vorher die Screenshots.

---

## Nebenbefund: SPF und DMARC fehlen

Die Domain hat **keinen SPF-Eintrag**. Das bedeutet: Jeder kann E-Mails im Namen
von `tierbestattung-memoria.de` fälschen, und eure eigenen Mails landen bei
Gmail & Co. schneller im Spam.

Das ist unabhängig vom Umzug – aber wenn ohnehin an der DNS-Zone gearbeitet
wird, ist es der ideale Moment. **Bitte den korrekten Wert bei Strato erfragen**
(üblicherweise etwas wie `v=spf1 include:_spf.strato.de ~all`) – ich rate hier
nichts, ein falscher SPF-Eintrag kann Mails blockieren.

Später optional zusätzlich: DKIM (bei Strato aktivierbar) und ein
DMARC-Eintrag.

---

## Reihenfolge in einem Satz

**Website umstellen → prüfen, dass Mails laufen → DNS zu Strato umziehen →
nochmal prüfen → dann erst Wix kündigen.**
