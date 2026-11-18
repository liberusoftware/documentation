# Billing: Payments Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payments). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-billing-payments-vue-inertia`
**Matching domain module:** `billing-payments`
**Application:** Billing
**Source feature:** [Payments](../features/payments.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/payments.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Unified payment-contracts and payment-core integration:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Methods and vaulted payment instruments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Mandates and Direct Debit lifecycles:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Gateway drivers and capability discovery:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Capture, partial invoice payments, and allocation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Refunds and credit reversals:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Disputes and chargeback evidence:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reconciliation and settlement batches:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-billing-payments-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `unified-payment-contracts-and-payment-core-integration`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `methods-and-vaulted-payment-instruments`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `mandates-and-direct-debit-lifecycles`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `gateway-drivers-and-capability-discovery`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `capture-partial-invoice-payments-and-allocation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `refunds-and-credit-reversals`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `disputes-and-chargeback-evidence`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `reconciliation-and-settlement-batches`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `billing-payments` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-billing-laravel-inertia-vue`](https://github.com/liberusoftware/project-billing-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-billing-payments-vue-inertia`](https://github.com/liberusoftware/module-billing-payments-vue-inertia) (`@liberusoftware/module-billing-payments-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/payments.md) · [Core plan](../core/payments.md) · [API plan](../api/payments.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Unified payment-contracts and payment-core integration** | Render `unified payment-contracts and payment-core integration` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Methods and vaulted payment instruments** | Render `methods and vaulted payment instruments` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Mandates and Direct Debit lifecycles** | Render `mandates and direct debit lifecycles` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Gateway drivers and capability discovery** | Render `gateway drivers and capability discovery` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Capture, partial invoice payments, and allocation** | Render `capture, partial invoice payments, and allocation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Refunds and credit reversals** | Render `refunds and credit reversals` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Disputes and chargeback evidence** | Render `disputes and chargeback evidence` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Reconciliation and settlement batches** | Render `reconciliation and settlement batches` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListPayments.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Queries/ListPayments.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocatePayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/AllocatePayment.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Payment $payment, int $amountMinor, ?int $invoiceId = null): PaymentAllocation` |
| [CapturePayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/CapturePayment.php) | `public function __construct(private DatabaseManager $database, private GatewayManager $gateways)`<br>`public function execute(Payment $payment): Payment` |
| [CreatePayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/CreatePayment.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): Payment` |
| [CreatePaymentMandate.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/CreatePaymentMandate.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): PaymentMandate` |
| [CreatePaymentMethod.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/CreatePaymentMethod.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): PaymentMethod` |
| [OpenDispute.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/OpenDispute.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Payment $payment, int $amountMinor, string $reason): PaymentDispute` |
| [ReconcilePayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/ReconcilePayment.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Payment $payment, string $providerReference, bool $matched = true, ?string $notes = null): PaymentReconciliation` |
| [RefundPayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/RefundPayment.php) | `public function __construct(private DatabaseManager $database, private GatewayManager $gateways)`<br>`public function execute(Payment $payment, int $amountMinor, string $reason = 'requested'): PaymentRefund` |
| [TransitionPaymentMandate.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/TransitionPaymentMandate.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(PaymentMandate $mandate, string $status): PaymentMandate` |
| [TransitionPaymentMethod.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/TransitionPaymentMethod.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(PaymentMethod $method, PaymentMethodStatus $status): PaymentMethod` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Payment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/Payment.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentAllocation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentAllocation.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentDispute.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentDispute.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentMandate.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentMandate.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentMethod.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentMethod.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentReconciliation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentReconciliation.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentRefund.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentRefund.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [PaymentController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-api/src/Http/Controllers/PaymentController.php) | `public function index(Request $request, ListPayments $query): JsonResponse`<br>`public function show(Request $request, Payment $payment): JsonResponse`<br>`public function store(Request $request, CreatePayment $create): JsonResponse`<br>`public function capture(Request $request, Payment $payment, CapturePayment $capture): JsonResponse`<br>`public function refund(Request $request, Payment $payment, RefundPayment $refund): JsonResponse`<br>`public function dispute(Request $request, Payment $payment, OpenDispute $dispute): JsonResponse`<br>`public function allocate(Request $request, Payment $payment, AllocatePayment $allocate): JsonResponse`<br>`public function reconcile(Request $request, Payment $payment, ReconcilePayment $reconcile): JsonResponse` |
| [PaymentMethodController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-api/src/Http/Controllers/PaymentMethodController.php) | `public function methods(Request $request): JsonResponse`<br>`public function storeMethod(Request $request, CreatePaymentMethod $create): JsonResponse`<br>`public function mandates(Request $request): JsonResponse`<br>`public function storeMandate(Request $request, CreatePaymentMandate $create): JsonResponse`<br>`public function transitionMethod(Request $request, PaymentMethod $method, TransitionPaymentMethod $transition): JsonResponse`<br>`public function transitionMandate(Request $request, PaymentMandate $mandate, TransitionPaymentMandate $transition): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-payments-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.payments.read'])
Route::get('/', [PaymentController::class, 'index'])->name('index');
Route::get('/{payment}', [PaymentController::class, 'show'])->whereNumber('payment')->name('show');
Route::get('/methods', [PaymentMethodController::class, 'methods'])->name('methods.index');
Route::get('/mandates', [PaymentMethodController::class, 'mandates'])->name('mandates.index');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.payments.write', 'idempotency'])
Route::post('/', [PaymentController::class, 'store'])->name('store');
Route::post('/methods', [PaymentMethodController::class, 'storeMethod'])->name('methods.store');
Route::post('/mandates', [PaymentMethodController::class, 'storeMandate'])->name('mandates.store');
Route::patch('/methods/{method}/status', [PaymentMethodController::class, 'transitionMethod'])->whereNumber('method')->name('methods.status');
Route::patch('/mandates/{mandate}/status', [PaymentMethodController::class, 'transitionMandate'])->whereNumber('mandate')->name('mandates.status');
Route::post('/{payment}/capture', [PaymentController::class, 'capture'])->name('capture');
Route::post('/{payment}/refund', [PaymentController::class, 'refund'])->name('refund');
Route::post('/{payment}/dispute', [PaymentController::class, 'dispute'])->name('dispute');
Route::post('/{payment}/allocate', [PaymentController::class, 'allocate'])->name('allocate');
Route::post('/{payment}/reconcile', [PaymentController::class, 'reconcile'])->name('reconcile');
```
<!-- layer-implementation-plan:end -->
