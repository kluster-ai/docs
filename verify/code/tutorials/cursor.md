---
title: Cursor: Firebase authentication 
description: See how Verify Code catches critical issues in real-time while migrating from localStorage to Firebase authentication
---

# Cursor: Firebase authentication

Learn how Verify Code acts as your safety net when using Cursor AI to write code. This tutorial demonstrates a real migration from localStorage to Firebase authentication in a buy-sell e-commerce platform, showcasing how AI plans can go wrong and the 4 critical issues Verify Code caught.

## Prerequisites

--8<-- 'text/kluster-api-onboarding.md'

- [Cursor IDE installed](https://cursor.com/downloads){target=_blank}

## Setup

Getting Verify Code working in Cursor takes just one click. Visit our [quickstart guide](/verify/code/quickstart/) and click **Add to Cursor** for automatic installation.

For manual setup or other IDEs, see our [integration guides](/verify/code/integrations/).

## Nextjs e-commerce

We built a buy-sell e-commerce platform where users post articles for purchase. The app initially used localStorage for user authentication, but we decided to **migrate to Firebase** for better security and user management.

We used **Gemini 2.5 Flash** (Cursor's standard free model) in **agentic mode** to handle the migration while Verify Code monitored the changes.

## The prompt and AI's plan

**Our prompt**: _"Implement a real user login with firebase"_ + firebase default app setting file.

![Cursor showing e-commerce app and AI's Firebase implementation plan](/images/verify/code/tutorials/cursor/tutorial-cursor-1.webp)

The AI responded confidently with a detailed 6-step plan:

1. **Create Firebase Initialization File** - Set up `src/lib/firebase.ts`
2. **Install Firebase** - Add the npm package  
3. **Update Authentication Context** - Modify `src/contexts/AuthContext.tsx`
4. **Update Login API Route** - Handle Firebase in `src/app/api/auth/login/route.ts`
5. **Update Signup API Route** - Handle Firebase in `src/app/api/auth/signup/route.ts`
6. **Update Login and Signup Pages** - Verify integration works

Sounds straightforward, right? Here's what actually happened.

## When AI plans meet reality

The AI's 6-step plan achieved just 17% success rate, with 4 critical failures and 1 endless correction loop.

**1. Firebase initialization** → ❌ **Issue 1: Incomplete implementation**  
**2. Install Firebase** → ✅ **Success**  
**3. Update AuthContext** → ❌ **Issue 4: Architecture regression**  
**4. Update login API** → ❌ **Issue 2: Breaking changes**  
**5. Update signup API** → ❌ **Issue 3: Security vulnerabilities**  
**6. Verify integration** → ❌ **Stuck in correction loops**

The AI got confused between steps 3-4, couldn't decide between direct Firebase calls vs API routes, kept reverting working code, and made **6+ correction attempts** throughout the implementation.

Without Verify Code, this would have been a debugging nightmare. With it, each issue was caught immediately.

## Caught by Verify Code

### Incomplete implementation

**What happened**: AI created Firebase config but missed the actual authentication setup.

**AI's incomplete code**:
```typescript
// src/lib/firebase.ts - Step 1 attempt
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

const firebaseConfig = { /* config */ };
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app); // ❌ No auth setup
```

**Verify Code alert**:
{Screenshot-HERE-Incomplete-Implementation-Alert}

**P1 - Intent (High)**: AI did not implement the actual user login functionality as requested.

**Developer impact**: Running the app would cause runtime errors when trying to authenticate - the `auth` object simply doesn't exist.

**Fixed with Verify Code guidance**:
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

**What happened**: AI removed working Firebase login logic, then got confused about the architecture.

**Original working code**:
```typescript
// src/app/api/auth/login/route.ts - Working version
export async function POST(req: NextRequest) {
  const { email, password } = await req.json();
  const userCredential = await signInWithEmailAndPassword(auth, email, password);
  return NextResponse.json({ message: "Login successful", user: user.toJSON() });
}
```

**AI's breaking change**:
```typescript
// AI's "fix" - Step 4 attempt
export async function POST(req: NextRequest) {
  return NextResponse.json({ message: "Not used for direct login" }); // ❌ Removed logic
}
```

**Verify Code alert**:

![Verify Code alert showing breaking changes detected in login API route](/images/verify/code/tutorials/cursor/tutorial-cursor-2.webp){ width="75%" }

**P1 - Intent (High)**: AI removed Firebase login implementation instead of maintaining it.

**Developer impact**: AI replaced working authentication logic with a non-functional placeholder response, breaking the API contract.

**The correction loop begins**: AI then spent 3+ attempts trying to decide whether login should happen in AuthContext or API routes, constantly switching approaches.

---

### Security vulnerabilities

**What happened**: During Step 5, AI created signup endpoint without input validation.

**AI's insecure code**:
```typescript
// src/app/api/auth/signup/route.ts - Step 5 attempt
export async function POST(request: NextRequest) {
  const body = await request.json();
  const { email, password, name } = body; // ❌ No validation!
  
  const userCredential = await createUserWithEmailAndPassword(auth, email, password);
}
```

**Verify Code alert**:

**P3 - Security (High)**: Lack of input validation for signup data.

**Developer impact**: Malformed data could crash the server, invalid emails cause Firebase errors, weak passwords accepted.

**Secure implementation**:
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

**What happened**: AI got confused during Step 3 and reverted Firebase back to localStorage approach.

**What AI should have implemented** (Step 3 goal):
```typescript
// src/contexts/AuthContext.tsx - Correct Firebase approach
const login = async (email: string, password: string) => {
  const userCredential = await signInWithEmailAndPassword(auth, email, password);
  return !!userCredential.user;
};
```

**AI's regression** (Step 3 actual):
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

**Verify Code alert**:

![Verify Code alert showing architecture regression from Firebase back to localStorage](/images/verify/code/tutorials/cursor/tutorial-cursor-3.webp){ width="75%" }

**P1 - Intent (High)**: AI reverted Firebase authentication implementation back to using localStorage and API calls.

**Developer impact**: Lost all Firebase benefits like real-time auth state, secure token management, and cross-device sessions. Back to the original problems we were trying to solve.

**The confusion deepens**: This triggered the AI to question its entire approach, leading to multiple "I apologize for the confusion" cycles.

---

## The results

Verify Code caught **4 critical issues** across a "simple" 6-step plan:

1. **Incomplete implementation** - Step 1 missed core functionality
2. **Breaking changes** - Step 4 deleted working code  
3. **Security vulnerabilities** - Step 5 ignored input validation
4. **Architecture regression** - Step 3 went backwards

### Successful implementation achieved

By following Verify Code's guidance at each step, we successfully completed the Firebase migration. Users can now register and authenticate properly.

**Firebase console showing the code@verify.com user created:**

![Firebase Authentication console showing successfully created users](/images/verify/code/tutorials/cursor/tutorial-cursor-4.webp)

**Successful login in the e-commerce app:**

![E-commerce app showing successful login with code@verify.com user](/images/verify/code/tutorials/cursor/tutorial-cursor-5.webp)

The migration from localStorage to Firebase authentication was completed without the typical debugging cycles. [Verify Code](/verify/code/) caught each issue in real-time, allowing us to fix problems immediately rather than discovering them during testing.

**Time saved**: Hours of debugging and testing cycles prevented. No more AI mistake loops.

## Key takeaway

Even with clear prompts and detailed plans, AI execution can go wrong. Verify Code acts as your safety net, catching issues before they compound into debugging nightmares.

The more complex the task, the more valuable this real-time verification becomes.

**Learn more**: Explore our [tools reference](/verify/code/tools/) to understand all issue types and priority levels that Verify Code monitors.