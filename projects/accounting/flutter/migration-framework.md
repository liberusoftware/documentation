# Migration Framework Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#migration-framework). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-migration-framework-flutter
**Matching core package:** module-accounting-migration-framework ([implementation](../core/migration-framework.md))
**Matching API package:** module-accounting-migration-framework-api ([contract](../api/migration-framework.md))

## Implementation plan

This adapter presents Migration Framework for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Migration Framework API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/migration-framework.md), and [API module](../api/migration-framework.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `migration-framework`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-migration-framework-flutter`](https://github.com/liberusoftware/module-accounting-migration-framework-flutter) (`module_accounting_migration_framework_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-migration-framework-dart-mobile`](https://github.com/liberusoftware/module-accounting-migration-framework-dart-mobile) (`module_accounting_migration_framework_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-migration-framework-dart-desktop`](https://github.com/liberusoftware/module-accounting-migration-framework-dart-desktop) (`module_accounting_migration_framework_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/migration-framework.md) · [Core plan](../core/migration-framework.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Source inventory** | Adaptive mobile cards/sheets for `source inventory` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `source inventory` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Mapping** | Adaptive mobile cards/sheets for `mapping` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `mapping` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Dry run** | Adaptive mobile cards/sheets for `dry run` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `dry run` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Transforms** | Adaptive mobile cards/sheets for `transforms` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `transforms` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Validation** | Adaptive mobile cards/sheets for `validation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `validation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Batches** | Adaptive mobile cards/sheets for `batches` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `batches` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Resume** | Adaptive mobile cards/sheets for `resume` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `resume` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Attachments** | Adaptive mobile cards/sheets for `attachments` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `attachments` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Errors** | Adaptive mobile cards/sheets for `errors` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `errors` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Counts** | Adaptive mobile cards/sheets for `counts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `counts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Reconciliation** | Adaptive mobile cards/sheets for `reconciliation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `reconciliation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [MigrationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Queries/MigrationQuery.php) | `public function sources(?int $teamId = null, int $perPage = 25): LengthAwarePaginator`<br>`public function batches(?int $teamId = null, int $perPage = 25): LengthAwarePaginator`<br>`public function counts(MigrationBatch $batch): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Actions/CreateBatch.php) | `public function handle(MigrationSource $source, MigrationMapping $mapping, array $attributes, array $rows = []): MigrationBatch` |
| [CreateMapping.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Actions/CreateMapping.php) | `public function handle(MigrationSource $source, array $attributes): MigrationMapping` |
| [ReconcileBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Actions/ReconcileBatch.php) | `public function handle(MigrationBatch $batch, array $attributes = []): MigrationReconciliation` |
| [RegisterSource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Actions/RegisterSource.php) | `public function handle(array $attributes): MigrationSource` |
| [RunBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Actions/RunBatch.php) | `public function handle(MigrationBatch $batch, bool $dryRun = false, int $limit = 100): MigrationBatch` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MigrationAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationAttachment.php) | `batch_id`, `file_ref`, `name`, `mime_type`, `size_bytes`, `checksum`, `metadata` |
| [MigrationBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationBatch.php) | `team_id`, `batch_ref`, `source_id`, `mapping_id`, `status`, `dry_run`, `resume_token`, `total_count`, `processed_count`, `success_count`, `error_count`, `skipped_count`, `started_at`, `completed_at`, `paused_at`, `failure_message`, `metadata` |
| [MigrationMapping.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationMapping.php) | `source_id`, `mapping_ref`, `entity_type`, `field_map`, `transforms`, `validation_rules`, `version`, `active`, `metadata` |
| [MigrationReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationReconciliation.php) | `batch_id`, `source_count`, `imported_count`, `failed_count`, `source_total`, `destination_total`, `variance`, `status`, `notes`, `metadata` |
| [MigrationRow.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationRow.php) | `batch_id`, `row_ref`, `source_key`, `destination_key`, `payload`, `transformed_payload`, `status`, `error_code`, `error_message`, `attempts`, `processed_at`, `metadata` |
| [MigrationSource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationSource.php) | `team_id`, `source_ref`, `provider`, `source_type`, `name`, `record_count`, `checksum`, `status`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MigrationFrameworkController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework-api/src/Http/Controllers/MigrationFrameworkController.php) | `public function sources(Request $request, MigrationQuery $query): mixed`<br>`public function source(Request $request, RegisterSource $action): JsonResponse`<br>`public function mapping(Request $request, MigrationSource $source, CreateMapping $action): JsonResponse`<br>`public function batches(Request $request, MigrationQuery $query): mixed`<br>`public function batch(Request $request, MigrationSource $source, CreateBatch $action): MigrationBatchResource`<br>`public function dryRun(MigrationBatch $batch, RunBatch $action): MigrationBatchResource`<br>`public function resume(MigrationBatch $batch, RunBatch $action): MigrationBatchResource`<br>`public function reconcile(Request $request, MigrationBatch $batch, ReconcileBatch $action): JsonResponse`<br>`public function counts(MigrationBatch $batch, MigrationQuery $query): array` |

**Observed route declarations:**

[modules/accounting-migration-framework-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/migration-framework')->group(function (): void {
Route::get('/sources', [MigrationFrameworkController::class, 'sources'])->name('accounting.migration-framework.sources');
Route::post('/sources', [MigrationFrameworkController::class, 'source'])->name('accounting.migration-framework.source');
Route::post('/sources/{source}/mappings', [MigrationFrameworkController::class, 'mapping'])->name('accounting.migration-framework.mapping');
Route::get('/batches', [MigrationFrameworkController::class, 'batches'])->name('accounting.migration-framework.batches');
Route::post('/sources/{source}/batches', [MigrationFrameworkController::class, 'batch'])->name('accounting.migration-framework.batch');
Route::post('/batches/{batch}/dry-run', [MigrationFrameworkController::class, 'dryRun'])->name('accounting.migration-framework.dry-run');
Route::post('/batches/{batch}/resume', [MigrationFrameworkController::class, 'resume'])->name('accounting.migration-framework.resume');
Route::post('/batches/{batch}/reconcile', [MigrationFrameworkController::class, 'reconcile'])->name('accounting.migration-framework.reconcile');
Route::get('/batches/{batch}/counts', [MigrationFrameworkController::class, 'counts'])->name('accounting.migration-framework.counts');
```
<!-- layer-implementation-plan:end -->
