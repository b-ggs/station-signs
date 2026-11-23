# Garibaldi bus stop

- **City, country:** Nice, France
- **Visited:** August 2026, after Prague and Paris
- **System and spec:** Lignes d’Azur. Uses “Nice Lignes d’Azur: bus shelter header” in the
  root `AGENTS.md`. This is the bus shelter header, not the nearby tram sign.
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
