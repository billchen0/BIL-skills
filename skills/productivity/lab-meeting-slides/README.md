# Lab Meeting Slide Library

A reusable, open-source PowerPoint toolkit for lab meetings, research updates, methods discussions, and decisions. It carries a light academic visual language: pale blue-gray canvas, deep navy type, blue and teal accents, white rounded cards, restrained shadows, clear sans-serif hierarchy, and 16:9 widescreen slides.

## Quick start

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build_template.py
python3 -m pytest -q
python3 scripts/render_previews.py
```

Open `preview/index.html` locally for a visual catalog. Generated decks live in `templates/` and `examples/`.

## File map

- `src/lab_meeting_slides/library.py`: reusable python-pptx API and deck builders
- `tokens.json`: semantic design tokens
- `DESIGN.md`: visual and accessibility system
- `scripts/build_template.py`: builds the editable template and generic demo
- `scripts/render_previews.py`: optional LibreOffice rendering and contact sheet
- `preview/index.html`: self-contained visual reference
- `tests/test_library.py`: smoke coverage for all formats

## Supported slide formats

Title, section divider, research update, methods/workflow, results with figure and takeaway, comparison, timeline/next steps, discussion/decision, and closing. Components also cover title blocks, labels, footers, cards, pills, bullets, figure placeholders, callouts, timelines, metrics, columns, and chart insertion.

## Customize

Edit `tokens.json` to change semantic colors, sizes, spacing, radii, and shadow values. Pass a token dictionary to `Library(...)` or use the helper functions directly. Keep content generic in the library and supply lab-specific text, figures, logos, and citations in your own deck.

## Build

The module uses `python-pptx`, inches internally, and a built-in-font stack of Aptos with Arial fallback. The build script emits editable PowerPoint objects and a small abstract figure placeholder rather than fabricated scientific data.

## Licensing and asset notes

Code and documentation are released under the MIT License. The visual direction is an original generic adaptation of the supplied timeline reference. No personal content, portrait, employer logo, or institutional mark is bundled. Official institutional logos and lab-specific assets must be supplied and licensed by users.
