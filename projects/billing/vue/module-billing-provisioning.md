# Billing: Module Billing Provisioning Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-provisioning). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-billing-module-billing-provisioning-vue-inertia`
**Matching domain module:** `module-billing-provisioning`
**Application:** Billing
**Source feature:** [Module Billing Provisioning](../features/module-billing-provisioning.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-billing-provisioning.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Service state machine:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Provider drivers:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Queued operations:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Rollback:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Polling:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reconciliation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-billing-module-billing-provisioning-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `service-state-machine`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `provider-drivers`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `queued-operations`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `rollback`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `polling`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `reconciliation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `module-billing-provisioning` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-billing-laravel-inertia-vue`](https://github.com/liberusoftware/project-billing-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-billing-provisioning-vue-inertia`](https://github.com/liberusoftware/module-billing-provisioning-vue-inertia) (`@liberusoftware/module-billing-provisioning-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/module-billing-provisioning.md) · [Core plan](../core/module-billing-provisioning.md) · [API plan](../api/module-billing-provisioning.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Service state machine** | Render `service state machine` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Provider drivers** | Render `provider drivers` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Queued operations** | Render `queued operations` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Rollback** | Render `rollback` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Polling** | Render `polling` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Reconciliation** | Render `reconciliation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
