# DNS: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-control-panel-dns`.

**Proposed design identifier:** `module-control-panel-dns-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/dns.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-control-panel-dns](../../../modules/source/liberusoftware--module-control-panel-dns.md) |
| API | [liberusoftware/module-control-panel-dns-api](../../../modules/source/liberusoftware--module-control-panel-dns-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Zones | A focused authorized view or workflow section for zones; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Records | A focused authorized view or workflow section for records; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Templates | A focused authorized view or workflow section for templates; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| DNSSEC | A focused authorized view or workflow section for dnssec; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Validation | A focused authorized view or workflow section for validation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Providers | A focused authorized view or workflow section for providers; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Propagation checks | A focused authorized view or workflow section for propagation checks; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ListZones.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Queries/ListZones.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [ActivateZone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/ActivateZone.php) | `public function execute(Zone $zone): Zone` |
| [ArchiveZone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/ArchiveZone.php) | `public function execute(Zone $zone): Zone` |
| [CheckDnsPropagation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/CheckDnsPropagation.php) | `public function execute(array $attributes): array` |
| [CheckDnsResolution.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/CheckDnsResolution.php) | `public function execute(array $attributes): array` |
| [CreateRecord.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/CreateRecord.php) | `public function execute(array $a): Record` |
| [CreateZone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/CreateZone.php) | `public function execute(array $attributes): Zone` |
| [DeleteRecord.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/DeleteRecord.php) | `public function execute(Record $record): void` |
| [RecordDnsCheck.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/RecordDnsCheck.php) | `public function execute(array $a): DnsCheck` |
| [RegisterDnsFeature.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/RegisterDnsFeature.php) | `public function execute(array $a): Model` |
| [SuspendZone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/SuspendZone.php) | `public function execute(Zone $zone): Zone` |
| [UpdateRecord.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/UpdateRecord.php) | `public function execute(Record $record, array $attributes): Record` |
| [UpdateZone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/UpdateZone.php) | `public function execute(Zone $zone, array $attributes): Zone` |
| [ValidateRecord.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/ValidateRecord.php) | `public function execute(array $attributes): array` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [DnsCheck.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/DnsCheck.php) | `id`, `team_id`, `zone_id`, `kind`, `status`, `result`, `checked_at` |
| [DnsProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/DnsProvider.php) | `id`, `team_id`, `name`, `driver`, `endpoint`, `credentials`, `settings`, `active` |
| [DnsTemplate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/DnsTemplate.php) | `id`, `team_id`, `name`, `records`, `active` |
| [DnsValidation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/DnsValidation.php) | `id`, `team_id`, `zone_id`, `record_id`, `status`, `resolver`, `expected`, `observed`, `checked_at`, `details` |
| [DnssecKey.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/DnssecKey.php) | `id`, `team_id`, `zone_id`, `key_tag`, `algorithm`, `digest_type`, `digest`, `public_key`, `private_key`, `active`, `rotated_at` |
| [PropagationCheck.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/PropagationCheck.php) | `id`, `team_id`, `zone_id`, `record_id`, `status`, `nameservers`, `results`, `checked_at` |
| [Record.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/Record.php) | `zone_id`, `name`, `type`, `content`, `ttl`, `priority`, `metadata` |
| [Zone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/Zone.php) | `team_id`, `domain`, `status`, `provider`, `dnssec_enabled`, `metadata` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/control-panel-dns-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/dns')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/zones', [ZoneController::class, 'index'])->name('control-panel.dns.zones.index');
Route::post('/zones', [ZoneController::class, 'store'])->name('control-panel.dns.zones.store');
Route::patch('/zones/{zone}', [ZoneController::class, 'update'])->name('control-panel.dns.zones.update');
Route::post('/records', [ZoneController::class, 'record'])->name('control-panel.dns.records.store');
Route::post('/records/validate', [ZoneController::class, 'validateRecord'])->name('control-panel.dns.records.validate');
Route::patch('/records/{record}', [ZoneController::class, 'updateRecord'])->name('control-panel.dns.records.update');
Route::delete('/records/{record}', [ZoneController::class, 'deleteRecord'])->name('control-panel.dns.records.delete');
Route::post('/records/bulk', [ZoneController::class, 'bulkRecords'])->name('control-panel.dns.records.bulk');
Route::post('/checks', [ZoneController::class, 'check'])->name('control-panel.dns.checks.store');
Route::post('zones/{zone}/resolution-check', [ZoneController::class, 'resolutionCheck'])->name('control-panel.dns.zones.resolution-check');
Route::post('zones/{zone}/propagation-check', [ZoneController::class, 'propagationCheck'])->name('control-panel.dns.zones.propagation-check');
Route::post('/features', [ZoneController::class, 'feature'])->name('control-panel.dns.features.store');
Route::post('zones/{zone}/suspend', [ZoneController::class, 'suspend'])->name('control-panel.dns.zones.suspend');
Route::post('zones/{zone}/archive', [ZoneController::class, 'archive'])->name('control-panel.dns.zones.archive');
Route::get('zones/{zone}', [ZoneController::class, 'show'])->name('control-panel.dns.show');
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
