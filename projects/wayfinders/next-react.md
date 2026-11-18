# Wayfinder technical specification: Next.js React

This is the technology-specific implementation specification for `next-react` project hosts. Product wayfinder issues embed the method and a condensed form of this specification, and link here for the durable reference.

- Boilerplate template: https://github.com/liberusoftware/project-boilerplate-next-react
- Reusable module foundation: https://github.com/liberusoftware/module-boilerplate-nextjs
- Capability skeleton catalog: [`modules/skeletons/next-react.md`](../../modules/skeletons/next-react.md)
- Presentation layer directory in product docs: `nextjs/`
- Adapter identity pattern: `module-{capability}-nextjs`
- Consumes product `-laravel-api`: yes

## Delivery boundary

Consume the product `-laravel-api` HTTP contracts from an independently deployed Next.js App Router app; specify server/client ownership, private caching and mutation invalidation.

## Authoritative documentation

- [Next.js standard](../../standards/NEXTJS.md)
- [React standard](../../standards/REACT.md)
- [API architecture](../../architecture/API.md)
- [Laravel API backends](../../guides/LARAVEL-API-BACKENDS.md)
- [Foundation and presentation build](../../guides/presentation/README.md)
- [Next.js implementation runbook](../../guides/presentation/NEXTJS.md)
- [Package build and npm release](../../guides/presentation/PACKAGES.md)
- [Module index](../../modules/nextjs/README.md)
- [Implementation evidence](../../standards/IMPLEMENTATION-EVIDENCE.md)
- [Testing / coverage policy](../../standards/TESTING.md)

## Robust implementation method

1. Start from the Next.js React Boilerplate (or this product skeleton); `npm ci`; use `.node-version`; run lint, typecheck and production build before feature work.
2. Set `API_BASE_URL` (server-only) to the matching `project-{product}-laravel-api` origin; never put credentials in `NEXT_PUBLIC_*`; mark secret-bearing modules with `server-only`.
3. Choose and document session integration (server cookies/BFF vs token); Laravel re-authorizes every API request; Next entry points authenticate and authorize their own handlers/actions.
4. Validate/generate DTOs from the published schema; copy allowlisted fields only; preserve pagination, error shapes, conflicts and job/pending semantics.
5. Own `src/app` routes, layouts, `loading.tsx`/`error.tsx` and deployment; import capability adapters explicitly—no silent global route injection from packages.
6. Default authenticated fetches to `cache: 'no-store'` (or equivalent) until a tenant-aware cache policy is reviewed; invalidate after confirmed mutations.
7. Implement one vertical journey with accessible loading/empty/denied/validation/conflict/retry states; keep write authority in Laravel even when a server action is the browser transport.
8. Expand using `nextjs/` plans and SOURCE-MAPPING.md; coordinate contract changes in the API/domain owners—not by forking rules into React.
9. Prove evidence: server/client boundary checks, secret exclusion from bundles, cross-tenant denial, clean install/build and preview/production env separation.

## Technical specification

### Host ownership
- This repository is an independently deployed Next.js (App Router) + React client. It does not use Inertia and does not own domain persistence.
- The matching `project-{product}-laravel-api` owns authorization, tenancy, business rules and the versioned OpenAPI contract.
- Application owns `app/` routes, middleware/proxy, environment, deployment and auth integration; adapters own capability UI and typed API helpers.

### Transport and session
- Server components/route handlers call a fixed configured Laravel origin with approved credentials only.
- Cookie authentication needs explicit CSRF, origin, cookie-domain and SameSite design for the real deployment topology.
- Commands use documented operations and idempotency/version headers; show conflicts without overwriting newer data.

### Package and directory contracts
- Reusable adapters follow `module-{capability}-nextjs` with separate client-safe and server-only exports.
- Do not barrel-export server clients into client components; keep ORM/PHP types out of JavaScript packages.
- Shared presentational packages must not import `next/navigation` or Inertia APIs—inject navigation/mutation callbacks.

### Security and tenancy
- Treat every server action/route handler as a public entry point: authenticate, validate, authorize.
- Cache keys must include tenant and permission-sensitive dimensions when caching is enabled.
- Never serialize service credentials or private fields into RSC payloads or client bundles.

### Verification and release
- Test cross-tenant denial, cache isolation, expired sessions, duplicate commands and rollback after API failure.
- Deploy compatible API changes first; roll back frontend artifacts without reversing database migrations.

## Related

- [Implementation wayfinders guide](../IMPLEMENTATION-WAYFINDERS.md)
- [Issue matrix](../IMPLEMENTATION-ISSUES.md)
- [Repository map](../REPOSITORIES.md)
