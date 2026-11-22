# Phrom Phong (E5)

- **City, country:** Bangkok, Thailand
- **Visited:** April 2026
- **Rail system and spec:** Bangkok BTS Skytrain. Its layout, sizes and colors are in the root
  `AGENTS.md` under "Bangkok BTS Skytrain: platform sign". This file covers only what's specific
  to Phrom Phong.

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
  brighter yellow. The full palette is in the root `AGENTS.md`.

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
