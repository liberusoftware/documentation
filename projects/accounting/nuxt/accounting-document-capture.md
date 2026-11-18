# Accounting: Accounting Document Capture Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-document-capture). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-document-capture-nuxt`
**Matching domain module:** `accounting-document-capture`
**Application:** Accounting
**Source feature:** [Accounting Document Capture](../features/accounting-document-capture.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-document-capture.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-document-capture` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Mobile/web/email upload:** page/component/composable/API-action behavior for this module's authorized workflow.
- **OCR/extraction adapters:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Supplier matching:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Line/tax capture:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Confidence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Duplicate checks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Review:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Source retention:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-document-capture-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `mobile-web-email-upload`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `ocr-extraction-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `supplier-matching`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `line-tax-capture`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `confidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `duplicate-checks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `review`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `source-retention`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-document-capture` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-document-capture.md)) |
| Capability Nuxt module skeleton | [`module-accounting-document-capture-nuxt`](https://github.com/liberusoftware/module-accounting-document-capture-nuxt) (`@liberusoftware/module-accounting-document-capture-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Mobile/web/email upload** | Expose composable and Vue 3 component for `mobile/web/email upload` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-document-capture.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **OCR/extraction adapters** | Expose composable and Vue 3 component for `ocr/extraction adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-document-capture.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Supplier matching** | Expose composable and Vue 3 component for `supplier matching` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-document-capture.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Line/tax capture** | Expose composable and Vue 3 component for `line/tax capture` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-document-capture.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Confidence** | Expose composable and Vue 3 component for `confidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-document-capture.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Duplicate checks** | Expose composable and Vue 3 component for `duplicate checks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-document-capture.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Review** | Expose composable and Vue 3 component for `review` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-document-capture.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Source retention** | Expose composable and Vue 3 component for `source retention` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-document-capture.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CaptureQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Queries/CaptureQuery.php) | `public function paginate(?int $teamId = null, ?CaptureStatus $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ArchiveDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Actions/ArchiveDocument.php) | `public function handle(CapturedDocument $d, ?string $actor = null): CapturedDocument` |
| [ExtractDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Actions/ExtractDocument.php) | `public function handle(CapturedDocument $d, array $extracted, float $confidence, string $adapter, ?string $actor = null): CapturedDocument` |
| [MarkDuplicateDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Actions/MarkDuplicateDocument.php) | `public function handle(CapturedDocument $d, CapturedDocument $original, ?string $actor = null): CapturedDocument` |
| [ReviewDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Actions/ReviewDocument.php) | `public function handle(CapturedDocument $d, bool $approved, ?string $reason = null, ?string $actor = null): CapturedDocument` |
| [UploadDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Actions/UploadDocument.php) | `public function handle(array $a): CapturedDocument` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CaptureEvent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Models/CaptureEvent.php) | `document_id`, `event`, `actor_ref`, `adapter_ref`, `message`, `metadata` |
| [CapturedDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Models/CapturedDocument.php) | `team_id`, `source_channel`, `file_ref`, `checksum`, `mime_type`, `status`, `supplier_ref`, `document_ref`, `extracted_data`, `confidence`, `duplicate_of`, `retention_until`, `reviewed_by`, `reviewed_at`, `rejection_reason`, `metadata` |
| [Document.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture-api/src/Models/Document.php) | `documentable_type`, `documentable_id`, `name`, `disk`, `retention_until`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [DocumentCaptureController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture-api/src/Http/Controllers/DocumentCaptureController.php) | `public function __construct(private readonly CaptureQuery $query)`<br>`public function index(Request $r): mixed`<br>`public function store(Request $r, UploadDocument $a): CapturedDocumentResource`<br>`public function show(CapturedDocument $d): CapturedDocumentResource`<br>`public function extract(Request $r, CapturedDocument $d, ExtractDocument $a): CapturedDocumentResource`<br>`public function review(Request $r, CapturedDocument $d, ReviewDocument $a): CapturedDocumentResource`<br>`public function duplicate(Request $r, CapturedDocument $d, MarkDuplicateDocument $a): CapturedDocumentResource`<br>`public function archive(Request $r, CapturedDocument $d, ArchiveDocument $a): CapturedDocumentResource` |

**Observed route declarations:**

[modules/accounting-document-capture-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/document-capture')->group(function (): void {
Route::middleware('ability:accounting.document-capture.read')->group(function (): void {
Route::get('/', [DocumentCaptureController::class, 'index']);
Route::get('/{d}', [DocumentCaptureController::class, 'show']);
Route::middleware('ability:accounting.document-capture.write')->group(function (): void {
Route::post('/', [DocumentCaptureController::class, 'store']);
Route::post('/{d}/extract', [DocumentCaptureController::class, 'extract']);
Route::post('/{d}/review', [DocumentCaptureController::class, 'review']);
Route::post('/{d}/duplicate', [DocumentCaptureController::class, 'duplicate']);
Route::post('/{d}/archive', [DocumentCaptureController::class, 'archive']);
```
<!-- layer-implementation-plan:end -->
