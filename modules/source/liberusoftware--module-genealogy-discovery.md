# liberusoftware/module-genealogy-discovery: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Liberu genealogy-discovery module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [genealogy-discovery](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/composer.json) | `577e93db23cc` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: genealogy-laravel, `genealogy-discovery`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-genealogy-discovery` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `genealogy-discovery` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Genealogy\\Discovery\\DiscoveryServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/composer.json) · [module.json](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/module.json).

**Declared capabilities:** genealogy.discovery, genealogy.discovery.search, genealogy.discovery.hints, genealogy.discovery.duplicates, genealogy.discovery.relationship-paths, genealogy.discovery.privacy-indexes, genealogy.discovery.social-family, genealogy.discovery.smart-matching, genealogy.discovery.lifecycle

**Declared features:** genealogy discovery, genealogy discovery search, genealogy discovery hints, genealogy discovery duplicates, genealogy discovery relationship-paths, genealogy discovery privacy-indexes, genealogy discovery social-family, genealogy discovery smart-matching, genealogy discovery lifecycle

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/identity-socialstream` | `^1.4` |
| `liberusoftware/module-genealogy-core` | `^1.0` |
| `liberusoftware/module-genealogy-evidence` | `^1.0` |
| `liberusoftware/module-genealogy-people` | `^1.0` |
| `liberusoftware/module-genealogy-places` | `^1.0` |
| `liberusoftware/module-genealogy-relationships` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Genealogy\\Discovery\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/identity-socialstream": "^1.4", "liberusoftware/module-genealogy-core": "^1.0", "liberusoftware/module-genealogy-evidence": "^1.0", "liberusoftware/module-genealogy-people": "^1.0", "liberusoftware/module-genealogy-places": "^1.0", "liberusoftware/module-genealogy-relationships": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateDiscoveryMatch.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Actions/CreateDiscoveryMatch.php) | `public function execute(array $attributes): DiscoveryMatch` |
| [src/Actions/DeleteDiscoveryMatch.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Actions/DeleteDiscoveryMatch.php) | `public function execute(DiscoveryMatch $match): void` |
| [src/Actions/ReviewDiscoveryMatch.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Actions/ReviewDiscoveryMatch.php) | `public function execute(DiscoveryMatch $match, string $status): DiscoveryMatch` |
| [src/Actions/ScanDuplicateCandidates.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Actions/ScanDuplicateCandidates.php) | `public function __construct( private readonly DuplicateCandidates $candidates, private readonly CreateDiscoveryMatch $create, )`<br>`public function execute(float $threshold = 0.7, int $limit = 100): array` |
| [src/Actions/UpdateDiscoveryMatch.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Actions/UpdateDiscoveryMatch.php) | `public function execute(DiscoveryMatch $match, array $attributes): DiscoveryMatch` |
| [src/Contracts/ExternalRecordProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Contracts/ExternalRecordProvider.php) | `public function key(): string`<br>`public function isAvailable(): bool`<br>`public function search(array $person): array` |
| [src/Queries/DiscoverySearch.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Queries/DiscoverySearch.php) | `public function execute(string $term, array $options = []): array` |
| [src/Queries/DuplicateCandidates.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Queries/DuplicateCandidates.php) | `public function execute(int $limit = 100, int $minimumConfidence = 70): array` |
| [src/Queries/RelationshipPath.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Queries/RelationshipPath.php) | `public function execute(string $from, string $to, int $maxDepth = 6, bool $publicOnly = false): array` |
| [src/Services/ExternalRecordMatcher.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Services/ExternalRecordMatcher.php) | `public function __construct(private readonly ?ExternalRecordProvider $provider = null)`<br>`public function execute(array $person, array $weights = []): array`<br>`public function scoreCandidates(array $person, array $candidates, array $weights = []): array` |
| [src/Services/SmartMatchingService.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Services/SmartMatchingService.php) | `public function findMatches(Person $person, iterable $providers, int $minimumConfidence = 60, int $limit = 10): array`<br>`public function persist(Model $user, Person $person, array $matches): Collection` |
| [src/Services/SocialFamilyDiscovery.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Services/SocialFamilyDiscovery.php) | `public function enable(ConnectedAccount $account): bool`<br>`public function disable(ConnectedAccount $account): bool`<br>`public function sync(ConnectedAccount $account): bool`<br>`public function privacy(int\|string $userId): SocialConnectionPrivacy`<br>`public function updatePrivacy(int\|string $userId, array $settings): SocialConnectionPrivacy`<br>`public function needsSync(ConnectedAccount $account): bool`<br>`public function findPotentialConnections(Model $user): Collection`<br>`public function processMatches(Model $user): int` |

Other non-legacy PHP sources: [src/Capability.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Capability.php) · [src/DiscoveryServiceProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/DiscoveryServiceProvider.php) · [src/Events/DiscoveryMatchDeleted.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Events/DiscoveryMatchDeleted.php) · [src/Events/DiscoveryMatchReviewed.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Events/DiscoveryMatchReviewed.php) · [src/Events/DiscoveryMatchUpdated.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Events/DiscoveryMatchUpdated.php) · [src/Models/DiscoveryMatch.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Models/DiscoveryMatch.php) · [src/Models/SmartMatch.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Models/SmartMatch.php) · [src/Models/SocialConnectionPrivacy.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Models/SocialConnectionPrivacy.php) · [src/Models/SocialFamilyConnection.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Models/SocialFamilyConnection.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_010000_create_genealogy_discovery_matches_table.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/database/migrations/2026_08_24_010000_create_genealogy_discovery_matches_table.php)
- [database/migrations/2026_08_24_020000_add_discovery_capability_fields.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/database/migrations/2026_08_24_020000_add_discovery_capability_fields.php)
- [database/migrations/2026_08_30_050000_create_genealogy_social_family_connections.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/database/migrations/2026_08_30_050000_create_genealogy_social_family_connections.php)
- [database/migrations/2026_08_30_060000_create_genealogy_smart_matches_table.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/database/migrations/2026_08_30_060000_create_genealogy_smart_matches_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/DomainTest.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/tests/Feature/DomainTest.php)
- [tests/Unit/CapabilityTest.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/tests/Unit/CapabilityTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
