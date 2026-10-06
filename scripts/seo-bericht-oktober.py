# -*- coding: utf-8 -*-
"""Monatsbericht im Stolz-Marketing-Branding.

    pip install reportlab && python3 scripts/seo-bericht-oktober.py

Farben und Aufbau sind aus der GDM-Keyword-Analyse übernommen:
dunkles Grün #0c1b10, Lime #e4f53f, Kartengrau #f3f6f1, Überschriften
fett serifenlos mit einem kursiven Serifen-Akzentwort.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether,
                                NextPageTemplate, PageBreak, Flowable)

# --- Markenfarben -----------------------------------------------------------
DUNKEL = colors.HexColor('#0c1b10')
LIME = colors.HexColor('#e4f53f')
KARTE = colors.HexColor('#f3f6f1')
WEISS = colors.white
TEXT = colors.HexColor('#141a15')
GRAU = colors.HexColor('#5d6b60')
LINIE = colors.HexColor('#dfe5dc')
SAGE = colors.HexColor('#9db5a0')

SEITE_B, SEITE_H = A4
RAND = 20 * mm
INHALT_B = SEITE_B - 2 * RAND


def stil(name, **kw):
    basis = dict(fontName='Helvetica', fontSize=9.6, leading=14.6,
                 textColor=TEXT, spaceAfter=7)
    basis.update(kw)
    return ParagraphStyle(name, **basis)


P = stil('P')
P_KLEIN = stil('P_KLEIN', fontSize=8.6, leading=12.8, textColor=GRAU)
P_WEISS = stil('P_WEISS', textColor=colors.HexColor('#c9d4c6'))
H2 = stil('H2', fontName='Helvetica-Bold', fontSize=15.5, leading=19,
          textColor=TEXT, spaceBefore=4, spaceAfter=9)
H3 = stil('H3', fontName='Helvetica-Bold', fontSize=10.4, leading=14,
          textColor=TEXT, spaceAfter=4)
TH = stil('TH', fontName='Helvetica-Bold', fontSize=8.4, leading=11,
          textColor=WEISS, spaceAfter=0)
TD = stil('TD', fontSize=9, leading=12.6, spaceAfter=0)
TD_B = stil('TD_B', fontName='Helvetica-Bold', fontSize=9, leading=12.6, spaceAfter=0)
KPI_ZAHL = stil('KPI_ZAHL', fontName='Helvetica-Bold', fontSize=21, leading=23, spaceAfter=2)
KPI_LABEL = stil('KPI_LABEL', fontName='Helvetica-Bold', fontSize=6.8, leading=9.5,
                 textColor=GRAU, spaceAfter=3)
KPI_SUB = stil('KPI_SUB', fontSize=7.6, leading=10.4, textColor=GRAU, spaceAfter=0)


def logo(c, x, y, gross=False):
    """Lime-Funke plus Wortmarke."""
    s = 1.5 if gross else 1.0
    c.saveState()
    c.setFillColor(LIME)
    c.translate(x, y)
    c.scale(s, s)
    p = c.beginPath()
    p.moveTo(0, 2.1); p.lineTo(5.0, 3.6); p.lineTo(9.4, 7.4)
    p.lineTo(5.6, 3.0); p.lineTo(9.0, -0.6); p.lineTo(4.6, 2.0)
    p.lineTo(1.2, -1.6); p.lineTo(3.6, 1.6); p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.restoreState()
    c.setFont('Helvetica-Bold', 10.5 * s)
    c.setFillColor(WEISS if gross else TEXT)
    c.drawString(x + 15 * s, y - 1.5 * s, 'Stolz Marketing')


def cover(c, doc):
    c.saveState()
    c.setFillColor(DUNKEL)
    c.rect(0, 0, SEITE_B, SEITE_H, stroke=0, fill=1)
    # Dezenter Lichtschimmer rechts oben, wie auf dem Vorbild.
    for i in range(26):
        c.setFillColor(colors.Color(0.56, 0.72, 0.18, alpha=0.013))
        r = (150 - i * 5) * mm
        c.circle(SEITE_B * 0.80, SEITE_H * 0.66, r, stroke=0, fill=1)

    logo(c, RAND, SEITE_H - 30 * mm, gross=True)

    # Pill
    y = SEITE_H - 108 * mm
    label = 'SEO-BERICHT · OKTOBER 2026'
    c.setFont('Helvetica-Bold', 7.6)
    br = c.stringWidth(label, 'Helvetica-Bold', 7.6) + 20
    c.setStrokeColor(LIME); c.setLineWidth(0.8)
    c.roundRect(RAND, y - 4, br, 17, 8.5, stroke=1, fill=0)
    c.setFillColor(LIME)
    c.drawString(RAND + 10, y + 1.5, label)

    # Headline mit kursivem Akzentwort
    y -= 20 * mm
    c.setFillColor(WEISS)
    c.setFont('Helvetica-Bold', 30)
    c.drawString(RAND, y, 'Sechzehn Seiten statt')
    y -= 12.5 * mm
    c.drawString(RAND, y, 'einer – was im')
    y -= 12.5 * mm
    breite = c.stringWidth('Oktober ', 'Helvetica-Bold', 30)
    c.drawString(RAND, y, 'Oktober ')
    c.setFillColor(LIME)
    c.setFont('Times-BoldItalic', 32)
    c.drawString(RAND + breite, y, 'passiert ist')

    y -= 18 * mm
    c.setFillColor(colors.HexColor('#c9d4c6'))
    c.setFont('Helvetica', 11)
    for zeile in ['Neue Landingpages, sichtbare Bewertungen und ein Ratgeber-Bereich',
                  'für Tierbestattung Memoria, Laudenbach.']:
        c.drawString(RAND, y, zeile)
        y -= 6.2 * mm

    # Meta-Zeile unten
    yl = 42 * mm
    c.setStrokeColor(colors.Color(1, 1, 1, alpha=0.18)); c.setLineWidth(0.6)
    c.line(RAND, yl, SEITE_B - RAND, yl)
    spalten = [
        ('FÜR', ['Tierbestattung Memoria', 'tierbestattung-memoria.de']),
        ('ERSTELLT VON', ['Iwo Sawicki', 'Stolz Marketing']),
        ('STAND', ['6. Oktober 2026', 'Datenbasis: Search Console']),
    ]
    for i, (label, zeilen) in enumerate(spalten):
        x = RAND + i * (INHALT_B / 3)
        c.setFillColor(LIME); c.setFont('Helvetica-Bold', 7)
        c.drawString(x, yl - 9 * mm, label)
        c.setFillColor(colors.HexColor('#c9d4c6')); c.setFont('Helvetica', 8.6)
        for j, z in enumerate(zeilen):
            c.drawString(x, yl - 14.5 * mm - j * 4.6 * mm, z)
    c.restoreState()


def innen(c, doc):
    c.saveState()
    c.setFillColor(WEISS)
    c.rect(0, 0, SEITE_B, SEITE_H, stroke=0, fill=1)
    logo(c, SEITE_B - RAND - 72, SEITE_H - 16 * mm)
    c.setStrokeColor(LINIE); c.setLineWidth(0.5)
    c.line(RAND, 16 * mm, SEITE_B - RAND, 16 * mm)
    c.setFont('Helvetica', 7.4); c.setFillColor(GRAU)
    c.drawString(RAND, 11.5 * mm, 'SEO-Bericht Oktober · Tierbestattung Memoria · Stolz Marketing')
    c.drawRightString(SEITE_B - RAND, 11.5 * mm, 'Seite %d' % (doc.page - 1))
    c.restoreState()


class Badge(Flowable):
    """Umrandete Pille als Kapitelmarke."""

    def __init__(self, text):
        super().__init__()
        self.text = text
        self.height = 18
        self.width = INHALT_B

    def draw(self):
        c = self.canv
        c.setFont('Helvetica-Bold', 7.4)
        b = c.stringWidth(self.text, 'Helvetica-Bold', 7.4) + 22
        c.setStrokeColor(DUNKEL); c.setLineWidth(0.8)
        c.roundRect(0, 0, b, 16, 8, stroke=1, fill=0)
        c.setFillColor(DUNKEL)
        c.drawString(11, 5, self.text)


class Titel(Flowable):
    """Fette Überschrift mit kursivem Serifen-Akzent."""

    def __init__(self, normal, akzent, groesse=21):
        super().__init__()
        self.normal, self.akzent, self.g = normal, akzent, groesse
        self.height = groesse * 1.35
        self.width = INHALT_B

    def draw(self):
        c = self.canv
        c.setFillColor(TEXT)
        c.setFont('Helvetica-Bold', self.g)
        c.drawString(0, 6, self.normal)
        b = c.stringWidth(self.normal, 'Helvetica-Bold', self.g)
        c.setFont('Times-BoldItalic', self.g + 1.5)
        c.drawString(b, 6, self.akzent)


def kpi_karte(zahl, label, sub, variante='hell'):
    bg = {'hell': KARTE, 'dunkel': DUNKEL, 'lime': LIME}[variante]
    fz = WEISS if variante == 'dunkel' else TEXT
    fl = LIME if variante == 'dunkel' else GRAU
    if variante == 'lime':
        fl = colors.HexColor('#4a5a2a')
    daten = [
        [Paragraph(label, stil('l', fontName='Helvetica-Bold', fontSize=6.8,
                               leading=9.5, textColor=fl, spaceAfter=3))],
        [Paragraph(zahl, stil('z', fontName='Helvetica-Bold', fontSize=21,
                              leading=23, textColor=fz, spaceAfter=2))],
        [Paragraph(sub, stil('s', fontSize=7.6, leading=10.4,
                             textColor=fl if variante != 'hell' else GRAU, spaceAfter=0))],
    ]
    t = Table(daten, colWidths=[(INHALT_B - 3 * 6) / 4])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg),
        ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (0, 0), 11), ('BOTTOMPADDING', (0, -1), (-1, -1), 11),
        ('TOPPADDING', (0, 1), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -2), 0),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    return t


def kpi_reihe(karten):
    t = Table([karten], colWidths=[(INHALT_B - 3 * 6) / 4 + 6] * 4)
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-2, -1), 6),
        ('RIGHTPADDING', (-1, 0), (-1, -1), 0),
    ]))
    return t


def info_karte(nr, titel, text, breite):
    kopf = Table([[
        Paragraph('<font color="#141a15"><b>%s</b></font>' % nr,
                  stil('n', fontName='Helvetica-Bold', fontSize=8, leading=10,
                       spaceAfter=0)),
        Paragraph(titel, H3),
    ]], colWidths=[14, breite - 14 - 28])
    kopf.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), LIME),
        ('LEFTPADDING', (0, 0), (0, 0), 5), ('RIGHTPADDING', (0, 0), (0, 0), 0),
        ('TOPPADDING', (0, 0), (0, 0), 2), ('BOTTOMPADDING', (0, 0), (0, 0), 2),
        ('LEFTPADDING', (1, 0), (1, 0), 8), ('RIGHTPADDING', (1, 0), (1, 0), 0),
        ('TOPPADDING', (1, 0), (1, 0), 0), ('BOTTOMPADDING', (1, 0), (1, 0), 0),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    t = Table([[kopf], [Paragraph(text, P)]], colWidths=[breite])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), KARTE),
        ('LEFTPADDING', (0, 0), (-1, -1), 14), ('RIGHTPADDING', (0, 0), (-1, -1), 14),
        ('TOPPADDING', (0, 0), (0, 0), 13), ('BOTTOMPADDING', (0, -1), (-1, -1), 13),
        ('TOPPADDING', (0, 1), (-1, -1), 5), ('BOTTOMPADDING', (0, 0), (-1, -2), 0),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    return t


def zwei_spalten(links, rechts):
    b = (INHALT_B - 8) / 2
    t = Table([[links, rechts]], colWidths=[b + 8, b])
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (0, 0), 8),
        ('RIGHTPADDING', (1, 0), (1, 0), 0),
    ]))
    return t


def tabelle(kopf, zeilen, breiten, fett_erste=True):
    daten = [[Paragraph(k, TH) for k in kopf]]
    for z in zeilen:
        daten.append([Paragraph(z[0], TD_B if fett_erste else TD)] +
                     [Paragraph(x, TD) for x in z[1:]])
    t = Table(daten, colWidths=breiten, repeatRows=1)
    stile = [
        ('BACKGROUND', (0, 0), (-1, 0), DUNKEL),
        ('LEFTPADDING', (0, 0), (-1, -1), 9), ('RIGHTPADDING', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 5.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 5.5),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LINEBELOW', (0, 1), (-1, -2), 0.5, LINIE),
    ]
    for i in range(1, len(daten)):
        if i % 2 == 0:
            stile.append(('BACKGROUND', (0, i), (-1, i), KARTE))
    t.setStyle(TableStyle(stile))
    return t


class Balken(Flowable):
    """Liegendes Balkendiagramm im Markenlook."""

    def __init__(self, daten, maxwert, einheit='', hoehe_zeile=17):
        super().__init__()
        self.daten = daten
        self.maxwert = maxwert
        self.einheit = einheit
        self.hz = hoehe_zeile
        self.width = INHALT_B
        self.height = len(daten) * hoehe_zeile + 26

    def draw(self):
        c = self.canv
        label_b = 92
        wert_b = 56
        bar_b = self.width - label_b - wert_b - 20
        y = self.height - 20
        for label, wert, dunkel in self.daten:
            y -= self.hz
            c.setFont('Helvetica', 8.6)
            c.setFillColor(TEXT)
            c.drawRightString(label_b, y + 3.5, label)
            b = max(2.0, bar_b * (wert / self.maxwert))
            c.setFillColor(DUNKEL if dunkel else SAGE)
            c.roundRect(label_b + 10, y, b, 9.5, 4.75, stroke=0, fill=1)
            c.setFont('Helvetica-Bold', 8.4)
            c.setFillColor(TEXT)
            c.drawString(label_b + 16 + b, y + 2.5,
                         ('%s %s' % (format(wert, ',d').replace(',', '.'), self.einheit)).strip())
        c.setStrokeColor(LINIE); c.setLineWidth(0.5)
        c.line(label_b + 10, y - 6, self.width - 10, y - 6)


def hinweis(text):
    """Callout mit Lime-Linie links."""
    t = Table([[Paragraph(text, P_KLEIN)]], colWidths=[INHALT_B])
    t.setStyle(TableStyle([
        ('LINEBEFORE', (0, 0), (0, -1), 2.2, LIME),
        ('LEFTPADDING', (0, 0), (-1, -1), 12), ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 2), ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    return t


def stufen_karte(label, titel, text, variante):
    bg = {'lime': LIME, 'dunkel': DUNKEL, 'hell': KARTE}[variante]
    ft = WEISS if variante == 'dunkel' else TEXT
    fl = LIME if variante == 'dunkel' else (colors.HexColor('#4a5a2a') if variante == 'lime' else GRAU)
    b = (INHALT_B - 2 * 7) / 3
    daten = [
        [Paragraph(label, stil('sl', fontName='Helvetica-Bold', fontSize=6.8,
                               leading=9.6, textColor=fl, spaceAfter=5))],
        [Paragraph(titel, stil('st', fontName='Helvetica-Bold', fontSize=10.4,
                               leading=13.6, textColor=ft, spaceAfter=5))],
        [Paragraph(text, stil('sx', fontSize=8.8, leading=12.8, textColor=ft, spaceAfter=0))],
    ]
    t = Table(daten, colWidths=[b])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg),
        ('LEFTPADDING', (0, 0), (-1, -1), 12), ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (0, 0), 13), ('BOTTOMPADDING', (0, -1), (-1, -1), 13),
        ('TOPPADDING', (0, 1), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -2), 0),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    return t


def drei_spalten(a, b_, c_):
    b = (INHALT_B - 2 * 7) / 3
    t = Table([[a, b_, c_]], colWidths=[b + 7, b + 7, b])
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-2, -1), 7),
        ('RIGHTPADDING', (-1, 0), (-1, -1), 0),
    ]))
    return t


# --- Dokument ---------------------------------------------------------------
doc = BaseDocTemplate(
    'docs/berichte/SEO-Bericht-2026-10.pdf', pagesize=A4,
    title='Tierbestattung Memoria – SEO-Bericht Oktober 2026',
    author='Stolz Marketing', subject='SEO-Bericht Oktober 2026',
    leftMargin=RAND, rightMargin=RAND, topMargin=26 * mm, bottomMargin=22 * mm)
rahmen = Frame(RAND, 22 * mm, INHALT_B, SEITE_H - 26 * mm - 22 * mm,
               leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
doc.addPageTemplates([
    PageTemplate(id='cover', frames=[rahmen], onPage=cover),
    PageTemplate(id='innen', frames=[rahmen], onPage=innen),
])

s = [NextPageTemplate('innen'), PageBreak()]

# --- 01 Auf einen Blick -----------------------------------------------------
s += [
    Badge('01 · AUF EINEN BLICK'), Spacer(1, 10),
    Titel('Der Monat in ', 'Kürze'), Spacer(1, 10),
    Paragraph('Im Oktober ging es darum, aus den im September gebauten Seiten '
              'richtige Landingpages zu machen – und Vertrauen sichtbar zu '
              'zeigen.', P),
    Spacer(1, 10),
    kpi_reihe([
        kpi_karte('16', 'SEITEN GESAMT', 'vorher: 5', 'dunkel'),
        kpi_karte('11', 'NEU SEIT SEPT.', 'davon 5 Ortsseiten'),
        kpi_karte('8', 'AUF SEITE 1', 'von 9 geprüften Seiten'),
        kpi_karte('4,9', 'STERNE SICHTBAR', 'aus 186 Bewertungen', 'lime'),
    ]),
    Spacer(1, 14),
    zwei_spalten(
        info_karte('1', 'Alle neuen Seiten ranken',
                   'Die neun Seiten vom 11. September werden inzwischen von '
                   'Google angezeigt – acht davon auf der ersten Ergebnisseite. '
                   'Keine hat seit Monatsbeginn verloren.', (INHALT_B - 8) / 2 + 8),
        info_karte('2', 'Die Adressen sind zusammengeführt',
                   'Nach dem Umbau kannte Google kurzzeitig zwei Adressen je '
                   'Seite. Das hat sich erledigt: Die alten bekommen keine '
                   'Anzeigen mehr, die neuen legen zu.', (INHALT_B - 8) / 2)),
    Spacer(1, 7),
    zwei_spalten(
        info_karte('3', 'Aus Textwüsten wurden Landingpages',
                   'Die Ortsseiten bestanden nur aus Text. Jetzt haben sie Bild, '
                   'Vertrauenszeile, Tabellen und einen klaren Abschluss – wie '
                   'die Startseite.', (INHALT_B - 8) / 2 + 8),
        info_karte('4', 'Erfundene Zitate sind raus',
                   'Die drei Kundenstimmen auf der Startseite stammten aus dem '
                   'Design-Entwurf. Sie wurden entfernt und durch die echte '
                   'Google-Bewertung ersetzt.', (INHALT_B - 8) / 2)),
    Spacer(1, 14),
    Paragraph('Die Website heute – aus einer Startseite sind sechzehn Seiten geworden', H3),
    Spacer(1, 3),
    tabelle(['Bereich', 'Seiten', 'Stand'],
            [['Bestand', '/ · /tierurnen-andenken · /impressum · /datenschutz',
              'vor September'],
             ['Leistung &amp; Preis', '/leistungen · /preise', 'September'],
             ['Kontakt', '/kontakt · /anfahrt', 'September'],
             ['Orte', '/tierkrematorium-laudenbach · /tierbestattung-bergstrasse '
              '· /tierbestattung-odenwald', 'September'],
             ['Orientierung', '/einzel-oder-gemeinschaftskremierung · '
              '/tier-nachts-gestorben', 'September'],
             ['Orte neu', '/tierbestattung-weinheim · /tierbestattung-einhausen',
              'Oktober'],
             ['Ratgeber', '/ratgeber', 'Oktober, intern']],
            [INHALT_B * 0.19, INHALT_B * 0.56, INHALT_B * 0.25]),
]

# --- 02 Zahlen --------------------------------------------------------------
s += [PageBreak(),
      Badge('02 · DIE ZAHLEN'), Spacer(1, 10),
      Titel('Was Google ', 'misst'), Spacer(1, 8),
      Paragraph('Datenbasis: Google Search Console, Export vom 6. Oktober 2026.', P_KLEIN),
      Spacer(1, 12),
      Paragraph('Besucher über Google je Monat', H3),
      Balken([('August', 274, False), ('September', 420, True),
              ('Oktober (1.–6.)', 34, False)], 460),
      Spacer(1, 10),
      Paragraph('Anzeigen in der Suche je Monat', H3),
      Balken([('August', 3119, False), ('September', 5284, True),
              ('Oktober (1.–6.)', 466, False)], 5600),
      Spacer(1, 10),
      hinweis('September wurde von Google nachträglich nach oben korrigiert '
              '(von 387 auf 420 Besucher). Das ist normal – Google füllt Daten '
              'einige Tage lang nach.'),
      Spacer(1, 16),
      Paragraph('Wo die neuen Seiten stehen', H3),
      Paragraph('Durchschnittliche Position. 1 bis 10 entspricht der ersten '
                'Seite der Google-Ergebnisse.', P_KLEIN),
      Spacer(1, 4),
      tabelle(['Seite', 'Position', 'Entwicklung seit 1.10.'],
              [['Kontakt', '3,8', 'leicht besser'],
               ['Anfahrt und Standorte', '4,4', 'stabil'],
               ['Tierkrematorium Laudenbach', '5,8', 'von 6,1'],
               ['Unsere Leistungen', '6,8', 'von 9,4 – stärkster Sprung'],
               ['Tierbestattung Bergstraße', '7,2', 'stabil'],
               ['Tier nachts gestorben', '7,9', 'von 9,2'],
               ['Tierbestattung Odenwald', '8,6', 'von 9,1'],
               ['Einzel- oder Gemeinschaftskremierung', '10,1', 'von 10,7'],
               ['Preise', '11,1', 'von 11,9']],
              [INHALT_B * 0.46, INHALT_B * 0.16, INHALT_B * 0.38]),
      Spacer(1, 10),
      hinweis('Weinheim und Einhausen sind erst am 1. Oktober dazugekommen und '
              'noch nicht in der Liste. Sie wurden bei Google zur Aufnahme '
              'angemeldet.'),
      ]

# --- 03 Ehrliche Einordnung -------------------------------------------------
s += [PageBreak(),
      Badge('03 · EINORDNUNG'), Spacer(1, 10),
      Titel('Was davon ist ', 'unsere Arbeit?'), Spacer(1, 10),
      Paragraph('Diese Frage beantworten wir lieber selbst, als sie offenzulassen.', P),
      Spacer(1, 8),
      tabelle(['', 'Zahl', 'Einordnung'],
              [['Zuwachs Besucher gesamt', '+146', 'August → September'],
               ['davon von neuen Seiten', '48', 'rund ein Drittel'],
               ['Rest', '98', 'Startseite und Suchen nach „Memoria"'],
               ['Markensuchen', '378 von 443', 'hängt am Ruf, nicht an uns']],
              [INHALT_B * 0.36, INHALT_B * 0.18, INHALT_B * 0.46]),
      Spacer(1, 12),
      zwei_spalten(
          info_karte('!', 'Der Vergleichsmonat ist unsauber',
                     'Die neue Website ging am 24. August live, bis dahin lief '
                     'die alte. Ein Teil der Verbesserung geht auf den Relaunch '
                     'selbst zurück.', (INHALT_B - 8) / 2 + 8),
          info_karte('!', 'Die Zahlen können auch fallen',
                     'Nach einem Website-Umzug schwanken die Werte drei bis '
                     'sechs Monate. Neue Seiten starten hinten und drücken den '
                     'Durchschnitt, solange sie aufsteigen.', (INHALT_B - 8) / 2)),
      Spacer(1, 12),
      hinweis('Unser Vorschlag: nicht Monat für Monat vergleichen, sondern nach '
              'drei Monaten – und gezielt auf die Besucher schauen, die nicht '
              'nach „Memoria" gesucht haben. Das sind aktuell 65 von 443.'),
      ]

# --- 04 Oktober -------------------------------------------------------------
s += [PageBreak(),
      Badge('04 · UMGESETZT'), Spacer(1, 10),
      Titel('Was im Oktober ', 'gebaut wurde'), Spacer(1, 10),
      tabelle(['Bereich', 'Was', 'Wirkung'],
              [['Preise', 'Eigene Abschnitte für Hund, Katze und Kleintier mit '
                'Tabellen statt Zahlenketten im Text',
                'Beantwortet die meistgesuchte Frage direkt'],
               ['Ortsseiten', 'Weinheim und Einhausen neu; alle fünf Ortsseiten '
                'auf Landingpage-Layout mit Bild, Tabellen und Abschluss',
                'Seiten wirken wie Seiten, nicht wie Textdateien'],
               ['Bewertungen', '4,9 Sterne aus 186 Bewertungen im ersten '
                'Bildschirm und in einem eigenen Abschnitt',
                'Vertrauen sofort sichtbar'],
               ['Anfahrt', 'Karte für beide Adressen, lädt erst auf Klick',
                'Besser auffindbar, ohne Datenschutzproblem'],
               ['Navigation', 'Leistungen und Preise führen auf die Unterseiten '
                'statt auf Sprungmarken',
                'Besucher landen auf dem ausführlichen Inhalt'],
               ['Suchbegriffe', '„Krematorium Laudenbach" und „Hundebestatter" '
                'ergänzt – fehlten komplett',
                '158 Anzeigen ohne Klick adressiert'],
               ['Technik', 'Zwei Fehlerseiten und eine Sitemap-Anmeldung von '
                '2022 korrigiert',
                'Keine Sackgassen mehr für Google'],
               ['Ratgeber', 'Bereich für Beiträge gebaut, noch nicht '
                'freigeschaltet',
                'Grundlage für monatliche Themen']],
              [INHALT_B * 0.17, INHALT_B * 0.47, INHALT_B * 0.36]),
      ]

# --- 05 Fahrplan ------------------------------------------------------------
s += [PageBreak(),
      Badge('05 · FAHRPLAN'), Spacer(1, 10),
      Titel('Wie es ', 'weitergeht'), Spacer(1, 12),
      drei_spalten(
          stufen_karte('NOCH IM OKTOBER', 'Daten und Inhalte',
                       'Suchvolumen über Keyword-Planer, Ahrefs und Sistrix '
                       'prüfen. Echte Bewertungen einbauen. Antworten von Ihnen '
                       'in die offenen Stellen einarbeiten.', 'lime'),
          stufen_karte('NOVEMBER', 'Ratgeber und Orte',
                       'Ratgeber freischalten, zwei Beiträge veröffentlichen. '
                       'Weitere Ortsseiten – aber nur dort, wo die Suchvolumen '
                       'es hergeben.', 'dunkel'),
          stufen_karte('DANACH', 'Auswerten',
                       'Drei-Monats-Vergleich auf Basis der Besucher ohne '
                       'Markensuche. Erst dann lässt sich seriös sagen, was '
                       'gewirkt hat.', 'hell')),
      Spacer(1, 16),
      Paragraph('Offene Punkte im Detail', H3),
      tabelle(['Thema', 'Was fehlt', 'Wann'],
              [['Bewertungen', '4–6 Google-Bewertungen im Wortlaut, die wir '
                'zeigen dürfen', 'Oktober'],
               ['Keywords', 'Suchvolumen für Mannheim, Heidelberg und Worms '
                '– die Search Console allein reicht dafür nicht', 'Oktober'],
               ['Abholung', 'Kostet die Abholung extra? Pauschale oder '
                'Kilometerpreis?', 'Oktober'],
               ['Zahlung', 'Wann und wie wird bezahlt?', 'Oktober'],
               ['Urne', 'Wie lange dauert es bis zur Rückgabe?', 'Oktober'],
               ['Nachts', 'Was sollen Tierhalter tun, bis jemand da ist? '
                'Fachliche Angabe', 'Oktober'],
               ['Tierfriedhof', 'Bieten Sie Beisetzung an – ja oder nein? '
                'Danach wird gesucht', 'Oktober'],
               ['Pferde', 'Selbst kremiert oder vermittelt? Davon hängt ab, ob '
                'eine eigene Seite entsteht', 'November']],
              [INHALT_B * 0.17, INHALT_B * 0.60, INHALT_B * 0.23]),
      Spacer(1, 12),
      hinweis('Zu den Punkten mit „Oktober" schreiben wir bewusst nichts auf die '
              'Website, solange die Angaben fehlen. Falsche Auskünfte wären hier '
              'schlechter als gar keine.'),
      ]

doc.build(s)
print('PDF erstellt: docs/berichte/SEO-Bericht-2026-10.pdf')
