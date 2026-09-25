# Lab Meeting HTML Slide System

An HTML-first design-system workspace and fixed-stage slide template library for research and lab meetings. It generates HTML slides, not PowerPoint files.

## Quick start

```bash
npx skills@latest add billchen0/BIL-skills
```

Choose `lab-meeting-slides`. From this directory, run `python3 -m http.server 8000`, then open `http://localhost:8000/design-system/index.html` or `http://localhost:8000/slides/example-lab-meeting.html`. Direct file opening also works in modern browsers.

The Design System workspace is the visual catalog; the example deck is a functional generic reference.

## File map

- `design-system/tokens.css`, `components.css`, `slides.css`: shared design tokens and HTML classes
- `design-system/index.html`: central workspace and canonical Slides gallery
- `slides/slide-formats.js`: shared slide-format registry
- `slides/example-lab-meeting.html`: functional generic HTML deck
- `DESIGN.md`: visual and accessibility system
- `scripts/validate.py`: dependency-free validator
- `tests/test_structure.py`: structural tests

## Supported slide formats

Title, section divider, research update, methods/workflow, results with figure and takeaway, comparison, timeline/next steps, discussion/decision, closing, and profile timeline. Components also cover title blocks, labels, footers, cards, pills, bullets, figure placeholders, callouts, timelines, metrics, columns, and chart insertion.

## Customize

Edit the CSS custom properties and registry. Keep content generic in the library and supply lab-specific text, figures, logos, and citations in your own deck.

## Build

Slides use fixed 1920×1080 HTML stages that scale uniformly to the viewport. The design system is dependency-free.

## Licensing and asset notes

Code and documentation are released under the MIT License. The visual direction is an original generic adaptation of the supplied timeline reference. No personal content, portrait, employer logo, or institutional mark is bundled. Official institutional logos and lab-specific assets must be supplied and licensed by users.
