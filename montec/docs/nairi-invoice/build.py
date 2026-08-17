#!/usr/bin/env python3
"""Builds the Nairi cost-recovery invoice + covering letter as print-ready HTML.

  python3 build.py            # English draft   -> nairi-invoice-en-draft.html
  python3 build.py --hy       # Armenian draft  -> nairi-invoice-hy-draft.html
  python3 build.py --final    # blanks vanish, so fill the requisites in first

Amounts come from montec/docs/nairi-cost-recovery.md — that file is the record
of what the owner confirmed; this one only renders it.

Fonts: one stack serves both languages. Latin resolves to Cormorant/Inter,
Armenian falls through to the Noto Armenian faces, which also supply ֏ (U+058F)
— neither brand face has that glyph, and without them every dram sign in the
document silently becomes the wrong letter.
"""
import base64, io, os, sys

ROOT = '/home/user/memorycare'
FONTS = f'{ROOT}/montec/site/public/fonts'
OUT = os.path.dirname(os.path.abspath(__file__))

HY = '--hy' in sys.argv
CONFIRM = '--confirm' in sys.argv      # the letter that precedes the invoice
DRAFT = '--final' not in sys.argv
if CONFIRM:
    HY = True                          # the confirmation letter is Armenian only
# The Armenian edition is the working copy for the bookkeeper, so it is the
# invoice alone — a covering letter is for the client, not for accounting.
# Pass --letter to include it anyway (e.g. if the Armenian also goes to Nairi).
WITH_LETTER = (not HY) or ('--letter' in sys.argv)

sys.path.insert(0, OUT)
import hy as A


def b64(path):
    return base64.b64encode(open(path, 'rb').read()).decode()


CORMORANT = b64(f'{FONTS}/co3bmX5slCNuHLi8bLeY9MK7whWMhyjYqXtK.woff2')
INTER = b64(f'{FONTS}/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa1ZL7.woff2')
ARM_SANS = b64(f'{FONTS}/ZgN7jOZKPa7CHqq0h37c7ReDUubm2SEdFXp7ig73qtTY5idbxZhVoDur.woff2')
ARM_SERIF = b64(f'{FONTS}/3XFBEqMt3YoFsciDRZxptyCUKJmytZ0kVU-XvF7QaZuL85rnQ9bfH8E2ew.woff2')
LOGO = b64(f'{ROOT}/montec/assets/brand/logo/logo-black-on-white.png')

SUBTOTAL = '353 000'
GOODWILL = '– 70 600'
TOTAL = '282 400'

CHARGED_EN = [
    ('01', 'Emboss die — packaging',
     'Cut for blind embossing of the presentation packaging.', '1', '35 000', '35 000'),
    ('02', 'Emboss die — Nairi 30th anniversary mark',
     'Nairi Insurance 30th-anniversary logo, for blind embossing on leather.',
     '1', '15 000', '15 000'),
    ('03', 'Emboss die set — personalisation',
     'Fixed line «Special Edition For» with a full Latin alphabet letter set, cut for '
     'individual name personalisation of the run.', '1', '80 000', '80 000'),
    ('04', 'Sample pieces — THE ACCESS',
     'Nine cardholders produced across the trial iterations for approval. Charged at '
     'production cost, not at the agreed programme unit price of 20 000 ֏.',
     '9', '12 000', '108 000'),
    ('05', 'Packaging development',
     'Four trial versions produced by an external supplier. The amount was held as a '
     'deposit refundable against placement of the full order, and was forfeited when '
     'the order did not proceed.', '4', '—', '115 000'),
]
NOT_CHARGED_EN = [
    ("Craftsmen's labour for the sample production", 'not charged'),
    ('Logistics and delivery', 'not charged'),
    ('Artwork preparation, test impressions and sample photography', 'not charged'),
]
LETTER_EN = {
    'dear': 'Dear',
    'paras': [
        'Following our conversation, we are closing out the preparation stage of the '
        '30th-anniversary programme and enclose the invoice for the costs already incurred.',

        'It covers three things: the emboss dies cut for your marks and for the name '
        'personalisation, the nine sample cardholders produced across the trial iterations, '
        'and the four packaging versions developed with our supplier — an amount the supplier '
        'held as a deposit against the full order and did not return once the order was not '
        'placed. The samples are charged at production cost rather than at the programme '
        'price. We are not charging for our craftsmen&rsquo;s time, for logistics, or for the '
        'artwork and photography, and there is no cancellation charge of any kind.',

        'The dies and the approved packaging remain with us and stay ready. If the programme '
        'resumes, the preparation work is done and production can begin without repeating this '
        'stage — and these costs will be credited against that order.',

        'We are glad to have worked on this with you and hope to complete it when your side '
        'is ready.',
    ],
    'sign_off': 'With respect,',
}

