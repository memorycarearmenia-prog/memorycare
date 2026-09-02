#!/usr/bin/env python3
"""
Computes every text-on-background pair this system can produce, from the hex
values in ../tokens.source.json. Nothing here is copied from a brief.

    python3 tools/check-contrast.py            # table to stdout
    python3 tools/check-contrast.py --md       # the body of CONTRAST.md
    python3 tools/check-contrast.py --assert   # exit 1 if a shipped pair fails

WCAG 2.1 relative luminance and contrast ratio, sRGB, no rounding until the
last step. Thresholds: 4.5 body text, 3.0 large text (>=24px, or >=18.66px
bold) and meaningful non-text graphics, no floor for disabled controls.
"""
import json, pathlib, sys, re

SRC = json.loads((pathlib.Path(__file__).parent.parent / "tokens.source.json")
                 .read_text(encoding="utf-8"))

HEX = {}
ALPHA = {}
for g in SRC["groups"]:
    for t in g["tokens"]:
        v = str(t["value"])
        if v.startswith("#"):
            HEX[t["name"]] = v
        m = re.match(r"rgb\((\d+) (\d+) (\d+) / ([\d.]+)\)", v)
        if m:
            r, gg, b, a = int(m[1]), int(m[2]), int(m[3]), float(m[4])
            ALPHA[t["name"]] = ("#%02X%02X%02X" % (r, gg, b), a)


def _lin(c):
    c /= 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def lum(h):
    h = h.lstrip("#")
    return (0.2126 * _lin(int(h[0:2], 16))
            + 0.7152 * _lin(int(h[2:4], 16))
            + 0.0722 * _lin(int(h[4:6], 16)))


