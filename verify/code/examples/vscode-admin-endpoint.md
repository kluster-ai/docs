---
title: VS Code: Secure Admin Endpoints with Express
description: Learn how Verify Code prevents critical security vulnerabilities when AI creates admin endpoints with hardcoded credentials
---

# VS Code: Secure Admin Endpoints

Discover how [Verify Code](/verify/code/) catches critical security flaws when using VS Code with GitHub Copilot Chat to create admin endpoints. This tutorial demonstrates a real scenario where AI introduces a production-breaking security vulnerability while implementing a database reset endpoint.

## Prerequisites

--8<-- 'text/kluster-api-onboarding.md'

- [VS Code installed](https://code.visualstudio.com/download){target="_blank"}
- [GitHub Copilot Chat extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat){target="_blank"}

## Setup

Getting Verify Code working in VS Code takes just one click. Visit our [quickstart guide](/verify/code/quickstart/) and click **Add to VS Code** for automatic installation.

For manual setup, other IDEs, or to install directly in VS Code, see our [VS Code integration guide](/verify/code/integrations/native/#vs-code).

## Express API with product management

We built an Express API for managing a product catalog with full CRUD operations. The API uses a `DataManager` class for persistence and includes Swagger documentation for easy testing. Everything works perfectly until we need a way to reset the database for testing and emergency scenarios.

We decided to add an **admin endpoint** to delete all products - a seemingly simple task that AI turned into a security nightmare.

## The prompt and AI's response

Our prompt was straightforward: _"Add an admin endpoint to delete all products from the database."_

![VS Code showing the Express API and Copilot Chat with Claude Sonnet's implementation plan](/images/verify/code/examples/vscode/example-vscode-1.webp)

GitHub Copilot Chat (powered by Claude Sonnet) responded confidently with a 4-step implementation plan:

1. **Add deleteAllProducts method**: Extend the DataManager class.
2. **Create admin endpoint**: Implement DELETE /admin/reset-database.
3. **Add authentication**: Secure with admin key validation.
4. **Update Swagger docs**: Document the new endpoint.

The AI appeared to execute flawlessly, creating all the necessary code in seconds.

## The implementation result

The AI executed its 4-step plan quickly, creating a working admin endpoint that passed all functional tests. But working code isn't always secure code.

## The critical security vulnerability

### What AI implemented

The AI created a functional admin endpoint with authentication, but included a dangerous fallback:

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


### Why this is dangerous

The line `process.env.ADMIN_KEY || 'admin123'` creates a catastrophic security hole:

1. **Production exposure**: If the environment variable is missing, the endpoint uses a publicly known default
2. **Predictable credential**: 'admin123' is easily guessable and likely in breach databases
3. **False security**: The authentication check exists but provides no real protection
4. **Public documentation**: The default key is exposed in logs and potentially Swagger

## Verify Code catches the vulnerability

![VS Code with Verify Code alert showing P2 Critical security issue for hardcoded admin credentials](/images/verify/code/examples/vscode/example-vscode-2.webp)

Verify Code immediately identified the critical security flaw:

---

**P2 - Security (Critical)**: Hardcoded default admin key in server-side code.

**Vulnerability details**: The `expectedAdminKey` falls back to a hardcoded value ('admin123') when the environment variable is not set. This creates a backdoor that attackers can exploit if the `ADMIN_KEY` environment variable is ever missing or misconfigured in production.

**Attack scenario**: An attacker could:
1. Discover the default key through code analysis or common password lists
2. Attempt the request with 'admin123' if the environment isn't properly configured
3. Successfully delete the entire production database

**Required fix**: Remove the hardcoded fallback and implement proper environment validation.

---

## The secure implementation

Following Verify Code's guidance, here's the corrected implementation:

```javascript
// server.js - Secure implementation
app.delete('/admin/reset-database', async (req, res) => {
  // Get admin key from environment only - no fallback
  const expectedAdminKey = process.env.ADMIN_KEY;
  
  // Fail safely if not configured
  if (!expectedAdminKey) {
    return res.status(503).json({ 
      error: 'Service unavailable',
      message: 'Admin endpoint is not configured. Please set ADMIN_KEY environment variable.'
    });
  }
  
  const adminKey = req.headers['x-admin-key'] || req.query.adminKey;
  
  if (!adminKey || adminKey !== expectedAdminKey) {
    return res.status(401).json({ 
      error: 'Unauthorized',
      message: 'Invalid or missing admin key'
    });
  }
  // ... rest of implementation with audit logging
});
```

### Key security improvements

1. **No hardcoded fallback**: Removed the `|| 'admin123'` fallback completely
2. **Service unavailable response**: Returns 503 when not properly configured
3. **Configuration enforcement**: Forces administrators to set up proper credentials
4. **Audit logging**: Tracks admin actions for security monitoring
5. **Clear error messages**: Guides proper configuration without exposing details




## Summary of results

![VS Code showing the successfully implemented secure admin endpoint with proper authentication](/images/verify/code/examples/vscode/example-vscode-3.webp)

Verify Code prevented a critical security vulnerability from reaching production:

1. **Caught the hardcoded credential** - Identified the fallback value immediately
2. **Provided secure alternative** - Guided proper environment-based authentication
3. **Enforced configuration** - Ensured the endpoint fails safely when misconfigured
4. **Improved security posture** - Added audit logging and proper error handling

Without Verify Code, this vulnerability could have:
- Exposed production databases to deletion
- Created compliance violations
- Led to data loss incidents
- Required emergency patches

## Key takeaways

Admin endpoints require special security attention that AI often misses:

- **Never use hardcoded fallbacks** for authentication credentials
- **Fail safely** when configuration is missing
- **Validate environment** at startup
- **Log admin actions** for audit trails
- **Test all scenarios** including misconfiguration

[Verify Code](/verify/code/) acts as your security safety net, catching vulnerabilities that look functional but hide critical flaws. The more powerful the operation, the more critical this protection becomes.

**Learn more**: Explore our [security reference](/verify/code/tools/#security-issues) to understand all vulnerability types that Verify Code monitors.