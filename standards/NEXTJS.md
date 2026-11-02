# Next.js presentation modules

**Status:** proposed architecture; package names in design documents do not prove that packages have been published. Confirm implementations in the [source inventory](../architecture/SOURCE-INVENTORY.md) before installation.

## Choose the application boundary

Next.js is a React framework with its own routing, server rendering, and data fetching. Inertia keeps Laravel routing and controllers and returns React page props through the Inertia protocol. Use a Laravel/Inertia application for server-owned navigation, or a Next.js application consuming the Laravel API for independently deployed web experiences. Sharing React does not make their page, link, form, or authentication adapters interchangeable.

Share accessible components, design tokens, formatting functions, and schema-derived types through framework-independent packages. Inject navigation and mutation callbacks rather than importing `@inertiajs/react` or `next/navigation` in shared components. Keep the API contract authoritative and keep pricing, permissions, accounting, and workflow transitions in core services.

References: [Next.js getting started](https://nextjs.org/docs/app/getting-started), [server and client components](https://nextjs.org/docs/app/getting-started/server-and-client-components), and [Inertia request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works).

## Package and application layout

A proposed `module-{domain}-nextjs` package exports module components, typed API adapters, and optional server helpers through explicit exports. It must document compatible Next.js/React peer dependency ranges. The consuming application owns `app/` routes, layouts, middleware or proxy configuration, environment variables, deployment, and authentication integration. Packages must not silently install global routes.

```text
packages/module-example-nextjs/
  src/components/       # interactive UI with explicit client boundaries
  src/contracts/        # generated API types
  src/server/           # server-only API integration
  src/index.ts          # public client-safe exports
  package.json
apps/portal/app/
  layout.tsx
  example/page.tsx       # application-owned route composition
  example/loading.tsx
  example/error.tsx
```

Use separate exports for server helpers; mark secret-bearing integration code server-only. Client components receive serializable view data and permitted actions. Avoid importing a complete server client into a client component through a barrel export. Keep ORM models and PHP internals outside JavaScript packages.

## Request, session, and tenant flow

1. The browser requests an application-owned route. Resolve the session on the server using the deployment's approved session or identity integration.
2. Resolve the active tenant from authenticated membership. A URL or submitted tenant ID is a selection, never proof of access.
3. A server API adapter calls a fixed, configured Laravel origin. Forward only the approved credentials and headers; never let user input select an arbitrary upstream host.
4. Laravel policies authorize the query or command. Return an explicit DTO with permitted fields, pagination, and version metadata.
5. Render the page or return structured action errors. Preserve validation fields, distinguish authentication from permission failures, and provide retry guidance for temporary failures.

A server action or route handler is a public entry point: authenticate, validate, and authorize every invocation. Laravel must independently authorize every API request. Never put service credentials in `NEXT_PUBLIC_` variables or serialized page data. Cookie authentication requires an explicit CSRF, origin, cookie-domain, and SameSite design for the actual deployment; do not assume that a separate Next.js host inherits Laravel's browser session automatically.

## Reads, writes, and caching

Authenticated enterprise reads should start with explicit `cache: 'no-store'` until a reviewed tenant-aware caching policy exists. Do not depend on framework-version defaults. Shared cache keys must include tenant and all permission-sensitive dimensions; never cache financial or personal data under a public URL key alone.

Commands use documented API operations and stable idempotency keys where supported. For concurrent edits send the API's documented version or conditional request value and show conflicts without overwriting newer data. Invalidate affected read models after confirmed writes. Poll long-running jobs using their job identifiers and preserve retry status after navigation. Keep write authority in Laravel even when a Next.js server action provides the browser-facing transport.

## User experience and verification

Every route defines loading, empty, denied, validation, conflict, partial-failure, and retry states. Use labelled inputs, keyboard navigation, focus restoration, announced errors, localized amounts and dates, and responsive tables. Hide unavailable actions for clarity while retaining server authorization. Large exports use jobs and expiring authorized download links.

Verify cross-tenant denial at the API and rendered page boundaries, cache isolation between users, secret exclusion from browser bundles, expired sessions, duplicate commands, concurrent updates, and rollback after API failures. Run the package's declared type, lint, unit, and build commands, plus browser tests for the meaningful user journeys. Test consumers against supported API and React/Next.js versions before widening compatibility ranges.

## Deployment and upgrades

Build with committed lockfiles and validate required environment variables. Configure the trusted API origin separately for preview and production; use isolated test tenants in previews. Deploy compatible API changes before dependent clients, retain old contracts during the rollout, and monitor authentication failures, latency, command errors, and cache behavior. Roll back the frontend artifact without reversing database migrations automatically.

Consult the [Next.js upgrade guide](https://nextjs.org/docs/app/guides/upgrading) for the installed major version. Upgrade React and Next.js as a compatible set, review server/client boundaries and caching changes, rebuild, and test authentication and tenant isolation before promotion.

## Step-by-step implementation

Use the [skeleton, implementation and release guide](../guides/presentation/NEXTJS.md) with the [shared foundation steps](../guides/presentation/README.md).
