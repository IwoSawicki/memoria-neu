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
  // Katalog (PDF) – liegt in public/downloads/ und kann dort jederzeit
  // ausgetauscht werden, ohne dass am Code etwas geändert werden muss.
  katalogPdf: '/downloads/tierurnen-katalog.pdf',
  // Online-Terminbuchung (Acuity Scheduling)
  bookingUrl: 'https://app.acuityscheduling.com/schedule.php?owner=35292506',
  // Partner für personalisierte Edelsteine aus Asche oder Haaren
  mevistoUrl: 'https://www.mevisto.com/de/mevisto-personalisiert/',
  // Umami (selbst gehostet, cookielos) – lädt immer, kein Cookie-Banner nötig.
  umamiSrc: 'https://analytics.stolz-marketing.de/script.js',
  umamiWebsiteId: '45e11098-414d-4c9a-9d4b-897494163617',
  // Google Analytics 4 Mess-ID (z. B. 'G-XXXXXXXXXX'). Leer lassen = kein
  // Analytics und kein Cookie-Banner. Sobald eine ID eingetragen ist, erscheint
  // der Cookie-Hinweis und GA wird NUR nach Einwilligung geladen.
  googleAnalyticsId: 'G-08LQ8WK59V',
  seo: {
    title:
      'Tierbestattung Memoria – Einzelkremierung mit Ascherückgabe in Laudenbach',
    description:
      'Tierbestattung Memoria in Laudenbach: rund um die Uhr erreichbar, Einzel- und Gemeinschaftskremierung, Tierurnen. Familienunternehmen. Telefon 06201 7303041.',
  },
  // Sichtbarkeit optionaler Blöcke (im Original: showPrices / showStickyBar).
  showPrices: true,
  showStickyBar: true,
};

// Navigation im Header. „Ablauf" ist bewusst nicht enthalten, damit die Leiste
// schlank bleibt – der Abschnitt ist weiterhin über den Footer erreichbar.
export const nav = [
  { label: 'Leistungen', href: '#leistungen' },
  { label: 'Preise', href: '#preise' },
  { label: 'Tierurnen', href: '/tierurnen-andenken' },
  { label: 'Über uns', href: '#ueber-uns' },
  { label: 'Kontakt', href: '#kontakt' },
];

// Footer-Navigation.
export const footerNav = [
  { label: 'Leistungen', href: '/#leistungen' },
  { label: 'Ablauf', href: '/#ablauf' },
  { label: 'Über uns', href: '/#ueber-uns' },
  { label: 'Preise', href: '/#preise' },
  { label: 'Tierurnen & Andenken', href: '/tierurnen-andenken' },
];

// Trust-Punkte in der Hero-Sektion.
export const trustPoints = [
  'Rund um die Uhr erreichbar',
  'Einzelkremierung mit Ascherückgabe',
  'Kleines Familienunternehmen',
];

