#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the ten account routes in three locales.

Rules this generator keeps, so that thirty files cannot drift apart:
  · every visible string comes from rebrand/strings/<loc>.json by key, and the
    key is printed in an HTML comment beside it;
  · a string the content lead has not written yet is drafted in strings_new.py
    and emitted with [NEW KEY] in the same comment, so one grep finds all of
    them;
  · no colour, no size, no hex in the HTML — every class is from
    assets/components.css;
  · <html lang> is `hy` in the am/ folder;
  · one <h1> per page.
"""
import html, json, os, sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from strings_new import NEW

ROOT = Path('/home/user/memorycare/rebrand')
SITE = ROOT / 'site'
LOCALES = [('en', 'en'), ('ru', 'ru'), ('am', 'hy')]   # (folder, lang attribute)
IDX = {'en': 0, 'ru': 1, 'am': 2}

J = {loc: json.loads((ROOT / 'strings' / f'{loc}.json').read_text(encoding='utf-8'))
     for loc, _ in LOCALES}

MISSING = set()


def raw(loc, key):
    if key in J[loc]:
        return J[loc][key], ''
    if key in NEW:
        MISSING.add(key)
        return NEW[key][IDX[loc]], ' [NEW KEY]'
    raise KeyError(key)


def t(loc, key):
    """String with its key in a comment, escaped for text content."""
    v, flag = raw(loc, key)
    return '<!-- ' + key + flag + ' -->' + html.escape(v)


def a(loc, key):
    """String for an attribute value. The key comment cannot live inside an
    attribute, so callers put it on the element instead."""
    v, _ = raw(loc, key)
    return html.escape(v, quote=True)


def kc(*keys):
    """A comment naming the keys used in the attributes of the next element."""
    out = []
    for k in keys:
        out.append(k + ('' if k in J['en'] else ' [NEW KEY]'))
    return '<!-- ' + ' · '.join(out) + ' -->'


# ---------------------------------------------------------------------------
# routes
# ---------------------------------------------------------------------------
ACCOUNT_NAV = [
    ('account/index.html',    'account.nav.overview'),
    ('account/plots.html',    'account.nav.plots'),
    ('account/packages.html', 'account.nav.packages'),
    ('account/payments.html', 'account.nav.payments'),
    ('account/profile.html',  'account.nav.profile'),
]
MAIN_NAV = [
    ('index.html',         'nav.how'),      # replaced below
]
PUBLIC_NAV = [
    ('how-it-works.html', 'nav.how'),
    ('prices.html',       'nav.prices'),
    ('sample-report.html','nav.report'),
    ('about.html',        'nav.about'),
    ('contact.html',      'nav.contacts'),
]
FOOTER_LEGAL = [
    ('legal/terms.html',        'footer.legal.terms'),
    ('legal/refunds.html',      'footer.legal.refund'),
    ('legal/privacy.html',      'footer.legal.privacy'),
    ('legal/cookies.html',      'footer.legal.cookies'),
    ('legal/restrictions.html', 'footer.legal.limitations'),
    ('legal/security.html',     'footer.legal.security'),
]


def head(loc, lang, route, title_key):
    title, _ = raw(loc, title_key)
    brand, _ = raw(loc, 'common.brand')
    alts = ''.join(
        '\n  <link rel="alternate" hreflang="%s" href="/%s/%s">' % (lg, lc, route)
        for lc, lg in LOCALES)
    return (
        '<!doctype html>\n'
        '<html lang="%s">\n<head>\n' % lang +
        '  <meta charset="utf-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '  <!-- NOT user-scalable=no: the live build ships that on all 36 pages (audit A12). -->\n'
        '  <!-- title: composed from %s + common.brand -->\n' % title_key +
        '  <title>' + html.escape(title) + ' · ' + html.escape(brand) + '</title>\n'
        '  <meta name="robots" content="noindex, nofollow">\n'
        '  <!-- The account area is behind a login: it is never indexed. The live\n'
        '       build sends INDEX, FOLLOW on all 36 pages, these included (audit A11). -->' +
        alts +
        '\n  <link rel="alternate" hreflang="x-default" href="/en/%s">' % route +
        '\n  <link rel="canonical" href="/%s/%s">\n' % (loc, route) +
        '  <!-- Every visible string carries its key from strings/<loc>.json in a\n'
        '       comment. A key marked [NEW KEY] does NOT exist in the string files: the\n'
        '       account area was not in the content lead\'s pass. Those are drafts by the\n'
        '       account engineer and need the content lead and the RU and HY writers. -->\n'
        '  <link rel="stylesheet" href="/assets/tokens.css">\n'
        '  <link rel="stylesheet" href="/assets/base.css">\n'
        '  <link rel="stylesheet" href="/assets/components.css">\n'
        '</head>\n<body>\n'
    )


def header(loc, lang, route, authed):
    L = []
    L.append('<a class="mc-skip-link" href="#main">' + t(loc, 'header.skip') + '</a>')
    L.append('<header class="mc-header">')
    L.append('  <div class="mc-page mc-header__inner">')
    L.append('    <a class="mc-header__brand" href="/%s/index.html">' % loc)
    L.append('      <img class="mc-header__mark" src="/assets/brand/MemoryCare_logo-mark_color.svg" alt="" width="48" height="48">')
    L.append('      <span class="mc-eyebrow">' + t(loc, 'common.brand') + '</span>')
    L.append('    </a>')
    # public menu — nothing is removed from the functionality (owner rule 1)
    L.append('    ' + kc('account.mainnav.label'))
    L.append('    <nav class="mc-nav" aria-label="%s">' % a(loc, 'account.mainnav.label'))
    L.append('      <ul class="mc-nav__list">')
    for href, key in PUBLIC_NAV:
        L.append('        <li class="mc-nav__item"><a class="mc-nav__link" href="/%s/%s">%s</a></li>'
                 % (loc, href, t(loc, key)))
    if authed:
        # Signing out is a POST. Over GET any page that can make the browser
        # issue a request — a prefetcher, a link scanner, an <img> on a hostile
        # page — can sign the customer out. [FOR IGOR] the handler needs a CSRF
        # token in this form and must reject the request without it.
        L.append('        <li class="mc-nav__item">')
        L.append('          <form method="post" action="/%s/account/logout/">' % loc)
        L.append(hidden_lang(loc))
        L.append('            <button class="mc-btn mc-btn--quiet" type="submit">%s</button>'
                 % t(loc, 'account.nav.signout'))
        L.append('          </form>')
        L.append('        </li>')
    else:
        L.append('        <li class="mc-nav__item"><a class="mc-nav__link" href="/%s/account/login.html">%s</a></li>'
                 % (loc, t(loc, 'header.signin')))
    L.append('      </ul>')
    L.append('    </nav>')
    L.append('    ' + kc('header.lang.label'))
    L.append('    <nav class="mc-lang" aria-label="%s">' % a(loc, 'header.lang.label'))
    L.append('      <ul class="mc-lang__list">')
    for lc, lg in LOCALES:
        cur = ' aria-current="true"' if lc == loc else ''
        L.append('        <li class="mc-lang__item"><a class="mc-lang__link" hreflang="%s" href="/%s/%s"%s>%s</a></li>'
                 % (lg, lc, route, cur, t(loc, 'header.lang.' + lg)))
    L.append('      </ul>')
    L.append('    </nav>')
    L.append('  </div>')
    L.append('</header>')
    return '\n'.join(L)


def account_rail(loc, route):
    """The account's own section nav plus the identity line the live build
    keeps in its sidebar. Kept as a nav so the payments item — audit A1, a
    sidebar item shown to paying customers that 404s — still exists."""
    L = ['<div class="mc-page">',
         '  ' + kc('account.nav.label'),
         '  <nav class="mc-nav" aria-label="%s">' % a(loc, 'account.nav.label'),
         '    <ul class="mc-nav__list">']
    for href, key in ACCOUNT_NAV:
        cur = ' aria-current="page"' if href == route else ''
        L.append('      <li class="mc-nav__item"><a class="mc-nav__link" href="/%s/%s"%s>%s</a></li>'
                 % (loc, href, cur, t(loc, key)))
    L += ['    </ul>', '  </nav>',
          '  <p class="mc-caption mc-text-secondary">',
          '    ' + t(loc, 'account.identity.label') + ': ',
          '    <span class="mc-num">{fullname}</span> · <span class="mc-num">{phone}</span> · <span class="mc-num">{email}</span>',
          '  </p>',
          '  <!-- ' + raw(loc, 'account.example.legend')[0] + ' -->',
          '</div>']
    return '\n'.join(L)


def footer(loc):
    L = ['<footer class="mc-footer">',
         '  <div class="mc-page mc-footer__grid">',
         '    <div>',
         '      <p class="mc-footer__heading">' + t(loc, 'footer.col.contact') + '</p>',
         '      <ul class="mc-footer__list" role="list">',
         '        <li class="mc-footer__contact"><a href="' + a(loc, 'common.founder.davit.tel') + '">'
         + t(loc, 'common.founder.davit.phone') + '</a> — ' + t(loc, 'common.founder.davit.roleShort') + '</li>',
         '        <li class="mc-footer__contact"><a href="' + a(loc, 'common.founder.hayk.tel') + '">'
         + t(loc, 'common.founder.hayk.phone') + '</a> — ' + t(loc, 'common.founder.hayk.roleShort') + '</li>',
         '        <li><a href="mailto:' + a(loc, 'common.email') + '">' + t(loc, 'common.email') + '</a></li>',
         '        <li>' + t(loc, 'common.hours') + '</li>',
         '      </ul>',
         '    </div>',
         '    <div>',
         '      <p class="mc-footer__heading">' + t(loc, 'footer.col.legal') + '</p>',
         '      <ul class="mc-footer__list" role="list">']
    for href, key in FOOTER_LEGAL:
        L.append('        <li><a href="/%s/%s">%s</a></li>' % (loc, href, t(loc, key)))
    L += ['      </ul>', '    </div>',
          '    <div>',
          '      <p class="mc-footer__heading">' + t(loc, 'footer.col.company') + '</p>',
          '      <ul class="mc-footer__list" role="list">',
          '        <li><a href="/%s/about.html">%s</a></li>' % (loc, t(loc, 'nav.about')),
          '        <li><a href="/%s/how-it-works.html">%s</a></li>' % (loc, t(loc, 'nav.how')),
          '        <li><a href="/%s/prices.html">%s</a></li>' % (loc, t(loc, 'nav.prices')),
          '      </ul>',
          '    </div>',
          '  </div>',
          '  <div class="mc-page">',
          '    <p class="mc-footer__legal">' + t(loc, 'footer.legal.entity') + '</p>',
          '    <p class="mc-footer__legal">' + t(loc, 'common.entity.registeredName') + '</p>',
          '    <p class="mc-footer__legal">' + t(loc, 'footer.copyright') + '</p>',
          '    <p class="mc-footer__legal">' + t(loc, 'legal.compliance.currency') + '</p>',
          '  </div>',
          '</footer>']
    return '\n'.join(L)


def page(loc, lang, route, title_key, body, authed=True, rail=True):
    out = [head(loc, lang, route, title_key),
           header(loc, lang, route, authed),
           '<main id="main" tabindex="-1">']
    if rail:
        out.append(account_rail(loc, route))
    out.append(body)
    out.append('</main>')
    out.append(footer(loc))
    out.append('</body>\n</html>')
    return '\n'.join(out) + '\n'


# ---------------------------------------------------------------------------
# small builders
# ---------------------------------------------------------------------------
def field(loc, name, label_key, itype='text', required=False, help_key=None,
          value='', extra='', autocomplete=None, help_text=None, inputmode=None):
    fid = 'f-' + name
    L = ['<div class="mc-field">']
    L.append('  <label class="mc-field__label" for="%s">%s%s</label>' % (
        fid, t(loc, label_key),
        ' <span class="mc-field__required" aria-hidden="true">*</span>' if required else
        ' <span class="mc-field__optional">(' + t(loc, 'account.optional') + ')</span>'))
    attrs = 'class="mc-input" id="%s" name="%s" type="%s"' % (fid, name, itype)
    if required:
        attrs += ' required'
    if value:
        attrs += ' value="%s"' % value
    if autocomplete:
        attrs += ' autocomplete="%s"' % autocomplete
    if inputmode:
        attrs += ' inputmode="%s"' % inputmode
    if help_key or help_text:
        attrs += ' aria-describedby="%s-help"' % fid
    if extra:
        attrs += ' ' + extra
    L.append('  <input %s>' % attrs)
    if help_key:
        L.append('  <p class="mc-field__help" id="%s-help">%s</p>' % (fid, t(loc, help_key)))
    elif help_text:
        L.append('  <p class="mc-field__help" id="%s-help">%s</p>' % (fid, help_text))
    L.append('</div>')
    return '\n'.join(L)


def hidden_lang(loc):
    return ('    <!-- The endpoint contract keeps the folder code (am|ru|en), not the\n'
            '         BCP-47 tag: this value is `am` where <html lang> is `hy`. -->\n'
            '    <input type="hidden" name="lang" value="%s">' % loc)


def error_summary(loc):
    """The failed-submit state, in an inert <template>. Not [hidden]: several
    components set their own `display`, which beats the UA rule for [hidden],
    so a 'hidden' example can appear on screen at some widths. Template content
    is never rendered, never fetched and never crawled."""
    return '\n'.join([
        '<!-- THE FAILED-SUBMIT STATE. The server renders the panel below at the top of',
        '     the form, with tabindex="-1" and autofocus, so focus lands on it with no',
        '     script. It is inside <template>: template content is inert — never',
        '     rendered, never fetched, never crawled — so the reference markup for the',
        '     other state can live in the same file without appearing on this one.',
        '     Field level: each wrong control gets aria-invalid="true",',
        '     aria-describedby pointing at a <p class="mc-field__error">, and a thicker',
        '     border. Three signals, never colour alone. -->',
        '<template data-state="invalid">',
        '  <div class="mc-form-error" role="alert" tabindex="-1">',
        '    <p class="mc-form-error__title">' + t(loc, 'account.error.summary.title') + '</p>',
        '    <p>' + t(loc, 'form.error.summary') + '</p>',
        '  </div>',
        '</template>'])


# ---------------------------------------------------------------------------
# 1. DASHBOARD — the empty state a new pilot customer meets in September
# ---------------------------------------------------------------------------
def p_index(loc):
    L = ['<section class="mc-section">', '  <div class="mc-page">',
         '    <h1>' + t(loc, 'account.dashboard.h1') + '</h1>',
         '    <p class="mc-body-lg mc-measure">' + t(loc, 'account.dashboard.standfirst') + '</p>',
         '',
         '    <!-- THE EMPTY STATE IS THE PAGE. A new account has no plot, no order and no',
         '         report; that is what the first pilot customer sees. Each panel names what',
         '         is missing and carries the one action that fills it. The populated',
         '         dashboard is the same three panels with the list markup used on',
         '         plots.html, packages.html and payments.html. -->',
         '    <!-- .mc-tariffs is used here only as the auto-fit grid; see the report: a',
         '         neutral grid utility does not exist in components.css. -->',
         '    <div class="mc-tariffs">',
         '',
         '      <div class="mc-empty">',
         '        <h2 class="mc-empty__title">' + t(loc, 'account.dashboard.plots.title') + '</h2>',
         '        <p class="mc-empty__text">' + t(loc, 'account.plots.empty.text') + '</p>',
         '        <a class="mc-btn mc-btn--primary" href="/%s/account/plot-new.html">%s</a>' % (loc, t(loc, 'account.plots.add.cta')),
         '      </div>',
         '',
         '      <div class="mc-empty">',
         '        <h2 class="mc-empty__title">' + t(loc, 'account.dashboard.orders.title') + '</h2>',
         '        <p class="mc-empty__text">' + t(loc, 'account.dashboard.orders.text') + '</p>',
         '        <a class="mc-btn mc-btn--secondary" href="/%s/account/order.html">%s</a>' % (loc, t(loc, 'account.order.h1')),
         '      </div>',
         '',
         '      <div class="mc-empty">',
         '        <h2 class="mc-empty__title">' + t(loc, 'account.dashboard.reports.title') + '</h2>',
         '        <p class="mc-empty__text">' + t(loc, 'empty.reports') + '</p>',
         '        <a class="mc-btn mc-btn--quiet" href="/%s/sample-report.html">%s</a>' % (loc, t(loc, 'report.h1')),
         '      </div>',
         '',
         '    </div>',
         '    <h2>' + t(loc, 'account.dashboard.next.h2') + '</h2>',
         '    <ol class="mc-measure">',
         '      <li>' + t(loc, 'account.dashboard.step1') + '</li>',
         '      <li>' + t(loc, 'account.dashboard.step2') + '</li>',
         '      <li>' + t(loc, 'account.dashboard.step3') + '</li>',
         '    </ol>',
         '    <p class="mc-measure">' + t(loc, 'frozen.callback') + '</p>',
         '    <p class="mc-measure">' + t(loc, 'prices.paymentReality') + '</p>',
         '    <p class="mc-measure">' + t(loc, 'legal.compliance.noTrial') + '</p>',
         '',
         '    <h2>' + t(loc, 'account.dashboard.help.h2') + '</h2>',
         '    <ul class="mc-measure" role="list">',
         '      <li class="mc-num"><a href="' + a(loc, 'common.founder.davit.tel') + '">' + t(loc, 'common.founder.davit.phone') + '</a> — ' + t(loc, 'common.founder.davit.role') + '</li>',
         '      <li class="mc-num"><a href="' + a(loc, 'common.founder.hayk.tel') + '">' + t(loc, 'common.founder.hayk.phone') + '</a> — ' + t(loc, 'common.founder.hayk.role') + '</li>',
         '      <li><a href="mailto:' + a(loc, 'common.email') + '">' + t(loc, 'common.email') + '</a></li>',
         '    </ul>',
         '    <p class="mc-measure">' + t(loc, 'common.channels') + '</p>',
         '  </div>',
         '</section>']
    return '\n'.join(L)


# ---------------------------------------------------------------------------
# 2. PLOTS — "my objects", empty today, with the way to add one
# ---------------------------------------------------------------------------
def p_plots(loc):
    cols = ['account.plots.col.name', 'account.plots.col.cemetery', 'account.plots.col.area',
            'account.plots.col.monuments', 'account.plots.col.care', 'account.plots.col.action']
    L = ['<section class="mc-section">', '  <div class="mc-page">',
         '    <h1>' + t(loc, 'account.plots.h1') + '</h1>',
         '    <p class="mc-body-lg mc-measure">' + t(loc, 'account.plots.standfirst') + '</p>',
         '',
         '    <!-- EMPTY STATE — the state of every account until a plot is added. The live',
         '         build renders this screen as 152 characters of header and footer chrome',
         '         with no content and no way to add anything (audit A7). -->',
         '    <div class="mc-empty">',
         '      <h2 class="mc-empty__title">' + t(loc, 'account.plots.empty.title') + '</h2>',
         '      <p class="mc-empty__text">' + t(loc, 'account.plots.empty.text') + '</p>',
         '      <a class="mc-btn mc-btn--primary" href="/%s/account/plot-new.html">%s</a>' % (loc, t(loc, 'account.plots.add.cta')),
         '      <p class="mc-empty__text">' + t(loc, 'account.plots.callInstead') + '</p>',
         '      <p class="mc-num"><a href="' + a(loc, 'common.founder.hayk.tel') + '">' + t(loc, 'common.founder.hayk.phone') + '</a></p>',
         '    </div>',
         '',
         '    <!-- POPULATED STATE — the same screen once a plot exists. The server renders',
         '         this table instead of the panel above; it is kept here in an inert',
         '         <template>, so the markup of both states lives in one file without the',
         '         other one rendering. --stack turns each row into a',
         '         labelled block below 48rem, which is the fix for the row that overlaps',
         '         itself at 360 (audit A2). -->',
         '    <template data-state="populated">',
         '      <p><a class="mc-btn mc-btn--primary" href="/%s/account/plot-new.html">%s</a></p>' % (loc, t(loc, 'account.plots.add.cta')),
         '      <table class="mc-table mc-table--stack">',
         '        <caption>' + t(loc, 'account.plots.table.caption') + '</caption>',
         '        <thead>',
         '          <tr>']
    for c in cols:
        L.append('            <th scope="col">' + t(loc, c) + '</th>')
    L += ['          </tr>', '        </thead>', '        <tbody>', '          <tr>',
          '            <th scope="row" data-label="' + a(loc, 'account.plots.col.name') + '">{plot_name}</th>',
          '            <td data-label="' + a(loc, 'account.plots.col.cemetery') + '">{cemetery}</td>',
          '            <td data-numeric data-label="' + a(loc, 'account.plots.col.area') + '">{area}</td>',
          '            <td data-numeric data-label="' + a(loc, 'account.plots.col.monuments') + '">{monuments}</td>',
          '            <td data-label="' + a(loc, 'account.plots.col.care') + '">{care}</td>',
          '            <td data-action data-label="' + a(loc, 'account.plots.col.action') + '">',
          '              <a class="mc-btn mc-btn--secondary" href="/%s/account/order.html">%s</a>' % (loc, t(loc, 'account.plots.order.cta')),
          '            </td>',
          '          </tr>', '        </tbody>', '      </table>', '    </template>',
          '  </div>', '</section>']
    return '\n'.join(L)


# ---------------------------------------------------------------------------
# 3. PLOT-NEW — the page that did not exist
# ---------------------------------------------------------------------------
def p_plot_new(loc):
    L = ['<section class="mc-section">', '  <div class="mc-page mc-page--narrow mc-stack--loose mc-stack">',
         '    <h1>' + t(loc, 'account.plotnew.h1') + '</h1>',
         '    <p class="mc-body-lg">' + t(loc, 'account.plotnew.standfirst') + '</p>',
         '',
         '    ' + error_summary(loc).replace('\n', '\n    '),
         '',
         '    <!-- [FOR IGOR] endpoint. The plot object does not exist in the platform today',
         '         (audit A7): there is no plot, no cemetery, no area and no monument count',
         '         anywhere behind the login. This form is the create step for it. -->',
         '    <form method="post" action="/%s/account/plots/create/">' % loc,
         hidden_lang(loc),
         '',
         '      <fieldset>',
         '        <legend class="mc-h3">' + t(loc, 'account.plotnew.fieldset') + '</legend>',
         field(loc, 'plot_name', 'account.plotnew.label.name', required=True,
               help_key='account.plotnew.help.name', autocomplete='off'),
         field(loc, 'cemetery', 'account.plotnew.label.cemetery', required=True,
               help_key='account.plotnew.help.cemetery', autocomplete='off'),
         field(loc, 'location', 'account.plotnew.label.location',
               help_key='account.plotnew.help.location', autocomplete='off'),
         field(loc, 'area', 'account.plotnew.label.area', itype='number',
               help_key='prices.coverage', extra='min="1" max="1000" step="0.5"', inputmode='decimal'),
         field(loc, 'monuments', 'account.plotnew.label.monuments', itype='number',
               help_key='prices.calc.rate2', extra='min="0" max="20" step="1"', inputmode='numeric'),
         field(loc, 'yerevan_contact', 'account.plotnew.label.contact',
               help_key='family.yerevanRelative', autocomplete='off'),
         '      </fieldset>',
         '',
         '      <div class="mc-field">',
         '        <label class="mc-check">',
         '          <input class="mc-check__input" type="checkbox" name="show_monument_name" value="1" aria-describedby="f-privacy-help">',
         '          <span class="mc-check__label">' + t(loc, 'account.plotnew.label.showName') + '</span>',
         '        </label>',
         '        <p class="mc-field__help" id="f-privacy-help">' + t(loc, 'family.privacy') + '</p>',
         '      </div>',
         '',
         '      <div class="mc-field">',
         '        <label class="mc-field__label" for="f-note">' + t(loc, 'account.plotnew.label.note') +
         ' <span class="mc-field__optional">(' + t(loc, 'account.optional') + ')</span></label>',
         '        <textarea class="mc-textarea" id="f-note" name="note" rows="4" aria-describedby="f-note-help"></textarea>',
         '        <p class="mc-field__help" id="f-note-help">' + t(loc, 'account.plotnew.help.note') + '</p>',
         '      </div>',
         '',
         '      <p class="mc-legal">' + t(loc, 'account.required') + '</p>',
         '      <p>',
         '        <button class="mc-btn mc-btn--primary" type="submit">' + t(loc, 'account.plotnew.submit') + '</button>',
         '        <a class="mc-btn mc-btn--quiet" href="/%s/account/plots.html">%s</a>' % (loc, t(loc, 'account.plotnew.back')),
         '      </p>',
         '    </form>',
         '',
         '    <p class="mc-measure">' + t(loc, 'account.plots.callInstead') + '</p>',
         '    <p class="mc-num"><a href="' + a(loc, 'common.founder.hayk.tel') + '">' + t(loc, 'common.founder.hayk.phone') + '</a> · <a href="mailto:' + a(loc, 'common.email') + '">' + t(loc, 'common.email') + '</a></p>',
         '  </div>',
         '</section>']
    return '\n'.join(L)


# ---------------------------------------------------------------------------
# 4. ORDER — the form that had six hidden inputs and no visible field
# ---------------------------------------------------------------------------
PRODUCTS = [
    ('inspection',  'prices.rail.name',           'prices.rail.description',      'prices.rail.price',           'prices.chip.oneoff'),
    ('single',      'prices.card.single.name',    'prices.card.single.pitch',     'prices.card.single.price',    'prices.chip.oneoff'),
    ('four',        'prices.card.optimal.name',   'prices.card.optimal.pitch',    'prices.card.optimal.price',   'prices.chip.peryear'),
    ('six',         'prices.card.maximum.name',   'prices.card.maximum.pitch',    'prices.card.maximum.price',   'prices.chip.peryear'),
]


def p_order(loc):
    L = ['<section class="mc-section">', '  <div class="mc-page mc-page--narrow mc-stack--loose mc-stack">',
         '    <h1>' + t(loc, 'account.order.h1') + '</h1>',
         '    <p class="mc-body-lg">' + t(loc, 'account.order.standfirst') + '</p>',
         '',
         '    ' + error_summary(loc).replace('\n', '\n    '),
         '',
         '    <!-- [FOR IGOR] endpoint. The live form is posted by script with no action and',
         '         no method; this one works with scripting off. -->',
         '    <form method="post" action="/%s/account/order/">' % loc,
         '',
         '      <!-- THE HIDDEN FIELDS, AND THE ONE THAT IS GONE.',
         '           Kept, because nothing is removed from the functionality:',
         '             cid   — the customer, as in the live build',
         '             title — the product name that reaches the invoice',
         '             p, f  — the visit counts the platform stores',
         '             lang  — the locale the endpoint answers in; per-locale here, so a',
         '                     Russian customer no longer posts to /am/ (audit A5)',
         '           REMOVED: <input type="hidden" name="price">. The amount must be derived',
         '           on the server from the chosen product and the plot. It travelled in a',
         '           browser-controlled field on both money forms (audit A6, question Q1),',
         '           and whether the server re-derives it was never tested.',
         '           ⚠ [BLOCKED — Igor] `p` and `f` are the preventive/full split the owner',
         '           rejected on 26.08 ("all visits are full visits"). The words appear',
         '           nowhere on this page. What the two fields should carry once the split',
         '           is gone is a data-model decision, not a copy decision; both are left',
         '           server-filled here rather than guessed. -->',
         '      <input type="hidden" name="cid" value="{customer_id}">',
         '      <input type="hidden" name="title" value="{product_title}">',
         '      <input type="hidden" name="p" value="{p}">',
         '      <input type="hidden" name="f" value="{f}">',
         hidden_lang(loc),
         '',
         '      <fieldset class="mc-stack">',
         '        <legend class="mc-h3">' + t(loc, 'account.order.step1') + '</legend>',
         '',
         '        <!-- THE MISSING FIELD (audit A7). One radio group of plots, so the order',
         '             carries the grave it is for. The add row is part of the control: an',
         '             empty picker must not be a dead end. -->',
         '        <div class="mc-plots">',
         '          <label class="mc-plot">',
         '            <input class="mc-plot__input" type="radio" name="plot" value="{plot_id}" checked required>',
         '            <span class="mc-plot__body">',
         '              <span class="mc-plot__name">{plot_name}</span>',
         '              <span class="mc-plot__meta">{cemetery} · {location}</span>',
         '            </span>',
         '            <span class="mc-plot__size mc-num">{area} · {monuments}</span>',
         '          </label>',
         '',
         '          <!-- The server repeats the label above once per plot on the account. -->',
         '',
         '          <a class="mc-plot mc-plot--add" href="/%s/account/plot-new.html">' % loc,
         '            <span aria-hidden="true">+</span>',
         '            <span class="mc-plot__body"><span class="mc-plot__name">' + t(loc, 'account.order.addplot') + '</span></span>',
         '          </a>',
         '        </div>',
         '',
         '        <!-- With no plot on the account the server renders this instead of the',
         '             radio group, and the add row above stays. -->',
         '        <template data-state="empty"><p class="mc-field__help">' + t(loc, 'account.order.noplot') + '</p></template>',
         '      </fieldset>',
         '',
         '      <fieldset class="mc-stack">',
         '        <legend class="mc-h3">' + t(loc, 'account.order.step2') + '</legend>',
         '        <!-- The plot picker markup, reused for the product: one radio group, one',
         '             choice always made, the choice inside the form data. -->',
         '        <div class="mc-plots">']
    for pid, nk, pk, prk, chipk in PRODUCTS:
        checked = ' checked' if pid == 'four' else ''
        L += ['          <label class="mc-plot">',
              '            <input class="mc-plot__input" type="radio" name="product" value="%s"%s required>' % (pid, checked),
              '            <span class="mc-plot__body">',
              '              <span class="mc-plot__name">' + t(loc, nk) + '</span>',
              '              <span class="mc-plot__meta">' + t(loc, pk) + '</span>',
              '            </span>',
              '            <span class="mc-plot__size mc-num">' + t(loc, prk) + '</span>',
              '          </label>']
    L += ['        </div>',
          '        <p class="mc-field__help">' + t(loc, 'prices.coverage') + '</p>',
          '        <p class="mc-field__help">' + t(loc, 'prices.card.optimal.credit') + '</p>',
          '        <p class="mc-field__help">' + t(loc, 'prices.special.entryRule') + ' <a href="/%s/index.html#consultation">%s</a></p>' % (loc, t(loc, 'prices.special.cta2')),
          '      </fieldset>',
          '',
          '      <h2>' + t(loc, 'account.order.step3') + '</h2>',
          '      <table class="mc-table mc-table--stack">',
          '        <caption>' + t(loc, 'account.order.summary.caption') + '</caption>',
          '        <tbody>',
          '          <tr><th scope="row">' + t(loc, 'prices.calc.row.base') + '</th>',
          '              <td data-numeric data-label="' + a(loc, 'prices.calc.row.base') + '">{base} ֏ AMD</td></tr>',
          '          <tr><th scope="row">' + t(loc, 'prices.calc.row.area') + '</th>',
          '              <td data-numeric data-label="' + a(loc, 'prices.calc.row.area') + '">{area_surcharge} ֏ AMD</td></tr>',
          '          <tr><th scope="row">' + t(loc, 'prices.calc.row.monuments') + '</th>',
          '              <td data-numeric data-label="' + a(loc, 'prices.calc.row.monuments') + '">{monument_surcharge} ֏ AMD</td></tr>',
          '          <tr><th scope="row">' + t(loc, 'prices.calc.row.total') + '</th>',
          '              <td data-numeric data-label="' + a(loc, 'prices.calc.row.total') + '"><strong class="mc-price">{total} ֏ AMD</strong></td></tr>',
          '        </tbody>',
          '      </table>',
          '      <p class="mc-field__help">' + t(loc, 'prices.calc.rate1') + '</p>',
          '      <p class="mc-field__help">' + t(loc, 'prices.calc.rate2') + '</p>',
          '      <p class="mc-field__help">' + t(loc, 'account.order.serverPrice') + '</p>',
          '      <p class="mc-field__help">' + t(loc, 'prices.noSurcharge') + '</p>',
          '',
          '      <div class="mc-field">',
          '        <label class="mc-check">',
          '          <input class="mc-check__input" type="checkbox" name="consent" value="1" required>',
          '          <span class="mc-check__label">' + t(loc, 'account.order.consent') +
          ' <a href="/%s/legal/terms.html">%s</a> · <a href="/%s/legal/refunds.html">%s</a></span>' % (
              loc, t(loc, 'footer.legal.terms'), loc, t(loc, 'footer.legal.refund')),
          '        </label>',
          '      </div>',
          '',
          '      <p><button class="mc-btn mc-btn--primary" type="submit">' + t(loc, 'account.order.submit') + '</button></p>',
          '    </form>',
          '',
          '    <h2>' + t(loc, 'account.order.next.h2') + '</h2>',
          '    <p class="mc-measure">' + t(loc, 'frozen.callback') + '</p>',
          '    <p class="mc-measure">' + t(loc, 'prices.paymentReality') + '</p>',
          '    <p class="mc-measure">' + t(loc, 'prices.paymentTerm') + '</p>',
          '    <p class="mc-measure">' + t(loc, 'legal.compliance.noTrial') + '</p>',
          '  </div>',
          '</section>']
    return '\n'.join(L)


# ---------------------------------------------------------------------------
# 5. PACKAGES — the Pay action, and the cancellation that did not exist
# ---------------------------------------------------------------------------
def p_packages(loc):
    cols = ['account.packages.col.service', 'account.packages.col.plot', 'account.packages.col.visits',
            'account.packages.col.period', 'account.packages.col.paid', 'account.packages.col.status',
            'account.packages.col.action']
    L = ['<section class="mc-section">', '  <div class="mc-page">',
         '    <h1>' + t(loc, 'account.packages.h1') + '</h1>',
         '    <p class="mc-body-lg mc-measure">' + t(loc, 'account.packages.standfirst') + '</p>',
         '',
         '    <!-- NARROW WIDTHS (audit A2). --stack turns every row into a labelled block',
         '         below 48rem and gives the action cell the full column width, so the Pay',
         '         button cannot sit at left:371px in a 360px viewport, and no row can',
         '         overlap another. Nothing here sets padding-inline: only .mc-page does. -->',
         '    <table class="mc-table mc-table--stack">',
         '      <caption>' + t(loc, 'account.packages.table.caption') + '</caption>',
         '      <thead>', '        <tr>']
    for c in cols:
        L.append('          <th scope="col">' + t(loc, c) + '</th>')
    L += ['        </tr>', '      </thead>', '      <tbody>',
          '',
          '        <!-- An active annual subscription: the row that can be cancelled. -->',
          '        <tr>',
          '          <th scope="row" data-label="' + a(loc, 'account.packages.col.service') + '">' + t(loc, 'prices.card.optimal.name') + '</th>',
          '          <td data-label="' + a(loc, 'account.packages.col.plot') + '">{plot_name}</td>',
          '          <td data-numeric data-label="' + a(loc, 'account.packages.col.visits') + '">{done} / {total}</td>',
          '          <td data-label="' + a(loc, 'account.packages.col.period') + '"><time datetime="{start_iso}">{start}</time> — <time datetime="{end_iso}">{end}</time></td>',
          '          <td data-numeric data-label="' + a(loc, 'account.packages.col.paid') + '">{paid} ֏ AMD</td>',
          '          <td data-label="' + a(loc, 'account.packages.col.status') + '">',
          '            <!-- Status is never colour alone: the badge prints a glyph. -->',
          '            <span class="mc-badge" data-status="active" data-glyph="✓">' + t(loc, 'account.packages.status.active') + '</span>',
          '          </td>',
          '          <td data-action data-label="' + a(loc, 'account.packages.col.action') + '">',
          '            <a class="mc-btn mc-btn--secondary" href="#cancel-1">' + t(loc, 'account.cancel.open') + '</a>',
          '          </td>',
          '        </tr>',
          '',
          '        <!-- An order that is not paid yet: the row that carries the Pay action. -->',
          '        <tr>',
          '          <th scope="row" data-label="' + a(loc, 'account.packages.col.service') + '">' + t(loc, 'prices.card.single.name') + '</th>',
          '          <td data-label="' + a(loc, 'account.packages.col.plot') + '">{plot_name}</td>',
          '          <td data-numeric data-label="' + a(loc, 'account.packages.col.visits') + '">{done} / {total}</td>',
          '          <td data-label="' + a(loc, 'account.packages.col.period') + '">{period}</td>',
          '          <td data-numeric data-label="' + a(loc, 'account.packages.col.paid') + '">{amount} ֏ AMD</td>',
          '          <td data-label="' + a(loc, 'account.packages.col.status') + '">',
          '            <span class="mc-badge" data-status="awaiting" data-glyph="•">' + t(loc, 'account.packages.status.awaiting') + '</span>',
          '          </td>',
          '          <td data-action data-label="' + a(loc, 'account.packages.col.action') + '">',
          '            <!-- The pay form keeps `id` and `lang` and has lost `price`: the',
          '                 amount is the server\'s, not the browser\'s (audit A6). The',
          '                 endpoint is per-locale, not the hard-coded /am/ of the live',
          '                 build (audit A5). White on pure red at 4.00 is gone with it',
          '                 (audit A14): this is the primary button of the system. -->',
          '            <form method="post" action="/%s/account/packages/pay/">' % loc,
          '              <input type="hidden" name="id" value="{order_id}">',
          hidden_lang(loc),
          '              <button class="mc-btn mc-btn--primary" type="submit">' + t(loc, 'account.packages.action.pay') + '</button>',
          '            </form>',
          '          </td>',
          '        </tr>',
          '      </tbody>',
          '    </table>',
          '',
          '    <!-- EMPTY STATE — rendered instead of the table when nothing is ordered. -->',
          '    <template data-state="empty">',
          '    <div class="mc-empty">',
          '      <h2 class="mc-empty__title">' + t(loc, 'account.packages.empty.title') + '</h2>',
          '      <p class="mc-empty__text">' + t(loc, 'account.dashboard.orders.text') + '</p>',
          '      <a class="mc-btn mc-btn--primary" href="/%s/account/order.html">%s</a>' % (loc, t(loc, 'account.order.h1')),
          '    </div>',
          '    </template>',
          '',
          '    <p class="mc-measure">' + t(loc, 'prices.paymentReality') + '</p>',
          '  </div>',
          '</section>',
          '',
          '<!-- THE CANCELLATION DIALOG (audit A8: nothing can be cancelled anywhere, in any',
          '     locale, and Ameriabank requires published cancellation terms).',
          '     Scriptless: the link above targets #cancel-1 and the dialog appears; the',
          '     first control inside it is the way out, and the destructive one is second in',
          '     the tab order. The server renders one of these per cancellable order and',
          '     should serve it as <dialog open>, which also brings ::backdrop with it.',
          '     The arithmetic is on screen before anything is confirmed, and it is computed',
          '     from the amount actually paid — never from the list price, which would',
          '     return more than the client gave us. -->',
          '<div class="mc-modal" id="cancel-1" role="dialog" aria-modal="true" aria-labelledby="cancel-1-title" tabindex="-1">',
          '  <h2 class="mc-modal__title" id="cancel-1-title">' + t(loc, 'account.cancel.title') + '</h2>',
          '  <div class="mc-modal__body mc-stack">',
          '    <p>' + t(loc, 'legal.refund.rule.p1') + '</p>',
          '    <p class="mc-num">' + t(loc, 'legal.refund.rule.formula') + '</p>',
          '    <p class="mc-num"><strong>' + t(loc, 'legal.refund.cancel.line') + '</strong></p>',
          '    <p class="mc-caption">' + t(loc, 'legal.refund.rule.rounding') + '</p>',
          '    <p class="mc-caption">' + t(loc, 'account.cancel.example') + '</p>',
          '    <p class="mc-caption mc-num">' + t(loc, 'legal.refund.example2.paid') + ' — ' + t(loc, 'legal.refund.example2.calc') + '</p>',
          '    <p>' + t(loc, 'legal.refund.cancel.p2') + '</p>',
          '    <p><a href="/%s/legal/refunds.html">%s</a></p>' % (loc, t(loc, 'legal.refund.h1')),
          '  </div>',
          '  <div class="mc-modal__actions">',
          '    <a class="mc-btn mc-btn--secondary" href="#">' + t(loc, 'account.cancel.keep') + '</a>',
          '    <form method="post" action="/%s/account/packages/cancel/">' % loc,
          '      <input type="hidden" name="id" value="{order_id}">',
          hidden_lang(loc),
          '      <button class="mc-btn mc-btn--destructive" type="submit">' + t(loc, 'account.cancel.confirm') + '</button>',
          '    </form>',
          '  </div>',
          '</div>']
    return '\n'.join(L)


# ---------------------------------------------------------------------------
# 6. PAYMENTS — the screen the dead sidebar link should have led to
# ---------------------------------------------------------------------------
def p_payments(loc):
    cols = ['account.payments.col.date', 'account.payments.col.what', 'account.payments.col.amount',
            'account.payments.col.method', 'account.payments.col.status', 'account.payments.col.invoice']
    L = ['<section class="mc-section">', '  <div class="mc-page">',
         '    <h1>' + t(loc, 'account.payments.h1') + '</h1>',
         '    <p class="mc-body-lg mc-measure">' + t(loc, 'account.payments.standfirst') + '</p>',
         '',
         '    <!-- AUDIT A1. This route answers 200 and renders the not-found template on',
         '         the live build, in all three locales, and it is linked from the sidebar',
         '         of every authenticated page — that is, it is shown to people who have',
         '         paid. The nav item is kept; this is the screen it leads to. -->',
         '',
         '    <!-- EMPTY STATE — and it is the true state today: the company has no paying',
         '         customers, so this is what the first pilot customer sees before the',
         '         first invoice. -->',
         '    <div class="mc-empty">',
         '      <h2 class="mc-empty__title">' + t(loc, 'account.payments.empty.title') + '</h2>',
         '      <p class="mc-empty__text">' + t(loc, 'empty.payments') + '</p>',
         '      <a class="mc-btn mc-btn--secondary" href="/%s/account/packages.html">%s</a>' % (loc, t(loc, 'account.packages.h1')),
         '    </div>',
         '',
         '    <!-- POPULATED STATE — rendered instead of the panel above once anything has',
         '         been charged. Every amount is in AMD (§3.5), every row names its',
         '         invoice, and a refunded row shows the refund, not a silent adjustment.',
         '         It is inside an inert <template>: nothing here is a live link, so the',
         '         invoice placeholder cannot be crawled or followed (§4.11).',
         '         [FOR IGOR] invoice URL pattern: /{loc}/account/invoice/<invoice id>/ —',
         '         the server renders the link only for a row that has an invoice, and',
         '         renders no control at all for a row that has none. -->',
         '    <template data-state="populated">',
         '    <table class="mc-table mc-table--stack">',
         '      <caption>' + t(loc, 'account.payments.table.caption') + '</caption>',
         '      <thead>', '        <tr>']
    for c in cols:
        L.append('          <th scope="col">' + t(loc, c) + '</th>')
    L += ['        </tr>', '      </thead>', '      <tbody>',
          '        <tr>',
          '          <th scope="row" data-label="' + a(loc, 'account.payments.col.date') + '"><time datetime="{date_iso}">{date}</time></th>',
          '          <td data-label="' + a(loc, 'account.payments.col.what') + '">{what} · {plot_name}</td>',
          '          <td data-numeric data-label="' + a(loc, 'account.payments.col.amount') + '">{amount} ֏ AMD</td>',
          '          <td data-label="' + a(loc, 'account.payments.col.method') + '">' + t(loc, 'account.payments.method.transfer') + '</td>',
          '          <td data-label="' + a(loc, 'account.payments.col.status') + '">',
          '            <span class="mc-badge" data-status="paid" data-glyph="✓">' + t(loc, 'account.payments.status.paid') + '</span>',
          '          </td>',
          '          <td data-action data-label="' + a(loc, 'account.payments.col.invoice') + '">',
          '            <!-- No href: a placeholder must never ship as a link (§4.11). The',
          '                 server fills the pattern named in the comment above, and',
          '                 renders no control at all for a row with no invoice. -->',
          '            <a class="mc-btn mc-btn--quiet" data-href-pattern="/%s/account/invoice/INVOICE-ID/">%s</a>' % (loc, t(loc, 'account.payments.invoice.link')),
          '          </td>',
          '        </tr>',
          '        <tr>',
          '          <th scope="row" data-label="' + a(loc, 'account.payments.col.date') + '"><time datetime="{date_iso}">{date}</time></th>',
          '          <td data-label="' + a(loc, 'account.payments.col.what') + '">' + t(loc, 'legal.refund.h1') + ' · {plot_name}</td>',
          '          <td data-numeric data-label="' + a(loc, 'account.payments.col.amount') + '">−{amount} ֏ AMD</td>',
          '          <td data-label="' + a(loc, 'account.payments.col.method') + '">' + t(loc, 'account.payments.method.transfer') + '</td>',
          '          <td data-label="' + a(loc, 'account.payments.col.status') + '">',
          '            <span class="mc-badge" data-status="refunded" data-glyph="↩">' + t(loc, 'account.payments.status.refunded') + '</span>',
          '          </td>',
          '          <td data-action data-label="' + a(loc, 'account.payments.col.invoice') + '">',
          '            <!-- No href: a placeholder must never ship as a link (§4.11). The',
          '                 server fills the pattern named in the comment above, and',
          '                 renders no control at all for a row with no invoice. -->',
          '            <a class="mc-btn mc-btn--quiet" data-href-pattern="/%s/account/invoice/INVOICE-ID/">%s</a>' % (loc, t(loc, 'account.payments.invoice.link')),
          '          </td>',
          '        </tr>',
          '      </tbody>',
          '    </table>',
          '    </template>',
          '',
          '    <h2>' + t(loc, 'account.payments.how.h2') + '</h2>',
          '    <p class="mc-measure">' + t(loc, 'legal.terms.payment.p1') + '</p>',
          '    <p class="mc-measure">' + t(loc, 'legal.terms.payment.p2') + '</p>',
          '    <p class="mc-measure">' + t(loc, 'prices.noSurcharge') + '</p>',
          '    <p class="mc-measure">' + t(loc, 'legal.compliance.noTrial') + '</p>',
          '    <p class="mc-measure"><a href="/%s/legal/refunds.html">%s</a> · <a href="/%s/legal/terms.html">%s</a></p>' % (
              loc, t(loc, 'legal.refund.h1'), loc, t(loc, 'footer.legal.terms')),
          '    <!-- The payment-system colour marks required by Ameriabank §4.10.11 belong',
          '         in the footer of every page and are the public site\'s footer component;',
          '         the mark images are not in assets/brand/ yet. Flagged, not faked. -->',
          '  </div>',
          '</section>']
    return '\n'.join(L)


# ---------------------------------------------------------------------------
# 7. PROFILE — the password change that asked for no current password
# ---------------------------------------------------------------------------
def p_profile(loc):
    L = ['<section class="mc-section">', '  <div class="mc-page mc-page--narrow mc-stack--loose mc-stack">',
         '    <h1>' + t(loc, 'account.profile.h1') + '</h1>',
         '',
         '    ' + error_summary(loc).replace('\n', '\n    '),
         '',
         '    <!-- TWO FORMS, NOT ONE. On the live build a single submit changes password,',
         '         e-mail and phone together, with no current password anywhere in it',
         '         (audit A3): a borrowed session becomes permanent account takeover and',
         '         the owner loses the recovery address in the same moment. -->',
         '',
         '    <form method="post" action="/%s/account/profile/">' % loc,
         hidden_lang(loc),
         '      <fieldset>',
         '        <legend class="mc-h3">' + t(loc, 'account.profile.details.h2') + '</legend>',
         '        <!-- input[name=fullname] is the one critical axe violation behind the',
         '             login: it ships with no label at all. It has one here. -->',
         field(loc, 'fullname', 'account.profile.label.fullname', required=True,
               value='{fullname}', autocomplete='name'),
         field(loc, 'phone', 'account.profile.label.phone', itype='tel', required=True,
               value='{phone}', autocomplete='tel', inputmode='tel'),
         field(loc, 'email', 'account.profile.label.email', itype='email', required=True,
               value='{email}', autocomplete='email', help_key='account.profile.help.email'),
         '      </fieldset>',
         '      <p class="mc-legal">' + t(loc, 'account.required') + '</p>',
         '      <p><button class="mc-btn mc-btn--primary" type="submit">' + t(loc, 'account.profile.save') + '</button></p>',
         '    </form>',
         '',
         '    <form method="post" action="/%s/account/password/">' % loc,
         hidden_lang(loc),
         '      <fieldset>',
         '        <legend class="mc-h3">' + t(loc, 'account.profile.password.h2') + '</legend>',
         '        <p class="mc-field__help">' + t(loc, 'account.profile.password.why') + '</p>',
         '        <!-- THE ADDED FIELD. Adding is permitted; removing is not. -->',
         field(loc, 'current_password', 'account.profile.label.current', itype='password',
               required=True, autocomplete='current-password'),
         '        <div class="mc-field">',
         '          <label class="mc-field__label" for="f-new_password">' + t(loc, 'account.profile.label.new') +
         ' <span class="mc-field__required" aria-hidden="true">*</span></label>',
         '          <input class="mc-input" id="f-new_password" name="new_password" type="password" required autocomplete="new-password" aria-describedby="pw-rules">',
         '        </div>',
         field(loc, 'repeat_password', 'account.profile.label.repeat', itype='password',
               required=True, autocomplete='new-password'),
         '        <div id="pw-rules">',
         '          <p class="mc-field__help">' + t(loc, 'account.profile.rules.h') + '</p>',
         '          <ul class="mc-field__help">']
    for i in range(1, 7):
        L.append('            <li>' + t(loc, 'account.profile.rule%d' % i) + '</li>')
    L += ['          </ul>',
          '          <!-- The live build hides these six rules inside a hover tooltip that',
          '               opens on ⓘ with an onclick and has no keyboard path. They are',
          '               plain text here, and the field points at them with',
          '               aria-describedby. -->',
          '        </div>',
          '      </fieldset>',
          '      <p class="mc-legal">' + t(loc, 'account.required') + '</p>',
          '      <p><button class="mc-btn mc-btn--primary" type="submit">' + t(loc, 'account.profile.password.save') + '</button></p>',
          '    </form>',
          '',
          '    <form method="post" action="/%s/account/logout/">' % loc,
          hidden_lang(loc),
          '      <button class="mc-btn mc-btn--quiet" type="submit">' + t(loc, 'account.nav.signout') + '</button>',
          '    </form>',
          '    <p class="mc-measure"><a href="/%s/legal/privacy.html">%s</a> · <a href="/%s/legal/security.html">%s</a></p>' % (
              loc, t(loc, 'footer.legal.privacy'), loc, t(loc, 'footer.legal.security')),
          '  </div>',
          '</section>']
    return '\n'.join(L)


# ---------------------------------------------------------------------------
# 8-10. LOGIN · REGISTER · RESET
# ---------------------------------------------------------------------------
def p_login(loc):
    L = ['<section class="mc-section">', '  <div class="mc-page mc-page--narrow mc-stack--loose mc-stack">',
         '    <h1>' + t(loc, 'account.login.h1') + '</h1>',
         '',
         '    ' + error_summary(loc).replace('\n', '\n    '),
         '',
         '    <form method="post" action="/%s/account/login/">' % loc,
         hidden_lang(loc),
         field(loc, 'email', 'account.profile.label.email', itype='email', required=True,
               autocomplete='username'),
         field(loc, 'password', 'account.label.password', itype='password', required=True,
               autocomplete='current-password'),
         '      <p class="mc-legal">' + t(loc, 'account.required') + '</p>',
         '      <p><button class="mc-btn mc-btn--primary" type="submit">' + t(loc, 'account.login.submit') + '</button></p>',
         '    </form>',
         '    <ul role="list">',
         '      <li><a href="/%s/account/register.html">%s</a></li>' % (loc, t(loc, 'account.login.register')),
         '      <li><a href="/%s/account/reset.html">%s</a></li>' % (loc, t(loc, 'account.login.reset')),
         '    </ul>',
         '    <!-- The live build already answers identically for a known and an unknown',
         '         address (audit B2). That is kept: no message here says whether an',
         '         account exists. -->',
         '  </div>',
         '</section>']
    return '\n'.join(L)


def p_register(loc):
    L = ['<section class="mc-section">', '  <div class="mc-page mc-page--narrow mc-stack--loose mc-stack">',
         '    <h1>' + t(loc, 'account.register.h1') + '</h1>',
         '    <p class="mc-body-lg">' + t(loc, 'account.register.standfirst') + '</p>',
         '',
         '    ' + error_summary(loc).replace('\n', '\n    '),
         '',
         '    <form method="post" action="/%s/account/register/">' % loc,
         hidden_lang(loc),
         field(loc, 'fullname', 'account.profile.label.fullname', required=True, autocomplete='name'),
         field(loc, 'phone', 'account.profile.label.phone', itype='tel', required=True,
               autocomplete='tel', inputmode='tel', help_key='common.channels'),
         field(loc, 'email', 'account.profile.label.email', itype='email', required=True,
               autocomplete='username', help_key='account.profile.help.email'),
         '      <div class="mc-field">',
         '        <label class="mc-field__label" for="f-password">' + t(loc, 'account.label.password') +
         ' <span class="mc-field__required" aria-hidden="true">*</span></label>',
         '        <input class="mc-input" id="f-password" name="password" type="password" required autocomplete="new-password" aria-describedby="pw-rules">',
         '      </div>',
         '      <div id="pw-rules">',
         '        <p class="mc-field__help">' + t(loc, 'account.profile.rules.h') + '</p>',
         '        <ul class="mc-field__help">']
    for i in range(1, 7):
        L.append('          <li>' + t(loc, 'account.profile.rule%d' % i) + '</li>')
    L += ['        </ul>',
          '      </div>',
          '      <div class="mc-field">',
          '        <label class="mc-check">',
          '          <input class="mc-check__input" type="checkbox" name="consent" value="1" required>',
          '          <span class="mc-check__label">' + t(loc, 'account.register.consent') +
          ' <a href="/%s/legal/privacy.html">%s</a></span>' % (loc, t(loc, 'footer.legal.privacy')),
          '        </label>',
          '      </div>',
          '      <p class="mc-legal">' + t(loc, 'account.required') + '</p>',
          '      <p><button class="mc-btn mc-btn--primary" type="submit">' + t(loc, 'account.register.submit') + '</button></p>',
          '    </form>',
          '    <p><a href="/%s/account/login.html">%s</a></p>' % (loc, t(loc, 'account.register.haveaccount')),
          '  </div>',
          '</section>']
    return '\n'.join(L)


def p_reset(loc):
    L = ['<section class="mc-section">', '  <div class="mc-page mc-page--narrow mc-stack--loose mc-stack">',
         '    <h1>' + t(loc, 'account.reset.h1') + '</h1>',
         '    <p class="mc-body-lg">' + t(loc, 'account.reset.standfirst') + '</p>',
         '',
         '    ' + error_summary(loc).replace('\n', '\n    '),
         '',
         '    <form method="post" action="/%s/account/reset/">' % loc,
         hidden_lang(loc),
         field(loc, 'email', 'account.profile.label.email', itype='email', required=True,
               autocomplete='username'),
         '      <p class="mc-legal">' + t(loc, 'account.required') + '</p>',
         '      <p><button class="mc-btn mc-btn--primary" type="submit">' + t(loc, 'account.reset.submit') + '</button></p>',
         '    </form>',
         '    <p class="mc-measure">' + t(loc, 'account.reset.note') + '</p>',
         '    <p><a href="/%s/account/login.html">%s</a></p>' % (loc, t(loc, 'account.login.h1')),
         '  </div>',
         '</section>']
    return '\n'.join(L)


PAGES = [
    ('account/index.html',     'account.dashboard.h1', p_index,    True,  True),
    ('account/plots.html',     'account.plots.h1',     p_plots,    True,  True),
    ('account/plot-new.html',  'account.plotnew.h1',   p_plot_new, True,  True),
    ('account/order.html',     'account.order.h1',     p_order,    True,  True),
    ('account/packages.html',  'account.packages.h1',  p_packages, True,  True),
    ('account/payments.html',  'account.payments.h1',  p_payments, True,  True),
    ('account/profile.html',   'account.profile.h1',   p_profile,  True,  True),
    ('account/login.html',     'account.login.h1',     p_login,    False, False),
    ('account/register.html',  'account.register.h1',  p_register, False, False),
    ('account/reset.html',     'account.reset.h1',     p_reset,    False, False),
]


def main():
    n = 0
    for loc, lang in LOCALES:
        for route, title_key, fn, authed, rail in PAGES:
            dest = SITE / loc / route
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(page(loc, lang, route, title_key, fn(loc), authed, rail), encoding='utf-8')
            n += 1
    print('wrote', n, 'files')
    print('new keys needed:', len(MISSING))
    for k in sorted(MISSING):
        print('  ', k)


if __name__ == '__main__':
    main()
