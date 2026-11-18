# Finance: Next.js presentation plan

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#finance). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Status:** proposed `module-sap-finance-nextjs` adapter. Confirm actual package identities and release availability before installation.

## Workspace and routes

Compose **posting exception inbox, journal evidence, source-to-ledger reconciliation, close checklist, consolidation status** from the [detailed domain design](../design/finance.md). The application owns a list route, detail route and appropriate command forms for `posting-batches`. Their public URL shape is an application decision, separate from API paths. Reuse existing product UI components and API adapters where their contracts fit.

## Reads and commands

The server integration resolves session and authorized tenant/entity scope, queries the owning API, validates its DTO, and sends only permitted serializable fields to UI components. Reads expose workflow state/version, source references and permitted actions. Command wrappers support `validate, approve, post, reverse` only after their API contracts are implemented and reviewed.

Preparers submit; independent approvers authorize journals and reopening; read access is scoped by ledger and legal entity.

Preserve the record version and operation identity across retries. Return field errors and conflict/review guidance instead of overwriting newer data. Keep credentials in server-only integration. Every server action or route handler authenticates and authorizes its request, and Laravel independently authorizes the domain command.

## Components and failure states

Separate the work queue, record summary, evidence panel, state timeline and command form into documented component boundaries. Framework-independent React primitives may also serve Inertia; navigation, session, form transport and cache invalidation remain adapter-specific. The [Next.js standard](../../../standards/NEXTJS.md) defines the server/client and cache boundaries.

For a timeout after posting, query by source operation identity before retrying. Reconcile the returned journal and control totals; a posted journal is never silently edited or deleted.

Show loading, empty, forbidden, validation, conflict, pending-operation and recoverable-error states. Refetch after confirmed state changes and recheck evidence download access. Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware policy exists.

## Verification and release

A duplicate invoice event creates one posting; a closed-period command is rejected; reversal preserves the original journal and audit chain.

Also verify session expiry, cross-tenant cache isolation, secret exclusion from browser bundles, keyboard/focus behavior and failure recovery. Build and test the packed adapter in a clean consuming application, then release through the [npm lifecycle guide](../../../guides/NPM.md). Deploy compatible owning API changes before the dependent frontend.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and backend integration

**Matching domain module:** `finance`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Next.js host skeleton | [`project-enterprise-sap-next-react`](https://github.com/liberusoftware/project-enterprise-sap-next-react) | Standalone Next.js App Router + React 19.2 shell ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |
| Shared product API backend | [`project-enterprise-sap-laravel-api`](https://github.com/liberusoftware/project-enterprise-sap-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/finance.md)) |
| Capability Next.js module skeleton | [`module-sap-finance-nextjs`](https://github.com/liberusoftware/module-sap-finance-nextjs) (`@liberusoftware/module-sap-finance-nextjs`) | Reusable Server/Client React components and typed DTO helpers ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |

### Next.js feature and component matrix

| Feature / aspect | Server & Client Component boundary | API transport, caching & recovery contract |
| --- | --- | --- |
| **General ledger** | Server Component fetches authorized `general ledger` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Receivables** | Server Component fetches authorized `receivables` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Payables** | Server Component fetches authorized `payables` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Banking** | Server Component fetches authorized `banking` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Tax** | Server Component fetches authorized `tax` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Assets** | Server Component fetches authorized `assets` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Budgets** | Server Component fetches authorized `budgets` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Treasury** | Server Component fetches authorized `treasury` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Consolidation** | Server Component fetches authorized `consolidation` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Close** | Server Component fetches authorized `close` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Statements** | Server Component fetches authorized `statements` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-enterprise-sap-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
<!-- layer-implementation-plan:end -->
