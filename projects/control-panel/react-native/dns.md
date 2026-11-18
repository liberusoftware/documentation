# Dns React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#dns). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-control-panel-dns-react-native
**Matching core package:** module-control-panel-dns ([implementation](../core/dns.md))
**Matching API package:** module-control-panel-dns-api ([contract](../api/dns.md))

## Implementation plan

This adapter presents Dns for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Dns API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/dns.md), and [API module](../api/dns.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `dns`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-control-panel-mobile-react`](https://github.com/liberusoftware/project-control-panel-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/dns.md)) |
| Capability React Native module skeleton | [`module-control-panel-dns-react-native`](https://github.com/liberusoftware/module-control-panel-dns-react-native) (`@liberusoftware/module-control-panel-dns-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Zones** | Progressive mobile list/detail/sheet flow for `zones` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Records** | Progressive mobile list/detail/sheet flow for `records` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Templates** | Progressive mobile list/detail/sheet flow for `templates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **DNSSEC** | Progressive mobile list/detail/sheet flow for `dnssec` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Validation** | Progressive mobile list/detail/sheet flow for `validation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Providers** | Progressive mobile list/detail/sheet flow for `providers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Propagation checks** | Progressive mobile list/detail/sheet flow for `propagation checks` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListZones.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Queries/ListZones.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateZone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/ActivateZone.php) | `public function execute(Zone $zone): Zone` |
| [ArchiveZone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/ArchiveZone.php) | `public function execute(Zone $zone): Zone` |
| [CheckDnsPropagation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/CheckDnsPropagation.php) | `public function __construct(private readonly DnsResolver $resolver)`<br>`public function execute(array $attributes): array` |
| [CheckDnsResolution.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/CheckDnsResolution.php) | `public function __construct(private readonly DnsResolver $resolver)`<br>`public function execute(array $attributes): array` |
| [CreateRecord.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/CreateRecord.php) | `public function execute(array $a): Record` |
| [CreateZone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/CreateZone.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(array $attributes): Zone` |
| [DeleteRecord.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/DeleteRecord.php) | `public function execute(Record $record): void` |
| [RecordDnsCheck.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/RecordDnsCheck.php) | `public function execute(array $a): DnsCheck` |
| [RegisterDnsFeature.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/RegisterDnsFeature.php) | `public function execute(array $a): Model` |
| [SuspendZone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Actions/SuspendZone.php) | `public function execute(Zone $zone): Zone` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DnsCheck.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/DnsCheck.php) | `id`, `team_id`, `zone_id`, `kind`, `status`, `result`, `checked_at` |
| [DnsProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/DnsProvider.php) | `id`, `team_id`, `name`, `driver`, `endpoint`, `credentials`, `settings`, `active` |
| [DnsTemplate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/DnsTemplate.php) | `id`, `team_id`, `name`, `records`, `active` |
| [DnsValidation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/DnsValidation.php) | `id`, `team_id`, `zone_id`, `record_id`, `status`, `resolver`, `expected`, `observed`, `checked_at`, `details` |
| [DnssecKey.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/DnssecKey.php) | `id`, `team_id`, `zone_id`, `key_tag`, `algorithm`, `digest_type`, `digest`, `public_key`, `private_key`, `active`, `rotated_at` |
| [PropagationCheck.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/PropagationCheck.php) | `id`, `team_id`, `zone_id`, `record_id`, `status`, `nameservers`, `results`, `checked_at` |
| [Record.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/Record.php) | `zone_id`, `name`, `type`, `content`, `ttl`, `priority`, `metadata` |
| [Zone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns/src/Models/Zone.php) | `team_id`, `domain`, `status`, `provider`, `dnssec_enabled`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ZoneController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-api/src/Http/Controllers/ZoneController.php) | `public function index(Request $request, ListZones $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function store(Request $request, CreateZone $create): JsonResponse`<br>`public function update(Request $request, string $id, UpdateZone $update): JsonResponse`<br>`public function record(Request $request, CreateRecord $create): JsonResponse`<br>`public function validateRecord(Request $request, ValidateRecord $validate): JsonResponse`<br>`public function updateRecord(Request $request, string $id, UpdateRecord $update): JsonResponse`<br>`public function deleteRecord(Request $request, string $id, DeleteRecord $delete): JsonResponse`<br>`public function bulkRecords(Request $request, CreateRecord $create): JsonResponse`<br>`public function check(Request $request, RecordDnsCheck $record): JsonResponse`<br>`public function resolutionCheck(Request $request, string $zone, CheckDnsResolution $check): JsonResponse`<br>`public function propagationCheck(Request $request, string $zone, CheckDnsPropagation $check): JsonResponse`<br>`public function feature(Request $request, RegisterDnsFeature $register): JsonResponse`<br>`public function suspend(Request $request, string $zone, SuspendZone $suspend): JsonResponse`<br>`public function archive(Request $request, string $zone, ArchiveZone $archive): JsonResponse` |

**Observed route declarations:**

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
<!-- layer-implementation-plan:end -->
