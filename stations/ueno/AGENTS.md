# Ueno (JY05)

- **City, country:** Tokyo, Japan
- **Visited:** March 2026
- **Rail system and spec:** JR East, the Yamanote Line. The shared JR East layout, sizes and
  colors are under "Design spec: JR East: station name sign (駅名標)" at the end of this file.
  [Akihabara](../akihabara/AGENTS.md) uses the same spec, so keep it general and record
  Akihabara's decisions there too when they apply to both. The sections before it cover only
  what's specific to Ueno.

## Station facts

- **Line:** JR Yamanote Line, code JY. The three-letter station code is **UEN**.
- **Station:** 上野 (うえの) / Ueno, Korean 우에노, number **JY05**
- **Neighbors:** JY04 御徒町 / Okachimachi, and JY06 鶯谷 / Uguisudani
- **Fare zones:** 山 (Yamanote-line area) and 区 (Tokyo wards area)

## The sign

`ueno.vectorcraft` holds a single sign: the station name sign facing the platform for trains
toward Uguisudani. Okachimachi is on the left and Uguisudani on the right, so the route band
points right.

## Reference photos

This came as a chat attachment and isn't stored in the repo.
- The Ueno JY05 sign, photographed from below at a slight angle. Its keystone was corrected
  using the face's corners, and its height set so the square numbering badges come out square.
  All the measurements in the shared spec come from this photo.

## Decisions and open questions

- Text was placed by comparing ink boxes against the corrected photo. Most elements are within
  about 2 pt.
- Open: the palette (`#156419` band, `#80c241` line color) is a first pass from the photo, so
  the user should review it.
