# Liberu Vue 3 + Inertia 3 architecture

## Canonical implementation specification

**Status:** Source of truth  
**Applies to:** Vue pages, layouts, components, composables, typed clients, Inertia forms, navigation, SSR, and Vite builds  
**Target stack:** Vue 3, Inertia.js 3, `@inertiajs/vue3`, TypeScript, Vite, Node.js 22+, Laravel 13, PHP 8.5, and Liberu API modules  
**Related specifications:** [MODULES.md](MODULES.md) · [API.md](API.md) · [THEMES.md](THEMES.md) · [NUXT.md](NUXT.md) · [DOCUMENTATION.md](DOCUMENTATION.md) · [TESTING.md](TESTING.md)

## Purpose

Vue + Inertia is an optional presentation layer for Laravel applications. It owns page composition, browser interaction, accessibility, loading and error states, typed client behavior, and navigation. Laravel remains authoritative for authentication, authorization, validation, team/tenant context, persistence, and domain rules.

> Applications compose Vue/Inertia surfaces; each `module-*-vue-inertia` package presents exactly one matching API module; the Laravel application remains the composition and authorization boundary.

## Package and directory rules

Reusable packages use:

```text
module-{independent-module-name}-vue-inertia
```

The canonical package layout is:

```text
resources/js/
├── Pages/                 # Inertia page components owned by this module
├── Components/            # focused module UI
├── Layouts/               # package-local layout adapters only
├── composables/           # typed, module-local Vue composables
├── lib/                   # API, error, and formatting adapters
├── types/                 # safe shared frontend contracts
└── index.ts               # explicit public exports
resources/css/
routes/
src/                       # PHP provider/manifest integration only
tests/
```

Use PascalCase for Vue SFC files, `camelCase` for composables and utilities, and explicit package prefixes for routes, DOM IDs, events, and exports. Create only directories the package uses.

## Ownership and dependency direction

```text
Laravel application
├── module-cms-pages-vue-inertia ─> module-cms-pages-api
├── module-billing-invoices-vue-inertia ─> module-billing-invoices-api
└── theme-* ─> supported Vue/Inertia extension points

Vue presentation -X-> Laravel private models/tables
Vue presentation -X-> another module's private API internals
```

The application owns `createInertiaApp`, root layouts, authentication integration, runtime configuration, global navigation, and cross-module workflows. A module owns only its matching pages and adapters. Themes style documented extension points and never add domain behavior or replace authorization.

## Inertia and API consumption

- Use Laravel named routes and Inertia visits for same-origin navigation; use `Link`, `router`, `useForm`, and typed page props.
- Consume only the matching API contract and keep transport code behind a typed module-local boundary.
- Use partial reloads, deferred props, remembered state, polling, and optimistic UI only when freshness, authorization, rollback, and failure behavior are explicit.
- Validate client input for usability, but rely on Laravel/API validation, authorization, concurrency, idempotency, and business invariants.
- Use Sanctum cookie authentication for same-site first-party applications. Never store long-lived tokens in local storage, URLs, source, SSR payloads, or logs.
- Preserve team/tenant context, correlation IDs, idempotency keys, ETags/`If-Match`, pagination, and RFC 9457 errors defined by [API.md](API.md).

## Vue quality, SSR, and accessibility

Use `<script setup lang="ts">`, typed props/emits, focused components, composables over global mutable state, and stable keys. Components must handle loading, empty, stale, error, unauthorized, forbidden, offline, and success states. Avoid hydration mismatches by keeping browser-only APIs in client-only code and using consistent Inertia props.

Use semantic HTML, labels, focus management, reduced-motion support, localization, RTL support, and automated accessibility checks. Client visibility is never authorization. Do not expose protected props through public caching or prerendering.

## Security, testing, and deployment

Apply CSP, secure cookies, HTTPS, CSRF protection for cookie-authenticated mutations, strict origin policy, dependency scanning, output escaping, and safe file handling. Never serialize secrets or unnecessary personal data into page props.

Test package registration and collision boundaries, typed clients, SFCs, composables, forms, authorization outcomes, wrong-team responses, loading/error states, accessibility, navigation, SSR hydration where enabled, and production builds. Use TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, dependency audits, and `npm run build` in CI. The application proves cross-module composition; the API/domain package proves business invariants.

Deploy compiled Vite assets with Laravel. If SSR is enabled, run the reviewed Inertia SSR Node process as a separate supervised service behind the trusted web boundary.

## Themes

Vue/Inertia themes consume the shared tokens and extension-point contracts in [THEMES.md](THEMES.md). A theme may provide Vue SFCs, layouts, composables for presentation state, CSS, and assets, but it must not own module actions or server authorization. The same theme identity may expose technology adapters such as `theme-corporate`, `theme-corporate-livewire`, `theme-corporate-react-inertia`, `theme-corporate-vue-inertia`, and `theme-corporate-nuxt`.

## References

- [Vue 3](https://vuejs.org/guide/introduction.html)
- [Inertia Vue 3 adapter](https://inertiajs.com/docs/v3/installation/vue)
- [Inertia server-side adapter](https://inertiajs.com/docs/v3/installation/server-side)
- [Vite](https://vite.dev/guide/)
- [Liberu API architecture](API.md)
