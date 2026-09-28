# Adoption by host

Install this package using your client’s supported skill mechanism. Do not overwrite an existing installation without reviewing it.

- Codex: use its skill installer or configured skill directory; invoke AI Coding Token Optimizer once the host lists it. A repository AGENTS.md map provides ongoing navigation independently of skill invocation.
- Claude Code: use the host’s supported project or user skill directory. Link shared project maps from existing CLAUDE.md when that is its instruction entry point. Do not assume it automatically reads AGENTS.md.
- OpenClaw: install through ClawHub, then ask the agent to use AI Coding Token Optimizer in a named repository. Workspace access must already exist.
- Other clients: paste the standalone GITHUB-PROMPT.md instructions into a repository-capable agent.

One-line request after installation:

> Use AI Coding Token Optimizer to map this project, preserve existing instructions, and make documentation-only changes.

For maintenance: “Refresh this project’s AI Coding Token Optimizer maps against the current repository.”

Adoption is proactive. “Adopt this skill” means running the whole workflow in [SKILL.md](../SKILL.md):
1. Measure.
2. Slim the entry point.
3. Write the routers.
4. Repoint references.
5. Verify.
6. Report.

It does not mean a questionnaire or a partial pass. The upkeep rules it writes into the entry point keep later sessions maintaining the map, even in clients where the skill isn't installed.

Only the current project is in scope unless the user names another. Do not edit global configuration, add background jobs or install another model. A prompt cannot grant filesystem access or guarantee an agent loads the map.
