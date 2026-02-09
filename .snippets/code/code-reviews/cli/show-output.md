<div data-termynal>
  <span data-ty="input">kluster show 507f1f77bcf86cd799439011</span>
  <span data-ty>→ Fetching review details...</span>
  <span data-ty></span>
  <span data-ty>Review: 507f1f77bcf86cd799439011</span>
  <span data-ty>Date: 2026-02-09 14:32:15</span>
  <span data-ty>Project: my-awesome-app</span>
  <span data-ty></span>
  <span data-ty>Found 2 issue(s)</span>
  <span data-ty></span>
  <span data-ty>#1 HIGH [P1] security</span>
  <span data-ty>Hardcoded credentials detected in configuration file.</span>
  <span data-ty>at config/database.go:12-15</span>
  <span data-ty></span>
  <span data-ty>More details</span>
  <span data-ty>  The database password is hardcoded as a string literal. This is a</span>
  <span data-ty>  security risk as credentials may be exposed in version control.</span>
  <span data-ty></span>
  <span data-ty>Fix</span>
  <span data-ty>  Use environment variables or a secrets manager. Replace the hardcoded</span>
  <span data-ty>  value with os.Getenv("DB_PASSWORD").</span>
  <span data-ty></span>
  <span data-ty>────────────────────────────────────────────────────────────────────────</span>
  <span data-ty></span>
  <span data-ty>#2 MEDIUM [P2] performance</span>
  <span data-ty>Inefficient loop detected - database query inside loop iteration.</span>
  <span data-ty>at internal/users/sync.go:45-60</span>
  <span data-ty></span>
  <span data-ty>Fix</span>
  <span data-ty>  Batch the database queries by collecting IDs first, then executing</span>
  <span data-ty>  a single query with WHERE id IN (...) clause.</span>
</div>
