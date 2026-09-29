import unittest
from pathlib import Path
import re, hashlib
ROOT=Path(__file__).resolve().parents[1]
class PackageTests(unittest.TestCase):
 def test_links(self):
  for p in ROOT.rglob('*.md'):
   text=re.sub(r'```.*?```','',p.read_text(),flags=re.S)  # links inside examples are illustrative
   text=re.sub(r'`[^`\n]*`','',text)
   for link in re.findall(r'\]\(([^)]+)\)',text):
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
  self.assertIn('version: 1.2.0',s)
 def test_boundaries(self):
  s=(ROOT/'SKILL.md').read_text()
  for phrase in ['documentation-only','CLAUDE.md','AGENTS.md','symlinks','mandatory instructions','rather than creating duplicates','Nothing is sent automatically']:
   self.assertIn(phrase,s)
 def test_entry_point_workflow(self):
  s=(ROOT/'SKILL.md').read_text()
  for phrase in ['always-loaded','No-loss check','verbatim','Repoint','Keep the map true','budget']:
   self.assertIn(phrase,s)
  for ref in ['references/templates.md','references/operations.md','references/verification.md']:
   self.assertIn(ref,s)
 def test_versions_agree(self):
  for p in ['README.md','CLAWHUB.md','GITHUB-PROMPT.md','CHANGELOG.md']:
   self.assertIn('1.2.0',(ROOT/p).read_text(),p)
  self.assertIn('# Version: 1.2.0',(ROOT/'.clawhubsafe').read_text())
 def test_feedback_handoff(self):
  s=(ROOT/'references'/'feedback.md').read_text()
  for phrase in ['Nothing is sent automatically','Do not submit it automatically','source code','secrets','ProSkills','ClawHub']:
   self.assertIn(phrase,s)
 def test_verification_snippets_compile(self):
  text=(ROOT/'references'/'verification.md').read_text()
  blocks=re.findall(r'^```python\n(.*?)^```$',text,re.S|re.M)
  self.assertGreaterEqual(len(blocks),3)
  for b in blocks:
   compile(b,'verification.md','exec')
 def test_no_machine_paths(self):
  for p in ROOT.rglob('*.md'):
   self.assertNotIn('/root/',p.read_text())
if __name__=='__main__': unittest.main()
