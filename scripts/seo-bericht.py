# -*- coding: utf-8 -*-
# Monatsbericht für den Kunden als PDF.
#
#   pip install reportlab && python3 scripts/seo-bericht.py
#
# Für den nächsten Monat: Zahlen in den KPI-Karten und die Textbausteine unten
# austauschen, Dateinamen anpassen. Die Zahlen kommen aus den CSV-Exporten der
# Search Console (Leistung -> Exportieren), Monatssummen über Diagramm.csv.
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether)

GRUEN   = colors.HexColor('#16260c')
DUNKEL  = colors.HexColor('#2b3a1e')
TEXT    = colors.HexColor('#3d4a30')
MUTED   = colors.HexColor('#5c6b4c')
KARTE   = colors.HexColor('#e6eecd')
SEITE   = colors.HexColor('#f3f8e5')
LINIE   = colors.HexColor('#d5deba')

def stil(name, **kw):
    basis = dict(fontName='Helvetica', fontSize=10, leading=15, textColor=TEXT,
                 alignment=TA_LEFT, spaceAfter=7)
    basis.update(kw)
    return ParagraphStyle(name, **basis)

H1   = stil('H1', fontName='Times-Roman', fontSize=25, leading=29, textColor=GRUEN, spaceAfter=3)
SUB  = stil('SUB', fontSize=10, textColor=MUTED, spaceAfter=20)
H2   = stil('H2', fontName='Times-Roman', fontSize=15, leading=19, textColor=GRUEN,
            spaceBefore=15, spaceAfter=7, keepWithNext=1)
P    = stil('P')
LI   = stil('LI', leftIndent=11, bulletIndent=1, spaceAfter=5)
KPIZ = stil('KPIZ', fontName='Helvetica-Bold', fontSize=19, leading=21, textColor=GRUEN, spaceAfter=1)
KPIL = stil('KPIL', fontSize=7.6, leading=10, textColor=MUTED, spaceAfter=0)
KPIV = stil('KPIV', fontSize=8, leading=11, textColor=TEXT, spaceAfter=0)
FUSS = stil('FUSS', fontSize=8, textColor=MUTED)

def seite(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(SEITE)
    canvas.rect(0, 0, A4[0], A4[1], stroke=0, fill=1)
    canvas.setFillColor(DUNKEL)
    canvas.rect(0, A4[1] - 7*mm, A4[0], 7*mm, stroke=0, fill=1)
    canvas.setFont('Helvetica', 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(20*mm, 11*mm, 'Tierbestattung Memoria · SEO-Bericht September 2026')
    canvas.drawRightString(A4[0] - 20*mm, 11*mm, 'Seite %d' % doc.page)
    canvas.setStrokeColor(LINIE)
    canvas.setLineWidth(0.5)
    canvas.line(20*mm, 15*mm, A4[0] - 20*mm, 15*mm)
    canvas.restoreState()

def kpi(zahl, label, vergleich):
    inner = [[Paragraph(zahl, KPIZ)], [Paragraph(label, KPIL)], [Paragraph(vergleich, KPIV)]]
    t = Table(inner, colWidths=[49*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), KARTE),
        ('LEFTPADDING', (0,0), (-1,-1), 9), ('RIGHTPADDING', (0,0), (-1,-1), 9),
        ('TOPPADDING', (0,0), (0,0), 9), ('BOTTOMPADDING', (0,-1), (-1,-1), 9),
        ('TOPPADDING', (0,1), (-1,-1), 1), ('BOTTOMPADDING', (0,0), (-1,-2), 1),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    return t

def liste(punkte):
    return [Paragraph(x, LI, bulletText='·') for x in punkte]

doc = BaseDocTemplate('docs/berichte/SEO-Bericht-2026-09.pdf',
                      pagesize=A4, title='Tierbestattung Memoria - SEO-Bericht September 2026',
                      author='Stolz Marketing', subject='SEO-Bericht',
                      leftMargin=20*mm, rightMargin=20*mm, topMargin=18*mm, bottomMargin=20*mm)
rahmen = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='n',
               leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
doc.addPageTemplates([PageTemplate(id='A', frames=[rahmen], onPage=seite)])

s = []
s.append(Paragraph('SEO-Bericht September 2026', H1))
s.append(Paragraph('Tierbestattung Memoria · erstellt am 1. Oktober 2026 von Stolz Marketing', SUB))

s.append(Paragraph('Die Zahlen auf einen Blick', H2))
s.append(Paragraph(
    'Verglichen wird September mit August. Quelle ist die Google Search Console, '
    'also Googles eigene Messung.', P))
s.append(Spacer(1, 7))
k = Table([[kpi('387', 'Besucher über Google', '274 im August'),
            kpi('4.954', 'Anzeigen in der Suche', '3.119 im August'),
            kpi('17', 'Seiten bei Google', '9 im August')]],
          colWidths=[55*mm, 55*mm, 55*mm])
k.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'),
                       ('LEFTPADDING', (0,0), (-1,-1), 0),
                       ('RIGHTPADDING', (0,0), (-1,-1), 6)]))
