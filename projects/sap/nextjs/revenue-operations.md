# Revenue operations: Next.js presentation plan

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#revenue-operations). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status:** proposed `module-sap-revenue-operations-nextjs` adapter. Confirm actual package identities and release availability before installation.

## Workspace and routes

Compose **usage completeness dashboard, rating explanation, invoice preview, dispute timeline, settlement reconciliation** from the [detailed domain design](../design/revenue-operations.md). The application owns a list route, detail route and appropriate command forms for `usage-settlements`. Their public URL shape is an application decision, separate from API paths. Reuse existing product UI components and API adapters where their contracts fit.

## Reads and commands

The server integration resolves session and authorized tenant/entity scope, queries the owning API, validates its DTO, and sends only permitted serializable fields to UI components. Reads expose workflow state/version, source references and permitted actions. Command wrappers support `validate, rate, approve, finalize, reconcile` only after their API contracts are implemented and reviewed.

Meter operators submit scoped usage; billing specialists approve adjustments; finance owns recognition policy and postings.

Preserve the record version and operation identity across retries. Return field errors and conflict/review guidance instead of overwriting newer data. Keep credentials in server-only integration. Every server action or route handler authenticates and authorizes its request, and Laravel independently authorizes the domain command.

## Components and failure states

Separate the work queue, record summary, evidence panel, state timeline and command form into documented component boundaries. Framework-independent React primitives may also serve Inertia; navigation, session, form transport and cache invalidation remain adapter-specific. The [Next.js standard](../../../standards/NEXTJS.md) defines the server/client and cache boundaries.

Late or corrected usage creates an adjustment referencing the original settlement. Preserve invoice finality and route disputes through Billing correction workflows.

Show loading, empty, forbidden, validation, conflict, pending-operation and recoverable-error states. Refetch after confirmed state changes and recheck evidence download access. Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware policy exists.

## Verification and release

Duplicate meter events do not increase invoice quantity; a late correction is traceable; retries cannot finalize the same invoice twice.

Also verify session expiry, cross-tenant cache isolation, secret exclusion from browser bundles, keyboard/focus behavior and failure recovery. Build and test the packed adapter in a clean consuming application, then release through the [npm lifecycle guide](../../../guides/NPM.md). Deploy compatible owning API changes before the dependent frontend.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and backend integration

**Matching domain module:** `revenue-operations`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Next.js host skeleton | [`project-enterprise-sap-next-react`](https://github.com/liberusoftware/project-enterprise-sap-next-react) | Standalone Next.js App Router + React 19.2 shell ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |
| Shared product API backend | [`project-enterprise-sap-laravel-api`](https://github.com/liberusoftware/project-enterprise-sap-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/revenue-operations.md)) |
| Capability Next.js module skeleton | [`module-sap-revenue-operations-nextjs`](https://github.com/liberusoftware/module-sap-revenue-operations-nextjs) (`@liberusoftware/module-sap-revenue-operations-nextjs`) | Reusable Server/Client React components and typed DTO helpers ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |

### Next.js feature and component matrix

| Feature / aspect | Server & Client Component boundary | API transport, caching & recovery contract |
| --- | --- | --- |
| **Catalog** | Server Component fetches authorized `catalog` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Pricing** | Server Component fetches authorized `pricing` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Subscriptions** | Server Component fetches authorized `subscriptions` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Usage** | Server Component fetches authorized `usage` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Licensing** | Server Component fetches authorized `licensing` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Billing** | Server Component fetches authorized `billing` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Payments** | Server Component fetches authorized `payments` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Collections** | Server Component fetches authorized `collections` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Revenue schedules** | Server Component fetches authorized `revenue schedules` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
<!-- layer-implementation-plan:end -->
