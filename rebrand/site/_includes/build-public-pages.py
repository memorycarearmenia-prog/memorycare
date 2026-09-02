#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MemoryCare rebrand — public-site generator.

Emits the six public routes in three locales plus the bare root redirect.
Every visible string is looked up in rebrand/strings/<loc>.json by key and
emitted with an HTML comment naming that key, so the key is traceable in the
shipped file. No colour, size or font value is written into the HTML: every
class is from assets/tokens.css + base.css + components.css.

Nothing outside the route list is written.
"""

import json, os, re, html

ROOT = "/home/user/memorycare/rebrand"
SITE = os.path.join(ROOT, "site")
STRINGS = os.path.join(ROOT, "strings")

LOCALES = [("en", "en", "en_US"), ("ru", "ru", "ru_RU"), ("am", "hy", "hy_AM")]
# (url segment, lang/hreflang, og:locale).  "am" is the URL segment the lead
# specified; "hy" is the language.  "am" is Amharic and must never be a lang.

S = {}


def load():
    for seg, _lang, _og in LOCALES:
        f = {"en": "en.json", "ru": "ru.json", "am": "am.json"}[seg]
        with open(os.path.join(STRINGS, f), encoding="utf-8") as fh:
            S[seg] = flat(json.load(fh))


def flat(o, p=""):
    r = {}
    for k, v in o.items():
        n = p + "." + k if p else k
        if isinstance(v, dict):
            r.update(flat(v, n))
        else:
            r[n] = v
    return r


MISSING = set()


def raw(loc, key):
    try:
        return S[loc][key]
    except KeyError:
        MISSING.add(key)
        return "[MISSING STRING: %s]" % key


def e(loc, key):
    """Escaped value only — for attributes."""
    return html.escape(raw(loc, key), quote=True)


def t(loc, key):
    """Value with its key as a trailing HTML comment — for text nodes."""
    return "%s<!--%s-->" % (html.escape(raw(loc, key)), key)


def num_split(loc, key):
    """'8 photographs — ...' -> ('8', 'photographs — ...'). Same shape in all
    three locales: every protocol line opens with the numeral."""
    v = raw(loc, key)
    m = re.match(r"^(\d+)\s+(.*)$", v, re.S)
    if not m:
        return "", html.escape(v)
    return html.escape(m.group(1)), html.escape(m.group(2))


# --------------------------------------------------------------------------
# route map
# --------------------------------------------------------------------------
R = {
    "home": "",
    "how": "how-it-works.html",
    "prices": "prices.html",
    "report": "sample-report.html",
    "contact": "contact.html",
    "404": "404.html",
    # Owned by the other specialists. These paths are read off
    # _includes/build-compliance-pages.py (ROUTES / FOOTER_LEGAL), so every
    # link below resolves to a file that team actually writes.
    "about": "about.html",
    "family": "family.html",
    "privacy": "legal/privacy.html",
    "cookies": "legal/cookies.html",
    "terms": "legal/terms.html",
    "refund": "legal/refunds.html",
    "security": "legal/security.html",
    "limitations": "legal/restrictions.html",
    "signin": "account/",
}

# The file each route is WRITTEN to (u() gives the URL; "/en/" is index.html).
FILE = {"home": "index.html", "how": "how-it-works.html", "prices": "prices.html",
        "report": "sample-report.html", "contact": "contact.html", "404": "404.html"}


def u(loc, route):
    return "/%s/%s" % (loc, R[route])


MEDALLION = None


def medallion():
    global MEDALLION
    if MEDALLION is None:
        with open(os.path.join(SITE, "assets/brand/medallion.svg"), encoding="utf-8") as fh:
            s = fh.read()
        # the asset carries an English aria-label; inline it as decoration only
        s = s.replace(' role="img" aria-label="Verified"',
                      ' class="mc-report__gps-mark" aria-hidden="true" focusable="false"')
        MEDALLION = s
    return MEDALLION


# --------------------------------------------------------------------------
# shell
# --------------------------------------------------------------------------

def head(loc, lang, og, route, metakey):
    alts = []
    for seg, l2, _ in LOCALES:
        alts.append('  <link rel="alternate" hreflang="%s" href="%s">' % (l2, u(seg, route)))
    alts.append('  <link rel="alternate" hreflang="x-default" href="%s">' % u("en", route))
    return """<!doctype html>
<html lang="%(lang)s">
<head>
  <meta charset="utf-8">
  <!-- Zoom is not blocked here. The live build ships a viewport that
       forbids it on all 36 pages; that is WCAG 1.4.4 and it goes. -->
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>%(title)s</title><!--meta.%(mk)s.title-->
  <meta name="description" content="%(desc)s"><!--meta.%(mk)s.description-->
  <link rel="canonical" href="%(canon)s">
%(alts)s
  <meta property="og:type" content="website">
  <meta property="og:locale" content="%(og)s">
  <meta property="og:url" content="%(canon)s">
  <meta property="og:title" content="%(ogt)s"><!--meta.og.title-->
  <meta property="og:description" content="%(ogd)s"><!--meta.og.description-->
  <meta name="robots" content="index, follow">
  <!-- Load order is not a preference: tokens.css declares the layer order. -->
  <link rel="stylesheet" href="/assets/tokens.css">
  <link rel="stylesheet" href="/assets/base.css">
  <link rel="stylesheet" href="/assets/components.css">
</head>
<body>
""" % {
        "lang": lang,
        "title": e(loc, "meta.%s.title" % metakey),
        "desc": e(loc, "meta.%s.description" % metakey),
        "mk": metakey,
        "canon": u(loc, route),
        "alts": "\n".join(alts),
        "og": og,
        "ogt": e(loc, "meta.og.title"),
        "ogd": e(loc, "meta.og.description"),
    }


def header(loc, current, langroute=None, ctahref=None):
    navitems = [
        ("how", "nav.how"),
        ("prices", "nav.prices"),
        ("report", "nav.report"),
        ("family", "nav.family"),
        ("about", "nav.about"),
        ("contact", "nav.contacts"),
    ]
    lis = []
    for route, key in navitems:
        cur = ' aria-current="page"' if route == current else ""
        lis.append(
            '          <li class="mc-nav__item"><a class="mc-nav__link" href="%s"%s>%s</a></li>'
            % (u(loc, route), cur, t(loc, key))
        )

    langs = []
    for seg, l2, _ in LOCALES:
        key = "header.lang.%s" % l2
        cur = ' aria-current="true"' if seg == loc else ""
        langs.append(
            '          <li class="mc-lang__item"><a class="mc-lang__link" hreflang="%s" lang="%s" href="%s"%s>%s</a></li>'
            % (l2, l2, u(seg, langroute or current), cur, t(loc, key))
        )

    return """  <a class="mc-skip-link" href="#main">%(skip)s</a>

  <header class="mc-header">
    <div class="mc-page mc-header__inner">
      <a class="mc-header__brand" href="%(homeurl)s">
        <img class="mc-header__mark" src="/assets/brand/MemoryCare_logo-mark_color.svg" alt="">
        <span class="mc-h4">%(brand)s</span>
        <span class="mc-sr-only">%(descriptor)s</span>
      </a>

      <!-- Flat nav. The live build's submenus open on :hover only, with no
           keyboard path; there is no submenu here to need one, and every
           destination is a page that exists. -->
      <nav class="mc-nav" aria-label="%(navlabel)s"><!--common.descriptor-->
        <ul class="mc-nav__list" role="list">
