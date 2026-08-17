#!/usr/bin/env python3
"""Builds the Nairi cost-recovery invoice + covering letter as print-ready HTML.

Amounts come from montec/docs/nairi-cost-recovery.md. Requisite fields that the
owner has not supplied yet are rendered as visible blanks, so a draft is
obviously a draft and no placeholder can be mistaken for real data.
"""
import base64, io, os, sys

ROOT = '/home/user/memorycare'
FONTS = f'{ROOT}/montec/site/public/fonts'
OUT = os.path.dirname(os.path.abspath(__file__))

DRAFT = '--final' not in sys.argv

def b64(path):
    return base64.b64encode(open(path, 'rb').read()).decode()

CORMORANT = b64(f'{FONTS}/co3bmX5slCNuHLi8bLeY9MK7whWMhyjYqXtK.woff2')
INTER = b64(f'{FONTS}/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa1ZL7.woff2')
# Neither Cormorant nor Inter carries U+058F (֏). Noto Sans Armenian does, and is
# scoped to the Armenian block only, so it never touches the Latin text.
ARM = b64(f'{FONTS}/ZgN7jOZKPa7CHqq0h37c7ReDUubm2SEdFXp7ig73qtTY5idbxZhVoDur.woff2')
LOGO = b64(f'{ROOT}/montec/assets/brand/logo/logo-black-on-white.png')

# ── the data ────────────────────────────────────────────────────────────────
CHARGED = [
    ('01', 'Emboss die — packaging', 'Cut for blind embossing of the presentation packaging.', '1', '35 000', '35 000'),
    ('02', 'Emboss die — Nairi 30th anniversary mark',
     'Nairi Insurance 30th-anniversary logo, for blind embossing on leather.', '1', '15 000', '15 000'),
    ('03', 'Emboss die set — personalisation',
     'Fixed line «Special Edition For» with a full Latin alphabet letter set, cut for individual name personalisation of the run.',
     '1', '80 000', '80 000'),
    ('04', 'Sample pieces — THE ACCESS',
     'Nine cardholders produced across the trial iterations for approval. Charged at production cost, not at the agreed programme unit price of 20 000 ֏.',
     '9', '12 000', '108 000'),
    ('05', 'Packaging development',
     'Four trial versions produced by an external supplier. The amount was held as a deposit refundable against placement of the full order, and was forfeited when the order did not proceed.',
     '4', '—', '115 000'),
]
TOTAL = '353 000'

NOT_CHARGED = [
    ("Craftsmen's labour for the sample production", 'not charged'),
    ('Logistics and delivery', 'not charged'),
    ('Artwork preparation, test impressions and sample photography', 'not charged'),
]

def blank(width='150px', label=''):
    return (f'<span class="blank" style="min-width:{width}">{label}</span>' if DRAFT
            else label)

