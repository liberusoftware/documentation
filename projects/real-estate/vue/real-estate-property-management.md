# Real Estate: Real Estate Property Management Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-property-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-real-estate-real-estate-property-management-vue-inertia`
**Matching domain module:** `real-estate-property-management`
**Application:** Real Estate
**Source feature:** [Real Estate Property Management](../features/real-estate-property-management.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/real-estate-property-management.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Rent schedule:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Statements:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Inspections:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Compliance:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Maintenance:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Contractors:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Owner approvals:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-real-estate-real-estate-property-management-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `rent-schedule`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `statements`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `inspections`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `compliance`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `maintenance`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `contractors`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `owner-approvals`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `real-estate-property-management` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-real-estate-laravel-inertia-vue`](https://github.com/liberusoftware/project-real-estate-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-real-estate-property-management-vue-inertia`](https://github.com/liberusoftware/module-real-estate-property-management-vue-inertia) (`@liberusoftware/module-real-estate-property-management-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/real-estate-property-management.md) · [Core plan](../core/real-estate-property-management.md) · [API plan](../api/real-estate-property-management.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Rent schedule** | Render `rent schedule` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Statements** | Render `statements` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Inspections** | Render `inspections` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Compliance** | Render `compliance` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Maintenance** | Render `maintenance` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Contractors** | Render `contractors` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Owner approvals** | Render `owner approvals` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListManagementRecords.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Queries/ListManagementRecords.php) | `public function handle(int\|string $teamId, ?string $capability = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ManagementRecordPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Policies/ManagementRecordPolicy.php) | `public function view($user, ManagementRecord $record): bool`<br>`public function update($user, ManagementRecord $record): bool`<br>`public function delete($user, ManagementRecord $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Inspection.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/Inspection.php) | No literal fillable array detected; inspect the model and API schema. |
| [MaintenanceRequest.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/MaintenanceRequest.php) | No literal fillable array detected; inspect the model and API schema. |
| [ManagementRecord.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/ManagementRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [VendorQuote.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/VendorQuote.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkOrder.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/WorkOrder.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkOrderUpdate.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/WorkOrderUpdate.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [InspectionController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Controllers/InspectionController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateInspection $create): JsonResponse`<br>`public function show(Request $request, Inspection $inspection): JsonResponse`<br>`public function update(Request $request, Inspection $inspection, UpdateInspection $update): JsonResponse` |
| [MaintenanceRequestController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Controllers/MaintenanceRequestController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateMaintenanceRequest $create): JsonResponse`<br>`public function show(Request $request, MaintenanceRequest $maintenance): JsonResponse`<br>`public function update(Request $request, MaintenanceRequest $maintenance, UpdateMaintenanceRequest $update): JsonResponse` |
| [ManagementRecordController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Controllers/ManagementRecordController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateManagementRecord $create): JsonResponse`<br>`public function show(Request $request, ManagementRecord $record): JsonResponse`<br>`public function update(Request $request, ManagementRecord $record, TransitionManagementRecord $transition): JsonResponse`<br>`public function updateDetails(Request $request, ManagementRecord $record, UpdateManagementDetails $update): JsonResponse`<br>`public function recordFailure(Request $request, ManagementRecord $record, RecordManagementFailure $failure): JsonResponse` |
| [VendorQuoteController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Controllers/VendorQuoteController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateVendorQuote $create): JsonResponse`<br>`public function show(Request $request, VendorQuote $contractorQuote): JsonResponse`<br>`public function update(Request $request, VendorQuote $contractorQuote): JsonResponse`<br>`public function decide(Request $request, VendorQuote $contractorQuote, DecideVendorQuote $decide): JsonResponse` |
| [WorkOrderController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Controllers/WorkOrderController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateWorkOrder $create): JsonResponse`<br>`public function show(Request $request, WorkOrder $workOrder): JsonResponse`<br>`public function update(Request $request, WorkOrder $workOrder): JsonResponse`<br>`public function updates(Request $request, WorkOrder $workOrder): JsonResponse`<br>`public function storeUpdate(Request $request, WorkOrder $workOrder, RecordWorkOrderUpdate $record): JsonResponse` |

**Observed route declarations:**

[modules/real-estate-property-management-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/property-management')->group(function (): void {
Route::get('/', [ManagementRecordController::class, 'index']);
Route::post('/', [ManagementRecordController::class, 'store']);
Route::get('/{record}', [ManagementRecordController::class, 'show']);
Route::patch('/{record}', [ManagementRecordController::class, 'update']);
Route::patch('/{record}/details', [ManagementRecordController::class, 'updateDetails']);
Route::post('/{record}/failure', [ManagementRecordController::class, 'recordFailure']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/work-orders')->group(function (): void {
Route::get('/', [WorkOrderController::class, 'index']);
Route::post('/', [WorkOrderController::class, 'store']);
Route::get('/{workOrder}', [WorkOrderController::class, 'show']);
Route::patch('/{workOrder}', [WorkOrderController::class, 'update']);
Route::get('/{workOrder}/updates', [WorkOrderController::class, 'updates']);
Route::post('/{workOrder}/updates', [WorkOrderController::class, 'storeUpdate']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/contractor-quotes')->group(function (): void {
Route::get('/', [VendorQuoteController::class, 'index']);
Route::post('/', [VendorQuoteController::class, 'store']);
Route::get('/{contractorQuote}', [VendorQuoteController::class, 'show']);
Route::patch('/{contractorQuote}', [VendorQuoteController::class, 'update']);
Route::post('/{contractorQuote}/decision', [VendorQuoteController::class, 'decide']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/maintenance')->group(function (): void {
Route::get('/', [MaintenanceRequestController::class, 'index']);
Route::post('/', [MaintenanceRequestController::class, 'store']);
Route::get('/{maintenance}', [MaintenanceRequestController::class, 'show']);
Route::patch('/{maintenance}', [MaintenanceRequestController::class, 'update']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/inspections')->group(function (): void {
Route::get('/', [InspectionController::class, 'index']);
Route::post('/', [InspectionController::class, 'store']);
Route::get('/{inspection}', [InspectionController::class, 'show']);
Route::patch('/{inspection}', [InspectionController::class, 'update']);
```
<!-- layer-implementation-plan:end -->
