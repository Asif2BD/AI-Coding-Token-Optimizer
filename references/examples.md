# Mapping patterns

These are illustrative only. Verify every path in the actual project before using it.

## Small project

Add a short Project map section to the existing entry point, linking its source entry point, tests and release guide. If the entry point is already small, stop there. Don't add three documents just to fill a template.

## Service with an oversized entry point (the common case)

A Node/TypeScript service with an account app and a staff console had a 39 KB `CLAUDE.md`, which is about 10,000 tokens loaded in every session. It held:
- a 100-line source tree
- the CI walkthrough
- an env-var table
- the production box layout
- a gotcha list
- the UI design rules

Adding maps on top of that file would have saved nothing on the always-loaded cost. The fix:

- `CLAUDE.md` went from 39 KB to 6.3 KB. It now holds the hard rules, workflow, commands, reflexes and the Project map, with its upkeep rules.
- `AGENTS.md` became a short pointer to the same routers.
- `docs/map/PRODUCT.md`, `OPERATIONS.md` and `DOCS.md` are task tables.
- `src/README.md`, `app/README.md` and `admin/README.md` replaced the source tree. The UI design rules moved into `app/README.md`, so they load only for UI work.
- The CI walkthrough, env vars, box layout and gotchas moved verbatim into `docs/guides/`.
- Six comments and scripts that said "see CLAUDE.md § …" were repointed.
- The no-loss check found a handful of dropped specifics (brand colour values, a service name, a git command). They were restored.

## Monorepo

Give each package its own entry point and routers. The root entry point stays small: shared rules, plus a router table of packages that links each package's entry point and the shared operations map. Avoid one giant inventory of every file.

## Existing work

Check `git status` first and preserve unrelated changes. On a rerun, measure again, update the existing routers and report the change. Don't create a second set of maps.
