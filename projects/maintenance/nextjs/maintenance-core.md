# Maintenance Core: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-maintenance-maintenance-core`.

**Proposed design identifier:** `module-maintenance-maintenance-core-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/maintenance-core.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **3 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-maintenance-maintenance-core](../../../modules/source/liberusoftware--module-maintenance-maintenance-core.md) |
| API | [liberusoftware/module-maintenance-core-api](../../../modules/source/liberusoftware--module-maintenance-core-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Organizations | A focused authorized view or workflow section for organizations; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Service settings | A focused authorized view or workflow section for service settings; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Statuses | A focused authorized view or workflow section for statuses; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Numbering | A focused authorized view or workflow section for numbering; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Priorities | A focused authorized view or workflow section for priorities; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Shared events | A focused authorized view or workflow section for shared events; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [ConfigureNumbering.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/ConfigureNumbering.php) | `public function execute(int $teamId, string $documentType, string $prefix, int $padding = 6): NumberingSequence` |
| [CreateOrganization.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/CreateOrganization.php) | `public function execute(int $teamId, string $name, string $code, ?string $description = null): Organization` |
| [CreatePriority.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/CreatePriority.php) | `public function execute(int $teamId, array $attributes): Priority` |
| [CreateStatus.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/CreateStatus.php) | `public function execute(int $teamId, array $attributes): Status` |
| [DeleteOrganization.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/DeleteOrganization.php) | `public function execute(Organization $organization): void` |
| [DeletePriority.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/DeletePriority.php) | `public function execute(Priority $priority): void` |
| [DeleteServiceSetting.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/DeleteServiceSetting.php) | `public function execute(ServiceSetting $setting): void` |
| [DeleteStatus.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/DeleteStatus.php) | `public function execute(Status $status): void` |
| [IssueNumber.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/IssueNumber.php) | `public function execute(int $teamId, string $documentType): string` |
| [SetServiceSetting.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/SetServiceSetting.php) | `public function execute(int $teamId, string $key, ?string $value, bool $encrypted = false): ServiceSetting` |
| [UpdateOrganization.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/UpdateOrganization.php) | `public function execute(Organization $organization, array $attributes): Organization` |
| [UpdatePriority.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/UpdatePriority.php) | `public function execute(Priority $priority, array $attributes): Priority` |
| [UpdateStatus.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/UpdateStatus.php) | `public function execute(Status $status, array $attributes): Status` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [NumberingSequence.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Models/NumberingSequence.php) | `team_id`, `document_type`, `prefix`, `next_number`, `padding` |
| [Organization.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Models/Organization.php) | `team_id`, `name`, `code`, `description`, `state` |
| [Priority.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Models/Priority.php) | `team_id`, `name`, `code`, `color`, `sort_order`, `is_default`, `is_active` |
| [ServiceSetting.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Models/ServiceSetting.php) | `team_id`, `key`, `value`, `is_encrypted` |
| [Status.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Models/Status.php) | `team_id`, `name`, `code`, `color`, `sort_order`, `is_default`, `is_active` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/module-maintenance-core-api/routes/api.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-api/routes/api.php)

```php
Route::middleware('api')
Route::middleware('auth:sanctum')->group(function (): void {
Route::get('organizations', [OrganizationController::class, 'index'])->name('organizations.index');
Route::post('organizations', [OrganizationController::class, 'store'])->name('organizations.store');
Route::get('organizations/{organization}', [OrganizationController::class, 'show'])->name('organizations.show');
Route::patch('organizations/{organization}', [OrganizationController::class, 'update'])->name('organizations.update');
Route::delete('organizations/{organization}', [OrganizationController::class, 'destroy'])->name('organizations.destroy');
Route::get('statuses', [StatusController::class, 'index'])->name('statuses.index');
Route::post('statuses', [StatusController::class, 'store'])->name('statuses.store');
Route::patch('statuses/{status}', [StatusController::class, 'update'])->name('statuses.update');
Route::delete('statuses/{status}', [StatusController::class, 'destroy'])->name('statuses.destroy');
Route::get('priorities', [PriorityController::class, 'index'])->name('priorities.index');
Route::post('priorities', [PriorityController::class, 'store'])->name('priorities.store');
Route::patch('priorities/{priority}', [PriorityController::class, 'update'])->name('priorities.update');
Route::delete('priorities/{priority}', [PriorityController::class, 'destroy'])->name('priorities.destroy');
Route::get('settings', [ServiceSettingController::class, 'index'])->name('settings.index');
Route::post('settings', [ServiceSettingController::class, 'store'])->name('settings.store');
Route::post('numbering/configure', [NumberingController::class, 'configure'])->name('numbering.configure');
Route::post('numbering/issue', [NumberingController::class, 'issue'])->name('numbering.issue');
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
