#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MemoryCare — compliance-route generator.

Emits the ten routes owned by the compliance engineer, in three locales,
plus the shared footer include. Every visible string is read from
rebrand/strings/<loc>.json by key and the key is written into an HTML
comment beside it. No prose is typed into this file except the two
[BLOCKED] build markers, which are deliberately not site copy.

Run:  python3 rebrand/site/_includes/build-compliance-pages.py
"""

import json, html, pathlib

ROOT   = pathlib.Path(__file__).resolve().parents[2]        # rebrand/
SITE   = ROOT / "site"
STR    = ROOT / "strings"
INC    = SITE / "_includes"

# folder name -> lang / hreflang code.  `am` is Amharic; the folder name is a
# lead instruction, the lang attribute is not negotiable.  See RECONCILIATION §12.
LOCALES = {"en": "en", "ru": "ru", "am": "hy"}

# ---------------------------------------------------------------------------
# §4.10.11 — the payment-system marks.
# WHICH SCHEMES ARE ACCEPTED IS NOT CONFIRMED.  The strip is data: put the
# scheme rows in here and the footer renders them, in colour, unmodified, at
# the minimum size each scheme's own brand rules specify.  Until the owner
# confirms the set, the strip renders as a visible gap.  Nothing is guessed.
# Row shape: {"id","alt","src","w","h"}   w/h are the scheme's own minimum.
PAYMENT_SCHEMES: list = []
BLOCKED_SCHEMES = ("[BLOCKED — which card schemes are accepted is not "
                   "confirmed; the colour marks required by Ameriabank §4.10.11 "
                   "cannot be chosen for us. → Davit, from the acquiring contract]")
BLOCKED_ROUTE   = ("[BLOCKED — this route has no strings in en/ru/am.json. It is "
                   "built from approved keys written for other pages so that it is "
                   "real and true; it needs its own copy. → content lead]")

# ---------------------------------------------------------------------------
# Route table.  path relative to the locale folder.
ROUTES = [
    "about.html", "history.html", "mission.html", "values.html",
    "legal/restrictions.html", "legal/privacy.html", "legal/cookies.html",
    "legal/refunds.html", "legal/terms.html", "legal/security.html",
]

# Routes owned by the other two engineers, linked from header and footer.
NAV = [("nav.about", "about.html"), ("nav.prices", "prices.html"),
       ("nav.how", "how-it-works.html"), ("nav.report", "sample-report.html"),
       ("nav.family", "index.html#family"), ("nav.contacts", "contact.html")]

FOOTER_LEGAL = [("footer.legal.terms", "legal/terms.html"),
                ("footer.legal.refund", "legal/refunds.html"),
                ("footer.legal.privacy", "legal/privacy.html"),
                ("footer.legal.cookies", "legal/cookies.html"),
                ("footer.legal.security", "legal/security.html"),
                ("footer.legal.limitations", "legal/restrictions.html")]

FOOTER_COMPANY = [("nav.about", "about.html"),
                  ("common.entity.registeredYear", "history.html"),
                  ("home.protocol.h2", "mission.html"),
                  ("how.includes.h2", "values.html"),
                  ("nav.contacts", "contact.html")]

FOOTER_SVC = ["footer.svc.inspection", "footer.svc.single", "footer.svc.four",
              "footer.svc.six", "footer.svc.special"]


class Loc:
    def __init__(self, folder):
        self.folder = folder
        self.lang = LOCALES[folder]
        self.d = json.load(open(STR / f"{folder}.json", encoding="utf-8"))

    def raw(self, key):
        if key not in self.d:
            raise KeyError(f"{self.folder}: missing string key {key}")
        return self.d[key]

    def t(self, key):
        """Escaped text plus the key in a comment, for inline use."""
        return f"<!-- {key} -->{html.escape(self.raw(key))}"

    def el(self, tag, key, cls=None, extra=""):
        c = f' class="{cls}"' if cls else ""
        return (f"<!-- {key} -->\n<{tag}{c}{extra}>"
                f"{html.escape(self.raw(key))}</{tag}>")

    def li(self, key):
        return f"<!-- {key} --><li>{html.escape(self.raw(key))}</li>"

    def has(self, key):
        return key in self.d


def url(folder, path):
    return f"/{folder}/{path}"


# ---------------------------------------------------------------------------
# HEADER
def header(L, current):
    f = L.folder
    items = []
    for key, path in NAV:
        cur = ' aria-current="page"' if path == current else ""
        items.append(f'<li class="mc-nav__item">'
                     f'<!-- {key} -->'
                     f'<a class="mc-nav__link" href="{url(f, path)}"{cur}>'
                     f'{html.escape(L.raw(key))}</a></li>')
    langs = []
    for other, code in (("am","hy"),("en","en"),("ru","ru")):
        key = f"header.lang.{code}"
        if other == f:
            langs.append(f'<li class="mc-lang__item"><!-- {key} -->'
                         f'<a class="mc-lang__link" href="{url(other, current)}" '
                         f'hreflang="{code}" lang="{code}" aria-current="true">'
                         f'{html.escape(L.raw(key))}</a></li>')
        else:
            langs.append(f'<li class="mc-lang__item"><!-- {key} -->'
                         f'<a class="mc-lang__link" href="{url(other, current)}" '
                         f'hreflang="{code}" lang="{code}">'
                         f'{html.escape(L.raw(key))}</a></li>')
    return f"""<header class="mc-header">
  <div class="mc-page mc-header__inner">
    <a class="mc-header__brand" href="{url(f, '')}">
      <img class="mc-header__mark" src="/assets/brand/MemoryCare_logo-mark_color.svg" alt="">
      <!-- common.brand --><span class="mc-h4">{html.escape(L.raw('common.brand'))}</span>
      <!-- common.descriptor --><span class="mc-sr-only">{html.escape(L.raw('common.descriptor'))}</span>
    </a>
    <nav class="mc-nav" aria-label="{html.escape(L.raw('common.descriptor'))}">
      <ul class="mc-nav__list">
        {'''
        '''.join(items)}
      </ul>
    </nav>
    <div class="mc-header__actions">
      <nav class="mc-lang" aria-label="{html.escape(L.raw('header.lang.label'))}">
        <!-- header.lang.label -->
        <ul class="mc-lang__list">
          {'''
          '''.join(langs)}
        </ul>
      </nav>
      <!-- header.signin -->
      <a class="mc-btn mc-btn--quiet" href="{url(f, 'account/')}">{html.escape(L.raw('header.signin'))}</a>
      <!-- header.cta -->
      <a class="mc-btn mc-btn--primary" href="{url(f, 'index.html#consultation')}">{html.escape(L.raw('header.cta'))}</a>
    </div>
  </div>
