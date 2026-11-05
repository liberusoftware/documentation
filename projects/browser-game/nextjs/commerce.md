# Commerce: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-browser-game-commerce`.

**Proposed design identifier:** `module-browser-game-commerce-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/commerce.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-browser-game-commerce](../../../modules/source/liberusoftware--module-browser-game-commerce.md) |
| API | [liberusoftware/module-browser-game-commerce-api](../../../modules/source/liberusoftware--module-browser-game-commerce-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Premium membership | A focused authorized view or workflow section for premium membership; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Entitlements | A focused authorized view or workflow section for entitlements; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Store | A focused authorized view or workflow section for store; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Regional pricing | A focused authorized view or workflow section for regional pricing; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Receipts | A focused authorized view or workflow section for receipts; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Refunds | A focused authorized view or workflow section for refunds; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Parental controls | A focused authorized view or workflow section for parental controls; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [CommerceQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Queries/CommerceQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [CommerceEntitlement.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceEntitlement.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommerceOrder.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceOrder.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommerceOrderLine.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceOrderLine.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommerceProduct.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceProduct.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommerceRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceRecord.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/browser-game-commerce-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/commerce')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [CommerceController::class, 'index'])->name('browser-game.commerce.index');
Route::get('/products', [CommerceController::class, 'products'])->name('browser-game.commerce.products');
Route::post('/checkout', [CommerceController::class, 'checkout'])->name('browser-game.commerce.checkout');
Route::post('/orders/{order}/complete', [CommerceController::class, 'complete'])->name('browser-game.commerce.orders.complete');
Route::post('/orders/{order}/refund', [CommerceController::class, 'refund'])->name('browser-game.commerce.orders.refund');
Route::get('/{commerce}', [CommerceController::class, 'show'])->name('browser-game.commerce.show');
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
