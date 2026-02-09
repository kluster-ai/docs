<div id="termynal" data-termynal>
  <span data-ty="input">git push origin feature-branch</span>
  <span data-ty>kluster.ai: Reviewing changes from a1b2c3d to e4f5g6h...</span>
  <span data-ty>→ Reviewing code [████████████████████████████████████████] 100%</span>
  <span data-ty>✓ Reviewing code complete!</span>
  <span data-ty></span>
  <span data-ty>Review: 507f1f77bcf86cd799439013</span>
  <span data-ty></span>
  <span data-ty>Found 1 issue(s)</span>
  <span data-ty></span>
  <span data-ty>#1 HIGH [P1] security</span>
  <span data-ty>API key exposed in source code.</span>
  <span data-ty>at src/config.js:15</span>
  <span data-ty></span>
  <span data-ty>Fix</span>
  <span data-ty>  Move the API key to environment variables and access via process.env.API_KEY</span>
  <span data-ty></span>
  <span data-ty></span>
  <span data-ty>kluster.ai: Push blocked due to code review issues (severity threshold: high).</span>
  <span data-ty>kluster.ai: Fix the issues above or use 'git push --no-verify' to skip.</span>
  <span data-ty>kluster.ai: View this review again: kluster show 507f1f77bcf86cd799439013</span>
</div>
