# The World Today — 23 November 2026 in one image

[![make.fun bounty](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/c/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/MrCoinw/makefun-news-image-20261123/rank.svg)](https://make.fun/c/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/MrCoinw/makefun-news-image-20261123/reward.svg)](https://make.fun/c/news-image-20261123)

Entry for the [make.fun](https://make.fun) bounty **"Sum up
23 November's world news in one image"**
([news-image-20261123](https://make.fun/c/news-image-20261123)),
by @welly-g, built with his AI agent in a session started after
the competition opened.

## What the image shows

One newspaper front page, dated **Monday, 23 November 2026** in large
type at the top, summing up that day:

- **Main story:** Trump, Putin & Xi meet in Shenzhen — the leaders
  issue a "Declaration toward Peace" on Ukraine.
- COP31 climate talks collapse.
- AI sell-off shakes markets.
- U.S.–Iran tension flares at Hormuz.
- Drones hit Kyiv homes.
- GTA VI breaks sales records.

The six stories span politics, climate, markets, energy, war and
culture, and every headline is printed in the image itself so a
viewer who missed the day can read what happened from the image
alone.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies
the bundled `entry.png` to `/output/entry.png`, byte for byte, and
checks the copy is complete. Run it twice and both runs write the
same bytes (sha256 `ba876207…b38f0` for the current image).

For a local dry run, `MAKEFUN_OUTPUT_DIR=<folder>` redirects the
output away from `/output`.

## Image gate

- PNG, 1024 × 1024 pixels
- 465,433 bytes — under the 1 MiB (1,048,576 byte) limit

## License

MIT — see `LICENSE`.
