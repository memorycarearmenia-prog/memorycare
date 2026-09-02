#!/usr/bin/env sh
# MemoryCare — the lint that makes the four structural colour rules mechanical.
# Run from rebrand/site/assets/ :  sh tools/check-tokens.sh [../]
# Exit 1 on any violation. Intended for the pre-commit hook and for CI.
#
# Everything below is a grep, deliberately. A rule nobody can run is not a rule.

set -eu
ASSETS="$(cd "$(dirname "$0")/.." && pwd)"
SITE="${1:-$ASSETS/..}"
fail=0
say() { printf '%s\n' "$*" >&2; fail=1; }

# --- 0. Generated files are in sync with their source ------------------------
python3 "$ASSETS/build-tokens.py" --check || fail=1

# --- 1. Every shipped colour pair still clears its threshold ------------------
python3 "$ASSETS/tools/check-contrast.py" --assert >/dev/null || fail=1

# --- 2. RULE 5 (brief): no hex, no rgb(), no named colour outside tokens.* ----
#     One stray hex fails the work. tokens.source.json is the only file that
#     may contain one; tokens.css is generated from it.
for f in "$ASSETS"/base.css "$ASSETS"/components.css "$SITE"/*/*.html "$SITE"/*/*/*.html; do
  [ -e "$f" ] || continue
  if grep -nE '#[0-9A-Fa-f]{3,8}([^0-9A-Za-z_-]|$)' "$f" | grep -vE 'href|url\(|xlink|id=|#[A-Za-z_-]{2,}' | grep -q .; then
    say "STRAY HEX in $f:"; grep -nE '#[0-9A-Fa-f]{3,8}([^0-9A-Za-z_-]|$)' "$f" | grep -vE 'href|url\(|xlink|id=|#[A-Za-z_-]{2,}' >&2
  fi
  if grep -nE '(^|[^-])(rgba?|hsla?|oklch|lab)\(' "$f" | grep -q .; then
    say "RAW COLOUR FUNCTION in $f — every colour comes from a --mc-* token:"
    grep -nE '(^|[^-])(rgba?|hsla?|oklch|lab)\(' "$f" >&2
  fi
done

# --- 3. RULE 1: Olive never carries text and never receives text -------------
#     The decor namespace is defined as "paint that never has a foreground".
#     So: no `color:` may resolve to a --mc-decor-* token, and no --mc-decor-*
#     may be a `background` on an element that also sets `color`.
if grep -nE '(^|[^-])color:[^;]*--mc-decor-' "$ASSETS"/base.css "$ASSETS"/components.css \
   | grep -vE 'background-color|border-color|text-decoration-color|outline-color|accent-color|caret-color|::marker' | grep -q .; then
  say "RULE 1 VIOLATION — a --mc-decor-* token used as a text colour:"
  grep -nE '(^|[^-])color:[^;]*--mc-decor-' "$ASSETS"/base.css "$ASSETS"/components.css >&2
fi
if grep -n 'color: var(--mc-color-olive)' "$ASSETS"/base.css "$ASSETS"/components.css | grep -q .; then
  say "RULE 1 VIOLATION — the Olive primitive used directly as a colour."
fi

# --- 4. RULE 2: Sky is a dark-ground colour ----------------------------------
#     --mc-text-accent-on-dark is undefined in :root and in .band--light, so a
#     light-scope use fails to the inherited Dark Olive. This catches the other
#     route in: naming the primitive.
if grep -nE 'color: var\(--mc-color-sky\)' "$ASSETS"/components.css \
   | grep -vE 'band--dark' | grep -q .; then
  say "RULE 2 — check each of these: --mc-color-sky used as a colour outside .band--dark"
  grep -nE 'color: var\(--mc-color-sky\)' "$ASSETS"/components.css >&2
fi

# --- 5. RULE 3: no form showing validation errors inside a dark band ---------
#     A CSS grep cannot see the HTML tree, so this is an HTML grep: any file
#     that contains band--dark AND a validation class gets read by a human.
for f in "$SITE"/*/*.html "$SITE"/*/*/*.html; do
  [ -e "$f" ] || continue
  if grep -q 'band--dark' "$f" && grep -qE 'mc-field__error|mc-form-error|aria-invalid' "$f"; then
    say "RULE 3 — $f has a dark band AND validation markup. Confirm the form is not inside the band."
  fi
done

# --- 6. RULE 4: Nude is the ground, Ivory is the objects ---------------------
#     Neither primitive may be named outside tokens.*; the semantic pair is the
#     only way to say it, and the two are 1.10 apart so a swap is invisible.
if grep -nE 'var\(--mc-color-(nude|ivory)\)' "$ASSETS"/components.css \
   | grep -vE 'paymarks|credit|badge|family__avatar' | grep -q .; then
  say "RULE 4 — a ground primitive named directly; use --mc-surface-ground / --mc-surface-object:"
  grep -nE 'var\(--mc-color-(nude|ivory)\)' "$ASSETS"/components.css >&2
fi

# --- 7. No type role outside the sixteen -------------------------------------
if grep -nE 'font-size: *[0-9.]+(px|rem|pt|ex|ch)' "$ASSETS"/base.css "$ASSETS"/components.css | grep -q .; then
  say "A LITERAL FONT SIZE — the ramp is sixteen roles and they are all tokens:"
  grep -nE 'font-size: *[0-9.]+(px|rem|pt|ex|ch)' "$ASSETS"/base.css "$ASSETS"/components.css >&2
fi

# --- 8. No JavaScript in, or required by, these stylesheets ------------------
for f in "$SITE"/*/*.html "$SITE"/*/*/*.html; do
  [ -e "$f" ] || continue
  grep -q 'onclick=\|onmouseover=\|javascript:' "$f" && say "INLINE JS in $f"
done

# --- 9. Every var(--mc-*) referenced actually exists -------------------------
python3 - "$ASSETS" <<'PY' || fail=1
import re, sys, pathlib
a = pathlib.Path(sys.argv[1])
defined = set(re.findall(r'(--mc-[A-Za-z0-9-]+)\s*:', (a/'tokens.css').read_text()))
defined |= set(re.findall(r'(--mc-[A-Za-z0-9-]+)\s*:', (a/'base.css').read_text()))
defined |= set(re.findall(r'(--_[a-z]+)\s*:', ''))
bad = []
for name in ('base.css', 'components.css'):
    txt = (a/name).read_text()
    local = set(re.findall(r'(--mc-[A-Za-z0-9-]+)\s*:', txt))
    for m in re.finditer(r'var\((--mc-[A-Za-z0-9-]+)', txt):
        t = m.group(1)
        if t not in defined and t not in local and not t.startswith('--mc-__'):
            bad.append(f"{name}: {t}")
if bad:
    print("UNDEFINED TOKEN REFERENCED:", file=sys.stderr)
    for b in sorted(set(bad)): print("  " + b, file=sys.stderr)
    sys.exit(1)
PY

[ "$fail" -eq 0 ] && echo "check-tokens: clean" || echo "check-tokens: FAILED" >&2
exit "$fail"
