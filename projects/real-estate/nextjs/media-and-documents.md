# Media and Documents: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/real-estate-media-and-documents`.

**Proposed design identifier:** `module-real-estate-media-and-documents-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/media-and-documents.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/real-estate-media-and-documents](../../../modules/source/liberusoftware--real-estate-media-and-documents.md) |
| API | [liberusoftware/real-estate-media-and-documents-api](../../../modules/source/liberusoftware--real-estate-media-and-documents-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Photos | A focused authorized view or workflow section for photos; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Floorplans | A focused authorized view or workflow section for floorplans; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Video | A focused authorized view or workflow section for video; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Certificates | A focused authorized view or workflow section for certificates; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Rights | A focused authorized view or workflow section for rights; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Ordering | A focused authorized view or workflow section for ordering; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Brochures | A focused authorized view or workflow section for brochures; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Retention | A focused authorized view or workflow section for retention; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

No concrete action/query signatures were established in the indexed source roots for this design. Use its source reference and owning application routes/contracts to resolve the integration, rather than inventing create/update/delete operations from the module name.

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [DocumentCategory.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentCategory.php) | No literal fillable array detected; inspect the model and API schema. |
| [DocumentEnvelope.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentEnvelope.php) | No literal fillable array detected; inspect the model and API schema. |
| [DocumentEnvelopeSignature.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentEnvelopeSignature.php) | No literal fillable array detected; inspect the model and API schema. |
| [DocumentParticipant.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentParticipant.php) | No literal fillable array detected; inspect the model and API schema. |
| [DocumentSignature.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentSignature.php) | No literal fillable array detected; inspect the model and API schema. |
| [DocumentTemplate.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentTemplate.php) | No literal fillable array detected; inspect the model and API schema. |
| [DocumentVersion.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/DocumentVersion.php) | No literal fillable array detected; inspect the model and API schema. |
| [HomeReport.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/HomeReport.php) | No literal fillable array detected; inspect the model and API schema. |
| [MediaDocument.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents/src/Models/MediaDocument.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/real-estate-media-and-documents-api/routes/api.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-media-and-documents-api/routes/api.php)

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

## Server/client and React reuse

Keep API credentials and session forwarding in server-only exports. A Server Component may load authorized serializable data and compose a Client Component for interaction. Put ordinary event callbacks inside the client boundary; server-to-client props must follow the framework serialization/action rules.

Share framework-independent React cards, tables, labels, formatting and field primitives with Inertia. Keep `next/link`, Next.js navigation, server actions and cache invalidation in this adapter, and Inertia visits, page props and redirects in its wrapper. Reuse domain/API DTOs without importing PHP models or another application's private frontend state.

## State, failures and verification

| Situation | User-facing behavior and integration requirement |
| --- | --- |
| Loading or empty authorized query | Accessible progress/empty copy; preserve filters and avoid displaying stale records from another scope |
| Expired session or denied permission | Reauthenticate or show a scoped denial; discard protected cached data and do not retry as a broader service identity |
| Invalid command input | Preserve safe draft values, announce field errors and use the authoritative API validation outcome |
| Stale record / concurrent change | Reload/review the current version; do not overwrite silently or invent an ETag contract the API does not support |
| Timeout after a write | Query the operation/current record when supported before retrying; an idempotency key works only if the owning API actually stores/enforces it |
| Long-running or partly failed operation | Show a durable operation reference, progress, last error and a permitted retry/recovery action |

Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware caching policy exists. Refresh affected read models after confirmed mutations; pending transport acceptance is not a completed business transition. Recheck access for evidence/export downloads.

Verify the actual supported query/command journeys, invalid and denied paths, tenant switching, stale state, retry recovery, keyboard/focus behavior and secret exclusion from browser bundles. Build/test the packed adapter in a clean consuming Next.js application using its declared versions and API contract. No npm package or application suite was executed by this plan generator.

See the [Next.js standard](../../../standards/NEXTJS.md), [npm lifecycle guide](../../../guides/NPM.md), [API architecture](../../../architecture/API.md), and [shared ownership guide](../../../architecture/SHARED-MODULES.md).
