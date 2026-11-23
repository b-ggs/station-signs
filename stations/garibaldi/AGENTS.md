# Garibaldi bus stop

- **City, country:** Nice, France
- **Visited:** August 2026, after Prague and Paris
- **System and spec:** Lignes d’Azur. Uses “Design spec: Nice Lignes d’Azur: bus shelter
  header” at the end of this file. This is the bus shelter header, not the nearby tram sign.
- **Routes on the sign:** 15, 33, 57, and `33s` (lowercase as printed).
- **Neighbors:** Port Lympia / Arson and Lycée Masséna on
  [line 15](https://nice-transports.fr/lignes/bus-15-nice) toward Lycée Masséna.

## References and decisions

- `Screenshot 2026-11-23 at 8.31.54 AM.png`: sharper oblique photo, rectified for layout.
- `Screenshot 2026-11-23 at 8.33.15 AM.png`: brighter photo used for the sky blue, white
  face, title ink, and route colors. Neither screenshot is stored in the repo.
- `Screenshot 2026-11-24 at 6.54.53 AM.png` (not tracked): the sharper close-up used to
  redraw GARIBALDI. The source corners are (34, 178), (846, 104), (877, 393), and
  (23, 420), clockwise from upper left. The user chose the photo-traced title over the
  existing Helvetica Neue and DIN Alternate and Barlow Medium alternatives.
- For the new palette, sample each tile and the adjacent white panel in the color-managed,
  rectified photo. Dividing each tile channel by the neighboring white in linear RGB
  gave `#58cbc8`, `#00665f`, `#093b7f`, and `#118a50`. The previous shadowed photo gives
  similar values after correction; the brighter photo washes out the colors. The user
  chose variant 8, which blends 43% of the corrected values with 57% of the previous palette
  in sRGB. These are visual estimates, not official line values.
- The user chose navy `#263c61` for GARIBALDI based on the first photo, then asked to make
  NICE the same navy. Variant 8 uses 108% horizontal scale for NICE, down from 116%.
- In the tile-width comparison, the user chose variant 2: 15 narrows from 160 to 152 pt
  from the fixed left edge, and 33s widens from 140 to 148 pt around its center.
- All route labels are 83 pt at baseline 346, at natural width, including `33s`.
  The logo uses the colors and editable paths from
  [Lignes dAzur logo 2010.svg](https://fr.wikipedia.org/wiki/Fichier:Lignes_dAzur_logo_2010.svg).
- Only the printed sign face is modeled; no shelter, metal frame, glare, or weathering.

## Compact version

`garibaldi-compact.vectorcraft` (1147 × 390) is a copy of the full sign with the blank areas
trimmed. The Lignes d’Azur logo moves left to x 944, 60 pt past the end of the traced
GARIBALDI (x 884), keeping its 18 pt right margin. The user chose 60 pt over 30 and 100.
The bottom is cut 30 pt below the route tiles, matching their 30 pt left margin. The white
face and sky-blue strip are resized to fit. The compact sign matches the full sign’s
lettering, route colors, and tile widths.

## Design spec: Nice Lignes d’Azur: bus shelter header

First pass for the Garibaldi panel, revised against the newer rectified photo. The original
typeface and exact inks are not confirmed. Coordinates are in pt.

- **Face:** white `#ffffff`, 1600 × 500, with a full-width sky-blue `#a0d0f8` strip from
  y 0 to 62. Leave the large blank area to the right of the title and route tiles.
- **Text:** Both labels are navy `#263c61`. NICE is Helvetica Neue Regular 47 at 108%
  horizontal scale, x 19, baseline 48. GARIBALDI is hand-traced as nine vector paths,
  with visible bounds approximately x 29–884 and y 101–229.
- **Route tiles:** plain filled rectangles in one row at y 272, 88 high, with centered
  white Arial Rounded MT Bold labels. From left to right: 15 at x 30, width 152,
  `#8fd8cf`; 33 at x 290, width 150, `#387b6e`; 57 at x 533, width 145, `#2c4484`;
  and 33s at x 767, width 148, `#589f73`.
- **Logo:** orange and yellow two-line Lignes d’Azur wordmark at the upper right,
  crossing the strip and white face. The photo does not show a contrasting logo panel.
