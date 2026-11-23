# Rochor station

- **City, country:** Singapore
- **Visited:** June 2026
- **System and spec:** Singapore MRT. Uses “Design spec: Singapore MRT: station name sign”
  at the end of this file.
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

## Design spec: Singapore MRT: station name sign

First pass from an oblique photo of the Rochor (DT13) platform sign. It was rectified with the
sign's corners, and its height set so Rochor's “o”s match LTAIdentity's proportions. All values
are in pt. Check this layout against other lines and stations before assuming it applies
system-wide.

- **Face:** 1600 × 376, dark charcoal `#353234`, sampled from the middle of the panel (the
  edges are lighter from glare; not yet reviewed by the user). A full-width line-color bar
  runs along the bottom, y 324–376. Ignore the red notices mounted below the sign.
- **Palette:**

  | Role | Color | Source |
  |---|---|---|
  | Panel | `#353234` | photo, middle of the panel |
  | Line color, Downtown Line (bar and badge) | `#0056b8` | LTA's official system map PDF (the DTL route stroke), ≈ Pantone 2935 C |
  | Text and badge ring | `#ffffff` | |

  The user chose the system map blue over the photo sample `#2454ae` (dimmed by station
  lighting), OpenStreetMap's `#0354a6` and the commonly cited `#005ec4`. For other lines, take
  colors from the same map: North South `#e1261c`, East West `#00953b`, North East `#9e28b5`,
  Circle `#ff9f19`, Thomson–East Coast `#9d5a18`.
- **Typefaces:**
  - English and the station code are **LTAIdentity** (the
    [IdentityFont](https://github.com/jglim/IdentityFont) reconstruction, a single Medium
    weight that VectorCraft lists as “Regular”). Install `font/LTAIdentity Medium.ttf` into
    `~/Library/Fonts`, then run `text.rescanFonts`. It has Latin letters only.
  - Chinese is **Hiragino Sans GB W3**, a stand-in, with a **1 pt white outline** to match the
    photo's 5 pt stems (W3 alone gives 4 pt).
  - Tamil is **InaiMathi Regular**, a stand-in, with a **1.5 pt white outline** and **106.5%
    horizontal scale** to match the photo's width. That gives 6 pt stems, and the user chose it
    over InaiMathi Bold (7 pt), and over outlines of 2 pt and 1 pt. Tamil Sangam MN is far too
    narrow.
- **Code badge:** a white shape at x 359–650.5, y 76.5–251, with elliptical ends (rx 60.5,
  ry 87.25, so the sides curve over the full height). Inside it is the line-color shape inset
  10.5 (rx 50, ry 76.75). The code (“DT 13”) is LTAIdentity 94 in white, centered at x 505,
  baseline 194, with −112 tracking on the space.
- **Station name:**

  | Element | Font, size | Position (baseline) |
  |---|---|---|
  | English (“Rochor”) | LTAIdentity 130 | left ink edge 725, baseline 152.5 |
  | Chinese (梧, 槽: one object per character) | Hiragino Sans GB W3 68, 1 pt outline | left edges 714.5 and 806, baseline 251.5 |
  | Tamil | InaiMathi Regular 66, 1.5 pt outline, 106.5% | left ink edge 927, baseline 252.5 |

  The Chinese characters are widely spaced, about 29 apart (ink to ink). The Tamil starts about
  57 after the last Chinese character.

Still open for Singapore MRT signs: the frame.
