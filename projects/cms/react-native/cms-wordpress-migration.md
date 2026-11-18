# Cms Wordpress Migration React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-wordpress-migration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-cms-wordpress-migration-react-native
**Matching core package:** module-cms-cms-wordpress-migration ([implementation](../core/cms-wordpress-migration.md))
**Matching API package:** module-cms-cms-wordpress-migration-api ([contract](../api/cms-wordpress-migration.md))

## Implementation plan

This adapter presents Cms Wordpress Migration for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Cms Wordpress Migration API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/cms-wordpress-migration.md), and [API module](../api/cms-wordpress-migration.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `cms-wordpress-migration`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-cms-mobile-react`](https://github.com/liberusoftware/project-cms-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/cms-wordpress-migration.md)) |
| Capability React Native module skeleton | [`module-cms-wordpress-migration-react-native`](https://github.com/liberusoftware/module-cms-wordpress-migration-react-native) (`@liberusoftware/module-cms-wordpress-migration-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Posts/pages/custom types** | Progressive mobile list/detail/sheet flow for `posts/pages/custom types` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Taxonomies** | Progressive mobile list/detail/sheet flow for `taxonomies` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Metadata** | Progressive mobile list/detail/sheet flow for `metadata` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Users/authors** | Progressive mobile list/detail/sheet flow for `users/authors` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Comments** | Progressive mobile list/detail/sheet flow for `comments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Media** | Progressive mobile list/detail/sheet flow for `media` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Menus** | Progressive mobile list/detail/sheet flow for `menus` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Redirects** | Progressive mobile list/detail/sheet flow for `redirects` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Source identifiers** | Progressive mobile list/detail/sheet flow for `source identifiers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [WordPressMigrationQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-wordpress-migration/src/Queries/WordPressMigrationQuery.php) | `public function __construct(private TenantContextInterface $tenant)`<br>`public function migrations(int $perPage = 15, ?int $teamId = null): LengthAwarePaginator`<br>`public function migration(int\|string $id, ?int $teamId = null): ?WordPressMigration`<br>`public function migrationByPublicId(string $publicId, ?int $teamId = null): ?WordPressMigration`<br>`public function records(WordPressMigration $migration, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [WordPressImporterInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-wordpress-migration/src/Contracts/WordPressImporterInterface.php) | `public function records(WordPressMigration $migration): iterable` |
| [WordPressMigrationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-wordpress-migration/src/Services/WordPressMigrationService.php) | `public function start(?string $sourceUrl = null, array $options = [], ?int $teamId = null): WordPressMigration`<br>`public function addRecord(WordPressMigration $migration, string $recordType, string $sourceId, array $payload = [], array $sourceIdentifiers = [], ?string $sourceParentId = null): WordPressMigrationRecord`<br>`public function processRecord(WordPressMigrationRecord $record, bool $success = true, ?string $failureReason = null): WordPressMigrationRecord`<br>`public function complete(WordPressMigration $migration): WordPressMigration`<br>`public function fail(WordPressMigration $migration, string $reason): WordPressMigration` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WordPressMigration.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-wordpress-migration/src/Models/WordPressMigration.php) | `public_id`, `source_url`, `status`, `total_records`, `processed_records`, `failed_records`, `options`, `metadata`, `failure_reason`, `started_at`, `completed_at`, `team_id` |
| [WordPressMigrationRecord.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-wordpress-migration/src/Models/WordPressMigrationRecord.php) | `migration_id`, `record_type`, `source_id`, `source_parent_id`, `status`, `payload`, `source_identifiers`, `failure_reason`, `processed_at`, `team_id` |
<!-- layer-implementation-plan:end -->
