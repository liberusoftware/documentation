# Accounting: Document Capture React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#document-capture). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-accounting-document-capture-react-inertia`
**Matching domain module:** `accounting-document-capture`
**Application:** Accounting
**Source feature:** [Document Capture](../features/document-capture.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/document-capture.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Mobile/web/email upload:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **OCR/extraction adapters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Supplier matching:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Line/tax capture:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Confidence:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Duplicate checks:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Review:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Source retention:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-accounting-document-capture-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `mobile-web-email-upload`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `ocr-extraction-adapters`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `supplier-matching`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `line-tax-capture`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `confidence`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `duplicate-checks`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `review`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `source-retention`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-document-capture` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-accounting-erp-laravel-inertia-react`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-accounting-document-capture-react-inertia`](https://github.com/liberusoftware/module-accounting-document-capture-react-inertia) (`@liberusoftware/module-accounting-document-capture-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/document-capture.md) · [Core plan](../core/document-capture.md) · [API plan](../api/document-capture.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Mobile/web/email upload** | Render `mobile/web/email upload` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **OCR/extraction adapters** | Render `ocr/extraction adapters` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Supplier matching** | Render `supplier matching` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Line/tax capture** | Render `line/tax capture` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Confidence** | Render `confidence` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Duplicate checks** | Render `duplicate checks` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Review** | Render `review` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Source retention** | Render `source retention` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

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