EN = {
    'doc_invoice': 'Invoice', 'doc_invoice_meta': '', 'doc_letter': 'Letter',
    'doc_letter_meta': 'Accompanying the invoice',
    'no': 'No.', 'date': 'date', 'from': 'From', 'to': 'To',
    'trading_as': 'Trading as MONTEC', 'tin': 'TIN (ՀՎՀՀ)', 'attn': 'For the attention of',
    'currency': 'Currency', 'currency_v': 'Armenian dram (֏)',
    'vat': 'VAT', 'vat_v': 'Not applied',
    'due': 'Payment due', 'due_ph': 'e.g. 10 banking days',
    'reference': 'Reference',
    'ref_text': ('Corporate programme — 500 × THE ACCESS cardholders at 20 000 ֏ per unit, '
                 'personalised for the 30th anniversary of Nairi Insurance, suspended '
                 'indefinitely at the client&rsquo;s request. This invoice covers the costs '
                 'already incurred in preparing it, as agreed, and carries no cancellation '
                 'charge.'),
    'th_desc': 'Description', 'th_qty': 'Qty', 'th_rate': 'Rate', 'th_amount': 'Amount',
    'subtotal': 'Subtotal', 'total': 'Total due', 'not_charged': 'Not charged',
    'goodwill': 'Goodwill reduction — 20% of the costs carried by Montec',
    'pay_details': 'Payment details', 'bank': 'Bank', 'account': 'Account / IBAN',
    'swift': 'SWIFT', 'supporting': 'Supporting documents',
    'supporting_v': 'Supplier invoices and receipts for the items above are held and '
                    'available on request.',
    'signed_by': 'For and on behalf of the supplier', 'name_title': 'name, title',
    'legal_entity': 'legal entity — FiCorp?', 'address': 'registered address',
    'legal_form': 'legal form',
    'foot_left': 'Montec · Batch 001', 'foot_right': 'Page 1 of 1',
    'draft': 'Draft — requisites pending',
}

T = A.L if HY else EN
CHARGED = A.CHARGED_HY if HY else CHARGED_EN
NOT_CHARGED = A.NOT_CHARGED_HY if HY else NOT_CHARGED_EN
LETTER = A.LETTER_HY if HY else LETTER_EN
NAIRI = '«Նաիրի Ինշուրանս»' if HY else 'Nairi Insurance'

# Armenian all-caps at Latin tracking is shouty and inflates width; the design
# system eases it for hy, and the same applies on paper.
TRACK_LBL = '.10em' if HY else '.2em'
TRACK_TH = '.09em' if HY else '.18em'
# Armenian runs ~20% longer than the English at the same size, and the invoice
# page clips rather than paginates, so the hy edition is set a notch tighter.
BODY_PT = '8.5pt' if HY else '9pt'
BODY_LH = '1.45' if HY else '1.5'
DESC_PT = '7.5pt' if HY else '8pt'
ROW_PAD = '1.9mm' if HY else '2.1mm'
PAGE_PAD = '12mm 15mm 7mm' if HY else '13mm 16mm 9mm'
NC_PT = '8pt' if HY else '8.5pt'
SIG_H = '6mm' if HY else '7mm'


def blank(width='150px', label=''):
    return (f'<span class="blank" style="min-width:{width}">{label}</span>' if DRAFT
            else label)


