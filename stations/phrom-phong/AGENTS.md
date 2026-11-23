# Phrom Phong (E5)

- **City, country:** Bangkok, Thailand
- **Visited:** April 2026
- **Rail system and spec:** Bangkok BTS Skytrain. The shared BTS layout, sizes and colors are
  under "Design spec: Bangkok BTS Skytrain: platform sign" at the end of this file. The sections
  before it cover only what's specific to Phrom Phong.

## Station facts

- **Line:** Sukhumvit Line (สายสุขุมวิท), line color green
- **Station:** พร้อมพงษ์ / Phrom Phong, code **E5**
- **Neighbors:** E6 ทองหล่อ / Thong Lo, and E4 อโศก / Asok

## The sign

`phrom-phong.vectorcraft` holds a single sign, the **Platform 2** sign. Its platform panel is on
the left. The previous station is E6 Thong Lo (left), and the next station is E4 Asok (right),
so the route strip points right.

## Reference photos

These came as chat attachments and aren't stored in the repo.
- A Platform 2 sign photographed at an angle. It shows the layout and the platform panel. The
  darker top navy in it is shadow.
- Victory Monument, Platform 1, photographed straight on. All the measurements in the shared
  spec come from this one.

## Decisions and open questions

- Colors (decided): navy `#2d3a5e` for every blue element, green `#6baa51`, E5 yellow
  `#f2d237`, chevrons `#e5d377`. The user mixed these from the photo-matched set and the
  white-balanced Victory Monument photo, with the yellows lightened to 75% of the way toward the
  brighter yellow. The full palette is in the design spec below.

- Thai font: Thonburi Regular plus a 1 pt same-color outline (decided after comparing 1, 1.5
  and 2 pt).
- All text on navy is white (decided).
- Arrow and chevron borders: 3.5 pt white, kept after comparing 1.5, 2.5, 4, 4.5, 6 and 7.5 pt.
- The platform number "2" sits 4 pt above the circle's center, as an optical correction (decided
  after comparing 0, 4, 8 and 12 pt).
- Station circle rings: 6 pt white (decided after comparing 5, 6, 7 and 8 pt).
- English font: Helvetica Neue Bold (decided after comparing Tahoma Bold and Thonburi Bold).
- The arrowhead matches the chevrons' angle. The gaps from the arrowhead to chevron 1 and from
  chevron 1 to chevron 2 are both 14 pt, measured horizontally. Gaps of 8 pt (too close) and
  20 pt were also tried.

## Design spec: Bangkok BTS Skytrain: platform sign

These measurements come from a straight-on reference photo (Victory Monument, Platform 1),
scaled so the sign is 420 pt tall. All values are in pt. Each station's `AGENTS.md` supplies the
text and station codes.

