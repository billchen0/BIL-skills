import unittest, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / 'scripts'))
import validate
class StructureTests(unittest.TestCase):
    def test_validator(self): self.assertEqual(validate.main(), 0)
    def test_deck_has_nine_stages(self): self.assertGreaterEqual((validate.ROOT/'slides/example-lab-meeting.html').read_text().count('class="slide-stage'), 9)
    def test_required_tabs(self):
        text=(validate.ROOT/'design-system/index.html').read_text()
        for label in ['Overview','Foundations','Components','Slides','Assets / usage']: self.assertIn(label,text)
if __name__ == '__main__': unittest.main()