CSS = f"""
@font-face{{font-family:'Cormorant';src:url(data:font/woff2;base64,{CORMORANT}) format('woff2');font-weight:300 600}}
@font-face{{font-family:'Inter';src:url(data:font/woff2;base64,{INTER}) format('woff2');font-weight:300 600}}
@font-face{{font-family:'ArmSans';src:url(data:font/woff2;base64,{ARM_SANS}) format('woff2');font-weight:300 600}}
@font-face{{font-family:'ArmSerif';src:url(data:font/woff2;base64,{ARM_SERIF}) format('woff2');font-weight:300 600}}
@page{{size:210mm 297mm;margin:0}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:'Inter','ArmSans',sans-serif;color:#141210;font-size:{BODY_PT};
  line-height:{BODY_LH};-webkit-font-smoothing:antialiased}}
.page{{width:210mm;height:296.5mm;overflow:hidden;padding:{PAGE_PAD};position:relative;
  background:#fff;display:flex;flex-direction:column}}
.page + .page{{page-break-before:always}}
.head{{display:flex;justify-content:space-between;align-items:flex-start;
  border-bottom:0.8pt solid #B8975A;padding-bottom:5mm}}
.head img{{height:13mm}}
.doc-type{{text-align:right}}
.doc-type .t{{font-family:'Cormorant','ArmSerif',serif;font-size:19pt;letter-spacing:.02em}}
.doc-type .m{{font-size:7.5pt;letter-spacing:.14em;text-transform:uppercase;color:#6F6F6F;margin-top:2mm}}
.parties{{display:grid;grid-template-columns:1fr 1fr;gap:10mm;margin-top:6mm}}
.lbl{{font-size:7pt;letter-spacing:{TRACK_LBL};text-transform:uppercase;color:#B8975A;margin-bottom:2.5mm}}
.party b{{font-family:'Cormorant','ArmSerif',serif;font-size:12.5pt;font-weight:500;display:block;margin-bottom:1.5mm}}
.party div{{color:#4A4A4A}}
.meta{{display:flex;gap:12mm;margin-top:5mm;padding:3mm 0;border-top:0.4pt solid #E4E0D8;
  border-bottom:0.4pt solid #E4E0D8}}
.meta .lbl{{margin-bottom:1.5mm}}
.ref{{margin-top:5mm}}
.ref p{{margin:0;max-width:152mm;color:#4A4A4A}}
table{{width:100%;border-collapse:collapse;margin-top:5mm}}
th{{font-size:7pt;letter-spacing:{TRACK_TH};text-transform:uppercase;color:#B8975A;text-align:left;
  padding:0 0 2.5mm;border-bottom:0.8pt solid #B8975A;font-weight:500}}
td{{padding:{ROW_PAD} 0;border-bottom:0.4pt solid #EDEAE3;vertical-align:top}}
td.n{{width:9mm;color:#9A9488;font-variant-numeric:tabular-nums}}
td.q,th.q{{width:15mm;text-align:right;font-variant-numeric:tabular-nums}}
td.r,th.r{{width:22mm;text-align:right;font-variant-numeric:tabular-nums}}
td.a,th.a{{width:26mm;text-align:right;font-variant-numeric:tabular-nums}}
.item b{{font-weight:500;display:block}}
.item span{{color:#6F6F6F;font-size:{DESC_PT};line-height:1.38;display:block;margin-top:0.8mm}}
.band{{display:flex;justify-content:space-between;gap:12mm;margin-top:3mm}}
.totals{{width:86mm}}
.nc2{{flex:1;padding-top:1mm}}
.nc2 .line{{display:flex;justify-content:space-between;padding:0.8mm 0;color:#4A4A4A;font-size:{NC_PT}}}
.nc2 .line i{{font-style:normal;color:#8A857B;white-space:nowrap;padding-left:4mm}}
.totals .row{{display:flex;justify-content:space-between;padding:1.4mm 0}}
.totals .row.sum{{border-top:0.8pt solid #141210;margin-top:1mm;padding-top:3mm}}
.totals .row.sum .k{{font-family:'Cormorant','ArmSerif',serif;font-size:{'11pt' if HY else '13pt'}}}
.totals .row.sum .v{{font-family:'Cormorant','ArmSerif',serif;font-size:17pt;font-variant-numeric:tabular-nums}}
.totals .muted{{color:#6F6F6F}}
.pay{{margin-top:auto;padding-top:4mm;border-top:0.4pt solid #E4E0D8;
  display:grid;grid-template-columns:1fr 1fr 1fr;gap:10mm;align-items:start}}
.sig-line{{width:58mm;border-bottom:0.4pt solid #141210;height:{SIG_H}}}
.foot{{margin-top:3mm;border-top:0.4pt solid #E4E0D8;padding-top:3mm;
  font-size:7pt;letter-spacing:.12em;text-transform:uppercase;color:#9A9488;
  display:flex;justify-content:space-between}}
.blank{{display:inline-block;border-bottom:0.5pt dashed #C0392B;min-height:3.6mm;
  color:#C0392B;font-size:7.5pt;letter-spacing:.05em}}
.draft{{position:absolute;top:11mm;right:16mm;font-size:7pt;letter-spacing:.2em;
  text-transform:uppercase;color:#C0392B}}
.letter p{{margin:0 0 4.5mm;max-width:152mm}}
.clist{{margin:0 0 5mm;max-width:152mm;border-top:0.4pt solid #E4E0D8}}
.cline{{display:flex;justify-content:space-between;gap:8mm;padding:2mm 0;
  border-bottom:0.4pt solid #EDEAE3}}
.cline i{{font-style:normal;white-space:nowrap;font-variant-numeric:tabular-nums}}
.cline.sub{{border-bottom:0;padding-top:3mm;font-weight:500}}
.cline.gw{{border-bottom:0.8pt solid #141210;padding-bottom:3mm;color:#4A4A4A}}
.cline.tot{{border-bottom:0;padding-top:3mm;font-family:'Cormorant','ArmSerif',serif;
  font-size:13pt}}
.cline.tot i{{font-family:'Cormorant','ArmSerif',serif;font-size:15pt}}
.letter .greet{{margin-top:9mm}}
"""


