# liberusoftware/module-browser-game-moderation-and-analytics: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral Browser Game ModerationAndAnalytics capability.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [browser-game-moderation-and-analytics](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-browser-game-laravel-filament, `browser-game-moderation-and-analytics`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-browser-game-moderation-and-analytics` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `browser-game-moderation-and-analytics` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\BrowserGame\\ModerationAndAnalytics\\ModerationAndAnalyticsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/composer.json) · [module.json](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/module.json).

**Declared capabilities:** browser-game.moderation-and-analytics

**Declared features:** Reports, sanctions, and appeals, Telemetry, funnels, balance, and economy, Fraud and health signals

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\BrowserGame\\ModerationAndAnalytics\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Queries/ModerationAndAnalyticsQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/src/Queries/ModerationAndAnalyticsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |
| [src/Support/ModerationAndAnalyticsManager.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/src/Support/ModerationAndAnalyticsManager.php) | `public function define(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null): ModerationAndAnalyticsRecord`<br>`public function record(string $kind, string $name, ?string $actorId = null, ?string $targetId = null, array $data = [], ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): ModerationAndAnalyticsRecord`<br>`public function resolve(ModerationAndAnalyticsRecord $record, string $status = 'resolved'): ModerationAndAnalyticsRecord`<br>`public function issueSanction(string $actorId, string $targetId, string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): ModerationAndAnalyticsRecord`<br>`public function submitAppeal(string $actorId, string $targetId, string $reason, array $data = [], ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): ModerationAndAnalyticsRecord`<br>`public function recordTelemetry(string $actorId, string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): ModerationAndAnalyticsRecord`<br>`public function recordFunnel(string $actorId, string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): ModerationAndAnalyticsRecord`<br>`public function recordBalance(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): ModerationAndAnalyticsRecord`<br>`public function recordEconomy(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): ModerationAndAnalyticsRecord`<br>`public function recordFraud(string $actorId, string $targetId, string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): ModerationAndAnalyticsRecord`<br>`public function recordHealth(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): ModerationAndAnalyticsRecord` |

Other non-legacy PHP sources: [src/Events/ModerationAndAnalyticsDefined.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/src/Events/ModerationAndAnalyticsDefined.php) · [src/Events/ModerationAndAnalyticsRecorded.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/src/Events/ModerationAndAnalyticsRecorded.php) · [src/Events/ModerationAndAnalyticsResolved.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/src/Events/ModerationAndAnalyticsResolved.php) · [src/Models/ModerationAndAnalyticsRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/src/Models/ModerationAndAnalyticsRecord.php) · [src/ModerationAndAnalyticsServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/src/ModerationAndAnalyticsServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_000510_create_browser_game_moderation_and_analytics_tables.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/database/migrations/2026_08_24_000510_create_browser_game_moderation_and_analytics_tables.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/tests/Pest.php)
- [tests/Unit/ModerationAndAnalyticsBoundaryTest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/tests/Unit/ModerationAndAnalyticsBoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
