# Formosa Boulevard (R10/O5)

- **City, country:** Kaohsiung, Taiwan
- **Visited:** October 2026
- **Rail system and spec:** Kaohsiung Metro. Uses “Kaohsiung Metro: entrance sign” in the root
  `AGENTS.md`.
- **Station:** 美麗島站 / Formosa Boulevard Station, Red Line **R10** and Orange Line **O5**.
- **Neighbors:** R9 Central Park and R11 Kaohsiung Main Station; O4 Cianjin and O6 Sinyi
  Elementary School, per the [Kaohsiung Metro guide map](https://www.krtc.com.tw/eng/Guide/guide_map).

## Sign and references

`formosa-boulevard.vectorcraft` holds one sign, **Entrance 1**. The two user-supplied reference
images are not stored in the repo:

- Entrance 1, `Screenshot 2026-11-23 at 7.10.49 AM.png`: oblique and heavily reflective. Used
  for the broad single numeral with a curved hook and no bottom foot.
- Entrance 10, `Screenshot 2026-11-23 at 7.08.41 AM.png`: nearly straight on, with a cool cast.
  Used to estimate face proportions, band height, badge positions, and lettering.
- Entrance 1 label close-up, `Screenshot 2026-11-23 at 7.28.14 AM.png`: the two lines share a
  left edge and are nearly the same width, with English shorter and compact.

## Decisions and open questions

- The individually editable Chinese characters sit at x 532, 725, 918, and 1117, with
  horizontal scales of 95%, 94%, 100%, and 96%. The user chose to raise the name 4 pt from
  the original badge alignment, to baseline 159. English starts at x 152 and uses 103.6%
  horizontal scale. The stacked entrance
  label aligns to its ink edges at y 276.75 and 331. Both label lines run from x 1212.75
  to 1321 by their visible edges. The larger, heavier Chinese lettering matches the width
  of “Entrance” without squeezing the English.
- The yellow “1” is an editable vector path, within x 1407–1522 and y 64–329.5 before its
  outline. Its position and outline are estimated from the oblique photo, using the shared
  badges and Chinese lettering as landmarks. It sits farther right than the “1” in “10,”
  and the bottom of its outline aligns with the bottom of the English lettering.
- Only the printed face is modeled. Reflections, seams, fasteners, frame, and surrounding
  architecture are not drawn.
