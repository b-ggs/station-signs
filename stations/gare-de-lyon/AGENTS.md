# Gare de Lyon

- **City, country:** Paris, France
- **Visited:** August 2026
- **System and spec:** Paris RATP. Uses “Paris RATP: Métro and RER entrance sign” in the
  root `AGENTS.md`.
- **Sign:** one outdoor entrance header with RER A and D and Métro 1 and 14. The Métro
  neighbors are Bastille and Reuilly–Diderot (1), and Châtelet and Bercy (14).

## Reference and decisions

- User-supplied `Screenshot 2026-11-23 at 7.57.42 AM.png` (not in the repo). The sign
  face was rectified for the layout. The user asked for a simple rectangular face instead
  of the original curved housing.
- Cropped 32 pt from the left and 47 pt from the top to balance the six circles in the
  white panel, measuring from the outer edges of the strokes. Cropped 21.63 pt from the
  right to balance the RATP lockup in its teal panel. The marks and lettering were not scaled.
- RER and M use the face navy; A uses `#b71e35`, D `#176546`, 1 `#efac00`, and 14
  `#292137`. These are visual matches to the photographed sign, not official line values.
- The legacy RATP symbol uses paths from [RATP.svg](https://fr.wikipedia.org/wiki/Fichier:RATP.svg).
  The heavier wordmark was redrawn from the photo with sharp corners and no stroke.
  Both are embedded, editable vectors.
- The user chose Parisine Bold over Source Sans 3 Bold, Helvetica Neue Bold, and Hind Bold.
  Source Sans 3 Bold is the manual fallback; no per-text fallback is configured.
- The 1 and 14 badge labels use Parisine Bold; RER, A, D, and M use Parisine Regular.
  The `8.14.08 AM` badge close-up shows tightly spaced digits in 14. The pair was
  tightened with tracking, not horizontal scaling. The D sits 3.5 pt right of geometric
  center and the single 1 sits 3.5 pt left and 0.75 pt down for optical balance.
- The user chose the smaller 39.5 pt RER label and 1.5 pt rounded outlines on RER, A,
  D, and M, over no outline, 0.75 pt, and 2.25 pt.
