---
name: lab-meeting-slides
description: Build and reuse an HTML-first design system and fixed-stage slide template library for lab meetings.
disable-model-invocation: false
argument-hint: "What lab-meeting HTML slide or format should we create?"
---

# Lab meeting slides

Use this skill to create HTML slide decks that share the central design system in `design-system/`. The canonical reference is `design-system/index.html`, especially its Slides tab.

## Workflow

1. Read `DESIGN.md`, `design-system/tokens.css`, `design-system/components.css`, `design-system/slides.css`, and `slides/slide-formats.js`.
2. Reuse semantic tokens, components, and registered format hooks. Add new formats to the registry before inventing layout classes.
3. Create fixed `1920px × 1080px` `.slide-stage` elements. Scale the stage uniformly to the viewport; never reflow slide content responsively.
4. Keep content generic and placeholder-first. Consuming labs provide approved data, logos, citations, figures, and photos.
5. Use opacity/visibility/pointer-events for deck navigation, preserve reading order, provide labels and keyboard navigation, and honor reduced-motion preferences.
6. Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v` before delivery.

The final medium is HTML. Do not create PowerPoint/PPTX files or use PowerPoint-specific libraries unless a user separately requests an export; PowerPoint is intentionally not the target medium for this skill.

## Design contract

- Use a 16:9 widescreen canvas.
- Preserve the light academic visual language: pale blue-gray canvas, deep navy hierarchy, blue secondary emphasis, teal active emphasis, white rounded surfaces, restrained borders, and generous whitespace.
- Treat the system as a communication aid, not a dashboard.
- Keep one dominant idea per slide and use direct titles.
- Prefer inspectable HTML/CSS primitives over pasted screenshots.
- Do not bundle personal data, portraits, employer logos, institutional marks, or confidential research data. Consuming labs provide their own approved assets.
- Do not use color alone to communicate status. Pair color with labels, position, or text.
- Keep normal body copy at 14 pt or larger and preserve reading order.

## Source of truth

- `design-system/index.html`: central workspace and canonical Slides gallery.
- `design-system/tokens.css`, `components.css`, `slides.css`: shared CSS sources.
- `slides/slide-formats.js`: slide format registry.
- `slides/example-lab-meeting.html`: generic reference deck.
- `DESIGN.md`: layout rules and component guidance.

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
10. Profile timeline (reference-derived)

## Verify

From this skill directory:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

## Extending the library

1. Add or revise semantic tokens first.
2. Add reusable component classes when a pattern appears in more than one slide.
3. Register the format in `slide-formats.js` and add it to the gallery and generic demo.
4. Validate structure and inspect both HTML pages at 16:9 before sharing.

## Asset and licensing boundary

This repository provides code and generic layout primitives. Official institutional logos, lab marks, figures, citations, photographs, and scientific data must be supplied by the consuming lab with the appropriate permissions.
