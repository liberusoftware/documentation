# Accounting: Accounting Reimbursements Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-reimbursements). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-reimbursements-nuxt`
**Matching domain module:** `accounting-reimbursements`
**Application:** Accounting
**Source feature:** [Accounting Reimbursements](../features/accounting-reimbursements.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-reimbursements.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-reimbursements` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Approved expense/mileage liabilities:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Payment batches:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Bank export/provider status:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Remittance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Failure:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-reimbursements-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `approved-expense-mileage-liabilities`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `payment-batches`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `bank-export-provider-status`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `remittance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `failure`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
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

- Package identity, public exports, API dependency, and module dependency match `accounting-reimbursements` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-reimbursements.md)) |
| Capability Nuxt module skeleton | [`module-accounting-reimbursements-nuxt`](https://github.com/liberusoftware/module-accounting-reimbursements-nuxt) (`@liberusoftware/module-accounting-reimbursements-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Approved expense/mileage liabilities** | Expose composable and Vue 3 component for `approved expense/mileage liabilities` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-reimbursements.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Payment batches** | Expose composable and Vue 3 component for `payment batches` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-reimbursements.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Bank export/provider status** | Expose composable and Vue 3 component for `bank export/provider status` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-reimbursements.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Remittance** | Expose composable and Vue 3 component for `remittance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-reimbursements.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Failure** | Expose composable and Vue 3 component for `failure` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-reimbursements.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reconciliation** | Expose composable and Vue 3 component for `reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-reimbursements.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePaymentBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Actions/CreatePaymentBatch.php) | `public function handle(array $liabilityIds, ?int $teamId = null): ReimbursementBatch` |
| [CreateReimbursementLiability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Actions/CreateReimbursementLiability.php) | `public function handle(array $attributes): ReimbursementLiability` |
| [ReconcilePaymentBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Actions/ReconcilePaymentBatch.php) | `public function handle(ReimbursementBatch $batch, float $settledAmount, ?string $externalRef = null): ReimbursementReconciliation` |
| [UpdatePaymentProviderStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Actions/UpdatePaymentProviderStatus.php) | `public function handle(ReimbursementBatch $batch, array $attributes): ReimbursementBatch` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReimbursementBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Models/ReimbursementBatch.php) | `team_id`, `currency`, `total_amount`, `status`, `provider`, `provider_ref`, `exported_at`, `submitted_at`, `paid_at`, `failure_message`, `metadata` |
| [ReimbursementLiability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Models/ReimbursementLiability.php) | `team_id`, `payee_ref`, `source_type`, `source_id`, `kind`, `currency`, `amount`, `approved_at`, `status`, `batch_id`, `metadata` |
| [ReimbursementReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Models/ReimbursementReconciliation.php) | `batch_id`, `expected_amount`, `settled_amount`, `variance`, `status`, `external_ref`, `notes`, `metadata` |
| [ReimbursementRemittance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Models/ReimbursementRemittance.php) | `batch_id`, `payee_ref`, `amount`, `currency`, `status`, `document_ref`, `sent_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ReimbursementsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements-api/src/Http/Controllers/ReimbursementsController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateReimbursementLiability $action): mixed`<br>`public function batch(Request $request, CreatePaymentBatch $action): ReimbursementBatch`<br>`public function status(Request $request, ReimbursementBatch $batch, UpdatePaymentProviderStatus $action): ReimbursementBatch`<br>`public function reconcile(Request $request, ReimbursementBatch $batch, ReconcilePaymentBatch $action): mixed` |

**Observed route declarations:**

[modules/accounting-reimbursements-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/reimbursements')->group(function (): void {
Route::middleware('ability:accounting.reimbursements.read')->group(function (): void {
Route::get('/', [ReimbursementsController::class, 'index']);
Route::middleware('ability:accounting.reimbursements.write')->group(function (): void {
Route::post('/', [ReimbursementsController::class, 'store']);
Route::post('/batches', [ReimbursementsController::class, 'batch']);
Route::post('/batches/{batch}/status', [ReimbursementsController::class, 'status']);
Route::post('/batches/{batch}/reconcile', [ReimbursementsController::class, 'reconcile']);
```
<!-- layer-implementation-plan:end -->
