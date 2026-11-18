# Billing: Module Billing Hosting Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-hosting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-billing-module-billing-hosting-nuxt`
**Matching domain module:** `module-billing-hosting`
**Application:** Billing
**Source feature:** [Module Billing Hosting](../features/module-billing-hosting.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-billing-hosting.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `module-billing-hosting` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Hosting accounts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Plans:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Control-panel adapters:** page/component/composable/API-action behavior for this module's authorized workflow.
- **SSL:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Resources:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Lifecycle operations:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-billing-module-billing-hosting-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `hosting-accounts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `plans`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `control-panel-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `ssl`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `resources`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `lifecycle-operations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `module-billing-hosting` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-billing-nuxt-vue`](https://github.com/liberusoftware/project-billing-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-billing-hosting.md)) |
| Capability Nuxt module skeleton | [`module-billing-hosting-nuxt`](https://github.com/liberusoftware/module-billing-hosting-nuxt) (`@liberusoftware/module-billing-hosting-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Hosting accounts** | Expose composable and Vue 3 component for `hosting accounts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-hosting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Plans** | Expose composable and Vue 3 component for `plans` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-hosting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Control-panel adapters** | Expose composable and Vue 3 component for `control-panel adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-hosting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **SSL** | Expose composable and Vue 3 component for `ssl` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-hosting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Resources** | Expose composable and Vue 3 component for `resources` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-hosting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Lifecycle operations** | Expose composable and Vue 3 component for `lifecycle operations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-hosting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListHostingRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Queries/ListHostingRecords.php) | `public function handle(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
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

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [HostingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Models/HostingAccount.php) | No literal fillable array detected; inspect the model and API schema. |
| [HostingCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Models/HostingCapability.php) | No literal fillable array detected; inspect the model and API schema. |
| [HostingServer.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Models/HostingServer.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [HostingCapabilityController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting-api/src/Http/Controllers/HostingCapabilityController.php) | `public function accounts(Request $request): JsonResponse`<br>`public function showAccount(Request $request, int $record): JsonResponse`<br>`public function storeAccount(Request $request, CreateHostingAccount $create): JsonResponse`<br>`public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateHostingCapability $create): JsonResponse`<br>`public function transition(Request $request, HostingCapability $capability, TransitionHostingCapability $transition): JsonResponse`<br>`public function transitionAccount(Request $request, int $account, TransitionHostingAccount $transition): JsonResponse`<br>`public function operation(Request $request, int $account, PerformHostingOperation $perform): JsonResponse` |

**Observed route declarations:**

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
<!-- layer-implementation-plan:end -->