def head(kind, meta):
    d = f'<div class="draft">{T["draft"]}</div>' if DRAFT else ''
    m = f'<div class="m">{meta}</div>' if meta else ''
    return f"""{d}<div class="head">
      <img src="data:image/png;base64,{LOGO}" alt="Montec">
      <div class="doc-type"><div class="t">{kind}</div>{m}</div>
    </div>"""


FROM = f"""<div class="party">
  <div class="lbl">{T['from']}</div>
  <b>{blank('60mm', T['legal_entity'])}</b>
  <div>{blank('60mm', T['address'])}</div>
  <div>{T['tin']}: {blank('32mm','')}</div>
  <div style="margin-top:2mm;color:#6F6F6F">{T['trading_as']}</div>
</div>"""

TO = f"""<div class="party">
  <div class="lbl">{T['to']}</div>
  <b>{NAIRI} {blank('26mm', T['legal_form'])}</b>
  <div>{blank('60mm', T['address'])}</div>
  <div>{T['tin']}: {blank('32mm','')}</div>
  <div style="margin-top:2mm;color:#6F6F6F">{T['attn']} {blank('40mm', T['name_title'])}</div>
</div>"""

rows = ''.join(f"""<tr>
  <td class="n">{n}</td>
  <td class="item"><b>{title}</b><span>{desc}</span></td>
  <td class="q">{qty}</td><td class="r">{rate}</td><td class="a">{amt}</td>
</tr>""" for n, title, desc, qty, rate, amt in CHARGED)

nc = ''.join(f'<div class="line"><span>{a}</span><i>{b}</i></div>' for a, b in NOT_CHARGED)

invoice = f"""<div class="page">
  {head(T['doc_invoice'], T['doc_invoice_meta'])}
  <div style="text-align:right;margin-top:3mm;font-size:8.5pt">
    {T['no']} {blank('20mm','')} &nbsp;·&nbsp; {blank('28mm', T['date'])}
  </div>
  <div class="parties">{FROM}{TO}</div>

  <div class="meta">
    <div><div class="lbl">{T['currency']}</div>{T['currency_v']}</div>
    <div><div class="lbl">{T['vat']}</div>{T['vat_v']}</div>
    <div><div class="lbl">{T['due']}</div>{blank('34mm', T['due_ph'])}</div>
  </div>

  <div class="ref">
    <div class="lbl">{T['reference']}</div>
    <p>{T['ref_text']}</p>
  </div>

  <table>
    <thead><tr><th></th><th>{T['th_desc']}</th><th class="q">{T['th_qty']}</th>
      <th class="r">{T['th_rate']}</th><th class="a">{T['th_amount']}</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>

  <div class="band">
    <div class="nc2"><div class="lbl">{T['not_charged']}</div>{nc}</div>
    <div class="totals">
      <div class="row"><span class="muted">{T['subtotal']}</span><span>{SUBTOTAL} ֏</span></div>
      <div class="row"><span class="muted" style="max-width:52mm;line-height:1.3">{T['goodwill']}</span><span>{GOODWILL} ֏</span></div>
      <div class="row"><span class="muted">{T['vat']}</span><span class="muted">{T['vat_v']}</span></div>
      <div class="row sum"><span class="k">{T['total']}</span><span class="v">{TOTAL} ֏</span></div>
    </div>
  </div>

  <div class="pay">
    <div>
      <div class="lbl">{T['pay_details']}</div>
      <div>{T['bank']}: {blank('30mm','')}</div>
      <div>{T['account']}: {blank('30mm','')}</div>
      <div>{T['swift']}: {blank('24mm','')}</div>
    </div>
    <div>
      <div class="lbl">{T['supporting']}</div>
      <div style="color:#4A4A4A;font-size:{NC_PT}">{T['supporting_v']}</div>
    </div>
    <div>
      <div class="lbl">{T['signed_by']}</div>
      <div class="sig-line"></div>
      <div style="margin-top:1.5mm">{blank('40mm', T['name_title'])}</div>
    </div>
  </div>

  <div class="foot"><span>{T['foot_left']}</span><span>{T['foot_right']}</span></div>
</div>"""

