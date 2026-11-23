# station-signs

Vector recreations of train station signs that mean something to me, from rail systems around
the world. They're built in **VectorCraft**, with an AI agent drawing live in the app.

## Stations

| Sign | Station | City, Country | Visited |
|---|---|---|---|
| <a href="stations/ueno/"><img src="stations/ueno/ueno.png" alt="Ueno, station name sign" width="240"></a> | [Ueno](stations/ueno/) | Tokyo, Japan | Mar 2026 |
| <a href="stations/phrom-phong/"><img src="stations/phrom-phong/phrom-phong.png" alt="Phrom Phong, Platform 2 sign" width="240"></a> | [Phrom Phong](stations/phrom-phong/) | Bangkok, Thailand | Apr 2026 |
| <a href="stations/ujezd/"><img src="stations/ujezd/ujezd.png" alt="Újezd tram direction sign" width="240"></a> | [Újezd](stations/ujezd/) | Prague, Czechia | Aug 2026 |
| <a href="stations/gare-de-lyon/"><img src="stations/gare-de-lyon/gare-de-lyon.png" alt="Gare de Lyon Métro and RER entrance sign" width="240"></a> | [Gare de Lyon](stations/gare-de-lyon/) | Paris, France | Aug 2026 |
| <a href="stations/akihabara/"><img src="stations/akihabara/akihabara.png" alt="Akihabara, station name sign" width="240"></a> | [Akihabara](stations/akihabara/) | Tokyo, Japan | Sep 2026 |
| <a href="stations/formosa-boulevard/"><img src="stations/formosa-boulevard/formosa-boulevard.png" alt="Formosa Boulevard, Entrance 1 sign" width="240"></a> | [Formosa Boulevard](stations/formosa-boulevard/) | Kaohsiung, Taiwan | Oct 2026 |

## Requirements

- VectorCraft 0.24.1 (desktop app) and `vectorcraft-cli`
- [uv](https://docs.astral.sh/uv/) for the occasional Python helper (image measuring and color
  sampling)
- Whatever fonts a sign's design spec calls for. The Bangkok BTS signs use Thonburi and Helvetica
  Neue, which come with macOS. The JR East signs use Hiragino Sans, Helvetica Neue and Apple SD Gothic
   Neo (also built in), plus Hind (`brew install --cask font-hind`). The Kaohsiung Metro sign uses
    Songti TC, Hiragino Sans GB, and Arial. The Prague tram and Paris RATP signs use
    Source Sans 3; the RATP sign also uses Helvetica Neue.

## Working on a sign

1. Start VectorCraft with its control server:

   ```sh
   open -a VectorCraft --args --control 7979
   ```

2. Open this folder in Claude Code (or another agent) and approve the `vectorcraft` MCP server
   from `.mcp.json` when asked.
3. Open a station's `.vectorcraft` file, or ask for a new one, and describe what you want. The
   agent draws in your VectorCraft window, so you can watch and edit alongside it. For
   subjective tweaks it lays out numbered variants on extra artboards for you to choose from.

## Exporting

```sh
mkdir -p stations/phrom-phong/exports
vectorcraft-cli convert stations/phrom-phong/phrom-phong.vectorcraft stations/phrom-phong/exports/phrom-phong.pdf
```

The output format follows the file extension (`.svg`, `.pdf`, `.png`, and so on). For PNGs, add
`--ppi 300`.

## Notes

These are personal, fan-made recreations, not official artwork from any rail operator. Where an
operator publishes no typeface or color specification, the fonts are stand-ins and the colors
were matched from photos. The sources are recorded in the `AGENTS.md` files.
