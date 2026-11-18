# Real Estate: Real Estate Media And Documents Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-media-and-documents). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-real-estate-real-estate-media-and-documents-vue-inertia`
**Matching domain module:** `real-estate-media-and-documents`
**Application:** Real Estate
**Source feature:** [Real Estate Media And Documents](../features/real-estate-media-and-documents.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/real-estate-media-and-documents.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Photos:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Floorplans:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Video:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Certificates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Rights:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Ordering:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Brochures:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Retention:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-real-estate-real-estate-media-and-documents-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `photos`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `floorplans`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `video`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `certificates`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `rights`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `ordering`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `brochures`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `retention`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `real-estate-media-and-documents` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-real-estate-laravel-inertia-vue`](https://github.com/liberusoftware/project-real-estate-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-real-estate-media-and-documents-vue-inertia`](https://github.com/liberusoftware/module-real-estate-media-and-documents-vue-inertia) (`@liberusoftware/module-real-estate-media-and-documents-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/real-estate-media-and-documents.md) · [Core plan](../core/real-estate-media-and-documents.md) · [API plan](../api/real-estate-media-and-documents.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Photos** | Render `photos` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Floorplans** | Render `floorplans` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Video** | Render `video` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Certificates** | Render `certificates` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Rights** | Render `rights` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Ordering** | Render `ordering` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Brochures** | Render `brochures` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Retention** | Render `retention` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [MediaDocumentPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Policies/MediaDocumentPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, MediaDocument $mediaDocument): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, MediaDocument $mediaDocument): bool`<br>`public function delete(AuthUser $authUser, MediaDocument $mediaDocument): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, MediaDocument $mediaDocument): bool`<br>`public function forceDelete(AuthUser $authUser, MediaDocument $mediaDocument): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, MediaDocument $mediaDocument): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DocumentCategory.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentCategory.php) | No literal fillable array detected; inspect the model and API schema. |
| [DocumentEnvelope.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentEnvelope.php) | No literal fillable array detected; inspect the model and API schema. |
| [DocumentEnvelopeSignature.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentEnvelopeSignature.php) | No literal fillable array detected; inspect the model and API schema. |
| [DocumentParticipant.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentParticipant.php) | No literal fillable array detected; inspect the model and API schema. |
| [DocumentSignature.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentSignature.php) | No literal fillable array detected; inspect the model and API schema. |
| [DocumentTemplate.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentTemplate.php) | No literal fillable array detected; inspect the model and API schema. |
| [DocumentVersion.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentVersion.php) | No literal fillable array detected; inspect the model and API schema. |
| [HomeReport.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/HomeReport.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [DocumentWorkflowController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents-api/src/Http/Controllers/DocumentWorkflowController.php) | `public function store(Request $request, DocumentTemplate $documentTemplate, CreateDocumentEnvelope $create): JsonResponse`<br>`public function show(Request $request, DocumentEnvelope $documentEnvelope): JsonResponse`<br>`public function sign(Request $request, DocumentEnvelope $documentEnvelope, DocumentParticipant $documentParticipant, SignDocumentEnvelope $sign): JsonResponse` |
| [HomeReportController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents-api/src/Http/Controllers/HomeReportController.php) | `public function index(Request $r, Property $property): JsonResponse`<br>`public function store(Request $r, Property $property, CreateHomeReport $create): JsonResponse`<br>`public function upload(Request $r, HomeReport $homeReport, UploadHomeReportFile $upload): JsonResponse` |
| [MediaDocumentController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents-api/src/Http/Controllers/MediaDocumentController.php) | `public function index(Request $request): JsonResponse`<br>`public function brochure(Request $request, GeneratePropertyBrochure $generate): JsonResponse`<br>`public function store(Request $request, CreateMediaDocument $create): JsonResponse`<br>`public function show(Request $request, MediaDocument $mediaDocument): JsonResponse`<br>`public function update(Request $request, MediaDocument $mediaDocument, UpdateMediaDocument $update): JsonResponse`<br>`public function rights(Request $request, MediaDocument $mediaDocument, UpdateMediaRights $update): JsonResponse`<br>`public function reorder(Request $request, MediaDocument $mediaDocument, ReorderMediaDocument $reorder): JsonResponse`<br>`public function retention(Request $request, MediaDocument $mediaDocument, SetMediaDocumentRetention $setRetention): JsonResponse`<br>`public function destroy(Request $request, MediaDocument $mediaDocument, DeleteMediaDocument $delete): Response` |
| [VirtualStagingController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents-api/src/Http/Controllers/VirtualStagingController.php) | `public function styles(): JsonResponse`<br>`public function upload(Request $r): JsonResponse`<br>`public function stage(Request $r, MediaDocument $mediaDocument): JsonResponse` |

**Observed route declarations:**

[modules/real-estate-media-and-documents-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/properties/{property}/home-reports')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [HomeReportController::class, 'index']);
Route::post('/', [HomeReportController::class, 'store']);
Route::prefix('api/v1/real-estate/media-and-documents')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::post('/templates/{documentTemplate}/envelopes', [DocumentWorkflowController::class, 'store'])->name('real-estate.documents.envelopes.store');
Route::get('/envelopes/{documentEnvelope}', [DocumentWorkflowController::class, 'show'])->name('real-estate.documents.envelopes.show');
Route::post('/envelopes/{documentEnvelope}/participants/{documentParticipant}/sign', [DocumentWorkflowController::class, 'sign'])->name('real-estate.documents.envelopes.sign');
Route::get('/staging/styles', [VirtualStagingController::class, 'styles']);
Route::post('/staging/upload', [VirtualStagingController::class, 'upload']);
Route::post('/staging/{mediaDocument}/stage', [VirtualStagingController::class, 'stage']);
Route::get('/', [MediaDocumentController::class, 'index'])->name('real-estate.media-documents.index');
Route::post('/', [MediaDocumentController::class, 'store'])->name('real-estate.media-documents.store');
Route::post('/brochure', [MediaDocumentController::class, 'brochure'])->name('real-estate.media-documents.brochure');
Route::get('/{mediaDocument}', [MediaDocumentController::class, 'show'])->name('real-estate.media-documents.show');
Route::patch('/{mediaDocument}/rights', [MediaDocumentController::class, 'rights'])->name('real-estate.media-documents.rights');
Route::patch('/{mediaDocument}/reorder', [MediaDocumentController::class, 'reorder'])->name('real-estate.media-documents.reorder');
Route::patch('/{mediaDocument}/retention', [MediaDocumentController::class, 'retention'])->name('real-estate.media-documents.retention');
Route::delete('/{mediaDocument}', [MediaDocumentController::class, 'destroy'])->name('real-estate.media-documents.destroy');
```
<!-- layer-implementation-plan:end -->
