# Design system

## Visual thesis

Make research legible before making it decorative. Use a pale blue-gray field, navy hierarchy, one blue or teal emphasis, and generous white space. The system should feel academic, calm, and editable.

## Tokens and grid

`tokens.json` is the source of truth. A 0.5 inch outer margin and 0.28 inch gutters create a 12-column mental grid on a 13.333 × 7.5 inch canvas. Cards align to that grid and should not crowd the footer.

## Typography and spacing

Titles are 30 pt, section labels 18 pt, subtitles 17 pt, body 14 pt, small labels 10 pt, and metrics 26 pt. Use Aptos or Arial. Prefer fewer words over smaller type. Use spacing tokens consistently: compact card padding, visible section gaps, and a quiet footer.

## Color usage

Navy carries headings and primary anchors. Blue supports secondary anchors and timeline nodes. Teal marks one active state or key takeaway. Muted text supports explanatory copy. White is reserved for editable surfaces. Lines are low-contrast separators, not decoration.

## Card rules

Use white rounded cards with a thin line and very restrained shadow. Cards group content that belongs together. Keep one main idea per card, with a short label and clear body hierarchy. Avoid dense dashboard grids.

## Footer and page numbering

Use a small lab or meeting label at lower left and a rounded page badge at lower right. Page numbers are two digits. Keep footer elements quiet and consistent.

## Data and figures

Figures should be editable when possible and should include a plain-language takeaway. Placeholder art is abstract only. Add source notes and uncertainty where relevant. Never imply a result from a decorative placeholder.

## Accessibility

Maintain strong navy-on-light contrast, do not use color alone to encode meaning, keep labels descriptive, preserve reading order, and use at least 14 pt body text. Supply alt text and source notes when replacing placeholders with figures.

## Do / don't

- Do use one accent color for emphasis; don't use a rainbow palette.
- Do align cards to the grid; don't float disconnected panels.
- Do write direct topic titles; don't use slogans or filler narration.
- Do keep figures and labels editable; don't paste screenshots when a native object works.
- Do supply official logos yourself; don't assume the library includes institutional branding.
