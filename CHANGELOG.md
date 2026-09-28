# Changelog

## v1.1.0 — 2026-09-28

- **Measure and slim the always-loaded entry point.** Record the bytes and estimated tokens of the always-loaded files. Keep the rules that bind every task, and move reference material verbatim into guides and routers. Report the before and after sizes.
- **Two-level routing.** `docs/map/` task tables, plus a README router beside each code area, which also carries that area's own rules.
- **An operations checklist** (`references/operations.md`) for CI triggers, what actually ships, rollback, health, config and secret names, and external services.
- **No-loss and link verification** (`references/verification.md`). Also repoints “see CLAUDE.md § …” references across the repository.
- **Proactive behaviour.** Adoption runs the full workflow. The upkeep rules written into the entry point keep later sessions maintaining the map, and agents offer the workflow when an entry point grows past its budget.
- **Templates** for the entry point, maps and area READMEs (`references/templates.md`), and a worked example of a 39 KB → 6.3 KB entry point.

## v1.0.2 — 2026-09-20

- Make ProSkills the primary homepage with hosted instructions and release downloads.

## v1.0.1 — 2026-09-20

- Explain the repeated-file-discovery problem and concrete map structure.
- Make onboarding agent-neutral and GitHub link-first, with standalone fallback.
- Separate registry guidance and clarify ongoing maintenance and benefits.


## v1.0.0 — 2026-09-20

- Rebrand user-supplied Workspace Map as AI Coding Token Optimizer.
- Add one-line adoption and host-aware AGENTS.md/CLAUDE.md guidance.
- Preserve documentation-only scope, targeted reading and idempotent updates.
- Add MIT license, security boundaries, examples and release integrity files.