CSS = f"""
@font-face{{font-family:'Cormorant';src:url(data:font/woff2;base64,{CORMORANT}) format('woff2');font-weight:300 600}}
@font-face{{font-family:'Inter';src:url(data:font/woff2;base64,{INTER}) format('woff2');font-weight:300 600}}
@font-face{{font-family:'ArmDram';src:url(data:font/woff2;base64,{ARM}) format('woff2');unicode-range:U+0530-058F}}
@page{{size:210mm 297mm;margin:0}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:'Inter','ArmDram',sans-serif;color:#141210;font-size:9pt;line-height:1.5;
  -webkit-font-smoothing:antialiased}}
.page{{width:210mm;height:297mm;padding:13mm 16mm 9mm;position:relative;
  page-break-after:always;background:#fff;display:flex;flex-direction:column}}
.page:last-child{{page-break-after:auto}}
.serif{{font-family:'Cormorant','ArmDram',Georgia,serif;font-weight:400}}
.head{{display:flex;justify-content:space-between;align-items:flex-start;
  border-bottom:0.8pt solid #B8975A;padding-bottom:5mm}}
.head img{{height:13mm}}
.doc-type{{text-align:right}}
.doc-type .t{{font-family:'Cormorant',serif;font-size:19pt;letter-spacing:.02em}}
.doc-type .m{{font-size:7.5pt;letter-spacing:.16em;text-transform:uppercase;color:#6F6F6F;margin-top:2mm}}
.parties{{display:grid;grid-template-columns:1fr 1fr;gap:10mm;margin-top:6mm}}
.lbl{{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;color:#B8975A;margin-bottom:2.5mm}}
.party b{{font-family:'Cormorant',serif;font-size:12.5pt;font-weight:500;display:block;margin-bottom:1.5mm}}
.party div{{color:#4A4A4A}}
.meta{{display:flex;gap:12mm;margin-top:5mm;padding:3mm 0;border-top:0.4pt solid #E4E0D8;
  border-bottom:0.4pt solid #E4E0D8}}
.meta .lbl{{margin-bottom:1.5mm}}
.ref{{margin-top:5mm}}
.ref p{{margin:0;max-width:150mm;color:#4A4A4A}}
table{{width:100%;border-collapse:collapse;margin-top:5mm}}
th{{font-size:7pt;letter-spacing:.18em;text-transform:uppercase;color:#B8975A;text-align:left;
  padding:0 0 2.5mm;border-bottom:0.8pt solid #B8975A;font-weight:500}}
td{{padding:2.1mm 0;border-bottom:0.4pt solid #EDEAE3;vertical-align:top}}
td.n{{width:9mm;color:#9A9488;font-variant-numeric:tabular-nums}}
td.q,th.q{{width:14mm;text-align:right;font-variant-numeric:tabular-nums}}
td.r,th.r{{width:22mm;text-align:right;font-variant-numeric:tabular-nums}}
td.a,th.a{{width:26mm;text-align:right;font-variant-numeric:tabular-nums}}
.item b{{font-weight:500;display:block}}
.item span{{color:#6F6F6F;font-size:8pt;line-height:1.4;display:block;margin-top:0.8mm}}
.band{{display:flex;justify-content:space-between;gap:12mm;margin-top:3mm}}
.totals{{width:84mm}}
.nc2{{flex:1;padding-top:1mm}}
.nc2 .line{{display:flex;justify-content:space-between;padding:0.9mm 0;color:#4A4A4A;font-size:8.5pt}}
.nc2 .line i{{font-style:normal;color:#8A857B;white-space:nowrap;padding-left:4mm}}
.totals .row{{display:flex;justify-content:space-between;padding:1.4mm 0}}
.totals .row.sum{{border-top:0.8pt solid #141210;margin-top:1mm;padding-top:3mm}}
.totals .row.sum .k{{font-family:'Cormorant',serif;font-size:13pt}}
.totals .row.sum .v{{font-family:'Cormorant','ArmDram',serif;font-size:17pt;font-variant-numeric:tabular-nums}}
.totals .muted{{color:#6F6F6F}}
.pay{{margin-top:auto;padding-top:4mm;border-top:0.4pt solid #E4E0D8;
  display:grid;grid-template-columns:1fr 1fr 1fr;gap:10mm;align-items:start}}
.sig-line{{width:60mm;border-bottom:0.4pt solid #141210;height:7mm}}
.foot{{margin-top:3mm;border-top:0.4pt solid #E4E0D8;padding-top:3mm;
  font-size:7pt;letter-spacing:.14em;text-transform:uppercase;color:#9A9488;
  display:flex;justify-content:space-between}}
.blank{{display:inline-block;border-bottom:0.5pt dashed #C0392B;min-height:3.6mm;
  color:#C0392B;font-size:7.5pt;letter-spacing:.05em}}
.draft{{position:absolute;top:11mm;right:18mm;font-size:7pt;letter-spacing:.24em;
  text-transform:uppercase;color:#C0392B}}
.letter p{{margin:0 0 4.5mm;max-width:152mm}}
.letter .greet{{margin-top:9mm}}
"""

def head(kind, meta):
    d = '<div class="draft">Draft — requisites pending</div>' if DRAFT else ''
    return f"""{d}<div class="head">
      <img src="data:image/png;base64,{LOGO}" alt="Montec">
      <div class="doc-type"><div class="t">{kind}</div><div class="m">{meta}</div></div>
    </div>"""

FROM = f"""<div class="party">
  <div class="lbl">From</div>
  <b>{blank('62mm','legal entity — FiCorp?')}</b>
  <div>{blank('62mm','registered address')}</div>
  <div>TIN (ՀՎՀՀ): {blank('34mm','')}</div>
  <div style="margin-top:2mm;color:#6F6F6F">Trading as MONTEC</div>
</div>"""

TO = f"""<div class="party">
  <div class="lbl">To</div>
  <b>Nairi Insurance {blank('30mm','legal form')}</b>
  <div>{blank('62mm','registered address')}</div>
  <div>TIN (ՀՎՀՀ): {blank('34mm','')}</div>
  <div style="margin-top:2mm;color:#6F6F6F">For the attention of {blank('44mm','name, title')}</div>
</div>"""

