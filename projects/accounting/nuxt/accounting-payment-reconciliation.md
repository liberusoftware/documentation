# Accounting: Accounting Payment Reconciliation Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-payment-reconciliation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-payment-reconciliation-nuxt`
**Matching domain module:** `accounting-payment-reconciliation`
**Application:** Accounting
**Source feature:** [Accounting Payment Reconciliation](../features/accounting-payment-reconciliation.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-payment-reconciliation.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-payment-reconciliation` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Gateway/merchant settlement imports:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Gross-to-net fees/refunds/disputes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Matching:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Missing items:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Provider drift:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-payment-reconciliation-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `gateway-merchant-settlement-imports`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `gross-to-net-fees-refunds-disputes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `matching`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `missing-items`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `provider-drift`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-payment-reconciliation` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-payment-reconciliation.md)) |
| Capability Nuxt module skeleton | [`module-accounting-payment-reconciliation-nuxt`](https://github.com/liberusoftware/module-accounting-payment-reconciliation-nuxt) (`@liberusoftware/module-accounting-payment-reconciliation-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Gateway/merchant settlement imports** | Expose composable and Vue 3 component for `gateway/merchant settlement imports` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payment-reconciliation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Gross-to-net fees/refunds/disputes** | Expose composable and Vue 3 component for `gross-to-net fees/refunds/disputes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payment-reconciliation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Matching** | Expose composable and Vue 3 component for `matching` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payment-reconciliation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Missing items** | Expose composable and Vue 3 component for `missing items` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payment-reconciliation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Provider drift** | Expose composable and Vue 3 component for `provider drift` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payment-reconciliation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [SettlementQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Queries/SettlementQuery.php) | `public function paginate(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function summary(?int $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [IdentifyMissingItems.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/IdentifyMissingItems.php) | `public function handle(SettlementRun $run, array $expected): array` |
| [ImportSettlement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/ImportSettlement.php) | `public function handle(array $attributes, array $items): SettlementRun` |
| [MatchSettlementItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/MatchSettlementItem.php) | `public function handle(SettlementItem $item, string $referenceType, string $referenceId, float $amount, ?int $actorId = null, ?string $idempotencyKey = null): SettlementMatch` |
| [RecordProviderDrift.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/RecordProviderDrift.php) | `public function handle(SettlementRun $run, string $field, mixed $expected, mixed $actual, string $severity = 'warning'): ProviderDrift` |
| [ResolveReconciliationException.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/ResolveReconciliationException.php) | `public function handle(ReconciliationException $exception, int $actorId, string $resolution, bool $waive = false): ReconciliationException` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AuditEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/AuditEvidence.php) | `run_id`, `event_type`, `actor_id`, `payload`, `payload_hash`, `created_at` |
| [ProviderDrift.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/ProviderDrift.php) | `run_id`, `field`, `expected_value`, `actual_value`, `severity`, `status`, `resolution`, `resolved_by`, `resolved_at`, `metadata` |
| [ReconciliationException.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/ReconciliationException.php) | `run_id`, `kind`, `external_ref`, `expected_amount`, `actual_amount`, `currency`, `status`, `severity`, `resolution`, `resolved_by`, `resolved_at`, `metadata` |
| [SettlementItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/SettlementItem.php) | `run_id`, `external_ref`, `type`, `currency`, `gross_amount`, `fee_amount`, `refund_amount`, `dispute_amount`, `net_amount`, `status`, `reference_type`, `reference_id`, `source_payload`, `source_hash`, `metadata` |
| [SettlementMatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/SettlementMatch.php) | `run_id`, `item_id`, `reference_type`, `reference_id`, `matched_amount`, `confidence`, `status`, `matched_by`, `matched_at`, `idempotency_key`, `metadata` |
| [SettlementRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/SettlementRun.php) | `team_id`, `provider`, `merchant_ref`, `settlement_ref`, `period_start`, `period_end`, `currency`, `gross_amount`, `fee_amount`, `refund_amount`, `dispute_amount`, `net_amount`, `status`, `idempotency_key`, `source_hash`, `failure_message`, `metadata` |
| [Payment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-api/src/Models/Payment.php) | `invoice_id`, `payment_date`, `payment_amount`, `qbo_id`, `qbo_sync_token`, `xero_id`, `sage_id`, `journal_entry_id`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PaymentReconciliationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-api/src/Http/Controllers/PaymentReconciliationController.php) | `public function index(Request $request, SettlementQuery $query): mixed`<br>`public function store(Request $request, ImportSettlement $action): JsonResponse`<br>`public function show(SettlementRun $settlementRun): SettlementResource`<br>`public function match(Request $request, SettlementItem $settlementItem, MatchSettlementItem $action): JsonResponse`<br>`public function missing(Request $request, SettlementRun $settlementRun, IdentifyMissingItems $action): JsonResponse`<br>`public function drift(Request $request, SettlementRun $settlementRun, RecordProviderDrift $action): JsonResponse`<br>`public function summary(Request $request, SettlementQuery $query): array` |

**Observed route declarations:**

[modules/accounting-payment-reconciliation-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/payment-reconciliation')->group(function (): void {
Route::get('/', [PaymentReconciliationController::class, 'index'])->name('accounting.payment-reconciliation.list');
Route::post('/', [PaymentReconciliationController::class, 'store'])->name('accounting.payment-reconciliation.create');
Route::get('/summary', [PaymentReconciliationController::class, 'summary'])->name('accounting.payment-reconciliation.summary');
Route::get('/{settlementRun}', [PaymentReconciliationController::class, 'show'])->name('accounting.payment-reconciliation.show');
Route::post('/{settlementRun}/missing-items', [PaymentReconciliationController::class, 'missing'])->name('accounting.payment-reconciliation.missing');
Route::post('/{settlementRun}/provider-drift', [PaymentReconciliationController::class, 'drift'])->name('accounting.payment-reconciliation.drift');
Route::post('/items/{settlementItem}/match', [PaymentReconciliationController::class, 'match'])->name('accounting.payment-reconciliation.match');
```
<!-- layer-implementation-plan:end -->
