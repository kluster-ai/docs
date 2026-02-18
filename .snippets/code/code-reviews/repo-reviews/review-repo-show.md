<div data-termynal>
  <span data-ty  ="input"> verify-code-demo % kluster review repo show</span>
  <span data-ty>→ Last review: Fri, 13 Feb 2026 08:15:12 PST</span>
  <span data-ty></span>
  <span data-ty>#1 HIGH performance</span>
  <span data-ty>Unbounded in-memory storage will lead to memory exhaustion (OOM).</span>
  <span data-ty>at src/endpoints.ts:13,50</span>
  <span data-ty></span>
  <span data-ty>More details</span>
  <span data-ty>  The `reviews` array (src/endpoints.ts, line 13) is used as a global</span>
  <span data-ty>  in-memory store with no size limit, TTL, or eviction policy.</span>
  <span data-ty></span>
  <span data-ty>Fix</span>
  <span data-ty>  Set a max size, use an eviction-capable cache, or move data to a</span>
  <span data-ty>  persistent database.</span>
  <span data-ty></span>
  <span data-ty>────────────────────────────────────────────────────────────────────────</span>
  <span data-ty></span>
  <span data-ty>#2 HIGH security</span>
  <span data-ty>Missing CSRF protection on state-changing POST endpoint.</span>
  <span data-ty>at src/endpoints.ts:23-62</span>
  <span data-ty></span>
  <span data-ty>More details</span>
  <span data-ty>  The '/reviews' endpoint accepts state-changing POST requests without</span>
  <span data-ty>  CSRF tokens or equivalent protections.</span>
  <span data-ty></span>
  <span data-ty>Fix</span>
  <span data-ty>  Validate CSRF tokens (or enforce SameSite/custom header protections)</span>
  <span data-ty>  on state-changing requests.</span>
  <span data-ty></span>
  <span data-ty>→ Repo Reviews establish a comprehensive understanding of your codebase,</span>
  <span data-ty>  surfacing risks, inconsistencies, and violations that can only be</span>
  <span data-ty>  detected when analyzing the code as a whole.</span>
</div>
