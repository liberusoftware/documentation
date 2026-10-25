# liberusoftware/module-browser-game-accounts: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral Browser Game Accounts capability.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [browser-game-accounts](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 3 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: browser-game-laravel, `browser-game-accounts`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-browser-game-accounts` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `browser-game-accounts` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\BrowserGame\\Accounts\\AccountsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/composer.json) · [module.json](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/module.json).

**Declared capabilities:** browser-game.accounts

**Declared features:** Player identity and lifecycle, Sessions and recovery, Age and region policy, Bans and privacy controls, Tenant-scoped audit events

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\BrowserGame\\Accounts\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Queries/AccountsQuery.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Queries/AccountsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |
| [src/Support/AccountsManager.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Support/AccountsManager.php) | `public function define(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null): AccountsRecord`<br>`public function updateIdentity(AccountsRecord $account, string $name, ?string $email = null, ?string $username = null): AccountsRecord`<br>`public function verifyEmail(AccountsRecord $account): AccountsRecord`<br>`public function setAgeRegionPolicy(AccountsRecord $account, ?int $birthYear, ?string $region, bool $verified): AccountsRecord`<br>`public function suspend(AccountsRecord $account, ?string $actorId = null): AccountsRecord`<br>`public function close(AccountsRecord $account, ?string $actorId = null): AccountsRecord`<br>`public function reactivate(AccountsRecord $account, ?string $actorId = null): AccountsRecord`<br>`public function createSession(AccountsRecord $account, ?string $ipAddress = null, ?string $userAgent = null, ?int $days = 30): array`<br>`public function revokeSession(AccountsRecord $account, AccountSession\|int $session, ?string $actorId = null): AccountSession`<br>`public function revokeAllSessions(AccountsRecord $account, ?string $actorId = null): int`<br>`public function issueRecovery(AccountsRecord $account, int $minutes = 30): array`<br>`public function consumeRecovery(string $token): ?AccountsRecord`<br>`public function resolveSession(string $token): ?AccountSession`<br>`public function ban(AccountsRecord $account, string $reason, ?string $endsAt = null, ?string $actorId = null): AccountBan`<br>`public function liftBan(AccountsRecord $account, AccountBan\|int $ban, ?string $actorId = null): AccountBan`<br>`public function isBanned(AccountsRecord $account): bool`<br>`public function updatePrivacy(AccountsRecord $account, string $visibility, bool $marketing, bool $analytics): AccountPrivacy`<br>`public function requestDeletion(AccountsRecord $account): AccountPrivacy`<br>`public function completeDeletion(AccountsRecord $account, ?string $actorId = null): AccountPrivacy` |

Other non-legacy PHP sources: [src/AccountsServiceProvider.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/AccountsServiceProvider.php) · [src/Events/AccountBanChanged.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Events/AccountBanChanged.php) · [src/Events/AccountEmailVerified.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Events/AccountEmailVerified.php) · [src/Events/AccountLifecycleChanged.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Events/AccountLifecycleChanged.php) · [src/Events/AccountRecoveryIssued.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Events/AccountRecoveryIssued.php) · [src/Events/AccountSessionRevoked.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Events/AccountSessionRevoked.php) · [src/Events/AccountsDefined.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Events/AccountsDefined.php) · [src/Models/AccountBan.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Models/AccountBan.php) · [src/Models/AccountPrivacy.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Models/AccountPrivacy.php) · [src/Models/AccountRecovery.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Models/AccountRecovery.php) · [src/Models/AccountSession.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Models/AccountSession.php) · [src/Models/AccountsRecord.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/src/Models/AccountsRecord.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_000501_create_browser_game_accounts_tables.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/database/migrations/2026_08_24_000501_create_browser_game_accounts_tables.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **3**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/tests/Pest.php)
- [tests/Unit/AccountsBehaviorTest.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/tests/Unit/AccountsBehaviorTest.php)
- [tests/Unit/AccountsBoundaryTest.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts/tests/Unit/AccountsBoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