- **Overall:** 1620 × 420. The platform panel is 320 wide, on the side of the platform it
  serves (for example, left for Phrom Phong Platform 2 and right for Victory Monument
  Platform 1). The main sign is 1300 wide, about 3.1 times its height. Its center (x = 970 when
  the panel is on the left, 650 when it's on the right) is the axis for the station name and
  route strip.
- **Bands:** navy 0–256 (61% of the height), then the line color 256–420. Any darker navy in
  photos is shadow.
- **Palette** (decided by the user after comparing several sets; no official BTS spec exists
  online):

  | Role | Color | Source |
  |---|---|---|
  | Navy, used for **every** blue element | `#2d3a5e` | matched to photos; a white-balanced photo gave nearly the same value |
  | Sukhumvit Line green | `#6baa51` | Victory Monument photo, white-balanced |
  | Current-station yellow | `#f2d237` | the photo yellow's hue, lightened 75% of the way toward `#f5d90a` (in OKLab) |
  | Chevrons | `#e5d377` | the same treatment as the yellow |
  | Platform panel | `#ffffff` | white, at the user's request (it was off-white `#efeee6` before) |
  | Panel divider | `#a5a49c` | |

  Other lines need their own line color, so ask the user. Rejected options include the BTS
  website's `#273e83` / `#358300`, the route map's `#8db63c` and Wikipedia's `#76b729`.
- **Typefaces:**
  - Thai is **Thonburi Regular** with a **1 pt outline in the text's own color**, which brings it
    about a third of the way to Bold. Set it with
    `text.setStyle {stroke: <fill color>, strokeWidth: 1}`. It's the same 1 pt at every size, not
    scaled. Thonburi has no adjustable weight, so this outline stands in for one. The real BTS
    typeface is undocumented.
  - Latin is **Helvetica Neue Bold**, chosen by the user over Tahoma Bold and Thonburi Bold.
- **One blue:** every blue element uses the same color, as the navy band does. That covers the
  station circles, the route bar, the platform circle, the platform text (ชานชาลา and "Platform")
  and the code label on the yellow circle. The user asked for this. Thai text in navy also gets a
  navy outline.
- **Text colors:** all text on navy *and* on the line color is pure white `#ffffff`, both Thai and
  English. That includes the previous and next station names. Don't use cream or off-white
  anywhere, including the platform panel and its number. The only non-white text is the navy
  platform text on the white panel and the navy code label on the yellow circle.
- **Main sign text** (x is measured from the main sign's left edge):

  | Element | Size | Position (baseline) |
  |---|---|---|
  | Line name, Thai (สายสุขุมวิท) | 50 | left 31, baseline 55 |
  | Line name, English ("Sukhumvit Line") | 49 | right-aligned to the same ink edge as the next-station name, baseline 57 |
  | Station name, Thai | 108 (matched on letter height; Thonburi's marks are tall) | centered, baseline 144 |
  | Station name, English | 81 | centered, baseline 232 |
  | Previous and next station, Thai | 38 | left 28 or right 27, baseline 324 (both sides) |
  | Previous and next station, English | 37 | same, baseline 371 (both sides) |

- **Route strip** (center line y = 337):
  - The current station is a yellow `#f2d237` circle with a **6 pt** white ring, centered on the
    main axis. The circle is drawn 75 across, so it measures 81 including the ring. All three
    station circles use the 6 pt ring, chosen over 5, 7 and 8 pt.
  - The previous station is a navy `#2d3a5e` circle, 80 across, about 205 from the axis.
  - The next station (the direction of travel) is a larger navy circle, about 101 across, about
    214 from the axis.
  - A navy bar 39 tall (y 317.5–356.5) with a **3.5 pt** white outline runs from the previous
    station to an arrowhead. The 3.5 pt was confirmed against 1.5–7.5 pt. It's deliberately
    thinner than the 6 pt station rings: thicker borders eat into the narrow chevrons.
  - Two pale chevrons `#e5d377` have the same 3.5 pt white outline. Each is 39 tall and 30 wide,
    with 14 of solid thickness and a 16 deep notch.
  - The arrowhead has the same angle as the chevrons: each edge runs 16 across for 19.5 down.
    There's one even rhythm: **14 pt** (measured horizontally) from the arrowhead to chevron 1, and
    14 pt from chevron 1 to chevron 2. The user rejected 8 pt (too close) and 20 pt.
  - Positions are measured from the axis toward the next station. Chevron 1's back corners are
    at +90 and chevron 2's at +118, so chevron 2's tip sits at +148. The arrowhead's corners are
    at +76 and its tip at +92.
  - (Phrom Phong values, with the axis at 970: arrowhead corners at 1046 and tip at 1062,
    chevrons at 1060 and 1088.)
  - Change only what the user asks for. Don't move neighboring elements, such as the chevrons,
    to make room.
  - The route strip points toward the next station. On a sign where the next station is on the
    left, mirror it.
  - Station code labels are 34 pt, or 40 pt in the next-station circle.
- **Platform panel:** white `#ffffff`, with a 2 pt gray divider `#a5a49c` and navy ink `#2d3a5e`.
  - ชานชาลา at 78 pt, centered, baseline 63
  - a circle 210 across, centered at y 207, with the number at 210 pt in white `#ffffff`. The number is
    centered horizontally by its ink, and **sits 4 pt above true center** (baseline 278, leaving
    26 pt of space above the digit and 35 pt below). That optical correction was chosen over
    exact centering and over 8 or 12 pt up. Measure the ink after placing a different digit, since
    each number's shape differs.
  - "Platform" at 57 pt, centered, baseline 395

Still open for BTS signs: the metal frame and production format.
