# Wayfinder technical specification: Nuxt Vue

This is the technology-specific implementation specification for `nuxt-vue` project hosts. Product wayfinder issues embed the method and a condensed form of this specification, and link here for the durable reference.

- Boilerplate template: https://github.com/liberusoftware/project-boilerplate-nuxt-vue
- Presentation layer directory in product docs: `nuxt/`
- Adapter identity pattern: `module-{capability}-nuxt`
- Consumes product `-laravel-api`: yes

## Delivery boundary

Consume the product `-laravel-api` HTTP contracts from an independently deployed Nuxt 4 Vue app; isolate authenticated SSR caches and hydration by actor and tenant.

## Authoritative documentation

- [Nuxt standard](../../standards/NUXT.md)
- [Vue standard](../../standards/VUE.md)
- [API architecture](../../architecture/API.md)
- [Laravel API backends](../../guides/LARAVEL-API-BACKENDS.md)
- [Foundation and presentation build](../../guides/presentation/README.md)
- [Nuxt implementation runbook](../../guides/presentation/NUXT.md)
- [Package build and npm release](../../guides/presentation/PACKAGES.md)
- [Module index](../../modules/nuxt/README.md)
- [Implementation evidence](../../standards/IMPLEMENTATION-EVIDENCE.md)
- [Testing / coverage policy](../../standards/TESTING.md)

## Robust implementation method

1. Start from the Nuxt Vue Boilerplate (or this product skeleton); `npm ci` from the lockfile; pin Node from `.node-version`; run typecheck/build before feature work.
2. Configure runtime `apiBase` (server-side) to the matching `project-{product}-laravel-api` origin; never accept arbitrary upstream URLs from the browser; keep credentials out of `runtimeConfig.public`.
3. Establish auth/session integration for the deployment (cookie/BFF or token) with CSRF/origin rules; Laravel remains authoritative for policy and tenancy.
4. Generate or validate DTOs against the published OpenAPI/schema; map only allowlisted fields; preserve pagination, errors, conflicts and pending-operation semantics.
5. Own `app/pages`, layouts and middleware in the application; import reusable Nuxt/Vue adapters explicitly—packages must not install silent global routes.
6. For SSR: scope fetches and caches to authenticated actor + tenant; default authenticated reads to private/`no-store` until a reviewed cache policy exists.
7. Implement one vertical journey with loading/empty/denied/validation/conflict/retry states; use deliberate BFF handlers only when the boundary is documented.
8. Expand capability-by-capability using `nuxt/` plans, SOURCE-MAPPING.md and reviewed package identities; do not invent endpoints for UI convenience.
9. Prove evidence: contract tests or typed client checks, SSR cache isolation, cross-tenant denial, clean install/build, and deployment env validation.

## Technical specification

### Host ownership
- This repository is an independently deployed Nuxt 4 + Vue 3 client. It is not an Inertia host and does not own domain persistence.
- The matching `project-{product}-laravel-api` composes domain + API adapters and publishes the versioned HTTP contract.
- Application owns routes, layouts, runtime config, BFF handlers (if any) and deployment; adapters own capability UI and transport mapping.

### Transport and session
- All product data access uses reviewed HTTP contracts; configure a fixed API base URL per environment.
- Browser cookie sessions require explicit origin, CSRF and cookie-domain design across Nuxt and Laravel hosts.
- Forward only approved credentials/headers; never proxy arbitrary user-selected upstreams.

### Package and directory contracts
- Reusable adapters follow `module-{capability}-nuxt`; share DTOs that mirror the public API—never PHP models.
- Keep capability UI importable; avoid global singleton stores that leak per-user SSR state across requests.
- Themes/tokens remain technology-neutral where shared; Nuxt applies them in application layout.

### Security and tenancy
- Authorize every server handler and rely on Laravel re-authorization for every API call.
- Isolate SSR payloads and caches by actor and tenant; never cache private data under a public URL key alone.
- Map 401/403/409/422/429 distinctly; support idempotent retries and revision conflicts per contract.

### Verification and release
- Verify SSR hydration safety, cache isolation, secret exclusion from client bundles and one full host journey.
- Deploy API-compatible contract versions before dependent clients; monitor auth failures and upstream errors.

## Related

- [Implementation wayfinders guide](../IMPLEMENTATION-WAYFINDERS.md)
- [Issue matrix](../IMPLEMENTATION-ISSUES.md)
- [Repository map](../REPOSITORIES.md)
