# Anneessens-Fontainas premetro station

- **City, country:** Brussels, Belgium
- **Visited:** September 2025, with David
- **System and spec:** Brussels STIB/MIVB premetro. Uses "Design spec: STIB: station name sign"
  at the end of this file.
- **Station:** Anneessens-Fontainas, on the North–South premetro axis under the city center,
  between Bourse and Lemonnier. It was formerly just "Anneessens", and "Fontainas" was added
  later (reportedly in 2019, not confirmed by an STIB source)
  ([Wikipedia](https://en.wikipedia.org/wiki/Anneessens-Fontainas_premetro_station)).
- **Lines on the sign:** tram 4 and tram 10. Line 10 replaced line 3 in 2024
  ([Wikipedia](https://en.wikipedia.org/wiki/Brussels_tram_route_4)).

## References and decisions

- `Screenshot 2026-11-23 at 11.07.18 PM.png` (not in the repo), supplied by the user, is a clean,
  nearly straight-on view. It was used for the layout, measurements and colors.
- `Screenshot 2026-11-23 at 11.07.20 PM.png` (not in the repo), supplied by the user, shows the
  same sign style with graffiti ("GTA") and a sticker. It was used only to confirm the layout.
- The sign is recreated clean, without the graffiti and the sticker.
- STIB's signage typeface is Brusseline
  ([Wikipedia](https://en.wikipedia.org/wiki/Brusseline)). It isn't installed, and it can't be
  obtained legitimately: it's a custom STIB face that isn't for sale
  ([Luc Devroye](https://luc.devroye.org/fonts-46367.html)). Parisine, which inspired its name,
  is the stand-in.
- The colors were sampled from the clean photo and white-balanced so that the panel comes out
  light gray. Line 4 comes out pink and line 10 purple, consistent with published values
  (`#EA4F80` and `#8F4199`, from a third-party listing).
- The photo was taken from slightly below, so its top frame lip looks thicker. The recreation
  uses an even 8 pt frame.

## Design spec: STIB: station name sign

First pass from the clean reference photo, at 0.5 pt per pixel of a 6× crop. Coordinates are in
pt.

- **Face:** 600 × 160. An aluminum frame `#c4c6cb`, 8 pt on every side, surrounds a light gray
  panel `#e9e9ef`.
- **Divider:** a 1 pt vertical line `#a8aabb` at x 248.5, from y 30 to 130. It splits the
  symbols, on the left, from the name, on the right.
- **Symbols:** vertically centered on y 80, in this order:
  - The tram symbol: a 45 pt circle `#df5a72` centered at x 61, with a white "T" (Parisine Bold
    32).
  - Line squares, 49 × 49 at y 55.5, starting at x 98.5 and x 160. The number is centered on
    baseline 93, in Parisine Bold 36. Line 4 is pink `#dd6391` with a dark `#222222` number.
    Line 10 is purple `#73489a` with a white number.
- **Name:** centered at x 420, the middle of the right section, in Parisine Bold 42, `#4a4b5e`.
  A two-word name is set on two lines, on baselines 74 and 121.
