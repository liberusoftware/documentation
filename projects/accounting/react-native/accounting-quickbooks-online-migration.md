# Accounting Quickbooks Online Migration React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-quickbooks-online-migration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-quickbooks-online-migration-react-native
**Matching core package:** module-accounting-accounting-quickbooks-online-migration ([implementation](../core/accounting-quickbooks-online-migration.md))
**Matching API package:** module-accounting-accounting-quickbooks-online-migration-api ([contract](../api/accounting-quickbooks-online-migration.md))

## Implementation plan

This adapter presents Accounting Quickbooks Online Migration for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Quickbooks Online Migration API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-quickbooks-online-migration.md), and [API module](../api/accounting-quickbooks-online-migration.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-quickbooks-online-migration`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-quickbooks-online-migration.md)) |
| Capability React Native module skeleton | [`module-accounting-quickbooks-online-migration-react-native`](https://github.com/liberusoftware/module-accounting-quickbooks-online-migration-react-native) (`@liberusoftware/module-accounting-quickbooks-online-migration-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Chart** | Progressive mobile list/detail/sheet flow for `chart` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Classes/locations** | Progressive mobile list/detail/sheet flow for `classes/locations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Contacts** | Progressive mobile list/detail/sheet flow for `contacts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Items** | Progressive mobile list/detail/sheet flow for `items` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Invoices/bills/credits/payments** | Progressive mobile list/detail/sheet flow for `invoices/bills/credits/payments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Journals** | Progressive mobile list/detail/sheet flow for `journals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Bank data** | Progressive mobile list/detail/sheet flow for `bank data` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Projects** | Progressive mobile list/detail/sheet flow for `projects` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tax** | Progressive mobile list/detail/sheet flow for `tax` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Attachments** | Progressive mobile list/detail/sheet flow for `attachments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Source IDs** | Progressive mobile list/detail/sheet flow for `source ids` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateMigrationRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Actions/CreateMigrationRun.php) | `public function handle(?int $connectionId, array $metadata = []): QboMigrationRun` |
| [ImportMigrationRecords.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Actions/ImportMigrationRecords.php) | `public function handle(QboMigrationRun $run, array $records): QboMigrationRun` |
| [ReconcileMigration.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Actions/ReconcileMigration.php) | `public function handle(QboMigrationRun $run): QboMigrationRun` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [QboMigrationConnection.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Models/QboMigrationConnection.php) | `team_id`, `realm_id`, `access_token`, `refresh_token`, `token_expires_at`, `status`, `last_synced_at` |
| [QboMigrationRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Models/QboMigrationRecord.php) | `run_id`, `entity_type`, `source_id`, `status`, `payload`, `payload_hash`, `error_message`, `metadata` |
| [QboMigrationRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Models/QboMigrationRun.php) | `connection_id`, `status`, `total_records`, `imported_records`, `failed_records`, `errors`, `metadata`, `started_at`, `finished_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [QboMigrationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration-api/src/Http/Controllers/QboMigrationController.php) | `public function index(): mixed`<br>`public function store(Request $request, CreateMigrationRun $create, ImportMigrationRecords $import): QboMigrationRun`<br>`public function show(QboMigrationRun $run): QboMigrationRun`<br>`public function reconcile(QboMigrationRun $run, ReconcileMigration $action): QboMigrationRun` |

**Observed route declarations:**

[modules/accounting-quickbooks-online-migration-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/quickbooks-online-migration')->group(function (): void {
Route::get('/', [QboMigrationController::class, 'index']);
Route::post('/', [QboMigrationController::class, 'store']);
Route::get('/{run}', [QboMigrationController::class, 'show']);
Route::post('/{run}/reconcile', [QboMigrationController::class, 'reconcile']);
```
<!-- layer-implementation-plan:end -->
