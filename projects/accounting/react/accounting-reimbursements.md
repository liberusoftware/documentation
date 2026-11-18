# Accounting: Accounting Reimbursements React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-reimbursements). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-accounting-accounting-reimbursements-react-inertia`
**Matching domain module:** `accounting-reimbursements`
**Application:** Accounting
**Source feature:** [Accounting Reimbursements](../features/accounting-reimbursements.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-reimbursements.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Approved expense/mileage liabilities:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Payment batches:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Bank export/provider status:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Remittance:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Failure:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reconciliation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-accounting-accounting-reimbursements-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `approved-expense-mileage-liabilities`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `payment-batches`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `bank-export-provider-status`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `remittance`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `failure`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `reconciliation`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-reimbursements` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-accounting-erp-laravel-inertia-react`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-accounting-reimbursements-react-inertia`](https://github.com/liberusoftware/module-accounting-reimbursements-react-inertia) (`@liberusoftware/module-accounting-reimbursements-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/accounting-reimbursements.md) · [Core plan](../core/accounting-reimbursements.md) · [API plan](../api/accounting-reimbursements.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Approved expense/mileage liabilities** | Render `approved expense/mileage liabilities` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Payment batches** | Render `payment batches` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Bank export/provider status** | Render `bank export/provider status` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Remittance** | Render `remittance` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Failure** | Render `failure` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Reconciliation** | Render `reconciliation` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

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
