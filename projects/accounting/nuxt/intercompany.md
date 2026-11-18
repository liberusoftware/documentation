# Accounting: Intercompany Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#intercompany). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-intercompany-nuxt`
**Matching domain module:** `accounting-intercompany`
**Application:** Accounting
**Source feature:** [Intercompany](../features/intercompany.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/intercompany.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-intercompany` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Counterparties:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Trading rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Paired transactions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Confirmations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Settlement:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Differences:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Transfer-pricing evidence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-intercompany-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `counterparties`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `trading-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `paired-transactions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `confirmations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `settlement`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `differences`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `transfer-pricing-evidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
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

- Package identity, public exports, API dependency, and module dependency match `accounting-intercompany` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/intercompany.md)) |
| Capability Nuxt module skeleton | [`module-accounting-intercompany-nuxt`](https://github.com/liberusoftware/module-accounting-intercompany-nuxt) (`@liberusoftware/module-accounting-intercompany-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Counterparties** | Expose composable and Vue 3 component for `counterparties` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/intercompany.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Trading rules** | Expose composable and Vue 3 component for `trading rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/intercompany.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Paired transactions** | Expose composable and Vue 3 component for `paired transactions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/intercompany.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Confirmations** | Expose composable and Vue 3 component for `confirmations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/intercompany.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Settlement** | Expose composable and Vue 3 component for `settlement` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/intercompany.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Differences** | Expose composable and Vue 3 component for `differences` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/intercompany.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Transfer-pricing evidence** | Expose composable and Vue 3 component for `transfer-pricing evidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/intercompany.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reconciliation** | Expose composable and Vue 3 component for `reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/intercompany.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [IntercompanyQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Queries/IntercompanyQuery.php) | `public function paginate(?int $teamId = null, ?TransactionStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function reconciliationSummary(IntercompanyTransaction $transaction): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddTransferPricingEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/AddTransferPricingEvidence.php) | `public function handle(IntercompanyTransaction $transaction, array $a): TransferPricingEvidence` |
| [ConfigureTradingRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/ConfigureTradingRule.php) | `public function handle(IntercompanyCounterparty $counterparty, array $a): TradingRule` |
| [ConfirmTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/ConfirmTransaction.php) | `public function handle(IntercompanyTransaction $transaction, string $entity, bool $confirmed, ?string $comment = null): IntercompanyTransaction` |
| [CreateCounterparty.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/CreateCounterparty.php) | `public function handle(array $a): IntercompanyCounterparty` |
| [CreateTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/CreateTransaction.php) | `public function handle(IntercompanyCounterparty $counterparty, array $a): IntercompanyTransaction` |
| [ReconcileIntercompany.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/ReconcileIntercompany.php) | `public function handle(array $a): IntercompanyReconciliation` |
| [RecordDifference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/RecordDifference.php) | `public function handle(IntercompanyTransaction $transaction, array $a): IntercompanyDifference` |
| [SettleTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/SettleTransaction.php) | `public function handle(IntercompanyTransaction $transaction, array $a): IntercompanyTransaction` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [IntercompanyConfirmation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanyConfirmation.php) | `transaction_id`, `entity_ref`, `status`, `confirmed_amount`, `comment`, `actor_ref`, `confirmed_at`, `metadata` |
| [IntercompanyCounterparty.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanyCounterparty.php) | `team_id`, `entity_ref`, `counterparty_ref`, `name`, `default_currency`, `active`, `metadata` |
| [IntercompanyDifference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanyDifference.php) | `transaction_id`, `difference_ref`, `amount`, `reason`, `status`, `actor_ref`, `resolved_at`, `metadata` |
| [IntercompanyReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanyReconciliation.php) | `team_id`, `reconciliation_ref`, `period_ref`, `entity_ref`, `counterparty_ref`, `transaction_count`, `source_total`, `counterparty_total`, `difference_total`, `status`, `actor_ref`, `reconciled_at`, `metadata` |
| [IntercompanySettlement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanySettlement.php) | `transaction_id`, `settlement_ref`, `amount`, `currency`, `settled_at`, `source_ref`, `metadata` |
| [IntercompanyTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanyTransaction.php) | `team_id`, `transaction_ref`, `counterparty_id`, `source_entity_ref`, `target_entity_ref`, `transaction_type`, `description`, `amount`, `currency`, `status`, `transaction_date`, `metadata` |
| [TradingRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/TradingRule.php) | `counterparty_id`, `rule_ref`, `description`, `pricing_method`, `markup_percent`, `currency`, `active`, `metadata` |
| [TransferPricingEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/TransferPricingEvidence.php) | `transaction_id`, `evidence_ref`, `kind`, `file_ref`, `description`, `arm_length_value`, `currency`, `captured_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [IntercompanyController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany-api/src/Http/Controllers/IntercompanyController.php) | `public function __construct(private readonly IntercompanyQuery $query)`<br>`public function index(Request $r): IntercompanyTransactionResource`<br>`public function counterparty(Request $r, CreateCounterparty $a): JsonResponse`<br>`public function rule(Request $r, IntercompanyCounterparty $counterparty, ConfigureTradingRule $a): JsonResponse`<br>`public function store(Request $r, IntercompanyCounterparty $counterparty, CreateTransaction $a): IntercompanyTransactionResource`<br>`public function show(IntercompanyTransaction $transaction): IntercompanyTransactionResource`<br>`public function confirm(Request $r, IntercompanyTransaction $transaction, ConfirmTransaction $a): IntercompanyTransactionResource`<br>`public function settle(Request $r, IntercompanyTransaction $transaction, SettleTransaction $a): IntercompanyTransactionResource`<br>`public function difference(Request $r, IntercompanyTransaction $transaction, RecordDifference $a): JsonResponse`<br>`public function evidence(Request $r, IntercompanyTransaction $transaction, AddTransferPricingEvidence $a): JsonResponse`<br>`public function summary(IntercompanyTransaction $transaction): JsonResponse`<br>`public function reconcile(Request $r, ReconcileIntercompany $a): JsonResponse` |

**Observed route declarations:**

[modules/accounting-intercompany-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/intercompany')->group(function (): void {
Route::get('/', [IntercompanyController::class, 'index'])->name('accounting.intercompany.list');
Route::post('/counterparties', [IntercompanyController::class, 'counterparty'])->name('accounting.intercompany.counterparty');
Route::post('/counterparties/{counterparty}/rules', [IntercompanyController::class, 'rule'])->name('accounting.intercompany.rule');
Route::post('/counterparties/{counterparty}/transactions', [IntercompanyController::class, 'store'])->name('accounting.intercompany.create');
Route::get('/transactions/{transaction}', [IntercompanyController::class, 'show'])->name('accounting.intercompany.show');
Route::post('/transactions/{transaction}/confirm', [IntercompanyController::class, 'confirm'])->name('accounting.intercompany.confirm');
Route::post('/transactions/{transaction}/settle', [IntercompanyController::class, 'settle'])->name('accounting.intercompany.settle');
Route::post('/transactions/{transaction}/differences', [IntercompanyController::class, 'difference'])->name('accounting.intercompany.difference');
Route::post('/transactions/{transaction}/evidence', [IntercompanyController::class, 'evidence'])->name('accounting.intercompany.evidence');
Route::get('/transactions/{transaction}/summary', [IntercompanyController::class, 'summary'])->name('accounting.intercompany.summary');
Route::post('/reconciliations', [IntercompanyController::class, 'reconcile'])->name('accounting.intercompany.reconcile');
```
<!-- layer-implementation-plan:end -->
