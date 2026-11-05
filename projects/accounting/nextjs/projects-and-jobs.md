# Projects and Jobs: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-projects-and-jobs`.

**Proposed design identifier:** `module-accounting-projects-and-jobs-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/projects-and-jobs.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-projects-and-jobs](../../../modules/source/liberusoftware--module-accounting-projects-and-jobs.md) |
| API | [liberusoftware/module-accounting-projects-and-jobs-api](../../../modules/source/liberusoftware--module-accounting-projects-and-jobs-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Customers | A focused authorized view or workflow section for customers; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Project/job hierarchy | A focused authorized view or workflow section for project/job hierarchy; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Status | A focused authorized view or workflow section for status; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Dates | A focused authorized view or workflow section for dates; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Managers | A focused authorized view or workflow section for managers; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Budgets | A focused authorized view or workflow section for budgets; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Dimensions | A focused authorized view or workflow section for dimensions; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Source links | A focused authorized view or workflow section for source links; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Lifecycle | A focused authorized view or workflow section for lifecycle; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CreateProjectJob.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs/src/Actions/CreateProjectJob.php) | `public function handle(array $attributes): ProjectJob` |
| [TransitionProject.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs/src/Actions/TransitionProject.php) | `public function handle(ProjectJob $project, ProjectStatus $status): ProjectJob` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [ProjectCustomer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs/src/Models/ProjectCustomer.php) | `team_id`, `customer_ref`, `name`, `status`, `metadata` |
| [ProjectJob.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs/src/Models/ProjectJob.php) | `team_id`, `customer_id`, `parent_id`, `name`, `code`, `description`, `start_date`, `end_date`, `status`, `manager_ref`, `budget_amount`, `budget_currency`, `dimensions`, `source_links`, `metadata` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-projects-and-jobs-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/projects-and-jobs')->group(function (): void {
Route::middleware('ability:accounting.projects-and-jobs.read')->group(function (): void {
Route::get('/', [ProjectsAndJobsController::class, 'index']);
Route::get('/{project}', [ProjectsAndJobsController::class, 'show']);
Route::middleware('ability:accounting.projects-and-jobs.write')->group(function (): void {
Route::post('/', [ProjectsAndJobsController::class, 'store']);
Route::post('/{project}/transition', [ProjectsAndJobsController::class, 'transition']);
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
