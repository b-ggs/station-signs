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
- Route rectangles, left to right: 15 at x 30, width 160, mint `#b8e1d5`; 33 at x 290,
  width 150, muted teal `#638b7a`; 57 at x 533, width 145, indigo `#464b88`; 33s at
  x 771, width 140, muted green `#8eaf8e` (chosen by the user over the original sage and
  two other greens). The other tile colors are estimates from the blurred bright photo,
  not official line values.
- The user chose navy `#263c61` for GARIBALDI based on the first photo; NICE stays dark gray.
- All route labels are 83 pt at baseline 346, at natural width, including `33s`.
  The logo uses the colors and editable paths from
  [Lignes dAzur logo 2010.svg](https://fr.wikipedia.org/wiki/Fichier:Lignes_dAzur_logo_2010.svg).
- Only the printed sign face is modeled; no shelter, metal frame, glare, or weathering.

## Compact version

`garibaldi-compact.vectorcraft` (1161 × 390) is a copy of the full sign with the blank areas
trimmed. The Lignes d’Azur logo moves left to x 958, 60 pt past the end of GARIBALDI (about
x 898), keeping its 18 pt right margin. The user chose 60 pt over 30 and 100. The bottom is
cut 30 pt below the route tiles, matching their 30 pt left margin. The white face and sky-blue
strip are resized to the new width and height. Everything else is identical to the full sign,
so carry over any changes made there.

## Design spec: Nice Lignes d’Azur: bus shelter header

First pass for the Garibaldi panel. Use the sharper, rectified photo for geometry and the
brighter photo for the palette; the bright photo is too soft to determine exact inks.
Coordinates are in pt.

- **Face:** white `#ffffff`, 1600 × 500, with a full-width sky-blue `#a0d0f8` strip from
  y 0 to 62. Leave the large blank area to the right of the title and route tiles.
- **Text:** NICE is dark gray `#56565f`, Helvetica Neue Regular 47 at 116% horizontal
  scale, x 19, baseline 48. The stop name is navy `#263c61`, Helvetica Neue Medium 178
  at 92.75%, x 26, baseline 225. Both styles stand in for the photographed lettering.
- **Route tiles:** plain filled rectangles in one row at y 272, 88 high, with centered
  white Arial Rounded MT Bold labels. Use the station's notes for tile colors and widths.
- **Logo:** orange and yellow two-line Lignes d’Azur wordmark at the upper right,
  crossing the strip and white face. The photo does not show a contrasting logo panel.
