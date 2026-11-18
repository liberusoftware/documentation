# Accounting: Accounting E Invoicing Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-e-invoicing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-e-invoicing-nuxt`
**Matching domain module:** `accounting-e-invoicing`
**Application:** Accounting
**Source feature:** [Accounting E Invoicing](../features/accounting-e-invoicing.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-e-invoicing.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-e-invoicing` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Structured invoice/credit formats:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tax-ID validation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Network/provider routing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Signatures:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Delivery/receipt status:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Archival:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-e-invoicing-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `structured-invoice-credit-formats`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tax-id-validation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `network-provider-routing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `signatures`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `delivery-receipt-status`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `archival`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
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

- Package identity, public exports, API dependency, and module dependency match `accounting-e-invoicing` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-e-invoicing.md)) |
| Capability Nuxt module skeleton | [`module-accounting-e-invoicing-nuxt`](https://github.com/liberusoftware/module-accounting-e-invoicing-nuxt) (`@liberusoftware/module-accounting-e-invoicing-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Structured invoice/credit formats** | Expose composable and Vue 3 component for `structured invoice/credit formats` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-e-invoicing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Tax-ID validation** | Expose composable and Vue 3 component for `tax-id validation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-e-invoicing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Network/provider routing** | Expose composable and Vue 3 component for `network/provider routing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-e-invoicing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Signatures** | Expose composable and Vue 3 component for `signatures` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-e-invoicing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Delivery/receipt status** | Expose composable and Vue 3 component for `delivery/receipt status` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-e-invoicing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Archival** | Expose composable and Vue 3 component for `archival` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-e-invoicing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reconciliation** | Expose composable and Vue 3 component for `reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-e-invoicing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

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
