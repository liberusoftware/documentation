# liberusoftware/module-browser-game-accounts-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

HTTP API adapter for Browser Game Accounts.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [browser-game-accounts-api](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts-api/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-browser-game-laravel-filament, `browser-game-accounts-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-browser-game-accounts-api` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `browser-game-accounts-api` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\BrowserGame\\AccountsApi\\AccountsApiServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts-api/composer.json) · [module.json](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts-api/module.json).

**Declared capabilities:** browser-game.accounts.api

**Declared features:** Account catalog, Progress actions, OpenAPI contract

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/routing` | `^13.0` |
| `liberusoftware/module-browser-game-accounts` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\BrowserGame\\AccountsApi\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-browser-game-accounts": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/AccountsController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts-api/src/Http/Controllers/AccountsController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function show(Request $request, AccountsRecord $account): JsonResponse`<br>`public function update(Request $request, AccountsRecord $account): JsonResponse`<br>`public function ageRegion(Request $request, AccountsRecord $account): JsonResponse`<br>`public function verifyEmail(Request $request, AccountsRecord $account): JsonResponse`<br>`public function suspend(Request $request, AccountsRecord $account): JsonResponse`<br>`public function reactivate(Request $request, AccountsRecord $account): JsonResponse`<br>`public function ban(Request $request, AccountsRecord $account): JsonResponse`<br>`public function liftBan(Request $request, AccountsRecord $account, AccountBan $ban): JsonResponse`<br>`public function privacy(Request $request, AccountsRecord $account): JsonResponse`<br>`public function requestDeletion(Request $request, AccountsRecord $account): JsonResponse`<br>`public function completeDeletion(Request $request, AccountsRecord $account): JsonResponse`<br>`public function revokeSession(Request $request, AccountsRecord $account, AccountSession $session): JsonResponse`<br>`public function sessions(Request $request, AccountsRecord $account): JsonResponse`<br>`public function revokeAllSessions(Request $request, AccountsRecord $account): JsonResponse`<br>`public function issueRecovery(Request $request, AccountsRecord $account): JsonResponse`<br>`public function consumeRecovery(Request $request): JsonResponse` |

Other non-legacy PHP sources: [src/AccountsApiServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts-api/src/AccountsApiServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1-browser-game-accounts.yaml](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts-api/openapi/v1-browser-game-accounts.yaml)
- [routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts-api/tests/Pest.php)
- [tests/Unit/PackageBoundaryTest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-accounts-api/tests/Unit/PackageBoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
