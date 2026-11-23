# Prospect Av station

- **City, country:** Brooklyn, New York City, USA.
- **Visited:** May 2019 with Rodj.
- **System and spec:** New York City Subway (NYCTA). Uses “Design spec: New York City Subway
  entrance sign” below.
- **Station:** Prospect Av at Prospect Avenue and Fourth Avenue, on the BMT Fourth Avenue
  Line. The **R** local stops here; the MTA GTFS stop ID is **R34**.
- **Neighbors:** 4 Av–9 St toward Manhattan and Queens, and 25 St toward Bay Ridge.
- **Sign:** “Prospect Av Station,” R bullet, and “Manhattan & Queens.” This is the
  Brooklyn station, not the Prospect Av station in the Bronx.

## References and decisions

- `Screenshot 2026-11-24 at 6.33.37 AM.png` (user attachment, not tracked): blurred
  Google Street View crop, used for layout and wording only. The right and bottom margins
  are estimates, not measurements of the physical panel. No color was sampled from it.
- The user chose a 24 pt bottom margin, measured from the visible ink of the direction
  line, over the original 67 pt and alternatives of 44 and 12 pt. Only the bottom edge moved.
- [NYCTA Graphics Standards Manual reissue and design history](https://standardsmanual.com/products/nyctacompactedition):
  documents the 1970 Unimark program and explains how the familiar black signs, white
  lettering, white top rule, and colored route discs developed. The original manual’s
  Standard Medium and later Helvetica practice are distinct.
- [Paul Shaw’s signage history for AIGA](https://web.archive.org/web/20140705150406/http://www.aiga.org/the-mostly-true-story-of-helvetica-and-the-new-york-city-subway/)
  identifies **Helvetica Medium** as the 1989 MTA Sign Manual’s NYCTA standard and calls
  the later cut **Neue Helvetica 65**. Linotype lists that weight as
  [Neue Helvetica 65 Medium](https://www.myfonts.com/products/pro-65-medium-189171-neue-helvetica-369223).
  The recreation already uses the macOS release of that family and weight, listed as
  **Helvetica Neue Medium** (`HelveticaNeue-Medium`). This verifies the type choice against
  the system standard, not the specific font file or fabrication of this blurred panel.
- [MTA stylesheet](https://www.mta.info/themes/custom/bootstrap_mta/dist/mta-style.css):
  its `span.line-r` SVG uses Broadway yellow `#fccc0a` and a black R. The recreation uses
  that digital R outline centered on an editable yellow disc.
- [MTA R line map](https://www.mta.info/maps/subway-line-maps/r-line) and
  [MTA subway GTFS](https://rrgtfsfeeds.s3.amazonaws.com/gtfs_subway.zip): station,
  line, stop ID, and neighbors. A
  [SubwayNut photo of an older entrance sign](https://subwaynut.com/bmt/prospectm/prospectm15.jpg)
  corroborates the station and direction wording, but has a different layout and an M
  bullet. The recreation follows the single R and the order in the supplied reference.

## Design spec: New York City Subway entrance sign

First pass for this directional entrance panel. Other entrances and installation dates
can have different layouts. Dimensions are in points.

- **Face:** 1000 × 497, black (`#000000`). White (`#ffffff`) inset top rule at
  x 24, y 25, 952 × 4.
- **Station title:** “Prospect Av Station,” live Helvetica Neue Medium 96, white, with
  baseline y 111 and visible left edge about x 24.
- **Route bullet:** A 150 pt Broadway yellow (`#fccc0a`) disc at (24, 136). The black
  glyph comes from the MTA’s R asset, scaled to the same disc diameter.
- **Direction:** “Manhattan & Queens,” live Helvetica Neue Medium 65, white, with
  baseline y 469 and visible left edge about x 24. The open space beneath the route
  bullet follows the supplied layout.
