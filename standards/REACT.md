# Liberu React 19.2 + Inertia 3 architecture

## Canonical implementation specification

**Status:** Source of truth
**Applies to:** React pages, layouts, components, hooks, typed API clients, Inertia forms, navigation, SSR, and frontend builds
**Target stack:** React 19.2, Inertia.js 3, `@inertiajs/react`, TypeScript, Vite, Node.js 22+, Laravel 13, PHP 8.5, and Liberu API modules
**Related specifications:** [MODULES.md](../architecture/MODULES.md) · [API.md](../architecture/API.md) · [THEMES.md](THEMES.md) · [projects/boilerplate/BOILERPLATE.md](../projects/boilerplate/BOILERPLATE.md) · [DOCUMENTATION.md](DOCUMENTATION.md) · [TESTING.md](TESTING.md)

## Purpose

React + Inertia is an optional presentation layer. It owns browser experience, page composition, accessibility, loading and error states, typed client behavior, and navigation over Laravel routes. Laravel remains authoritative for authentication, authorization, validation, team context, persistence, and domain rules.

The governing rule is:

> Applications compose React/Inertia surfaces; each `module-*-react-inertia` package presents exactly one matching API module; the Laravel application remains the composition and authorization boundary.

## Version baseline

Use the current supported patch releases of React 19.2, `react-dom` 19.2, Inertia.js 3, `@inertiajs/react` 3, TypeScript, Vite, and the repository's supported even-numbered Node.js release. Pin exact resolutions through the lock file and update them through review and CI. Do not use Create React App for new work.

```bash
npm install react@^19.2 react-dom@^19.2 @inertiajs/react@^3
npm install --save-dev typescript vite @vitejs/plugin-react
```

The application must use the Laravel Inertia server adapter and the official React adapter. Keep the actual compatible package versions in the application lock file; this document defines the supported major-line baseline rather than bypassing dependency resolution.

## Package and directory rules

Reusable packages use:

```text
module-{independent-module-name}-react-inertia
```

The package presents one matching API module and lives under `/modules/{installer-name}`. A canonical package layout is:

```text
resources/js/
├── Pages/                 # Inertia page components owned by this module
├── Components/            # focused module UI
├── Layouts/               # package-local layout adapters only
├── hooks/                 # typed, module-local React hooks
├── lib/                   # API/error/formatting adapters
├── types/                 # safe shared frontend contracts
└── index.ts               # explicit public exports
resources/css/
routes/                    # package-owned route declarations, if required
src/                      # PHP provider/manifest integration only
tests/
```

Use PascalCase for React component files, `camelCase` for hooks and utilities, and explicit package prefixes for route names, DOM IDs, events, and exports. Create only directories that are used.

## Ownership and dependency direction

```text
Laravel application
├── module-genealogy-people-react-inertia ─> module-genealogy-people-api
├── module-billing-invoices-react-inertia ─> module-billing-invoices-api
└── theme-* ─> supported React/Inertia extension points

React presentation -X-> Laravel private models/tables
React presentation -X-> another module's private API internals
```

The application owns `createInertiaApp`, root layouts, authentication integration, runtime configuration, global navigation, and cross-module workflows. A module package owns only its matching pages and adapters. Themes may style supported extension points but may not add domain behavior or replace authorization.

## Inertia and API consumption

- Use Laravel named routes and Inertia visits for same-origin page navigation; use `Link`, `router`, and `useForm` rather than duplicating server routing.
- Consume only the matching API contract, with generated or hand-checked TypeScript types derived from its OpenAPI schema. Keep transport code behind a typed module-local boundary.
- Use partial reloads, deferred props, polling, remembered state, and optimistic UI only when their authorization, freshness, rollback, and failure semantics are explicit.
- Treat page props, form data, query strings, headers, events, and uploaded files as untrusted input. Validate at the server boundary and again in the authoritative domain action.
- Use Sanctum cookie authentication for same-site first-party Inertia applications. Never store long-lived tokens in local storage, URLs, source, SSR payloads, or logs.
- Preserve team context, correlation IDs, idempotency keys, ETags/`If-Match`, pagination, and RFC 9457 errors defined by [API.md](../architecture/API.md).
- Do not expose protected props through public caching or prerendering. Use explicit shared props and redact sensitive fields.

## React quality and accessibility

Keep components focused, typed, keyboard-operable, resilient to loading/empty/error/unauthorized/offline states, and free of hidden authorization assumptions. Prefer composition and hooks over global mutable state. Use stable keys, avoid unnecessary effects, clean up subscriptions, and preserve state intentionally across Inertia navigations. Use semantic HTML, labels, focus management, reduced-motion support, localization, RTL support, and automated accessibility checks.

## Security, testing, and deployment

Apply CSP, secure cookies, HTTPS, CSRF protection for cookie-authenticated mutations, strict origin policy, dependency scanning, output escaping, and safe file handling. Never serialize secrets or unnecessary personal data into page props.

Test package registration and collision boundaries, typed clients, pages, forms, authorization outcomes, wrong-team responses, loading/error states, accessibility, navigation, SSR hydration where enabled, and production builds. Use TypeScript, ESLint, Vitest, React Testing Library, Playwright, dependency audits, and `npm run build` in CI. The application proves cross-module composition; the API/domain package proves business invariants.

Deploy the compiled Vite assets with the Laravel application and serve them through the chosen deployment target. For SSR, run the reviewed Inertia SSR Node process as a separate supervised service and keep it behind the trusted web boundary. See [deployment/README.md](../deployment/README.md).

## References

- [React versions](https://react.dev/versions)
- [React 19.2 release](https://react.dev/blog/2025/10/01/react-19-2)
- [React versioning policy](https://react.dev/community/versioning-policy)
- [Inertia.js v3 documentation](https://inertiajs.com/docs/v3/getting-started)
- [Inertia React adapter](https://inertiajs.com/docs/v3/installation/react)
- [Inertia Laravel adapter](https://inertiajs.com/docs/v3/installation/server-side)
- [Vite](https://vite.dev/guide/)
- [Liberu API architecture](../architecture/API.md)
