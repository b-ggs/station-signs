# Artis tram stop

- **City, country:** Amsterdam, Netherlands
- **Visited:** August 2025, with David
- **System and spec:** GVB (Amsterdam tram and bus). Uses "Design spec: GVB: stop flag" at the
  end of this file.
- **Stop:** Artis/Nationaal Holocaustmuseum, on Plantage Middenlaan, next to the Artis zoo. The
  stop was formerly just "Artis". It was renamed after the National Holocaust Museum opened
  nearby in 2024. A Stolperstein (stumbling stone) was placed at the stop, tied to GVB
  acknowledging the trams' role in the WWII deportations
  ([nieuws.nl](https://nieuws.nl/algemeen/gedenktekens-en-100-000-euro-om-betaalde-tramritten-joden),
  [IamExpat](https://www.iamexpat.nl/lifestyle/lifestyle-news/stumbling-block-placed-amsterdam-tram-stop-holocaust-memorial-day)).
- **Lines on the sign:** tram 14 and night bus N87 (the night line is in a black box).
- **Zone:** 5700, probably the stop's fare zone from the old national zone system, which applied
  to strip tickets. Not confirmed by a source.

## References and decisions

- `Screenshot 2026-11-23 at 10.15.40 PM.png` (not in the repo) is the user's own photo, taken in
  August 2025. It shows the renamed stop with a two-line, left-aligned name, white graffiti on the
  blue column, and a crinkled plastic sleeve over the lower panel. The colors were sampled from
  this photo and white-balanced so that the panel comes out white.
- `Screenshot 2026-11-23 at 10.17.41 PM.png` (not in the repo) is an older Google Street View
  image showing the pre-rename "Artis" sign, with a centered name. It is used only for the
  geometry: the panel proportions, the rule grid, and the positions of the pictograms and line
  numbers.
- The user chose the renamed version, as they saw it.
- The small text under each line number is unreadable in both images. The user wanted the side
  toward the Red Light District, which is the westbound stop, so both lines read
  "Centraal Station". This is inferred, not read from a photo.
- The recreation leaves out the graffiti, the plastic sleeve, the wear, and the tiny unreadable
  text at the bottom right. A white mark at the bottom of the blue column, possibly the GVB logo,
  is also left out for now.
- Helvetica Neue is a stand-in typeface.
- The bus and tram pictograms were traced by hand from a clear photo, supplied by the user, of
  a Dutch round blue bus-and-tram traffic sign that uses the same pictograms. The photo was
  used for their shapes only, not for any colors. On the stop sign they're black on white.

## Compact version

`artis-compact.vectorcraft` (400 × 334) is a copy of the full sign, cut off 31 pt below the
rules under "Centraal Station" at y 303, which matches the full sign's margin below its last rule.
Only the two occupied rule rows (y 224 and 303) are kept, and the blue column and line panel are
shortened to the new bottom edge. Everything above y 303 is identical to the full sign, so
carry over any changes made there.

## Design spec: GVB: stop flag

First pass at the older GVB stop flag (haltevlag), with the zone box and the blue column.
Coordinates are in pt.

- **Face:** 400 × 650, with no outer border.
- **Colors:** blue `#526eba`, yellow `#ffd968`, white `#ffffff` panels, ink `#1a1a1a` to
  `#3a3a3a`. Blue and yellow are white-balanced estimates from a dim photo.
- **Header:** a blue band from y 0 to 122. It holds two white pictogram boxes, each 175 × 84 at
  y 20, at x 18 (bus) and x 207 (tram). The pictograms are the standard Dutch bus and tram
  side views, facing left, traced at 0.19 pt per pixel of the 7× reference crop. Each has large
  white windows in thin black frames over a solid black lower body.
  - **Bus:** from x 37.6 to 174 and y 32 to 92. It has a raked windshield and a vertical front
    face below it. The windshield window reaches lower than the side windows. There are five
    side windows, with the rear one narrower. The rear-bottom corner is cut at an angle. Two
    wheels 19 across sit at x 68.7 and 139.4, each in a white wheel arch 25.8 across.
  - **Tram:** from x 224.5 to 363.6, with its roof at y 55 and its body at y 91. Both ends are
    raked. It has seven windows: small front and back windows, with five equal windows between
    them. A 1.9 pt outlined diamond pantograph (47 × 28) sits at x 269 and rests on the roof.
    The body's bottom edge rises 2.9 pt into a notch, with small rounded corners, over each
    bogie. Each bogie has two wheels 11 across with flat tops at y 91.2, just below the notch,
    at x 246.7, 264.0, 324.6, and 341.7. The wheels were enlarged inward from the outer edges of
    each pair, chosen from variants. A 1.3 pt bar along the flat tops joins the two wheels of
    each bogie, as on the street signs.
- **Left column:** 124 wide. The yellow zone box runs from y 122 to 224, with "zone" (Helvetica
  Neue Bold 23) and the zone number (Bold 34) left-aligned at x 24, on baselines 150 and 194.
  "zone" is about two thirds as wide as the number, which nearly fills the box's width. Below it, the blue column runs to the bottom.
- **Line panel:** white, from x 124 to 400 and y 122 to the bottom. The stop name is set left at
  x 128 in Helvetica Neue Bold 26, `#3a3a3a`, on baselines 181 and 208. Its width matches the
  photo. A short name like the older "Artis" was centered
  on the panel.
- **Line slots:** two columns of blue 1.5 pt rules, from x 130 to 247 and from x 263 to 380, at
  y 224, then every 79 down to 619. Line numbers sit in the slot under the first rule, at
  x 134 and x 263. A day line is set in Helvetica Neue Medium 44, on baseline 275. A night
  line is set in white Bold 48.5, centered at x 309 on baseline 273.4, in a `#1e1e1e` box
  92 × 40 at (263, 236). The text fills the box almost to its edges, with about 1 pt of
  padding at the sides and 3 pt at the top and bottom. The destination is 8 pt regular, on baseline 293.
