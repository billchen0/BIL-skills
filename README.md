# BIL-skills

A small collection of reusable skills for Bill's research and lab workflows.

## Included skills

- [`lab-meeting-slides`](./skills/productivity/lab-meeting-slides/SKILL.md): create and extend an editable PowerPoint slide library for lab meetings, research updates, methods discussions, results, and decisions.

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
      tokens.json
      src/
      scripts/
      templates/
      examples/
      preview/
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

The slide skill is intentionally local and editable. It uses `python-pptx` and Pillow, with no external data or credentials. See the skill README for installation and build commands.

## License

MIT. See [`skills/productivity/lab-meeting-slides/LICENSE`](./skills/productivity/lab-meeting-slides/LICENSE).
