import type { APIRoute } from 'astro';

// Nur die echte Live-Domain darf indexiert werden. Jede andere Umgebung
// (Dev-Subdomain, Vorschau) wird für Suchmaschinen komplett gesperrt –
// sonst konkurriert eine Kopie der Seite mit dem Original.
const LIVE_HOST = 'www.tierbestattung-memoria.de';

export const GET: APIRoute = ({ site }) => {
  const isLive = site?.hostname === LIVE_HOST;

  const body = isLive
    ? `User-agent: *
Allow: /

Sitemap: https://${LIVE_HOST}/sitemap-index.xml
`
    : `# Nicht-Live-Umgebung – Indexierung vollständig gesperrt.
User-agent: *
Disallow: /
`;

  return new Response(body, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};
