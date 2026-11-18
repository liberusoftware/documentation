# Accounting: E-Invoicing React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#e-invoicing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-accounting-e-invoicing-react-inertia`
**Matching domain module:** `accounting-e-invoicing`
**Application:** Accounting
**Source feature:** [E-Invoicing](../features/e-invoicing.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/e-invoicing.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Structured invoice/credit formats:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Tax-ID validation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Network/provider routing:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Signatures:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Delivery/receipt status:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Archival:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reconciliation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-accounting-e-invoicing-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `structured-invoice-credit-formats`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `tax-id-validation`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `network-provider-routing`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `signatures`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `delivery-receipt-status`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `archival`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
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

- Package identity, public exports, API dependency, and module dependency match `accounting-e-invoicing` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-accounting-erp-laravel-inertia-react`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-accounting-e-invoicing-react-inertia`](https://github.com/liberusoftware/module-accounting-e-invoicing-react-inertia) (`@liberusoftware/module-accounting-e-invoicing-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/e-invoicing.md) · [Core plan](../core/e-invoicing.md) · [API plan](../api/e-invoicing.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Structured invoice/credit formats** | Render `structured invoice/credit formats` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Tax-ID validation** | Render `tax-id validation` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Network/provider routing** | Render `network/provider routing` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Signatures** | Render `signatures` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Delivery/receipt status** | Render `delivery/receipt status` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Archival** | Render `archival` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Reconciliation** | Render `reconciliation` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EInvoiceQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Queries/EInvoiceQuery.php) | `public function paginate(?int $legalEntityId = null, ?DocumentStatus $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ArchiveEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/ArchiveEInvoice.php) | `public function handle(EInvoiceDocument $d, ?string $actor = null): EInvoiceDocument` |
| [CreateEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/CreateEInvoice.php) | `public function handle(array $a): EInvoiceDocument` |
| [ReconcileEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/ReconcileEInvoice.php) | `public function handle(EInvoiceDocument $d, ?string $actor = null): EInvoiceDocument` |
| [RecordEInvoiceReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/RecordEInvoiceReceipt.php) | `public function handle(EInvoiceDocument $d, bool $accepted, ?string $message = null, ?string $actor = null): EInvoiceDocument` |
| [SignEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/SignEInvoice.php) | `public function handle(EInvoiceDocument $d, string $signature, ?string $actor = null): EInvoiceDocument` |
| [SubmitEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/SubmitEInvoice.php) | `public function handle(EInvoiceDocument $d, string $provider, ?string $actor = null): EInvoiceDocument` |
| [ValidateEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/ValidateEInvoice.php) | `public function handle(EInvoiceDocument $d, ?string $actor = null): EInvoiceDocument` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EInvoiceDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Models/EInvoiceDocument.php) | `legal_entity_id`, `document_ref`, `document_type`, `format`, `status`, `tax_id`, `counterparty_ref`, `currency`, `provider_ref`, `payload`, `signature`, `submitted_at`, `received_at`, `archived_at`, `metadata` |
| [EInvoiceEvent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Models/EInvoiceEvent.php) | `document_id`, `event`, `provider_ref`, `actor_ref`, `message`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [EInvoicingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing-api/src/Http/Controllers/EInvoicingController.php) | `public function __construct(private readonly EInvoiceQuery $query)`<br>`public function index(Request $r): mixed`<br>`public function store(Request $r, CreateEInvoice $a): EInvoiceResource`<br>`public function show(EInvoiceDocument $d): EInvoiceResource`<br>`public function validateDocument(Request $r, EInvoiceDocument $d, ValidateEInvoice $a): EInvoiceResource`<br>`public function sign(Request $r, EInvoiceDocument $d, SignEInvoice $a): EInvoiceResource`<br>`public function submit(Request $r, EInvoiceDocument $d, SubmitEInvoice $a): EInvoiceResource`<br>`public function receipt(Request $r, EInvoiceDocument $d, RecordEInvoiceReceipt $a): EInvoiceResource`<br>`public function reconcile(Request $r, EInvoiceDocument $d, ReconcileEInvoice $a): EInvoiceResource`<br>`public function archive(Request $r, EInvoiceDocument $d, ArchiveEInvoice $a): EInvoiceResource` |

**Observed route declarations:**

[modules/accounting-e-invoicing-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/e-invoicing')->group(function (): void {
Route::middleware('ability:accounting.e-invoicing.read')->group(function (): void {
Route::get('/', [EInvoicingController::class, 'index']);
Route::get('/{d}', [EInvoicingController::class, 'show']);
Route::middleware('ability:accounting.e-invoicing.write')->group(function (): void {
Route::post('/', [EInvoicingController::class, 'store']);
Route::post('/{d}/validate', [EInvoicingController::class, 'validateDocument']);
Route::post('/{d}/sign', [EInvoicingController::class, 'sign']);
Route::post('/{d}/submit', [EInvoicingController::class, 'submit']);
Route::post('/{d}/receipt', [EInvoicingController::class, 'receipt']);
Route::post('/{d}/reconcile', [EInvoicingController::class, 'reconcile']);
Route::post('/{d}/archive', [EInvoicingController::class, 'archive']);
```
<!-- layer-implementation-plan:end -->
