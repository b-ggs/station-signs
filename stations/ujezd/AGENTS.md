# Újezd tram stop

- **City, country:** Prague, Czechia
- **Visited:** August 2026
- **System and spec:** Prague tram, operated by Dopravní podnik hl. m. Prahy (DPP) within
  Pražská integrovaná doprava (PID). Uses “Design spec: Prague tram (DPP / PID): direction
  sign” at the end of this file.
- **Panel:** `809 / 2-p` as printed. Straight arrow: 12, 15, 20, toward Tyršův dům
  (formerly the northbound Hellichova stop); right arrow: 9, 98, 99, toward Národní divadlo.
  Švandovo divadlo is the preceding stop on that approach. See the
  [PID stop rename notice](https://pid.cz/prejmenovani-tramvajove-zastavky-hellichova-od-28-cervna).

## References and decisions

- User-supplied `Screenshot 2026-11-23 at 7.37.44 AM.png` (not in the repo). The printed face
  was rectified for measurements. The recreation omits the metal frame, glass, reflections,
  and wear. The route numbers reproduce the photographed panel, not a live schedule.
- The oblique reference (`7.43.24 AM`) and footer and title close-ups (`7.44.05 AM` and
  `7.45.05 AM`) show gray backing and separate rounded plates. The user specified pure
  white, not off-white, for the light panels.
- Footer: `809 / 2-p`, `Infolinka / infoline: 296 19 18 17`, and `www.dpp.cz`, followed by
  the DPP and PID lockups. The phone number is corroborated by the
  [DPP operator listing](https://pid.cz/dopravci-a-partneri/dopravni-podnik-hl-m-prahy/).
- The DPP lockup is embedded from the [operator's website](https://www.dpp.cz/common/images/layout/logo.webp).
  The Czech PID lockup is vector artwork from the [official logo pack](https://pid.cz/o-systemu/loga-pid-ropid/).
- The 6 pt right crop balances the title and grid margins. The bottom crop hides the
  footer plates' lower corners, and the right crop hides the logo plate's upper-right
  corner. Both logos were lowered to align their visible bottoms with `www.dpp.cz`.
- Source Sans 3 is a stand-in. The exact backing gray is estimated.

## Compact version

`ujezd-compact.vectorcraft` (594 × 634) is a copy of the full sign without the fifth grid row
(the empty cells at y 613). The footer (stop code, contact plate and logo plate) moves up
108 pt, one row pitch, so it starts at y 612, and the gray backing is shortened to match.
Everything above the footer is identical to the full sign, so carry over any changes made
there.

## Design spec: Prague tram (DPP / PID): direction sign

First pass from the rectified photo of the Újezd tram direction panel. These measurements
describe this style of printed panel, not newer PID stop signs. Coordinates are in pt.

- **Face:** 594 × 742 after trimming the right and bottom edges. The title and grid have
  matching 6 pt side margins. Neutral gray `#d4d4d4` backing shows around the pure white
  `#ffffff` panels and in the grid gutters. Dark ink is `#23262a`.
- **Stop name:** centered at x 305, Source Sans 3 Bold 83 at 92% horizontal scale,
  baseline 121. Preserve the uppercase accents. Its rounded white panel is at (6, 6),
  582 × 171 with a 6 pt corner radius.
- **Grid:** three columns and five rows, including empty cells. Cell left edges are
  x 6, 202, and 398; top edges start at y 181 and repeat every 108. Cells are 190 × 104
  with 6 pt corner radii and no outlines. Night routes use solid dark cells and pure
  white numerals. Traced direction arrows occupy the top row.
- **Route numbers:** Source Sans 3 SemiBold 119 at 91% horizontal scale, with baselines
  379, 487, and 595 in the three occupied number rows. Align to the appropriate column.
- **Footer:** stop plate code at left on the gray backing. Czech and English information-line
  labels, phone number, and website share one rounded white plate; the DPP and PID lockups
  share a second. The cropped plates run from y 720 to the bottom edge. The contact plate
  has two 5 pt top corners; the logo plate only retains its 5 pt upper-left corner.
  Match the specific photo rather than replacing the historical contact details or branding.