s.append(k)
s.append(Spacer(1, 11))
s.append(Paragraph(
    '<b>Wie viel davon ist auf unsere Arbeit zurückzuführen?</b> Ehrlicherweise '
    'nur ein Teil, und das lässt sich beziffern. Die neuen Seiten sind erst am '
    '11. September online gegangen – also für 19 der 30 Tage. In dieser Zeit haben '
    'sie <b>3.257 Anzeigen und 38 Besucher</b> erzeugt. Der Zuwachs insgesamt '
    'beträgt aber 113 Besucher. Das heißt: Rund ein Drittel des Zuwachses kommt '
    'nachweislich von den neuen Seiten, zwei Drittel kommen von der Startseite '
    'und aus Suchen nach dem Namen „Memoria" – und die hängen eher an Ihrem Ruf '
    'und an Empfehlungen als an unserer Arbeit.', P))
s.append(Paragraph(
    '<b>Der Vergleichsmonat ist außerdem unsauber.</b> Die neue Website ist am '
    '24. August live gegangen; bis dahin lief die alte. Ein Teil der Verbesserung '
    'geht also auf den Relaunch selbst zurück, nicht auf die Arbeit des '
    'vergangenen Monats.', P))

s.extend([
    Paragraph('Was im September umgesetzt wurde', H2),
    Paragraph(
        'Der Schwerpunkt lag darauf, dass es für jede wichtige Frage eine eigene Seite gibt. '
        'Vorher stand alles auf der Startseite – Google kann eine Startseite aber nur für '
        '<i>ein</i> Thema gut platzieren.', P),
    *liste([
        '<b>Vier alte Seitenadressen zurückgeholt.</b> Preise, Leistungen, Kontakt und Anfahrt '
        'waren bei Google seit Jahren bekannt, führten aber nur noch auf die Startseite. '
        'Sie sind jetzt wieder eigene Seiten mit ausführlichem Inhalt.',
        '<b>Sieben neue Seiten erstellt:</b> Tierkrematorium Laudenbach sowie '
        'Tierbestattung Bergstraße, Odenwald, Weinheim und Einhausen, dazu ein Vergleich '
        '„Einzel- oder Gemeinschaftskremierung" und eine Seite für den Fall, dass ein '
        'Tier nachts stirbt.',
        '<b>Ihre Google-Bewertungen sichtbar gemacht.</b> 4,9 Sterne aus 186 Bewertungen '
        'stehen jetzt direkt im ersten Bildschirm und in einem eigenen Abschnitt. Sobald '
        'Sie uns einzelne Bewertungen im Wortlaut schicken, laufen diese dort mit.',
        '<b>Das Einzugsgebiet sichtbar gemacht.</b> Bisher stand nirgends auf der Website, '
        'wohin Memoria fährt. Jetzt steht es auf der Startseite und auf der Kontaktseite.',
        '<b>Preise nach Tierart beantwortet.</b> Viele Menschen suchen nach „was kostet '
        'die Einäscherung eines Hundes" oder „Kaninchen einäschern Kosten". Dafür gibt es '
        'jetzt eigene Abschnitte mit konkreten Beträgen.',
        '<b>Technische Altlasten beseitigt.</b> Zwei Fehlerseiten aus der Zeit der alten '
        'Website und eine veraltete Sitemap-Anmeldung von 2022 wurden korrigiert.',
    ]),
])

s.extend([
    Paragraph('Was wir dabei gelernt haben', H2),
    *liste([
        '<b>Die meisten Suchenden kennen Memoria bereits.</b> 342 der 402 Klicks entfallen auf '
        'Suchen nach dem Namen. Das spricht für den guten Ruf – das Wachstumspotenzial liegt '
        'aber bei denen, die Memoria noch nicht kennen.',
        '<b>Beim Thema Kosten entsteht die größte Lücke.</b> 113 Suchanfragen rund um Preise '
        'erzeugten 417 Anzeigen, aber keinen einzigen Klick. Hier wurde im September '
        'nachgebessert; die Wirkung zeigt sich im Oktober.',
        '<b>Handy schlägt Computer deutlich.</b> Am Handy liegt Memoria auf Position 5,3, am '
        'Computer auf Position 19,9. Die meisten Menschen suchen in dieser Situation mobil – '
        'das passt gut, erklärt aber den Unterschied.',
    ]),
])