</header>"""


# ---------------------------------------------------------------------------
# FOOTER  — one component, identical on every page and in every locale.
# Carries Ameriabank §4.10.2 (entity, registration number, taxpayer number,
# legal address, phones, e-mail) and §4.10.11 (the payment-system marks).
def footer(L):
    f = L.folder

    def col(head_key, rows):
        return (f'<div>\n      <!-- {head_key} -->\n'
                f'      <h2 class="mc-footer__heading">{html.escape(L.raw(head_key))}</h2>\n'
                f'      <ul class="mc-footer__list">\n        '
                + "\n        ".join(rows) + "\n      </ul>\n    </div>")

    company = [f'<li><!-- {k} --><a href="{url(f, p)}">{html.escape(L.raw(k))}</a></li>'
               for k, p in FOOTER_COMPANY]
    legal = [f'<li><!-- {k} --><a href="{url(f, p)}">{html.escape(L.raw(k))}</a></li>'
             for k, p in FOOTER_LEGAL]
    svc = [f'<li><!-- {k} --><a href="{url(f, "prices.html")}">{html.escape(L.raw(k))}</a></li>'
           for k in FOOTER_SVC]
    svc.append(f'<li class="mc-legal"><!-- common.currencyLine -->'
               f'{html.escape(L.raw("common.currencyLine"))}</li>')

    contact = []
    for who in ("davit", "hayk"):
        n, r = f"common.founder.{who}.name", f"common.founder.{who}.roleShort"
        ph, tel = f"common.founder.{who}.phone", f"common.founder.{who}.tel"
        contact.append(
            f'<li class="mc-footer__contact">'
            f'<!-- {n} --><span>{html.escape(L.raw(n))}</span>, '
            f'<!-- {r} --><span class="mc-text-secondary">{html.escape(L.raw(r))}</span><br>'
            f'<!-- {ph} / {tel} --><a href="{html.escape(L.raw(tel))}">'
            f'{html.escape(L.raw(ph))}</a></li>')
    contact.append(f'<li><!-- common.email -->'
                   f'<a href="mailto:{html.escape(L.raw("common.email"))}">'
                   f'{html.escape(L.raw("common.email"))}</a></li>')
    contact.append(f'<li class="mc-legal"><!-- common.channels -->'
                   f'{html.escape(L.raw("common.channels"))}</li>')
    contact.append(f'<li class="mc-legal"><!-- common.hours -->'
                   f'{html.escape(L.raw("common.hours"))}</li>')
    contact.append(f'<li class="mc-legal"><!-- common.entity.addressLabel / '
                   f'common.entity.address -->'
                   f'{html.escape(L.raw("common.entity.addressLabel"))}: '
                   f'{html.escape(L.raw("common.entity.address"))}</li>')

    # --- §4.10.11 payment-system marks -------------------------------------
    if PAYMENT_SCHEMES:
        marks = "\n        ".join(
            f'<li><img class="mc-paymarks__mark" src="{s["src"]}" '
            f'alt="{html.escape(s["alt"])}" width="{s["w"]}" height="{s["h"]}"></li>'
            for s in PAYMENT_SCHEMES)
    else:
        marks = f'<li class="mc-paymarks__note" data-blocked="schemes">{html.escape(BLOCKED_SCHEMES)}</li>'

    return f"""<footer class="mc-footer">
  <div class="mc-page">
    <div class="mc-footer__grid">
    {col('footer.col.company', company)}
    {col('footer.col.services', svc)}
    {col('footer.col.legal', legal)}
    {col('footer.contactHeading', contact)}
    </div>

    <section aria-labelledby="mc-paymarks-heading">
      <!-- footer.payment.heading -->
      <h2 class="mc-footer__heading" id="mc-paymarks-heading">{html.escape(L.raw('footer.payment.heading'))}</h2>
      <ul class="mc-paymarks">
        {marks}
      </ul>
      <!-- footer.payment.note -->
      <p class="mc-legal">{html.escape(L.raw('footer.payment.note'))}</p>
      <!-- prices.noSurcharge -->
      <p class="mc-legal">{html.escape(L.raw('prices.noSurcharge'))}</p>
    </section>

    <div class="mc-footer__legal">
      <!-- footer.legal.entity -->
      <p>{html.escape(L.raw('footer.legal.entity'))}</p>
      <!-- common.entity.registeredName -->
      <p>{html.escape(L.raw('common.entity.registeredName'))}</p>
      <!-- legal.compliance.currency -->
      <p>{html.escape(L.raw('legal.compliance.currency'))}</p>
      <!-- footer.copyright -->
      <p>{html.escape(L.raw('footer.copyright'))}</p>
    </div>
  </div>
