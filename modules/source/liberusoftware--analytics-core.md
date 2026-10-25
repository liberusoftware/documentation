# liberusoftware/analytics-core: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Consent-aware provider-neutral analytics event routing and durable delivery evidence.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/analytics-core/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 4 |
| [automation](../../projects/automation/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/analytics-core/composer.json) | `68e5f07a6704` | [Variant 1](#variant-1) | 4 |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/analytics-core/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 4 |
| [boilerplate](../../projects/boilerplate/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/boilerplate-laravel/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/analytics-core/composer.json) | `3ade34046c3d` | [Variant 1](#variant-1) | 4 |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/analytics-core/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 4 |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/analytics-core/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 4 |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core/composer.json) | `63aad94e94c0` | [Variant 2](#variant-2) | 4 |
| [sap](../../projects/sap/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/analytics-core/composer.json) | `b12a8c841c6a` | [Variant 1](#variant-1) | 4 |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/analytics-core/composer.json) | `577e93db23cc` | [Variant 1](#variant-1) | 4 |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/analytics-core/composer.json) | `c267d625e264` | [Variant 1](#variant-1) | 4 |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/analytics-core/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 4 |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [analytics-core](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/analytics-core/composer.json) | `08bbc484b50f` | [Variant 1](#variant-1) | 4 |

Physical source locations: **12**. Reference variants: **2**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `analytics-core`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/analytics-core` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `analytics-core` |
| Module version field | `1.4.1` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Analytics\\Core\\AnalyticsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/analytics-core/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/analytics-core/module.json).

**Declared capabilities:** analytics.route

**Declared features:** Versioned event envelopes, Consent, Mapping, Minimization, Routing, Deduplication, Queues, Redaction, Delivery audit

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/analytics-contracts` | `^1.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Analytics\\Core\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/analytics-contracts": "^1.0", "liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Support/ConsentPolicy.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/analytics-core/src/Support/ConsentPolicy.php) | `public function permits(string $category, array $grants): bool` |
| [src/Support/DestinationRegistry.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/analytics-core/src/Support/DestinationRegistry.php) | `public function register(AnalyticsDestination $destination): void`<br>`public function get(string $name): AnalyticsDestination`<br>`public function all(): array` |
| [src/Support/EventRouter.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/analytics-core/src/Support/EventRouter.php) | `public function __construct(private DestinationRegistry $destinations, private ConsentPolicy $consent)`<br>`public function route(AnalyticsEvent $event, array $grants, array $allowedDestinations): array` |
| [src/Support/EventSanitizer.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/analytics-core/src/Support/EventSanitizer.php) | `public function sanitize(array $properties, array $allowed): array`<br>`public function pseudonymize(?string $identifier, string $salt): ?string` |

Other non-legacy PHP sources: [src/AnalyticsServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/analytics-core/src/AnalyticsServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_01_040000_create_analytics_deliveries_table.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/analytics-core/database/migrations/2026_08_01_040000_create_analytics_deliveries_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **4**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/analytics-core/tests/.gitkeep)
- [tests/Pest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/analytics-core/tests/Pest.php)
- [tests/Unit/DestinationsCoverageTest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/analytics-core/tests/Unit/DestinationsCoverageTest.php)
- [tests/Unit/EventRouterTest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/analytics-core/tests/Unit/EventRouterTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 2

Representative: crm-laravel, `analytics-core`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/analytics-core` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `analytics-core` |
| Module version field | `1.4.1` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Analytics\\Core\\AnalyticsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core/module.json).

**Declared capabilities:** analytics.route

**Declared features:** Versioned event envelopes, Consent, Mapping, Minimization, Routing, Deduplication, Queues, Redaction, Delivery audit

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/analytics-contracts` | `^1.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Analytics\\Core\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/analytics-contracts": "^1.0", "liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Support/ConsentPolicy.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core/src/Support/ConsentPolicy.php) | `public function permits(string $category, array $grants): bool` |
| [src/Support/DestinationRegistry.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core/src/Support/DestinationRegistry.php) | `public function register(AnalyticsDestination $destination): void`<br>`public function get(string $name): AnalyticsDestination`<br>`public function all(): array` |
| [src/Support/EventRouter.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core/src/Support/EventRouter.php) | `public function __construct(private DestinationRegistry $destinations, private ConsentPolicy $consent)`<br>`public function route(AnalyticsEvent $event, array $grants, array $allowedDestinations): array` |
| [src/Support/EventSanitizer.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core/src/Support/EventSanitizer.php) | `public function sanitize(array $properties, array $allowed): array`<br>`public function pseudonymize(?string $identifier, string $salt): ?string` |

Other non-legacy PHP sources: [src/AnalyticsServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core/src/AnalyticsServiceProvider.php).

**Legacy review:** 20 files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2024_02_15_000004_create_reporting_tables.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core/database/migrations/2024_02_15_000004_create_reporting_tables.php)
- [database/migrations/2024_10_22_000000_create_dashboard_widgets_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core/database/migrations/2024_10_22_000000_create_dashboard_widgets_table.php)
- [database/migrations/2026_08_01_040000_create_analytics_deliveries_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core/database/migrations/2026_08_01_040000_create_analytics_deliveries_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **4**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core/tests/.gitkeep)
- [tests/Pest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core/tests/Pest.php)
- [tests/Unit/DestinationsCoverageTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core/tests/Unit/DestinationsCoverageTest.php)
- [tests/Unit/EventRouterTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/analytics-core/tests/Unit/EventRouterTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
