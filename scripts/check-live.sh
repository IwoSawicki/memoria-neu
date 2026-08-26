#!/usr/bin/env bash
# Prüft die Live-Seite auf die Fehler, die beim Deployen am ehesten passieren.
# Aufruf:  ./scripts/check-live.sh
set -uo pipefail

WWW="https://www.tierbestattung-memoria.de"
BARE="https://tierbestattung-memoria.de"
ok=0; fail=0

chk() { # chk "Beschreibung" "erwartet" "tatsächlich"
  if [ "$2" = "$3" ]; then printf "  ✅ %-52s %s\n" "$1" "$3"; ok=$((ok+1))
  else printf "  ❌ %-52s %s (erwartet: %s)\n" "$1" "$3" "$2"; fail=$((fail+1)); fi
}

code() { curl -s -o /dev/null -w '%{http_code}' --max-time 15 "$1"; }
loc()  { curl -sI --max-time 15 "$1" | grep -i '^location:' | tr -d '\r' | awk '{print $2}'; }

echo "── Erreichbarkeit ─────────────────────────────────────────────────"
chk "www liefert die Seite aus"            "200" "$(code $WWW/)"
chk "Unterseite Tierurnen"                 "200" "$(code $WWW/tierurnen-andenken/)"
chk "Impressum"                            "200" "$(code $WWW/impressum/)"
chk "Katalog-PDF"                          "200" "$(code $WWW/downloads/tierurnen-katalog.pdf)"

echo "── Weiterleitung ohne www ─────────────────────────────────────────"
chk "ohne www antwortet mit 301"           "301" "$(code $BARE/)"
chk "ohne www zeigt auf www"               "$WWW/" "$(loc $BARE/)"

echo "── Alte URLs (SEO) ────────────────────────────────────────────────"
for p in leistungen preise pferdekremierung kontakt; do
  chk "/$p leitet auf die Startseite"      "$WWW/" "$(loc $WWW/$p)"
done
chk "/anfahrt leitet aufs Impressum"       "$WWW/impressum" "$(loc $WWW/anfahrt)"

echo "── Indexierung (fängt eine falsche SITE_URL ab) ───────────────────"
rob=$(curl -s --max-time 15 $WWW/robots.txt | head -3 | tr -d '\r' | tr '\n' ' ')
case "$rob" in
  *Disallow:\ /*) printf "  ❌ %-52s %s\n" "robots.txt sperrt die Seite!" "$rob"; fail=$((fail+1));;
  *Allow:\ /*)    printf "  ✅ %-52s\n" "robots.txt erlaubt Indexierung"; ok=$((ok+1));;
  *)              printf "  ⚠️  %-52s %s\n" "robots.txt unerwartet" "$rob";;
esac
if curl -s --max-time 15 $WWW/ | grep -q 'name="robots" content="noindex'; then
  printf "  ❌ %-52s\n" "Startseite hat noindex!"; fail=$((fail+1))
else
  printf "  ✅ %-52s\n" "Startseite ohne noindex"; ok=$((ok+1))
fi
chk "Sitemap erreichbar"                   "200" "$(code $WWW/sitemap-index.xml)"

echo "── Zertifikate ────────────────────────────────────────────────────"
for h in www.tierbestattung-memoria.de tierbestattung-memoria.de; do
  iss=$(echo | openssl s_client -connect $h:443 -servername $h 2>/dev/null \
        | openssl x509 -noout -issuer 2>/dev/null | sed 's/.*O = //;s/,.*//')
  if [ -n "$iss" ]; then printf "  ✅ %-52s %s\n" "Zertifikat $h" "$iss"; ok=$((ok+1))
  else printf "  ❌ %-52s %s\n" "Zertifikat $h" "nicht lesbar"; fail=$((fail+1)); fi
done

echo
echo "  $ok bestanden, $fail fehlgeschlagen"
[ "$fail" -eq 0 ] || exit 1