%(nav)s
        </ul>
      </nav>

      <div class="mc-header__actions">
        <nav class="mc-lang" aria-label="%(langlabel)s"><!--header.lang.label-->
          <ul class="mc-lang__list" role="list">
%(langs)s
          </ul>
        </nav>
        <a class="mc-btn mc-btn--quiet" href="%(signin)s">%(signintxt)s</a>
        <a class="mc-btn mc-btn--primary" href="%(cta)s">%(ctatxt)s</a>
      </div>
    </div>
  </header>

  <main id="main" tabindex="-1">
""" % {
        "skip": t(loc, "header.skip"),
        "homeurl": u(loc, "home"),
        "brand": t(loc, "common.brand"),
        "descriptor": t(loc, "common.descriptor"),
        "navlabel": e(loc, "common.descriptor"),
        "nav": "\n".join(lis),
        "langlabel": e(loc, "header.lang.label"),
        "langs": "\n".join(langs),
        "signin": u(loc, "signin"),
        "signintxt": t(loc, "header.signin"),
        "cta": ctahref or "#consultation",
        "ctatxt": t(loc, "header.cta"),
    }


SHARED_FOOTER = {}


def footer(loc):
    """The shared footer from _includes/footer.<loc>.html, written by the
    compliance-pages engineer and meant to be pasted verbatim on every page.
    ONE correction is applied: that file links /<loc>/contacts.html, and the
    route this team gave me is contact.html. Ameriabank §4.11 requires every
    link to be real, so the href is rewritten rather than shipped broken.
    → lead: one of the two filenames has to move."""
    if loc not in SHARED_FOOTER:
        with open(os.path.join(SITE, "_includes", "footer.%s.html" % loc), encoding="utf-8") as fh:
            f = fh.read()
        f = f.replace('href="/%s/contacts.html"' % loc,
                      'href="/%s/contact.html"' % loc)
        SHARED_FOOTER[loc] = f
    return "  </main>\n\n" + SHARED_FOOTER[loc] + "\n</body>\n</html>\n"


def _footer_unused(loc):
    company = [("about", "nav.about"), ("family", "nav.family"), ("how", "nav.how"), ("contact", "nav.contacts")]
    services = [
        ("prices", "footer.svc.inspection"),
        ("prices", "footer.svc.single"),
        ("prices", "footer.svc.four"),
        ("prices", "footer.svc.six"),
        ("prices", "footer.svc.special"),
    ]
    legal = [
        ("privacy", "footer.legal.privacy"),
        ("cookies", "footer.legal.cookies"),
        ("terms", "footer.legal.terms"),
        ("refund", "footer.legal.refund"),
        ("security", "footer.legal.security"),
        ("limitations", "footer.legal.limitations"),
    ]

    def col(headingkey, items):
        lis = "\n".join(
            '            <li><a href="%s">%s</a></li>' % (u(loc, r), t(loc, k)) for r, k in items
        )
        return """        <div>
          <h2 class="mc-footer__heading">%s</h2>
          <ul class="mc-footer__list" role="list">
%s
          </ul>
        </div>""" % (t(loc, headingkey), lis)

    def person(who):
        return """            <li class="mc-footer__contact">
              <a href="%(tel)s">%(phone)s</a>
              <span class="mc-caption mc-text-secondary">%(name)s · %(role)s</span>
              <a href="%(wa)s" rel="noopener">%(walabel)s</a>
            </li>""" % {
            "tel": e(loc, "common.founder.%s.tel" % who),
            "phone": t(loc, "common.founder.%s.phone" % who),
            "name": t(loc, "common.founder.%s.name" % who),
            "role": t(loc, "common.founder.%s.roleShort" % who),
            "wa": e(loc, "common.founder.%s.whatsapp" % who),
            "walabel": t(loc, "form.whatsapp"),
        }

    return """  </main>

  <footer class="mc-footer">
    <div class="mc-page">
      <div class="mc-footer__grid">
%(company)s
%(services)s
        <div>
          <h2 class="mc-footer__heading">%(contactheading)s</h2>
          <ul class="mc-footer__list" role="list">
%(davit)s
%(hayk)s
            <li><a href="mailto:%(email)s">%(emailtxt)s</a></li>
            <li class="mc-caption mc-text-secondary">%(hours)s</li>
            <li class="mc-caption mc-text-secondary">%(channels)s</li>
          </ul>
        </div>
%(legal)s
      </div>

      <!-- Ameriabank §4.10 requires the payment systems' own colour marks.
           The scheme logo files do not exist in assets/brand/ yet, so the
           strip carries the heading and the honest note and no mark: a
           fabricated mark would be worse than a missing one. -->
      <div class="mc-paymarks">
        <h2 class="mc-footer__heading">%(payheading)s</h2>
        <p class="mc-paymarks__note">%(paynote)s</p>
      </div>

      <div class="mc-footer__legal">
        <p>%(entity)s</p>
        <p>%(registered)s</p>
        <p>%(currency)s</p>
        <p>%(copyright)s</p>
      </div>
    </div>
  </footer>
