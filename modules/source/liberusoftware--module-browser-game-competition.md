# liberusoftware/module-browser-game-competition: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral Browser Game Competition capability.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [browser-game-competition](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: browser-game-laravel, `browser-game-competition`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-browser-game-competition` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `browser-game-competition` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\BrowserGame\\Competition\\CompetitionServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/composer.json) · [module.json](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/module.json).

**Declared capabilities:** browser-game.competition

**Declared features:** PvP modes and matchmaking, Seasons, rankings, and leaderboards, Rewards and anti-collusion evidence

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\BrowserGame\\Competition\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Queries/CompetitionQuery.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Queries/CompetitionQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |
| [src/Support/CompetitionManager.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Support/CompetitionManager.php) | `public function define(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null): CompetitionRecord`<br>`public function create(string $name, string $kind = 'pvp', array $data = [], ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): CompetitionRecord`<br>`public function createPvp(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): CompetitionRecord`<br>`public function createMatchmaking(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): CompetitionRecord`<br>`public function createSeason(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): CompetitionRecord`<br>`public function createLeaderboard(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): CompetitionRecord`<br>`public function queue(CompetitionRecord $competition, string $actorId): CompetitionEntry`<br>`public function match(CompetitionRecord $competition, string $playerA, string $playerB, ?string $idempotencyKey = null): CompetitionMatch`<br>`public function resolve(CompetitionMatch $match, string $winnerId, array $evidence = []): CompetitionMatch`<br>`public function leaderboard(CompetitionRecord $competition, int $limit = 100): Collection`<br>`public function claimReward(string $actorId, CompetitionReward\|int $reward): CompetitionReward`<br>`public function flagCollusion(CompetitionRecord $competition, string $actorId, string $reason, ?CompetitionMatch $match = null): CompetitionFlag` |

Other non-legacy PHP sources: [src/CompetitionServiceProvider.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/CompetitionServiceProvider.php) · [src/Events/CompetitionCollusionFlagged.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Events/CompetitionCollusionFlagged.php) · [src/Events/CompetitionDefined.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Events/CompetitionDefined.php) · [src/Events/CompetitionMatchResolved.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Events/CompetitionMatchResolved.php) · [src/Events/CompetitionRewardGranted.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Events/CompetitionRewardGranted.php) · [src/Models/CompetitionEntry.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Models/CompetitionEntry.php) · [src/Models/CompetitionFlag.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Models/CompetitionFlag.php) · [src/Models/CompetitionMatch.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Models/CompetitionMatch.php) · [src/Models/CompetitionRecord.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Models/CompetitionRecord.php) · [src/Models/CompetitionReward.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Models/CompetitionReward.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_000506_create_browser_game_competition_tables.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/database/migrations/2026_08_24_000506_create_browser_game_competition_tables.php)
- [database/migrations/2026_08_24_001300_add_competition_rewards_and_flags.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/database/migrations/2026_08_24_001300_add_competition_rewards_and_flags.php)
- [database/migrations/2026_08_25_000515_scope_match_idempotency.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/database/migrations/2026_08_25_000515_scope_match_idempotency.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/tests/Pest.php)
- [tests/Unit/CompetitionBoundaryTest.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/tests/Unit/CompetitionBoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
