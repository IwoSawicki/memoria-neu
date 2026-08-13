// Zentrale Inhaltsdaten (Single Source of Truth) – siehe CLAUDE.md §5.

export const site = {
  name: 'Memoria',
  fullName: 'Tierbestattung Memoria',
  legalName: 'Memoria Tierbestattung GmbH',
  managingDirector: 'Dr. Klaus Göck',
  phoneDisplay: '06201 7303041',
  phoneHref: 'tel:+4962017303041',
  email: 'info@tierbestattung-memoria.de',
  emailHref: 'mailto:info@tierbestattung-memoria.de',
  instagram: 'https://www.instagram.com/memoria.tierbestattung',
  instagramHandle: 'memoria.tierbestattung',
  owners: ['Sarina Göck-König', 'Dr. Klaus Göck'],
  address: 'Konrad-Zuse-Str. 3, 69514 Laudenbach',
  pickupAddress: 'Abholadresse: Carl-Benz-Str. 1, 64683 Einhausen',
  // FormSubmit.co: Ziel für das Kontaktformular. Kein Key nötig – beim ersten
  // Absenden schickt FormSubmit eine Aktivierungs-Mail, die einmalig bestätigt
  // werden muss. Zum Schutz vor Spam kann hier später der von FormSubmit
  // erzeugte Hash-Endpoint statt der Klartext-Adresse eingetragen werden
  // (z. B. 'abc123def456').
  formsubmitTarget: 'info@tierbestattung-memoria.de',
  // Google Analytics 4 Mess-ID (z. B. 'G-XXXXXXXXXX'). Leer lassen = kein
  // Analytics und kein Cookie-Banner. Sobald eine ID eingetragen ist, erscheint
  // der Cookie-Hinweis und GA wird NUR nach Einwilligung geladen.
  googleAnalyticsId: '',
  seo: {
    title:
      'Tierbestattung Memoria – Einzelkremierung mit Ascherückgabe in Laudenbach',
    description:
      'Tierbestattung Memoria in Laudenbach: Abholung rund um die Uhr, Einzel- und Gemeinschaftskremierung, Tierurnen. Familienunternehmen. Telefon 06201 7303041.',
  },
  // Sichtbarkeit optionaler Blöcke (im Original: showPrices / showStickyBar).
  showPrices: true,
  showStickyBar: true,
};

// Navigation im Header (Anker auf der Startseite).
export const nav = [
  { label: 'Ablauf', href: '#ablauf' },
  { label: 'Leistungen', href: '#leistungen' },
  { label: 'Über uns', href: '#ueber-uns' },
  { label: 'Kontakt', href: '#kontakt' },
  { label: 'Preise', href: '#preise' },
];

// Footer-Navigation.
export const footerNav = [
  { label: 'Leistungen', href: '#leistungen' },
  { label: 'Ablauf', href: '#ablauf' },
  { label: 'Über uns', href: '#ueber-uns' },
  { label: 'Preise', href: '#preise' },
];

// Trust-Punkte in der Hero-Sektion.
export const trustPoints = [
  'Abholung rund um die Uhr',
  'Einzelkremierung mit Ascherückgabe',
  'Kleines Familienunternehmen',
];

// Leistungskarten.
export const leistungen = [
  {
    icon: 'certificate',
    title: 'Einzelkremierung',
    text: 'Ihr Tier wird allein kremiert. Sie erhalten seine Asche in einer Urne Ihrer Wahl zurück, dazu eine Urkunde.',
  },
  {
    icon: 'heart',
    title: 'Gemeinschaftskremierung',
    text: 'Ein würdiger Abschied ohne Ascherückgabe. Die Beisetzung erfolgt gemeinschaftlich und in Ruhe.',
  },
  {
    icon: 'urn',
    title: 'Tierurnen und Andenken',
    text: 'Urnen aus Holz, Stein und Keramik, dazu kleine Andenken zum Aufbewahren. Wir beraten Sie persönlich.',
  },
];

// Ablauf-Schritte.
export const ablaufSteps = [
  {
    num: '01',
    title: 'Sie rufen an',
    text: 'Zu jeder Tages- und Nachtzeit. Wir hören zu und besprechen alles Weitere mit Ihnen.',
  },
  {
    num: '02',
    title: 'Wir holen ab',
    text: 'Wir kommen zu Ihnen nach Hause oder zur Tierklinik und überführen Ihr Tier behutsam.',
  },
  {
    num: '03',
    title: 'Die Kremierung',
    text: 'Einzeln oder gemeinschaftlich – ganz wie Sie es sich wünschen. Sie erhalten eine Urkunde.',
  },
  {
    num: '04',
    title: 'Die Urne',
    text: 'Bei der Einzelkremierung erhalten Sie die Asche Ihres Tieres in einer Urne Ihrer Wahl zurück.',
  },
];

// Testimonials (Zitat-Slider).
export const quotes = [
  {
    text: '„Wir haben nachts angerufen und sofort einen ruhigen Menschen am Telefon gehabt. Das hat uns sehr geholfen.“',
    author: 'M. K.',
  },
  {
    text: '„Unser Hund wurde mit einer Achtsamkeit abgeholt, die wir nicht erwartet hatten. Danke dafür.“',
    author: 'A. B.',
  },
  {
    text: '„Alles wurde uns in Ruhe erklärt, nichts musste schnell entschieden werden. Die Urne ist wunderschön.“',
    author: 'S. R.',
  },
];

// Preistabellen.
export const priceTables = [
  {
    title: 'Einzelkremierung mit Ascherückgabe',
    badge: 'inkl. Urnengutschrift',
    rows: [
      { label: 'Vögel & Kleintiere', price: '115 €' },
      { label: 'Kaninchen', price: '135 €' },
      { label: 'Katzen & Hunde bis 5 kg', price: '195 €' },
      { label: '5–20 kg', price: '235 €' },
      { label: '20–40 kg', price: '315 €' },
      { label: '40–60 kg', price: '370 €' },
      { label: 'über 60 kg', price: '430 €' },
    ],
  },
  {
    title: 'Gemeinschaftskremierung',
    badge: 'ohne Ascherückgabe',
    rows: [
      { label: 'Vögel & Kleintiere', price: '60 €' },
      { label: 'Kaninchen', price: '70 €' },
      { label: 'Katzen & Hunde bis 5 kg', price: '120 €' },
      { label: '5–20 kg', price: '160 €' },
      { label: '20–40 kg', price: '210 €' },
      { label: '40–60 kg', price: '260 €' },
      { label: 'über 60 kg', price: '320 €' },
    ],
  },
];
