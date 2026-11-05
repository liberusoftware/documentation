# liberusoftware/module-social-network-media: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Images, video, audio, files, processing, accessibility text, captions, rights, and delivery.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [social-network-media](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/composer.json) | `08bbc484b50f` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-social-network-laravel-filament, `social-network-media`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-social-network-media` |
| Composer version field | `0.1.2` |
| Package type | `liberu-module` |
| Module manifest name | `social-network-media` |
| Module version field | `0.1.2` |
| Category / layers | `"product"` |
| Manifest provider(s) | `"Liberu\\SocialNetwork\\Media\\MediaServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/composer.json) · [module.json](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/module.json).

**Declared capabilities:** social-network.media

**Declared features:** Images, Video, Audio, Files, Processing, Alt text, Captions, Rights, Delivery, Albums with privacy controls

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-social-network-profiles` | `^0.1` |
| `liberusoftware/module-social-network-social-graph` | `^0.1` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\SocialNetwork\\Media\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-social-network-profiles": "^0.1", "liberusoftware/module-social-network-social-graph": "^0.1"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateAlbum.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/CreateAlbum.php) | `public function handle(Profile $owner, array $attributes): Album` |
| [src/Actions/DeleteAlbum.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/DeleteAlbum.php) | `public function handle(Profile $owner, Album $album): void` |
| [src/Actions/DeleteMediaAsset.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/DeleteMediaAsset.php) | `public function handle(Profile $owner, MediaAsset $asset): void` |
| [src/Actions/MarkMediaReady.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/MarkMediaReady.php) | `public function handle(Profile $owner, MediaAsset $asset): MediaAsset` |
| [src/Actions/RegisterMediaAsset.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/RegisterMediaAsset.php) | `public function __construct(private MediaAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $owner, array $attributes): MediaAsset` |
| [src/Actions/UpdateAlbum.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/UpdateAlbum.php) | `public function handle(Profile $owner, Album $album, array $attributes): Album` |
| [src/Actions/UpdateMediaAsset.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/UpdateMediaAsset.php) | `public function __construct(private MediaAuthorizer $authorizer)`<br>`public function handle(Profile $owner, MediaAsset $asset, array $attributes): MediaAsset` |
| [src/Contracts/MediaAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Contracts/MediaAuthorizer.php) | `public function upload(Profile $owner): void`<br>`public function update(Profile $owner): void` |

Other non-legacy PHP sources: [src/Authorization/GateMediaAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Authorization/GateMediaAuthorizer.php) · [src/Events/MediaAssetCreated.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Events/MediaAssetCreated.php) · [src/MediaServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/MediaServiceProvider.php) · [src/Models/Album.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Models/Album.php) · [src/Models/MediaAsset.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Models/MediaAsset.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_060000_create_social_media_assets_table.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/database/migrations/2026_08_24_060000_create_social_media_assets_table.php)
- [database/migrations/2026_08_30_000000_create_social_media_albums_table.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/database/migrations/2026_08_30_000000_create_social_media_albums_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest", "test:coverage": "pest --coverage --min=100 --coverage-clover=coverage.xml", "test:feature": "pest tests/Feature", "test:parallel": "pest --parallel", "test:unit": "pest tests/Unit"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/tests/Pest.php)
- [tests/Unit/PackageStructureTest.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/tests/Unit/PackageStructureTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
