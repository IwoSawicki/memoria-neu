# Branches & Umgebungen

| Branch | Umgebung | Domain | Indexierung |
|---|---|---|---|
| `main` | **Live** | `www.tierbestattung-memoria.de` | ✅ erlaubt |
| `dev` | **Test** | `memoria.stolz-marketing.de` | 🚫 gesperrt |

## Arbeitsweise

```
dev  ──►  testen auf der Subdomain  ──►  merge  ──►  main  ──►  live
```

1. Änderungen **immer auf `dev`** committen.
2. Dokploy baut die Dev-App automatisch → auf `memoria.stolz-marketing.de` prüfen.
3. Passt alles? → `dev` in `main` mergen → Dokploy deployt live.

```bash
# Änderung auf dev
git checkout dev
# ... arbeiten, committen ...
git push origin dev

# Wenn es passt: live nehmen
git checkout main
git merge dev
git push origin main
```

## Dokploy-Einstellungen

**Live-App**
- Branch: `main`
- Domains: `www.tierbestattung-memoria.de` (+ `tierbestattung-memoria.de`)
- Environment: *(keine SITE_URL nötig – Standard ist die Live-Domain)*

**Dev-App**
- Branch: `dev`
- Domain: `memoria.stolz-marketing.de`
- Environment: **`SITE_URL=https://memoria.stolz-marketing.de`**

> ⚠️ Die Variable `SITE_URL` auf der Dev-App ist wichtig. Sie sorgt dafür, dass
> Canonical-URLs, Sitemap und Open Graph auf die Dev-Domain zeigen – **und**
> dass die Seite für Suchmaschinen gesperrt wird.

## Schutz gegen doppelte Inhalte

Ohne Absicherung wäre die Testseite eine vollständige Kopie der Live-Seite –
Google könnte sie indexieren und beide würden gegeneinander konkurrieren.
Deshalb ist eingebaut:

- **`<meta name="robots" content="noindex, nofollow">`** auf allen Seiten,
  sobald die Domain **nicht** `www.tierbestattung-memoria.de` ist
- **`robots.txt`** liefert auf allen Nicht-Live-Umgebungen `Disallow: /`

Beides greift automatisch anhand der Domain – es kann nicht vergessen werden.

## Einmalig auf GitHub einstellen

**Settings → General → Default branch → `main`**

Damit landen neue Pull Requests standardmäßig auf `main` und nicht auf dem
alten Arbeitsbranch.


## Nach jedem Deploy prüfen

```bash
./scripts/check-live.sh
```

Prüft in einem Durchlauf: Erreichbarkeit aller Seiten, die Weiterleitung von
ohne-www auf www, die alten URLs, Zertifikate für **beide** Hostnamen und ob
`robots.txt`/`noindex` versehentlich die Live-Seite sperren.

> **Wichtig:** Beide Domains müssen in Dokploy eingetragen sein – auch die, die
> nur weiterleitet. Traefik reicht eine Anfrage nur dann an den Container
> weiter, wenn es für den Hostnamen einen Router kennt. Fehlt der Eintrag,
> antwortet Traefik mit 404 und die Weiterleitung in nginx wird nie erreicht.
