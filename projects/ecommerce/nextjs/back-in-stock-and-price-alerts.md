# Back-in-Stock and Price Alerts: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter over a published capability skeleton, not a certified npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `planned:ecommerce:back-in-stock-and-price-alerts`.<br>
**Matching domain module:** `back-in-stock-and-price-alerts`

**Proposed design identifier:** `module-ecommerce-back-in-stock-and-price-alerts-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope, skeleton repositories, and backend ownership

The [domain specification](../features/back-in-stock-and-price-alerts.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Next.js host skeleton | [`project-ecommerce-next-react`](https://github.com/liberusoftware/project-ecommerce-next-react) | Application App Router shell, session/BFF boundary, layout, and route composition ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |
| Shared product API backend | [`project-ecommerce-laravel-api`](https://github.com/liberusoftware/project-ecommerce-laravel-api) | Product HTTP composition root publishing versioned `/api/v1` contracts ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/back-in-stock-and-price-alerts.md)) |
| Capability Next.js module skeleton | [module-ecommerce-back-in-stock-and-price-alerts-nextjs](https://github.com/liberusoftware/module-ecommerce-back-in-stock-and-price-alerts-nextjs) (`@liberusoftware/module-ecommerce-back-in-stock-and-price-alerts-nextjs`) | Reusable React Server/Client component and typed DTO adapter ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |

No dedicated API package name match is established among the mapped consumers of this core identity. Review routes in the core/application tree and define an authorized HTTP contract before implementing browser mutations; PHP actions are not directly callable by JavaScript.

Ecommerce implementation also lives outside `modules/`. Preserve this scope and use the [application capability map](../SOURCE-APPLICATION.md) for current services, policies, REST/GraphQL entry points and checkout behavior. A blank package match does not remove the capability.

## Module surfaces and component contracts

| Capability / feature aspect | Next.js Server & Client Component boundary | API transport, caching & recovery contract |
| --- | --- | --- |
| **Subscriptions** | Server Component loads authorized `subscriptions` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-ecommerce-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Consent** | Server Component loads authorized `consent` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-ecommerce-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Thresholds** | Server Component loads authorized `thresholds` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-ecommerce-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Notification deduplication** | Server Component loads authorized `notification deduplication` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-ecommerce-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Expiry** | Server Component loads authorized `expiry` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-ecommerce-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Channel selection** | Server Component loads authorized `channel selection` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-ecommerce-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Conversion reporting** | Server Component loads authorized `conversion reporting` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-ecommerce-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

No concrete action/query signatures were established in the indexed source roots for this design. Use its source reference and owning application routes/contracts to resolve the integration, rather than inventing create/update/delete operations from the module name.

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

## Server/client and React reuse

Keep API credentials and session forwarding in server-only exports. A Server Component may load authorized serializable data and compose a Client Component for interaction. Put ordinary event callbacks inside the client boundary; server-to-client props must follow the framework serialization/action rules.

Share framework-independent React cards, tables, labels, formatting and field primitives with Inertia. Keep `next/link`, Next.js navigation, server actions and cache invalidation in this adapter, and Inertia visits, page props and redirects in its wrapper. Reuse domain/API DTOs without importing PHP models or another application's private frontend state.

## State, failures and verification

| Situation | User-facing behavior and integration requirement |
| --- | --- |
| Loading or empty authorized query | Accessible progress/empty copy; preserve filters and avoid displaying stale records from another scope |
| Expired session or denied permission | Reauthenticate or show a scoped denial; discard protected cached data and do not retry as a broader service identity |
| Invalid command input | Preserve safe draft values, announce field errors and use the authoritative API validation outcome |
| Stale record / concurrent change | Reload/review the current version; do not overwrite silently or invent an ETag contract the API does not support |
| Timeout after a write | Query the operation/current record when supported before retrying; an idempotency key works only if the owning API actually stores/enforces it |
| Long-running or partly failed operation | Show a durable operation reference, progress, last error and a permitted retry/recovery action |

Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware caching policy exists. Refresh affected read models after confirmed mutations; pending transport acceptance is not a completed business transition. Recheck access for evidence/export downloads.

Verify the actual supported query/command journeys, invalid and denied paths, tenant switching, stale state, retry recovery, keyboard/focus behavior and secret exclusion from browser bundles. Build/test the packed adapter in a clean consuming Next.js application using its declared versions and API contract. No npm package or application suite was executed by this plan generator.

See the [Next.js standard](../../../standards/NEXTJS.md), [npm lifecycle guide](../../../guides/NPM.md), [API architecture](../../../architecture/API.md), and [shared ownership guide](../../../architecture/SHARED-MODULES.md).
