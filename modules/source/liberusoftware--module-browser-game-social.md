# liberusoftware/module-browser-game-social: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral Browser Game Social capability.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [browser-game-social](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-browser-game-laravel-filament, `browser-game-social`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-browser-game-social` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `browser-game-social` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\BrowserGame\\Social\\SocialServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/composer.json) · [module.json](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/module.json).

**Declared capabilities:** browser-game.social

**Declared features:** Friends, parties, chat, and mail, Guilds, alliances, and permissions, Activity and reporting, Friend request lifecycle, Group membership lifecycle, Mail delivery lifecycle

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\BrowserGame\\Social\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Queries/SocialQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Queries/SocialQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |
| [src/Support/SocialManager.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Support/SocialManager.php) | `public function define(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null): SocialRecord`<br>`public function create(string $name, string $kind, string $ownerId, array $data = [], ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null, ?string $targetId = null): SocialRecord`<br>`public function createFriendRequest(string $actorId, string $targetId, ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): SocialRecord`<br>`public function respondToFriendRequest(SocialRecord $request, string $actorId, string $status): SocialRecord`<br>`public function createParty(string $ownerId, string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): SocialRecord`<br>`public function createChat(string $ownerId, string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): SocialRecord`<br>`public function createMail(string $ownerId, string $recipientId, string $body, ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): SocialRecord`<br>`public function createGuild(string $ownerId, string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): SocialRecord`<br>`public function createAlliance(string $ownerId, string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): SocialRecord`<br>`public function updatePermissions(SocialRecord $record, string $actorId, string $memberId, array $permissions): SocialMembership`<br>`public function recordActivity(string $actorId, string $kind, ?string $targetId = null, array $data = []): SocialActivity`<br>`public function addMember(SocialRecord $record, string $actorId, string $role = 'member', array $permissions = [], ?string $requestedBy = null): SocialMembership`<br>`public function send(string $actorId, SocialRecord $record, string $body): SocialRecord`<br>`public function report(string $actorId, string $targetId, string $reason, array $data = [], ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null): SocialRecord` |

Other non-legacy PHP sources: [src/Events/SocialDefined.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Events/SocialDefined.php) · [src/Models/SocialActivity.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Models/SocialActivity.php) · [src/Models/SocialMembership.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Models/SocialMembership.php) · [src/Models/SocialRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Models/SocialRecord.php) · [src/SocialServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/SocialServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_000505_create_browser_game_social_tables.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/database/migrations/2026_08_24_000505_create_browser_game_social_tables.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/tests/Pest.php)
- [tests/Unit/SocialBoundaryTest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/tests/Unit/SocialBoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
