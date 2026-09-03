#!/usr/bin/env bash
# Rebuild the handover archive from the repository. Everything it copies is
# generated or committed, so the archive is reproducible and never the
# authority — the repository is.
set -euo pipefail
cd "$(dirname "$0")/.."
OUT="${1:-/tmp/MemoryCare-Handover-$(date +%F)}"

rm -rf "$OUT"
mkdir -p "$OUT"/{01-site,01-site-generators,02-screenshots,03-design-system/tools,04-content,05-documents,07-figma}

cp -r rebrand/site/* "$OUT/01-site/"
rm -rf "$OUT/01-site/_includes"
cp rebrand/site/_includes/*.py rebrand/site/_includes/*.html "$OUT/01-site-generators/"

if compgen -G 'rebrand/render/screens/*.png' > /dev/null; then
  cp rebrand/render/screens/*.png "$OUT/02-screenshots/"
else
  echo "note: no screenshots on disk — run rebrand/render/shoot.py first" >&2
fi
cp rebrand/render/manifest.json rebrand/render/capture-log.json rebrand/render/shoot.py "$OUT/02-screenshots/"

cp rebrand/site/assets/tokens.source.json rebrand/site/assets/tokens.css \
   rebrand/site/assets/tokens.json rebrand/site/assets/build-tokens.py \
   rebrand/site/assets/SYSTEM.md rebrand/site/assets/CONTRAST.md "$OUT/03-design-system/"
cp rebrand/site/assets/tools/* "$OUT/03-design-system/tools/"

cp rebrand/strings/*.json rebrand/strings/*.md "$OUT/04-content/"

cp rebrand/BRIEF.md rebrand/DECISIONS.md rebrand/LEGAL-FACTS.md \
   rebrand/DATA-CONTRACT.md rebrand/COMPLIANCE.md \
   rebrand/site/assets/fonts/FONTS.md "$OUT/05-documents/"

cp rebrand/render/extract.py rebrand/render/pack-for-figma.py "$OUT/07-figma/"
cp rebrand/FIGMA.md "$OUT/07-figma/README.md"

cp rebrand/HANDOVER-README.md "$OUT/README.md"
cp rebrand/OPEN-QUESTIONS.md "$OUT/06-OPEN-QUESTIONS.md"

echo "$OUT"
find "$OUT" -type f | wc -l | sed 's/^/files: /'
du -sh "$OUT" | cut -f1 | sed 's/^/size:  /'
