# Cms Joomla Migration Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-joomla-migration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-cms-joomla-migration-flutter
**Matching core package:** module-cms-cms-joomla-migration ([implementation](../core/cms-joomla-migration.md))
**Matching API package:** module-cms-cms-joomla-migration-api ([contract](../api/cms-joomla-migration.md))

## Implementation plan

This adapter presents Cms Joomla Migration for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Cms Joomla Migration API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/cms-joomla-migration.md), and [API module](../api/cms-joomla-migration.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `cms-joomla-migration`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-cms-mobile-flutter`](https://github.com/liberusoftware/project-cms-mobile-flutter) | [`module-cms-joomla-migration-flutter`](https://github.com/liberusoftware/module-cms-joomla-migration-flutter) (`module_cms_joomla_migration_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-cms-dart-mobile`](https://github.com/liberusoftware/project-cms-dart-mobile) | [`module-cms-joomla-migration-dart-mobile`](https://github.com/liberusoftware/module-cms-joomla-migration-dart-mobile) (`module_cms_joomla_migration_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-cms-dart-desktop`](https://github.com/liberusoftware/project-cms-dart-desktop) | [`module-cms-joomla-migration-dart-desktop`](https://github.com/liberusoftware/module-cms-joomla-migration-dart-desktop) (`module_cms_joomla_migration_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | [API plan](../api/cms-joomla-migration.md) · [Core plan](../core/cms-joomla-migration.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Articles/categories** | Adaptive mobile cards/sheets for `articles/categories` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `articles/categories` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Custom fields** | Adaptive mobile cards/sheets for `custom fields` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `custom fields` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Contacts** | Adaptive mobile cards/sheets for `contacts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `contacts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Menus** | Adaptive mobile cards/sheets for `menus` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `menus` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Modules/positions** | Adaptive mobile cards/sheets for `modules/positions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `modules/positions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Media** | Adaptive mobile cards/sheets for `media` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `media` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Users/authors** | Adaptive mobile cards/sheets for `users/authors` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `users/authors` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Tags** | Adaptive mobile cards/sheets for `tags` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `tags` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Languages** | Adaptive mobile cards/sheets for `languages` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `languages` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Redirects** | Adaptive mobile cards/sheets for `redirects` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `redirects` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [JoomlaMigrationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-joomla-migration/src/Services/JoomlaMigrationService.php) | `public function __construct(private MigrationFrameworkService $framework)`<br>`public function start(string $source, array $options = [], ?int $teamId = null): MigrationJob`<br>`public function add(MigrationJob $job, string $type, string $sourceId, array $payload = []): MigrationRecord`<br>`public function process(MigrationRecord $record, bool $success, ?string $reason = null): MigrationRecord`<br>`public function complete(MigrationJob $job): MigrationJob` |
<!-- layer-implementation-plan:end -->
