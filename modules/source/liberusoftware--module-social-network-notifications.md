# liberusoftware/module-social-network-notifications: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Notification preferences, delivery, grouping, digests, quiet hours, and read state.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [social-network-notifications](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/composer.json) | `08bbc484b50f` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-social-network-laravel-filament, `social-network-notifications`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-social-network-notifications` |
| Composer version field | `0.1.2` |
| Package type | `liberu-module` |
| Module manifest name | `social-network-notifications` |
| Module version field | `0.1.2` |
| Category / layers | `"product"` |
| Manifest provider(s) | `"Liberu\\SocialNetwork\\Notifications\\NotificationsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/composer.json) · [module.json](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/module.json).

**Declared capabilities:** social-network.notifications

**Declared features:** Preferences, In-app, email, and push delivery, Grouping, Digests, Quiet hours, Read state

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-social-network-profiles` | `^0.1` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\SocialNetwork\\Notifications\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-social-network-profiles": "^0.1"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateNotification.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/CreateNotification.php) | `public function __construct(private Dispatcher $events)`<br>`public function handle(string $profileId, string $kind, array $payload = [], string $channel = 'in_app', ?string $groupKey = null): SocialNotification` |
| [src/Actions/DismissNotification.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/DismissNotification.php) | `public function __construct(private NotificationAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $profile, string $id): SocialNotification` |
| [src/Actions/MarkAllRead.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/MarkAllRead.php) | `public function __construct(private NotificationAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $profile): int` |
| [src/Actions/MarkRead.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/MarkRead.php) | `public function __construct(private NotificationAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $profile, string $id): SocialNotification` |
| [src/Actions/UnreadCount.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/UnreadCount.php) | `public function __construct(private NotificationAuthorizer $authorizer)`<br>`public function handle(Profile $profile): int` |
| [src/Actions/UpdatePreferences.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/UpdatePreferences.php) | `public function __construct(private NotificationAuthorizer $authorizer)`<br>`public function handle(Profile $profile, array $data): NotificationPreference` |
| [src/Contracts/NotificationAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Contracts/NotificationAuthorizer.php) | `public function manage(Profile $profile): void`<br>`public function view(Profile $profile): void` |

Other non-legacy PHP sources: [src/Authorization/GateNotificationAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Authorization/GateNotificationAuthorizer.php) · [src/Events/NotificationCreated.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Events/NotificationCreated.php) · [src/Events/NotificationStateChanged.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Events/NotificationStateChanged.php) · [src/Models/NotificationPreference.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Models/NotificationPreference.php) · [src/Models/SocialNotification.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Models/SocialNotification.php) · [src/NotificationsServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/NotificationsServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_090000_create_social_notifications_tables.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/database/migrations/2026_08_24_090000_create_social_notifications_tables.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest", "test:coverage": "pest --coverage --min=100 --coverage-clover=coverage.xml", "test:feature": "pest tests/Feature", "test:parallel": "pest --parallel", "test:unit": "pest tests/Unit"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/tests/Pest.php)
- [tests/Unit/PackageStructureTest.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/tests/Unit/PackageStructureTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