</body>
</html>
""" % {
        "company": col("footer.col.company", company),
        "services": col("footer.col.services", services),
        "legal": col("footer.col.legal", legal),
        "contactheading": t(loc, "footer.contactHeading"),
        "davit": person("davit"),
        "hayk": person("hayk"),
        "email": e(loc, "common.email"),
        "emailtxt": t(loc, "common.email"),
        "hours": t(loc, "common.hours"),
        "channels": t(loc, "common.channels"),
        "payheading": t(loc, "footer.payment.heading"),
        "paynote": t(loc, "footer.payment.note"),
        "entity": t(loc, "footer.legal.entity"),
        "registered": t(loc, "common.entity.registeredName"),
        "currency": t(loc, "common.currencyLine"),
        "copyright": t(loc, "footer.copyright"),
    }


# --------------------------------------------------------------------------
# shared blocks
# --------------------------------------------------------------------------

def consultation_form(loc, headingkey, supportkey, heading_level="h2"):
    """The consultation form. Never inside band--dark: it can show validation
    errors and error red measures 2.12 on Dark Olive (structural rule 3)."""
    sources = [
        ("search", "form.source.search"),
        ("social", "form.source.social"),
        ("video", "form.source.video"),
        ("word", "form.source.word"),
        ("cemetery", "form.source.cemetery"),
        ("other", "form.source.other"),
    ]
    opts = "\n".join(
        '            <option value="%s">%s</option>' % (v, t(loc, k)) for v, k in sources
    )
    return """      <div class="mc-page mc-page--narrow">
        <%(hl)s id="consultation-heading">%(heading)s</%(hl)s>
        <p class="mc-body-lg">%(support)s</p>

        <!-- method="post" to a handler the developer wires up. Nothing here
             needs script: validation is the browser's plus the server's, and
             the error summary panel is server-rendered at the top of the form
             with tabindex="-1" and autofocus.
             This form is never inside band--dark: error red measures 2.12 on
             Dark Olive (structural rule 3). -->
        <form method="post" action="#" aria-labelledby="consultation-heading">
          <input type="hidden" name="lang" value="%(loc)s">

          <div class="mc-field">
            <label class="mc-field__label" for="f-name">%(lname)s</label>
            <input class="mc-input" type="text" id="f-name" name="name" maxlength="60" autocomplete="name" required>
          </div>

          <div class="mc-field">
            <label class="mc-field__label" for="f-contact">%(lcontact)s</label>
            <input class="mc-input" type="text" id="f-contact" name="contact" inputmode="text" autocomplete="tel" aria-describedby="f-contact-help" required>
            <p class="mc-field__help" id="f-contact-help">%(hcontact)s</p>
          </div>

          <div class="mc-field">
            <label class="mc-field__label" for="f-place">%(lplace)s</label>
            <input class="mc-input" type="text" id="f-place" name="place" list="f-place-options" aria-describedby="f-place-help" required>
            <datalist id="f-place-options">
              <option value="%(placeunknown)s"></option><!--form.placeUnknown-->
            </datalist>
            <p class="mc-field__help" id="f-place-help">%(hplace)s</p>
          </div>

          <div class="mc-field">
            <label class="mc-field__label" for="f-relative">%(lrelative)s</label>
            <input class="mc-input" type="text" id="f-relative" name="relative" aria-describedby="f-relative-help">
            <p class="mc-field__help" id="f-relative-help">%(hrelative)s</p>
          </div>

          <div class="mc-field">
            <label class="mc-field__label" for="f-note">%(lnote)s</label>
            <textarea class="mc-textarea" id="f-note" name="note" maxlength="500" aria-describedby="f-note-help"></textarea>
            <p class="mc-field__help" id="f-note-help">%(hnote)s</p>
          </div>

          <div class="mc-field">
            <label class="mc-field__label" for="f-source">%(lsource)s</label>
            <select class="mc-select" id="f-source" name="source">
%(opts)s
            </select>
          </div>

          <div class="mc-field">
            <span class="mc-field__label" id="f-consent-label">%(lconsent)s</span>
            <div class="mc-check">
              <input class="mc-check__input" type="checkbox" id="f-consent" name="consent" value="yes" required>
              <label class="mc-check__label" for="f-consent">%(consent)s</label>
            </div>
            <p class="mc-field__help"><a href="%(privacyurl)s">%(privacy)s</a></p>
          </div>

          <button class="mc-btn mc-btn--primary" type="submit">%(submit)s</button>
          <p class="mc-field__help">%(callback)s %(hours)s</p>
        </form>
      </div>""" % {
        "hl": heading_level,
        "heading": t(loc, headingkey),
        "support": t(loc, supportkey),
        "loc": loc,
        "lname": t(loc, "form.label.name"),
        "lcontact": t(loc, "form.label.contact"),
        "hcontact": t(loc, "form.helper.contact"),
        "lplace": t(loc, "form.label.place"),
        "placeunknown": e(loc, "form.placeUnknown"),
        "hplace": t(loc, "form.helper.place"),
        "lrelative": t(loc, "form.label.relative"),
        "hrelative": t(loc, "form.helper.relative"),
        "lnote": t(loc, "form.label.note"),
        "hnote": t(loc, "form.notePrompt"),
        "lsource": t(loc, "form.source.question"),
        "opts": opts,
        "lconsent": t(loc, "form.label.consent"),
        "consent": t(loc, "form.consent"),
        "privacyurl": u(loc, "privacy"),
        "privacy": t(loc, "footer.legal.privacy"),
        "submit": t(loc, "form.submit"),
        "callback": t(loc, "frozen.callback"),
        "hours": t(loc, "frozen.hours"),
    }


def report_sheet(loc, with_body, eyebrow=True):
    """The report sheet. NO PHOTOGRAPHS EXIST, so no <img> and no empty frame
    pretending to be one: the sheet carries the metadata strip, the GPS row and
    the written blocks, and gains the eight photographs when the September
    shoot happens."""
    eb = '          <p class="mc-eyebrow">%s</p>\n' % t(loc, "home.report.overline") if eyebrow else ""
    head_html = """        <div class="mc-report__head">
%(overline)s          <p class="mc-report__meta">%(meta)s</p>
          <span class="mc-badge mc-badge--accent">%(chip)s</span>
        </div>""" % {
        "overline": eb,
        "meta": t(loc, "home.hero.sheetMeta"),
        "chip": t(loc, "home.hero.sheetChip"),
    }
    if not with_body:
        return '      <div class="mc-report">\n%s\n      </div>' % head_html

    body = """        <div class="mc-report__body">
          <div>
            <h3>%(before)s</h3>
            <p>%(angles)s</p>
          </div>
          <div>
            <h3>%(after)s</h3>
            <p>%(time)s</p>
          </div>
          <div>
            <h3>%(gpsh)s</h3>
            <div class="mc-report__gps">
              %(mark)s
              <span>%(gps)s</span>
            </div>
          </div>
          <div>
            <h3>%(noteh)s</h3>
            <p>%(note)s</p>
          </div>
          <div>
            <h3>%(nexth)s</h3>
            <p>%(nextp)s</p>
          </div>
          <div>
            <h3>%(confh)s</h3>
            <p>%(confp)s</p>
          </div>
        </div>""" % {
        "before": t(loc, "report.block.before"),
        "angles": t(loc, "home.report.ann.angles"),
        "after": t(loc, "report.block.after"),
        "time": t(loc, "home.report.ann.time"),
        "gpsh": t(loc, "report.block.gps"),
        "mark": medallion(),
        "gps": t(loc, "home.report.ann.gps"),
        "noteh": t(loc, "report.block.note"),
        "note": t(loc, "report.ann.4"),
        "nexth": t(loc, "report.block.next"),
        "nextp": t(loc, "home.protocol.note"),
        "confh": t(loc, "report.block.confirmation"),
        "confp": t(loc, "home.protocol.closing"),
    }
    return '      <div class="mc-report">\n%s\n%s\n      </div>' % (head_html, body)


def protocol_band(loc):
    """The repurposed statistics band (DECISIONS §2). The four invented
    numbers are gone; these are the published visit protocol, and each numeral
    is split off the front of its own string, so both halves are keyed."""
    items = []
    for key in ("home.protocol.photos", "home.protocol.videos", "home.protocol.gps"):
        v, lab = num_split(loc, key)
        items.append(
            """          <div class="mc-figures__item" data-source="protocol">
            <p class="mc-figures__value">%s</p>
            <p class="mc-figures__label">%s<!--%s--></p>
          </div>""" % (v, lab, key)
        )
    items.append(
        """          <div class="mc-figures__item" data-source="protocol">
            <p class="mc-figures__label">%s</p>
          </div>""" % t(loc, "home.protocol.note")
    )
    return """    <section class="mc-section">
      <div class="mc-page">
        <h2>%s</h2>
        <div class="mc-figures">
