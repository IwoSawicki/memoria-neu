# Original-Bilddateien (nicht ausgeliefert)

Hier liegen die vom Kunden hochgeladenen Originale in voller Auflösung. Sie
werden **nicht** an Besucher ausgeliefert und sind absichtlich außerhalb von
`public/`, damit sie nicht im Build landen.

| Original | Wird ausgeliefert als | Verwendung |
|---|---|---|
| `memoria-herobild.png` (1553×1013) | `public/images/hero.webp` · `public/images/og.jpg` | Hero-Bild, Social-Vorschau |
| `pasted-1785311187667-0.png` (994×1240) | `public/images/about.webp` | „Über uns" |
| `Memoria-Kontaktbild.png` (3992×890) | `public/images/contact.webp` | Kontakt-Parallax |

## Neu erzeugen

Falls ein Bild neu optimiert werden soll (benötigt `sharp`):

```js
const sharp = require('sharp');
// Hero (max. 1920 breit)
sharp('assets/originals/memoria-herobild.png')
  .resize({ width: 1920, withoutEnlargement: true })
  .webp({ quality: 80 }).toFile('public/images/hero.webp');
// Über uns (max. 1000 breit, Hochformat 4:5)
sharp('assets/originals/pasted-1785311187667-0.png')
  .resize({ width: 1000, withoutEnlargement: true })
  .webp({ quality: 82 }).toFile('public/images/about.webp');
// Kontakt (max. 2400 breit)
sharp('assets/originals/Memoria-Kontaktbild.png')
  .resize({ width: 2400, withoutEnlargement: true })
  .webp({ quality: 78 }).toFile('public/images/contact.webp');
// Open-Graph-Bild (exakt 1200×630)
sharp('assets/originals/memoria-herobild.png')
  .resize(1200, 630, { fit: 'cover' })
  .jpeg({ quality: 82, mozjpeg: true }).toFile('public/images/og.jpg');
```
