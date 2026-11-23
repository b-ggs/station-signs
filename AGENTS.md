# AGENTS.md

Guidance for AI agents working in this repo.

## What this repo is

Recreations of train station signs that are **personally significant to the user**, from rail
systems in different countries. The first is Bangkok BTS, and Japanese and Taiwanese stations
are coming next. They're designed in **VectorCraft** (v0.24.1, `/Applications/VectorCraft.app`).
Agents build artwork **live in the user's running VectorCraft window**, so the user can watch,
hand-edit, and steer as the work happens.

Write all docs in **American English**: color, center, gray, neighbor, catalog, labeled.

Every rail system has its own sign design. Don't carry BTS conventions (layout, fonts, colors,
the platform panel, the route strip) into another system's signs. Each system gets its own
design spec below, built from that system's reference photos.

## Working mode: live in the app

The default is live mode. Don't use headless `vectorcraft-cli run` or `convert` for design work
unless the user asks. Live mode has two parts:

1. **The app, started with its control server on port 7979:**

   ```sh
   open -a VectorCraft --args --control 7979
   ```

   If VectorCraft is already open without `--control`, ask the user to quit it and relaunch with
   the command above. Don't kill the app yourself, because it may hold unsaved work.
   Check that the server is up with:

   ```sh
   lsof -nP -iTCP:7979 -sTCP:LISTEN
   ```

2. **The MCP server**, registered in `.mcp.json` as `vectorcraft`:

   ```sh
   vectorcraft-cli mcp --connect 127.0.0.1:7979
   ```

   Pass `--connect` explicitly. With it, the server fails with `Connection refused` when the
   app isn't listening. Without it, the server silently falls back to a headless in-process
   session, and you end up drawing into an invisible document.

Claude Code reads `.mcp.json` only when a session starts. The approval prompt appears in a new
session, not in the one that created or edited the file.

**If the vectorcraft MCP tools fail to connect:** start the app (step 1), then have the user
reconnect the MCP server with `/mcp`. Don't switch to headless mode as a workaround.

### Live-mode etiquette

- The user may be editing at the same time. Before changing an existing document, inspect it
  (`document.inspect`, `document.find`) rather than assuming its state.
- Name layers and objects meaningfully so the user can find them in the Layers panel.
- Build in small, visible steps and tell the user what changed. Don't rebuild a whole
  document in one opaque batch.
- After each meaningful change, check your work visually with `render_preview` (the document)
  or `screenshot` / `ui_screenshot` (the app window). Don't assume the geometry came out right.
- Ask before closing, reverting, or overwriting a document, or deleting anything the user made.
- Save each station's source file into its own station folder (see "Repo layout" below).

### Show variants for visual tweaks

When the user asks for a subjective visual change ("slightly thicker", "a bit closer", "try a
different font", "bigger"), **show variants automatically** instead of guessing a single value.
Don't ask first.

1. Rename artboard 0 to note what it shows, for example "Ring 5 pt (current)", and keep it
   unchanged as the reference.
2. Make about three copies with `artboard.duplicate {index, art: true, side: "bottom"}`, each from
   the previous copy so they stack downwards. Name each one after its value, for example
   "Ring 6 pt".
   - The user counts variants **from 1, top to bottom**. "Variant 7" means the seventh artboard,
     which is index 6. Start every artboard name with that number, for example "1 · Ring 5 pt
     (current)" and "2 · Ring 6 pt", and use the same numbers when you report back.
3. Afterwards, check that nothing was left behind. Text whose line box sticks out past the edge
   isn't copied (on the BTS sign, that's ชานชาลา), so copy it with
   `object.move {ids, dx: 0, dy: 440·n, copy: true}`.
4. Apply one value per copy. Pick steps that are clearly different from each other, and measure
   when you can. For example, compare a value with the next font weight up, so the steps aren't too
   small to see.
5. Render every version and check it. Tell the user what changed and what to look for, and note
   any trade-offs, such as a change that affects small and large text differently.
6. When the user picks one, apply that value to artboard 0, delete the other copies and their
   art, and rename artboard 0 back to the sign's name. Then record the decision in the rail
   system's spec (if it applies to every station on that system) or in the station's
   `AGENTS.md`, and save.

If a request is ambiguous ("bump up" could mean bigger or higher), state your reading in one line
before making variants.

Only make a single direct change when the user gives an exact value ("make it 14 pt") or the
change is clearly objective (a fix, a typo, an alignment to a measured edge).

