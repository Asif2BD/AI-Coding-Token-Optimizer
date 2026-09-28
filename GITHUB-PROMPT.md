# GitHub adoption prompt — any repository-capable AI agent

## One sentence

> Read https://proskills.md/downloads/ai-coding-token-optimizer/1.1.0/SKILL.md and apply its project-mapping workflow to this project, preserving existing instructions and application code.

No skill installation is required. The agent must be able to read this repository and edit the target project. If links cannot be opened, paste the standalone prompt below.

## Standalone prompt

Make this repository cheap for an AI agent to work in. Change documentation only, never application behaviour.

1. **Measure.** Record the byte size of every instruction file this agent loads at session start (AGENTS.md, CLAUDE.md, and anything they import). Read them fully, then inspect the real project tree, its existing indexes and `git status`.
2. **Slim the entry point.** Keep only what binds every task: purpose, read-first, hard and security rules, branch and PR workflow, core commands, "when you are about to X, do Y" reflexes, and a Project map section. Move reference material verbatim into the guide or router that owns its topic: source trees, env-var tables, CI walkthroughs, deploy and server layouts, gotchas, and one area's style rules. Aim for about 8 KB or less, and never weaken a rule.
3. **Write routers as tables.** Put `docs/map/PRODUCT.md` (code area → its README router → its design doc), `OPERATIONS.md` (local setup, checks before a PR, CI triggers, preview and production deploy, what ships, rollback, health, config and secret *names*, external services, release) and a docs map in `docs/map/`, plus a short README router beside each code area. Keep each to about 15–35 lines, verified against the code, with no secrets, private hosts or machine paths.
4. **Install upkeep rules in the entry point.** Read the router for the task first, then only the files it links. A change that adds, moves or removes a routed file updates that router in the same change. A new area gets its own README router. Reference material goes in docs/, not the entry point. If both AGENTS.md and CLAUDE.md are used, make one a pointer to the other and to the same routers.
5. **Repoint.** Search the repository for mentions of moved sections ("see CLAUDE.md § …") in comments, scripts, workflows and skills, and point each at its new home.
6. **Verify.** Confirm that every backticked term and link from the old entry point still appears somewhere, and restore what is missing. Check that every relative link and anchor resolves, and review the diff for weakened rules and sensitive details.
7. **Report.** Give the before and after sizes, the files changed, the validation results and any uncertainty. Do not commit, push, merge or deploy unless asked. If this has been run before, refresh the existing maps rather than creating duplicates.