paras = ''.join(f'<p>{p}</p>' for p in LETTER['paras'])

letter = f"""<div class="page letter">
  {head(T['doc_letter'], T['doc_letter_meta'])}
  <div style="margin-top:10mm" class="lbl">{T['to']}</div>
  <div class="party"><b>{NAIRI}</b>
    <div>{T['attn']} {blank('44mm', T['name_title'])}</div>
    <div style="margin-top:2mm">{blank('28mm', T['date'])}</div>
  </div>

  <div style="margin-top:10mm">
    <p class="greet">{LETTER['dear']} {blank('36mm', T['name_title'].split(',')[0])},</p>
    {paras}
    <p style="margin-top:9mm">{LETTER['sign_off']}<br>
    {blank('46mm', T['name_title'])}<br>
    <span style="color:#6F6F6F">Montec · {blank('36mm', T['legal_entity'].split('—')[0].strip())}</span></p>
  </div>

  <div class="foot" style="margin-top:auto"><span>{T['foot_left']}</span><span></span></div>
</div>"""

C = A.CONFIRM_HY
c_lines = ''.join(
    f'<div class="cline"><span>{a}</span><i>{b}</i></div>' for a, b in C['lines'])
c_intro = ''.join(f'<p>{p}</p>' for p in C['intro'])
c_body = ''.join(f'<p>{p}</p>' for p in C['body'])

confirm = f"""<div class="page letter">
  {head(C['doc'], C['meta'])}
  <div style="margin-top:9mm" class="lbl">{T['to']}</div>
  <div class="party"><b>{C['to_org']}</b>
    <div>{C['to_name']} — {C['to_role']}</div>
    <div style="margin-top:2mm">{blank('28mm', T['date'])}</div>
  </div>

  <div style="margin-top:8mm">
    <p class="greet" style="margin-top:0">{C['greet']}</p>
    {c_intro}

    <div class="clist">
      {c_lines}
      <div class="cline sub"><span>{C['subtotal'][0]}</span><i>{C['subtotal'][1]}</i></div>
      <div class="cline gw"><span>{C['goodwill'][0]}</span><i>{C['goodwill'][1]}</i></div>
      <div class="cline tot"><span>{C['total'][0]}</span><i>{C['total'][1]}</i></div>
    </div>

    {c_body}

    <p style="margin-top:8mm">{C['sign_off']}<br>
    {blank('46mm', T['name_title'])}<br>
    <span style="color:#6F6F6F">Montec · {blank('36mm', T['legal_entity'])}</span></p>
  </div>

  <div class="foot" style="margin-top:auto"><span>{T['foot_left']}</span><span></span></div>
</div>"""

body_html = confirm if CONFIRM else (invoice + (letter if WITH_LETTER else ''))
html = (f'<!doctype html><html lang="{"hy" if HY else "en"}"><meta charset="utf-8">'
        f'<style>{CSS}</style>{body_html}</html>')
name = ('nairi-confirmation-hy' if CONFIRM
        else f'nairi-invoice-{"hy" if HY else "en"}') + ('-draft' if DRAFT else '')
io.open(f'{OUT}/{name}.html', 'w', encoding='utf-8').write(html)
print(f'{name}.html written, {len(html)//1024} KB')
