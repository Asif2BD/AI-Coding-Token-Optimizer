# GitHub adoption prompt — any repository-capable AI agent

## One sentence

> Read https://github.com/Asif2BD/AI-Coding-Token-Optimizer and apply its project-mapping workflow to this project, preserving existing instructions and application code.

No skill installation is required. The agent must be able to read this repository and edit the target project. If links cannot be opened, paste the standalone prompt below.

## Standalone prompt

Create or refresh a concise navigation map for this repository so an AI agent can find the right files without loading every document.

Read existing agent instructions and inspect the real project structure first. Choose a few useful areas based on the work this project actually contains—CONTENT, PRODUCT and OPERATIONS are examples, not required names. If this is a small project, a single Map section may be enough.

For each useful area, create or update a short Markdown router, ideally 15–35 lines. Include one relative link and one sentence explaining each important file or folder. Point to authoritative guides and likely edit locations. Distinguish current source, historical references, generated output and runtime data outside Git. Reuse existing indexes instead of duplicating them.

Add a Map section to the existing AGENTS.md or CLAUDE.md entry point that directs agents to the relevant router first, then only the linked files needed for the task. Preserve all existing mandatory instructions. Add a rule to maintain these maps whenever paths or workflow ownership change. Link from README if useful.

Validate the links and descriptions, keep secrets and machine-specific paths out, and review the diff. Make documentation changes only; do not move application files or change behavior. Summarize what changed and any uncertainty. Do not commit, push, merge, deploy or publish unless requested. If run again, refresh the existing maps rather than creating duplicates.
