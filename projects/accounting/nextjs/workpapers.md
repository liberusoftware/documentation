# Workpapers: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-workpapers`.

**Proposed design identifier:** `module-accounting-workpapers-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/workpapers.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-workpapers](../../../modules/source/liberusoftware--module-accounting-workpapers.md) |
| API | [liberusoftware/module-accounting-workpapers-api](../../../modules/source/liberusoftware--module-accounting-workpapers-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Lead schedules | A focused authorized view or workflow section for lead schedules; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| References | A focused authorized view or workflow section for references; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Attachments | A focused authorized view or workflow section for attachments; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Procedures | A focused authorized view or workflow section for procedures; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Conclusions | A focused authorized view or workflow section for conclusions; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Preparer/reviewer | A focused authorized view or workflow section for preparer/reviewer; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Rollover | A focused authorized view or workflow section for rollover; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Export | A focused authorized view or workflow section for export; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [AddWorkpaperAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/AddWorkpaperAttachment.php) | `public function handle(Workpaper $workpaper, array $attributes): WorkpaperAttachment` |
| [AddWorkpaperProcedure.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/AddWorkpaperProcedure.php) | `public function handle(Workpaper $workpaper, array $attributes): WorkpaperProcedure` |
| [AddWorkpaperReference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/AddWorkpaperReference.php) | `public function handle(Workpaper $workpaper, array $attributes): WorkpaperReference` |
| [AssignWorkpaperReviewer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/AssignWorkpaperReviewer.php) | `public function handle(Workpaper $workpaper, int $reviewerId): Workpaper` |
| [ConcludeWorkpaper.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/ConcludeWorkpaper.php) | `public function handle(Workpaper $workpaper, string $conclusion): Workpaper` |
| [CreateWorkpaper.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/CreateWorkpaper.php) | `public function handle(array $attributes): Workpaper` |
| [RequestWorkpaperExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/RequestWorkpaperExport.php) | `public function handle(Workpaper $workpaper, string $format): WorkpaperExport` |
| [RolloverWorkpaper.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/RolloverWorkpaper.php) | `public function handle(Workpaper $source, array $attributes = []): Workpaper` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [Workpaper.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/Workpaper.php) | `team_id`, `title`, `reference`, `status`, `period_start`, `period_end`, `preparer_id`, `reviewer_id`, `conclusion`, `metadata` |
| [WorkpaperAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/WorkpaperAttachment.php) | `workpaper_id`, `name`, `disk`, `path`, `mime_type`, `size` |
| [WorkpaperExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/WorkpaperExport.php) | `workpaper_id`, `format`, `status`, `path`, `error` |
| [WorkpaperProcedure.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/WorkpaperProcedure.php) | `workpaper_id`, `description`, `status`, `performed_by`, `performed_at`, `evidence` |
| [WorkpaperReference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/WorkpaperReference.php) | `workpaper_id`, `label`, `target_type`, `target_id`, `notes` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-workpapers-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/workpapers')->middleware('auth:sanctum')->group(function (): void {
Route::get('/', [WorkpapersController::class, 'index'])->middleware('ability:accounting.workpapers.read');
Route::post('/', [WorkpapersController::class, 'store'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/references', [WorkpapersController::class, 'reference'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/attachments', [WorkpapersController::class, 'attachment'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/procedures', [WorkpapersController::class, 'procedure'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/reviewer', [WorkpapersController::class, 'reviewer'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/conclude', [WorkpapersController::class, 'conclude'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/rollover', [WorkpapersController::class, 'rollover'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/exports', [WorkpapersController::class, 'export'])->middleware('ability:accounting.workpapers.write');
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
