# Wayfinder technical specification: Laravel Inertia React

This is the technology-specific implementation specification for `laravel-inertia-react` project hosts. Product wayfinder issues embed the method and a condensed form of this specification, and link here for the durable reference.

- Boilerplate template: https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react
- Reusable module foundation: https://github.com/liberusoftware/module-boilerplate-react-inertia
- Capability skeleton catalog: [`modules/skeletons/laravel-inertia-react.md`](../../modules/skeletons/laravel-inertia-react.md)
- Presentation layer directory in product docs: `react/`
- Adapter identity pattern: `module-{capability}-react-inertia`
- Consumes product `-laravel-api`: no (Laravel/Inertia host; HTTP API optional)

## Delivery boundary

Laravel routes, sessions and CSRF own mutations; page components receive allowlisted Inertia props. A separate HTTP API is optional for these pages.

## Authoritative documentation

- [Inertia standard](../../standards/INERTIA.md)
- [React standard](../../standards/REACT.md)
- [Laravel standard](../../standards/LARAVEL.md)
- [Themes](../../standards/THEMES.md)
- [Foundation and presentation build](../../guides/presentation/README.md)
- [Inertia Vue/React implementation runbook](../../guides/presentation/INERTIA.md)
- [React package build and npm release](../../guides/presentation/PACKAGES.md)
- [Module index](../../modules/react/README.md)
- [Implementation evidence](../../standards/IMPLEMENTATION-EVIDENCE.md)
- [Testing / coverage policy](../../standards/TESTING.md)

## Robust implementation method

1. Clone or open this host from the matching Boilerplate template; install from committed Composer and npm lockfiles; configure local `.env`; run migrations and the host test suite before feature work.
2. Confirm Inertia 3 middleware is registered once on the `web` group; share only minimal actor, workspace and navigation props—never full models, tokens or secrets.
3. Install or verify React 19.2 + `@inertiajs/react` + Vite; keep `private: true`, typecheck and build scripts; commit lockfile changes with dependency review.
4. Resolve pages explicitly under `resources/js/Pages`; keep layouts, navigation and session composition application-owned.
5. For each capability: read `core/`, `api/` (if used) and `react/` plans plus SOURCE-MAPPING.md; identify the exact Composer/npm identities before requiring packages.
6. Deliver one vertical journey (auth context → authorized read → command → authoritative result) with loading/empty/denied/validation/conflict states and accessibility.
7. Prefer public application actions from domain modules; if an HTTP adapter is used inside the host, treat it as an internal transport—do not invent endpoints to match screens.
8. Keep installed `/modules` and `/themes` tracked in the host; bump source releases and lockfiles together; never fork domain rules into React.
9. Prove evidence: feature/browser tests for the journey, policy/tenant denial, CSRF/session behavior, SSR/hydration if enabled, clean `composer install` + `npm ci` + production build.

## Technical specification

### Host ownership
- This repository is a Laravel application composition root with React pages over Inertia 3.
- Domain modules own persistence, policies, transitions and jobs; React owns UI state, forms and presentation mapping only.
- Routes, middleware, authorization, validation, redirects and shared props remain Laravel-owned.

### Transport and session
- Mutations use Laravel session + CSRF; Inertia form/visit semantics apply (`Link`, `router`, partial reloads, deferred props).
- Controllers invoke authorized public actions/queries and return props or redirects—not ad-hoc REST JSON unless a deliberate API surface exists.
- Preserve correlation IDs, idempotency keys, pagination and concurrency/revision headers where the contract defines them.

### Package and directory contracts
- Reusable adapters follow `module-{capability}-react-inertia` and export pages/components without global discovery collisions.
- Application owns `resources/js` boot, Blade root template, Vite entry, navigation and deployment.
- Themes supply tokens/appearance via the theme policy; do not hard-code a second design system.

### Security and tenancy
- Re-check authorization and Team/Store (or tenant) context server-side on every mutation and sensitive query.
- Allowlist page props; exclude private fields from shared/public caches and SSR payloads.
- Revision conflicts and duplicate submits must be visible and recoverable without silent overwrite.

### Verification and release
- Independent domain/adapter tests plus at least one host journey; follow the coverage policy and evidence standard.
- Release with locked installs, reviewed dependency diffs, operational signals and upgrade/rollback notes.

## Related

- [Implementation wayfinders guide](../IMPLEMENTATION-WAYFINDERS.md)
- [Issue matrix](../IMPLEMENTATION-ISSUES.md)
- [Repository map](../REPOSITORIES.md)