</footer>"""


# ---------------------------------------------------------------------------
def page(L, route, title_key, desc_key, body, title_compose=None):
    f, lang = L.folder, L.lang
    depth = route.count("/")
    alts = "\n  ".join(
        f'<link rel="alternate" hreflang="{code}" href="{url(o, route)}">'
        for o, code in LOCALES.items())
    if title_key:
        title = html.escape(L.raw(title_key))
        tcomment = f"<!-- {title_key} -->"
    else:
        a, b = title_compose
        title = f"{html.escape(L.raw(a))} — {html.escape(L.raw(b))}"
        tcomment = f"<!-- {a} + {b} -->"
    if desc_key:
        desc = f'\n  <!-- {desc_key} -->\n  <meta name="description" content="{html.escape(L.raw(desc_key), quote=True)}">'
    else:
        desc = ""
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  {tcomment}
  <title>{title}</title>{desc}
  <link rel="canonical" href="{url(f, route)}">
  {alts}
  <link rel="alternate" hreflang="x-default" href="{url('en', route)}">
  <link rel="stylesheet" href="/assets/tokens.css">
  <link rel="stylesheet" href="/assets/base.css">
  <link rel="stylesheet" href="/assets/components.css">
</head>
<body>
<!-- header.skip -->
<a class="mc-skip-link" href="#main">{html.escape(L.raw('header.skip'))}</a>

{header(L, route)}

<main id="main" tabindex="-1">
{body}
</main>

{footer(L)}
</body>
</html>
"""


