<div data-termynal>
  <span data-ty="input">kluster@Commodore64 % kluster review staged</span>
  <span data-ty>→ Reviewing code [████████████████████████████████████████] 100%</span>
  <span data-ty>✓ Reviewing code complete!</span>
  <span data-ty></span>
  <span data-ty>Review: 507f1f77bcf86cd799439011</span>
  <span data-ty></span>
  <span data-ty>Found 2 issue(s)</span>
  <span data-ty></span>
  <span data-ty>#1 CRITICAL [P0] security</span>
  <span data-ty>SQL injection vulnerability detected in user input handling. User-provided</span>
  <span data-ty>data is concatenated directly into SQL query without sanitization.</span>
  <span data-ty>at src/db/queries.go:45-52</span>
  <span data-ty></span>
  <span data-ty>More details</span>
  <span data-ty>  The function buildQuery() takes user input from the request body and</span>
  <span data-ty>  concatenates it directly into the SQL string.</span>
  <span data-ty></span>
  <span data-ty>Fix</span>
  <span data-ty>  Use parameterized queries: db.Query("SELECT * FROM users</span>
  <span data-ty>  WHERE id = ?", userID)</span>
  <span data-ty></span>
  <span data-ty>────────────────────────────────────────────────────────────────────────</span>
  <span data-ty></span>
  <span data-ty>#2 HIGH [P1] logical</span>
  <span data-ty>Potential null pointer dereference. The variable 'config' may be nil</span>
  <span data-ty>when accessed on line 78.</span>
  <span data-ty>at cmd/server.go:78</span>
  <span data-ty></span>
  <span data-ty>Fix</span>
  <span data-ty>  Add a nil check before accessing config properties.</span>
</div>
