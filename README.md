# AI Coding Token Optimizer

[![Version](https://img.shields.io/badge/version-1.0.1-brightgreen.svg)](CHANGELOG.md)
[![MissionDeck](https://img.shields.io/badge/MissionDeck-ai-blueviolet)](https://missiondeck.ai)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.txt)

**A project map for your AI agent. Less rediscovery. More focused work.**

Created by M Asif Rahman · Built by [MissionDeck.ai](https://missiondeck.ai)

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

## Get started with any coding agent

1. Open the project you want to optimize in your usual AI agent.
2. Give the agent access to this repository’s instructions and your project files.
3. Paste this one-sentence request:

> Read https://github.com/Asif2BD/AI-Coding-Token-Optimizer and apply its project-mapping workflow to this project, preserving existing instructions and application code.

The agent inspects your project, creates or refreshes appropriate maps, connects them to its existing project instructions, and checks the links. Review the resulting documentation diff. Then continue asking for your normal project changes—the entry point tells the agent where to start.

**If your agent cannot open GitHub links:** copy the standalone instructions in [GITHUB-PROMPT.md](GITHUB-PROMPT.md) into the agent instead. You do not need to install a skill, use Git commands or create another repository merely to adopt the approach.

## Prefer installing a skill?

For an agent with ClawHub support:

```sh
clawhub install ai-coding-token-optimizer
```

Then say: **“Use AI Coding Token Optimizer to map this project.”**

Other clients can use their own supported skill installer with this repository. Installation locations and discovery differ by client; see [adoption notes](references/adoption.md). ClawHub-specific listing text and usage guidance are separate in [CLAWHUB.md](CLAWHUB.md).

## How it helps over time

- **Before a change:** the agent uses the relevant map to find likely edit locations and applicable procedures.
- **During a change:** it reads the actual source it needs; the map is not a substitute for code inspection or mandatory instructions.
- **When paths change:** the affected map should be updated in the same change.
- **In a new session:** the project entry point makes the maps discoverable, provided the host reads that entry point.

Initial mapping takes work and model usage. Repeated tasks are where avoiding repeated exploration may help most. Time and token savings depend on project size, task and agent behavior; no percentage or subscription-lifetime guarantee has been measured.

## What it does not do

It does not change model settings, bypass provider limits, modify application code, install dependencies, run a background service or upload project content. It does not require a particular model, API key or paid account. Your chosen agent still has its normal costs and permissions.

## Safety and control

This package contains Markdown instructions, not an executable optimizer. When invoked, your agent reads selected project files and edits navigation documentation, including the applicable instruction entry point. Existing rules, unrelated edits and release gates must remain intact. Mapping does not authorize committing, pushing or deploying.

Review the diff; undo by reverting only the mapping changes. Never put secrets or private file contents in maps. [SECURITY.md](SECURITY.md) describes the boundaries; [SHA256SUMS.txt](SHA256SUMS.txt) verifies package integrity, not independent safety certification.

## Documentation

- [GITHUB-PROMPT.md](GITHUB-PROMPT.md): one-sentence request and installation-free standalone prompt.
- [SKILL.md](SKILL.md): agent execution workflow.
- [CLAWHUB.md](CLAWHUB.md): registry description and installed-skill usage.
- [Examples](references/examples.md): small projects, larger repositories and monorepos.

## More by Asif2BD

- [OpenClaw Token Optimizer](https://clawhub.ai/asif2bd/openclaw-token-optimizer): a separate runtime audit skill. This project focuses on coding-project navigation.
- [MissionDeck.ai](https://missiondeck.ai): agent coordination; optional and independent of this skill.
- [ProSkills.md](https://proskills.md): discover AI skills.

## License and provenance

MIT © 2026 M Asif Rahman. Adapted from the user-supplied Workspace Map release. Project indexes are an established pattern; no exclusive invention of the underlying idea is claimed. No private project files or source screenshots are included.
