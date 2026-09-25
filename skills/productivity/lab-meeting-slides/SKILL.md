---
name: lab-meeting-slides
description: Build and reuse an editable PowerPoint library for lab meetings.
disable-model-invocation: false
argument-hint: "What lab-meeting slide or format should we create?"
---

# Lab meeting slides

Use this skill when creating, revising, or extending the shared lab-meeting PowerPoint system.

## Design contract

- Use a 16:9 widescreen canvas.
- Preserve the light academic visual language: pale blue-gray canvas, deep navy hierarchy, blue secondary emphasis, teal active emphasis, white rounded surfaces, restrained borders, and generous whitespace.
- Treat the system as a communication aid, not a dashboard.
- Keep one dominant idea per slide and use direct titles.
- Prefer editable PowerPoint primitives over pasted screenshots.
- Do not bundle personal data, portraits, employer logos, institutional marks, or confidential research data. Consuming labs provide their own approved assets.
- Do not use color alone to communicate status. Pair color with labels, position, or text.
- Keep normal body copy at 14 pt or larger and preserve reading order.

## Source of truth

- `tokens.json`: semantic colors, typography, spacing, radii, and shadow values.
- `DESIGN.md`: layout rules and component guidance.
- `src/lab_meeting_slides/library.py`: reusable `python-pptx` helpers and deck builders.
- `templates/`: placeholder-first editable deck.
- `examples/`: generic sample deck showing the same formats with sample content.
- `preview/index.html`: visual catalog of tokens, components, and formats.

## Supported formats

1. Title
2. Section divider
3. Research update
4. Methods / workflow
5. Results + takeaway
6. Comparison
7. Timeline / next steps
8. Discussion / decision
9. Closing

## Build and verify

From this skill directory:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build_template.py
python3 -m pytest -q
python3 scripts/render_previews.py
```

`render_previews.py` uses LibreOffice when it is installed. If it is unavailable, it exits cleanly and reports that PowerPoint rendering still needs a local LibreOffice pass.

## Extending the library

1. Add or revise semantic tokens first.
2. Add a reusable helper to `library.py` if the pattern appears in more than one slide.
3. Add the format to both the placeholder template and the generic demo.
4. Add a smoke test for slide count and build success.
5. Update `DESIGN.md`, the preview catalog, and this skill when the design contract changes.
6. Rebuild the decks and inspect the final PowerPoint at 16:9 before sharing.

## Asset and licensing boundary

This repository provides code and generic layout primitives. Official institutional logos, lab marks, figures, citations, photographs, and scientific data must be supplied by the consuming lab with the appropriate permissions.
