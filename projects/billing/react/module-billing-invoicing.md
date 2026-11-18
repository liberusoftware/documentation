# Billing: Module Billing Invoicing React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-invoicing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-billing-module-billing-invoicing-react-inertia`
**Matching domain module:** `module-billing-invoicing`
**Application:** Billing
**Source feature:** [Module Billing Invoicing](../features/module-billing-invoicing.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-billing-invoicing.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Schedules:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Line generation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Tax:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Credits:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Adjustments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **PDFs:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Delivery:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Finalization:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-billing-module-billing-invoicing-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `schedules`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `line-generation`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `tax`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `credits`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `adjustments`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `pdfs`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `delivery`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `finalization`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `module-billing-invoicing` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-billing-laravel-inertia-react`](https://github.com/liberusoftware/project-billing-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-billing-invoicing-react-inertia`](https://github.com/liberusoftware/module-billing-invoicing-react-inertia) (`@liberusoftware/module-billing-invoicing-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/module-billing-invoicing.md) · [Core plan](../core/module-billing-invoicing.md) · [API plan](../api/module-billing-invoicing.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Schedules** | Render `schedules` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Line generation** | Render `line generation` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Tax** | Render `tax` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Credits** | Render `credits` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Adjustments** | Render `adjustments` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **PDFs** | Render `pdfs` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Delivery** | Render `delivery` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Finalization** | Render `finalization` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListInvoices.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Queries/ListInvoices.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddInvoiceLine.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/AddInvoiceLine.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, string $description, int $quantity, int $unitAmountMinor, float $taxRate = 0): InvoiceLine` |
| [ApplyInvoiceAdjustment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/ApplyInvoiceAdjustment.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, int $amountMinor, string $reason, string $type = 'adjustment'): Invoice` |
| [ApplyInvoiceLateFee.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/ApplyInvoiceLateFee.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, int $amountMinor, ?CarbonInterface $at = null): Invoice` |
| [CreateInvoice.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/CreateInvoice.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): Invoice` |
| [CreateInvoiceSchedule.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/CreateInvoiceSchedule.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): InvoiceSchedule` |
| [CreateInvoiceSupport.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/CreateInvoiceSupport.php) | `public function execute(int $teamId, array $attributes): InvoiceSupport` |
| [CreatePaymentPlan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/CreatePaymentPlan.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, int $totalInstallments, string $frequency = 'monthly', ?CarbonInterface $startAt = null): PaymentPlan` |
| [DeliverInvoice.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/DeliverInvoice.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, string $destination, ?int $documentId = null): InvoiceSupport` |
| [FinalizeInvoice.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/FinalizeInvoice.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice): Invoice` |
| [GenerateInvoiceDocument.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/GenerateInvoiceDocument.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, string $format = 'pdf'): InvoiceSupport` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Invoice.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/Invoice.php) | No literal fillable array detected; inspect the model and API schema. |
| [InvoiceLine.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/InvoiceLine.php) | No literal fillable array detected; inspect the model and API schema. |
| [InvoiceSchedule.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/InvoiceSchedule.php) | No literal fillable array detected; inspect the model and API schema. |
| [InvoiceSupport.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/InvoiceSupport.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentPlan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/PaymentPlan.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [InvoiceController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing-api/src/Http/Controllers/InvoiceController.php) | `public function index(Request $request, ListInvoices $query): JsonResponse`<br>`public function store(Request $request, CreateInvoice $create): JsonResponse`<br>`public function line(Request $request, Invoice $invoice, AddInvoiceLine $add): JsonResponse`<br>`public function finalize(Request $request, Invoice $invoice, FinalizeInvoice $finalize): JsonResponse`<br>`public function schedule(Request $request, CreateInvoiceSchedule $create): JsonResponse`<br>`public function runSchedule(Request $request, InvoiceSchedule $schedule, RunInvoiceSchedule $run): JsonResponse`<br>`public function paymentPlan(Request $request, CreatePaymentPlan $create): JsonResponse`<br>`public function runPaymentPlan(Request $request, PaymentPlan $paymentPlan, RunPaymentPlan $run): JsonResponse`<br>`public function adjust(Request $request, Invoice $invoice, ApplyInvoiceAdjustment $adjust): JsonResponse`<br>`public function lateFee(Request $request, Invoice $invoice, ApplyInvoiceLateFee $lateFee): JsonResponse`<br>`public function document(Request $request, Invoice $invoice, GenerateInvoiceDocument $document): JsonResponse`<br>`public function deliver(Request $request, Invoice $invoice, DeliverInvoice $deliver): JsonResponse` |
| [InvoiceSupportController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing-api/src/Http/Controllers/InvoiceSupportController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateInvoiceSupport $create): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-invoicing-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.invoicing.read'])->prefix('api/v1/billing/invoicing/support')->name('billing.invoicing.support.')->group(function (): void {
Route::get('/', [InvoiceSupportController::class, 'index'])->name('index');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.invoicing.write', 'idempotency'])->prefix('api/v1/billing/invoicing/support')->name('billing.invoicing.support.')->group(function (): void {
Route::post('/', [InvoiceSupportController::class, 'store'])->name('store');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.invoicing.read'])->prefix('api/v1/billing/invoicing')->name('billing.invoicing.')->group(function (): void {
Route::get('/', [InvoiceController::class, 'index'])->name('index');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.invoicing.write', 'idempotency'])->prefix('api/v1/billing/invoicing')->name('billing.invoicing.')->group(function (): void {
Route::post('/', [InvoiceController::class, 'store'])->name('store');
Route::post('/schedules', [InvoiceController::class, 'schedule'])->name('schedule');
Route::post('/schedules/{schedule}/run', [InvoiceController::class, 'runSchedule'])->name('schedule.run');
Route::post('/payment-plans', [InvoiceController::class, 'paymentPlan'])->name('payment-plan.create');
Route::post('/payment-plans/{paymentPlan}/run', [InvoiceController::class, 'runPaymentPlan'])->name('payment-plan.run');
Route::post('/{invoice}/lines', [InvoiceController::class, 'line'])->name('line');
Route::post('/{invoice}/finalize', [InvoiceController::class, 'finalize'])->name('finalize');
Route::post('/{invoice}/adjustments', [InvoiceController::class, 'adjust'])->name('adjust');
Route::post('/{invoice}/late-fees', [InvoiceController::class, 'lateFee'])->name('late-fee');
Route::post('/{invoice}/document', [InvoiceController::class, 'document'])->name('document');
Route::post('/{invoice}/deliver', [InvoiceController::class, 'deliver'])->name('deliver');
```
<!-- layer-implementation-plan:end -->
