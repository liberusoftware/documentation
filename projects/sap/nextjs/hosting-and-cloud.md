# Hosting and cloud: Next.js presentation plan

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#hosting-and-cloud). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status:** proposed `module-sap-hosting-and-cloud-nextjs` adapter. Confirm actual package identities and release availability before installation.

## Workspace and routes

Compose **service request wizard, capacity preview, approval summary, provisioning progress, drift and failed-resource reconciliation** from the [detailed domain design](../design/hosting-and-cloud.md). The application owns a list route, detail route and appropriate command forms for `provisioning-requests`. Their public URL shape is an application decision, separate from API paths. Reuse existing product UI components and API adapters where their contracts fit.

## Reads and commands

The server integration resolves session and authorized tenant/entity scope, queries the owning API, validates its DTO, and sends only permitted serializable fields to UI components. Reads expose workflow state/version, source references and permitted actions. Command wrappers support `validate, approve, provision, reconcile, suspend, retire` only after their API contracts are implemented and reviewed.

Customers request entitled services; operators act on scoped infrastructure; approvers authorize high-impact or high-cost changes.

Preserve the record version and operation identity across retries. Return field errors and conflict/review guidance instead of overwriting newer data. Keep credentials in server-only integration. Every server action or route handler authenticates and authorizes its request, and Laravel independently authorizes the domain command.

## Components and failure states

Separate the work queue, record summary, evidence panel, state timeline and command form into documented component boundaries. Framework-independent React primitives may also serve Inertia; navigation, session, form transport and cache invalidation remain adapter-specific. The [Next.js standard](../../../standards/NEXTJS.md) defines the server/client and cache boundaries.

On partial infrastructure creation, record every created resource and compensation result. Query provider/control-plane state before retry; a new retry must not allocate another billable resource unintentionally.

Show loading, empty, forbidden, validation, conflict, pending-operation and recoverable-error states. Refetch after confirmed state changes and recheck evidence download access. Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware policy exists.

## Verification and release

A retry returns the existing resource reference; partial failure is recoverable; secrets are absent from UI/log projections and cross-tenant resource access is denied.

Also verify session expiry, cross-tenant cache isolation, secret exclusion from browser bundles, keyboard/focus behavior and failure recovery. Build and test the packed adapter in a clean consuming application, then release through the [npm lifecycle guide](../../../guides/NPM.md). Deploy compatible owning API changes before the dependent frontend.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and backend integration

**Matching domain module:** `hosting-and-cloud`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Next.js host skeleton | [`project-enterprise-sap-next-react`](https://github.com/liberusoftware/project-enterprise-sap-next-react) | Standalone Next.js App Router + React 19.2 shell ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |
| Shared product API backend | [`project-enterprise-sap-laravel-api`](https://github.com/liberusoftware/project-enterprise-sap-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/hosting-and-cloud.md)) |
| Capability Next.js module skeleton | [`module-sap-hosting-and-cloud-nextjs`](https://github.com/liberusoftware/module-sap-hosting-and-cloud-nextjs) (`@liberusoftware/module-sap-hosting-and-cloud-nextjs`) | Reusable Server/Client React components and typed DTO helpers ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |

### Next.js feature and component matrix

| Feature / aspect | Server & Client Component boundary | API transport, caching & recovery contract |
| --- | --- | --- |
| **Services** | Server Component fetches authorized `services` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Subscriptions** | Server Component fetches authorized `subscriptions` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Provisioning** | Server Component fetches authorized `provisioning` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Infrastructure inventory** | Server Component fetches authorized `infrastructure inventory` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Domains/DNS** | Server Component fetches authorized `domains/dns` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Capacity** | Server Component fetches authorized `capacity` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Usage** | Server Component fetches authorized `usage` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Operations** | Server Component fetches authorized `operations` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
<!-- layer-implementation-plan:end -->
