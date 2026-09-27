#!/usr/bin/env bash
# Download third-party inputs for the pilot into <workdir> (not committed).
# Usage: ./fetch_inputs.sh <workdir>
set -euo pipefail
W="${1:?workdir}"; UA="Mozilla/5.0"
mkdir -p "$W"/{A,B,C}/{blind/figures,reference}
# medRxiv v1 JATS XML (version-specific) and figures F1..Fn
fetch_medrxiv() { local c=$1 date=$2 id=$3 n=$4
  curl -sL -A "$UA" -o "$W/$c/blind/preprint_v1.xml" "https://www.medrxiv.org/content/early/$date/$id.source.xml"
  for i in $(seq 1 "$n"); do curl -sL -A "$UA" -o "$W/$c/blind/figures/F$i.jpg" "https://www.medrxiv.org/content/medrxiv/early/$date/$id/F$i.large.jpg"; sleep 3; done; }
fetch_medrxiv A 2025/06/25 2025.06.24.25330216 20
fetch_medrxiv B 2025/07/21 2025.07.19.25331823 8
curl -sL -A "$UA" -o "$W/C/blind/preprint_v1.pdf" "https://www.researchsquare.com/article/rs-7394486/v1.pdf"
# Peer Review Files (Nature supplementary information)
curl -sL -o "$W/A/reference/prf.pdf" "https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-026-10627-z/MediaObjects/41586_2026_10627_MOESM6_ESM.pdf"
curl -sL -o "$W/B/reference/prf.pdf" "https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-026-10274-4/MediaObjects/41586_2026_10274_MOESM4_ESM.pdf"
curl -sL -o "$W/C/reference/prf.pdf" "https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-026-10341-w/MediaObjects/41586_2026_10341_MOESM2_ESM.pdf"
echo "Done. Convert XML to text before review (see protocol.md)."
