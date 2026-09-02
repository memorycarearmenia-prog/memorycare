#!/usr/bin/env python3
"""
MemoryCare token build.

    python3 build-tokens.py            # writes tokens.css and tokens.json
    python3 build-tokens.py --check    # exits 1 if either file is out of date

tokens.source.json is the only file anyone edits. tokens.css and tokens.json
are both emitted here, in one pass, from the same in-memory objects, so they
cannot drift: there is no second place where a value is written down. The
fluid type ramp is arithmetic performed here, not two hand-kept copies of the
same clamp(). CI runs --check; a hand-edit of a generated file fails the build.
"""
import json, sys, pathlib, re

HERE = pathlib.Path(__file__).parent
SRC  = HERE / "tokens.source.json"
PFX  = "mc"

src   = json.loads(SRC.read_text(encoding="utf-8"))
meta  = src["$meta"]
VMIN, VMAX = meta["fluid_range_px"]
ROOT_PX    = meta["root_font_px"]


def alias(value):
    """{token-name} -> var(--mc-token-name). Unknown names stay unknown on
    purpose: that is how the guard tokens fail."""
    return re.sub(r"\{([^}]+)\}", lambda m: f"var(--{PFX}-{m.group(1)})", str(value))


def rem(px):
    v = round(px / ROOT_PX, 4)
    return f"{v:g}rem"


def fluid(lo, hi):
    """clamp() between the two viewport ends declared in $meta."""
    if lo == hi:
        return rem(lo)
    slope = (hi - lo) / (VMAX - VMIN)
    vw    = round(slope * 100, 4)
    base  = round((lo - slope * VMIN) / ROOT_PX, 4)
    return f"clamp({rem(lo)}, {base:g}rem + {vw:g}vw, {rem(hi)})"


def wrap(text, prefix, width=78):
    """Reflow a source comment as CSS comment body lines, each already
    carrying `prefix`."""
    out, line = [], ""
    for w in text.split():
        if len(line) + len(w) + 1 > width - len(prefix):
            out.append(line); line = w
        else:
            line = f"{line} {w}".strip()
    if line:
        out.append(line)
    return "\n".join(prefix + l for l in out)


# ---------------------------------------------------------------- CSS ------
css = [
    "/* GENERATED FILE — DO NOT EDIT.",
    " * Source: tokens.source.json  ·  Generator: build-tokens.py",
    f" * {meta['name']} v{meta['version']} — {meta['date']}",
    " *",
    wrap(meta["palette_rule"], " * "),
    " *",
    " * Every ratio quoted below was computed by tools/check-contrast.py from the",
    " * hex values in this file. CONTRAST.md is that script's output.",
    " */",
    "",
    "/* Layer order is declared HERE, in the first stylesheet the page loads,",
    " * because a later @layer statement cannot reorder layers that already",
    " * exist. Load order is fixed: tokens.css, base.css, components.css. */",
    "@layer mc.reset, mc.tokens, mc.base, mc.components, mc.utilities;",
    "",
    "@layer mc.tokens {",
]

root_groups = [g for g in src["groups"] if g["scope"] == "root"]
dark_groups = [g for g in src["groups"] if g["scope"] == "band-dark"]


def emit(groups, selector, note=None):
    css.append(f"  {selector} {{")
    if note:
        css.append(f"    /* {note} */")
    for g in groups:
        css.append("")
        css.append(f"    /* ---------------------------------------------------------------")
        css.append(f"       {g['title']}")
        if g.get("comment"):
            css.append(wrap(g["comment"], "       "))
        css.append(f"       --------------------------------------------------------------- */")
        for t in g["tokens"]:
            if t.get("comment"):
                css.append(f"    /* {t['comment']} */")
            css.append(f"    --{PFX}-{t['name']}: {alias(t['value'])};")
    return


emit(root_groups, ":root", "LIGHT SCOPE — the default page.")

# type roles, generated into the same :root block
css.append("")
css.append("    /* ---------------------------------------------------------------")
css.append("       TYPE — sixteen roles, four tokens each. Sizes are clamp()")
css.append(f"       between {VMIN}px and {VMAX}px viewport, computed by the generator.")
css.append("       --------------------------------------------------------------- */")
for r in src["type"]["roles"]:
    css.append(f"    /* {r['name']}: {r['use']} */")
    css.append(f"    --{PFX}-type-{r['name']}-size: {fluid(r['min'], r['max'])};")
    css.append(f"    --{PFX}-type-{r['name']}-leading: {r['leading']};")
    css.append(f"    --{PFX}-type-{r['name']}-tracking: {r['tracking']};")
    css.append(f"    --{PFX}-type-{r['name']}-weight: {r['weight']};")
    css.append(f"    --{PFX}-type-{r['name']}-family: var(--{PFX}-font-{r['family']});")
    css.append(f"    --{PFX}-type-{r['name']}-case: {r['case']};")
