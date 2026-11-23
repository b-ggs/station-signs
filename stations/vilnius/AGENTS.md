# Vilnius railway station

- **City, country:** Vilnius, Lithuania
- **Visited:** August 2025 with David
- **System and spec:** Lithuanian Railways (LTG). Uses “Design spec: LTG station facade sign”
  below.
- **Names:** Vilnius railway station (English), Vilniaus geležinkelio stotis (Lithuanian).
- **Sign:** The front facade has the LTG / Lietuvos geležinkeliai lockup above
  **GELEŽINKELIO STOTIS**, which means “Railway Station” and is not the station's name.

## References and decisions

- `Screenshot 2026-11-24 at 5.57.08 AM.png` (user attachment, not tracked): the oblique
  facade reference. The logo and lower lettering were leveled separately. Photo corners
  in upper-left, lower-left, lower-right, upper-right order were (402,53), (401,148),
  (964,159), (964,65) for the logo and (75,298), (75,413), (1300,451), (1300,333) for the
  lower crop.
- [Augustas Didžgalvis's facade photo](https://commons.wikimedia.org/wiki/File:Vln_Bahnhof_by_Augustas_Didzgalvis.jpg)
  confirms the station and placement. The
  [digital LTG lockup reference](https://en.wikipedia.org/wiki/File:LTG_Lithuania_logo.png)
  was used to redraw the logo geometry, not to set its colors.
- The logo plaques, lower lettering, and slatted backing are reproduced without the rest of
  the facade. The slat material isn't clear in the photo. The user chose a small offset
  letter shadow instead of an outline. The logo and lettering share a center line.
- In the final comparison, the user chose the 20 pt gap from the logo to the top of the
  **Ž** accent over gaps of 28, 36, and 44 pt.
- The user chose palette variant 9: silver-white lettering, slate slats, and a stone-gray
  background. The letters' color was estimated by comparing the photographed letter faces
  with the nominally white LTG monogram to account for the blue cast. The first slat palette
  was sampled from the photo (`#959eac` faces, `#bbc2d1` edges, `#030c18` gaps); variant 9
  uses less contrast between slat edges and gaps so the lettering stands out.

## Font research

- [LTG's website stylesheet](https://ltg.lt/wp-content/themes/ltg/dist/theme.css) specifies
  **Euclid Circular A**, Regular and Semibold, from [Swiss Typefaces](https://www.swisstypefaces.com/fonts/euclid/).
  This confirms the web typography, not a specification for the facade. Euclid Circular A's
  **S** has horizontal terminals; the facade **S** has angled terminals. The facade also
  has broader **E** and **Ž** relative to their heights.
- **Montserrat Bold** was a close editable stand-in among the faces compared, especially in
  **E**, **N**, and **S**, but its **O** is wider and the **Ž** accent differs. The original
  typeface for the physical sign remains unconfirmed. The lower letters are individual,
  hand-drawn vector paths based on the reference, so there is no font dependency.

## Design spec: LTG station facade sign

First pass for this Vilnius installation, not a system-wide signage standard. Coordinates
are in points.

- **Artboard:** 1260 × 265, filled with a building-inspired stone gray (`#7d8894`).
  Both elements are centered at x 630.
- **Lockup:** 565 wide, approximately 94 high, at x 347.5, y 24. The opposing points of
  the two plaques nearly meet. Dark plaque `#111a26`, red plaque `#a82736`, lettering
  `#f7fbff`. These are visual estimates for the installed sign, not official brand colors.
- **Facade letters:** Silver-white (`#d4e3f2`), with flat caps 76 high and a common baseline
  at y 234.58. The **Ž** accent reaches y 138.38, 20 pt below the plaques. Repeated
  letters share the same redrawn shapes, and the horizontal spacing follows the leveled photo.
- **Shadow:** Separate vector copies on the layer behind the lettering, offset 3.2 pt to
  the right and 4.6 pt down, in slate (`#3f4b5a`) at 42% opacity.
- **Slatted backing:** A 1232 × 86 panel at x 14, y 155, behind the lettering and its
  shadow. Fifteen horizontal slats on a 5.55 pt pitch with slate faces (`#626e7c`),
  lighter edges (`#8794a3`), and dark gaps (`#454f5c`). The **Ž** accent sits above the panel.

### Compact version

`vilnius-compact.vectorcraft` crops to the LTG ribbon's 565 × 94.381 bounds with no
outer margin. The areas around the curved corners and between the plaques are transparent.
The ribbon keeps the full sign's artwork, scale, and colors. It identifies Lithuanian Railways,
not Vilnius specifically; the README supplies the station name.
