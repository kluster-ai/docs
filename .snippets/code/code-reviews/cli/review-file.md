<div data-termynal>
  <span data-ty="input">kluster review file src/auth.go src/middleware.go</span>
  <span data-ty>→ Reviewing code [████████████████████████████████████████] 100%</span>
  <span data-ty>✓ Reviewing code complete!</span>
  <span data-ty></span>
  <span data-ty>Review: 507f1f77bcf86cd799439018</span>
  <span data-ty></span>
  <span data-ty>Found 1 issue(s)</span>
  <span data-ty></span>
  <span data-ty>#1 CRITICAL [P2] security</span>
  <span data-ty>JWT token verification skips expiration check</span>
  <span data-ty>at src/auth.go:67-72</span>
  <span data-ty></span>
  <span data-ty>Fix</span>
  <span data-ty>  Add token expiration validation before processing claims.</span>
</div>
