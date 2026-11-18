# Accounting: Leases Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#leases). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-leases-nuxt`
**Matching domain module:** `accounting-leases`
**Application:** Accounting
**Source feature:** [Leases](../features/leases.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/leases.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-leases` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Lease records:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Payment schedules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Right-of-use assets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Liabilities:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Interest/depreciation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Modifications:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Disclosures (optional):** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-leases-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `lease-records`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `payment-schedules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `right-of-use-assets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `liabilities`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `interest-depreciation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `modifications`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `disclosures-optional`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-leases` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/leases.md)) |
| Capability Nuxt module skeleton | [`module-accounting-leases-nuxt`](https://github.com/liberusoftware/module-accounting-leases-nuxt) (`@liberusoftware/module-accounting-leases-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Lease records** | Expose composable and Vue 3 component for `lease records` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/leases.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Payment schedules** | Expose composable and Vue 3 component for `payment schedules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/leases.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Right-of-use assets** | Expose composable and Vue 3 component for `right-of-use assets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/leases.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Liabilities** | Expose composable and Vue 3 component for `liabilities` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/leases.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Interest/depreciation** | Expose composable and Vue 3 component for `interest/depreciation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/leases.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Modifications** | Expose composable and Vue 3 component for `modifications` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/leases.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Disclosures (optional)** | Expose composable and Vue 3 component for `disclosures (optional)` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/leases.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [LeaseQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Queries/LeaseQuery.php) | `public function leases(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function disclosure(Lease $lease): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDisclosure.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/CreateDisclosure.php) | `public function handle(Lease $lease, string $asOfDate): LeaseDisclosure` |
| [CreateLease.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/CreateLease.php) | `public function handle(array $attributes): Lease` |
| [GenerateSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/GenerateSchedule.php) | `public function handle(Lease $lease): Lease` |
| [ModifyLease.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/ModifyLease.php) | `public function handle(Lease $lease, array $attributes): Lease` |
| [PostPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/PostPayment.php) | `public function handle(LeasePayment $payment): LeasePayment` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Lease.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Models/Lease.php) | `team_id`, `lease_ref`, `name`, `lessor_ref`, `asset_ref`, `commencement_date`, `end_date`, `currency`, `payment_amount`, `payment_frequency`, `interest_rate`, `discount_rate`, `useful_life_months`, `status`, `right_of_use_asset`, `lease_liability`, `accumulated_depreciation`, `metadata` |
| [LeaseDisclosure.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Models/LeaseDisclosure.php) | `lease_id`, `as_of_date`, `remaining_liability`, `current_liability`, `non_current_liability`, `future_payments`, `notes`, `metadata` |
| [LeaseModification.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Models/LeaseModification.php) | `lease_id`, `modification_ref`, `effective_date`, `kind`, `old_term_end`, `new_term_end`, `old_payment_amount`, `new_payment_amount`, `adjustment_amount`, `reason`, `metadata` |
| [LeasePayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Models/LeasePayment.php) | `lease_id`, `payment_ref`, `due_date`, `amount`, `principal_amount`, `interest_amount`, `depreciation_amount`, `status`, `posted_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [LeasesController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases-api/src/Http/Controllers/LeasesController.php) | `public function index(Request $request, LeaseQuery $query): mixed`<br>`public function store(Request $request, CreateLease $action): LeaseResource`<br>`public function show(Lease $lease): LeaseResource`<br>`public function schedule(Lease $lease, GenerateSchedule $action): LeaseResource`<br>`public function modify(Request $request, Lease $lease, ModifyLease $action): LeaseResource`<br>`public function disclosure(Request $request, Lease $lease, CreateDisclosure $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-leases-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/leases')->group(function (): void {
Route::get('/', [LeasesController::class, 'index'])->name('accounting.leases.list');
Route::post('/', [LeasesController::class, 'store'])->name('accounting.leases.create');
Route::get('/{lease}', [LeasesController::class, 'show'])->name('accounting.leases.show');
Route::post('/{lease}/schedule', [LeasesController::class, 'schedule'])->name('accounting.leases.schedule');
Route::post('/{lease}/modify', [LeasesController::class, 'modify'])->name('accounting.leases.modify');
Route::post('/{lease}/disclosure', [LeasesController::class, 'disclosure'])->name('accounting.leases.disclosure');
```
<!-- layer-implementation-plan:end -->
