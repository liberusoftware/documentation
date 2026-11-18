# Revisions: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter over a published capability skeleton, not a certified npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-cms-revisions`.<br>
**Matching domain module:** `revisions`

**Proposed design identifier:** `module-cms-revisions-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope, skeleton repositories, and backend ownership

The [domain specification](../features/revisions.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Next.js host skeleton | [`project-cms-next-react`](https://github.com/liberusoftware/project-cms-next-react) | Application App Router shell, session/BFF boundary, layout, and route composition ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Product HTTP composition root publishing versioned `/api/v1` contracts ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/revisions.md)) |
| Capability Next.js module skeleton | [module-cms-revisions-nextjs](https://github.com/liberusoftware/module-cms-revisions-nextjs) (`@liberusoftware/module-cms-revisions-nextjs`) | Reusable React Server/Client component and typed DTO adapter ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |

This plan is the shared documentation home for **3 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-cms-revisions](../../../modules/source/liberusoftware--module-cms-revisions.md) |
| API | [liberusoftware/module-cms-revisions-api](../../../modules/source/liberusoftware--module-cms-revisions-api.md) |

## Module surfaces and component contracts

| Capability / feature aspect | Next.js Server & Client Component boundary | API transport, caching & recovery contract |
| --- | --- | --- |
| **Immutable revisions** | Server Component loads authorized `immutable revisions` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-cms-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Autosave** | Server Component loads authorized `autosave` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-cms-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Compare** | Server Component loads authorized `compare` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-cms-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Restore** | Server Component loads authorized `restore` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-cms-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Branching** | Server Component loads authorized `branching` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-cms-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Attribution** | Server Component loads authorized `attribution` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-cms-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Retention** | Server Component loads authorized `retention` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-cms-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Published-versus-working copies** | Server Component loads authorized `published-versus-working copies` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-cms-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [RevisionService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-revisions/src/Services/RevisionService.php) | `public function create(string $type, int $id, array $snapshot, ?int $userId = null, string $branch = 'main', bool $autosave = false, array $metadata = []): Revision`<br>`public function autosave(string $type, int $id, array $snapshot, ?int $userId = null, string $branch = 'main'): Revision`<br>`public function compare(Revision $from, Revision $to): array`<br>`public function restore(Revision $revision, ?int $userId = null, string $branch = 'main'): Revision`<br>`public function branch(Revision $revision, string $branch, ?int $userId = null): Revision`<br>`public function publish(Revision $revision): Revision`<br>`public function prune(string $type, int $id, int $retain = 20, string $branch = 'main'): int` |

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
