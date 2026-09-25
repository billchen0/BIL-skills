from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from lab_meeting_slides.library import build_template_deck, build_demo_deck

root=Path(__file__).resolve().parents[1]
build_template_deck(root/'templates/lab-meeting-slide-library.pptx')
build_demo_deck(root/'examples/lab-meeting-slide-library-demo.pptx')
print('Built template and demo decks')
