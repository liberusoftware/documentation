# Accounting: Mileage Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#mileage). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-mileage-nuxt`
**Matching domain module:** `accounting-mileage`
**Application:** Accounting
**Source feature:** [Mileage](../features/mileage.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/mileage.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-mileage` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Vehicles/rates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Trip capture/import:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Distance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Business purpose:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Projects:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Policy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approval:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reimbursement:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Regional reporting:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-mileage-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `vehicles-rates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `trip-capture-import`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `distance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `business-purpose`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `projects`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `policy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approval`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reimbursement`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `regional-reporting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-mileage` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/mileage.md)) |
| Capability Nuxt module skeleton | [`module-accounting-mileage-nuxt`](https://github.com/liberusoftware/module-accounting-mileage-nuxt) (`@liberusoftware/module-accounting-mileage-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Vehicles/rates** | Expose composable and Vue 3 component for `vehicles/rates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mileage.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Trip capture/import** | Expose composable and Vue 3 component for `trip capture/import` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mileage.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Distance** | Expose composable and Vue 3 component for `distance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mileage.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Business purpose** | Expose composable and Vue 3 component for `business purpose` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mileage.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Projects** | Expose composable and Vue 3 component for `projects` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mileage.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Policy** | Expose composable and Vue 3 component for `policy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mileage.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Approval** | Expose composable and Vue 3 component for `approval` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mileage.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reimbursement** | Expose composable and Vue 3 component for `reimbursement` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mileage.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Regional reporting** | Expose composable and Vue 3 component for `regional reporting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mileage.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [MileageQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Queries/MileageQuery.php) | `public function trips(?int $teamId = null, int $perPage = 25): LengthAwarePaginator`<br>`public function rates(?int $teamId = null, int $perPage = 25): LengthAwarePaginator`<br>`public function regionalReport(?int $teamId = null, ?string $region = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveTrip.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/ApproveTrip.php) | `public function handle(MileageTrip $trip, string $actor, bool $approved = true, ?string $reason = null): MileageTrip` |
| [CaptureTrip.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/CaptureTrip.php) | `public function handle(array $attributes): MileageTrip` |
| [CreateVehicle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/CreateVehicle.php) | `public function handle(array $attributes): Vehicle` |
| [RecordMileageRate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/RecordMileageRate.php) | `public function handle(array $attributes): MileageRate` |
| [ReimburseTrip.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/ReimburseTrip.php) | `public function handle(MileageTrip $trip, string $payee, ?string $externalRef = null): MileageReimbursement` |
| [SubmitTrip.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/SubmitTrip.php) | `public function handle(MileageTrip $trip): MileageTrip` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MileageApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileageApproval.php) | `trip_id`, `actor_ref`, `decision`, `reason`, `decided_at`, `metadata` |
| [MileagePolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileagePolicy.php) | `team_id`, `name`, `region`, `max_distance_per_trip`, `max_distance_per_day`, `requires_purpose`, `requires_project`, `approval_threshold`, `currency`, `active`, `metadata` |
| [MileageRate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileageRate.php) | `team_id`, `region`, `vehicle_type`, `currency`, `rate_per_distance`, `effective_from`, `effective_until`, `active`, `metadata` |
| [MileageReimbursement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileageReimbursement.php) | `trip_id`, `payee_ref`, `currency`, `amount`, `status`, `external_ref`, `failure_message`, `paid_at`, `metadata` |
| [MileageTrip.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileageTrip.php) | `team_id`, `trip_ref`, `employee_ref`, `vehicle_id`, `rate_id`, `policy_id`, `project_ref`, `origin`, `destination`, `trip_date`, `distance`, `distance_unit`, `business_purpose`, `region`, `currency`, `reimbursement_amount`, `status`, `source`, `source_hash`, `submitted_at`, `approved_at`, `reimbursed_at`, `metadata` |
| [Vehicle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/Vehicle.php) | `team_id`, `owner_ref`, `registration`, `make`, `model`, `fuel_type`, `co2_g_per_km`, `active`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MileageController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage-api/src/Http/Controllers/MileageController.php) | `public function index(Request $request, MileageQuery $query): mixed`<br>`public function store(Request $request, CaptureTrip $action): MileageResource`<br>`public function show(MileageTrip $trip): MileageResource`<br>`public function vehicles(Request $request): mixed`<br>`public function vehicle(Request $request, CreateVehicle $action): JsonResponse`<br>`public function rate(Request $request, RecordMileageRate $action): JsonResponse`<br>`public function submit(MileageTrip $trip, SubmitTrip $action): MileageResource`<br>`public function approve(Request $request, MileageTrip $trip, ApproveTrip $action): MileageResource`<br>`public function reimburse(Request $request, MileageTrip $trip, ReimburseTrip $action): JsonResponse`<br>`public function report(Request $request, MileageQuery $query): array` |

**Observed route declarations:**

[modules/accounting-mileage-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/mileage')->group(function (): void {
Route::get('/', [MileageController::class, 'index'])->name('accounting.mileage.list');
Route::post('/', [MileageController::class, 'store'])->name('accounting.mileage.create');
Route::get('/vehicles', [MileageController::class, 'vehicles'])->name('accounting.mileage.vehicles');
Route::post('/vehicles', [MileageController::class, 'vehicle'])->name('accounting.mileage.vehicle');
Route::post('/rates', [MileageController::class, 'rate'])->name('accounting.mileage.rate');
Route::get('/report/regional', [MileageController::class, 'report'])->name('accounting.mileage.report');
Route::get('/{trip}', [MileageController::class, 'show'])->name('accounting.mileage.get');
Route::post('/{trip}/submit', [MileageController::class, 'submit'])->name('accounting.mileage.submit');
Route::post('/{trip}/approve', [MileageController::class, 'approve'])->name('accounting.mileage.approve');
Route::post('/{trip}/reimburse', [MileageController::class, 'reimburse'])->name('accounting.mileage.reimburse');
```
<!-- layer-implementation-plan:end -->