## Command reference

- Full catalog: `vectorcraft-cli commands` (JSON, about 1,400 commands, about 800 KB). Don't
  read it into context whole. Filter it instead, for example:

  ```sh
  vectorcraft-cli commands | python3 -c "import json,sys; [print(c['id'], '—', c['params']) for c in json.load(sys.stdin) if c['id'].startswith('shape.')]"
  ```

- Each entry has `id`, `params` (a compact signature with the return shape), and `enabled` /
  `disabled_reason` (for example, "no document open").
- Commonly used commands:
  - Documents: `file.new`, `document.setup`, `document.setUnits`, `document.inspect`,
    `document.find`, `file.saveAs`, `document.export`
  - Artboards: `artboard.new`, `artboard.setProps`, `artboard.rename`
  - Shapes and paths: `shape.rectangle {x, y, width, height, radius?}`, `shape.ellipse`,
    `shape.line`, `shape.polygon`, `path.create`, `object.pathfinder.*`
  - Text: `text.create {x, y, text, size?, font?, style?, color?, justify?, area?}`,
    `text.setStyle`, `text.fonts`, `text.fontList`. Check `warning` in the result, which means
    the requested font fell back to another one.
- Fonts installed on this machine:
  - Thai: **Thonburi** (Light, Regular and Bold), Sukhumvit Set, Tahoma, Noto Sans Thai,
    Ayuthaya, Silom, Sathu and Krungthep
  - Latin: Helvetica Neue, Arial, Inter and Avenir Next. Thonburi and Tahoma also have Latin
    letters.
- Coordinates are in points (pt) by default, with the origin at the top left and y increasing
  downward. A new document defaults to US Letter (612 × 792 pt).
- `artboard.setProps` with a new `x`, `y`, `width` or `height` changes only the artboard. The art
  inside doesn't move or scale with it, so move it yourself with `object.move {ids, dx, dy}`.
- `artboard.duplicate {index, art: true, side}` copies an artboard with its art, which is handy for
  side-by-side variants. The copied objects come back in the same order as the originals. It only
  copies objects that sit **fully inside** the artboard. Text whose line box sticks out past the
  edge, such as tall Thai text near the top, is left behind, so copy it yourself with
  `object.move {ids, dx, dy, copy: true}`.
- `file.saveAs` saves in the background and won't create missing folders. Run `mkdir -p` first,
  then confirm the file exists.
- `stroke.set` takes `weight`, not `width`.
- `render_preview` renders at most 1:1. To measure positions in it, use Pillow through uv
  (`uv run --with pillow python ...`).
- New shapes default to a white fill with a 1 pt black stroke. Set paint explicitly.

## Headless mode (only when asked)

Use this for quick checks, batch exports, or format conversion without touching the user's window:

```sh
vectorcraft-cli run [--in FILE] --cmd ID --params 'JSON' ... --export out.svg
vectorcraft-cli convert in.vectorcraft out.pdf
vectorcraft-cli info FILE
```

## Repo layout

- `README.md`: a short overview for people. When you add a station, add a row to its table, which
  has four columns: `Sign | Station | City, Country | Visited`.
  - **Sign:** a thumbnail of the station's preview PNG, linked to its folder:
    `<a href="stations/<slug>/"><img src="stations/<slug>/<slug>.png" alt="…" width="240"></a>`
  - **Station:** the station name, linked to its folder.
  - **Visited:** a short month and year, for example "Apr 2026". Ask the user when they visited;
    don't guess.
  - Keep the rows in order of visit, earliest first, and insert a new station where its date falls.
- `AGENTS.md`: this file. It holds guidance shared by every station, plus one design spec per
  rail system.
