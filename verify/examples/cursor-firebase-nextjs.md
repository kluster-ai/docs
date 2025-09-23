---
title: Cursor: Firebase Authentication with Next.js
description: See how Verify Code catches critical issues in real-time while migrating from localStorage to Firebase authentication
---

# Cursor: Firebase authentication

Learn how [Verify Code](/verify/) acts as your safety net when using Cursor AI to write code. This tutorial demonstrates a real migration from localStorage to Firebase authentication in a buy-sell e-commerce platform, showcasing how AI plans can go wrong and the four critical issues Verify Code caught.

## Prerequisites

- [Cursor IDE installed](https://cursor.com/downloads){target="_blank"}

## Setup

Getting Verify Code working in Cursor takes just one click. Visit our [quickstart guide](/verify/quickstart/) and click **Add to Cursor** for automatic installation.

## Next.js e-commerce

We built a buy-sell e-commerce platform where users post articles for purchase. The app initially used `localStorage` for user authentication, but we decided to **migrate to Firebase** for better security and user management.

We used **Gemini 2.5 Flash** (Cursor's standard free model) in **agentic mode** to handle the migration while Verify Code monitored the changes.

## The prompt and AI's plan

Our prompt was to _implement a real user login with Firebase_ + Firebase default app setting file.

![Cursor showing e-commerce app and AI's Firebase implementation plan](/images/verify/code/examples/cursor/example-cursor-1.webp)

The AI responded confidently with a detailed 5-step plan:

1. **Create Firebase initialization file**: Set up `src/lib/firebase.ts`.
2. **Install Firebase**: Add the npm package.
3. **Update authentication context**: Modify `src/contexts/AuthContext.tsx`.
4. **Update Login API route**: Handle Firebase in `src/app/api/auth/login/route.ts`.
5. **Update Signup API route**: Handle Firebase in `src/app/api/auth/signup/route.ts`.


## Plan vs. implementation outcomes

The AI's 5-step implementation plan achieved just 20% success rate, with four critical failures.

| Step | Task | Result |
|------|------|--------|
| 1 | Firebase initialization | ❌ Failed - Incomplete implementation |
| 2 | Install Firebase | ✅ Success |
| 3 | Update AuthContext | ❌ Failed - Architecture regression |
| 4 | Update login API | ❌ Failed - Breaking changes |
| 5 | Update signup API | ❌ Failed - Security vulnerabilities |

The AI got confused between steps 3-4, couldn't decide between direct Firebase calls vs API routes, kept reverting working code, and made **multiple correction attempts** throughout the implementation.

## Key issues caught by Verify Code

The AI made four key mistakes along the way, escalating from simple import issues to reverting the entire Firebase implementation. Below, we examine each catch.

### Incomplete implementation

What happened? AI created Firebase config but missed the actual authentication setup.

```typescript
// src/lib/firebase.ts - Step 1 attempt
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

const firebaseConfig = { /* config */ };
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app); // ❌ No auth setup
```

Verify Code provided the following response:

---

**P1 - Intent (High)**: AI did not implement the actual user login functionality as requested.

**Why this matters**: Running the app would cause runtime errors when trying to authenticate - the `auth` object simply doesn't exist.

**Correct approach**:
```typescript
// src/lib/firebase.ts - Corrected
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth"; // ✅ Added

const firebaseConfig = { /* config */ };
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth(app); // ✅ Initialize auth

export { app, auth, analytics }; // ✅ Export auth
```

---

### Breaking changes

What happened? AI removed the working Firebase login logic from the API route.

```typescript
// src/app/api/auth/login/route.ts - Working version
export async function POST(req: NextRequest) {
  const { email, password } = await req.json();
  const userCredential = await signInWithEmailAndPassword(auth, email, password);
  return NextResponse.json({ message: "Login successful", user: user.toJSON() });
}
```

```typescript
// AI's "fix" - Step 4 attempt
export async function POST(req: NextRequest) {
  return NextResponse.json({ message: "Not used for direct login" }); // ❌ Removed logic
}
```

The screenshot below shows Cursor's interface with Verify Code's alert panel displaying a critical P1 Intent violation. The alert clearly identifies that the AI removed working Firebase authentication logic from the login API route, replacing functional code with a placeholder response.

![Verify Code alert showing breaking changes detected in login API route](/images/verify/code/examples/cursor/example-cursor-2.webp){ width="75%" }

Verify Code provided the following response:

---

**P1 - Intent (High)**: AI removed Firebase login implementation instead of maintaining it.

**Why this matters**: AI replaced working authentication logic with a non-functional placeholder response, breaking the API contract.

**Correct approach**: Keep the original working Firebase authentication logic.

---

### Security vulnerabilities

What happened? AI created a signup endpoint without input validation.

```typescript
// src/app/api/auth/signup/route.ts - Step 5 attempt
export async function POST(request: NextRequest) {
  const body = await request.json();
  const { email, password, name } = body; // ❌ No validation!
  
  const userCredential = await createUserWithEmailAndPassword(auth, email, password);
}
```

Verify Code provided the following response:

---

**P3 - Security (High)**: Lack of input validation for signup data.

**Why this matters**: Malformed data could crash the server, invalid emails cause Firebase errors, weak passwords accepted.

**Correct approach**:

```typescript
import { SignupSchema } from '@/lib/validation';

export async function POST(request: NextRequest) {
  const body = await request.json();
  
  // ✅ Validate input
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

### Architecture regression

What happened? AI reverted the Firebase authentication logic back to the `localStorage` approach.

```typescript
// src/contexts/AuthContext.tsx - Correct Firebase approach
const login = async (email: string, password: string) => {
  const userCredential = await signInWithEmailAndPassword(auth, email, password);
  return !!userCredential.user;
};
```

```typescript
// AI reverted to original localStorage approach
const [user, setUser] = useState(() => {
  const savedUser = localStorage.getItem('user'); // ❌ Back to localStorage!
  return savedUser ? JSON.parse(savedUser) : null;
});

const login = async (email: string, password: string) => {
  const response = await fetch('/api/auth/login', { // ❌ API calls instead of Firebase
    method: 'POST',
    body: JSON.stringify({ email, password })
  });
};
```

The screenshot below displays Cursor with Verify Code's alert highlighting a P1 Intent violation. The alert detects that the AI has regressed the authentication architecture by reverting from the Firebase implementation back to the original localStorage and API-based approach, undoing the intended migration.

![Verify Code alert showing architecture regression from Firebase back to localStorage](/images/verify/code/examples/cursor/example-cursor-3.webp){ width="75%" }


Verify Code provided the following response:

---

**P1 - Intent (High)**: AI reverted Firebase authentication implementation back to using localStorage and API calls.

**Why this matters**: Lost all Firebase benefits like real-time auth state, secure token management, and cross-device sessions. Back to the original problems we were trying to solve.

**Correct approach**:
```typescript
// src/contexts/AuthContext.tsx
const login = async (email: string, password: string) => {
  const userCredential = await signInWithEmailAndPassword(auth, email, password);
  return !!userCredential.user;
};
```

---

## Summary of results

Verify Code caught **four critical issues** across a "simple" five-step plan:

1. **Incomplete implementation** - Step one missed core functionality.
2. **Breaking changes** - Step four deleted working code.
3. **Security vulnerabilities** - Step five ignored input validation.
4. **Architecture regression** - Step three went backwards.

By following Verify Code's guidance at each step, Gemini 2.5 Flash completed the Firebase migration. Users can now register and authenticate properly.

The following image shows the Firebase console showing the `code@verify.com` user creation:

![Firebase Authentication console showing successfully created users](/images/verify/code/examples/cursor/example-cursor-4.webp)

Users can now successfully login into the e-commerce app and Firebase user created:

![E-commerce app showing successful login with code@verify.com user](/images/verify/code/examples/cursor/example-cursor-5.webp)

The migration from `localStorage` to Firebase authentication was completed without the typical debugging cycles. [Verify Code](/verify/) caught each issue in real-time, allowing us to fix problems immediately rather than discovering them during testing.

## Key takeaways

Even with clear prompts and detailed plans, AI execution can go wrong. Verify Code acts as your safety net, catching issues before they compound into debugging nightmares.

The more complex the task, the more valuable this real-time verification becomes.

**Learn more**: Explore our [tools reference](/verify/tools/) to understand all issue types and priority levels that Verify Code monitors.