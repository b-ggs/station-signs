# Formosa Boulevard (R10/O5)

- **City, country:** Kaohsiung, Taiwan
- **Visited:** October 2026
- **Rail system and spec:** Kaohsiung Metro. Uses “Design spec: Kaohsiung Metro: entrance sign” at
  the end of this file.
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

## Design spec: Kaohsiung Metro: entrance sign

Based on two photos of Formosa Boulevard. The nearly straight-on Entrance 10 photo was
rectified to measure the face and shared typography. The oblique Entrance 1 photo supplies the
single-digit placement and shape. Check this layout against other stations before assuming it
applies system-wide. Coordinates are in pt.

- **Face:** 1600 × 380, about 4.2:1. Light neutral gray `#b6b6b6` above y 234 (chosen
  over the cool photo sample, white, and warmer grays). Deep blue `#0a1736` below, sampled
  from unobstructed patches in the Entrance 10 photo without white balancing.
- **Route badges:** 128 pt discs centered at y 119, with centers at x 170 and 340 on the
  two-line sign. Red `#b13442` and orange `#c47b38`; codes in off-white `#f3f0e9`, Arial
  Bold 64, centered on the discs at baseline 142 (R10 at 95% horizontal scale).
- **Station names:** traditional Chinese in Songti TC Bold 140, near-black `#19191b`,
  with a 2 pt outline in the same color (chosen over no outline, 1 pt, and 3.5 pt). Baseline
  163 was the measured starting point; for Formosa Boulevard, the user preferred the name
  4 pt higher, at baseline 159. English is Arial Bold 73, off-white, baseline 330. The
  station's notes record spacing and widths.
- **Entrance label:** 出入口 in Hiragino Sans GB W6, 35 pt with tracking 142, and “Entrance”
  in Arial Bold 26 at its natural width. Both are off-white, left-aligned by their visible
  edges, and the same visual width. Align the visible top of 出入口 to the English station
  name's top, and the visible bottom of “Entrance” to the English name and outlined numeral.
  On Formosa Boulevard that puts the visible edges at y 276.75 and 331.
- **Entrance number:** tall yellow `#d7bc54` with a 3 pt dark outline `#202023`, spanning
  both bands. Trace the photographed numeral rather than substituting a font digit; adjust
  placement for the number of digits.

Still open: whether to include the physical frame and fasteners.