- Fonts (decided 2026-11-23, after rounds of variants): Hiragino Sans W7 for Japanese, Helvetica
  Neue for English (Bold "Ueno", Regular neighbors, condensed to the photo's width), and Hind for
  the badges (UEN Bold, JY and numbers SemiBold). The full reasoning and rejected options are
  in the design spec below.
- The neighbor names on the band (御徒町, 鶯谷) are Hiragino W5, not W7 (decided).
- Badges: the 40/60 layout from the shared spec, decided on the Akihabara sign and applied
  here. It replaced the earlier 05/06 nudges.
- Okachimachi's left ink edge is aligned with 御徒町's, both at x 67.25 (at the user's request).
  Re-measure at 4× if either font or weight changes.
- A second reference: JR East's official mockup of the Shinjuku (JY17) sign from its station
  numbering announcement. It was used **only** for the badge lettering (three weights). Don't
  take colors from it.

## Design spec: JR East: station name sign (駅名標)

Used by Ueno (Yamanote Line, JY) and Akihabara (Chūō–Sōbu Line, JB).

These measurements come from a reference photo of the Ueno JY05 sign, taken from below. Its
keystone was corrected using the sign's corners, and its height set so the square numbering
badges (JY05 and JY06) come out square. That makes the sign **1600 × 425** (about 3.75:1). All
values are in pt.

**Every JR East sign uses 1600 × 425**, even where the real sign is a different length.
Akihabara's real sign is about 5:1, and the user chose to keep these proportions so the set
matches. Element sizes stay the same; only the spacing of the station name changes (see
"Station name block"). Each station's `AGENTS.md` supplies the text and station codes.

- **Overall:** a white face `#ffffff`, 1600 × 425, with no frame yet. The main axis, which the
  kanji pair, kana, English name and current-station block center on, is x = 795 (measured, not
  exactly the middle).
- **Route band:** y 242–330 (88 tall; the photo measured 87). It runs from the left edge to
  x 1470, then an arrowhead points at the next station, with its tip at (1557, 286). The current
  station is a line-color block, x 753–834, the full band height. Mirror the band when the next
  station is on the left. Keep the band's top and bottom on **even** y values. At 87 tall, the
  bottom edge fell on a half pixel in the 0.5× preview PNG, which left a faint row and a visible
  step where it met the arrowhead.
- **Palette** (first pass, matched from the photo. The user hasn't reviewed it yet):

  | Role | Color | Source |
  |---|---|---|
  | Route band, dark green | `#156419` | photo, white-balanced (the photo's white was 229) |
  | Line color (current-station block, badge borders): Yamanote (JY) | `#80c241` | between the photo's block and badge greens; close to the commonly cited Yamanote green |
  | Line color: Chūō–Sōbu (JB) | `#f5e119` | midpoint of the Akihabara photo's raw yellow `#ebee32` and the commonly cited `#ffd400` |
  | Ink | `#1a1a1a` | near-black |

- **Typefaces** (stand-ins, chosen by the user after comparing variants). A type researcher's
  survey of Kanto railway signage gives JR East's real fonts as **Shin Go B** for Japanese,
  **Helvetica Bold** for English and **Frutiger Bold** for station numbers. A JR East post on X
  backs up the Helvetica/Frutiger split. Shin Go and Frutiger are commercial fonts and aren't
  installed.
  - Japanese is **Hiragino Sans W7**, closer to Shin Go B than W6. Two exceptions use W5: the
    small kanji next to the main name, and the previous and next station names on the band. W5
    matches the photo's 4 pt stems on 御徒町; W7, W4 and W3 were compared.
  - English is **Helvetica Neue**. The station name is Bold. The neighbor names are **Regular**:
    the photo's stems measure about 4 pt on the neighbors against 8 pt on "Ueno". Long names are
    condensed with horizontal scale (`text.setFormat {hScale}`) to the photo's width. Don't use
    tracking for this, because tightening the spacing crowds the letters.
  - Badge text is **Hind** (`brew install --cask font-hind`, then `text.rescanFonts`), standing in
    for Frutiger. It uses three weights, as JR East's official numbering mockup does: the
    three-letter code in **Bold**, and the line letters ("JY", "JB") and the number in
    **SemiBold**. Rejected: Seravek (its J drops below the baseline), Source Sans 3 (shapes off, even
    with an outline added), Istok Web, Avenir Next, PT Sans, Helvetica Neue, and Hind with "JY"
    in Regular or Medium (too light).
  - Korean is **Apple SD Gothic Neo Regular**.
- **Station name block:**

  | Element | Font, size | Position (baseline) |
  |---|---|---|
  | 上 / 野 (one object per kanji) | W7, 131 | centered at x 665.5 and 919, baseline 135 |
  | Kana (うえの) | W7, 44, tracking 400 | centered on the axis, baseline 210.5 |
  | Chinese name, simplified (上野, 秋叶原) | W5, 40 | left 1042 on Ueno, baseline 67 |
  | Korean (우에노) | Apple SD Gothic Neo, 36, tracking 250 | left 1042, baseline 133 |
  | English name ("Ueno") | Helvetica Neue Bold, 60 | centered on the axis, baseline 398 |

  The small line next to the name is the **Chinese** name in simplified characters. On Ueno it
  happens to match the Japanese (上野), but Akihabara's is 秋叶原.

  For a three-kanji name, space the kanji 165 apart, centered on the axis (秋葉原: x 630, 795,
  960). Keep the photo's gaps: 66 from the badge's right edge to the first kanji's ink, and about
  68 from the last kanji's ink to the Chinese and Korean names. Tune the kana's tracking per
  station (400 for うえの, 45 for あきはばら).

- **Numbering badge (JY05):** a black `#1a1a1a` rounded rectangle at x 388, y 27.5, 155 × 185,
  radius 16. Inside it is a line-color square at (400, 71), 131 × 131, radius 8, with a white
  square inset 10 (radius 2). The three-letter code "UEN" is Hind Bold 45 in white, centered at
  x 465.5, baseline 64. Below it, the line letters and number split the white square's height
  **40/60**, each filling its zone with 7 pt of white above, between and below. "JY" is Hind
  SemiBold 50.8 at baseline 121.9 (ink 34 tall), and "05" is Hind SemiBold 84.1 at baseline 185
  (ink 56 tall), both centered at x 465.5. Chosen over the earlier small "JY" with a Bold
  number, a 45/55 split, and 40/60 with 10 pt margins.
  Earlier, the user compared this badge with geometry scaled from Wikimedia's JR numbering artwork
  (JY17, JB26): a thicker 13 pt frame, rounder corners, sharp white corners, and larger letters
  over a smaller number. They kept the current badge.
- **Fare-zone marks** (top right): 山 (Yamanote-line area) is an outlined box. It has a white fill
  with a 5 pt black stroke, outer edge x 1370–1441 and y 20–88, radius 5, and a black W7 52 山
  centered at x 1405.5, baseline 74. 区 (Tokyo wards area) is solid: a black box at x 1461–1532,
  y 20–88, radius 7, with a white W7 52 区 centered at x 1496.5, baseline 74. Which marks appear
  depends on the station.
- **Neighbors:**

  | Element | Font, size | Position (baseline) |
  |---|---|---|
  | Previous station, Japanese (white, on the band) | W5, 52, tracking 125 | left 66, baseline 310 |
  | Next station, Japanese (white, on the band) | W5, 72, tracking 250 | centered at x 1313, baseline 314 |
  | Previous station, English | Helvetica Neue Regular, 50, hScale fitted (96.5% for Okachimachi) | **left ink edge aligned with the Japanese name's left ink edge** (measure it at 4× and nudge), baseline 397 |
  | Next station, English | Helvetica Neue Regular, 52, hScale fitted (96% for Uguisudani) | right-aligned at 1411, baseline 397 |

  The next station's number badge sits after its English name. It's a white rounded square,
  x 1431.5–1498.5 and y 344.5–410.5, with a 5 pt line-color stroke and radius 5. Inside it is
  the same 40/60 split, scaled to the smaller box: "JY" is Hind SemiBold 27.9 at baseline 369.45
  and "06" is Hind SemiBold 46.2 at baseline 404.15, both centered at x 1465. The previous station has no badge on this sign.

The route band is JR East's dark green on **every** line. The Akihabara (JB) sign confirms it,
so only the current-station block and the badge borders take the line color.

Still open for JR East signs: the palette review and the frame.
