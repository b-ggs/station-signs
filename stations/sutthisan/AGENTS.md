# Sutthisan station

- **City, country:** Bangkok, Thailand
- **Visited:** March 2024 with Rodj
- **System and spec:** Bangkok MRT. Uses “Design spec: Bangkok MRT entrance sign” below.
- **Names:** Sutthisan (English), สุทธิสาร (Thai)
- **Line and code:** Blue Line, **BL17**
- **Neighbors:** Ratchadaphisek (BL16) and Huai Khwang (BL18)
- **Sign:** Exit 4, serving Soi Ratchadaphisek 17, Sutthisan Winitchai Road, and
  Thanachart Building per [BEM's station page](https://metro.bemplc.co.th/Line-Maps?Line=1&Station=17&lang=en).

## References and decisions

- `Screenshot 2026-11-24 at 1.19.24 AM.png` (user attachment, not tracked): an oblique view
  of the printed sign. The photo was straightened with a quadrilateral warp using the estimated
  corners (44, 53), (1396, 146), (1400, 289), and (39, 214), clockwise from top left.
  The normalized dimensions are an estimate, not a measurement of the physical sign.
- Only the printed sign face is reproduced, not the structure around it. The palette compensates
  for the dim lighting and is not an official color specification.
- The MRT emblem is an editable vector redraw from the sign photo. The MRTA and BEM marks
  were revised from the user's separate logo references: the MRTA chevron image and
  `Screenshot 2026-11-24 at 1.23.48 AM.png` for BEM (not tracked). The BEM caption is
  approximated with editable type. The smallest badge lettering is approximate because it
  is blurry in the sign photo.
- In the comparison, the user chose variant 3's neutral gray and variant 6's 12 pt upward
  shift for both names. The final sign also centers the names horizontally rather than
  following the photo's slight right offset, uses equal end panels, and squares the exit
  badge. In the badge color comparison, the user chose variant 3's deep navy (`#0c2040`)
  over the main panel blue and the lighter and darker navy alternatives.

## Design spec: Bangkok MRT entrance sign

First pass based on the Sutthisan Blue Line Exit 4 sign. Confirm this layout against other exits
and lines before applying it system-wide. Dimensions are in points.

- **Face:** 1400 × 168, with matching 177 pt neutral gray end panels (`#b6b8b8`).
  The navy center (`#153365`) spans x 177–1223.
- **Station name:** Both lines are centered at x 700. Thai is Thonburi Regular 47,
  baseline y 84, in off-white (`#f4f4ed`). English is Arial Bold 34 with −12 tracking,
  baseline y 134, in gold (`#f5be49`).
- **Left panel:** The flat-bottom MRT roundel (`#173660`) is x 38–141, y 10–94, with an
  off-white M and navy MRT lettering below. The interlaced deep blue (`#101c69`) and
  red (`#ff0000`) MRTA chevrons sit above the รฟม. label in the same deep blue. The
  connected BEM wordmark and its Avenir Next Demi Bold caption match the MRT roundel's
  blue (`#173660`) at the user's request. Both marks are near the bottom of the panel.
- **Right panel:** Station code in Arial Bold 35, navy (`#18294c`), centered at x 1311.5
  with baseline y 44. The exit badge is x 1269.5, y 63, 84 × 84, with a 4 pt off-white
  rim and a deep navy inset (`#0c2040`). The white numeral is Arial Bold 55, with smaller
  white Thai and gold English captions underneath.

### Compact version

The compact face is 720 × 168. It keeps both 177 pt end panels and trims 340 pt of blue
space on either side of the station names. The blue panel is x 177–543, the names are
centered at x 360, and the right panel's code and badge are centered at x 631.5. The
artwork sizes, colors, and vertical positions are unchanged.
