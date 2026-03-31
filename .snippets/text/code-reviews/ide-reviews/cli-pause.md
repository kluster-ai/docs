### Pause from the terminal

In CLI tools and agentic tools such as Claude Code and Codex CLI, you can pause reviews through the chat interface. Ask your agent to pause kluster reviews, and it calls the `kluster_review_pause` MCP tool.

The pause lasts **1 hour** by default. Custom durations are not available in the terminal flow due to a system limitation. While paused, the system automatically resolves any MCP requests so the response is almost instantaneous.

To pause reviews, ask your agent to pause kluster. The following example shows the pause flow in Claude Code:

--8<-- 'code/code-reviews/ide-reviews/pause-reviews.md'

To resume reviews before the pause expires, ask your agent to resume kluster:

--8<-- 'code/code-reviews/ide-reviews/resume-reviews.md'

!!! note "Cross-environment pause"
    Pause is project-specific. Pausing in a CLI tool also pauses reviews in any IDE working on the same project, and vice versa.