%s
        </div>
        <p class="mc-body-lg">%s</p>
      </div>
    </section>""" % (t(loc, "home.protocol.h2"), "\n".join(items), t(loc, "home.protocol.closing"))


def faq(loc, headingkey, qa):
    items = "\n".join(
        """          <details class="mc-accordion__item" name="faq">
            <summary class="mc-accordion__summary">%s</summary>
            <div class="mc-accordion__panel"><p>%s</p></div>
          </details>""" % (t(loc, q), t(loc, a))
        for q, a in qa
    )
    return """    <section class="mc-section">
      <div class="mc-page mc-page--narrow">
        <h2>%s</h2>
        <div class="mc-accordion">
%s
        </div>
      </div>
    </section>""" % (t(loc, headingkey), items)


# --------------------------------------------------------------------------
# pages
# --------------------------------------------------------------------------

def page_home(loc, lang, og):
    o = [head(loc, lang, og, "home", "home"), header(loc, "home")]

    # ---- 1. HERO. The fold ends on the report sheet cropped at its metadata
    #         strip: a date, a cemetery, a plot number, a GPS chip.
    strip = "\n".join(
        '            <li><span class="mc-badge">%s</span></li>' % t(loc, k)
        for k in ("home.hero.strip.media", "home.hero.strip.gps", "home.hero.strip.report")
    )
    o.append("""    <section class="mc-section">
      <div class="mc-page">
        <p class="mc-eyebrow">%(overline)s</p>
        <h1>%(h1)s</h1>
        <p class="mc-body-lg mc-measure">%(standfirst)s</p>
        <p>
          <a class="mc-btn mc-btn--primary" href="#consultation">%(cta)s</a>
          <a class="mc-btn mc-btn--secondary" href="%(reporturl)s">%(reportlink)s</a>
        </p>
        <p class="mc-caption mc-text-secondary">%(ctasupport)s</p>
        <ul class="mc-stack--tight" role="list">
%(strip)s
        </ul>
%(sheet)s
      </div>
    </section>""" % {
        "overline": t(loc, "home.hero.overline"),
        "h1": t(loc, "home.hero.h1"),
        "standfirst": t(loc, "home.hero.standfirst"),
        "cta": t(loc, "home.hero.cta"),
        "reporturl": u(loc, "report"),
        "reportlink": t(loc, "home.hero.reportLink"),
        "ctasupport": t(loc, "home.hero.ctaSupport"),
        "strip": strip,
        "sheet": report_sheet(loc, with_body=False, eyebrow=False),
    })

    # ---- 2. THE REPORT
    o.append("""    <section class="mc-section">
      <div class="mc-page">
        <h2>%(h2)s</h2>
        <p class="mc-body-lg mc-measure">%(standfirst)s</p>
%(sheet)s
        <p><a href="%(reporturl)s">%(link)s</a></p>
      </div>
    </section>""" % {
        "h2": t(loc, "home.report.h2"),
        "standfirst": t(loc, "home.report.standfirst"),
        "sheet": report_sheet(loc, with_body=True),
        "reporturl": u(loc, "report"),
        "link": t(loc, "home.report.link"),
    })

    # ---- 2b. the repurposed statistics band
    o.append(protocol_band(loc))

    # ---- 3. HOW IT WORKS
    steps = "\n".join(
        """          <li class="mc-verify__item">
            <h3 class="mc-verify__title">%s</h3>
            <p class="mc-verify__text">%s</p>
          </li>""" % (t(loc, "home.how.step%d.label" % n), t(loc, "home.how.step%d.line" % n))
        for n in (1, 2, 3)
    )
    o.append("""    <section class="mc-section">
      <div class="mc-page">
        <h2>%s</h2>
        <ol class="mc-verify" role="list">
%s
        </ol>
        <p><a href="%s">%s</a></p>
      </div>
    </section>""" % (t(loc, "nav.how"), steps, u(loc, "how"), t(loc, "home.how.link")))

    # ---- 4. WHAT A VISIT INCLUDES / WHAT WE DO NOT DO
    method = "\n".join(
        """          <div class="mc-verify__item">
            <h3 class="mc-verify__title">%s</h3>
            <p class="mc-verify__text">%s</p>
          </div>""" % (t(loc, "home.method.%s.label" % k), t(loc, "home.method.%s.line" % k))
        for k in ("crew", "equipment", "chemistry", "record")
    )
    notdo = "\n".join("          <li>%s</li>" % t(loc, "home.notdo.%d" % n) for n in (1, 2, 3))
    o.append("""    <section class="mc-section">
      <div class="mc-page">
        <h2>%(h2)s</h2>
        <div class="mc-verify">
%(method)s
        </div>
        <h3>%(notdoh)s</h3>
        <ul>
%(notdo)s
        </ul>
        <p><a href="%(limurl)s">%(notdolink)s</a></p>
      </div>
    </section>""" % {
        "h2": t(loc, "home.method.h2"),
        "method": method,
        "notdoh": t(loc, "home.notdo.h3"),
        "notdo": notdo,
        "limurl": u(loc, "limitations"),
        "notdolink": t(loc, "home.notdo.link"),
    })

    # ---- 5. PRICES
    lines = "\n".join(
        "          <li>%s</li>" % t(loc, "home.prices.line.%s" % k)
        for k in ("inspection", "single", "four", "six", "special")
    )
    o.append("""    <section class="mc-section">
      <div class="mc-page">
        <h2>%(h2)s</h2>
        <p class="mc-body-lg">%(sameness)s</p>
        <ul>
%(lines)s
        </ul>
        <p>%(onelist)s</p>
        <p><a href="%(pricesurl)s">%(link)s</a></p>
      </div>
    </section>""" % {
        "h2": t(loc, "home.prices.h2"),
        "sameness": t(loc, "home.prices.sameness"),
        "lines": lines,
        "onelist": t(loc, "home.prices.onePriceList"),
        "pricesurl": u(loc, "prices"),
        "link": t(loc, "home.prices.link"),
    })

    # ---- 6. FAMILY CIRCLE — the one dark band. No form inside it (rule 3).
    bullets = "\n".join("          <li>%s</li>" % t(loc, "home.family.b%d" % n) for n in (1, 2, 3))
    o.append("""    <section class="mc-section band--dark">
      <div class="mc-page">
        <p class="mc-eyebrow">%(eyebrow)s</p>
        <h2>%(h2)s</h2>
        <p class="mc-body-lg mc-measure">%(line)s</p>
        <p class="mc-measure">%(definition)s</p>
        <ul>
%(bullets)s
        </ul>
        <p><a href="%(familyurl)s">%(link)s</a></p>
      </div>
    </section>""" % {
        "eyebrow": t(loc, "home.family.eyebrow"),
        "h2": t(loc, "home.family.h2"),
        "line": t(loc, "home.family.line"),
        "definition": t(loc, "home.family.definition"),
        "bullets": bullets,
        "familyurl": u(loc, "family"),
        "link": t(loc, "home.family.link"),
    })

    # ---- 7. TRUST AND VERIFICATION
    trust = "\n".join(
        """          <div class="mc-verify__item">
            <h3 class="mc-verify__title">%s</h3>
            <p class="mc-verify__text">%s</p>
          </div>""" % (t(loc, "home.trust.%d.label" % n), t(loc, "home.trust.%d.line" % n))
        for n in (1, 2, 3, 4)
    )
    o.append("""    <section class="mc-section">
      <div class="mc-page">
        <h2>%s</h2>
        <div class="mc-verify">
