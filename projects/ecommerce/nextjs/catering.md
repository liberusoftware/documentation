# Ecommerce: Catering — Next.js React

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#catering). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Delivery boundary

Define server/client component boundaries explicitly. Server-side API calls use scoped identity; mutations invalidate only the relevant event/revision cache. Private quotation/recipe data must not enter shared static rendering, public caches or unrelated client bundles.

## Shared workflow and security

Use the [core lifecycle](../core/catering.md) and [approved API contract](../api/catering.md). Show event requirements (date, timezone, venue, guests, dietary/service needs), menu quantities and revision, quote currency/expiry/revision and a clear acceptance confirmation. Show availability, accepted quote, order creation and payment as separate statuses. A changed menu or stale/expired quotation requires refresh/re-quote; never optimistically claim acceptance or payment success.

Staff-only capabilities maintain meals, recipes/yields and packages and investigate pending conversion. Customer-facing DTOs, caches, exports, notifications and error messages exclude recipes, preparation instructions and ingredient costs. Scope all caches and queries by actor/Team/Store; clear private state on sign-out or account/store switch. The server rechecks every policy and transition. Disable unavailable integrations with an actionable explanation.

Provide loading, empty, validation, permission-denied, conflict, offline, unavailable-capacity, expired-quote and pending-conversion states. Retrying uses the same conversion idempotency key and reconciles with the server. Quote acceptance/order conversion requires online confirmation and must never silently replay a stale offline action.

## Completion evidence

Test customer and staff journeys, keyboard/screen-reader or native semantics, timezone/currency formatting, stale revision recovery, duplicate taps, interrupted network, privacy after account switch and absence of sensitive fields in client storage/logs. Contract tests use approved schemas and a host integration test proves quote-to-order behavior. Keep all business rules in the owning domain; templates/widgets/components only present approved projections.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and backend integration

**Matching domain module:** `catering`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Next.js host skeleton | [`project-ecommerce-next-react`](https://github.com/liberusoftware/project-ecommerce-next-react) | Standalone Next.js App Router + React 19.2 shell ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |
| Shared product API backend | [`project-ecommerce-laravel-api`](https://github.com/liberusoftware/project-ecommerce-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/catering.md)) |
| Capability Next.js module skeleton | `module-ecommerce-catering-nextjs` | Reusable Server/Client React components and typed DTO helpers ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |

### Next.js feature and component matrix

| Feature / aspect | Server & Client Component boundary | API transport, caching & recovery contract |
| --- | --- | --- |
| **Meals and ingredient composition** | Server Component fetches authorized `meals and ingredient composition` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-ecommerce-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Recipes and preparation yields** | Server Component fetches authorized `recipes and preparation yields` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-ecommerce-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Staff-managed catering packages** | Server Component fetches authorized `staff-managed catering packages` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-ecommerce-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Event requirements and venue context** | Server Component fetches authorized `event requirements and venue context` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-ecommerce-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Immutable menu revisions** | Server Component fetches authorized `immutable menu revisions` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-ecommerce-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Reproducible quotation context** | Server Component fetches authorized `reproducible quotation context` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-ecommerce-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
| **Availability confirmation and order conversion** | Server Component fetches authorized `availability confirmation and order conversion` DTOs; Client Component (`'use client'`) handles interaction, focus, and form state. | Call `project-ecommerce-laravel-api` with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve user drafts on error. |
<!-- layer-implementation-plan:end -->
