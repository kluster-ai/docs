---
title: VS Code: Secure Admin Endpoints with Express
description: Learn how Code Reviews prevents critical security vulnerabilities when AI creates admin endpoints with hardcoded credentials
Categories: AI-generated code
---

# VS Code: Secure Admin Endpoints

Discover how [Code Reviews](/code-reviews/) catches critical security flaws when using VS Code with GitHub Copilot Chat to create admin endpoints. This tutorial demonstrates a real scenario where AI introduces a production-breaking security vulnerability while implementing a database reset endpoint.

## Prerequisites

--8<-- 'text/kluster-api-onboarding.md'

- [VS Code installed](https://code.visualstudio.com/download){target="_blank"}
- [GitHub Copilot Chat extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat){target="_blank"}

## Setup

Getting Code Reviews working in VS Code takes just one click. Visit the [installation guide](/code-reviews/get-started/installation/) and click **Add to VS Code** for automatic installation.

## Express API with product management

This Express API manages a product catalog with full CRUD operations. The API uses a `DataManager` class for persistence and includes Swagger documentation for easy testing. Everything works perfectly until the team needs a way to reset the database for testing and emergency scenarios.

The team decided to add an **admin endpoint** to delete all products - a seemingly simple task that AI turned into a security nightmare.

## The prompt and AI's response

Our prompt was straightforward: _"Add an admin endpoint to delete all products from the database."_

![VS Code showing the Express API and Copilot Chat with Claude Sonnet's implementation plan](/images/code-reviews/ai-generated-code/examples/vscode/example-vscode-1.webp)

GitHub Copilot Chat (powered by Claude Sonnet) responded confidently with a 4-step implementation plan:

1. **Add deleteAllProducts method**: Extend the DataManager class.
2. **Create admin endpoint**: Implement DELETE /admin/reset-database.
3. **Add authentication**: Secure with admin key validation.
4. **Update Swagger docs**: Document the new endpoint.

The AI appeared to execute flawlessly, creating all the necessary code in seconds.

## The implementation result

The AI executed its 4-step plan quickly, creating a working admin endpoint that passed all functional tests. But working code isn't always secure code.

## The critical security vulnerability

The AI created a functional admin endpoint with authentication, but included a dangerous fallback that could expose production databases to unauthorized deletion:

```javascript
// server.js - AI's implementation
app.delete('/admin/reset-database', async (req, res) => {
  const adminKey = req.headers['x-admin-key'] || req.query.adminKey;
  const expectedAdminKey = process.env.ADMIN_KEY || 'admin123'; // ❌ CRITICAL: Hardcoded default

  if (!adminKey || adminKey !== expectedAdminKey) {
    return res.status(401).json({
      error: 'Unauthorized: Invalid admin key'
    });
  }
  // ... rest of implementation
});
```

The line `process.env.ADMIN_KEY || 'admin123'` creates a catastrophic security hole. If the environment variable is missing, the endpoint uses a publicly known default. This means 'admin123' becomes a backdoor key that works in production if the environment isn't properly configured - turning a simple misconfiguration into a database deletion vulnerability.

## Code Reviews catches the vulnerability

![VS Code with Code Reviews alert showing P2 Critical security issue for hardcoded admin credentials](/images/code-reviews/ai-generated-code/examples/vscode/example-vscode-2.webp)

Code Reviews immediately identified the critical security flaw:

---

**P2 - Security (Critical)**: Hardcoded default admin key in the server-side code.

**Why this matters**: The `expectedAdminKey` falls back to a hardcoded default value ('admin123') when the environment variable is not set. If the `ADMIN_KEY` environment variable is ever missing or misconfigured in production, the system defaults to a publicly known, hardcoded key that attackers could easily discover.

**Required fix**: Remove the hardcoded default value. Change from `process.env.ADMIN_KEY || 'admin123'` to `process.env.ADMIN_KEY`. Add validation to ensure the environment variable is set, logging a critical error if missing.

---

Beyond the immediate security fix, Code Reviews also recommended strengthening the admin endpoint with additional layers of protection: implementing multi-factor authentication (MFA) or role-based access control (RBAC), adding rate limiting to prevent brute-force attacks, and setting up comprehensive audit logging for all access attempts. These security recommendations can be customized in your [configuration settings](/code-reviews/configuration/options/) to match your team's specific security requirements.

## The secure implementation

Following Code Reviews's guidance, the solution eliminates the backdoor by removing `|| 'admin123'` entirely. The secure implementation validates that `process.env.ADMIN_KEY` exists and returns a 503 Service Unavailable if it's missing.

```javascript
// Before - VULNERABLE
// const expectedAdminKey = process.env.ADMIN_KEY || 'admin123'; // ❌ Hardcoded fallback

// After - SECURE
const expectedAdminKey = process.env.ADMIN_KEY;

if (!expectedAdminKey) {
  console.error('CRITICAL SECURITY ERROR: ADMIN_KEY environment variable is not set');
  return res.status(503).json({
    error: 'Service unavailable: Admin endpoint not configured'
  });
}

const adminKey = req.headers['x-admin-key'] || req.query.adminKey;

if (!adminKey || adminKey !== expectedAdminKey) {
  return res.status(401).json({
    error: 'Unauthorized: Invalid or missing admin key'
  });
}
```




## Summary of results

![VS Code showing the successfully implemented secure admin endpoint with proper authentication](/images/code-reviews/ai-generated-code/examples/vscode/example-vscode-3.webp)

Code Reviews prevented a critical security vulnerability from reaching production:

1. **Caught the hardcoded credential** - Identified the fallback value immediately.
2. **Provided secure alternative** - Guided proper environment-based authentication.
3. **Enforced configuration** - Ensured the endpoint fails safely when misconfigured.
4. **Improved security posture** - Added audit logging and proper error handling.

Without Code Reviews, this vulnerability could have:

- Exposed production databases to deletion.
- Created compliance violations.
- Led to data loss incidents.
- Required emergency patches.

## Key takeaways

Admin endpoints require special security attention that AI often misses:

- **Never use hardcoded fallbacks** for authentication credentials.
- **Fail safely** when configuration is missing.
- **Validate environment** at startup.
- **Log admin actions** for audit trails.
- **Test all scenarios** including misconfiguration.

[Code Reviews](/code-reviews/) acts as your security safety net, catching vulnerabilities that look functional but hide critical flaws. The more powerful the operation, the more critical this protection becomes.

**Learn more**: Explore our [MCP tools reference](/code-reviews/reference/mcp-tools/) to understand all vulnerability types that Code Reviews monitors.
