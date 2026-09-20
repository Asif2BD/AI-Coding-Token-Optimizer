# AI Coding Token Optimizer

[![Version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)](CHANGELOG.md)
[![MissionDeck](https://img.shields.io/badge/MissionDeck-ai-blueviolet)](https://missiondeck.ai)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.txt)

Built by MissionDeck.ai · Created by M Asif Rahman · [GitHub](https://github.com/Asif2BD/AI-Coding-Token-Optimizer)

**Spend less context finding files. Keep more room for coding.**

## Start here — choose your setup

**Using GitHub directly?** Open [GITHUB-PROMPT.md](GITHUB-PROMPT.md), copy the standalone prompt into your coding agent, and open the project you want to optimize. Skill installation is optional.

**Using ClawHub?** Install the skill using the command below, then use the one-sentence request. Registry-specific guidance is in [CLAWHUB.md](CLAWHUB.md).

## One-sentence request

After installing the skill, open your project and say:

> Use AI Coding Token Optimizer to reduce unnecessary project context by creating concise navigation maps, preserving existing instructions and application code.

No API key, background service or additional model is required by this package. Your host agent still consumes its normal model usage.

## What it does

AI Coding Token Optimizer is a portable project-navigation skill for repository-capable AI coding agents. It helps an agent inspect the real project, create concise area maps and connect them to existing AGENTS.md or CLAUDE.md instructions. It does not autonomously manage, build or deploy your application.

Instead of repeatedly searching an entire codebase, future tasks can start with a small map, then open the relevant source and procedure. Detailed documentation stays where it belongs.

- Adapts to small projects and monorepos.
- Reuses existing maps and preserves project instructions.
- Separates editable source, generated output and historical references.
- Checks relative links and explains uncertainties.
- Refreshes existing maps rather than producing duplicates.

## Install

```sh
clawhub install ai-coding-token-optimizer
```

This installs into the location selected by your ClawHub environment; it does not automatically configure every coding client. For other hosts, place this package in that host’s supported skill directory. See [adoption guide](references/adoption.md). Without skill support, use the [standalone prompt](GITHUB-PROMPT.md).

## Example result

```text
AGENTS.md or CLAUDE.md → Project Map
  CONTENT.md          → content sources and editorial guidance
  PRODUCT.md          → code entry points and development guides
  OPERATIONS.md       → release, verification and recovery guides
```

These names are examples, not mandatory files. A small project may need only one Map section. Routers are short navigation documents, not application routing code.

## Compatibility and limits

Designed for Codex, Claude Code and OpenClaw-style agents that can read Markdown instructions and edit a repository. Client skill discovery and installation differ. This release’s packaging and fixture checks do not prove end-to-end behavior in every client; no cross-client inference benchmark is claimed.

Maps may reduce repeated searching and unnecessary context loading. No percentage token savings, speedup or accuracy improvement has been measured. Stale maps can mislead: maintain affected links when paths or ownership change. Existing mandatory context and release gates always apply.

## Safety

Documentation-only package: no executable scripts, dependency installation, telemetry or network client. When invoked, your agent reads project files and edits navigation Markdown. Review the diff as usual. The skill does not authorize commits, pushes, deployments or publication. See [SECURITY.md](SECURITY.md).

## Verification

```sh
sha256sum -c SHA256SUMS.txt
```

Checksums demonstrate integrity against this manifest, not independent security approval.

## MissionDeck.ai — Your Agent Command Center

Explore [MissionDeck.ai](https://missiondeck.ai) for agent coordination. AI Coding Token Optimizer works independently; no MissionDeck account or connection is required.

## Provenance and license

Adapted from the user-supplied Workspace Map release, developed in project work by M Asif Rahman. Repository navigation and area indexes are established patterns; no exclusive invention of the underlying idea is claimed. Private project files and original screenshots are not included. MIT licensed; see [LICENSE.txt](LICENSE.txt).

## More by Asif2BD

- [OpenClaw Token Optimizer](https://clawhub.ai/asif2bd/openclaw-token-optimizer)
- [ProSkills.md](https://proskills.md)

## Frequently asked questions

**Does it change my model or subscription?** No. It organizes project navigation; it does not alter provider limits, billing, model settings or your code.

**Can I use it anywhere?** With a repository-capable agent that can read and edit your project. A chat-only interface needs files supplied or connected; the prompt does not grant access.

**Does it save tokens immediately?** Initial inspection itself costs context. Benefits depend on repeated use, host behavior and maintaining maps. No savings benchmark is claimed.

**How do I undo it?** Review and revert only its documentation diff, retaining unrelated changes.

**Is this OpenClaw Token Optimizer?** No. That separate skill audits runtime configuration. This skill organizes coding-project context and has no runtime adapter.
