# Billing: Module Billing Payments Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-payments). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-billing-module-billing-payments-nuxt`
**Matching domain module:** `module-billing-payments`
**Application:** Billing
**Source feature:** [Module Billing Payments](../features/module-billing-payments.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-billing-payments.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `module-billing-payments` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Unified payment-contracts and payment-core integration:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Methods and vaulted payment instruments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Mandates and Direct Debit lifecycles:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Gateway drivers and capability discovery:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Capture and allocation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Refunds and disputes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-billing-module-billing-payments-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `unified-payment-contracts-and-payment-core-integration`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `methods-and-vaulted-payment-instruments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `mandates-and-direct-debit-lifecycles`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `gateway-drivers-and-capability-discovery`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `capture-and-allocation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `refunds-and-disputes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
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

- Package identity, public exports, API dependency, and module dependency match `module-billing-payments` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-billing-nuxt-vue`](https://github.com/liberusoftware/project-billing-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-billing-payments.md)) |
| Capability Nuxt module skeleton | [`module-billing-payments-nuxt`](https://github.com/liberusoftware/module-billing-payments-nuxt) (`@liberusoftware/module-billing-payments-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Unified payment-contracts and payment-core integration** | Expose composable and Vue 3 component for `unified payment-contracts and payment-core integration` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-payments.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Methods and vaulted payment instruments** | Expose composable and Vue 3 component for `methods and vaulted payment instruments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-payments.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Mandates and Direct Debit lifecycles** | Expose composable and Vue 3 component for `mandates and direct debit lifecycles` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-payments.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Gateway drivers and capability discovery** | Expose composable and Vue 3 component for `gateway drivers and capability discovery` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-payments.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Capture and allocation** | Expose composable and Vue 3 component for `capture and allocation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-payments.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Refunds and disputes** | Expose composable and Vue 3 component for `refunds and disputes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-payments.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Reconciliation** | Expose composable and Vue 3 component for `reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-payments.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |

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
