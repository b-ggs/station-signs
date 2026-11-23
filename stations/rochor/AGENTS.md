# Rochor station

- **City, country:** Singapore
- **Visited:** June 2026
- **System and spec:** Singapore MRT. Uses “Singapore MRT: station name sign” in the root
  `AGENTS.md`.
- **Names:** Rochor, 梧槽 (Chinese), ரோச்சோர் (Tamil)
- **Line and code:** Downtown Line, **DT13**
- **Neighbors:** Little India (DT12) and Bugis (DT14)

## References and decisions

- `Screenshot 2026-11-23 at 5.00.28 PM.png`: an oblique photo from below. It isn't stored in the
  repo. Corners in the photo are (63, 187), (2302, 143), (2339, 682) and (32, 697). The height was
  set so the two “o”s in Rochor match LTAIdentity's proportions (the photo's were about 3% wide
  at the first guess), which gives 1600 × 376.
- The red notices below the sign are ignored, as the user asked. Only the printed face is
  modeled. The blue bar at the bottom is part of the sign.
- Badge text spacing: the photo's space between DT and 13 is narrower than the font's, so the
  space carries −112 tracking.
- Weights (variants compared Nov 2026): the user asked for lighter Tamil and thicker Chinese, and
  chose variant 3. Tamil is InaiMathi Regular 66 with a 1.5 pt white outline at 106.5%
  horizontal scale, which gives 6 pt stems. It was chosen over Bold (7 pt) and over 2 pt and 1 pt
  outlines. Chinese is W3 with a 1 pt outline, which gives 5 pt stems and matches the photo. It
  was chosen over 0.5 and 1.5 pt. Tamil Sangam MN was about 26% too narrow.
- Blue (variants compared Nov 2026): `#0056b8`, read from LTA's system map PDF, chosen over the
  photo sample `#2454ae`, OSM's `#0354a6` and `#005ec4`.
- Open: the panel charcoal (photo sample, not reviewed) and the frame.