def legal_tail(L, extra_gov=True):
    """The strip every legal document ends with."""
    gov = (f'\n    <!-- legal.governingLanguage -->\n'
           f'    <p class="mc-legal" data-blocked="governing-language">'
           f'{html.escape(L.raw("legal.governingLanguage"))}</p>' if extra_gov else "")
    return f"""  <section class="mc-section">
    <div class="mc-page mc-page--narrow">
    <!-- legal.updatedLabel / legal.updatedValue -->
    <p class="mc-legal" data-blocked="publication-date">{html.escape(L.raw('legal.updatedLabel'))}: {html.escape(L.raw('legal.updatedValue'))}</p>
    <!-- legal.entityLine -->
    <p class="mc-legal">{html.escape(L.raw('legal.entityLine'))}</p>{gov}
    </div>
  </section>"""


def blocked(text, tag="blocked"):
    return (f'<p class="mc-legal" data-blocked="{tag}">{html.escape(text)}</p>')


def section(inner, narrow=True, dark=False):
    cls = "mc-section" + (" band--dark" if dark else "")
    pg = "mc-page mc-page--narrow" if narrow else "mc-page"
    return f'  <section class="{cls}">\n    <div class="{pg}">\n{inner}\n    </div>\n  </section>'


def h2sec(L, key, parts):
    body = "\n".join(parts)
    return section(f"      {L.el('h2', key)}\n{body}")


def P(L, key, cls=None, blocked_tag=None):
    c = f' class="{cls}"' if cls else ""
    b = f' data-blocked="{blocked_tag}"' if blocked_tag else ""
    return f"      <!-- {key} -->\n      <p{c}{b}>{html.escape(L.raw(key))}</p>"


def UL(L, keys, cls=None):
    c = f' class="{cls}"' if cls else ""
    items = "\n".join(f"        {L.li(k)}" for k in keys)
    return f"      <ul{c}>\n{items}\n      </ul>"


def OL(L, keys, blocked_keys=()):
    items = []
    for k in keys:
        b = ' data-blocked="sequence"' if k in blocked_keys else ""
        items.append(f'        <!-- {k} --><li{b}>{html.escape(L.raw(k))}</li>')
    return "      <ol>\n" + "\n".join(items) + "\n      </ol>"


# ===========================================================================
# THE PAGES
# ===========================================================================
def build_about(L):
    ent = [("common.entity.legalName", None),
           ("common.entity.regNumber", "common.entity.regNumberLabel"),
           ("common.entity.taxNumber", "common.entity.taxNumberLabel"),
           ("common.entity.address", "common.entity.addressLabel")]
    rows = []
    for val, lab in ent:
        if lab:
            rows.append(f'        <!-- {lab} --><dt>{html.escape(L.raw(lab))}</dt>\n'
                        f'        <!-- {val} --><dd>{html.escape(L.raw(val))}</dd>')
        else:
            rows.append(f'        <!-- common.entity.legalName --><dt>{html.escape(L.raw("about.entity.h2"))}</dt>\n'
                        f'        <dd>{html.escape(L.raw(val))}</dd>')
    people = []
    for who in ("davit", "hayk"):
        people.append(f"""      <div class="mc-verify__item">
        <!-- common.founder.{who}.name --><h3 class="mc-verify__title">{html.escape(L.raw(f'common.founder.{who}.name'))}</h3>
        <!-- common.founder.{who}.role --><p class="mc-text-secondary">{html.escape(L.raw(f'common.founder.{who}.role'))}</p>
        <!-- about.{who}.line --><p>{html.escape(L.raw(f'about.{who}.line'))}</p>
        <!-- common.founder.{who}.phone / .tel --><p><a href="{html.escape(L.raw(f'common.founder.{who}.tel'))}">{html.escape(L.raw(f'common.founder.{who}.phone'))}</a></p>
        <!-- common.founder.{who}.whatsapp --><p class="mc-legal"><a href="{html.escape(L.raw(f'common.founder.{who}.whatsapp'))}">{html.escape(L.raw(f'common.founder.{who}.phone'))}</a></p>
      </div>""")

    body = "\n".join([
        section("\n".join([
            L.el("h1", "about.h1"),
            P(L, "about.p1", cls="mc-body-lg"),
            P(L, "about.why"),
            P(L, "about.p2"),
            UL(L, ["about.method1", "about.method2", "about.method3"]),
        ])),
        section("\n".join([
            L.el("h2", "about.entity.h2"),
            P(L, "about.entity.tradingAs"),
            "      <dl>\n" + "\n".join(rows) + "\n      </dl>",
            P(L, "common.entity.registeredName"),
            P(L, "common.entity.country"),
            P(L, "about.entity.bank"),
        ])),
        section("\n".join([
            L.el("h2", "about.people.h2"),
            '      <div class="mc-verify">',
            "\n".join(people),
            "      </div>",
            P(L, "common.hours"),
            P(L, "common.channels", cls="mc-legal"),
        ])),
        section("\n".join([
            L.el("h2", "home.trust.h2"),
            P(L, "home.honesty", cls="mc-body-lg"),
        ])),
    ])
    return page(L, "about.html", "meta.about.title", "meta.about.description", body)


