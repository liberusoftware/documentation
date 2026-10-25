# Accounts: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-browser-game-accounts`.

**Proposed design identifier:** `module-browser-game-accounts-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/accounts.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-browser-game-accounts](../../../modules/source/liberusoftware--module-browser-game-accounts.md) |
| API | [liberusoftware/module-browser-game-accounts-api](../../../modules/source/liberusoftware--module-browser-game-accounts-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Player identity | A focused authorized view or workflow section for player identity; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Sessions | A focused authorized view or workflow section for sessions; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Age/region policy | A focused authorized view or workflow section for age/region policy; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Bans | A focused authorized view or workflow section for bans; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Recovery | A focused authorized view or workflow section for recovery; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Privacy | A focused authorized view or workflow section for privacy; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Account lifecycle | A focused authorized view or workflow section for account lifecycle; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [AccountsQuery.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Queries/AccountsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [AccountBan.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Models/AccountBan.php) | No literal fillable array detected; inspect the model and API schema. |
| [AccountPrivacy.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Models/AccountPrivacy.php) | No literal fillable array detected; inspect the model and API schema. |
| [AccountRecovery.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Models/AccountRecovery.php) | No literal fillable array detected; inspect the model and API schema. |
| [AccountSession.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Models/AccountSession.php) | No literal fillable array detected; inspect the model and API schema. |
| [AccountsRecord.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Models/AccountsRecord.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/browser-game-accounts-api/routes/api.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/accounts')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [AccountsController::class, 'index'])->name('browser-game.accounts.index');
Route::post('/', [AccountsController::class, 'store'])->name('browser-game.accounts.store');
Route::patch('/{account}', [AccountsController::class, 'update'])->name('browser-game.accounts.update');
Route::post('/{account}/verify-email', [AccountsController::class, 'verifyEmail'])->name('browser-game.accounts.verify-email');
Route::post('/{account}/suspend', [AccountsController::class, 'suspend'])->name('browser-game.accounts.suspend');
Route::post('/{account}/reactivate', [AccountsController::class, 'reactivate'])->name('browser-game.accounts.reactivate');
Route::post('/{account}/ban', [AccountsController::class, 'ban'])->name('browser-game.accounts.ban');
Route::post('/{account}/bans/{ban}/lift', [AccountsController::class, 'liftBan'])->name('browser-game.accounts.bans.lift');
Route::post('/{account}/age-region', [AccountsController::class, 'ageRegion'])->name('browser-game.accounts.age-region');
Route::put('/{account}/privacy', [AccountsController::class, 'privacy'])->name('browser-game.accounts.privacy');
Route::post('/{account}/deletion-request', [AccountsController::class, 'requestDeletion'])->name('browser-game.accounts.deletion-request');
Route::post('/{account}/deletion-complete', [AccountsController::class, 'completeDeletion'])->name('browser-game.accounts.deletion-complete');
Route::get('/{account}/sessions', [AccountsController::class, 'sessions'])->name('browser-game.accounts.sessions');
Route::post('/{account}/recovery', [AccountsController::class, 'issueRecovery'])->name('browser-game.accounts.recovery.issue');
Route::post('/{account}/sessions/{session}/revoke', [AccountsController::class, 'revokeSession'])->name('browser-game.accounts.sessions.revoke');
Route::post('/{account}/sessions/revoke-all', [AccountsController::class, 'revokeAllSessions'])->name('browser-game.accounts.sessions.revoke-all');
Route::get('/{account}', [AccountsController::class, 'show'])->name('browser-game.accounts.show');
Route::post('api/v1/browser-game/accounts/recovery/consume', [AccountsController::class, 'consumeRecovery'])
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
