# Implement the Nuxt presentation layer with Vue

Nuxt 4 is an independently deployed Vue 3 application consuming reviewed Laravel APIs. Complete the [foundation and contract steps](README.md) first. This walkthrough uses an explicitly **public** read contract for a first render, then describes protected integration. `/api/v1/example-records` and its response shape are illustrative; implement or substitute a reviewed API before running the request.

## 1. Create a private skeleton

Use the supported Node.js release (22+ under the current repository standard) and npm for a new empty application:

```bash
npm create nuxt@latest example-web -- -t v4
cd example-web
npm install
npm install --save-dev typescript vue-tsc
npm run dev
```

Choose npm in the generator and keep Nuxt on the supported 4.x major. Review the generated manifest/lock, set `private: true`, and record generator/toolchain versions. Preserve generated scripts and add `typecheck: nuxt typecheck` if absent. Keep the generated Nuxt TypeScript project references rather than replacing them with a generic Vue tsconfig. See the official [starter templates](https://github.com/nuxt/starter) and [Nuxt installation](https://nuxt.com/docs/4.x/getting-started/installation).

## 2. Arrange application-owned integration

```text
app/
  app.vue
  pages/example.vue           # application URL and page metadata
  layouts/default.vue         # navigation, theme, focus landmarks
  components/                 # application composition
  composables/                # typed transport/view state
  middleware/                 # navigation UX only
server/
  api/example-records.get.ts  # deliberate BFF, if selected
  utils/                      # server-only session/transport helpers
shared/                       # DTOs safe for browser and server
nuxt.config.ts
```

Use `app/app.vue` to render `<NuxtLayout><NuxtPage /></NuxtLayout>` and put a `<slot />` in the default layout. Keep capability UI inside its reusable package and import it explicitly; the application owns its URL. Avoid global singleton stores with per-user SSR state.

In `nuxt.config.ts`:

```ts
export default defineNuxtConfig({
  runtimeConfig: {
    apiBase: '',
    public: { applicationName: 'Example' },
  },
});
```

Set `NUXT_API_BASE=https://api.example.com` in local/deployment configuration, with a safe `.env.example`. This server-side address is not a secret by itself, but access credentials must stay private. Only intentionally public values go in `runtimeConfig.public`. Runtime deployment must supply variables explicitly; the built Node server does not rely on loading your development `.env` file.

## 3. Define and validate the public read contract

For the teaching shape `{ data: Array<{ id: string; title: string }> }`, create `shared/example.ts`:

```ts
export type ExampleRecord = { id: string; title: string };
export function parseExampleRecords(value: unknown): ExampleRecord[] {
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

Generate/check production DTOs against the actual schema; preserve pagination metadata when the endpoint is paginated. This small parser intentionally copies only allowed fields.

For a server-owned, fixed-path BFF read, create `server/api/example-records.get.ts`:

```ts
import { parseExampleRecords } from '../../shared/example';
export default defineEventHandler(async event => {
  setHeader(event, 'Cache-Control', 'private, no-store');
  const config = useRuntimeConfig(event);
  try {
    const value = await $fetch<unknown>('/api/v1/example-records', {
      baseURL: config.apiBase,
      headers: { Accept: 'application/json' },
      timeout: 10000,
      retry: 0,
    });
    return parseExampleRecords(value);
  } catch {
    throw createError({ statusCode: 502, statusMessage: 'Records unavailable' });
  }
});
```

This handler intentionally forwards no user credentials and is suitable only for a public API. It is not a generic authenticated proxy. Keep the upstream origin deployment-controlled; do not accept arbitrary target URLs/headers from a browser. Add request IDs and redacted server diagnostics without returning upstream internals.

## 4. Render a Vue page with SSR-safe data

Create `app/pages/example.vue`:

```vue
<script setup lang="ts">
const { data, status, error, refresh } = await useFetch('/api/example-records', {
  key: 'public-example-records',
});
</script>

<template>
  <main>
    <h1>Records</h1>
    <p v-if="status === 'pending'" role="status">Loading records…</p>
    <div v-else-if="error" role="alert">
      Records could not be loaded. <button @click="refresh()">Retry</button>
    </div>
    <p v-else-if="!data?.length">No records available.</p>
    <ul v-else><li v-for="record in data" :key="record.id">{{ record.title }}</li></ul>
  </main>
</template>
```

Use `useFetch`/`useAsyncData` for initial SSR data, and event-driven `$fetch` for mutations; avoid duplicate mounted requests and hydration mismatches. Replace list markup with the explicit component export from `module-<capability>-nuxt` when that adapter exists. Keep data-fetch keys scoped to user/workspace/filter when appropriate and clear them on context changes. See [Nuxt data fetching](https://nuxt.com/docs/4.x/getting-started/data-fetching).

## 5. Integrate authenticated reads and commands

Choose and document one authentication topology before extending the public example:

1. **Direct first-party Sanctum cookies:** configure Laravel stateful domains, exact allowed frontend origins, credentialed CORS, secure session cookies and the reviewed cookie domain. Initialize CSRF with `/sanctum/csrf-cookie`, send cookies with requests, and send the decoded XSRF token in the required header for writes. Login/logout use the foundation identity routes. A generic `$fetch` call does not automatically implement every Sanctum CSRF step.
2. **Server session/BFF:** use the approved identity integration to establish an HttpOnly/Secure browser session and store upstream credentials on the server. Resolve that session separately for each request. A protected Nitro handler retrieves only that session's credential, calls a fixed reviewed API route, and returns a minimal DTO. Do not replace user authorization with a shared administrator token.

For SSR with a cookie topology, forward only the reviewed credential/context headers to the fixed trusted API origin on that request. Never share cookies/transport instances across users. Route middleware improves navigation UX; the Laravel API must still authorize every read/write. See [Laravel Sanctum](https://laravel.com/docs/13.x/sanctum).

Implement a command end to end:

1. Create a typed form/composable with field values, pending flag and field-error map; native browser validation can help input UX but does not replace owner validation.
2. In the submit handler, send the exact reviewed payload and credential/CSRF context to the fixed API or BFF POST route. Cookie-authenticated BFF writes also need an explicit CSRF/origin defense. Never automatically replay writes after ambiguous network failure.
3. Map actual contract status codes: 401 to reauthentication while protecting the draft, 403 to denied access, 422 to field errors, 409 to conflict review, 429 to bounded retry guidance, and 202 to an operation reference/polling flow. Preserve safe upstream status semantics in protected BFF handlers rather than using the public example's generic 502 mapping.
4. On confirmed completion, refresh/invalidate only the affected scoped reads. If the command is pending, show pending and query the owner operation. Use idempotency/version headers only when implemented by the API.
5. Clear cached data and credentials according to logout, revocation and workspace-switch policy. Never prerender or publicly cache authenticated payloads; include SSR serialized data in the privacy review.

## 6. Package Vue UI or a Nuxt layer

For ordinary components/composables, use the [Vue library recipe](PACKAGES.md#3-vue-library), peer Vue/Nuxt only when imported, inject transport, and avoid application aliases/config. Keep Nuxt-specific composables separate from Vue-neutral UI.

For a layer containing components/layouts/composables, create a package with a `nuxt.config.ts`, the used `app/` directories and a files allowlist including those source files. Export `./nuxt.config` to that config (and its documented root entry if desired). In the consuming application's config explicitly add `extends: ['@example/module-example-nuxt/nuxt.config']`. Use prefixed names and avoid injecting application routes by surprise. The layer ships source for Nuxt to compile; test its tarball in a fresh Nuxt application. See [Nuxt layers](https://nuxt.com/docs/4.x/guide/going-further/layers).

For a true Nuxt module that registers runtime integration, scaffold the official module template (`npm create nuxt@latest module-example-nuxt -- -t module`), retain its module-builder scripts, and build its declared `dist` entry. Do not publish the example app or pretend a source layer has the same artifact as a compiled module. Run [the npm release procedure](PACKAGES.md) for the chosen format.

## 7. Verify and deploy

Run `npm ci`, `npm run typecheck`, declared lint/tests and `npm run build`; smoke-test the generated Node artifact with `node .output/server/index.mjs` and deployment environment variables. Add contract/component/E2E coverage for session expiry, wrong tenant, invalid fields, conflicts, pending operations, hydration and two concurrent users with isolated data.

Deploy `.output` to the selected supported Nitro target behind TLS. Use runtime environment settings, readiness checks, structured redacted logs, compatible API rollout and artifact rollback. Static generation is suitable only for deliberately public content: it cannot replace this runtime BFF or authenticated SSR. See [Nuxt deployment](https://nuxt.com/docs/4.x/getting-started/deployment) and [the Nuxt standard](../../standards/NUXT.md).
