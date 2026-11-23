# Akihabara (JB19)

- **City, country:** Tokyo, Japan
- **Visited:** September 2026
- **Rail system and spec:** JR East. It uses the spec "Design spec: JR East: station name sign
  (駅名標)" in [Ueno's `AGENTS.md`](../ueno/AGENTS.md) (fonts, sizes, badge, band), with the
  Chūō–Sōbu Line's yellow as the line color. Read it before working on this sign, and record
  decisions that apply to both signs there. This file covers only what's specific to Akihabara.

## Station facts

- **Line:** JR Chūō–Sōbu Line (local), code JB. The three-letter station code is **AKB**.
- **Station:** 秋葉原 (あきはばら) / Akihabara. The Chinese name is 秋叶原 (simplified), and the
  Korean is 아키하바라. Number **JB19**.
- **Neighbors:** JB20 浅草橋 / Asakusabashi, and JB18 御茶ノ水 / Ochanomizu
- **Fare zones:** 山 (Yamanote-line area) and 区 (Tokyo wards area)

## The sign

`akihabara.vectorcraft` holds a single sign: the station name sign for trains toward
Ochanomizu. Asakusabashi is on the left and Ochanomizu on the right, so the route band points
right. It started as a copy of the Ueno file.

## Reference photos

These came as chat attachments and aren't stored in the repo.
- The JB19 sign, photographed nearly straight on, but at low resolution (about 4 pt per photo
  pixel after correction). The positions specific to Akihabara come from it.
- A close-up from below at a steep angle. It shows the badge and lettering only.

## Decisions and open questions

- **Proportions (decided by the user):** the real Akihabara sign is about 5:1 (2128 × 425 at
  the spec's height; the square badges confirm it). It uses Ueno's 1600 × 425 anyway, so the set
  stays consistent.
- **Layout at 1600 × 425:** everything Ueno has is in Ueno's positions. The three kanji are
  Hiragino W7 131, centered at x 630, 795 and 960 (165 apart). The badge keeps the photo's
  66 pt gap to 秋, so it's at x 351–506. The small Chinese name and the Korean are left-aligned
  at x 1088, keeping the photo's gap after 原.
- Tracking: あきはばら 45, 秋叶原 100, 아키하바라 250 (as on Ueno).
- English widths fitted to the photo: Asakusabashi hScale 96%, Ochanomizu 94%. Asakusabashi's
  left ink edge is aligned with 浅草橋's, at x 68.5.
- 御茶ノ水 (W5 72, no tracking) is centered at x 1255.75, so its right ink edge (1397.5) sits just
  inside Ochanomizu's (1407.5), as 鶯谷 does on Ueno.
- Open: the yellow `#f5e119` is a first pass. It's the midpoint of the photo's raw block color
  `#ebee32` (white-balancing clips it to `#ffff39`) and the commonly cited Chūō–Sōbu yellow
  `#ffd400`.
- Badges: "JB" and the number now split the white square 40/60 (both Hind SemiBold, 7 pt
  margins). It was decided here after comparing 45/55 and roomier margins, and applied to Ueno
  too. Details are in the JR East spec in Ueno's `AGENTS.md`.
