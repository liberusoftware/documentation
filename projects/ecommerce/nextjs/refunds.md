# Refunds: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `planned:ecommerce:refunds`.

**Proposed design identifier:** `module-ecommerce-refunds-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/refunds.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

No dedicated API package name match is established among the mapped consumers of this core identity. Review routes in the core/application tree and define an authorized HTTP contract before implementing browser mutations; PHP actions are not directly callable by JavaScript.

Ecommerce implementation also lives outside `modules/`. Preserve this scope and use the [application capability map](../SOURCE-APPLICATION.md) for current services, policies, REST/GraphQL entry points and checkout behavior. A blank package match does not remove the capability.

Observed application sources for this capability: [app/Models/Refund.php](https://github.com/liberusoftware/ecommerce-laravel/blob/af5a2b29c9c26ba89c97b9daccbb3facf20a8c2f/app/Models/Refund.php) · [app/Models/RefundItem.php](https://github.com/liberusoftware/ecommerce-laravel/blob/af5a2b29c9c26ba89c97b9daccbb3facf20a8c2f/app/Models/RefundItem.php) · [app/Http/Controllers/Api/OrderRefundController.php](https://github.com/liberusoftware/ecommerce-laravel/blob/af5a2b29c9c26ba89c97b9daccbb3facf20a8c2f/app/Http/Controllers/Api/OrderRefundController.php).

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Refund calculation | A focused authorized view or workflow section for refund calculation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Original/alternative tender policy | A focused authorized view or workflow section for original/alternative tender policy; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Approval | A focused authorized view or workflow section for approval; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Provider execution | A focused authorized view or workflow section for provider execution; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Store credit | A focused authorized view or workflow section for store credit; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Failure recovery | A focused authorized view or workflow section for failure recovery; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Accounting events | A focused authorized view or workflow section for accounting events; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

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
