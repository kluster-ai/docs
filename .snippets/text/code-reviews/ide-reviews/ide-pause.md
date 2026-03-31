You can temporarily pause all kluster code reviews for the current project. While paused, the system automatically resolves any MCP requests so the response is almost instantaneous.

### Pause from the status bar

1. Click the **kluster.ai** button in the IDE status bar.
2. Select **Pause Agent Review...** from the command palette.
3. Choose a duration from the available options.
4. Verify that kluster is paused by the pause icon in the kluster.ai IDE status bar.

<video autoplay loop muted playsinline controls style="max-width: 100%; border-radius: 8px;">
  <source src="/images/code-reviews/ide-reviews/pause-reviews/pause-reviews.webm" type="video/webm">
  Your browser does not support the video tag. You can
  <a href="/images/code-reviews/ide-reviews/pause-reviews/pause-reviews.webm">download the pause reviews demo video</a>
  instead.
</video>

Reviews resume automatically when the selected duration expires. Select **Indefinitely (disable)** to keep reviews paused until you re-enable them manually.

!!! note "Pause is project-specific"
    Pausing applies to the project identified by its Git remote URL or filesystem path. If you pause reviews in one tool (for example, VS Code), reviews are also paused for every other tool working on the same project, including Claude Code and Codex CLI.