def ratio(fg, bg):
    a, b = lum(fg), lum(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def flatten(fg, alpha, bg):
    fg, bg = fg.lstrip("#"), bg.lstrip("#")
    return "#" + "".join("%02X" % round(int(fg[i:i+2], 16) * alpha
                                        + int(bg[i:i+2], 16) * (1 - alpha))
                         for i in (0, 2, 4))


def resolve(name, ground):
    """A token name -> the opaque colour it actually paints on `ground`."""
    if name in HEX:
        return HEX[name]
    if name in ALPHA:
        base, a = ALPHA[name]
        return flatten(base, a, ground)
    raise KeyError(name)


# ---- the pairs the system can actually produce -----------------------------
# (scope, where the text sits, the token that paints it, the ground token,
#  threshold, note)
PAIRS = [
 # ---------------- light scope, on the page ground (Nude) -------------------
 ("light", "page",        "text-primary",   "color-nude",  4.5, "Body copy, every heading."),
 ("light", "page",        "text-secondary", "color-nude",  4.5, "Metadata, captions, helper text."),
 ("light", "page",        "text-accent",    "color-nude",  4.5, "Links and accent text."),
 ("light", "page",        "text-link",      "color-nude",  4.5, "Same value; underlined as well as coloured."),
 ("light", "page",        "text-link-hover","color-nude",  4.5, "Hover goes darker, not lighter."),
 ("light", "page",        "text-error",     "color-nude",  4.5, "Validation message outside a card."),
 ("light", "page",        "text-muted",     "color-nude",  0.0, "DISABLED labels only. 1.4.3 exempts inactive controls."),
 ("light", "page",        "border-control", "color-nude",  3.0, "Input boundary. Non-text, 1.4.11."),
 ("light", "page",        "border-focus",   "color-nude",  3.0, "Focus ring. Non-text, 1.4.11."),
 ("light", "page",        "decor-olive-rule","color-nude", 3.0, "A divider that carries meaning."),
 # ---------------- light scope, on an object (Ivory) ------------------------
 ("light", "object",      "text-primary",   "color-ivory", 4.5, "Card and report-sheet copy."),
 ("light", "object",      "text-secondary", "color-ivory", 4.5, ""),
 ("light", "object",      "text-accent",    "color-ivory", 4.5, ""),
 ("light", "object",      "text-link-hover","color-ivory", 4.5, ""),
 ("light", "object",      "text-error",     "color-ivory", 4.5, "Field-level error inside a form card."),
 ("light", "object",      "text-muted",     "color-ivory", 0.0, "Disabled only."),
 ("light", "object",      "border-control", "color-ivory", 3.0, "Input boundary, the usual case."),
 ("light", "object",      "border-focus",   "color-ivory", 3.0, ""),
 ("light", "object",      "decor-olive-rule","color-ivory",3.0, "The rule inside a tariff card."),
 # ---------------- light scope, filled and tinted areas ---------------------
 ("light", "primary btn", "text-on-action",  "color-dark-olive", 4.5, "Ivory label on the Dark Olive fill."),
 ("light", "primary btn hover", "text-on-action", "color-deep-olive", 4.5, "The fill lightens on hover; the label must still hold."),
 ("light", "sky chip",    "text-primary",    "color-sky", 4.5, "Dark Olive on the Sky TINT. This is the only way Sky appears on a light page."),
 ("light", "sky chip",    "border-focus",    "color-sky", 3.0, "The ring survives on a Sky-tinted chip."),
 ("light", "error panel", "text-primary",    "wash-error@color-ivory", 4.5, "The error-summary panel's own copy."),
 ("light", "error panel", "text-error",      "wash-error@color-ivory", 4.5, "The red heading on its own wash."),
 ("light", "well",        "text-primary",    "ink-a08@color-ivory", 4.5, "Striped table row, calculator readout."),
 # ---------------- dark band ------------------------------------------------
 ("dark",  "band",        "color-nude",   "color-dark-olive", 4.5, "text-primary in the dark scope."),
 ("dark",  "band",        "color-ivory",  "color-dark-olive", 4.5, "text-secondary in the dark scope."),
 ("dark",  "band",        "color-sky",    "color-dark-olive", 4.5, "text-accent and text-link. THIS is Sky's job."),
 ("dark",  "band",        "paper-a48",    "color-dark-olive", 0.0, "text-muted, disabled only."),
 ("dark",  "band",        "paper-a48",    "color-dark-olive", 3.0, "border-control, as a non-text boundary."),
 ("dark",  "band",        "color-sky",    "color-dark-olive", 3.0, "border-focus, as a non-text ring."),
 ("dark",  "band",        "color-olive",  "color-dark-olive", 3.0, "decor-olive-rule on dark. Graphic only."),
 ("dark",  "raised card", "color-nude",   "paper-a06@color-dark-olive", 4.5, "Copy on the raised card in the band."),
 ("dark",  "raised card", "color-sky",    "paper-a06@color-dark-olive", 4.5, ""),
 ("dark",  "primary btn", "color-dark-olive", "color-nude", 4.5, "Dark Olive label on the Nude fill."),
 ("dark",  "primary btn hover", "color-dark-olive", "color-ivory", 4.5, ""),
]

# Pairs the system must NEVER produce. Listed so the failure is on the record
# and so the structural prevention has something to point at.
FORBIDDEN = [
 ("color-olive",      "color-nude",       "Rule 1. Olive as text on the page."),
 ("color-olive",      "color-ivory",      "Rule 1. Olive as text on a card."),
 ("color-olive",      "color-dark-olive", "Rule 1. Olive as text in the dark band — clears AA-large only, which is why the wordmark is allowed to be art and body text is not."),
 ("color-olive",      "color-sky",        "Rule 1. Olive as text on a Sky chip."),
 ("color-dark-olive", "color-olive",      "Rule 1 again, from the other side: Olive never RECEIVES text either."),
 ("color-ivory",      "color-olive",      "Rule 1. A light label on an Olive fill."),
 ("color-sky",        "color-nude",       "Rule 2. Sky as type on the page ground."),
 ("color-sky",        "color-ivory",      "Rule 2. Sky as type on a card."),
 ("color-error",      "color-dark-olive", "Rule 3. A validation message inside a dark band."),
 ("color-deep-olive", "color-dark-olive", "Deep Olive is a light-ground colour only."),
 ("color-nude",       "color-ivory",      "Rule 4. Ground colour used as an object, or the reverse — the two are 1.10 apart and invisible against each other."),
]


def paint(token, ground_token):
    """Resolve `token@ground` composites written into the table above."""
    if "@" in ground_token:
        over, base = ground_token.split("@")
        ground = resolve(over, HEX[base])
    else:
        ground = HEX[ground_token]
    return resolve(token, ground), ground


def rows():
    for scope, where, fg, bg, thr, note in PAIRS:
        fgh, bgh = paint(fg, bg)
        r = ratio(fgh, bgh)
        ok = r >= thr if thr else None
        yield scope, where, fg, bg, fgh, bgh, r, thr, ok, note


def main():
    md = "--md" in sys.argv
    fails = []
    for scope, where, fg, bg, fgh, bgh, r, thr, ok, note in rows():
        if ok is False:
            fails.append((fg, bg, r, thr))
        if md:
            v = "—" if thr == 0 else ("pass" if ok else "**FAIL**")
            print(f"| {scope} | {where} | `{fg}` {fgh} | `{bg}` {bgh} | "
                  f"**{r:.2f}** | {thr or 'n/a'} | {v} | {note} |")
        else:
            print(f"{scope:5s} {where:16s} {fg:18s} on {bg:22s} "
                  f"{r:6.2f}  need {thr or '-'}  {'ok' if ok is not False else 'FAIL'}")
    if md:
        print()
        for fg, bg, why in FORBIDDEN:
            print(f"| `{fg}` {HEX[fg]} | `{bg}` {HEX[bg]} | "
                  f"**{ratio(HEX[fg], HEX[bg]):.2f}** | {why} |")
    if "--assert" in sys.argv:
        if fails:
            for fg, bg, r, thr in fails:
                print(f"FAIL {fg} on {bg}: {r:.2f} < {thr}", file=sys.stderr)
            sys.exit(1)
        print("all shipped pairs clear their threshold", file=sys.stderr)


if __name__ == "__main__":
    main()
