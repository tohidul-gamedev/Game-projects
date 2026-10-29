#!/usr/bin/env bash
set -euo pipefail
if [[ $# != 2 ]]; then
  echo 'Usage: bash tools/finalize-shirt.sh composed-585x559.png final.png' >&2
  exit 2
fi
script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
pack_dir=$(dirname -- "$script_dir")
size=$(magick identify -format '%wx%h' "$1")
if [[ "$size" != 585x559 ]]; then
  echo 'Input must already be exactly585x559. Assemble the UV faces first.' >&2
  exit 2
fi
magick "$1" -colorspace sRGB -font DejaVu-Sans-Bold -pointsize 29 -fill '#161616' -stroke none -draw "text 40,210 '2.94'" "$pack_dir/03-shirt-alpha-mask.png" -alpha off -compose CopyOpacity -composite -depth 8 -define png:color-type=6 -strip "$2"
echo "Wrote $2. Run tools/validate_png.py and inspect the native layout."
