# liberusoftware/module-browser-game-game-core: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral Browser Game worlds, clocks, rulesets, content versions, feature flags, and maintenance state.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [browser-game-game-core](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-browser-game-laravel-filament, `browser-game-game-core`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-browser-game-game-core` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `browser-game-game-core` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\BrowserGame\\GameCore\\GameCoreServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/composer.json) · [module.json](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/module.json).

**Declared capabilities:** browser-game.game-core

**Declared features:** Worlds and shards, Authoritative game clocks, Versioned rulesets, Content versions, Feature flags, Maintenance state

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\BrowserGame\\GameCore\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/GameCoreContext.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Contracts/GameCoreContext.php) | `public function actorId(): ?string`<br>`public function tenantId(): ?string`<br>`public function teamId(): ?string` |
| [src/Policies/GameCorePolicy.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Policies/GameCorePolicy.php) | `public function view(GameCoreContext $context, GameWorld $world): bool`<br>`public function manage(GameCoreContext $context, GameWorld $world): bool` |
| [src/Queries/GameCoreOverview.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Queries/GameCoreOverview.php) | `public function forWorld(GameCoreContext $context, string $worldId): array`<br>`public function enabledFlags(?string $worldId = null): Collection`<br>`public function isEnabled(GameCoreContext $context, ?GameWorld $world, string $key, array $attributes = []): bool`<br>`public function enabledFor(GameCoreContext $context, ?GameWorld $world, array $attributes = []): Collection` |
| [src/Support/ArrayGameCoreContext.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Support/ArrayGameCoreContext.php) | `public function __construct( private ?string $actor = null, private ?string $tenant = null, private ?string $team = null, )`<br>`public function actorId(): ?string`<br>`public function tenantId(): ?string`<br>`public function teamId(): ?string` |
| [src/Support/GameCoreManager.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Support/GameCoreManager.php) | `public function createWorld(GameCoreContext $context, string $name, string $slug, array $metadata = []): GameWorld`<br>`public function setClock(GameCoreContext $context, GameWorld $world, string $currentAt, string $speed = '1', bool $paused = false): GameClock`<br>`public function updateWorld(GameCoreContext $context, GameWorld $world, string $name, string $status, array $metadata = []): GameWorld`<br>`public function publishRuleset(GameCoreContext $context, GameWorld $world, int $version, array $rules): GameRuleset`<br>`public function publishContentVersion(GameCoreContext $context, GameWorld $world, int $version, string $contentHash, array $manifest): GameContentVersion`<br>`public function setFeatureFlag(GameCoreContext $context, ?GameWorld $world, string $key, bool $enabled, int $rolloutPercentage = 100, array $constraints = []): GameFeatureFlag`<br>`public function setMaintenance(GameCoreContext $context, GameWorld $world, string $status, ?string $message = null): GameMaintenanceState` |

Other non-legacy PHP sources: [src/Events/GameClockChanged.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Events/GameClockChanged.php) · [src/Events/GameContentVersionPublished.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Events/GameContentVersionPublished.php) · [src/Events/GameFeatureFlagChanged.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Events/GameFeatureFlagChanged.php) · [src/Events/GameMaintenanceStateChanged.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Events/GameMaintenanceStateChanged.php) · [src/Events/GameRulesetPublished.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Events/GameRulesetPublished.php) · [src/Events/GameWorldCreated.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Events/GameWorldCreated.php) · [src/Events/GameWorldUpdated.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Events/GameWorldUpdated.php) · [src/GameCoreServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/GameCoreServiceProvider.php) · [src/Models/GameClock.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameClock.php) · [src/Models/GameContentVersion.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameContentVersion.php) · [src/Models/GameFeatureFlag.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameFeatureFlag.php) · [src/Models/GameMaintenanceState.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameMaintenanceState.php) · [src/Models/GameRuleset.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameRuleset.php) · [src/Models/GameWorld.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameWorld.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_000000_create_browser_game_core_tables.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/database/migrations/2026_08_24_000000_create_browser_game_core_tables.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/tests/Pest.php)
- [tests/Unit/GameCoreBoundaryTest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/tests/Unit/GameCoreBoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
