# Genealogy Core: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter over a published capability skeleton, not a certified npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-genealogy-core`.<br>
**Matching domain module:** `genealogy-core`

**Proposed design identifier:** `module-genealogy-core-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope, skeleton repositories, and backend ownership

The [domain specification](../features/genealogy-core.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Next.js host skeleton | [`project-genealogy-next-react`](https://github.com/liberusoftware/project-genealogy-next-react) | Application App Router shell, session/BFF boundary, layout, and route composition ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |
| Shared product API backend | [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api) | Product HTTP composition root publishing versioned `/api/v1` contracts ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/genealogy-core.md)) |
| Capability Next.js module skeleton | [module-genealogy-core-nextjs](https://github.com/liberusoftware/module-genealogy-core-nextjs) (`@liberusoftware/module-genealogy-core-nextjs`) | Reusable React Server/Client component and typed DTO adapter ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-genealogy-core](../../../modules/source/liberusoftware--module-genealogy-core.md) |
| API | [liberusoftware/module-genealogy-core-api](../../../modules/source/liberusoftware--module-genealogy-core-api.md) |

## Module surfaces and component contracts

| Capability / feature aspect | Next.js Server & Client Component boundary | API transport, caching & recovery contract |
| --- | --- | --- |
| **Trees** | Server Component loads authorized `trees` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-genealogy-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Ownership** | Server Component loads authorized `ownership` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-genealogy-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Identifiers** | Server Component loads authorized `identifiers` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-genealogy-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Privacy defaults** | Server Component loads authorized `privacy defaults` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-genealogy-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Terminology** | Server Component loads authorized `terminology` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-genealogy-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Shared events** | Server Component loads authorized `shared events` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-genealogy-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [TreeStatistics.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Queries/TreeStatistics.php) | `public function __construct(private readonly ?ParentGraphReader $graph = null)`<br>`public function for(Tree $tree): array` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CreateTree.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Actions/CreateTree.php) | `public function __construct(private readonly ?PersonReferenceResolver $personReference = null)`<br>`public function execute(array $attributes): Tree` |
| [DeleteTree.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Actions/DeleteTree.php) | `public function execute(Tree $tree): void` |
| [SetTreeOwner.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Actions/SetTreeOwner.php) | `public function execute(Tree $tree, string\|int\|null $userId): Tree` |
| [SetTreeVisibility.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Actions/SetTreeVisibility.php) | `public function execute(Tree $tree, bool $isPublic): Tree` |
| [UpdateTree.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Actions/UpdateTree.php) | `public function __construct(private readonly ?PersonReferenceResolver $personReference = null)`<br>`public function execute(Tree $tree, array $attributes): Tree` |
| [ParentGraphReader.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Contracts/ParentGraphReader.php) | `public function relatedPeople(string $teamId, array $personIds, bool $ancestors): array` |
| [PersonReferenceResolver.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Contracts/PersonReferenceResolver.php) | `public function existsForTeam(mixed $personId, string $teamId): bool` |
| [TeamOwnedPolicy.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Policies/TeamOwnedPolicy.php) | `public function viewAny(?object $actor): bool`<br>`public function view(?object $actor, object $record): bool`<br>`public function create(?object $actor): bool`<br>`public function update(?object $actor, object $record): bool`<br>`public function delete(?object $actor, object $record): bool` |
| [TreePolicy.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Policies/TreePolicy.php) | `public function view(?object $actor, Tree $tree): bool`<br>`public function manage(?object $actor, Tree $tree): bool` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [Tree.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Models/Tree.php) | `team_id`, `name`, `status`, `description`, `root_person_id`, `is_public`, `metadata`, `user_id`, `identifier`, `terminology` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/genealogy-core-api/routes/api.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core-api/routes/api.php)

```php
Route::get('/', [TreeController::class, 'index'])->name('genealogy.core.index');
Route::get('/{tree}', [TreeController::class, 'show'])->name('genealogy.core.show');
Route::middleware('auth:sanctum')->group(function (): void {
Route::post('/', [TreeController::class, 'store'])->name('genealogy.core.store');
Route::patch('/{tree}/visibility', [TreeController::class, 'visibility'])->name('genealogy.core.visibility');
Route::patch('/{tree}/owner', [TreeController::class, 'owner'])->name('genealogy.core.owner');
Route::patch('/{tree}', [TreeController::class, 'update'])->name('genealogy.core.update');
Route::delete('/{tree}', [TreeController::class, 'destroy'])->name('genealogy.core.destroy');
```

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
