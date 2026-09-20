# AI Coding Token Optimizer — ClawHub description

Version: 1.0.1
Slug: ai-coding-token-optimizer

## Stop making your agent rediscover your project

For a small change, an AI agent may first search folders, open unrelated files and reread documentation just to work out where the change belongs. Repeating that exploration across tasks uses time and context that could go toward the actual work.

**AI Coding Token Optimizer gives your agent a short, maintained map of the project.** It shows where important code, content and procedures live, so the agent can start in the right area and read what the task needs. It is designed to reduce repeated searching, unnecessary context loading and time spent getting oriented—not to replace understanding the code.

**For ChatGPT Codex, Claude Code, OpenClaw and any other AI agent with project-file access.** OpenClaw is one supported environment, not a requirement. A chat-only assistant needs a connected project or uploaded files; no prompt can grant access on its own.

## What it creates

```text
Your existing agent instructions
(AGENTS.md, CLAUDE.md, or your agent’s established entry point)
  └── Project Map
      ├── CONTENT.md     → content sources and publishing guidance
      ├── PRODUCT.md     → application code, components and tests
      └── OPERATIONS.md  → build, deployment and recovery procedures
```

These are examples, not a mandatory folder layout. A small project may need just one Map section. A monorepo may use package-level maps. The skill reuses good existing indexes instead of adding clutter.

Each map is a short Markdown document with links and a sentence explaining each destination. It does not move your application files, duplicate the documentation or change application routing.

**Example:** for “change the checkout button,” the agent reads the product map, follows its component and test links, and inspects those files. It still searches and reads more when the map is incomplete or the task requires it.

## Install and use

`clawhub install ai-coding-token-optimizer`

Then ask: “Use AI Coding Token Optimizer to map this project.”

ClawHub is a distribution option, not an OpenClaw-only dependency. For agents without ClawHub, use the GitHub adoption prompt or their supported skill installer.

## Agent guidelines

Follow SKILL.md: inspect the chosen project, reuse existing indexes, preserve mandatory instructions and source code, write concise maps, validate links and report documentation changes. Update maps when paths change. No project scripts, external publishing or secret reading is authorized by mapping.

## Expectations

The first mapping pass uses normal agent context. Later tasks may benefit from less repeated exploration; no numerical savings or speed guarantee is claimed. Host discovery of project instructions varies.

## Related projects

OpenClaw Token Optimizer audits runtime settings; this skill maps coding projects. MissionDeck.ai offers optional agent coordination. Find more skills at ProSkills.md. None is required to use this package.