// Leistungskarten.
export const leistungen = [
  {
    icon: 'certificate',
    title: 'Einzelkremierung',
    text: 'Ihr Tier wird einzeln eingeäschert. Sie erhalten die Asche in einer Urne Ihrer Wahl zurück, dazu eine Urkunde.',
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
    href: '/tierurnen-andenken',
    linkText: 'Katalog ansehen',
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

// Urnen-Galerie (Fotos aus dem Katalog) – 4 Modelle als kleiner Einblick.
export const urnenGalerie = [
  { img: '/images/urnen/verona-weiss.webp', name: 'Verona Weiß', material: 'Keramik samtiert' },
  { img: '/images/urnen/verona-schwarz.webp', name: 'Verona Schwarz', material: 'Keramik samtiert' },
  { img: '/images/urnen/mondschein.webp', name: 'Mondschein', material: 'Motivurne' },
  { img: '/images/urnen/tatzenspuren.webp', name: 'Tatzenspuren im Sand', material: 'Motivurne' },
];

// Größentabelle aus dem Katalog (Mindestvolumen nach Tiergewicht).
export const urnenGroessen = [
  { gewicht: 'bis 1,5 kg', volumen: '0,25 L' },
  { gewicht: 'bis 10 kg', volumen: '0,5 L' },
  { gewicht: 'bis 20 kg', volumen: '1 L' },
  { gewicht: 'bis 35 kg', volumen: '1,5 L' },
  { gewicht: 'bis 50 kg', volumen: '2 L' },
  { gewicht: 'über 50 kg', volumen: '2,5 L' },
];

// Materialien aus dem Katalog.
export const urnenMaterialien = [
  'Keramik samtiert',
  'Keramik frostsicher',
  'Keramikherz & Keramikpyramide',
  'Holzurnen (furniert)',
  'Holzurnen Einzelstücke',
  'Natursteinurnen Alabaster',
  'Kupfermotivurnen',
  'Messing-Herz & Messing-Rainbow',
];

// FAQ (Startseite) – dient auch als strukturierte Daten für Google.
export const faq = [
  {
    q: 'Wie schnell können Sie mein Tier abholen?',
    a: 'Wir sind rund um die Uhr für Sie erreichbar und holen an 365 Tagen im Jahr ab – auch am Wochenende. Ein Anruf unter 06201 7303041 genügt, alles Weitere besprechen wir in Ruhe mit Ihnen.',
  },
  {
    q: 'Was ist der Unterschied zwischen Einzel- und Gemeinschaftskremierung?',
    a: 'Bei der Einzelkremierung wird Ihr Tier einzeln eingeäschert. Sie erhalten die Asche in einer Urne Ihrer Wahl zurück, dazu eine Urkunde. Bei der Gemeinschaftskremierung erfolgt die Beisetzung gemeinschaftlich, eine Ascherückgabe ist dabei nicht möglich.',
  },
  {
    q: 'Was kostet eine Tierkremierung?',
    a: 'Die Einzelkremierung mit Ascherückgabe beginnt bei 115 € für Vögel und Kleintiere, die Gemeinschaftskremierung bei 60 €. Der Preis richtet sich nach dem Gewicht des Tieres. Alle Preise verstehen sich inklusive Urkunde, Überführung, Energie- und CO₂-Zuschlag sowie 19 % MwSt. Für Serviceleistungen außerhalb der regulären Zeiten kommt ein Zuschlag hinzu.',
  },
  {
    q: 'Holen Sie mein Tier auch in der Tierklinik ab?',
    a: 'Ja. Wir kommen zu Ihnen nach Hause oder in die Tierarztpraxis bzw. Tierklinik und überführen Ihr Tier behutsam.',
  },
  {
    q: 'Kremieren Sie auch Pferde und große Tiere?',
    a: 'Ja, auch Pferde und große Tiere werden bei uns kremiert. Die Preise für die Pferdekremierung nennen wir Ihnen gern persönlich am Telefon.',
  },
  {
    q: 'Welche Urnengröße brauche ich?',
    a: 'Die passende Größe richtet sich nach dem Gewicht Ihres Tieres – bis 10 kg genügen zum Beispiel 0,5 Liter, bis 20 kg 1 Liter. Die Urne darf gern größer sein, sollte vom Fassungsvolumen aber nicht kleiner ausfallen. Die vollständige Tabelle und unsere gesamte Auswahl finden Sie auf der Seite Tierurnen & Andenken.',
  },
  {
    q: 'Kann ich einen Pfotenabdruck oder eine Locke bekommen?',
    a: 'Ja, auf Wunsch nehmen wir einen Pfotenabdruck ab oder sichern eine Locke. Sagen Sie uns am besten zeitnah nach dem Empfang Ihres Tieres Bescheid, damit wir es rechtzeitig berücksichtigen können.',
  },
  {
    q: 'Wer steht hinter Memoria?',
    a: 'Memoria ist ein kleines Familienunternehmen aus Laudenbach. Sarina Göck-König und Dr. Klaus Göck führen es gemeinsam, nehmen Ihren Anruf persönlich entgegen und begleiten jeden Abschied selbst.',
  },
];

// Preistabellen – Werte und Urnengutschriften 1:1 von der bisherigen Seite.
export const priceTables = [
  {
    title: 'Einzelkremierung mit Ascherückgabe',
    badge: 'inkl. Urnengutschrift',
    rows: [
      { label: 'Vögel & Kleintiere', note: 'inkl. 15 € Urnengutschrift', price: '115 €' },
      { label: 'Kaninchen', note: 'inkl. 15 € Urnengutschrift', price: '135 €' },
      { label: 'Katzen & Hunde bis 5 kg', note: 'inkl. 15 € Urnengutschrift', price: '195 €' },
      { label: 'Katzen & Hunde 5–20 kg', note: 'inkl. 15 € Urnengutschrift', price: '235 €' },
      { label: 'Hunde 20–40 kg', note: 'inkl. 25 € Urnengutschrift', price: '315 €' },
      { label: 'Hunde 40–60 kg', note: 'inkl. 30 € Urnengutschrift', price: '370 €' },
      { label: 'Hunde über 60 kg', note: 'inkl. 30 € Urnengutschrift', price: '430 €' },
    ],
  },
  {
    title: 'Gemeinschaftskremierung',
    badge: 'ohne Ascherückgabe',
    rows: [
      { label: 'Vögel & Kleintiere', price: '60 €' },
      { label: 'Kaninchen', price: '70 €' },
      { label: 'Katzen & Hunde bis 5 kg', price: '120 €' },
      { label: 'Katzen & Hunde 5–20 kg', price: '160 €' },
      { label: 'Hunde 20–40 kg', price: '210 €' },
      { label: 'Hunde 40–60 kg', price: '260 €' },
      { label: 'Hunde über 60 kg', price: '320 €' },
    ],
  },
];

// Zuschläge für Serviceleistungen außerhalb der regulären Zeiten.
export const priceSurcharges = [
  { zeit: 'Mo–Fr 18:00–20:00 Uhr und Sa 14:00–18:00 Uhr', zuschlag: 'zzgl. 29 €' },
  { zeit: 'Mo–Fr nach 20:00 Uhr, Sa nach 18:00 Uhr und sonntags', zuschlag: 'zzgl. 49 €' },
];
