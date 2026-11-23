# Roma Termini station

- **City, country:** Rome, Italy
- **Visited:** September 2024, with David
- **System and spec:** Roma Termini's own signage (the station is run by Grandi Stazioni for
  the FS group). Uses "Design spec: Roma Termini: entrance sign" at the end of this file. It's
  a one-off station sign, not a network-wide design.
- **Station:** Roma Termini, Rome's main railway station, on Piazza dei Cinquecento. It's the
  interchange between Metro lines A and B.
- **Sign:** the "Roma Termini" lettering on the glass over the main entrance, and the blue
  wayfinding band under it. The user asked for just those two.

## References and decisions

- The user supplied a watermarked stock photo (iStock 877041924, credit Cineberg; not in the
  repo) of the entrance, taken straight on. It was used for the layout, sizes and colors.
- Left out: the watermark, the stone walls, the advertising, the glass mullions and the
  horizontal transoms that cross the letters, and the building's shadow on the left of the
  band.
- The user chose background variant 2, a subtle top-to-bottom smoked-glass gradient,
  over the original flat blue-gray, four other flat colors, and a diagonal gradient.
- The left part of the band is in shadow in the photo, so the band blue was sampled from its
  sunlit right part.
- The real lettering is a heavy geometric sans with a single-story "a", set so tightly that
  letters touch. Futura Bold is the stand-in. A character stroke thickens it, and it's widened
  4% to fill the photo's width without the dots going visibly oval. Stronger widening (about
  12%) made the i-dots oval, and a thicker stroke merged "r" and "m", so both were backed off.
- In the photo the i-dots top out at the cap height; Futura's sit higher. Not corrected yet.
- "Roma" and "Termini" are separate text objects with a 10 pt gap between the "a" and the
  T's bar, as in the photo. The user asked for the R's start and the final i's end to be
  equidistant from the band's ends, so the lettering is centered on the band with 17.5 pt on
  each side (in the photo it's off by a few pt).
- Pictograms, corrected by the user against the photo:
  - **Tickets:** an upright blue ticket resting in a rounded, open palm. A close-up supplied
    by the user shows the open wrist on the right and the thumb crossing the front of the
    ticket. The English label is 3 pt closer to "Biglietti" than in the first layout.
  - **Info:** the "i" has serifs, a flag at the top and a foot.
  - **Escalators:** rounded, white with a blue outline. The rider is only a head and a body,
    with no legs or arms. Both torsos meet the upper edge of the sloping rail. The user picked
    83% of the original artwork size for more clearance inside the discs.
  - **Pharmacy:** four green corners form a cross. The 0.76 pt white gaps run all the way
    through the horizontal and vertical arms.
  - **Left luggage:** a rounded suitcase with a white strap line on each side.
  - **Platforms:** a white train in 3/4 view coming in from the left, its body narrowing
    toward the back. The entrance photo guided the broad, rounded nose, horizontal windshield,
    and two short rail strokes tucked under the nose. The windshield, four small side windows,
    and two headlights are cut out so the black disc shows through. An earlier drawing used
    a stock train illustration the user supplied (Shutterstock 2773259181; not in the repo).
- Two-line labels: the English line is nudged so its ink lines up with the bold Italian's
  left edge (Avenir's side bearings differ between sizes and weights).
- The band typeface is a humanist sans; Avenir Next (Bold, Regular for "Tickets", Medium for
  the English subtitles) stands in.
- The pictograms are simplified redraws at band scale, not traced: hand with ticket, info "i",
  Metro M, escalator, stairs, shopping bag, escalator, pharmacy cross, suitcase, train, plane.

## Design spec: Roma Termini: entrance sign

From the photo at 0.5 pt per pixel, with the photo's pixel (180, 452) at the origin.
Coordinates are in pt.

- **Artboard:** 880 × 170. The smoked-glass background fades vertically from `#46545d`
  at y 0 to `#2b3439` at y 130 and stays at that color to the bottom edge.
- **Lettering:** "Roma" and "Termini" as two text objects, Futura Bold 118, tracking −14, a
  2.5 pt character stroke in the fill color, widened to 104%, in `#ebecee`. The ink runs from
  x 27.5 to 853.5 (17.5 in from each end of the band), with 10 pt between "a" and "T". Cap
  height 90.5, baseline about 108.
- **Band:** x 10 to 871, y 127 to 149.5, blue `#034ea2`, with a 7 pt underside in `#09101d`.
  Thin separators (0.6 pt, `#9fb8d8`) at x 195, 321 and 473.5.
- **Binari panel:** yellow `#e3bf3c`, x 597.5 to 726, with text and pictogram in `#1a1a1a`.
- **Single-line labels** (Biglietti / Tickets, Metro, Shopping): Avenir Next 14.5, baseline
  143. **Two-line labels** (Deposito Bagagli, Binari, Fiumicino Aeroporto): Bold 10 on
  baseline 139, with the English in Medium 5.5 on baseline 146.3, its ink left-aligned to the
  Italian's (the English text sits 0.25 pt right of the Italian's origin). "12 - 29": Bold 16.5,
  tracking −80, baseline 144.
- **Pictograms:** 12.5 pt white discs (black for the train) centered on y 138.25 with a blue
  symbol (see the decisions above for what each shows); the Metro M is a white M on a red
  `#d0283a` 12 pt square; the plane is blue on a
  white 12 pt rounded square. Arrows are 2.3 pt strokes with miter joins, about 11 pt across.
