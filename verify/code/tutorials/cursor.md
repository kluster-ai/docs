---
title: Cursor: Firebase authentication 
description: See how Verify Code catches critical issues in real-time while migrating from localStorage to Firebase authentication
---

# Cursor: Firebase authentication

Learn how Verify Code acts as your safety net when using Cursor AI to write code. This tutorial demonstrates a real migration from localStorage to Firebase authentication in a buy-sell e-commerce platform, showcasing the 4 critical issues Verify Code caught.

## Prerequisites

--8<-- 'text/kluster-api-onboarding.md'

- [Cursor IDE installed](https://cursor.com/downloads){target=_blank}

## Setup

Getting Verify Code working in Cursor takes just one click. Visit our [quickstart guide](/verify/code/quickstart/) and click **Add to Cursor** for automatic installation.

For manual setup or other IDEs, see our [integration guides](/verify/code/integrations/).

## The migration project

We built a buy-sell e-commerce platform where users post articles for purchase. The app initially used localStorage for user authentication, but we decided to migrate to Firebase for better security and user management.

We used **Gemini 2.5 Flash** (Cursor's standard free model) in **agentic mode** to handle the migration while Verify Code monitored the changes.

{Screenshot-HERE-Cursor-with-VerifyCode-Active}

## The AI mistake loop

Without Verify Code, this migration would have been painful. The AI went through **6+ correction cycles**, constantly reverting changes and breaking the same code repeatedly. Each cycle followed the pattern: mistake → apology → "fix" → new mistake → repeat.

Verify Code breaks this cycle by catching issues immediately.

## Issue 1: Incomplete implementation

**What happened**: Asked Cursor AI to implement Firebase login functionality.

**AI's incomplete code**:
```typescript
// src/lib/firebase.ts
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

const firebaseConfig = { /* config */ };
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
```

**Verify Code alert**:
{Screenshot-HERE-Incomplete-Implementation-Alert}

**P1 - Intent (High)**: AI did not implement the actual user login functionality as requested.

**Developer impact**: Running the app would cause runtime errors when trying to authenticate users - the `auth` object simply doesn't exist.

**Fixed with Verify Code guidance**:
```typescript
// src/lib/firebase.ts
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth"; // Added

const firebaseConfig = { /* config */ };
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth(app); // Initialize auth

export { app, auth, analytics }; // Export auth
```

---

## Issue 2: Breaking changes  

**What happened**: AI removed working Firebase login logic from API route.

**Original working code**:
```typescript
// src/app/api/auth/login/route.ts
export async function POST(req: NextRequest) {
  const { email, password } = await req.json();
  const userCredential = await signInWithEmailAndPassword(auth, email, password);
  return NextResponse.json({ message: "Login successful", user: user.toJSON() });
}
```

**AI's breaking change**:
```typescript
export async function POST(req: NextRequest) {
  return NextResponse.json({ message: "Not used for direct login" });
}
```

**Verify Code alert**:
{Screenshot-HERE-Breaking-Changes-Alert}

**P1 - Intent (High)**: AI removed Firebase login implementation instead of maintaining it.

**Developer impact**: Login endpoint would return a useless message instead of actually authenticating users. All login attempts would fail silently.

---

## Issue 3: Security vulnerabilities

**What happened**: AI created signup endpoint without input validation.

**AI's insecure code**:
```typescript
// src/app/api/auth/signup/route.ts
export async function POST(request: NextRequest) {
  const body = await request.json();
  const { email, password, name } = body; // No validation!
  
  const userCredential = await createUserWithEmailAndPassword(auth, email, password);
}
```

**Verify Code alert**:
{Screenshot-HERE-Security-Vulnerability-Alert}

**P3 - Security (High)**: Lack of input validation for signup data.

**Developer impact**: Malformed data could crash the server, invalid emails would cause Firebase errors, and weak passwords could be accepted.

**Secure implementation**:
```typescript
import { SignupSchema } from '@/lib/validation';

export async function POST(request: NextRequest) {
  const body = await request.json();
  
  // Validate input
  const validationResult = SignupSchema.safeParse(body);
  if (!validationResult.success) {
    return NextResponse.json({
      error: 'Validation failed',
      details: validationResult.error.issues
    }, { status: 400 });
  }
  
  const { email, password, name } = validationResult.data;
  const userCredential = await createUserWithEmailAndPassword(auth, email, password);
}
```

---

## Issue 4: Architecture regression

**What happened**: AI reverted Firebase authentication back to localStorage and API calls.

**Correct Firebase implementation**:
```typescript
// src/contexts/AuthContext.tsx
const login = async (email: string, password: string) => {
  const userCredential = await signInWithEmailAndPassword(auth, email, password);
  return !!userCredential.user;
};
```

**AI's regression**:
```typescript
// AI reverted to localStorage approach
const [user, setUser] = useState(() => {
  const savedUser = localStorage.getItem('user'); // Wrong approach!
  return savedUser ? JSON.parse(savedUser) : null;
});

const login = async (email: string, password: string) => {
  const response = await fetch('/api/auth/login', {
    method: 'POST',
    body: JSON.stringify({ email, password })
  });
};
```

**Verify Code alert**:
{Screenshot-HERE-Architecture-Regression-Alert}

**P1 - Intent (High)**: AI reverted Firebase authentication implementation back to using localStorage and API calls.

**Developer impact**: Lost all Firebase benefits like real-time auth state, secure token management, and cross-device sessions. Back to the original localStorage problems we were trying to solve.

---

## The results

Verify Code caught **4 critical issues** that would have caused:

1. **Incomplete implementation** - Runtime authentication errors
2. **Breaking changes** - Non-functional login endpoint  
3. **Security vulnerabilities** - Unvalidated user input
4. **Architecture regression** - Lost Firebase benefits

**Time saved**: Hours of debugging and testing cycles prevented. No more AI mistake loops.

## Key takeaway

AI accelerates development, but Verify Code ensures quality. Without it, you're stuck in cycles of AI mistakes, apologies, and corrections. With it, issues are caught instantly so you can maintain both speed and reliability.

**Learn more**: Explore our [tools reference](/verify/code/tools/) to understand all issue types and priority levels that Verify Code monitors.