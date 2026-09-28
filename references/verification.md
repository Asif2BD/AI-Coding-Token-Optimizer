# Verification

Run these from the project root of a Git repository. They only read files. Before you edit anything, save a copy of each always-loaded file, for example `cp CLAUDE.md /tmp/CLAUDE.before.md`.

## Measure the always-loaded context

This counts the entry points (`CLAUDE.md`, `.claude/CLAUDE.md`, `AGENTS.md`) plus every file they import (`@path` lines, which Claude Code follows, including imports of imports). Run it before and after the change. Imports that resolve outside the project are listed but not read.

```python
import re, pathlib
root = pathlib.Path('.').resolve()
todo = [root / p for p in ('CLAUDE.md', '.claude/CLAUDE.md', 'AGENTS.md') if (root / p).is_file()]
seen, total = set(), 0
while todo:
    p = todo.pop().resolve()
    if p in seen: continue
    seen.add(p)
    if root not in p.parents or not p.is_file():
        print('not read (outside project or missing):', p); continue
    text = p.read_text(errors='ignore')
    total += len(text.encode())
    print(f'{len(text.encode()):>7}  {p.relative_to(root)}')
    body = re.sub(r'```.*?```|`[^`\n]*`', '', text, flags=re.S)  # imports in code are not imports
    todo += [p.parent / m for m in re.findall(r'(?<![\w/])@([\w./-]+\.\w+)', body)]
print(f'{total:>7}  total bytes, about {total // 4} tokens')
```

Nested instruction files that the host loads while working inside a subdirectory (such as `app/CLAUDE.md`) count for tasks in that area. Measure them the same way and report them separately.

## No-loss check

For each old always-loaded file, this lists every heading, backticked term and link destination that no longer appears in the project's documentation.

- Only Markdown that Git tracks, or that is new but not ignored, is read. Build output, virtual environments and ignored private files cannot satisfy the check.
- Symlinks and anything that resolves outside the root are skipped.
- Code examples are ignored on both sides, so a term that survives only inside an example doesn't count as kept.
- Relative links are compared by **destination**, resolved from the file that holds them. A link that moved into a nested guide and was rewritten (`docs/setup.md` → `../setup.md`) still counts as kept. External URLs are compared literally.

Restore anything listed, or name it in the report as deliberately dropped.

```python
import re, os, subprocess, pathlib
OLD, OLD_AT = '/tmp/CLAUDE.before.md', 'CLAUDE.md'   # saved copy, and where it lived
root = pathlib.Path('.').resolve()
listed = subprocess.run(['git', 'ls-files', '-co', '--exclude-standard', '--', '*.md'],
                        capture_output=True, text=True, check=True).stdout.splitlines()
def readable(rel):
    p = root / rel
    return p.is_file() and not p.is_symlink() and root in p.resolve().parents
docs = {rel: (root / rel).read_text(errors='ignore') for rel in listed if readable(rel)}
def prose(text):
    return re.sub(r'```.*?```', '', text, flags=re.S)
def destinations(src, text):
    out = set()
    for t in re.findall(r'\]\(([^)#\s]+)', prose(text)):
        external = '://' in t or t.startswith('mailto:')
        out.add(t if external else os.path.normpath(os.path.join(os.path.dirname(src), t)))
    return out
old = open(OLD).read()
corpus = ''.join(prose(t) for t in docs.values())
kept = set().union(set(), *(destinations(rel, text) for rel, text in docs.items()))
terms = set(re.findall(r'`([^`\n]{3,80})`', old)) | {h.strip() for h in re.findall(r'^#{1,6} +(.+)$', prose(old), re.M)}
lost = sorted(t for t in terms if t not in corpus) + sorted(d for d in destinations(OLD_AT, old) if d not in kept)
print('\n'.join(lost) or 'nothing lost')
```

## Links and anchors

Pass the files you touched as arguments. Code examples are ignored on both sides: a link inside an example is not checked, and a `# Heading` inside an example is not treated as an anchor. Anchors follow GitHub's slug rule, which lowercases the heading, drops punctuation and turns spaces into hyphens.

```python
import re, os, sys
root = os.path.realpath('.')
def inside(path):  # never read a symlink or anything outside the project
    return not os.path.islink(path) and os.path.realpath(path).startswith(root + os.sep)
def prose(path):
    return re.sub(r'```.*?```', '', open(path).read(), flags=re.S)
def slugs(path):
    return {re.sub(r'[^\w\- ]', '', l.lstrip('#').strip().lower()).replace(' ', '-')
            for l in prose(path).splitlines() if re.match(r'#{1,6} ', l)}
bad = 0
for f in sys.argv[1:]:
    for m in re.findall(r'\]\(([^)\s]+)\)', re.sub(r'`[^`\n]*`', '', prose(f))):
        if '://' in m or m.startswith('mailto:'): continue
        path, _, anchor = m.partition('#')
        t = os.path.normpath(os.path.join(os.path.dirname(f), path)) if path else f
        if not os.path.exists(t): print('missing', f, m); bad += 1
        elif not inside(t): print('outside project', f, m); bad += 1
        elif anchor and t.endswith('.md') and anchor not in slugs(t): print('anchor', f, m); bad += 1
print('broken:', bad)
```

## Stale references

```sh
git grep -n -e 'CLAUDE\.md' -e 'AGENTS\.md' -- ':!CLAUDE.md' ':!AGENTS.md'
```

Check every hit that names a section of the old entry point, and repoint it to where that section now lives.
