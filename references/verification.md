# Verification

Run these from the project root. They only read files. Save a copy of the old entry point before you edit it, for example `cp CLAUDE.md /tmp/CLAUDE.before.md`.

## Measure the always-loaded context

```sh
wc -c CLAUDE.md AGENTS.md 2>/dev/null   # tokens ≈ bytes ÷ 4; repeat after the change
```

## No-loss check

This lists every backticked term and link target in the old entry point that no longer appears in any Markdown file. Restore each one, or list it in the report as deliberately dropped.

```python
import re, pathlib
old = pathlib.Path('/tmp/CLAUDE.before.md').read_text()
docs = ''.join(p.read_text(errors='ignore') for p in pathlib.Path('.').rglob('*.md')
               if 'node_modules' not in p.parts and '.git' not in p.parts)
terms = set(re.findall(r'`([^`\n]{3,80})`', old)) | set(re.findall(r'\]\(([^)#\s]+)', old))
print('\n'.join(sorted(t for t in terms if t not in docs)) or 'nothing lost')
```

## Links and anchors

Pass the files you touched as arguments. Anchors use GitHub's slug rule: lowercase, punctuation removed, spaces turned into hyphens.

```python
import re, os, sys
def slugs(p):
    return {re.sub(r'[^\w\- ]', '', l.lstrip('#').strip().lower()).replace(' ', '-')
            for l in open(p) if l.startswith('#')}
bad = 0
for f in sys.argv[1:]:
    text = re.sub(r'`[^`\n]*`', '', re.sub(r'```.*?```', '', open(f).read(), flags=re.S))  # skip examples
    for m in re.findall(r'\]\(([^)\s]+)\)', text):
        if '://' in m or m.startswith('mailto:'): continue
        path, _, anchor = m.partition('#')
        t = os.path.normpath(os.path.join(os.path.dirname(f), path)) if path else f
        if not os.path.exists(t): print('missing', f, m); bad += 1
        elif anchor and t.endswith('.md') and anchor not in slugs(t): print('anchor', f, m); bad += 1
print('broken:', bad)
```

## Stale references

```sh
grep -rn "CLAUDE.md\|AGENTS.md" --exclude-dir=node_modules --exclude-dir=.git . | grep -v "^./CLAUDE.md\|^./AGENTS.md"
```

Check every hit that names a section of the old entry point.