def build_history(L):
    body = "\n".join([
        section("\n".join([
            L.el("h1", "common.entity.registeredYear"),
            f"      {blocked(BLOCKED_ROUTE, 'route-copy')}",
            P(L, "about.p1", cls="mc-body-lg"),
            P(L, "about.entity.tradingAs"),
            P(L, "common.entity.registeredName"),
            P(L, "about.why"),
        ])),
        section("\n".join([
            L.el("h2", "home.trust.h2"),
            P(L, "home.honesty", cls="mc-body-lg"),
            P(L, "about.p2"),
        ])),
    ])
    return page(L, "history.html", None, "meta.about.description", body,
                title_compose=("common.entity.registeredYear", "common.brand"))


def build_mission(L):
    trust = []
    for n in "1234":
        trust.append(f"""      <div class="mc-verify__item">
        <!-- home.trust.{n}.label --><h3 class="mc-verify__title">{html.escape(L.raw(f'home.trust.{n}.label'))}</h3>
        <!-- home.trust.{n}.line --><p class="mc-verify__text">{html.escape(L.raw(f'home.trust.{n}.line'))}</p>
      </div>""")
    body = "\n".join([
        section("\n".join([
            L.el("h1", "home.protocol.h2"),
            f"      {blocked(BLOCKED_ROUTE, 'route-copy')}",
            P(L, "about.method3", cls="mc-body-lg"),
            UL(L, ["home.protocol.photos", "home.protocol.videos",
                   "home.protocol.gps", "home.protocol.note"]),
            P(L, "home.protocol.closing"),
            P(L, "home.trust.1.line"),
        ])),
        section("\n".join([
            L.el("h2", "home.trust.h2"),
            '      <div class="mc-verify">',
            "\n".join(trust),
            "      </div>",
        ])),
        section("\n".join([
            L.el("h2", "legal.terms.after.h2"),
            P(L, "legal.terms.after.p1"),
            P(L, "legal.terms.after.p2"),
            f'      <!-- footer.legal.terms --><p><a href="{url(L.folder, "legal/terms.html")}">{html.escape(L.raw("footer.legal.terms"))}</a></p>',
        ])),
    ])
    return page(L, "mission.html", None, "meta.report.description", body,
                title_compose=("home.protocol.h2", "common.brand"))


def build_values(L):
    body = "\n".join([
        section("\n".join([
            L.el("h1", "how.includes.h2"),
            f"      {blocked(BLOCKED_ROUTE, 'route-copy')}",
            P(L, "about.method1", cls="mc-body-lg"),
            UL(L, [f"how.includes.{n}" for n in range(1, 9)]),
            P(L, "how.firstVisit"),
            P(L, "how.crew"),
        ])),
        section("\n".join([
            L.el("h2", "how.notdo.h2"),
            UL(L, [f"how.notdo.{n}" for n in range(1, 5)]),
            P(L, "how.overclean"),
            P(L, "legal.limitations.stone"),
            f'      <!-- how.notdo.link --><p><a href="{url(L.folder, "legal/restrictions.html")}">{html.escape(L.raw("how.notdo.link"))}</a></p>',
        ])),
        section("\n".join([
            L.el("h2", "legal.terms.winter.h2"),
            P(L, "how.weather"),
        ])),
    ])
    return page(L, "values.html", None, "meta.how.description", body,
                title_compose=("how.includes.h2", "common.brand"))