%s
        </div>
      </div>
    </section>""" % (t(loc, "home.trust.h2"), trust))

    # ---- 8. THE HONESTY PANEL
    o.append("""    <section class="mc-section">
      <div class="mc-page mc-page--narrow">
        <p class="mc-body-lg">%s</p>
      </div>
    </section>""" % t(loc, "home.honesty"))

    # ---- 9. FOUNDERS
    def founder(who):
        return """          <div class="mc-family__row">
            <span class="mc-family__avatar" aria-hidden="true"></span>
            <div>
              <p class="mc-family__name">%(name)s</p>
              <p class="mc-family__role">%(role)s</p>
              <p class="mc-family__role">%(line)s</p>
            </div>
            <a class="mc-btn mc-btn--secondary" href="%(tel)s">%(phone)s</a>
            <a class="mc-btn mc-btn--quiet" href="%(wa)s" rel="noopener">%(walabel)s</a>
          </div>""" % {
            "name": t(loc, "common.founder.%s.name" % who),
            "role": t(loc, "common.founder.%s.role" % who),
            "line": t(loc, "home.founders.%s.line" % who),
            "tel": e(loc, "common.founder.%s.tel" % who),
            "phone": t(loc, "common.founder.%s.phone" % who),
            "wa": e(loc, "common.founder.%s.whatsapp" % who),
            "walabel": t(loc, "form.whatsapp"),
        }

    o.append("""    <section class="mc-section">
      <div class="mc-page">
        <h2>%s</h2>
        <div class="mc-family">
%s
%s
        </div>
      </div>
    </section>""" % (t(loc, "home.founders.h2"), founder("davit"), founder("hayk")))

    # ---- 10. FAQ
    o.append(faq(loc, "home.faq.h2", [("home.faq.q%d" % n, "home.faq.a%d" % n) for n in range(1, 7)]))

    # ---- 11. THE CONSULTATION FORM, on the page, not behind a button
    o.append("""    <section class="mc-section" id="consultation">
%s
    </section>""" % consultation_form(loc, "home.closing.h2", "home.closing.support"))

    o.append(footer(loc))
    return "\n".join(o)


def page_how(loc, lang, og):
    o = [head(loc, lang, og, "how", "how"), header(loc, "how")]
    steps = "\n".join(
        """          <li>
            <p class="mc-eyebrow">%s</p>
            <h2>%s</h2>
            <p>%s</p>
          </li>""" % (t(loc, "how.step%d.num" % n), t(loc, "how.step%d.heading" % n), t(loc, "how.step%d.body" % n))
        for n in (1, 2, 3, 4)
    )
    includes = "\n".join("          <li>%s</li>" % t(loc, "how.includes.%d" % n) for n in range(1, 9))
    notdo = "\n".join("          <li>%s</li>" % t(loc, "how.notdo.%d" % n) for n in range(1, 5))
    o.append("""    <section class="mc-section">
      <div class="mc-page">
        <h1>%(h1)s</h1>
        <p class="mc-body-lg mc-measure">%(standfirst)s</p>
      </div>
    </section>

    <section class="mc-section">
      <div class="mc-page">
        <ol class="mc-stack--loose" role="list">
%(steps)s
        </ol>
      </div>
    </section>

    <section class="mc-section">
      <div class="mc-page">
        <h2>%(inch)s</h2>
        <ul>
%(includes)s
        </ul>
        <p class="mc-measure">%(overclean)s</p>
        <p class="mc-measure">%(crew)s</p>
        <p class="mc-measure">%(first)s</p>
      </div>
    </section>

    <section class="mc-section">
      <div class="mc-page">
        <h2>%(notdoh)s</h2>
        <ul>
%(notdo)s
        </ul>
        <p><a href="%(limurl)s">%(notdolink)s</a></p>
      </div>
    </section>

    <section class="mc-section">
      <div class="mc-page mc-page--narrow">
        <h2>%(winterh)s</h2>
        <p>%(weather)s</p>
        <p>%(footnote)s</p>
      </div>
    </section>""" % {
        "h1": t(loc, "how.h1"),
        "standfirst": t(loc, "how.standfirst"),
        "steps": steps,
        "inch": t(loc, "how.includes.h2"),
        "includes": includes,
        "overclean": t(loc, "how.overclean"),
        "crew": t(loc, "how.crew"),
        "first": t(loc, "how.firstVisit"),
        "notdoh": t(loc, "how.notdo.h2"),
        "notdo": notdo,
        "limurl": u(loc, "limitations"),
        "notdolink": t(loc, "how.notdo.link"),
        "winterh": t(loc, "prices.year.winter"),
        "weather": t(loc, "how.weather"),
        "footnote": t(loc, "prices.year.footnote"),
    })
    o.append(protocol_band(loc))
    o.append("""    <section class="mc-section" id="consultation">
%s
    </section>""" % consultation_form(loc, "form.heading", "form.support"))
    o.append(footer(loc))
    return "\n".join(o)


def tariff_card(loc, prefix, recommended, oneoff, periodkey, ctaroute, ctakey, features, phrase=False):
    cls = "mc-tariff"
    if recommended:
        cls += " mc-tariff--recommended"
    if oneoff:
        cls += " mc-tariff--oneoff"
    badge = ""
    if recommended:
        badge = '          <p><span class="mc-badge mc-badge--recommended">%s</span></p>\n' % t(loc, "prices.badge.recommended")
    feats = "\n".join("            <li>%s</li>" % t(loc, k) for k in features)
    pricecls = "mc-tariff__price"
    if phrase:
        pricecls += " mc-tariff__price--phrase"
    return """        <div class="%(cls)s">
%(badge)s          <p class="mc-tariff__eyebrow">%(period)s</p>
          <h3 class="mc-tariff__name">%(name)s</h3>
          <p class="%(pricecls)s">%(price)s</p>
          <p class="mc-tariff__period">%(pitch)s</p>
          <ul class="mc-tariff__list" role="list">
