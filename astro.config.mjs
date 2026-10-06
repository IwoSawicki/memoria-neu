// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Live-Domain als Standard (für Canonical/Sitemap/OG).
// Für die Entwicklungs-Domain in Dokploy die Env-Variable setzen:
//   SITE_URL=https://memoria.stolz-marketing.de
const SITE = process.env.SITE_URL || 'https://www.tierbestattung-memoria.de';

// https://astro.build/config
export default defineConfig({
  // Statische Ausgabe – keine SSR nötig.
  output: 'static',
  site: SITE,
  integrations: [
    sitemap({
      // Der Ratgeber ist noch im Aufbau und nirgends verlinkt – bis zum Start
      // gehoert er weder in die Sitemap noch in den Index (siehe noindex in
      // src/pages/ratgeber/). Zum Freischalten diese Zeile entfernen.
      filter: (seite) => !seite.includes('/ratgeber'),
      // lastmod signalisiert Google, wann zuletzt etwas geaendert wurde.
      // Build-Zeitpunkt ist hier die ehrlichste verfuegbare Angabe: Ein Deploy
      // findet nur statt, wenn sich tatsaechlich etwas geaendert hat.
      serialize: (item) => ({ ...item, lastmod: new Date().toISOString() }),
    }),
  ],
});
