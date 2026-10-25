# liberusoftware/module-social-network-profiles: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Tenant-aware social profiles, handles, visibility, verification, and blocking.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [social-network-profiles](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/composer.json) | `08bbc484b50f` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: social-network-laravel, `social-network-profiles`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-social-network-profiles` |
| Composer version field | `0.1.2` |
| Package type | `liberu-module` |
| Module manifest name | `social-network-profiles` |
| Module version field | `0.1.2` |
| Category / layers | `"product"` |
| Manifest provider(s) | `"Liberu\\SocialNetwork\\Profiles\\ProfilesServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/composer.json) · [module.json](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/module.json).

**Declared capabilities:** social-network.profiles

**Declared features:** Handles, Bios, Attributes, Avatars, Verification, Visibility, Blocking, Profile lifecycle

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\SocialNetwork\\Profiles\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/BlockProfile.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Actions/BlockProfile.php) | `public function __construct(private ProfileAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $blocker, Profile $blocked): void` |
| [src/Actions/GetProfile.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Actions/GetProfile.php) | `public function __construct(private ProfileRepository $profiles, private ProfileAuthorizer $authorizer)`<br>`public function byId(string $id): Profile`<br>`public function forUser(int\|string $userId): Profile` |
| [src/Actions/UnblockProfile.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Actions/UnblockProfile.php) | `public function __construct(private ProfileAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $blocker, Profile $blocked): void` |
| [src/Actions/UpdateLifecycleState.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Actions/UpdateLifecycleState.php) | `public function __construct(private Dispatcher $events)`<br>`public function handle(Profile $profile, string $state): Profile` |
| [src/Actions/UpdateProfile.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Actions/UpdateProfile.php) | `public function __construct(private ProfileRepository $profiles, private ProfileAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $profile, array $attributes): Profile` |
| [src/Actions/UpdateVerificationStatus.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Actions/UpdateVerificationStatus.php) | `public function __construct(private Dispatcher $events)`<br>`public function handle(Profile $profile, string $status): Profile` |
| [src/Contracts/ProfileAuthorizer.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Contracts/ProfileAuthorizer.php) | `public function view(Profile $profile): void`<br>`public function update(Profile $profile): void`<br>`public function block(Profile $profile, Profile $target): void` |
| [src/Contracts/ProfileRepository.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Contracts/ProfileRepository.php) | `public function forUser(int\|string $userId): Profile`<br>`public function find(string $id): Profile` |

Other non-legacy PHP sources: [src/Authorization/GateProfileAuthorizer.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Authorization/GateProfileAuthorizer.php) · [src/Events/ProfileBlocked.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Events/ProfileBlocked.php) · [src/Events/ProfileLifecycleUpdated.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Events/ProfileLifecycleUpdated.php) · [src/Events/ProfileUnblocked.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Events/ProfileUnblocked.php) · [src/Events/ProfileUpdated.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Events/ProfileUpdated.php) · [src/Events/ProfileVerificationUpdated.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Events/ProfileVerificationUpdated.php) · [src/Models/Profile.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Models/Profile.php) · [src/ProfilesServiceProvider.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/ProfilesServiceProvider.php) · [src/Repositories/EloquentProfileRepository.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Repositories/EloquentProfileRepository.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_010000_create_social_profiles_table.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/database/migrations/2026_08_24_010000_create_social_profiles_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest", "test:coverage": "pest --coverage --min=100 --coverage-clover=coverage.xml", "test:feature": "pest tests/Feature", "test:parallel": "pest --parallel", "test:unit": "pest tests/Unit"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/tests/Pest.php)
- [tests/Unit/PackageStructureTest.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/tests/Unit/PackageStructureTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
