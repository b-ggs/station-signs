"""Generate the Prince Edward tile mosaic as an SVG, for placing into VectorCraft.

Usage: uv run python mosaic.py mosaic.svg

The full wall is 528 x 378 pt, the framing of the reference photo. CROP keeps only the tiles
inside a rectangle on the tile grid and shifts them to the origin, so the crop shows exactly the
same tiles as the full wall.

The 12 shades were measured from the user's reference photo: tile centers sampled around the
lettering, pulled 40% toward their mean to remove JPEG noise, then split by lightness into 12
equal-sized groups. Tiles are 5 pt squares on a 6 pt pitch, nudged up to 0.25 pt at random so the
grid looks hand-set. The fixed seed makes the output repeatable.
"""

import random
import sys

W, H = 528, 378  # wall size in pt
PITCH, TILE = 6.0, 5.0
JITTER = 0.25
GROUT = "#5f5052"
SHADES = [
    "#735e60", "#796366", "#7c6769", "#7e696c", "#806c6e", "#836e70",
    "#857073", "#887376", "#8b7779", "#8f7b7d", "#948183", "#9d8e8f",
]
SEED = 20250201
CROP = (126, 114, 276, 144)  # x, y, width, height on the full wall; None for all of it


def main(out):
    cx, cy, cw, ch = CROP or (0, 0, W, H)
    random.seed(SEED)
    paths = {k: [] for k in range(len(SHADES))}
    for r in range(int(H / PITCH)):
        for c in range(int(W / PITCH)):
            k = random.choices(range(len(SHADES)))[0]
            jx = random.uniform(-JITTER, JITTER)
            jy = random.uniform(-JITTER, JITTER)
            x = c * PITCH + (PITCH - TILE) / 2 + jx
            y = r * PITCH + (PITCH - TILE) / 2 + jy
            if not (cx <= c * PITCH < cx + cw and cy <= r * PITCH < cy + ch):
                continue
            paths[k].append(f"M{x - cx:.2f} {y - cy:.2f}h{TILE}v{TILE}h{-TILE}z")
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{cw}" height="{ch}" viewBox="0 0 {cw} {ch}">',
        f'<rect id="Grout" x="0" y="0" width="{cw}" height="{ch}" fill="{GROUT}"/>',
    ]
    for k, color in enumerate(SHADES):
        svg.append(f'<path id="Tiles_{k + 1:02d}" fill="{color}" d="{"".join(paths[k])}"/>')
    svg.append("</svg>")
    with open(out, "w") as f:
        f.write("\n".join(svg))


if __name__ == "__main__":
    main(sys.argv[1])
