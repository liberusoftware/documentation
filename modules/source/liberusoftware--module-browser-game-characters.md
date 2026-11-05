# liberusoftware/module-browser-game-characters: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral Browser Game character creation, progression, skills, health, and respec.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [browser-game-characters](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 3 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-browser-game-laravel-filament, `browser-game-characters`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-browser-game-characters` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `browser-game-characters` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\BrowserGame\\Characters\\CharactersServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/composer.json) · [module.json](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/module.json).

**Declared capabilities:** browser-game.characters

**Declared features:** Character creation, Race class background, Statistics and skills, Experience and level, Health, Respec

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\BrowserGame\\Characters\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Policies/CharacterPolicy.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/src/Policies/CharacterPolicy.php) | `public function view(?string $actorId, ?string $teamId, GameCharacter $character): bool`<br>`public function manage(?string $actorId, ?string $teamId, GameCharacter $character): bool` |
| [src/Queries/CharacterQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/src/Queries/CharacterQuery.php) | `public function forPlayer(string $playerId, ?string $worldId = null): Builder`<br>`public function levelForExperience(int $experience): int` |
| [src/Support/CharactersManager.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/src/Support/CharactersManager.php) | `public function __construct(private readonly CharacterQuery $query)`<br>`public function create(string $playerId, string $name, string $race, string $class, ?string $background = null, array $statistics = [], array $skills = [], ?string $worldId = null, ?string $teamId = null, ?string $tenantId = null): GameCharacter`<br>`public function awardExperience(GameCharacter $character, int $amount, ?string $operationKey = null): GameCharacter`<br>`public function respec(GameCharacter $character, array $skills, ?string $operationKey = null): GameCharacter`<br>`public function spendStatPoints(GameCharacter $character, array $points): GameCharacter`<br>`public function allocateSkills(GameCharacter $character, array $skills, ?string $operationKey = null): GameCharacter`<br>`public function updateProfile(GameCharacter $character, string $name, string $race, string $class, ?string $background = null): GameCharacter`<br>`public function updateVitals(GameCharacter $character, int $health, int $mana): GameCharacter` |

Other non-legacy PHP sources: [src/CharactersServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/src/CharactersServiceProvider.php) · [src/Events/CharacterCreated.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/src/Events/CharacterCreated.php) · [src/Events/CharacterProgressed.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/src/Events/CharacterProgressed.php) · [src/Events/CharacterRespecced.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/src/Events/CharacterRespecced.php) · [src/Events/CharacterSkillsAllocated.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/src/Events/CharacterSkillsAllocated.php) · [src/Models/GameCharacter.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/src/Models/GameCharacter.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_000100_create_browser_game_characters_table.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/database/migrations/2026_08_24_000100_create_browser_game_characters_table.php)
- [database/migrations/2026_08_24_001200_add_character_operation_tracking.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/database/migrations/2026_08_24_001200_add_character_operation_tracking.php)
- [database/migrations/2026_08_25_000513_scope_character_identity.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/database/migrations/2026_08_25_000513_scope_character_identity.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **3**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/tests/Pest.php)
- [tests/Unit/CharacterBoundaryTest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/tests/Unit/CharacterBoundaryTest.php)
- [tests/Unit/CharactersBehaviorTest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/tests/Unit/CharactersBehaviorTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