css.append("  }")

css.append("")
css.append("  /* =================================================================")
css.append("     .band--dark — the two sections that flip.")
css.append("     Not a dark theme: no media query, no toggle, no persistence.")
css.append("     ================================================================= */")
emit(dark_groups, ".band--dark")
css.append("  }")

css.append("""
  /* .band--light — the explicit way back.
     Custom properties inherit, so a light region nested inside .band--dark
     would otherwise keep the dark scope's values, including a Sky text token
     that measures 1.26 once the ground turns pale. This class restores the
     light scope AND re-arms the two guards in the other direction. */
  .band--light {
    color-scheme: light;""")
for g in root_groups:
    if g["id"] in ("surface", "text", "border", "decor"):
        for t in g["tokens"]:
            if t["name"].startswith(("border-width",)):
                continue
            css.append(f"    --{PFX}-{t['name']}: {alias(t['value'])};")
css.append("""    /* Sky is not type on a light ground — rule 2. Re-pointed at a name that
       does not exist, so `color` falls back to the inherited Dark Olive. */
    --mc-text-accent-on-dark: var(--mc-__SKY-BLUE-IS-1-POINT-2-6-ON-NUDE--USE-text-accent-OR-decor-sky-tint);
  }

  /* The Sky-as-type token exists in exactly one scope. */
  .band--dark { --mc-text-accent-on-dark: var(--mc-color-sky); }
  :root       { --mc-text-accent-on-dark: var(--mc-__SKY-BLUE-IS-1-POINT-2-6-ON-NUDE--USE-text-accent-OR-decor-sky-tint); }
}""")

CSS_TEXT = "\n".join(css) + "\n"


# --------------------------------------------------------------- JSON ------
out = {
    "$schema": "https://design-tokens.org/schema.json",
    "$description": (
        "GENERATED FILE — DO NOT EDIT. Source: tokens.source.json, generator: "
        "build-tokens.py. This file and tokens.css are written in a single run "
        "from the same parsed objects, so a value cannot exist in one and not "
        "the other. `python3 build-tokens.py --check` fails CI if either is "
        "stale. Aliases use DTCG {curly} references; the CSS emitter turns the "
        "same string into var(--mc-…). Guard tokens beginning `__` are "
        "deliberately never defined — see $description on each."
    ),
    "$meta": meta,
}
for g in src["groups"]:
    bucket = out.setdefault("band-dark" if g["scope"] == "band-dark" else g["layer"], {})
    grp = bucket.setdefault(g["id"], {"$description": g["title"]})
    if g.get("comment"):
        grp["$description"] += " " + g["comment"]
    for t in g["tokens"]:
        entry = {"$value": t["value"], "$type": t.get("type", "other"),
                 "$extensions": {"mc.css": f"--{PFX}-{t['name']}", "mc.scope": g["scope"]}}
        if t.get("comment"):
            entry["$description"] = t["comment"]
        grp[t["name"]] = entry

typ = out.setdefault("semantic", {}).setdefault("type", {"$description": src["type"]["comment"]})
for r in src["type"]["roles"]:
    typ[r["name"]] = {
        "$type": "typography",
        "$description": r["use"],
        "$value": {
            "fontSize": fluid(r["min"], r["max"]),
            "fontSizeMinPx": r["min"], "fontSizeMaxPx": r["max"],
            "lineHeight": r["leading"], "letterSpacing": r["tracking"],
            "fontWeight": r["weight"], "fontFamily": "{font-" + r["family"] + "}",
            "textTransform": r["case"],
        },
        "$extensions": {"mc.css": f"--{PFX}-type-{r['name']}-*", "mc.scope": "root"},
    }

JSON_TEXT = json.dumps(out, indent=2, ensure_ascii=False) + "\n"

WANT = {HERE / "tokens.css": CSS_TEXT, HERE / "tokens.json": JSON_TEXT}

if "--check" in sys.argv:
    stale = [p.name for p, want in WANT.items()
             if not p.exists() or p.read_text(encoding="utf-8") != want]
    if stale:
        print("STALE (hand-edited, or the source changed without a rebuild): "
              + ", ".join(stale), file=sys.stderr)
        print("Run: python3 build-tokens.py", file=sys.stderr)
        sys.exit(1)
    print("tokens.css and tokens.json are in sync with tokens.source.json")
    sys.exit(0)

for p, want in WANT.items():
    p.write_text(want, encoding="utf-8")
print(f"wrote tokens.css and tokens.json  ({len(src['type']['roles'])} type roles)")