def build_restrictions(L):
    body = "\n".join([
        section("\n".join([
            L.el("h1", "legal.limitations.h1"),
            P(L, "legal.limitations.standfirst", cls="mc-body-lg"),
        ])),
        h2sec(L, "legal.limitations.notus.h2",
              [P(L, "legal.limitations.notus.p1"), P(L, "legal.limitations.notus.p2")]),
        h2sec(L, "legal.limitations.construction.h2",
              [P(L, "legal.limitations.construction.p1"),
               P(L, "legal.limitations.construction.p2"),
               P(L, "legal.limitations.construction.p3"),
               P(L, "legal.limitations.construction.blocked", cls="mc-legal",
                 blocked_tag="minor-repair-boundary")]),
        h2sec(L, "legal.limitations.ask.h2",
              [UL(L, [f"legal.limitations.ask.{n}" for n in range(1, 7)]),
               P(L, "legal.limitations.stone")]),
        h2sec(L, "legal.limitations.access.h2",
              [P(L, "legal.limitations.access.p1"),
               P(L, "legal.limitations.access.p2"),
               P(L, "legal.limitations.access.blocked", cls="mc-legal",
                 blocked_tag="cemetery-access-opinion")]),
        h2sec(L, "legal.limitations.photo.h2",
              [P(L, "legal.limitations.photo.p1"),
               P(L, "legal.limitations.photo.blocked", cls="mc-legal",
                 blocked_tag="photo-consent-form")]),
        h2sec(L, "legal.limitations.liability.h2",
              [P(L, "legal.limitations.liability.blocked", cls="mc-legal",
                 blocked_tag="liability-figure"),
               P(L, "legal.compliance.ageNote", cls="mc-legal",
                 blocked_tag="age-restriction-and-licence")]),
        legal_tail(L),
    ])
    return page(L, "legal/restrictions.html", "meta.limitations.title",
                "meta.limitations.description", body)


def build_privacy(L):
    body = "\n".join([
        section("\n".join([
            L.el("h1", "legal.privacy.h1"),
            P(L, "legal.privacy.summary", cls="mc-body-lg"),
        ])),
        h2sec(L, "legal.privacy.who.h2", [P(L, "legal.privacy.who.p1")]),
        h2sec(L, "legal.privacy.collect.h2",
              [P(L, "legal.privacy.collect.consultation"),
               P(L, "legal.privacy.collect.client"),
               P(L, "legal.privacy.collect.cards")]),
        h2sec(L, "legal.privacy.who2.h2",
              [UL(L, ["legal.privacy.who2.staff", "legal.privacy.who2.dev",
                      "legal.privacy.who2.crm", "legal.privacy.who2.bank",
                      "legal.privacy.who2.family"]),
               P(L, "legal.privacy.who2.blocked", cls="mc-legal",
                 blocked_tag="hosting-country-and-transfer-basis")]),
        h2sec(L, "legal.privacy.retention.h2",
              [P(L, "legal.privacy.retention.reports"),
               P(L, "legal.privacy.retention.blocked", cls="mc-legal",
                 blocked_tag="retention-periods")]),
        h2sec(L, "legal.privacy.name.h2",
              [P(L, "legal.privacy.name.p1"), P(L, "legal.privacy.name.p2")]),
        h2sec(L, "legal.privacy.notdo.h2", [P(L, "legal.privacy.notdo.p1")]),
        h2sec(L, "legal.privacy.rights.h2",
              [P(L, "legal.privacy.rights.intro"),
               OL(L, [f"legal.privacy.rights.{n}" for n in range(1, 7)]),
               P(L, "legal.privacy.rights.accounting"),
               P(L, "legal.privacy.rights.window", cls="mc-legal",
                 blocked_tag="data-request-window")]),
        h2sec(L, "legal.cookies.h1",
              [P(L, "legal.cookies.p1"),
               f'      <!-- footer.legal.cookies --><p><a href="{url(L.folder, "legal/cookies.html")}">{html.escape(L.raw("footer.legal.cookies"))}</a></p>']),
        h2sec(L, "legal.privacy.changes.h2", [P(L, "legal.privacy.changes.p1")]),
        legal_tail(L),
    ])
    return page(L, "legal/privacy.html", "meta.privacy.title",
                "meta.privacy.description", body)


