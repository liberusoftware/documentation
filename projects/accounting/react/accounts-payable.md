# Accounting: Accounts Payable React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounts-payable). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-accounting-accounts-payable-react-inertia`
**Matching domain module:** `accounting-accounts-payable`
**Application:** Accounting
**Source feature:** [Accounts Payable](../features/accounts-payable.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounts-payable.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Supplier subledger:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Open items:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Aging:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Balances:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Credits:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Disputes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Holds:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Payment terms:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Control-account reconciliation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-accounting-accounts-payable-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `supplier-subledger`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `open-items`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `aging`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `balances`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `credits`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `disputes`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `holds`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `payment-terms`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `control-account-reconciliation`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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
- Test observable behavior with TypeScript, ESLint, Vitest, React Testing Library, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `accounting-accounts-payable` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-accounting-erp-laravel-inertia-react`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-accounting-accounts-payable-react-inertia`](https://github.com/liberusoftware/module-accounting-accounts-payable-react-inertia) (`@liberusoftware/module-accounting-accounts-payable-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/accounts-payable.md) · [Core plan](../core/accounts-payable.md) · [API plan](../api/accounts-payable.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Supplier subledger** | Render `supplier subledger` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Open items** | Render `open items` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Aging** | Render `aging` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Balances** | Render `balances` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Credits** | Render `credits` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Disputes** | Render `disputes` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Holds** | Render `holds` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Payment terms** | Render `payment terms` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Control-account reconciliation** | Render `control-account reconciliation` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

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
