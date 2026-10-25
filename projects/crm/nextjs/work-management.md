# Work Management: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-crm-work-management`.

**Proposed design identifier:** `module-crm-work-management-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/work-management.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-crm-work-management](../../../modules/source/liberusoftware--module-crm-work-management.md) |
| API | [liberusoftware/module-crm-work-management-api](../../../modules/source/liberusoftware--module-crm-work-management-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Cross-record task boards | A focused authorized view or workflow section for cross-record task boards; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Queues | A focused authorized view or workflow section for queues; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Recurring work | A focused authorized view or workflow section for recurring work; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Checklists | A focused authorized view or workflow section for checklists; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Approvals | A focused authorized view or workflow section for approvals; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Workload | A focused authorized view or workflow section for workload; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Dependencies | A focused authorized view or workflow section for dependencies; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Personal/team views | A focused authorized view or workflow section for personal/team views; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [AddChecklistItem.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/AddChecklistItem.php) | `public function execute(WorkItem $item, ?int $actorId, string $title): ChecklistItem` |
| [AddDependency.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/AddDependency.php) | `public function execute(WorkItem $item, WorkItem $dependsOn, ?int $actorId): Dependency` |
| [CompleteWorkItem.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/CompleteWorkItem.php) | `public function execute(WorkItem $item, ?int $actorId, ?int $expectedVersion = null): WorkItem` |
| [CreateWorkItem.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/CreateWorkItem.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): WorkItem` |
| [CreateWorkQueue.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/CreateWorkQueue.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): WorkQueue` |
| [ReviewApproval.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/ReviewApproval.php) | `public function request(WorkItem $item, ?int $actorId, ?string $comment = null): Approval`<br>`public function review(Approval $approval, int $actorId, string $status, ?string $comment = null): Approval` |
| [UpdateWorkItem.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/UpdateWorkItem.php) | `public function execute(WorkItem $item, ?int $actorId, array $attributes, ?int $expectedVersion = null): WorkItem` |
| [UpdateWorkQueue.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/UpdateWorkQueue.php) | `public function execute(WorkQueue $queue, ?int $actorId, array $attributes): WorkQueue` |
| [WorkAudit.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Services/WorkAudit.php) | `public function record(Model $item, ?int $actorId, string $event, array $details = []): void` |
| [WorkloadQuery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Services/WorkloadQuery.php) | `public function forTeam(int $teamId): Collection` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [Approval.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Models/Approval.php) | `work_item_id`, `team_id`, `requested_by`, `reviewed_by`, `status`, `comment`, `reviewed_at` |
| [ChecklistItem.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Models/ChecklistItem.php) | `work_item_id`, `team_id`, `actor_id`, `title`, `completed`, `position` |
| [Dependency.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Models/Dependency.php) | `work_item_id`, `depends_on_id`, `team_id` |
| [WorkItem.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Models/WorkItem.php) | `team_id`, `actor_id`, `assigned_to`, `queue_id`, `title`, `description`, `status`, `priority`, `subject_type`, `subject_id`, `due_at`, `recurrence`, `next_run_at`, `version`, `metadata` |
| [WorkQueue.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Models/WorkQueue.php) | `team_id`, `actor_id`, `name`, `description`, `status`, `rules` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/crm-work-management-api/routes/api.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/work-management')->group(function (): void {
Route::get('/', [WorkManagementController::class, 'index']);
Route::post('/', [WorkManagementController::class, 'store']);
Route::get('/workload', [WorkManagementController::class, 'workload']);
Route::get('/queues', [WorkManagementController::class, 'queues']);
Route::post('/queues', [WorkManagementController::class, 'storeQueue']);
Route::get('/{workItem}', [WorkManagementController::class, 'show']);
Route::patch('/{workItem}', [WorkManagementController::class, 'update']);
Route::post('/{workItem}/complete', [WorkManagementController::class, 'complete']);
Route::post('/{workItem}/checklist', [WorkManagementController::class, 'checklist']);
Route::post('/{workItem}/approvals', [WorkManagementController::class, 'requestApproval']);
Route::post('/{workItem}/dependencies', [WorkManagementController::class, 'dependency']);
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
