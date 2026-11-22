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
- `AGENTS.md`: this file. It holds guidance shared by every station, plus one design spec per
  rail system.
- `.mcp.json`: registers the `vectorcraft` MCP server (live mode)
- `stations/<station-slug>/`: one folder per station, for example `stations/phrom-phong/`. Each
  holds:
  - `<station-slug>.vectorcraft`: the source file. It holds **exactly one sign** on one artboard.
    Extra artboards only exist temporarily while comparing variants, and get deleted once the
    user picks one.
  - `<station-slug>.png`: a small preview, exported with
    `vectorcraft-cli convert <slug>.vectorcraft <slug>.png --scale 0.5`, which gives an
    810 × 210 px image for a BTS sign. The station README shows it full size, and the root
    README's table shows it as a 240 px thumbnail.
    **Re-export it whenever the sign changes.**
  - `README.md`: a short overview for people, with the station name in English and the local
    script, the city and country, line, code and neighbors, when the user visited, which sign it
    is (for example "Platform 2"), an export command and brief design notes. Keep it simple, with
    no signs table. The full decision log goes in `AGENTS.md`, not here.
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
