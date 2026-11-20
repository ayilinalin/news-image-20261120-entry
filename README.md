# Front Page — Friday 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/ayilinalin/news-image-20261120-entry/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/ayilinalin/news-image-20261120-entry/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

Entry for the [make.fun](https://make.fun) bounty
[`news-image-20261120`](https://make.fun/bounty/news-image-20261120):
one image summing up the world news of **Friday 20 November 2026**.

## The image

A newspaper front page — banner date, headline, four stories:

| Story | Panel |
| --- | --- |
| Russia's overnight blitz hits Kyiv — 100+ missiles, 3 bridges down, power out | Headline + damaged bridge at night |
| Shenzhen peace declaration — Trump, Xi, Putin: no breakthrough on Ukraine | US, China and Russia flags over Shenzhen |
| GTA VI — record $2.36B day one, ~24.6M copies (Sensor Tower estimate) | Neon Vice City street, $2.36B sign |
| Anthropic IPO — shares soar 34%, ~$2T valuation | Rising stock chart + AI chip |

The date **FRIDAY 20 NOVEMBER 2026** is printed large at the top and
again in the footer, so the day the image sums up is unmistakable.

## How it runs

`main.py` (Python 3.13, standard library only, no network) copies the
image baked into this repository to `$MAKEFUN_OUTPUT_DIR/entry.png`.
It self-checks the PNG magic, the 1 MiB size cap and the 1024×1024
dimension cap, and writes the output with mode `0644`.
It is deterministic: two runs write byte-identical output.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Output: `entry.png` — 1024×1024 PNG, 875,375 bytes (under the 1 MiB cap).

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
