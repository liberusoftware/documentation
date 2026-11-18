# Accounting: Accounting Accounts Receivable Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-accounts-receivable). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-accounting-accounts-receivable-vue-inertia`
**Matching domain module:** `accounting-accounts-receivable`
**Application:** Accounting
**Source feature:** [Accounting Accounts Receivable](../features/accounting-accounts-receivable.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-accounts-receivable.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Customer subledger:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Open items:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Statements:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Aging:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Balances:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Unapplied cash:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Disputes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Credit limits/holds:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Control-account reconciliation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-accounting-accounts-receivable-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `customer-subledger`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `open-items`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `statements`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `aging`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `balances`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `unapplied-cash`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `disputes`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `credit-limits-holds`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `control-account-reconciliation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-accounts-receivable` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-accounts-receivable-vue-inertia`](https://github.com/liberusoftware/module-accounting-accounts-receivable-vue-inertia) (`@liberusoftware/module-accounting-accounts-receivable-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/accounting-accounts-receivable.md) · [Core plan](../core/accounting-accounts-receivable.md) · [API plan](../api/accounting-accounts-receivable.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Customer subledger** | Render `customer subledger` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Open items** | Render `open items` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Statements** | Render `statements` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Aging** | Render `aging` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Balances** | Render `balances` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Unapplied cash** | Render `unapplied cash` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Disputes** | Render `disputes` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Credit limits/holds** | Render `credit limits/holds` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Control-account reconciliation** | Render `control-account reconciliation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AgingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Queries/AgingQuery.php) | `public function handle(?int $partyId = null, ?\DateTimeInterface $asOf = null): array` |
| [ControlAccountReconciliationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Queries/ControlAccountReconciliationQuery.php) | `public function handle(?float $controlBalance = null): array` |
| [CustomerSubledgerQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Queries/CustomerSubledgerQuery.php) | `public function handle(int $partyId): array` |
| [StatementQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Queries/StatementQuery.php) | `public function handle(int $partyId, ?\DateTimeInterface $from = null, ?\DateTimeInterface $to = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApplyReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/ApplyReceipt.php) | `public function handle(ReceivableReceipt $receipt, ReceivableOpenItem $item, float $amount): ReceivableReceipt` |
| [CreateOpenItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/CreateOpenItem.php) | `public function handle(array $attributes): ReceivableOpenItem` |
| [EnsureAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/EnsureAccount.php) | `public function handle(int $partyId): ReceivableAccount` |
| [OpenDispute.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/OpenDispute.php) | `public function handle(ReceivableOpenItem $item, string $reason, ?float $amount = null): ReceivableDispute` |
| [RecalculateAccountBalance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/RecalculateAccountBalance.php) | `public function handle(int $partyId): ReceivableAccount` |
| [RecordReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/RecordReceipt.php) | `public function handle(array $attributes): ReceivableReceipt` |
| [ResolveDispute.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/ResolveDispute.php) | `public function handle(ReceivableDispute $dispute, string $resolution, bool $accepted = false): ReceivableDispute` |
| [SetCreditControl.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/SetCreditControl.php) | `public function handle(int $partyId, ?float $creditLimit = null, ?bool $hold = null, ?string $reason = null): ReceivableAccount` |
| [SyncFinalizedInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/SyncFinalizedInvoice.php) | `public function handle(SalesInvoice $invoice): ReceivableOpenItem` |
| [AccountsReceivablePolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-api/src/Policies/AccountsReceivablePolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, object $model): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, object $model): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReceiptApplication.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Models/ReceiptApplication.php) | `receipt_id`, `open_item_id`, `amount` |
| [ReceivableAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Models/ReceivableAccount.php) | `party_id`, `credit_limit`, `current_balance`, `credit_hold`, `hold_reason`, `control_account_code`, `status`, `metadata` |
| [ReceivableDispute.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Models/ReceivableDispute.php) | `open_item_id`, `amount`, `reason`, `status`, `opened_at`, `resolved_at`, `resolution`, `metadata` |
| [ReceivableOpenItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Models/ReceivableOpenItem.php) | `party_id`, `source_type`, `source_id`, `reference`, `issued_on`, `due_on`, `original_amount`, `applied_amount`, `currency`, `status`, `metadata` |
| [ReceivableReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Models/ReceivableReceipt.php) | `party_id`, `received_on`, `amount`, `applied_amount`, `currency`, `reference`, `status`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [AccountsReceivableController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-api/src/Http/Controllers/AccountsReceivableController.php) | `public function index(Request $request): JsonResponse`<br>`public function receipts(Request $request): JsonResponse`<br>`public function disputes(Request $request): JsonResponse`<br>`public function show(ReceivableOpenItem $openItem): ReceivableOpenItemResource`<br>`public function store(Request $request): ReceivableOpenItemResource`<br>`public function statement(Request $request, int $party): JsonResponse`<br>`public function aging(Request $request): JsonResponse`<br>`public function balances(Request $request, int $party): JsonResponse`<br>`public function receipt(Request $request): JsonResponse`<br>`public function apply(Request $request, ReceivableReceipt $receipt): JsonResponse`<br>`public function dispute(Request $request): JsonResponse`<br>`public function resolve(Request $request, ReceivableDispute $dispute): JsonResponse`<br>`public function credit(Request $request, int $party): JsonResponse`<br>`public function reconcile(Request $request): JsonResponse` |

**Observed route declarations:**

[modules/accounting-accounts-receivable-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/accounts-receivable')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [AccountsReceivableController::class, 'index'])->middleware('ability:accounting.receivables.read');
Route::get('/receipts', [AccountsReceivableController::class, 'receipts'])->middleware('ability:accounting.receivables.read');
Route::get('/disputes', [AccountsReceivableController::class, 'disputes'])->middleware('ability:accounting.receivables.read');
Route::get('/aging', [AccountsReceivableController::class, 'aging'])->middleware('ability:accounting.receivables.read');
Route::get('/reconciliation', [AccountsReceivableController::class, 'reconcile'])->middleware('ability:accounting.receivables.read');
Route::get('/statement/{party}', [AccountsReceivableController::class, 'statement'])->middleware('ability:accounting.receivables.read');
Route::get('/balances/{party}', [AccountsReceivableController::class, 'balances'])->middleware('ability:accounting.receivables.read');
Route::post('/', [AccountsReceivableController::class, 'store'])->middleware('ability:accounting.receivables.write');
Route::post('/receipts', [AccountsReceivableController::class, 'receipt'])->middleware('ability:accounting.receivables.write');
Route::post('/receipts/{receipt}/apply', [AccountsReceivableController::class, 'apply'])->middleware('ability:accounting.receivables.write');
Route::post('/disputes', [AccountsReceivableController::class, 'dispute'])->middleware('ability:accounting.receivables.write');
Route::post('/disputes/{dispute}/resolve', [AccountsReceivableController::class, 'resolve'])->middleware('ability:accounting.receivables.write');
Route::post('/customers/{party}/credit-control', [AccountsReceivableController::class, 'credit'])->middleware('ability:accounting.receivables.write');
Route::get('/{openItem}', [AccountsReceivableController::class, 'show'])->middleware('ability:accounting.receivables.read');
```
<!-- layer-implementation-plan:end -->
