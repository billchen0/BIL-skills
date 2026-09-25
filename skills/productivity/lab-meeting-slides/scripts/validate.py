#!/usr/bin/env python3
"""Dependency-free structural checks for the HTML slide system."""
from pathlib import Path
import re, sys
ROOT = Path(__file__).resolve().parents[1]
required = ['SKILL.md','DESIGN.md','README.md','design-system/index.html','design-system/tokens.css','design-system/components.css','design-system/slides.css','slides/example-lab-meeting.html','slides/slide-formats.js']
formats = ['Title','Section divider','Research update','Methods / workflow','Results + takeaway','Comparison','Timeline / next steps','Discussion / decision','Closing','Profile timeline']
def main():
    errors=[]
    for f in required:
        if not (ROOT/f).exists(): errors.append(f'missing {f}')
    deck=(ROOT/'slides/example-lab-meeting.html').read_text() if (ROOT/'slides/example-lab-meeting.html').exists() else ''
    index=(ROOT/'design-system/index.html').read_text() if (ROOT/'design-system/index.html').exists() else ''
    tokens=(ROOT/'design-system/tokens.css').read_text() if (ROOT/'design-system/tokens.css').exists() else ''
    if len(re.findall(r'class="slide-stage',deck)) < 9: errors.append('example deck has fewer than 9 slide stages')
    if not ('1920px' in tokens and '1080px' in tokens and '16 / 9' in tokens): errors.append('fixed stage tokens missing')
    registry=(ROOT/'slides/slide-formats.js').read_text() if (ROOT/'slides/slide-formats.js').exists() else ''
    for name in formats:
        if name not in index and name not in registry: errors.append(f'missing format {name}')
    for label in ['Overview','Foundations','Components','Slides','Assets / usage']:
        if label not in index: errors.append(f'missing tab {label}')
    for path in ROOT.rglob('*'):
        if path.is_file() and path.suffix.lower() in {'.html','.css','.js','.md','.py','.json'}:
            text=path.read_text(errors='ignore').lower()
            if ('python-pptx' in text or '.pptx' in text or 'build_template.py' in text or 'render_previews.py' in text) and path.name not in {'SKILL.md','README.md','validate.py'}:
                errors.append(f'stale PowerPoint/PPTX reference: {path.relative_to(ROOT)}')
    if errors:
        print('VALIDATION FAILED'); print('\n'.join(f'- {e}' for e in errors)); return 1
    stages = len(re.findall('class="slide-stage', deck))
    print(f'OK: {len(required)} required files, {stages} slide stages, fixed 1920x1080 tokens, tabs, and {len(formats)} formats verified.')
    return 0
if __name__ == '__main__': sys.exit(main())
