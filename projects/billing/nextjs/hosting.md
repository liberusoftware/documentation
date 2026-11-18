# Hosting: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter over a published capability skeleton, not a certified npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-billing-hosting`.<br>
**Matching domain module:** `hosting`

**Proposed design identifier:** `module-billing-hosting-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope, skeleton repositories, and backend ownership

The [domain specification](../features/hosting.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Next.js host skeleton | [`project-billing-next-react`](https://github.com/liberusoftware/project-billing-next-react) | Application App Router shell, session/BFF boundary, layout, and route composition ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Product HTTP composition root publishing versioned `/api/v1` contracts ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/hosting.md)) |
| Capability Next.js module skeleton | [module-billing-hosting-nextjs](https://github.com/liberusoftware/module-billing-hosting-nextjs) (`@liberusoftware/module-billing-hosting-nextjs`) | Reusable React Server/Client component and typed DTO adapter ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-billing-hosting](../../../modules/source/liberusoftware--module-billing-hosting.md) |
| API | [liberusoftware/module-billing-hosting-api](../../../modules/source/liberusoftware--module-billing-hosting-api.md) |

## Module surfaces and component contracts

| Capability / feature aspect | Next.js Server & Client Component boundary | API transport, caching & recovery contract |
| --- | --- | --- |
| **Hosting accounts** | Server Component loads authorized `hosting accounts` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-billing-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Plans** | Server Component loads authorized `plans` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-billing-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Control-panel adapters** | Server Component loads authorized `control-panel adapters` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-billing-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **SSL** | Server Component loads authorized `ssl` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-billing-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Resources** | Server Component loads authorized `resources` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-billing-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Lifecycle operations** | Server Component loads authorized `lifecycle operations` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-billing-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ListHostingRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Queries/ListHostingRecords.php) | `public function handle(int $teamId): Collection` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CreateHostingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Actions/CreateHostingAccount.php) | `public function handle(int $teamId, array $attributes): HostingAccount` |
| [CreateHostingCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Actions/CreateHostingCapability.php) | `public function handle(int $teamId, array $attributes): HostingCapability` |
| [CreateHostingServer.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Actions/CreateHostingServer.php) | `public function handle(int $teamId, array $attributes): HostingServer` |
| [PerformHostingOperation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Actions/PerformHostingOperation.php) | `public function __construct(private HostingDriverRegistry $drivers)`<br>`public function handle(HostingAccount $account, string $operation): HostingAccount` |
| [TransitionHostingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Actions/TransitionHostingAccount.php) | `public function handle(HostingAccount $account, string $status): HostingAccount` |
| [TransitionHostingCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Actions/TransitionHostingCapability.php) | `public function handle(HostingCapability $capability, string $status): HostingCapability` |
| [ControlPanelDriver.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Contracts/ControlPanelDriver.php) | `public function unsuspend(array $attributes): array`<br>`public function changePackage(array $attributes): array`<br>`public function addAddon(array $attributes): array`<br>`public function removeAddon(array $attributes): array` |
| [HostingDriver.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Contracts/HostingDriver.php) | `public function key(): string`<br>`public function provision(array $attributes): array`<br>`public function suspend(array $attributes): array`<br>`public function terminate(array $attributes): array` |
| [HostingAccountPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Policies/HostingAccountPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, HostingAccount $record): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, HostingAccount $record): bool` |
| [HostingCapabilityPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Policies/HostingCapabilityPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function update(?object $user, object $record): bool` |
| [HostingDriverRegistry.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Services/HostingDriverRegistry.php) | `public function register(HostingDriver $driver): void`<br>`public function resolve(string $key): HostingDriver`<br>`public function keys(): array` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [HostingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Models/HostingAccount.php) | No literal fillable array detected; inspect the model and API schema. |
| [HostingCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Models/HostingCapability.php) | No literal fillable array detected; inspect the model and API schema. |
| [HostingServer.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Models/HostingServer.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/module-billing-hosting-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.hosting.read'])->prefix('api/v1/billing/hosting/capabilities')->group(function (): void {
Route::get('/', [HostingCapabilityController::class, 'index'])->name('billing.hosting.capabilities.index');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.hosting.write', 'idempotency'])->prefix('api/v1/billing/hosting/capabilities')->group(function (): void {
Route::post('/', [HostingCapabilityController::class, 'store'])->name('billing.hosting.capabilities.store');
Route::patch('/{capability}/lifecycle', [HostingCapabilityController::class, 'transition'])->name('billing.hosting.capabilities.lifecycle');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.hosting.write', 'idempotency'])->prefix('api/v1/billing/hosting')->group(function (): void {
Route::post('/', [HostingCapabilityController::class, 'storeAccount'])->name('billing.hosting.store');
Route::post('/{account}/operation', [HostingCapabilityController::class, 'operation'])->whereNumber('account')->name('billing.hosting.accounts.operation');
Route::patch('/{account}/lifecycle', [HostingCapabilityController::class, 'transitionAccount'])->whereNumber('account')->name('billing.hosting.accounts.lifecycle');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.hosting.read'])->prefix('api/v1/billing/hosting')->group(function (): void {
Route::get('/', [HostingCapabilityController::class, 'accounts'])->name('billing.hosting.accounts.index');
Route::get('/{record}', [HostingCapabilityController::class, 'showAccount'])->whereNumber('record')->name('billing.hosting.accounts.show');
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
