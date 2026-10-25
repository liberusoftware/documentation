# liberusoftware/module-browser-game-game-core-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Filament 5 adapter for Browser Game Game Core.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [browser-game-game-core-filament](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: browser-game-laravel, `browser-game-game-core-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-browser-game-game-core-filament` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `browser-game-game-core-filament` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\BrowserGame\\GameCoreFilament\\GameCoreFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/composer.json) · [module.json](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/module.json).

**Declared capabilities:** browser-game.game-core.filament

**Declared features:** World administration, Clock administration, Ruleset administration, Content version administration, Feature flag administration, Maintenance visibility, Scoped resource policies

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.1` |
| `liberusoftware/module-browser-game-game-core` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\BrowserGame\\GameCoreFilament\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-browser-game-game-core": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/GameCoreFilamentPlugin.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/GameCoreFilamentPlugin.php) · [src/GameCoreFilamentServiceProvider.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/GameCoreFilamentServiceProvider.php) · [src/Resources/GameClockResource.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameClockResource.php) · [src/Resources/GameClockResource/Pages/CreateGameClock.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameClockResource/Pages/CreateGameClock.php) · [src/Resources/GameClockResource/Pages/EditGameClock.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameClockResource/Pages/EditGameClock.php) · [src/Resources/GameClockResource/Pages/ListGameClocks.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameClockResource/Pages/ListGameClocks.php) · [src/Resources/GameContentVersionResource.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameContentVersionResource.php) · [src/Resources/GameContentVersionResource/Pages/CreateGameContentVersion.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameContentVersionResource/Pages/CreateGameContentVersion.php) · [src/Resources/GameContentVersionResource/Pages/EditGameContentVersion.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameContentVersionResource/Pages/EditGameContentVersion.php) · [src/Resources/GameContentVersionResource/Pages/ListGameContentVersions.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameContentVersionResource/Pages/ListGameContentVersions.php) · [src/Resources/GameFeatureFlagResource.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameFeatureFlagResource.php) · [src/Resources/GameFeatureFlagResource/Pages/CreateGameFeatureFlag.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameFeatureFlagResource/Pages/CreateGameFeatureFlag.php) · [src/Resources/GameFeatureFlagResource/Pages/EditGameFeatureFlag.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameFeatureFlagResource/Pages/EditGameFeatureFlag.php) · [src/Resources/GameFeatureFlagResource/Pages/ListGameFeatureFlags.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameFeatureFlagResource/Pages/ListGameFeatureFlags.php) · [src/Resources/GameMaintenanceStateResource.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameMaintenanceStateResource.php) · [src/Resources/GameMaintenanceStateResource/Pages/CreateGameMaintenanceState.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameMaintenanceStateResource/Pages/CreateGameMaintenanceState.php) · [src/Resources/GameMaintenanceStateResource/Pages/EditGameMaintenanceState.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameMaintenanceStateResource/Pages/EditGameMaintenanceState.php) · [src/Resources/GameMaintenanceStateResource/Pages/ListGameMaintenanceStates.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameMaintenanceStateResource/Pages/ListGameMaintenanceStates.php) · [src/Resources/GameRulesetResource.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameRulesetResource.php) · [src/Resources/GameRulesetResource/Pages/CreateGameRuleset.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameRulesetResource/Pages/CreateGameRuleset.php) · [src/Resources/GameRulesetResource/Pages/EditGameRuleset.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameRulesetResource/Pages/EditGameRuleset.php) · [src/Resources/GameRulesetResource/Pages/ListGameRulesets.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameRulesetResource/Pages/ListGameRulesets.php) · [src/Resources/GameWorldResource.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameWorldResource.php) · [src/Resources/GameWorldResource/Pages/CreateGameWorld.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameWorldResource/Pages/CreateGameWorld.php) · [src/Resources/GameWorldResource/Pages/EditGameWorld.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameWorldResource/Pages/EditGameWorld.php) · [src/Resources/GameWorldResource/Pages/ListGameWorlds.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/src/Resources/GameWorldResource/Pages/ListGameWorlds.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/tests/Pest.php)
- [tests/Unit/PackageBoundaryTest.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-filament/tests/Unit/PackageBoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
