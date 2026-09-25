# BIL-skills

A small collection of reusable skills for Bill's research and lab workflows.

## Included skills

- [`lab-meeting-slides`](./skills/productivity/lab-meeting-slides/SKILL.md): create and reuse an HTML-first design system and fixed 16:9 HTML slide library for lab meetings, research updates, methods discussions, results, and decisions.

## Repository layout

This repository follows the category-and-skill layout used by the reference skills repository:

```text
skills/
  productivity/
    README.md
    lab-meeting-slides/
      SKILL.md
      agents/openai.yaml
      DESIGN.md
      design-system/
      slides/
      scripts/
      tests/
```

Each skill is self-contained. Read its `SKILL.md` first, then use its supporting files and scripts.

## Installation

To copy the skills into a project with the Skills installer:

```bash
npx skills@latest add billchen0/BIL-skills
```

Choose `lab-meeting-slides` when prompted. The root `skills/` layout is compatible with the Skills installer workflow.

## Development

The slide skill is intentionally local, editable, and dependency-free. Open `design-system/index.html` for the central workspace and Slides gallery, or `slides/example-lab-meeting.html` for a functional HTML deck. See the skill README for local usage and validation commands. PowerPoint/PPTX is intentionally not the target medium.

## License

MIT. See [`skills/productivity/lab-meeting-slides/LICENSE`](./skills/productivity/lab-meeting-slides/LICENSE).
