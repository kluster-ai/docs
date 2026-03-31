### Pause from the terminal

In CLI tools and agentic tools such as Claude Code and Codex CLI, you can pause reviews through the chat interface. Ask your agent to pause kluster reviews, and it calls the `kluster_review_pause` MCP tool.

The pause lasts **1 hour** by default. Custom durations are not available in the terminal flow due to a system limitation. While paused, the system automatically resolves any MCP requests so the response is almost instantaneous.

To pause reviews, ask your agent to pause kluster. The following example shows the pause flow in Claude Code:

<div data-termynal>
  <span data-ty>╭─── Claude Code v2.1.87 ────────────────────────────╮</span>
  <span data-ty>│                                                    │</span>
  <span data-ty>│               Welcome back kluster.ai!             │</span>
  <span data-ty>│                                                    │</span>
  <span data-ty>│                     ▐▛███▜▌                        │</span>
  <span data-ty>│                    ▝▜█████▛▘                       │</span>
  <span data-ty>│                      ▘▘ ▝▝                         │</span>
  <span data-ty>│                                                    │</span>
  <span data-ty>│  Opus 4.6 · Claude Max · kluster's Organization    │</span>
  <span data-ty>│                      /workspace                    │</span>
  <span data-ty>╰────────────────────────────────────────────────────╯</span>
  <span data-ty></span>
  <span data-ty="input" data-ty-prompt="❯ "> pause kluster</span>
  <span data-ty></span>
  <span data-ty>● Pausing kluster reviews...</span>
  <span data-ty></span>
  <span data-ty>● kluster-verify — kluster_review_pause (MCP)(action: "pause")</span>
  <span data-ty></span>
  <span data-ty>  ⎿  kluster code review has been paused for 1 hour for this</span>
  <span data-ty>     project. Reviews will resume automatically after 60</span>
  <span data-ty>     minutes. To re-enable sooner, type "resume kluster</span>
  <span data-ty>     verification".</span>
  <span data-ty></span>
  <span data-ty>● kluster reviews have been paused for 1 hour. Automated code</span>
  <span data-ty>  reviews will resume automatically after that, or you can say</span>
  <span data-ty>  "resume kluster" to re-enable them sooner.</span>
</div>

To resume reviews before the pause expires, ask your agent to resume kluster:

<div data-termynal>
  <span data-ty>╭─── Claude Code v2.1.87 ────────────────────────────╮</span>
  <span data-ty>│                                                    │</span>
  <span data-ty>│               Welcome back kluster.ai!             │</span>
  <span data-ty>│                                                    │</span>
  <span data-ty>│                     ▐▛███▜▌                        │</span>
  <span data-ty>│                    ▝▜█████▛▘                       │</span>
  <span data-ty>│                      ▘▘ ▝▝                         │</span>
  <span data-ty>│                                                    │</span>
  <span data-ty>│  Opus 4.6 · Claude Max · kluster's Organization    │</span>
  <span data-ty>│                      /workspace                    │</span>
  <span data-ty>╰────────────────────────────────────────────────────╯</span>
  <span data-ty></span>
  <span data-ty="input" data-ty-prompt="❯ "> resume kluster</span>
  <span data-ty></span>
  <span data-ty>● Resuming kluster reviews...</span>
  <span data-ty></span>
  <span data-ty>● kluster-verify — kluster_review_pause (MCP)(action: "resume")</span>
  <span data-ty></span>
  <span data-ty>  ⎿  kluster code review has been resumed for this project.</span>
  <span data-ty>     Code changes will be verified again from now on.</span>
  <span data-ty></span>
  <span data-ty>● kluster reviews have been resumed. Automated code reviews</span>
  <span data-ty>  are active again.</span>
</div>

!!! note "Cross-environment pause"
    Pause is project-specific. Pausing in a CLI tool also pauses reviews in any IDE working on the same project, and vice versa.
