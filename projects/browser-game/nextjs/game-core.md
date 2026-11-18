# Game Core: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter over a published capability skeleton, not a certified npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-browser-game-game-core`.<br>
**Matching domain module:** `game-core`

**Proposed design identifier:** `module-browser-game-game-core-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope, skeleton repositories, and backend ownership

The [domain specification](../features/game-core.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Next.js host skeleton | [`project-browser-game-next-react`](https://github.com/liberusoftware/project-browser-game-next-react) | Application App Router shell, session/BFF boundary, layout, and route composition ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Product HTTP composition root publishing versioned `/api/v1` contracts ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/game-core.md)) |
| Capability Next.js module skeleton | [module-browser-game-game-core-nextjs](https://github.com/liberusoftware/module-browser-game-game-core-nextjs) (`@liberusoftware/module-browser-game-game-core-nextjs`) | Reusable React Server/Client component and typed DTO adapter ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-browser-game-game-core](../../../modules/source/liberusoftware--module-browser-game-game-core.md) |
| API | [liberusoftware/module-browser-game-game-core-api](../../../modules/source/liberusoftware--module-browser-game-game-core-api.md) |

## Module surfaces and component contracts

| Capability / feature aspect | Next.js Server & Client Component boundary | API transport, caching & recovery contract |
| --- | --- | --- |
| **Worlds/shards** | Server Component loads authorized `worlds/shards` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-browser-game-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Game clock** | Server Component loads authorized `game clock` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-browser-game-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Rulesets** | Server Component loads authorized `rulesets` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-browser-game-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Content versions** | Server Component loads authorized `content versions` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-browser-game-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Feature flags** | Server Component loads authorized `feature flags` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-browser-game-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Maintenance state** | Server Component loads authorized `maintenance state` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-browser-game-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [GameCoreOverview.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Queries/GameCoreOverview.php) | `public function forWorld(GameCoreContext $context, string $worldId): array`<br>`public function enabledFlags(?string $worldId = null): Collection`<br>`public function isEnabled(GameCoreContext $context, ?GameWorld $world, string $key, array $attributes = []): bool`<br>`public function enabledFor(GameCoreContext $context, ?GameWorld $world, array $attributes = []): Collection` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [GameCoreContext.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Contracts/GameCoreContext.php) | `public function actorId(): ?string`<br>`public function tenantId(): ?string`<br>`public function teamId(): ?string` |
| [GameCorePolicy.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Policies/GameCorePolicy.php) | `public function view(GameCoreContext $context, GameWorld $world): bool`<br>`public function manage(GameCoreContext $context, GameWorld $world): bool` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [GameClock.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameClock.php) | `world_id`, `current_at`, `speed`, `paused`, `updated_by` |
| [GameContentVersion.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameContentVersion.php) | `world_id`, `version`, `status`, `content_hash`, `manifest`, `published_at`, `published_by` |
| [GameFeatureFlag.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameFeatureFlag.php) | `world_id`, `key`, `enabled`, `rollout_percentage`, `constraints`, `changed_by` |
| [GameMaintenanceState.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameMaintenanceState.php) | `world_id`, `status`, `message`, `starts_at`, `ends_at`, `changed_by` |
| [GameRuleset.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameRuleset.php) | `world_id`, `version`, `status`, `rules`, `published_at`, `published_by` |
| [GameWorld.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameWorld.php) | `tenant_id`, `team_id`, `name`, `slug`, `status`, `metadata` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/browser-game-game-core-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/game-core')
Route::get('/', [GameCoreController::class, 'index'])->name('browser-game.game-core.index');
Route::post('/', [GameCoreController::class, 'store'])->name('browser-game.game-core.store');
Route::get('/{world}', [GameCoreController::class, 'show'])->name('browser-game.game-core.show');
Route::patch('/{world}', [GameCoreController::class, 'update'])->name('browser-game.game-core.update');
Route::put('/{world}/clock', [GameCoreController::class, 'clock'])->name('browser-game.game-core.clock');
Route::post('/{world}/rulesets', [GameCoreController::class, 'ruleset'])->name('browser-game.game-core.ruleset');
Route::post('/{world}/content-versions', [GameCoreController::class, 'content'])->name('browser-game.game-core.content');
Route::put('/{world}/feature-flags/{key}', [GameCoreController::class, 'flag'])->name('browser-game.game-core.flag');
Route::get('/{world}/feature-flags/{key}', [GameCoreController::class, 'evaluateFlag'])->name('browser-game.game-core.flag.evaluate');
Route::put('/{world}/maintenance', [GameCoreController::class, 'maintenance'])->name('browser-game.game-core.maintenance');
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
