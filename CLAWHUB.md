# ClawHub listing and usage

Display name: AI Coding Token Optimizer
Slug: ai-coding-token-optimizer
Version: 1.0.0

## Short description
Reduce unnecessary AI coding context with concise, project-specific navigation maps for Codex, Claude Code and other repository-capable agents—without changing application code.

## Install

```sh
clawhub install ai-coding-token-optimizer
```

## One-sentence request

> Use AI Coding Token Optimizer to reduce unnecessary project context by creating concise navigation maps, preserving existing instructions and application code.

## Agent guidelines

Follow SKILL.md. Inspect the selected repository, preserve mandatory instructions, reuse existing maps, and validate relative links. Use the established AGENTS.md or CLAUDE.md entry point. Do not read secrets, run project scripts, change source code, install dependencies or publish changes as part of mapping. Explain any uncertainty and return a concise documentation diff summary.

The host needs filesystem access and Markdown skill support. Installation does not configure every client. GitHub-only adoption has a separate standalone prompt in GITHUB-PROMPT.md. No paid service, API key, telemetry or bundled executable is required. Host inference still has its normal cost. No measured savings percentage or independent review verdict is asserted here.
