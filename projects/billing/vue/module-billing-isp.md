# Billing: Module Billing Isp Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-isp). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-billing-module-billing-isp-vue-inertia`
**Matching domain module:** `module-billing-isp`
**Application:** Billing
**Source feature:** [Module Billing Isp](../features/module-billing-isp.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-billing-isp.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Access services:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Coverage:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Installation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **RADIUS/AAA:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Usage:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Equipment:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Network adapters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-billing-module-billing-isp-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `access-services`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `coverage`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `installation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `radius-aaa`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `usage`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `equipment`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `network-adapters`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `module-billing-isp` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-billing-laravel-inertia-vue`](https://github.com/liberusoftware/project-billing-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-billing-isp-vue-inertia`](https://github.com/liberusoftware/module-billing-isp-vue-inertia) (`@liberusoftware/module-billing-isp-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/module-billing-isp.md) · [Core plan](../core/module-billing-isp.md) · [API plan](../api/module-billing-isp.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Access services** | Render `access services` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Coverage** | Render `coverage` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Installation** | Render `installation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **RADIUS/AAA** | Render `radius/aaa` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Usage** | Render `usage` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Equipment** | Render `equipment` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Network adapters** | Render `network adapters` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListIspRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Queries/ListIspRecords.php) | `public function handle(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAccessService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/CreateAccessService.php) | `public function handle(int $teamId, array $attributes): AccessService` |
| [CreateIspCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/CreateIspCapability.php) | `public function handle(int $teamId, array $attributes): IspCapability` |
| [RecordRadiusAccounting.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/RecordRadiusAccounting.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(AccessService $service, array $accounting): RadiusSession` |
| [ResetUsagePeriod.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/ResetUsagePeriod.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(AccessService $service): AccessService` |
| [SynchronizeAccessService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/SynchronizeAccessService.php) | `public function __construct(private DatabaseManager $database, private NetworkAdapterRegistry $adapters)`<br>`public function execute(AccessService $service, string $adapter): AccessService` |
| [TransitionAccessService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/TransitionAccessService.php) | `public function handle(AccessService $service, string $status): AccessService` |
| [TransitionIspCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/TransitionIspCapability.php) | `public function handle(IspCapability $capability, string $status): IspCapability` |
| [NetworkAdapter.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Contracts/NetworkAdapter.php) | `public function key(): string`<br>`public function install(array $attributes): array`<br>`public function suspend(array $attributes): array`<br>`public function remove(array $attributes): array` |
| [AccessServicePolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Policies/AccessServicePolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, AccessService $record): bool`<br>`public function update(?Authenticatable $user, AccessService $record): bool` |
| [IspCapabilityPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Policies/IspCapabilityPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function view(?object $user, object $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccessService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Models/AccessService.php) | No literal fillable array detected; inspect the model and API schema. |
| [IspCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Models/IspCapability.php) | No literal fillable array detected; inspect the model and API schema. |
| [RadiusSession.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Models/RadiusSession.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [IspCapabilityController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp-api/src/Http/Controllers/IspCapabilityController.php) | `public function accounts(Request $request): JsonResponse`<br>`public function showAccount(Request $request, int $record): JsonResponse`<br>`public function storeAccessService(Request $request, CreateAccessService $create): JsonResponse`<br>`public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateIspCapability $create): JsonResponse`<br>`public function transition(Request $request, int $capability, TransitionIspCapability $transition): JsonResponse`<br>`public function transitionAccessService(Request $request, int $service, TransitionAccessService $transition): JsonResponse`<br>`public function synchronizeAccessService(Request $request, int $service, SynchronizeAccessService $synchronize): JsonResponse`<br>`public function recordAccounting(Request $request, int $service, RecordRadiusAccounting $record): JsonResponse`<br>`public function resetUsage(Request $request, int $service, ResetUsagePeriod $reset): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-isp-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.isp.read'])->prefix('api/v1/billing/isp/capabilities')->group(function (): void {
Route::get('/', [IspCapabilityController::class, 'index'])->name('billing.isp.capabilities.index');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.isp.write', 'idempotency'])->prefix('api/v1/billing/isp/capabilities')->group(function (): void {
Route::post('/', [IspCapabilityController::class, 'store'])->name('billing.isp.capabilities.store');
Route::patch('/{capability}/lifecycle', [IspCapabilityController::class, 'transition'])->whereNumber('capability')->name('billing.isp.capabilities.lifecycle');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.isp.write', 'idempotency'])->prefix('api/v1/billing/isp')->group(function (): void {
Route::post('/', [IspCapabilityController::class, 'storeAccessService'])->name('billing.isp.store');
Route::patch('/{service}/lifecycle', [IspCapabilityController::class, 'transitionAccessService'])->whereNumber('service')->name('billing.isp.services.lifecycle');
Route::post('/{service}/synchronize', [IspCapabilityController::class, 'synchronizeAccessService'])->whereNumber('service')->name('billing.isp.services.synchronize');
Route::post('/{service}/accounting', [IspCapabilityController::class, 'recordAccounting'])->whereNumber('service')->name('billing.isp.services.accounting');
Route::post('/{service}/usage/reset', [IspCapabilityController::class, 'resetUsage'])->whereNumber('service')->name('billing.isp.services.usage.reset');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.isp.read'])->prefix('api/v1/billing/isp')->group(function (): void {
Route::get('/', [IspCapabilityController::class, 'accounts'])->name('billing.isp.services.index');
Route::get('/{record}', [IspCapabilityController::class, 'showAccount'])->whereNumber('record')->name('billing.isp.services.show');
```
<!-- layer-implementation-plan:end -->
