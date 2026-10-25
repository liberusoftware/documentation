# Security: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-control-panel-security`.

**Proposed design identifier:** `module-control-panel-security-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/security.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-control-panel-security](../../../modules/source/liberusoftware--module-control-panel-security.md) |
| API | [liberusoftware/module-control-panel-security-api](../../../modules/source/liberusoftware--module-control-panel-security-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Hardening | A focused authorized view or workflow section for hardening; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Patching | A focused authorized view or workflow section for patching; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| MFA/RBAC | A focused authorized view or workflow section for mfa/rbac; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Secrets | A focused authorized view or workflow section for secrets; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Malware | A focused authorized view or workflow section for malware; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Intrusion controls | A focused authorized view or workflow section for intrusion controls; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Vulnerability and compliance status | A focused authorized view or workflow section for vulnerability and compliance status; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ListFindings.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Queries/ListFindings.php) | `public function execute(string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [ConfigureFail2ban.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/ConfigureFail2ban.php) | `public function execute(array $attributes): Fail2banSetting` |
| [RecordFail2banBan.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/RecordFail2banBan.php) | `public function execute(Fail2banSetting $setting, array $attributes): Fail2banBan` |
| [RecordFinding.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/RecordFinding.php) | `public function execute(array $attributes): SecurityFinding` |
| [RecordSecurityResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/RecordSecurityResource.php) | `public function execute(string $modelClass, array $attributes): Model` |
| [ResolveSecurityFinding.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/ResolveSecurityFinding.php) | `public function execute(SecurityFinding $finding): SecurityFinding` |
| [StoreSecret.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/StoreSecret.php) | `public function execute(array $attributes): SecretRecord` |
| [UnbanFail2banBan.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/UnbanFail2banBan.php) | `public function execute(Fail2banBan $ban): Fail2banBan` |
| [UpdateSecurityFinding.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/UpdateSecurityFinding.php) | `public function execute(SecurityFinding $finding, array $attributes): SecurityFinding` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [ComplianceStatus.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/ComplianceStatus.php) | `team_id`, `framework`, `control`, `status`, `score`, `evidence`, `assessed_at`, `expires_at` |
| [Fail2banBan.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/Fail2banBan.php) | `team_id`, `jail_name`, `ip_address`, `banned_at`, `unbanned_at`, `ban_count`, `reason` |
| [Fail2banSetting.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/Fail2banSetting.php) | `team_id`, `jail_name`, `enabled`, `max_retry`, `find_time`, `ban_time`, `whitelist_ips` |
| [HardeningControl.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/HardeningControl.php) | `team_id`, `subject_type`, `subject_id`, `control`, `desired`, `observed`, `status`, `evidence`, `checked_at` |
| [IntrusionControl.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/IntrusionControl.php) | `team_id`, `subject_type`, `subject_id`, `kind`, `action`, `threshold`, `window_seconds`, `enabled`, `metadata` |
| [MalwareScan.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/MalwareScan.php) | `team_id`, `subject_type`, `subject_id`, `status`, `scanner`, `findings`, `started_at`, `finished_at` |
| [MfaRbacPolicy.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/MfaRbacPolicy.php) | `team_id`, `subject_type`, `subject_id`, `mfa_required`, `roles`, `permissions`, `status`, `metadata` |
| [PatchRecord.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/PatchRecord.php) | `team_id`, `subject_type`, `subject_id`, `package`, `current_version`, `target_version`, `severity`, `status`, `published_at`, `installed_at`, `metadata` |
| [SecretRecord.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/SecretRecord.php) | `team_id`, `name`, `purpose`, `value`, `version`, `status`, `expires_at`, `rotated_at` |
| [SecurityFinding.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/SecurityFinding.php) | `team_id`, `subject_type`, `subject_id`, `code`, `severity`, `status`, `summary`, `evidence` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/control-panel-security-api/routes/api.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/security')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [SecurityFindingController::class, 'index'])->name('control-panel.security.index');
Route::post('/', [SecurityFindingController::class, 'store'])->name('control-panel.security.store');
Route::post('{finding}/resolve', [SecurityFindingController::class, 'resolve'])->name('control-panel.security.resolve');
Route::patch('{finding}', [SecurityFindingController::class, 'update'])->name('control-panel.security.update');
Route::post('hardening', [SecurityFindingController::class, 'hardening'])->name('control-panel.security.hardening.store');
Route::post('patches', [SecurityFindingController::class, 'patch'])->name('control-panel.security.patches.store');
Route::post('mfa-rbac', [SecurityFindingController::class, 'policy'])->name('control-panel.security.mfa-rbac.store');
Route::get('mfa-rbac', [SecurityFindingController::class, 'policies'])->name('control-panel.security.mfa-rbac.index');
Route::post('secrets', [SecurityFindingController::class, 'secret'])->name('control-panel.security.secrets.store');
Route::get('secrets', [SecurityFindingController::class, 'secrets'])->name('control-panel.security.secrets.index');
Route::post('malware-scans', [SecurityFindingController::class, 'malware'])->name('control-panel.security.malware.store');
Route::get('malware-scans', [SecurityFindingController::class, 'malwareScans'])->name('control-panel.security.malware.index');
Route::post('intrusion-controls', [SecurityFindingController::class, 'intrusion'])->name('control-panel.security.intrusion.store');
Route::get('intrusion-controls', [SecurityFindingController::class, 'intrusionControls'])->name('control-panel.security.intrusion.index');
Route::get('patches', [SecurityFindingController::class, 'patches'])->name('control-panel.security.patches.index');
Route::post('fail2ban', [SecurityFindingController::class, 'fail2ban'])->name('control-panel.security.fail2ban.store');
Route::get('fail2ban/{jail}/bans', [SecurityFindingController::class, 'listFail2banBans'])->name('control-panel.security.fail2ban.bans.index');
Route::post('fail2ban/{jail}/bans', [SecurityFindingController::class, 'fail2banBans'])->name('control-panel.security.fail2ban.bans.store');
Route::post('fail2ban/bans/{ban}/unban', [SecurityFindingController::class, 'unbanFail2ban'])->name('control-panel.security.fail2ban.bans.unban');
Route::post('compliance', [SecurityFindingController::class, 'compliance'])->name('control-panel.security.compliance.store');
Route::get('{finding}', [SecurityFindingController::class, 'show'])->name('control-panel.security.show');
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