%(feats)s
          </ul>
          <p class="mc-tariff__cta"><a class="mc-btn mc-btn--%(rank)s" href="%(ctaurl)s">%(cta)s</a></p>
        </div>""" % {
        "cls": cls,
        "badge": badge,
        "period": t(loc, periodkey),
        "name": t(loc, prefix + ".name"),
        "pricecls": pricecls,
        "price": t(loc, prefix + ".price"),
        "pitch": t(loc, prefix + ".pitch"),
        "feats": feats,
        "rank": "primary" if recommended else "secondary",
        "ctaurl": ctaroute,
        "cta": t(loc, ctakey),
    }


def page_prices(loc, lang, og):
    o = [head(loc, lang, og, "prices", "prices"), header(loc, "prices")]

    o.append("""    <section class="mc-section">
      <div class="mc-page">
        <h1>%(h1)s</h1>
        <p class="mc-body-lg mc-measure">%(subhead)s</p>
        <p class="mc-measure">%(sameness)s</p>
        <p class="mc-measure">%(onelist)s</p>
        <p class="mc-caption mc-text-secondary">%(coverage)s</p>
        <p class="mc-caption mc-text-secondary">%(currency)s</p>
      </div>
    </section>""" % {
        "h1": t(loc, "prices.h1"),
        "subhead": t(loc, "prices.subhead"),
        "sameness": t(loc, "prices.sameness"),
        "onelist": t(loc, "prices.onePriceList"),
        "coverage": t(loc, "prices.coverage"),
        "currency": t(loc, "common.currencyLine"),
    })

    # The inspection stands apart from the annual packages: it is a one-off.
    o.append("""    <section class="mc-section">
      <div class="mc-page">
        <div class="mc-tariff mc-tariff--oneoff">
          <p><span class="mc-badge">%(chip)s</span></p>
          <p class="mc-tariff__eyebrow">%(rchip)s</p>
          <h2 class="mc-tariff__name">%(name)s</h2>
          <p class="mc-tariff__price">%(price)s</p>
          <p>%(description)s</p>
          <p class="mc-tariff__cta"><a class="mc-btn mc-btn--secondary" href="#consultation">%(cta)s</a></p>
        </div>
      </div>
    </section>""" % {
        "chip": t(loc, "prices.chip.oneoff"),
        "rchip": t(loc, "prices.rail.chip"),
        "name": t(loc, "prices.rail.name"),
        "price": t(loc, "prices.rail.price"),
        "description": t(loc, "prices.rail.description"),
        "cta": t(loc, "prices.rail.cta"),
    })

    single = tariff_card(
        loc, "prices.card.single", False, True, "prices.chip.oneoff", "#consultation",
        "prices.card.single.cta",
        ["prices.card.single.f1", "prices.card.single.f2", "prices.card.single.f3",
         "prices.card.single.f4", "prices.card.single.arithmetic", "prices.card.single.credit"])
    optimal = tariff_card(
        loc, "prices.card.optimal", True, False, "prices.chip.peryear", "#consultation",
        "prices.card.optimal.cta",
        ["prices.card.optimal.f1", "prices.card.optimal.f2", "prices.card.optimal.f3",
         "prices.card.optimal.f4", "prices.card.optimal.arithmetic", "prices.card.optimal.credit"])
    maximum = tariff_card(
        loc, "prices.card.maximum", False, False, "prices.chip.peryear", "#consultation",
        "prices.card.maximum.cta",
        ["prices.card.maximum.f1", "prices.card.maximum.f2", "prices.card.maximum.f3",
         "prices.card.maximum.f4", "prices.card.maximum.arithmetic", "prices.card.maximum.credit"])

    special = """        <div class="mc-tariff">
          <h3 class="mc-tariff__name">%(name)s</h3>
          <p class="mc-tariff__price mc-tariff__price--phrase"><a href="#calculator">%(price)s</a></p>
          <p class="mc-tariff__period">%(definition)s</p>
          <ul class="mc-tariff__list" role="list">
            <li>%(entry)s</li>
            <li>%(floor)s</li>
          </ul>
          <p class="mc-tariff__cta">
            <a class="mc-btn mc-btn--secondary" href="#consultation">%(cta1)s</a>
            <a class="mc-btn mc-btn--quiet" href="#consultation">%(cta2)s</a>
          </p>
        </div>""" % {
        "name": t(loc, "prices.special.name"),
        "price": t(loc, "prices.calc.heading"),
        "definition": t(loc, "prices.special.definition"),
        "entry": t(loc, "prices.special.entryRule"),
        "floor": t(loc, "prices.special.floor"),
        "cta1": t(loc, "prices.special.cta1"),
        "cta2": t(loc, "prices.special.cta2"),
    }

    o.append("""    <section class="mc-section">
      <div class="mc-page">
        <div class="mc-tariffs">
%s
%s
%s
%s
        </div>
        <p class="mc-caption mc-text-secondary">%s</p>
        <p class="mc-caption mc-text-secondary">%s</p>
        <p class="mc-caption mc-text-secondary">%s</p>
      </div>
    </section>""" % (single, optimal, maximum, special,
                     t(loc, "prices.paymentTerm"), t(loc, "prices.noSurcharge"),
                     t(loc, "prices.paymentReality")))

    # ---- THE YEAR RAIL
    cells = []
    for m in range(1, 13):
        attrs = ""
        if m in (3, 6, 9, 12):
            attrs = ' data-visit'
        if m == 12:
            attrs += ' data-window'
        cells.append('            <div class="mc-rail-year__cell"%s><span class="mc-rail-year__tick"></span></div>' % attrs)
    seasons = "\n".join(
        '            <p class="mc-rail-year__season">%s</p>' % t(loc, "prices.year.%s" % s)
        for s in ("spring", "summer", "autumn", "winter")
    )
    o.append("""    <section class="mc-section">
      <div class="mc-page">
        <h2>%(h2)s</h2>
        <div class="mc-rail-year">
%(cells)s
%(seasons)s
        </div>
        <p class="mc-measure">%(footnote)s</p>
      </div>
    </section>""" % {
        "h2": t(loc, "prices.card.optimal.pitch"),
        "cells": "\n".join(cells),
        "seasons": seasons,
        "footnote": t(loc, "prices.year.footnote"),
    })

    # ---- THE CREDIT BLOCK
    routes = "\n".join(
        """          <div class="mc-credit__route">
            <p class="mc-credit__step">%s</p>
          </div>""" % t(loc, "prices.credit.worked%d" % n)
        for n in (1, 2, 3)
    )
    rules = "\n".join("          <li>%s</li>" % t(loc, "prices.credit.rule%d" % n) for n in range(1, 6))
    o.append("""    <section class="mc-section">
      <div class="mc-page">
        <h2>%(headline)s</h2>
        <p class="mc-body-lg mc-measure">%(subline)s</p>
        <div class="mc-credit">
%(routes)s
        </div>
        <ul>
%(rules)s
        </ul>
      </div>
    </section>""" % {
        "headline": t(loc, "prices.credit.headline"),
        "subline": t(loc, "prices.credit.subline"),
        "routes": routes,
        "rules": rules,
    })

    # ---- THE CALCULATOR
    o.append(calculator(loc))

    # ---- RITUAL EXTRAS
    o.append("""    <section class="mc-section">
      <div class="mc-page mc-page--narrow">
        <h2>%(h2)s</h2>
        <ul>
          <li>%(flowers)s</li>
          <li>%(candle)s</li>
        </ul>
        <p>%(line)s</p>
        <p class="mc-caption mc-text-secondary">%(price)s</p>
      </div>
    </section>""" % {
        "h2": t(loc, "prices.ritual.heading"),
        "flowers": t(loc, "prices.ritual.flowers"),
        "candle": t(loc, "prices.ritual.candle"),
        "line": t(loc, "prices.ritual.line"),
        "price": t(loc, "prices.ritual.price"),
    })

    # ---- GUARANTEES
    gs = "\n".join(
        """          <div class="mc-verify__item">
            <h3 class="mc-verify__title">%s</h3>
            <p class="mc-verify__text">%s</p>
          </div>""" % (t(loc, "prices.guarantee.%d.name" % n), t(loc, "prices.guarantee.%d.remedy" % n))
        for n in (1, 2, 3)
    )
    o.append("""    <section class="mc-section">
      <div class="mc-page">
        <h2>%s</h2>
        <div class="mc-verify">
