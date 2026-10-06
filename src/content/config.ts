import { defineCollection, z } from 'astro:content';

// Ratgeber-Beiträge. Ein Beitrag = eine Markdown-Datei in
// src/content/ratgeber/. Der Dateiname wird zur URL:
// "urne-aufbewahren.md" -> /ratgeber/urne-aufbewahren/
const ratgeber = defineCollection({
  type: 'content',
  schema: z.object({
    /** Überschrift der Seite (h1). */
    titel: z.string(),
    /** Title-Tag für Google, max. 60 Zeichen. Fehlt er, wird `titel` genommen. */
    seoTitel: z.string().optional(),
    /** Meta-Description, 150–160 Zeichen. */
    beschreibung: z.string(),
    /** Einleitender Satz unter der Überschrift. */
    lead: z.string(),
    /** Veröffentlichungsdatum, steuert die Reihenfolge in der Übersicht. */
    datum: z.date(),
    /** Hero-Bild. */
    bild: z.enum(['wald', 'hund', 'kind']).default('wald'),
    /** Auf false setzen, um einen Beitrag zu verstecken (Entwurf). */
    veroeffentlicht: z.boolean().default(true),
  }),
});

export const collections = { ratgeber };