- `.mcp.json`: registers the `vectorcraft` MCP server (live mode)
- `stations/<station-slug>/`: one folder per station, for example `stations/phrom-phong/`. Each
  holds:
  - `<station-slug>.vectorcraft`: the source file. It holds **exactly one sign** on one artboard.
    Extra artboards only exist temporarily while comparing variants, and get deleted once the
    user picks one.
  - `<station-slug>.png`: a preview, exported at 1× with
    `vectorcraft-cli convert <slug>.vectorcraft <slug>.png --scale 1`, which gives a
    1620 × 420 px image for a BTS sign. The user chose 1× over 0.5× because the smaller image
    looked fuzzy on Retina screens, especially fine Tamil and Chinese text. The station README
    shows it full width, and the root README's table shows it as a 240 px thumbnail.
    **Re-export it whenever the sign changes.**
  - `README.md`: a short overview for people, with the station name in English and the local
    script, the city and country, line, code and neighbors, when the user visited and who with
    (one line, for example "Visited in March 2026 with Clark and Paul."; ask, don't guess), which
    sign it is (for example "Platform 2"), an export command and brief design notes. Keep it
    simple, with no signs table. The full decision log goes in `AGENTS.md`, not here.
  - `AGENTS.md`: station-specific facts (names, codes, neighbors, platforms, the reference
    photos used, decisions and open questions), plus a `CLAUDE.md` containing `@AGENTS.md`
  - `exports/`: rendered SVG, PDF and PNG files (create when needed)

Put working practices shared by every station, and each rail system's design spec, in this file.
Put anything specific to one station in that station's `AGENTS.md`. When starting a new station,
copy the folder structure of an existing station, but not its design. Each station's `AGENTS.md`
should say which rail system and spec it uses. Use the station's common English name for the
slug. If two stations would get the same slug, add the city, for example `stations/ueno-tokyo/`.

## Sign design specs (one per rail system)

When starting a station on a new system, add a new `###` spec here, built from straight-on
reference photos, the way the BTS spec was. Ask the user for photos if there aren't any.

### Bangkok BTS Skytrain: platform sign

These measurements come from a straight-on reference photo (Victory Monument, Platform 1),
scaled so the sign is 420 pt tall. All values are in pt. Each station's `AGENTS.md` supplies the
text and station codes.

- **Overall:** 1620 × 420. The platform panel is 320 wide, on the side of the platform it
  serves (for example, left for Phrom Phong Platform 2 and right for Victory Monument
  Platform 1). The main sign is 1300 wide, about 3.1 times its height. Its center (x = 970 when
  the panel is on the left, 650 when it's on the right) is the axis for the station name and
  route strip.
- **Bands:** navy 0–256 (61% of the height), then the line color 256–420. Any darker navy in
  photos is shadow.
- **Palette** (decided by the user after comparing several sets; no official BTS spec exists
  online):

  | Role | Color | Source |
  |---|---|---|
  | Navy, used for **every** blue element | `#2d3a5e` | matched to photos; a white-balanced photo gave nearly the same value |
  | Sukhumvit Line green | `#6baa51` | Victory Monument photo, white-balanced |
  | Current-station yellow | `#f2d237` | the photo yellow's hue, lightened 75% of the way toward `#f5d90a` (in OKLab) |
  | Chevrons | `#e5d377` | the same treatment as the yellow |
  | Platform panel | `#ffffff` | white, at the user's request (it was off-white `#efeee6` before) |
  | Panel divider | `#a5a49c` | |

  Other lines need their own line color, so ask the user. Rejected options include the BTS
  website's `#273e83` / `#358300`, the route map's `#8db63c` and Wikipedia's `#76b729`.
- **Typefaces:**
  - Thai is **Thonburi Regular** with a **1 pt outline in the text's own color**, which brings it
    about a third of the way to Bold. Set it with
    `text.setStyle {stroke: <fill color>, strokeWidth: 1}`. It's the same 1 pt at every size, not
    scaled. Thonburi has no adjustable weight, so this outline stands in for one. The real BTS
    typeface is undocumented.
  - Latin is **Helvetica Neue Bold**, chosen by the user over Tahoma Bold and Thonburi Bold.
- **One blue:** every blue element uses the same color, as the navy band does. That covers the
  station circles, the route bar, the platform circle, the platform text (ชานชาลา and "Platform")
  and the code label on the yellow circle. The user asked for this. Thai text in navy also gets a
  navy outline.
- **Text colors:** all text on navy *and* on the line color is pure white `#ffffff`, both Thai and
  English. That includes the previous and next station names. Don't use cream or off-white
  anywhere, including the platform panel and its number. The only non-white text is the navy
  platform text on the white panel and the navy code label on the yellow circle.
- **Main sign text** (x is measured from the main sign's left edge):

  | Element | Size | Position (baseline) |
  |---|---|---|
  | Line name, Thai (สายสุขุมวิท) | 50 | left 31, baseline 55 |
  | Line name, English ("Sukhumvit Line") | 49 | right-aligned to the same ink edge as the next-station name, baseline 57 |
  | Station name, Thai | 108 (matched on letter height; Thonburi's marks are tall) | centered, baseline 144 |
  | Station name, English | 81 | centered, baseline 232 |
  | Previous and next station, Thai | 38 | left 28 or right 27, baseline 324 (both sides) |
  | Previous and next station, English | 37 | same, baseline 371 (both sides) |

- **Route strip** (center line y = 337):
  - The current station is a yellow `#f2d237` circle with a **6 pt** white ring, centered on the
    main axis. The circle is drawn 75 across, so it measures 81 including the ring. All three
    station circles use the 6 pt ring, chosen over 5, 7 and 8 pt.
  - The previous station is a navy `#2d3a5e` circle, 80 across, about 205 from the axis.
  - The next station (the direction of travel) is a larger navy circle, about 101 across, about
    214 from the axis.
  - A navy bar 39 tall (y 317.5–356.5) with a **3.5 pt** white outline runs from the previous
    station to an arrowhead. The 3.5 pt was confirmed against 1.5–7.5 pt. It's deliberately
    thinner than the 6 pt station rings: thicker borders eat into the narrow chevrons.
  - Two pale chevrons `#e5d377` have the same 3.5 pt white outline. Each is 39 tall and 30 wide,
    with 14 of solid thickness and a 16 deep notch.
  - The arrowhead has the same angle as the chevrons: each edge runs 16 across for 19.5 down.
    There's one even rhythm: **14 pt** (measured horizontally) from the arrowhead to chevron 1, and
    14 pt from chevron 1 to chevron 2. The user rejected 8 pt (too close) and 20 pt.
  - Positions are measured from the axis toward the next station. Chevron 1's back corners are
    at +90 and chevron 2's at +118, so chevron 2's tip sits at +148. The arrowhead's corners are
    at +76 and its tip at +92.
  - (Phrom Phong values, with the axis at 970: arrowhead corners at 1046 and tip at 1062,
    chevrons at 1060 and 1088.)
  - Change only what the user asks for. Don't move neighboring elements, such as the chevrons,
    to make room.
  - The route strip points toward the next station. On a sign where the next station is on the
    left, mirror it.
  - Station code labels are 34 pt, or 40 pt in the next-station circle.
- **Platform panel:** white `#ffffff`, with a 2 pt gray divider `#a5a49c` and navy ink `#2d3a5e`.
  - ชานชาลา at 78 pt, centered, baseline 63
  - a circle 210 across, centered at y 207, with the number at 210 pt in white `#ffffff`. The number is
    centered horizontally by its ink, and **sits 4 pt above true center** (baseline 278, leaving
    26 pt of space above the digit and 35 pt below). That optical correction was chosen over
    exact centring and over 8 or 12 pt up. Measure the ink after placing a different digit, since
    each number's shape differs.
  - "Platform" at 57 pt, centered, baseline 395

Still open for BTS signs: the metal frame and production format.

### JR East: station name sign (駅名標)

Used by Ueno (Yamanote Line, JY) and Akihabara (Chūō–Sōbu Line, JB).

These measurements come from a reference photo of the Ueno JY05 sign, taken from below. Its
keystone was corrected using the sign's corners, and its height set so the square numbering
badges (JY05 and JY06) come out square. That makes the sign **1600 × 425** (about 3.75:1). All
values are in pt.

**Every JR East sign uses 1600 × 425**, even where the real sign is a different length.
Akihabara's real sign is about 5:1, and the user chose to keep these proportions so the set
matches. Element sizes stay the same; only the spacing of the station name changes (see
"Station name block"). Each station's `AGENTS.md` supplies the text and station codes.

- **Overall:** a white face `#ffffff`, 1600 × 425, with no frame yet. The main axis, which the
  kanji pair, kana, English name and current-station block center on, is x = 795 (measured, not
  exactly the middle).
- **Route band:** y 242–330 (88 tall; the photo measured 87). It runs from the left edge to
  x 1470, then an arrowhead points at the next station, with its tip at (1557, 286). The current
  station is a line-color block, x 753–834, the full band height. Mirror the band when the next
  station is on the left. Keep the band's top and bottom on **even** y values. At 87 tall, the
  bottom edge fell on a half pixel in the 0.5× preview PNG, which left a faint row and a visible
  step where it met the arrowhead.
- **Palette** (first pass, matched from the photo. The user hasn't reviewed it yet):

  | Role | Color | Source |
  |---|---|---|
  | Route band, dark green | `#156419` | photo, white-balanced (the photo's white was 229) |
  | Line color (current-station block, badge borders): Yamanote (JY) | `#80c241` | between the photo's block and badge greens; close to the commonly cited Yamanote green |
  | Line color: Chūō–Sōbu (JB) | `#f5e119` | midpoint of the Akihabara photo's raw yellow `#ebee32` and the commonly cited `#ffd400` |
  | Ink | `#1a1a1a` | near-black |

- **Typefaces** (stand-ins, chosen by the user after comparing variants). A type researcher's
  survey of Kanto railway signage gives JR East's real fonts as **Shin Go B** for Japanese,
  **Helvetica Bold** for English and **Frutiger Bold** for station numbers. A JR East post on X
  backs up the Helvetica/Frutiger split. Shin Go and Frutiger are commercial fonts and aren't
  installed.
  - Japanese is **Hiragino Sans W7**, closer to Shin Go B than W6. Two exceptions use W5: the
    small kanji next to the main name, and the previous and next station names on the band. W5
    matches the photo's 4 pt stems on 御徒町; W7, W4 and W3 were compared.
  - English is **Helvetica Neue**. The station name is Bold. The neighbor names are **Regular**:
    the photo's stems measure about 4 pt on the neighbors against 8 pt on "Ueno". Long names are
    condensed with horizontal scale (`text.setFormat {hScale}`) to the photo's width. Don't use
    tracking for this, because tightening the spacing crowds the letters.
  - Badge text is **Hind** (`brew install --cask font-hind`, then `text.rescanFonts`), standing in
    for Frutiger. It uses three weights, as JR East's official numbering mockup does: the
    three-letter code in **Bold**, and the line letters ("JY", "JB") and the number in
    **SemiBold**. Rejected: Seravek (its J drops below the baseline), Source Sans 3 (shapes off, even
    with an outline added), Istok Web, Avenir Next, PT Sans, Helvetica Neue, and Hind with "JY"
    in Regular or Medium (too light).
  - Korean is **Apple SD Gothic Neo Regular**.
- **Station name block:**

  | Element | Font, size | Position (baseline) |
  |---|---|---|
  | 上 / 野 (one object per kanji) | W7, 131 | centered at x 665.5 and 919, baseline 135 |
  | Kana (うえの) | W7, 44, tracking 400 | centered on the axis, baseline 210.5 |
  | Chinese name, simplified (上野, 秋叶原) | W5, 40 | left 1042 on Ueno, baseline 67 |
  | Korean (우에노) | Apple SD Gothic Neo, 36, tracking 250 | left 1042, baseline 133 |
  | English name ("Ueno") | Helvetica Neue Bold, 60 | centered on the axis, baseline 398 |

  The small line next to the name is the **Chinese** name in simplified characters. On Ueno it
  happens to match the Japanese (上野), but Akihabara's is 秋叶原.

  For a three-kanji name, space the kanji 165 apart, centered on the axis (秋葉原: x 630, 795,
  960). Keep the photo's gaps: 66 from the badge's right edge to the first kanji's ink, and about
  68 from the last kanji's ink to the Chinese and Korean names. Tune the kana's tracking per
  station (400 for うえの, 45 for あきはばら).

- **Numbering badge (JY05):** a black `#1a1a1a` rounded rectangle at x 388, y 27.5, 155 × 185,
  radius 16. Inside it is a line-color square at (400, 71), 131 × 131, radius 8, with a white
  square inset 10 (radius 2). The three-letter code "UEN" is Hind Bold 45 in white, centered at
  x 465.5, baseline 64. Below it, the line letters and number split the white square's height
  **40/60**, each filling its zone with 7 pt of white above, between and below. "JY" is Hind
  SemiBold 50.8 at baseline 121.9 (ink 34 tall), and "05" is Hind SemiBold 84.1 at baseline 185
  (ink 56 tall), both centered at x 465.5. Chosen over the earlier small "JY" with a Bold
  number, a 45/55 split, and 40/60 with 10 pt margins.
  Earlier, the user compared this badge with geometry scaled from Wikimedia's JR numbering artwork
  (JY17, JB26): a thicker 13 pt frame, rounder corners, sharp white corners, and larger letters
  over a smaller number. They kept the current badge.
- **Fare-zone marks** (top right): 山 (Yamanote-line area) is an outlined box. It has a white fill
  with a 5 pt black stroke, outer edge x 1370–1441 and y 20–88, radius 5, and a black W7 52 山
  centered at x 1405.5, baseline 74. 区 (Tokyo wards area) is solid: a black box at x 1461–1532,
  y 20–88, radius 7, with a white W7 52 区 centered at x 1496.5, baseline 74. Which marks appear
  depends on the station.
- **Neighbors:**

  | Element | Font, size | Position (baseline) |
  |---|---|---|
  | Previous station, Japanese (white, on the band) | W5, 52, tracking 125 | left 66, baseline 310 |
  | Next station, Japanese (white, on the band) | W5, 72, tracking 250 | centered at x 1313, baseline 314 |
  | Previous station, English | Helvetica Neue Regular, 50, hScale fitted (96.5% for Okachimachi) | **left ink edge aligned with the Japanese name's left ink edge** (measure it at 4× and nudge), baseline 397 |
  | Next station, English | Helvetica Neue Regular, 52, hScale fitted (96% for Uguisudani) | right-aligned at 1411, baseline 397 |

  The next station's number badge sits after its English name. It's a white rounded square,
  x 1431.5–1498.5 and y 344.5–410.5, with a 5 pt line-color stroke and radius 5. Inside it is
  the same 40/60 split, scaled to the smaller box: "JY" is Hind SemiBold 27.9 at baseline 369.45
  and "06" is Hind SemiBold 46.2 at baseline 404.15, both centered at x 1465. The previous station has no badge on this sign.

The route band is JR East's dark green on **every** line. The Akihabara (JB) sign confirms it,
so only the current-station block and the badge borders take the line color.

Still open for JR East signs: the palette review and the frame.

### Kaohsiung Metro: entrance sign

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

### Prague tram (DPP / PID): direction sign

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

### Paris RATP: Métro and RER entrance sign

First pass from the rectified Gare de Lyon photo. Use the photographed legacy sign, not a
current wayfinding template. Measurements are in pt.

- **Face:** plain 1546.37 × 213 rectangle. The white `#ffffff` route badge panel is 364 wide;
  the rest is navy `#11172c`. No metal frame or reflections.
- **Name:** white Parisine Bold 139 at natural width, x 410 and baseline 158. If Parisine
  is unavailable, manually use Source Sans 3 Bold 148 at 95.5% horizontal scale.
- **Route badges:** two rows centered at y 57 and 156, with column centers x 84, 182,
  and 280. The visible margins are 40.25 pt on both sides and 13.25 pt above and below.
  Circles are 82 across before the 5.5 pt stroke on outlined badges. The photographed
  arrangement is RER, A, D above M, 1, 14. Use Parisine Regular 39.5 for RER (83% horizontal
  scale) and Parisine Regular 60 for A, D, and M, all with a 1.5 pt same-color outline
  with round joins. Use Parisine Bold 65 for the numbers. Both
  numerals are at natural width; “14” uses −124 tracking for a visible gap just under
  4 pt.
- **RATP plaque:** teal `#006b5b`, flush right, from x 1320 to 1546.37 and y 43 to 175.
  The white legacy lockup follows the symbol and wordmark proportions in the photo.
  The wordmark has sharp corners and no stroke. The lockup has 25.67 pt of teal on each
  side, measured from the left edge of the symbol and right edge of the wordmark.

The colors are first-pass estimates from the reference, not official paint values.

### Nice Lignes d’Azur: bus shelter header

First pass for the Garibaldi panel. Use the sharper, rectified photo for geometry and the
brighter photo for the palette; the bright photo is too soft to determine exact inks.
Coordinates are in pt.

- **Face:** white `#ffffff`, 1600 × 500, with a full-width sky-blue `#a0d0f8` strip from
  y 0 to 62. Leave the large blank area to the right of the title and route tiles.
- **Text:** NICE is dark gray `#56565f`, Helvetica Neue Regular 47 at 116% horizontal
  scale, x 19, baseline 48. The stop name is navy `#263c61`, Helvetica Neue Medium 178
  at 92.75%, x 26, baseline 225. Both styles stand in for the photographed lettering.
- **Route tiles:** plain filled rectangles in one row at y 272, 88 high, with centered
  white Arial Rounded MT Bold labels. Use the station's notes for tile colors and widths.
- **Logo:** orange and yellow two-line Lignes d’Azur wordmark at the upper right,
  crossing the strip and white face. The photo does not show a contrasting logo panel.

### Singapore MRT: station name sign

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