%s
        </div>
      </div>
    </section>""" % (t(loc, "prices.guarantee.h2"), gs))

    o.append(faq(loc, "prices.faq.h2", [("prices.faq.q%d" % n, "prices.faq.a%d" % n) for n in range(1, 7)]))

    o.append("""    <section class="mc-section" id="consultation">
%s
    </section>""" % consultation_form(loc, "form.heading", "form.support"))
    o.append(footer(loc))
    return "\n".join(o)


def calculator(loc):
    """No-JS contract, as specified by the system engineer:
       <form method="get">, each range paired with a number input carrying the
       same value, the arithmetic printed in full above the total.
       The figures below are the DEFAULT configuration (16 m², 2 monuments,
       four visits a year). A GET handler that re-renders them from the query
       string is the developer's job; nothing on this page requires script."""
    return """    <section class="mc-section">
      <div class="mc-page">
        <h2 id="calc-heading">%(h2)s</h2>
        <p class="mc-body-lg mc-measure">%(openformula)s</p>

        <form class="mc-calc" method="get" action="#calculator" id="calculator" aria-labelledby="calc-heading">
          <fieldset>
            <legend class="mc-field__label">%(planlegend)s</legend><!--prices.sameness: no prices.calc.planLegend key exists-->
            <div class="mc-calc__row">
              <label class="mc-chip"><input type="radio" name="plan" value="single"> %(chipsingle)s</label>
              <label class="mc-chip"><input type="radio" name="plan" value="four" checked> %(chipfour)s</label>
              <label class="mc-chip"><input type="radio" name="plan" value="six"> %(chipsix)s</label>
            </div>
          </fieldset>

          <div class="mc-calc__controls">
            <div class="mc-calc__control">
              <label class="mc-field__label" for="calc-area">%(slidearea)s</label>
              <div class="mc-calc__row">
                <input class="mc-slider" type="range" id="calc-area" name="area" min="1" max="100" step="1" value="16" aria-describedby="calc-area-help">
                <label class="mc-sr-only" for="calc-area-n">%(rowarea)s</label>
                <input class="mc-input mc-calc__number" type="number" id="calc-area-n" name="area_n" min="1" max="100" step="1" value="16">
              </div>
              <p class="mc-calc__bounds"><span>1</span><span>100</span></p>
              <p class="mc-field__help" id="calc-area-help">%(caparea)s</p>
            </div>

            <div class="mc-calc__control">
              <label class="mc-field__label" for="calc-mon">%(slidemon)s</label>
              <div class="mc-calc__row">
                <input class="mc-slider" type="range" id="calc-mon" name="monuments" min="1" max="10" step="1" value="2" aria-describedby="calc-mon-help">
                <label class="mc-sr-only" for="calc-mon-n">%(rowmon)s</label>
                <input class="mc-input mc-calc__number" type="number" id="calc-mon-n" name="monuments_n" min="1" max="10" step="1" value="2">
              </div>
              <p class="mc-calc__bounds"><span>1</span><span>10</span></p>
              <p class="mc-field__help" id="calc-mon-help">%(capmon)s</p>
            </div>
          </div>

          <button class="mc-btn mc-btn--secondary" type="submit">%(recalc)s</button>

          <!-- The arithmetic, printed in full so nobody has to trust the total.
               The two rate sentences are the whole formula. -->
          <div class="mc-calc__formula">
            <p>%(rate1)s</p>
            <p>%(rate2)s</p>
            <dl>
              <dt>%(rowbase)s</dt><dd>160,000 ֏</dd>
              <dt>%(rowarea)s</dt><dd>16 m&sup2; &times; 0 = 0 ֏</dd>
              <dt>%(rowmon)s</dt><dd>2 &times; 0 = 0 ֏</dd>
            </dl>
          </div>

          <div class="mc-calc__total">
            <span>%(rowtotal)s</span>
            <span class="mc-calc__total-value">160,000 ֏</span>
          </div>
          <p class="mc-field__help">%(default)s</p>
          <p class="mc-field__help">%(ceiling)s</p>
        </form>
      </div>
    </section>""" % {
        "h2": t(loc, "prices.calc.heading"),
        "openformula": t(loc, "prices.calc.openFormula"),
        "planlegend": t(loc, "prices.sameness"),
        "chipsingle": t(loc, "prices.calc.chip.single"),
        "chipfour": t(loc, "prices.calc.chip.four"),
        "chipsix": t(loc, "prices.calc.chip.six"),
        "slidearea": t(loc, "prices.calc.slider.area"),
        "rowarea": t(loc, "prices.calc.row.area"),
        "caparea": t(loc, "prices.calc.caption.area"),
        "slidemon": t(loc, "prices.calc.slider.monuments"),
        "rowmon": t(loc, "prices.calc.row.monuments"),
        "capmon": t(loc, "prices.calc.caption.monuments"),
        "recalc": t(loc, "form.retry"),
        "rate1": t(loc, "prices.calc.rate1"),
        "rate2": t(loc, "prices.calc.rate2"),
        "rowbase": t(loc, "prices.calc.row.base"),
        "rowtotal": t(loc, "prices.calc.row.total"),
        "default": t(loc, "prices.calc.default"),
        "ceiling": t(loc, "prices.calc.ceiling"),
    }


def page_report(loc, lang, og):
    o = [head(loc, lang, og, "report", "report"), header(loc, "report")]
    anns = "\n".join(
        """          <div class="mc-verify__item">
            <p class="mc-verify__text">%s</p>
          </div>""" % t(loc, "report.ann.%d" % n)
        for n in (1, 2, 3, 4)
    )
    delivery = "\n".join(
        "          <li>%s</li>" % t(loc, "report.delivery.opt%d" % n) for n in (1, 2, 3)
    )
    o.append("""    <section class="mc-section">
      <div class="mc-page">
        <h1>%(h1)s</h1>
        <p class="mc-body-lg mc-measure">%(standfirst)s</p>
      </div>
    </section>

    <section class="mc-section">
      <div class="mc-page">
        <h2>%(sheeth)s</h2>
        <!-- NO PHOTOGRAPHS EXIST. There is no <img>, no stock and no grey
             rectangle standing in for one. The sheet carries what is real
             today; the eight photographs join it after the September shoot. -->
%(sheet)s
        <div class="mc-verify">
%(anns)s
        </div>
      </div>
    </section>

    <section class="mc-section">
      <div class="mc-page mc-page--narrow">
        <h2>%(deliveryq)s</h2>
        <ul>
%(delivery)s
        </ul>
        <p>%(linkpreview)s</p>
        <p>%(reporttime)s</p>
      </div>
    </section>""" % {
        "h1": t(loc, "report.h1"),
        "standfirst": t(loc, "home.report.standfirst"),
        "sheet": report_sheet(loc, with_body=True),
        "sheeth": t(loc, "home.report.h2"),
        "anns": anns,
        "deliveryq": t(loc, "report.delivery.question"),
        "delivery": delivery,
        "linkpreview": t(loc, "report.linkPreview"),
        "reporttime": t(loc, "frozen.report"),
    })
    o.append(protocol_band(loc))
    o.append("""    <section class="mc-section" id="consultation">
%s
    </section>""" % consultation_form(loc, "form.heading", "form.support"))
    o.append(footer(loc))
    return "\n".join(o)


