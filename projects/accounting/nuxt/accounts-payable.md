# Accounting: Accounts Payable Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounts-payable). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounts-payable-nuxt`
**Matching domain module:** `accounting-accounts-payable`
**Application:** Accounting
**Source feature:** [Accounts Payable](../features/accounts-payable.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounts-payable.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-accounts-payable` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Supplier subledger:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Open items:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Aging:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Balances:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Credits:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Disputes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Holds:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Payment terms:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Control-account reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounts-payable-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `supplier-subledger`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `open-items`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `aging`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `balances`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `credits`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `disputes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `holds`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `payment-terms`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `control-account-reconciliation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-accounts-payable` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounts-payable.md)) |
| Capability Nuxt module skeleton | [`module-accounting-accounts-payable-nuxt`](https://github.com/liberusoftware/module-accounting-accounts-payable-nuxt) (`@liberusoftware/module-accounting-accounts-payable-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Supplier subledger** | Expose composable and Vue 3 component for `supplier subledger` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounts-payable.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Open items** | Expose composable and Vue 3 component for `open items` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounts-payable.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Aging** | Expose composable and Vue 3 component for `aging` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounts-payable.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Balances** | Expose composable and Vue 3 component for `balances` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounts-payable.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Credits** | Expose composable and Vue 3 component for `credits` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounts-payable.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Disputes** | Expose composable and Vue 3 component for `disputes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounts-payable.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Holds** | Expose composable and Vue 3 component for `holds` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounts-payable.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Payment terms** | Expose composable and Vue 3 component for `payment terms` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounts-payable.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Control-account reconciliation** | Expose composable and Vue 3 component for `control-account reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounts-payable.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AgingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Queries/AgingQuery.php) | `public function handle(?int $partyId = null, ?\DateTimeInterface $asOf = null): array` |
| [ControlAccountReconciliationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Queries/ControlAccountReconciliationQuery.php) | `public function handle(): array` |
| [SupplierSubledgerQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Queries/SupplierSubledgerQuery.php) | `public function handle(int $partyId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApplyPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/ApplyPayment.php) | `public function handle(PayablePayment $payment, PayableOpenItem $item, float $amount): PayablePayment` |
| [CreateOpenItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/CreateOpenItem.php) | `public function handle(array $attributes): PayableOpenItem` |
| [EnsureAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/EnsureAccount.php) | `public function handle(int $partyId): PayableAccount` |
| [OpenDispute.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/OpenDispute.php) | `public function handle(PayableOpenItem $item, string $reason, ?float $amount = null): PayableDispute` |
| [RecalculateAccountBalance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/RecalculateAccountBalance.php) | `public function handle(int $partyId): PayableAccount` |
| [RecordPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/RecordPayment.php) | `public function handle(array $attributes): PayablePayment` |
| [ResolveDispute.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/ResolveDispute.php) | `public function handle(PayableDispute $dispute, string $resolution, bool $accepted = false): PayableDispute` |
| [SetPaymentControl.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/SetPaymentControl.php) | `public function handle(int $partyId, ?bool $paymentHold = null, ?string $holdReason = null): PayableAccount` |
| [AccountingAccountsPayablePolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-api/src/Policies/AccountingAccountsPayablePolicy.php) | `public function viewAny(?object $user = null): bool`<br>`public function view(?object $user, object $item): bool`<br>`public function create(?object $user = null): bool`<br>`public function update(?object $user, object $item): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PayableAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Models/PayableAccount.php) | `party_id`, `current_balance`, `payment_hold`, `hold_reason`, `control_account_code`, `status`, `metadata` |
| [PayableDispute.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Models/PayableDispute.php) | `open_item_id`, `amount`, `reason`, `status`, `opened_at`, `resolved_at`, `resolution`, `metadata` |
| [PayableOpenItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Models/PayableOpenItem.php) | `party_id`, `source_type`, `source_id`, `reference`, `issued_on`, `due_on`, `original_amount`, `paid_amount`, `currency`, `payment_terms`, `status`, `metadata` |
| [PayablePayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Models/PayablePayment.php) | `party_id`, `paid_on`, `amount`, `applied_amount`, `currency`, `reference`, `status`, `metadata` |
| [PaymentApplication.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Models/PaymentApplication.php) | `payment_id`, `open_item_id`, `amount` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PayableOpenItemController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-api/src/Http/Controllers/PayableOpenItemController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateOpenItem $action): PayableOpenItemResource`<br>`public function show(string $payableOpenItem): PayableOpenItemResource`<br>`public function aging(Request $request, AgingQuery $query): JsonResponse`<br>`public function balances(string $party, SupplierSubledgerQuery $query): JsonResponse`<br>`public function payment(Request $request, RecordPayment $action): JsonResponse`<br>`public function apply(Request $request, string $payment, ApplyPayment $action): JsonResponse`<br>`public function dispute(Request $request, OpenDispute $action): JsonResponse`<br>`public function resolve(Request $request, string $dispute, ResolveDispute $action): JsonResponse`<br>`public function paymentControl(Request $request, string $party, SetPaymentControl $action): JsonResponse`<br>`public function reconcile(ControlAccountReconciliationQuery $query): JsonResponse` |

**Observed route declarations:**

[modules/accounting-accounts-payable-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/accounts-payable')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.payables.read')->group(function (): void {
Route::get('/', [PayableOpenItemController::class, 'index']);
Route::get('/aging', [PayableOpenItemController::class, 'aging']);
Route::get('/balances/{party}', [PayableOpenItemController::class, 'balances']);
Route::get('/reconciliation', [PayableOpenItemController::class, 'reconcile']);
Route::get('/open-items/{payableOpenItem}', [PayableOpenItemController::class, 'show']);
Route::middleware('ability:accounting.payables.write')->group(function (): void {
Route::post('/open-items', [PayableOpenItemController::class, 'store']);
Route::post('/payments', [PayableOpenItemController::class, 'payment']);
Route::post('/payments/{payment}/apply', [PayableOpenItemController::class, 'apply']);
Route::post('/disputes', [PayableOpenItemController::class, 'dispute']);
Route::post('/disputes/{dispute}/resolve', [PayableOpenItemController::class, 'resolve']);
Route::post('/suppliers/{party}/payment-control', [PayableOpenItemController::class, 'paymentControl']);
```
<!-- layer-implementation-plan:end -->
