# Accounting Migration Framework React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-migration-framework). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-migration-framework-react-native
**Matching core package:** module-accounting-accounting-migration-framework ([implementation](../core/accounting-migration-framework.md))
**Matching API package:** module-accounting-accounting-migration-framework-api ([contract](../api/accounting-migration-framework.md))

## Implementation plan

This adapter presents Accounting Migration Framework for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Migration Framework API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-migration-framework.md), and [API module](../api/accounting-migration-framework.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-migration-framework`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-migration-framework.md)) |
| Capability React Native module skeleton | [`module-accounting-migration-framework-react-native`](https://github.com/liberusoftware/module-accounting-migration-framework-react-native) (`@liberusoftware/module-accounting-migration-framework-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Source inventory** | Progressive mobile list/detail/sheet flow for `source inventory` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Mapping** | Progressive mobile list/detail/sheet flow for `mapping` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Dry run** | Progressive mobile list/detail/sheet flow for `dry run` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Transforms** | Progressive mobile list/detail/sheet flow for `transforms` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Validation** | Progressive mobile list/detail/sheet flow for `validation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Batches** | Progressive mobile list/detail/sheet flow for `batches` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Resume** | Progressive mobile list/detail/sheet flow for `resume` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Attachments** | Progressive mobile list/detail/sheet flow for `attachments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Errors** | Progressive mobile list/detail/sheet flow for `errors` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Counts** | Progressive mobile list/detail/sheet flow for `counts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reconciliation** | Progressive mobile list/detail/sheet flow for `reconciliation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
