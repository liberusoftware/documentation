# liberusoftware/module-social-network-analytics: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Privacy-aware social network analytics and metric snapshots.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [social-network-analytics](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/composer.json) | `08bbc484b50f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: social-network-laravel, `social-network-analytics`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-social-network-analytics` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `social-network-analytics` |
| Module version field | `0.1.0` |
| Category / layers | `"product"` |
| Manifest provider(s) | `"Liberu\\SocialNetwork\\Analytics\\AnalyticsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/composer.json) · [module.json](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/module.json).

**Declared capabilities:** analytics.growth, analytics.engagement, analytics.retention, analytics.health, analytics.delivery, analytics.moderation, analytics.privacy-governed-insights

**Declared features:** metric events, privacy redaction, cohort snapshots, retention windows

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `laravel/framework` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\SocialNetwork\\Analytics\\": "src/"}`.

Module resolver requirements: `{"modules": [], "packages": []}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/BuildSnapshot.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Actions/BuildSnapshot.php) | `public function __construct( private AnalyticsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(object $actor, string $metric, string $periodStart, string $periodEnd, int $cohortSize, float $value, array $dimensions = []): MetricSnapshot` |
| [src/Actions/GetMetrics.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Actions/GetMetrics.php) | `public function __construct(private AnalyticsAuthorizer $authorizer)`<br>`public function handle(object $actor, string $metric, int $limit = 30): Collection` |
| [src/Actions/RecordMetric.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Actions/RecordMetric.php) | `public function __construct( private AnalyticsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(object $actor, string $name, array $dimensions = [], int $value = 1): AnalyticsEvent` |
| [src/Contracts/AnalyticsAuthorizer.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Contracts/AnalyticsAuthorizer.php) | `public function view(object $actor, string $metric): void`<br>`public function record(object $actor, string $metric): void` |

Other non-legacy PHP sources: [src/AnalyticsServiceProvider.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/AnalyticsServiceProvider.php) · [src/Authorization/GateAnalyticsAuthorizer.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Authorization/GateAnalyticsAuthorizer.php) · [src/Events/MetricRecorded.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Events/MetricRecorded.php) · [src/Events/MetricSnapshotCreated.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Events/MetricSnapshotCreated.php) · [src/Models/AnalyticsEvent.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Models/AnalyticsEvent.php) · [src/Models/MetricSnapshot.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Models/MetricSnapshot.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_150000_create_social_analytics_tables.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/database/migrations/2026_08_24_150000_create_social_analytics_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
