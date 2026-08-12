// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  // Statische Ausgabe – keine SSR nötig.
  output: 'static',
  // TODO: echte Domain eintragen, sobald bekannt (für Canonical/Sitemap).
  site: 'https://www.tierbestattung-memoria.de',
});
