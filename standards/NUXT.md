# Liberu Nuxt 4 architecture

## Canonical implementation specification

**Status:** Source of truth
**Applies to:** Nuxt 4 applications, pages, layouts, components, composables, typed API clients, server routes, and deployment adapters
**Target stack:** Nuxt 4, Vue 3, TypeScript, Node.js 22+, and Liberu API modules
**Related specifications:** [MODULES.md](../architecture/MODULES.md) · [API.md](../architecture/API.md) · [THEMES.md](THEMES.md) · [projects/boilerplate/BOILERPLATE.md](../projects/boilerplate/BOILERPLATE.md) · [DOCUMENTATION.md](DOCUMENTATION.md) · [TESTING.md](TESTING.md)

## Purpose

Nuxt is an optional API-consuming presentation layer. It owns browser and server-rendered experience, routing, accessibility, loading/error states, typed API clients, and composition of the matching API contract. It does not own Laravel domain rules, persistence, authorization policy, or a second data model.

The governing rule is:

> Applications own Nuxt composition; each `module-*-nuxt` package presents exactly one matching API module; the Laravel API remains authoritative.

## Version and project baseline

Use Nuxt 4 with the current supported Node.js even-numbered release, TypeScript, Vue 3, and the package manager locked by the repository. New applications can start with:

```bash
npm create nuxt@latest app
cd app
npm install
npm run dev
```

Use `nuxt build` for the production Node server unless the application explicitly uses a tested static/prerendered deployment. Pin dependencies through the lock file and verify the supported Node version in CI.

## Mandatory naming rule

Reusable module presentation packages use:

```text
module-{independent-module-name}-nuxt
```

The same lowercase kebab-case name applies to the repository, package basename, manifest identity, and installed directory. A package may be implemented as a Nuxt layer, Nuxt module, or application-consumed package, but its public exports must use an explicit module prefix to avoid collisions.

## Ownership and dependency direction

```text
Nuxt application
├── module-cms-content-nuxt ─> module-cms-content-api
├── module-billing-invoices-nuxt ─> module-billing-invoices-api
└── theme-* ─> supported Nuxt UI extension points

Nuxt presentation -X-> Laravel private models/tables
Nuxt presentation -X-> another independent module's API internals
```

Each Nuxt package depends on exactly one matching API presentation package or its published contract and shared frontend contracts. It must not call undocumented endpoints, duplicate API validation, import Laravel classes, or access another module's API data merely for convenience. The application composes packages and owns runtime configuration, authentication integration, navigation, layouts, and cross-module workflows.

## API consumption

- Use typed clients generated or checked against the matching OpenAPI contract; keep transport code in `app/composables`, `app/utils`, or a package-local client boundary.
- Use `useFetch` or `useAsyncData` for SSR-safe initial data and `$fetch` for event-driven browser actions. Give shared async data explicit stable keys.
- Keep API base URLs and public configuration in `runtimeConfig`; expose only values intended for the browser through `runtimeConfig.public`.
- Use Sanctum cookie authentication for a first-party same-site SPA where appropriate. Never place long-lived personal access tokens in browser source, local storage, URLs, or logs.
- If a server-side proxy/BFF is required, forward only allowlisted headers/cookies and preserve authorization, tenant/team context, timeouts, correlation IDs, and error semantics.
- Map API errors into accessible, typed UI states. Never treat client-side route guards or hidden controls as authorization.
- Use API pagination, filters, idempotency keys, ETags, and operation resources as defined by [API.md](../architecture/API.md); do not recreate server-side business workflows in the client.

## Nuxt structure and quality

- Use `app/pages` for file-based routes, `app/layouts` for shared layouts, `app/components` for focused UI, `app/composables` for reusable state/data access, and `shared/` for types safe in both environments.
- Use `server/` only for deliberate Nuxt server handlers or a documented BFF; never use it to bypass the Laravel API boundary.
- Keep components small, typed, accessible, keyboard-operable, and resilient to loading, empty, error, stale, unauthorized, and offline states.
- Prefer composables and dependency injection over global mutable state. Use Pinia only when shared client state materially needs a store.
- Avoid hydration mismatches: keep browser-only APIs in client-only code and make SSR/client data keys and transforms consistent.
- Define page metadata, canonical URLs, structured data, and robots behavior deliberately; do not expose protected content through prerendering or caches.
- Use runtime validation for external API responses at trust boundaries when generated types alone are insufficient.

## Security and privacy

Apply CSP, secure cookies, HTTPS, CSRF protection for cookie-authenticated mutations, strict CORS, dependency scanning, and output escaping. Do not serialize secrets or protected API payloads into public SSR payloads. Respect API field visibility, team context, consent, retention, deletion, and audit requirements.

## Testing and deployment

Test typed API clients, composables, pages, authorization outcomes, wrong-team responses, loading/error states, SSR hydration, accessibility, navigation, and production builds. Run unit/component tests, end-to-end tests against a contract-compatible API, type checking, linting, dependency audits, and `nuxt build` in CI.

Deploy the generated Nuxt server as an immutable Node artifact behind TLS and a reverse proxy, or use a deliberately tested static target for public, non-sensitive routes. See [deployment/README.md](../deployment/README.md).

## References

- [Nuxt 4 installation](https://nuxt.com/docs/4.x/getting-started/installation)
- [Nuxt 4 data fetching](https://nuxt.com/docs/4.x/getting-started/data-fetching)
- [`useFetch`](https://nuxt.com/docs/4.x/api/composables/use-fetch)
- [Nuxt 4 server routes](https://nuxt.com/docs/4.x/directory-structure/server)
- [Nuxt 4 deployment](https://nuxt.com/docs/4.x/getting-started/deployment)
- [Liberu API architecture](../architecture/API.md)
