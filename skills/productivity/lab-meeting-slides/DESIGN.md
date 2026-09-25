# Lab meeting HTML design-system contract

## Visual thesis

Calm academic biomedical-research communication: pale blue-gray canvas, dark navy hierarchy, blue milestones, teal active/current emphasis, white rounded surfaces, cool-gray lines, restrained shadows, neutral sans-serif typography, generous whitespace, and a horizontal trajectory motif. The system should feel like an inspectable design-system tool.

## Exact starting tokens

| Semantic token | Value |
|---|---|
| canvas | `#F7F8FC` |
| navy | `#08255B` |
| blue | `#0D5D8C` |
| teal | `#16A6A1` |
| muted | `#5E6B82` |
| line | `#CBD4E1` |
| surface | `#FFFFFF` |

These live in `design-system/tokens.css` with the type scale, spacing, radii, shadow, fixed-stage, and timeline geometry tokens.

## Typography and spacing

Use the neutral system sans stack. The scale is 112px hero, 72px slide title, 48px section title, 34px body, 28px small body, and 22px metadata. Use an 8px spacing unit, 12/20/32px radii, and restrained shadows. Body copy should usually be at least 28px on a 1920px stage.

## Fixed stage and responsive behavior

Every slide is a fixed `1920px × 1080px` stage with a 16:9 ratio. The outer workspace and deck viewport may reflow and scale. Slide content scales uniformly as a whole; it must not reflow into mobile columns or change internal geometry.

## Component anatomy

Shared classes cover slide shell, top badge, title block, avatar/profile area, role badge, logo card/cluster, timeline rail/node, step badge, section label, headings, body/list, callout, metric, figure placeholder, comparison columns, and footer/page number. Add a component only when it is reusable and semantic.

## Slide-format registry

`slides/slide-formats.js` registers Title, Section divider, Research update, Methods / workflow, Results + takeaway, Comparison, Timeline / next steps, Discussion / decision, Closing, and Profile timeline with purposes and source class hooks. The Slides tab in `design-system/index.html` is the canonical layout gallery; the example deck uses the same hooks.

## Accessibility and motion

Use semantic headings, landmark navigation, meaningful `aria-label`s, keyboard-accessible tabs, and keyboard deck navigation. Never communicate status with color alone. Deck switching uses opacity, visibility, and pointer-events rather than `display:none`. Respect `prefers-reduced-motion: reduce`.

## Content density

One dominant idea per slide. Prefer one short paragraph, three to five bullets, or one figure plus one takeaway. Use explicit labels such as “Current focus” and “Decision needed”. Keep examples generic and use abstract placeholders rather than fabricated data.

## Do / don't

Do use tokens, shared classes, direct titles, whitespace, and a clear next action. Add approved lab assets only in consuming projects.

Don't add personal photos, employer or institutional marks, fake data, dashboard-like decoration, dense prose, or arbitrary colors. Don't create PowerPoint/PPTX artifacts: HTML is the target medium unless a user separately requests an export.
