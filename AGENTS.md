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
design spec, built from that system's reference photos (see "Sign design specs" below).

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
  - **Sign:** a thumbnail of the station's SVG, linked to its folder:
    `<a href="stations/<slug>/"><img src="stations/<slug>/<slug>.svg" alt="…" width="240"></a>`
  - **Station:** the station name, linked to its folder.
  - **Visited:** a short month and year, for example "Apr 2026". Ask the user when they visited;
    don't guess.
  - Keep the rows in order of visit, earliest first, and insert a new station where its date falls.
- `AGENTS.md`: this file. It holds guidance shared by every station, and an index of the rail
  system specs.
- `.mcp.json`: registers the `vectorcraft` MCP server (live mode)
- `stations/<station-slug>/`: one folder per station, for example `stations/phrom-phong/`. Each
  holds:
  - `<station-slug>.vectorcraft`: the source file. It holds **exactly one sign** on one artboard.
    Extra artboards only exist temporarily while comparing variants, and get deleted once the
    user picks one. Its File Info title (`file.info {title}`) and its artboard name are both
    "Station – sign", with an en dash and no line code, for example "Rochor – station name sign"
    or "Phrom Phong – Platform 2 sign". The title becomes the SVG's `<title>`.
  - `<station-slug>.svg`: the preview, exported with
    `vectorcraft-cli convert <slug>.vectorcraft <slug>.svg --outline-text`. The text is converted
    to outlines so it looks right without the sign's fonts, including on GitHub. The station
    README shows it full width, and the root README's table shows it as a 240 px thumbnail.
    There's no PNG preview: the user chose SVG only, since it stays sharp at any size.
    **Re-export it whenever the sign changes.**
  - `README.md`: a short overview for people, with the station name in English and the local
    script, the city and country, line, code and neighbors, when the user visited and who with
    (one line, for example "Visited in March 2026 with Clark and Paul."; ask, don't guess), which
    sign it is (for example "Platform 2") and brief design notes. Keep it simple, with no signs
    table. The full decision log goes in `AGENTS.md`, not here.
  - `AGENTS.md`: station-specific facts (names, codes, neighbors, platforms, the reference
    photos used, decisions and open questions) and, for the first station on a rail system,
    that system's design spec. Plus a `CLAUDE.md` containing `@AGENTS.md`
  - `exports/`: rendered SVG, PDF and PNG files (create when needed)

Put working practices shared by every station in this file. Put each rail system's design spec,
and anything specific to one station, in a station's `AGENTS.md`. When starting a new station,
copy the folder structure of an existing station, but not its design. Each station's `AGENTS.md`
should say which rail system and spec it uses. Use the station's common English name for the
slug. If two stations would get the same slug, add the city, for example `stations/ueno-tokyo/`.

## Sign design specs (one per rail system)

Each rail system's design spec lives in the `AGENTS.md` of the station it was built from, under
"Design spec: …". A station on a system that already has a spec points to that file instead of
copying it (Akihabara uses Ueno's JR East spec). When a decision applies to every station on a
system, record it in that spec.

| System | Spec |
|---|---|
| Bangkok BTS Skytrain | [`stations/phrom-phong/AGENTS.md`](stations/phrom-phong/AGENTS.md) |
| JR East | [`stations/ueno/AGENTS.md`](stations/ueno/AGENTS.md) |
| Kaohsiung Metro | [`stations/formosa-boulevard/AGENTS.md`](stations/formosa-boulevard/AGENTS.md) |
| Prague tram (DPP / PID) | [`stations/ujezd/AGENTS.md`](stations/ujezd/AGENTS.md) |
| Paris RATP | [`stations/gare-de-lyon/AGENTS.md`](stations/gare-de-lyon/AGENTS.md) |
| Nice Lignes d’Azur | [`stations/garibaldi/AGENTS.md`](stations/garibaldi/AGENTS.md) |
| Singapore MRT | [`stations/rochor/AGENTS.md`](stations/rochor/AGENTS.md) |

When starting a station on a new system, write its spec in that station's `AGENTS.md`, built
from straight-on reference photos, the way the BTS spec was. Ask the user for photos if there
aren't any.
