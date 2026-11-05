# Implement the Next.js presentation layer with React

## Liberu boilerplate repository

Start from [project-boilerplate-next-react](https://github.com/liberusoftware/project-boilerplate-next-react), a Next.js and React application template with a committed npm lockfile, architecture guidance and CI checks:

```bash
gh repo create YOUR-OWNER/YOUR-PROJECT --template liberusoftware/project-boilerplate-next-react --private --clone
cd YOUR-PROJECT
cp .env.example .env.local
npm ci
npm run dev
```

Use the Node version in `.node-version`. Run `npm run lint`, `npm run typecheck` and `npm run build` before extending it. The shell does not implement authentication or a product API; follow the contract and tenant boundaries below when adding those workflows.


Next.js is a separate React application consuming reviewed Laravel APIs. Start with the [foundation and contract guide](README.md). Laravel remains the domain owner; Next.js owns routes, server/client composition, session integration and deployment. Do not add Inertia to this shell. Example endpoints/types below must be replaced with the actual reviewed API.

## 1. Generate a private App Router skeleton

```bash
npx create-next-app@latest example-web --typescript --eslint --app --src-dir --use-npm
cd example-web
npm run dev
```

Review prompts and selected versions against [the Next.js standard](../../standards/NEXTJS.md); keep the supported React/framework pair, Node version and lockfile in CI. Set `private: true`, record the generator version, retain generated scripts and add `typecheck: tsc --noEmit`. Check the selected linter command; do not assume `next lint` exists. See [official installation](https://nextjs.org/docs/app/getting-started/installation).

## 2. Establish the skeleton directories

```text
src/app/layout.tsx                # app theme, landmarks, metadata
src/app/example/page.tsx          # application-owned route
src/app/example/loading.tsx       # accessible loading feedback
src/app/example/error.tsx         # client error boundary and retry
src/app/api/                      # only deliberate BFF route handlers
src/components/                  # application composition
src/lib/server/                  # request-scoped session and API integration
src/lib/contracts/               # generated/checked DTOs
```

Retain the generated root layout and global CSS. Keep tokens and presentational components reusable; select capability adapters via explicit package imports. Do not import application code into a reusable library.

## 3. Implement a server-only public read

Install the server-boundary guard and create `src/lib/server/example.ts`:

```bash
npm install server-only
```

```ts
import 'server-only';
export type ExampleRecord = { id: string; title: string };

export async function loadPublicRecords(): Promise<ExampleRecord[]> {
  const base = process.env.API_BASE_URL;
  if (!base) throw new Error('API_BASE_URL is required');
  const response = await fetch(new URL('/api/v1/example-records', base), {
    headers: { Accept: 'application/json' },
    cache: 'no-store',
    signal: AbortSignal.timeout(10000),
  });
  if (!response.ok) throw new Error('Records unavailable');
  const value: unknown = await response.json();
  if (typeof value !== 'object' || value === null || !('data' in value)
    || !Array.isArray(value.data)) throw new Error('Invalid API response');
  return value.data.map((item: unknown) => {
    if (typeof item !== 'object' || item === null
      || !('id' in item) || typeof item.id !== 'string'
      || !('title' in item) || typeof item.title !== 'string') {
      throw new Error('Invalid API record');
    }
    return { id: item.id, title: item.title };
  });
}
```

Set `API_BASE_URL=https://api.example.com` in local/deployment environment; never use a `NEXT_PUBLIC_` variable for a credential. This function intentionally uses a public read contract and no authentication. It copies allowed fields, disables storage caching and bounds waiting. Replace the parser with schema-generated/checked mapping and preserve pagination where needed. The API origin is trusted deployment configuration, not user input.

Create `src/app/example/page.tsx`:

```tsx
import { loadPublicRecords } from '@/lib/server/example';
export const dynamic = 'force-dynamic';
export default async function ExamplePage() {
  const records = await loadPublicRecords();
  return <main>
    <h1>Records</h1>
    {records.length === 0 ? <p>No records available.</p> :
      <ul>{records.map(record => <li key={record.id}>{record.title}</li>)}</ul>}
  </main>;
}
```

This sample assumes Cache Components is disabled; if enabling it, use the selected Next.js version's supported dynamic-data/Suspense conventions instead of unsupported route-segment options. Use `loading.tsx` to return a status message and `error.tsx` with `'use client'`, a generic error message and a button invoking its `reset` prop. Log diagnostic details only through the server's redacted logger. See [data fetching](https://nextjs.org/docs/app/getting-started/fetching-data) and [server/client components](https://nextjs.org/docs/app/getting-started/server-and-client-components).

## 4. Add a small interactive boundary

A reusable list can be a Server Component when it only renders data. Put `'use client'` at the top of search/filter/form components that use state, effects or event handlers. Pass only serializable authorized DTOs into them; ordinary server callbacks cannot cross the boundary. Keep server-only imports, session credentials and secret configuration outside their import graph.

For a form, use a focused client component that tracks input/pending/field errors and submits either to an explicit Route Handler or to a documented Server Action. The application owns the URL/action wiring and refresh behavior; the reusable component emits command intent and renders outcomes. Use accessible labels, error descriptions, focus management and keyboard controls.

## 5. Establish a protected session before adding commands

Choose a reviewed authentication topology compatible with the foundation identity/API modules:

1. A server-session BFF keeps upstream tokens in server-managed session storage; the browser receives only an HttpOnly/Secure session cookie with deliberate SameSite settings. Integrate the approved login/callback/logout mechanism, rotate sessions and expire/revoke them. OAuth native/public-client assumptions do not apply to this confidential server integration.
2. If using direct first-party Sanctum cookies, configure stateful domains, exact credentialed CORS and cookie domain, initialize `/sanctum/csrf-cookie`, and implement its XSRF header for writes. SSR forwarding must be request-scoped and limited to the trusted API origin. See [Sanctum](https://laravel.com/docs/13.x/sanctum).

Implement a request-scoped server session resolver using the application's reviewed identity integration. When using Next.js cookies APIs, follow the installed version's asynchronous API. Never use a process-global current user/token, a browser-submitted actor ID, or a shared administrator API token to impersonate users. Hidden routes and client guards do not authorize anything.

To turn the public read into a protected read, resolve the current session, send its credential and established context to the fixed Laravel endpoint, map only authorized fields, disable shared caching, and handle 401/403 distinctly. Never call the public example for protected data while silently omitting credentials. Test two simultaneous users/tenants through SSR and client navigation.

## 6. Implement the command path

For a Route Handler, place a POST handler at a fixed path such as `src/app/api/example-records/route.ts`. For a Server Action, place `'use server'` functions in an application-owned server module. In either case implement the same steps:

1. Resolve and verify the session on every invocation. Validate the request's origin/CSRF policy for cookie-authenticated writes; do not assume that using a BFF automatically supplies CSRF defense. Bound body sizes, timeouts and supported content types.
2. Parse only the reviewed command fields. Establish workspace context through the identity/API integration and forward only allowlisted auth/context/correlation headers to a fixed trusted API endpoint. Do not proxy arbitrary URLs or echo arbitrary upstream headers/cookies.
3. Let Laravel authorize and validate against its canonical owner. Map 401/403/422/409/429 and operation outcomes into the typed UI result. Return field errors without upstream stack traces or private records. A Server Action is a reachable server entry and needs the same checks as a public endpoint.
4. Return confirmed completion, pending operation reference, invalid input or conflict as distinct outcomes. Do not blindly retry an uncertain write; reconcile it using the owner's operation or idempotency contract.
5. Refresh the affected route/read only after confirmed success, or poll the authorized operation when pending. Scope cache tags to the actual tenant/resource if caching is deliberately introduced; default protected reads to no-store. On logout/context changes clear client state and prevent protected history/caches from displaying previous-user content.

Test these status mappings and the real owner operation rather than returning a local fake success. See [Next.js mutation guidance](https://nextjs.org/docs/app/getting-started/updating-data).

## 7. Extract and build the React adapter

Implement `module-<capability>-nextjs` according to its [ownership plan](../../modules/nextjs/OWNERSHIP.md). Share framework-neutral React UI with React/Inertia where compatible; isolate `next/navigation`, `next/link`, session and server imports in Next.js-specific wrappers. The app retains route files and composition.

Use the [React library recipe](PACKAGES.md#2-react-library). Add explicit `./client` and `./server` exports as needed; preserve `'use client'`, server-only guards, declarations and required styles. Declare compatible React/Next peers only where used, and externalize framework runtimes. Document API versions and cache/session assumptions. Install the packed artifact in a fresh Next.js consumer and run typecheck plus a production build before following the [npm publication steps](PACKAGES.md#6-publish-the-reviewed-tarball).

## 8. Verify and deploy the application

Run `npm ci`, `npm run typecheck`, the declared linter/tests and `npm run build`. Start the production artifact with `npm run start` (or the selected standalone/container output) and smoke-test actual navigation and a protected command. Add component/contract/E2E checks for errors, denied/wrong-tenant access, cache isolation, session expiry, hydration, concurrent edits and asynchronous results.

Deploy a supported Node/container platform with runtime secrets, TLS, health checks, redacted diagnostics and the compatible API. If using standalone output, copy the required static/public assets as documented for that target. A static export cannot run the BFF/Server Actions in this guide. Retain a known-good artifact for rollback and maintain API compatibility throughout deployment. See [Next.js deployment](https://nextjs.org/docs/app/getting-started/deploying).
