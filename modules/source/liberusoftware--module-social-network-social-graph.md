# liberusoftware/module-social-network-social-graph: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Tenant-aware follows, friendship requests, lists, suggestions, and relationship visibility.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [social-network-social-graph](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/composer.json) | `08bbc484b50f` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: social-network-laravel, `social-network-social-graph`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-social-network-social-graph` |
| Composer version field | `0.1.2` |
| Package type | `liberu-module` |
| Module manifest name | `social-network-social-graph` |
| Module version field | `0.1.2` |
| Category / layers | `"product"` |
| Manifest provider(s) | `"Liberu\\SocialNetwork\\SocialGraph\\SocialGraphServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/composer.json) · [module.json](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/module.json).

**Declared capabilities:** social-network.social-graph

**Declared features:** Follows, Friendship requests, Lists, Suggestions, Blocks, Relationship visibility

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-social-network-profiles` | `^0.1` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\SocialNetwork\\SocialGraph\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-social-network-profiles": "^0.1"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AcceptFriendship.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/AcceptFriendship.php) | `public function handle(Profile $actor, Relationship $relationship): Relationship` |
| [src/Actions/AddProfileToList.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/AddProfileToList.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $owner, GraphList $list, Profile $profile): GraphList` |
| [src/Actions/BlockProfile.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/BlockProfile.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $source, Profile $target): Block` |
| [src/Actions/CancelFriendship.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/CancelFriendship.php) | `public function handle(Profile $actor, Relationship $relationship): Relationship` |
| [src/Actions/CreateList.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/CreateList.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $owner, array $attributes): GraphList` |
| [src/Actions/CreateRelationship.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/CreateRelationship.php) | `public function __construct(private GraphAuthorizer $authorizer, private Dispatcher $events)`<br>`public function follow(Profile $source, Profile $target): Relationship`<br>`public function friend(Profile $source, Profile $target): Relationship` |
| [src/Actions/ListOwnedBlocks.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/ListOwnedBlocks.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $owner): Collection` |
| [src/Actions/ListOwnedLists.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/ListOwnedLists.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $owner): Collection` |
| [src/Actions/ListRelationships.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/ListRelationships.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $viewer, ?string $type = null, ?string $status = null, int $limit = 100): Collection` |
| [src/Actions/RejectFriendship.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/RejectFriendship.php) | `public function handle(Profile $actor, Relationship $relationship): Relationship` |
| [src/Actions/RemoveProfileFromList.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/RemoveProfileFromList.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $owner, GraphList $list, Profile $profile): GraphList` |
| [src/Actions/SuggestProfiles.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/SuggestProfiles.php) | `public function for(Profile $profile, int $limit = 10): Collection` |
| [src/Actions/UnblockProfile.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/UnblockProfile.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $source, Profile $target): bool` |
| [src/Actions/UpdateRelationshipVisibility.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/UpdateRelationshipVisibility.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $actor, Relationship $relationship, string $visibility): Relationship` |
| [src/Contracts/GraphAuthorizer.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Contracts/GraphAuthorizer.php) | `public function follow(Profile $source, Profile $target): void`<br>`public function friend(Profile $source, Profile $target): void`<br>`public function list(Profile $owner): void`<br>`public function block(Profile $source, Profile $target): void`<br>`public function unblock(Profile $source, Profile $target): void`<br>`public function visibility(Profile $actor, Relationship $relationship): void` |

Other non-legacy PHP sources: [src/Authorization/GateGraphAuthorizer.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Authorization/GateGraphAuthorizer.php) · [src/Events/RelationshipCreated.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Events/RelationshipCreated.php) · [src/Models/Block.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Models/Block.php) · [src/Models/GraphList.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Models/GraphList.php) · [src/Models/Relationship.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Models/Relationship.php) · [src/SocialGraphServiceProvider.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/SocialGraphServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_000100_create_social_graph_blocks_table.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/database/migrations/2026_08_24_000100_create_social_graph_blocks_table.php)
- [database/migrations/2026_08_24_020000_create_social_graph_tables.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/database/migrations/2026_08_24_020000_create_social_graph_tables.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest", "test:coverage": "pest --coverage --min=100 --coverage-clover=coverage.xml", "test:feature": "pest tests/Feature", "test:parallel": "pest --parallel", "test:unit": "pest tests/Unit"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/tests/Pest.php)
- [tests/Unit/PackageStructureTest.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/tests/Unit/PackageStructureTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