def build_cookies(L):
    body = "\n".join([
        section("\n".join([
            L.el("h1", "legal.cookies.h1"),
            P(L, "legal.cookies.p1", cls="mc-body-lg"),
            P(L, "legal.cookies.p2"),
            P(L, "legal.cookies.p3"),
            P(L, "legal.cookies.p4"),
            P(L, "legal.cookies.p5"),
            P(L, "legal.cookies.p6"),
            f'      <!-- footer.legal.privacy --><p><a href="{url(L.folder, "legal/privacy.html")}">{html.escape(L.raw("footer.legal.privacy"))}</a></p>',
        ])),
        legal_tail(L),
    ])
    return page(L, "legal/cookies.html", "meta.cookies.title",
                "meta.cookies.description", body)


def build_refunds(L):
    ex = []
    for n in (1, 2, 3):
        ex.append(f"""      <div class="mc-verify__item">
        <!-- legal.refund.example{n}.title --><h3 class="mc-verify__title">{html.escape(L.raw(f'legal.refund.example{n}.title'))}</h3>
        <!-- legal.refund.example{n}.paid --><p class="mc-verify__text">{html.escape(L.raw(f'legal.refund.example{n}.paid'))}</p>
        <!-- legal.refund.example{n}.calc --><p class="mc-num">{html.escape(L.raw(f'legal.refund.example{n}.calc'))}</p>
      </div>""")
    body = "\n".join([
        section("\n".join([
            L.el("h1", "legal.refund.h1"),
            P(L, "legal.refund.standfirst", cls="mc-body-lg"),
        ])),
        h2sec(L, "legal.refund.rule.h2",
              [P(L, "legal.refund.rule.p1"),
               P(L, "legal.refund.rule.formula", cls="mc-num"),
               P(L, "legal.refund.rule.rounding")]),
        section("\n".join([
            L.el("h2", "legal.refund.visits.h2"),
            P(L, "legal.refund.visits.p1"),
            L.el("h3", "legal.refund.base.h2"),
            P(L, "legal.refund.base.p1"),
            '      <div class="mc-verify">',
            "\n".join(ex),
            "      </div>",
            P(L, "common.currencyLine", cls="mc-legal"),
        ])),
        h2sec(L, "legal.refund.cancel.h2",
              [P(L, "legal.refund.cancel.p1"), P(L, "legal.refund.cancel.p2")]),
        h2sec(L, "legal.refund.unhappy.h2", [P(L, "legal.refund.unhappy.p1")]),
        h2sec(L, "legal.refund.oneoff.h2",
              [P(L, "legal.refund.oneoff.blocked", cls="mc-legal",
                 blocked_tag="one-off-cancellation-rule")]),
        h2sec(L, "legal.refund.how.h2",
              [P(L, "legal.refund.how.p1"),
               P(L, "legal.refund.how.blocked", cls="mc-legal",
                 blocked_tag="refund-turnaround-days")]),
        legal_tail(L),
    ])
    return page(L, "legal/refunds.html", "meta.refund.title",
                "meta.refund.description", body)