rows = ''.join(f"""<tr>
  <td class="n">{n}</td>
  <td class="item"><b>{title}</b><span>{desc}</span></td>
  <td class="q">{qty}</td><td class="r">{rate}</td><td class="a">{amt}</td>
</tr>""" for n, title, desc, qty, rate, amt in CHARGED)

nc = ''.join(f'<div class="line"><span>{a}</span><i>{b}</i></div>' for a, b in NOT_CHARGED)

invoice = f"""<div class="page">
  {head('Invoice', f'No. {blank("22mm","")} &nbsp;·&nbsp; {blank("30mm","date")}')}
  <div class="parties">{FROM}{TO}</div>

  <div class="meta">
    <div><div class="lbl">Currency</div>Armenian dram (֏)</div>
    <div><div class="lbl">VAT</div>Not applied</div>
    <div><div class="lbl">Payment due</div>{blank('34mm','e.g. 10 banking days')}</div>
  </div>

  <div class="ref">
    <div class="lbl">Reference</div>
    <p>Corporate programme — 500 × THE ACCESS cardholders at 20 000 ֏ per unit, personalised for the
    30th anniversary of Nairi Insurance, suspended indefinitely at the client's request. This invoice
    covers the costs already incurred in preparing it, as agreed, and carries no cancellation charge.</p>
  </div>

  <table>
    <thead><tr><th></th><th>Description</th><th class="q">Qty</th><th class="r">Rate</th><th class="a">Amount</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>

  <div class="band">
    <div class="nc2">
      <div class="lbl">Not charged</div>
      {nc}
    </div>
    <div class="totals">
      <div class="row"><span class="muted">Subtotal</span><span>{TOTAL} ֏</span></div>
      <div class="row"><span class="muted">VAT</span><span class="muted">Not applied</span></div>
      <div class="row sum"><span class="k">Total due</span><span class="v">{TOTAL} ֏</span></div>
    </div>
  </div>

  <div class="pay">
    <div>
      <div class="lbl">Payment details</div>
      <div>Bank: {blank('36mm','')}</div>
      <div>Account / IBAN: {blank('36mm','')}</div>
      <div>SWIFT: {blank('26mm','')}</div>
    </div>
    <div>
      <div class="lbl">Supporting documents</div>
      <div style="color:#4A4A4A;font-size:8.5pt">Supplier invoices and receipts for the items
      above are held and available on request.</div>
    </div>
    <div>
      <div class="lbl">For and on behalf of the supplier</div>
      <div class="sig-line"></div>
      <div style="margin-top:1.5mm">{blank('40mm','name, title')}</div>
    </div>
  </div>

  <div class="foot"><span>Montec · Batch 001</span><span>Page 1 of 1</span></div>
</div>"""

letter = f"""<div class="page letter">
  {head('Letter', 'Accompanying the invoice')}
  <div style="margin-top:10mm" class="lbl">To</div>
  <div class="party"><b>Nairi Insurance</b>
    <div>For the attention of {blank('50mm','name, title')}</div>
    <div style="margin-top:2mm">{blank('30mm','date')}</div>
  </div>

  <div style="margin-top:10mm">
    <p class="greet">Dear {blank('40mm','name')},</p>

    <p>Following our conversation, we are closing out the preparation stage of the
    30th-anniversary programme and enclose the invoice for the costs already incurred.</p>

    <p>It covers three things: the emboss dies cut for your marks and for the name
    personalisation, the nine sample cardholders produced across the trial iterations, and the
    four packaging versions developed with our supplier — an amount the supplier held as a
    deposit against the full order and did not return once the order was not placed. The samples
    are charged at production cost rather than at the programme price. We are not charging for
    our craftsmen's time, for logistics, or for the artwork and photography, and there is no
    cancellation charge of any kind.</p>

    <p>The dies and the approved packaging remain with us and stay ready. If the programme
    resumes, the preparation work is done and production can begin without repeating this stage —
    and these costs will be credited against that order.</p>

    <p>We are glad to have worked on this with you and hope to complete it when your side is
    ready.</p>

    <p style="margin-top:9mm">With respect,<br>
    {blank('50mm','name, title')}<br>
    <span style="color:#6F6F6F">Montec · {blank('40mm','entity')}</span></p>
  </div>

  <div class="foot" style="margin-top:auto"><span>Montec · Batch 001</span><span></span></div>
</div>"""

html = f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>{invoice}{letter}'
name = 'nairi-invoice-draft' if DRAFT else 'nairi-invoice'
io.open(f'{OUT}/{name}.html', 'w', encoding='utf-8').write(html)
print(f'{name}.html written, {len(html)//1024} KB')
