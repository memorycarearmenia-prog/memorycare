#!/usr/bin/env python3
"""
RULE 3, checked against the actual document tree.

    python3 tools/check-dark-forms.py <file.html> [more.html ...]
    python3 tools/check-dark-forms.py --glob <site-root>

"No form showing validation errors may sit in a dark band." Error red measures
2.12 on Dark Olive — invisible. The token guards in tokens.css already make the
message fall back to a readable colour, and components.css draws a dashed
outline so it shows in a screenshot; this is the check that fails the build.

WHY THIS EXISTS: the first version of this rule was a whole-file substring grep
in check-tokens.sh. It fired on any page containing both `band--dark` and
validation markup ANYWHERE, in any relationship — including inside a comment.
An engineer tripped it on the home page and had to reword a comment that merely
contained the string `mc-form-error`. A check that cries wolf gets muted, and a
muted check is worse than none.

This parses the HTML and maintains the open-element stack, so it reports a
violation only when validation markup is genuinely a DESCENDANT of an element
carrying `band--dark` — with `band--light` correctly cancelling it, because
that is exactly what `band--light` does in the cascade. Comments are ignored by
the parser, so a comment can say anything it likes.
"""
import sys, glob, pathlib
from html.parser import HTMLParser

# Markup that means "this element can show a validation error to a user".
VALIDATION_CLASSES = {"mc-form-error", "mc-field__error", "mc-toast--error",
                      "mc-badge--error", "mc-empty--error"}
VALIDATION_ATTRS = {"aria-invalid"}

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "source", "track", "wbr"}


class DarkBandScanner(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.stack = []          # [(tag, scope) …]  scope: 'dark' | 'light' | None
        self.hits = []

    # --- the inherited scope at this point in the tree -----------------------
    def _scope(self):
        for _tag, scope in reversed(self.stack):
            if scope:
                return scope
        return "light"

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = set((a.get("class") or "").split())
        scope = ("dark" if "band--dark" in classes else
                 "light" if "band--light" in classes else None)

        inherited = self._scope()
        effective = scope or inherited

        is_validation = bool(classes & VALIDATION_CLASSES) or any(
            k in VALIDATION_ATTRS and (v or "").lower() not in ("", "false")
            for k, v in a.items())

        if is_validation and effective == "dark":
            cls = sorted(classes & VALIDATION_CLASSES)
            att = sorted(k for k in a if k in VALIDATION_ATTRS)
            what = (f'class="{" ".join(cls)}"' if cls else "") + \
                   (" " if cls and att else "") + \
                   (" ".join(f'{k}="{a[k]}"' for k in att) if att else "")
            self.hits.append((self.getpos()[0], tag, what))

        if tag not in VOID and not self.get_starttag_text().endswith("/>"):
            self.stack.append((tag, scope))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                return


def scan(path):
    p = DarkBandScanner(path)
    p.feed(pathlib.Path(path).read_text(encoding="utf-8", errors="replace"))
    return p.hits


def main(argv):
    if "--glob" in argv:
        root = argv[argv.index("--glob") + 1]
        files = sorted(glob.glob(f"{root}/**/*.html", recursive=True))
    else:
        files = [a for a in argv[1:] if a.endswith(".html")]

    bad = 0
    for f in files:
        for line, tag, what in scan(f):
            bad += 1
            print(f"{f}:{line}: RULE 3 — <{tag} {what}> is inside a "
                  f"band--dark. Error red is 2.12 on Dark Olive: invisible. "
                  f"Move the form out of the band, or wrap it in band--light.",
                  file=sys.stderr)
    if bad:
        print(f"check-dark-forms: {bad} violation(s) in {len(files)} file(s)",
              file=sys.stderr)
        return 1
    print(f"check-dark-forms: clean ({len(files)} file(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
