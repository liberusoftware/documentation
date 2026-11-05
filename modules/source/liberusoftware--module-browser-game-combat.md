# liberusoftware/module-browser-game-combat: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral Browser Game combat turns, abilities, effects, cooldowns, enemies, loot, logs, and simulation.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [browser-game-combat](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-browser-game-laravel-filament, `browser-game-combat`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-browser-game-combat` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `browser-game-combat` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\BrowserGame\\Combat\\CombatServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/composer.json) · [module.json](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/module.json).

**Declared capabilities:** browser-game.combat

**Declared features:** Turn and action rules, Abilities and effects, Cooldowns and combatants, Loot and audit logs, Deterministic simulation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\BrowserGame\\Combat\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Policies/CombatPolicy.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Policies/CombatPolicy.php) | `public function view(mixed $user, CombatBattle $battle): bool`<br>`public function act(mixed $user, CombatBattle $battle): bool` |
| [src/Queries/CombatQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Queries/CombatQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |
| [src/Support/CombatManager.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Support/CombatManager.php) | `public function startPve(string $actorId, string $opponentId, ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null, array $state = []): CombatBattle`<br>`public function startPvp(string $actorId, string $opponentId, ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null, array $state = []): CombatBattle`<br>`public function defineAbility(string $slug, string $name, array $effects = [], array $data = [], int $cooldown = 0): CombatDefinition`<br>`public function defineEffect(string $slug, string $name, array $effects = [], array $data = [], int $cooldown = 0): CombatDefinition`<br>`public function defineEnemy(string $slug, string $name, array $effects = [], array $data = [], int $cooldown = 0): CombatDefinition`<br>`public function defineBoss(string $slug, string $name, array $effects = [], array $data = [], int $cooldown = 0): CombatDefinition`<br>`public function defineLoot(string $slug, string $name, array $effects = [], array $data = [], int $cooldown = 0): CombatDefinition`<br>`public function start(string $actorId, string $opponentId, ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null, array $state = []): CombatBattle`<br>`public function resolve(CombatBattle $battle, string $actorId, string $action, int $value = 0, ?string $idempotencyKey = null, array $effects = []): CombatAction`<br>`public function define(string $kind, string $slug, string $name, array $effects = [], array $data = [], int $cooldown = 0): CombatDefinition`<br>`public function simulate(string $actorId, string $opponentId, array $actions, array $state = []): array` |

Other non-legacy PHP sources: [src/CombatServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/CombatServiceProvider.php) · [src/Events/CombatActionResolved.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Events/CombatActionResolved.php) · [src/Events/CombatBattleCompleted.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Events/CombatBattleCompleted.php) · [src/Events/CombatBattleStarted.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Events/CombatBattleStarted.php) · [src/Events/CombatLootGranted.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Events/CombatLootGranted.php) · [src/Models/CombatAction.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Models/CombatAction.php) · [src/Models/CombatBattle.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Models/CombatBattle.php) · [src/Models/CombatDefinition.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Models/CombatDefinition.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_000300_create_browser_game_combat_tables.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/database/migrations/2026_08_24_000300_create_browser_game_combat_tables.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/tests/Pest.php)
- [tests/Unit/CombatBoundaryTest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/tests/Unit/CombatBoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
