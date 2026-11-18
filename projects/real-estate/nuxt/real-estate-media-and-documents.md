# Real Estate: Real Estate Media And Documents Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-media-and-documents). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-real-estate-real-estate-media-and-documents-nuxt`
**Matching domain module:** `real-estate-media-and-documents`
**Application:** Real Estate
**Source feature:** [Real Estate Media And Documents](../features/real-estate-media-and-documents.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/real-estate-media-and-documents.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `real-estate-media-and-documents` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Photos:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Floorplans:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Video:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Certificates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rights:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Ordering:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Brochures:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Retention:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-real-estate-real-estate-media-and-documents-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `photos`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `floorplans`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `video`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `certificates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rights`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `ordering`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `brochures`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `retention`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `real-estate-media-and-documents` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-real-estate-nuxt-vue`](https://github.com/liberusoftware/project-real-estate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/real-estate-media-and-documents.md)) |
| Capability Nuxt module skeleton | [`module-real-estate-media-and-documents-nuxt`](https://github.com/liberusoftware/module-real-estate-media-and-documents-nuxt) (`@liberusoftware/module-real-estate-media-and-documents-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Photos** | Expose composable and Vue 3 component for `photos` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-media-and-documents.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Floorplans** | Expose composable and Vue 3 component for `floorplans` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-media-and-documents.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Video** | Expose composable and Vue 3 component for `video` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-media-and-documents.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Certificates** | Expose composable and Vue 3 component for `certificates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-media-and-documents.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Rights** | Expose composable and Vue 3 component for `rights` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-media-and-documents.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Ordering** | Expose composable and Vue 3 component for `ordering` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-media-and-documents.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Brochures** | Expose composable and Vue 3 component for `brochures` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-media-and-documents.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Retention** | Expose composable and Vue 3 component for `retention` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-media-and-documents.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |

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
