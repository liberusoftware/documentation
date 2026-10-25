# liberusoftware/module-social-network-discovery: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Framework-neutral discovery domain module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [social-network-discovery](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/composer.json) | `08bbc484b50f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: social-network-laravel, `social-network-discovery`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-social-network-discovery` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `social-network-discovery` |
| Module version field | `0.1.0` |
| Category / layers | `"product"` |
| Manifest provider(s) | `"Liberu\\SocialNetwork\\Discovery\\DiscoveryServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/composer.json) · [module.json](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/module.json).

**Declared capabilities:** social-network.discovery

**Declared features:** Search, Hashtags, Trends, Recommendations, Directories, Privacy-aware indexing

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `laravel/framework` | `^13.0` |
| `liberusoftware/module-social-network-profiles` | `^0.1` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\SocialNetwork\\Discovery\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-social-network-profiles": "^0.1"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/IndexResource.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/src/Actions/IndexResource.php) | `public function __construct(private DiscoveryAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $owner, array $attributes): DiscoveryIndex` |
| [src/Actions/ListTrends.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/src/Actions/ListTrends.php) | `public function __construct(private DiscoveryAuthorizer $authorizer)`<br>`public function handle(Profile $viewer, int $limit = 20): array` |
| [src/Actions/SearchDiscovery.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/src/Actions/SearchDiscovery.php) | `public function __construct(private DiscoveryAuthorizer $authorizer)`<br>`public function handle(Profile $viewer, string $query, int $limit = 25): Collection` |
| [src/Contracts/DiscoveryAuthorizer.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/src/Contracts/DiscoveryAuthorizer.php) | `public function search(Profile $viewer): void`<br>`public function index(Profile $owner): void` |

Other non-legacy PHP sources: [src/Authorization/GateDiscoveryAuthorizer.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/src/Authorization/GateDiscoveryAuthorizer.php) · [src/DiscoveryServiceProvider.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/src/DiscoveryServiceProvider.php) · [src/Events/DiscoveryIndexUpdated.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/src/Events/DiscoveryIndexUpdated.php) · [src/Models/DiscoveryIndex.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/src/Models/DiscoveryIndex.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_120000_create_social_discovery_index_table.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/database/migrations/2026_08_24_120000_create_social_discovery_index_table.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