def page_contact(loc, lang, og):
    o = [head(loc, lang, og, "contact", "contacts"), header(loc, "contact")]

    def person(who):
        return """          <div class="mc-family__row">
            <span class="mc-family__avatar" aria-hidden="true"></span>
            <div>
              <p class="mc-family__name">%(name)s</p>
              <p class="mc-family__role">%(role)s</p>
            </div>
            <a class="mc-btn mc-btn--secondary" href="%(tel)s">%(phone)s</a>
            <a class="mc-btn mc-btn--quiet" href="%(wa)s" rel="noopener">%(walabel)s</a>
          </div>""" % {
            "name": t(loc, "common.founder.%s.name" % who),
            "role": t(loc, "common.founder.%s.role" % who),
            "tel": e(loc, "common.founder.%s.tel" % who),
            "phone": t(loc, "common.founder.%s.phone" % who),
            "wa": e(loc, "common.founder.%s.whatsapp" % who),
            "walabel": t(loc, "form.whatsapp"),
        }

    o.append("""    <section class="mc-section">
      <div class="mc-page">
        <h1>%(h1)s</h1>
        <p class="mc-body-lg mc-measure">%(hours)s</p>
        <div class="mc-family">
%(davit)s
%(hayk)s
        </div>
        <p><a href="mailto:%(email)s">%(emailtxt)s</a></p>
        <p>%(channels)s</p>
      </div>
    </section>

    <section class="mc-section">
      <div class="mc-page">
        <h2>%(entityh)s</h2>
        <ul>
          <li>%(legalname)s</li>
          <li>%(registered)s</li>
          <li>%(regnumlabel)s: %(regnum)s</li>
          <li>%(taxlabel)s: %(tax)s</li>
          <li>%(addrlabel)s: %(addr)s</li>
          <li>%(country)s</li>
        </ul>
        <!-- The map is not drawn: the address is published, the map is not
             yet confirmed. A plausible map pin would be invented content. -->
        <p class="mc-caption mc-text-secondary">%(map)s</p>
      </div>
    </section>

    <section class="mc-section" id="consultation">
%(form)s
    </section>""" % {
        "h1": t(loc, "contacts.h1"),
        "hours": t(loc, "contacts.hours"),
        "davit": person("davit"),
        "hayk": person("hayk"),
        "email": e(loc, "common.email"),
        "emailtxt": t(loc, "common.email"),
        "channels": t(loc, "common.channels"),
        "entityh": t(loc, "about.entity.h2"),
        "legalname": t(loc, "common.entity.legalName"),
        "registered": t(loc, "common.entity.registeredName"),
        "regnumlabel": t(loc, "common.entity.regNumberLabel"),
        "regnum": t(loc, "common.entity.regNumber"),
        "taxlabel": t(loc, "common.entity.taxNumberLabel"),
        "tax": t(loc, "common.entity.taxNumber"),
        "addrlabel": t(loc, "common.entity.addressLabel"),
        "addr": t(loc, "common.entity.address"),
        "country": t(loc, "common.entity.country"),
        "map": t(loc, "contacts.map"),
        "form": consultation_form(loc, "contacts.writeUs", "form.support"),
    })
    o.append(footer(loc))
    return "\n".join(o)


def page_404(loc, lang, og):
    # Defect 6: the live 404 template drops the language switcher on all 19
    # routes. This one carries the whole header, switcher included.
    o = [head(loc, lang, og, "404", "404"),
         header(loc, "home", langroute="404", ctahref=u(loc, "contact") + "#consultation")]
    links = [
        ("how", "nav.how"), ("prices", "nav.prices"), ("report", "nav.report"),
        ("family", "nav.family"), ("about", "nav.about"), ("contact", "nav.contacts"),
    ]
    lis = "\n".join('          <li><a href="%s">%s</a></li>' % (u(loc, r), t(loc, k)) for r, k in links)
    o.append("""    <section class="mc-section">
      <div class="mc-page mc-page--narrow">
        <h1>%(h1)s</h1>
        <p class="mc-body-lg">%(line)s</p>
        <ul>
%(links)s
        </ul>
        <p><a href="%(tel)s">%(phone)s</a></p>
      </div>
    </section>""" % {
        "h1": t(loc, "error404.heading"),
        "line": t(loc, "error404.line"),
        "links": lis,
        "tel": e(loc, "common.founder.hayk.tel"),
        "phone": t(loc, "error404.phone"),
    })
    o.append(footer(loc))
    return "\n".join(o)


def page_root():
    """The bare root. No script: a meta refresh plus three real links, so a
    reader who lands here with scripting off still gets a choice."""
    langs = "\n".join(
        '      <li class="mc-lang__item"><a class="mc-lang__link" hreflang="%s" lang="%s" href="%s">%s</a></li>'
        % (l2, l2, u(seg, "home"), html.escape(S[seg]["header.lang." + l2]))
        for seg, l2, _ in LOCALES
    )
    alts = "\n".join(
        '  <link rel="alternate" hreflang="%s" href="%s">' % (l2, u(seg, "home")) for seg, l2, _ in LOCALES
    )
    return """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>%(title)s</title><!--meta.home.title-->
  <meta http-equiv="refresh" content="0; url=/en/">
  <link rel="canonical" href="/en/">
%(alts)s
  <link rel="alternate" hreflang="x-default" href="/en/">
  <meta name="robots" content="noindex, follow">
  <link rel="stylesheet" href="/assets/tokens.css">
  <link rel="stylesheet" href="/assets/base.css">
  <link rel="stylesheet" href="/assets/components.css">
</head>
<body>
  <main id="main" tabindex="-1" class="mc-section">
    <div class="mc-page mc-page--narrow">
      <h1>%(brand)s</h1>
      <p class="mc-body-lg">%(descriptor)s</p>
      <nav class="mc-lang" aria-label="%(langlabel)s"><!--header.lang.label-->
        <ul class="mc-lang__list" role="list">
%(langs)s
        </ul>
      </nav>
    </div>
  </main>
</body>
</html>
""" % {
        "title": html.escape(S["en"]["meta.home.title"]),
        "alts": alts,
        "brand": html.escape(S["en"]["common.brand"]) + "<!--common.brand-->",
        "descriptor": html.escape(S["en"]["common.descriptor"]) + "<!--common.descriptor-->",
        "langlabel": html.escape(S["en"]["header.lang.label"], quote=True),
        "langs": langs,
    }


PAGES = [
    ("home", page_home), ("how", page_how), ("prices", page_prices),
    ("report", page_report), ("contact", page_contact), ("404", page_404),
]


def main():
    load()
    written = []
    for seg, lang, og in LOCALES:
        d = os.path.join(SITE, seg)
        os.makedirs(d, exist_ok=True)
        for route, fn in PAGES:
            path = os.path.join(d, FILE[route])
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(fn(seg, lang, og))
            written.append(path)
    p = os.path.join(SITE, "index.html")
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(page_root())
    written.append(p)
    print("wrote %d files" % len(written))
    if MISSING:
        print("MISSING KEYS:", sorted(MISSING))


if __name__ == "__main__":
    main()
