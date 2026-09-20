import unittest
from pathlib import Path
import re, hashlib
ROOT=Path(__file__).resolve().parents[1]
class PackageTests(unittest.TestCase):
 def test_links(self):
  for p in ROOT.rglob('*.md'):
   for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
    if '://' not in link and not link.startswith('#'):
     self.assertTrue((p.parent/link.split('#')[0]).exists(),str((p,link)))
 def test_integrity(self):
  for line in (ROOT/'SHA256SUMS.txt').read_text().splitlines():
   digest,path=line.split('  ',1)
   self.assertEqual(digest,hashlib.sha256((ROOT/path).read_bytes()).hexdigest())
 def test_license(self):
  self.assertEqual((ROOT/'LICENSE').read_bytes(),(ROOT/'LICENSE.txt').read_bytes())
  self.assertIn('MIT License',(ROOT/'LICENSE').read_text())
 def test_identity(self):
  s=(ROOT/'SKILL.md').read_text()
  self.assertIn('name: ai-coding-token-optimizer',s)
  self.assertIn('version: 1.0.1',s)
 def test_boundaries(self):
  s=(ROOT/'SKILL.md').read_text()
  for phrase in ['documentation-only','CLAUDE.md','AGENTS.md','symlinks','mandatory instructions','rather than creating duplicates']:
   self.assertIn(phrase,s)
 def test_no_machine_paths(self):
  for p in ROOT.rglob('*.md'):
   self.assertNotIn('/root/',p.read_text())
if __name__=='__main__': unittest.main()
