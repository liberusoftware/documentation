# Billing: Module Billing Provisioning Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-provisioning). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-billing-module-billing-provisioning-nuxt`
**Matching domain module:** `module-billing-provisioning`
**Application:** Billing
**Source feature:** [Module Billing Provisioning](../features/module-billing-provisioning.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-billing-provisioning.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `module-billing-provisioning` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Service state machine:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Provider drivers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Queued operations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rollback:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Polling:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-billing-module-billing-provisioning-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `service-state-machine`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `provider-drivers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `queued-operations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rollback`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `polling`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reconciliation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `module-billing-provisioning` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-billing-nuxt-vue`](https://github.com/liberusoftware/project-billing-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-billing-provisioning.md)) |
| Capability Nuxt module skeleton | [`module-billing-provisioning-nuxt`](https://github.com/liberusoftware/module-billing-provisioning-nuxt) (`@liberusoftware/module-billing-provisioning-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Service state machine** | Expose composable and Vue 3 component for `service state machine` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-provisioning.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Provider drivers** | Expose composable and Vue 3 component for `provider drivers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-provisioning.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Queued operations** | Expose composable and Vue 3 component for `queued operations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-provisioning.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Rollback** | Expose composable and Vue 3 component for `rollback` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-provisioning.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Polling** | Expose composable and Vue 3 component for `polling` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-provisioning.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Reconciliation** | Expose composable and Vue 3 component for `reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-provisioning.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListProvisionedServices.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Queries/ListProvisionedServices.php) | `public function execute(?int $teamId = null): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateProvisionedService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Actions/CreateProvisionedService.php) | `public function execute(array $attributes): ProvisionedService` |
| [QueueProvisioningOperation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Actions/QueueProvisioningOperation.php) | `public function execute(ProvisionedService $service, string $operation, array $payload = []): ProvisioningOperation` |
| [ReconcileProvisionedService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Actions/ReconcileProvisionedService.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(ProvisionedService $service): ProvisionedService` |
| [RunProvisioningOperation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Actions/RunProvisioningOperation.php) | `public function __construct(private DatabaseManager $database, private ProvisioningDriverRegistry $drivers)`<br>`public function execute(ProvisioningOperation $operation): ProvisioningOperation` |
| [TransitionProvisionedService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Actions/TransitionProvisionedService.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(ProvisionedService $service, ProvisioningState $state, ?string $error = null): ProvisionedService` |
| [ProvisioningDriver.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Contracts/ProvisioningDriver.php) | `public function provision(ProvisionedService $service): string`<br>`public function deprovision(ProvisionedService $service): void`<br>`public function poll(ProvisionedService $service): array` |
| [ProvisioningPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Policies/ProvisioningPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function update(?object $user, object $record): bool` |
| [ProvisioningDriverRegistry.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Services/ProvisioningDriverRegistry.php) | `public function register(string $provider, ProvisioningDriver $driver): void`<br>`public function resolve(string $provider): ProvisioningDriver` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ProvisionedService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Models/ProvisionedService.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProvisioningOperation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Models/ProvisioningOperation.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProvisioningOperationController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning-api/src/Http/Controllers/ProvisioningOperationController.php) | `public function services(Request $request): JsonResponse`<br>`public function showService(Request $request, int $provisionedService): JsonResponse`<br>`public function storeService(Request $request, CreateProvisionedService $create): JsonResponse`<br>`public function index(Request $request): JsonResponse`<br>`public function queue(Request $request, ProvisionedService $provisionedService, QueueProvisioningOperation $queue): JsonResponse`<br>`public function reconcile(Request $request, ProvisionedService $provisionedService, ReconcileProvisionedService $reconcile): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-provisioning-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.provisioning.read'])->prefix('api/v1/billing/provisioning/operations')->group(function (): void {
Route::get('/', [ProvisioningOperationController::class, 'index'])->name('billing.provisioning.operations.index');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.provisioning.write', 'idempotency'])->prefix('api/v1/billing/provisioning')->group(function (): void {
Route::post('/', [ProvisioningOperationController::class, 'storeService'])->name('billing.provisioning.store');
Route::post('/{provisionedService}/operations', [ProvisioningOperationController::class, 'queue'])->name('billing.provisioning.operations.store');
Route::post('/{provisionedService}/reconcile', [ProvisioningOperationController::class, 'reconcile'])->name('billing.provisioning.reconcile');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.provisioning.read'])->prefix('api/v1/billing/provisioning')->group(function (): void {
Route::get('/', [ProvisioningOperationController::class, 'services'])->name('billing.provisioning.services.index');
Route::get('/{provisionedService}', [ProvisioningOperationController::class, 'showService'])->whereNumber('provisionedService')->name('billing.provisioning.services.show');
```
<!-- layer-implementation-plan:end -->
