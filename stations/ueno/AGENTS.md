# Ueno (JY05)

- **City, country:** Tokyo, Japan
- **Visited:** March 2026
- **Rail system and spec:** JR East, the Yamanote Line. Its layout, sizes and colors are in the
  root `AGENTS.md` under "JR East: station name sign (駅名標), Yamanote Line". This file covers
  only what's specific to Ueno.

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
  the badges (UEN Bold, JY SemiBold, numbers Bold). The full reasoning and rejected options are
  in the root spec.
- The neighbor names on the band (御徒町, 鶯谷) are Hiragino W5, not W7 (decided).
- In the badges, "05" sits 4 pt lower and "06" 2 pt higher than first measured (decided after
  comparing 2/1, 4/2 and 6/3 pt).
- Okachimachi's left ink edge is aligned with 御徒町's, both at x 67.25 (at the user's request).
  Re-measure at 4× if either font or weight changes.
- A second reference: JR East's official mockup of the Shinjuku (JY17) sign from its station
  numbering announcement. It was used **only** for the badge lettering (three weights). Don't
  take colors from it.