def build_terms(L):
    body = "\n".join([
        section("\n".join([
            L.el("h1", "legal.terms.h1"),
            P(L, "legal.terms.what.p1", cls="mc-body-lg"),
            P(L, "prices.sameness"),
            UL(L, FOOTER_SVC),
            P(L, "prices.coverage"),
            P(L, "prices.special.definition"),
            P(L, "prices.special.entryRule"),
            P(L, "common.currencyLine", cls="mc-legal"),
            f'      <!-- home.prices.link --><p><a href="{url(L.folder, "prices.html")}">{html.escape(L.raw("home.prices.link"))}</a></p>',
        ])),
        h2sec(L, "legal.terms.where.h2",
              [P(L, "legal.terms.where.p1"), P(L, "legal.terms.where.p2"),
               P(L, "prices.onePriceList")]),
        h2sec(L, "legal.terms.sequence.h2",
              [OL(L, [f"legal.terms.sequence.{n}" for n in range(1, 8)],
                  blocked_keys={"legal.terms.sequence.6"})]),
        h2sec(L, "legal.terms.after.h2",
              [P(L, "legal.terms.after.p1"), P(L, "legal.terms.after.p2")]),
        h2sec(L, "legal.terms.year.h2", [P(L, "legal.terms.year.p1"),
                                         P(L, "prices.paymentTerm")]),
        h2sec(L, "legal.terms.winter.h2", [P(L, "legal.terms.winter.p1")]),
        h2sec(L, "legal.terms.crew.h2", [P(L, "legal.terms.crew.p1")]),
        h2sec(L, "legal.terms.credit.h2",
              [P(L, "legal.terms.credit.p1"),
               UL(L, [f"prices.credit.rule{n}" for n in range(1, 6)]),
               P(L, "legal.terms.credit.p2"),
               P(L, "legal.compliance.noTrial")]),
        h2sec(L, "legal.terms.payment.h2",
              [P(L, "legal.terms.payment.p1"),
               P(L, "prices.noSurcharge"),
               P(L, "legal.terms.payment.p2"),
               P(L, "legal.compliance.currency"),
               P(L, "common.fx.long", cls="mc-legal"),
               P(L, "prices.paymentReality"),
               f'      <!-- footer.legal.security --><p><a href="{url(L.folder, "legal/security.html")}">{html.escape(L.raw("footer.legal.security"))}</a></p>']),
        h2sec(L, "legal.terms.guarantees.h2",
              [P(L, "legal.terms.guarantees.p1"), P(L, "legal.terms.guarantees.p2"),
               f'      <!-- footer.legal.refund --><p><a href="{url(L.folder, "legal/refunds.html")}">{html.escape(L.raw("footer.legal.refund"))}</a></p>']),
        h2sec(L, "legal.terms.complaints.h2",
              [P(L, "legal.terms.complaints.p1"), P(L, "common.hours")]),
        h2sec(L, "legal.limitations.h1",
              [P(L, "legal.limitations.standfirst"),
               f'      <!-- footer.legal.limitations --><p><a href="{url(L.folder, "legal/restrictions.html")}">{html.escape(L.raw("footer.legal.limitations"))}</a></p>']),
        legal_tail(L),
    ])
    return page(L, "legal/terms.html", "meta.terms.title",
                "meta.terms.description", body)


def build_security(L):
    body = "\n".join([
        section("\n".join([
            L.el("h1", "legal.security.h1"),
            P(L, "legal.security.p1", cls="mc-body-lg"),
            P(L, "legal.security.p2"),
            P(L, "legal.security.p3"),
            P(L, "legal.security.p4"),
            P(L, "legal.security.p5"),
        ])),
        h2sec(L, "legal.terms.payment.h2",
              [P(L, "legal.privacy.collect.cards"),
               P(L, "legal.terms.payment.p2"),
               P(L, "legal.compliance.currency"),
               P(L, "legal.compliance.noTrial"),
               f'      <!-- footer.legal.privacy --><p><a href="{url(L.folder, "legal/privacy.html")}">{html.escape(L.raw("footer.legal.privacy"))}</a></p>']),
        legal_tail(L),
    ])
    return page(L, "legal/security.html", "meta.security.title",
                "meta.security.description", body)


BUILDERS = {
    "about.html": build_about,
    "history.html": build_history,
    "mission.html": build_mission,
    "values.html": build_values,
    "legal/restrictions.html": build_restrictions,
    "legal/privacy.html": build_privacy,
    "legal/cookies.html": build_cookies,
    "legal/refunds.html": build_refunds,
    "legal/terms.html": build_terms,
    "legal/security.html": build_security,
}


def main():
    written = []
    for folder in LOCALES:
        L = Loc(folder)
        for route in ROUTES:
            out = SITE / folder / route
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(BUILDERS[route](L), encoding="utf-8")
            written.append(out)
        inc = INC / f"footer.{folder}.html"
        inc.write_text(
            "<!-- MemoryCare shared footer — Ameriabank §4.10.2 and §4.10.11.\n"
            "     Generated by _includes/build-compliance-pages.py. Do not hand-edit:\n"
            "     edit the generator or strings/" + folder + ".json and re-run.\n"
            "     Paste verbatim at the end of <body> on every page in /" + folder + "/. -->\n"
            + footer(L) + "\n", encoding="utf-8")
        written.append(inc)
    print(f"wrote {len(written)} files")
    for w in written:
        print("  ", w.relative_to(ROOT.parent))


if __name__ == "__main__":
    main()
