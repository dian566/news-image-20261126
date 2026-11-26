# The World in One Page — 26 November 2026

[![News Image 26](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![Rank](https://make.fun/badge/news-image-20261126/dian566/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![Reward](https://make.fun/badge/news-image-20261126/dian566/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126)

One image that sums up the world's news of **Thursday, 26 November 2026**,
built for the [News Image 26](https://make.fun/bounty/news-image-20261126)
bounty on make.fun.

## The image

`news.png` is a newspaper front page, 1024 by 1024 pixels: a masthead naming
the day, six stories across regions and beats, and an "also today" strip.
Every story was first reported on 26 November 2026.

- **Space** — Pakistan's first astronaut reaches Tiangong: Muhammad Zeeshan
  Ali boards China's space station aboard Shenzhou-24, the first foreign
  astronaut ever to fly on a Chinese mission.
- **Gulf shipping** — two tankers hit mines in the Strait of Hormuz: Iran
  says an LNG carrier and an oil tanker struck mines and caught fire on an
  unauthorised route.
- **Saudi Arabia** — Houthis hit a refinery after a Riyadh attack: Yemen's
  Houthis say they struck Ras Tanura, the kingdom's largest refinery, after
  a strike on a Riyadh tower injured 11 people.
- **Trade** — the US is set to unveil new tariffs on 16 economies, including
  China, the EU and Japan; Asian tech shares slide.
- **Ukraine war** — Russia's own figures show nearly 500,000 dead: Moscow's
  statistics, analysed by the BBC, put Russian soldiers killed since 2022 at
  about 490,000.
- **Americas** — Colombia police free 20 hostages after a 17-hour supermarket
  siege in Cartagena.

Also today: Bangladesh raises garment wages 36%; Australia and Solomon
Islands sign a security treaty; Huawei is found guilty in a New York trial;
India marks Constitution Day, 18 years after the 26/11 Mumbai attacks;
Gukesh plays on at the World Chess Championship.

## How it runs

`main.py` (Python 3.13, standard library only) validates `news.png` — PNG
signature, dimensions, every chunk's CRC — and copies it to
`$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`). It touches no
network and writes the same bytes on every run:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
