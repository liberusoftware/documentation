# Sales and CRM: Next.js presentation plan

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sales-and-crm). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status:** proposed `module-sap-sales-and-crm-nextjs` adapter. Confirm actual package identities and release availability before installation.

## Workspace and routes

Compose **opportunity-to-order workspace, accepted quote comparison, approval evidence, handoff exception queue** from the [detailed domain design](../design/sales-and-crm.md). The application owns a list route, detail route and appropriate command forms for `commercial-handoffs`. Their public URL shape is an application decision, separate from API paths. Reuse existing product UI components and API adapters where their contracts fit.

## Reads and commands

The server integration resolves session and authorized tenant/entity scope, queries the owning API, validates its DTO, and sends only permitted serializable fields to UI components. Reads expose workflow state/version, source references and permitted actions. Command wrappers support `prepare, approve, submit, reconcile` only after their API contracts are implemented and reviewed.

Account teams propose; commercial approvers authorize within value/entity limits; destination services independently authorize acceptance.

Preserve the record version and operation identity across retries. Return field errors and conflict/review guidance instead of overwriting newer data. Keep credentials in server-only integration. Every server action or route handler authenticates and authorizes its request, and Laravel independently authorizes the domain command.

## Components and failure states

Separate the work queue, record summary, evidence panel, state timeline and command form into documented component boundaries. Framework-independent React primitives may also serve Inertia; navigation, session, form transport and cache invalidation remain adapter-specific. The [Next.js standard](../../../standards/NEXTJS.md) defines the server/client and cache boundaries.

If quote validity expires or the destination rejects a product mapping, request review and prepare a new version. Retry a network failure under the original handoff identity.

Show loading, empty, forbidden, validation, conflict, pending-operation and recoverable-error states. Refetch after confirmed state changes and recheck evidence download access. Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware policy exists.

## Verification and release

An expired or superseded quote cannot be accepted; a retry returns the same downstream order; unauthorized customer details are absent from projections.

Also verify session expiry, cross-tenant cache isolation, secret exclusion from browser bundles, keyboard/focus behavior and failure recovery. Build and test the packed adapter in a clean consuming application, then release through the [npm lifecycle guide](../../../guides/NPM.md). Deploy compatible owning API changes before the dependent frontend.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and backend integration

**Matching domain module:** `sales-and-crm`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Next.js host skeleton | [`project-enterprise-sap-next-react`](https://github.com/liberusoftware/project-enterprise-sap-next-react) | Standalone Next.js App Router + React 19.2 shell ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |
| Shared product API backend | [`project-enterprise-sap-laravel-api`](https://github.com/liberusoftware/project-enterprise-sap-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/sales-and-crm.md)) |
| Capability Next.js module skeleton | [`module-sap-sales-and-crm-nextjs`](https://github.com/liberusoftware/module-sap-sales-and-crm-nextjs) (`@liberusoftware/module-sap-sales-and-crm-nextjs`) | Reusable Server/Client React components and typed DTO helpers ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |

### Next.js feature and component matrix

| Feature / aspect | Server & Client Component boundary | API transport, caching & recovery contract |
| --- | --- | --- |
| **Accounts** | Server Component fetches authorized `accounts` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Leads** | Server Component fetches authorized `leads` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Opportunities** | Server Component fetches authorized `opportunities` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Quotes** | Server Component fetches authorized `quotes` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Contracts** | Server Component fetches authorized `contracts` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Orders** | Server Component fetches authorized `orders` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Customer success** | Server Component fetches authorized `customer success` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Communications** | Server Component fetches authorized `communications` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Forecasts** | Server Component fetches authorized `forecasts` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
<!-- layer-implementation-plan:end -->