s.extend([
    Paragraph('Womit zu rechnen ist', H2),
    Paragraph(
        'Wir halten es für wichtig, das vorab zu sagen: <b>Die Zahlen können im Oktober '
        'auch wieder schlechter aussehen.</b> Dafür gibt es drei nachvollziehbare Gründe.', P),
    *liste([
        '<b>Nach einem Website-Umzug schwanken die Werte monatelang.</b> Google sortiert '
        'eine Website nach einem Relaunch neu ein. Schwankungen in beide Richtungen sind '
        'über drei bis sechs Monate normal und kein Alarmzeichen.',
        '<b>Alte und neue Seitenadressen laufen noch parallel.</b> Google kennt im Moment '
        'beide Varianten und verteilt die Bewertung auf zwei Adressen. Bis das '
        'zusammengeführt ist, sieht die durchschnittliche Platzierung schlechter aus, '
        'als sie ist.',
        '<b>Neue Seiten starten weit hinten.</b> Jede der sieben neuen Seiten beginnt auf '
        'einer schlechten Position und arbeitet sich über Wochen nach vorn. Solange das '
        'läuft, drücken sie den Durchschnitt.',
    ]),
    Paragraph(
        '<b>Unser Vorschlag für die Bewertung:</b> nicht Monat für Monat vergleichen, sondern '
        'nach drei Monaten – und dabei gezielt auf die Besucher schauen, die <i>nicht</i> nach '
        '„Memoria" gesucht haben. Das ist die Zahl, die unsere Arbeit tatsächlich abbildet. '
        'Aktuell sind das 60 von rund 400 Besuchern.', P),
])

s.extend([
    Paragraph('Was als Nächstes ansteht', H2),
    *liste([
        '<b>Einzelne Bewertungen einbauen.</b> Die Gesamtnote steht jetzt auf der Website. '
        'Was fehlt, sind vier bis sechs Bewertungen im Wortlaut – die wirken erfahrungsgemäß '
        'deutlich stärker als eine Zahl allein.',
        '<b>Die Kostenseite beobachten.</b> Rund um Preise gab es im September 417 Anzeigen '
        'und keinen einzigen Besucher. Wir haben nachgebessert; ob es wirkt, zeigt sich im '
        'Oktober.',
        '<b>Weitere Orte mit Augenmaß.</b> Für Weinheim und Einhausen gibt es jetzt eigene '
        'Seiten. Mannheim, Heidelberg und Worms sind in den Zahlen bisher sehr klein – wir '
        'bauen dort erst Seiten, wenn sich zeigt, dass es sich lohnt.',
        '<b>Pferdekremierung klären.</b> Es wird danach gesucht, aber es gibt bewusst noch keine '
        'Seite dazu – erst muss feststehen, was genau angeboten wird.',
    ]),
])

s.append(KeepTogether([
    Paragraph('Themen für unseren Termin', H2),
    Paragraph('Wir gehen den Bericht in den nächsten Tagen gemeinsam durch. Für die folgenden '
              'Punkte brauchen wir Angaben von Ihnen – wir schreiben bewusst nichts auf die '
              'Website, was wir nicht sicher wissen. Am Telefon ist das in zehn Minuten '
              'geklärt:', P),
    *liste([
        'Kostet die Abholung extra – und wenn ja, wie viel?',
        'Wann und wie wird bezahlt?',
        'Wie lange dauert es ungefähr, bis die Urne zurück ist?',
        'Was sollten Tierhalter tun, bis jemand vor Ort ist? (Fachliche Angabe)',
        'Bietet Memoria auch eine Beisetzung oder einen Tierfriedhof an, oder ausschließlich '
        'die Kremierung? (Danach wird häufig gesucht.)',
        'Vier bis sechs Google-Bewertungen, die wir im Wortlaut zeigen dürfen.',
    ]),
    Spacer(1, 9),
    Paragraph('Jede dieser Antworten lässt sich sofort einbauen und beantwortet eine Frage, '
              'die Menschen bei Google tatsächlich stellen. Wir melden uns mit '
              'Terminvorschlägen bei Ihnen.', FUSS),
]))

doc.build(s)
print('PDF erstellt')
