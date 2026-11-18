# Crm Territories And Ownership React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-territories-and-ownership). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-territories-and-ownership-react-native
**Matching core package:** module-crm-crm-territories-and-ownership ([implementation](../core/crm-territories-and-ownership.md))
**Matching API package:** module-crm-crm-territories-and-ownership-api ([contract](../api/crm-territories-and-ownership.md))

## Implementation plan

This adapter presents Crm Territories And Ownership for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Territories And Ownership API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-territories-and-ownership.md), and [API module](../api/crm-territories-and-ownership.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-territories-and-ownership`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-territories-and-ownership.md)) |
| Capability React Native module skeleton | [`module-crm-territories-and-ownership-react-native`](https://github.com/liberusoftware/module-crm-territories-and-ownership-react-native) (`@liberusoftware/module-crm-territories-and-ownership-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Territories** | Progressive mobile list/detail/sheet flow for `territories` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Books of business** | Progressive mobile list/detail/sheet flow for `books of business` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Teams** | Progressive mobile list/detail/sheet flow for `teams` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Queues** | Progressive mobile list/detail/sheet flow for `queues` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Assignment rules** | Progressive mobile list/detail/sheet flow for `assignment rules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Round-robin/capacity routing** | Progressive mobile list/detail/sheet flow for `round-robin/capacity routing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Temporary coverage** | Progressive mobile list/detail/sheet flow for `temporary coverage` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Ownership history** | Progressive mobile list/detail/sheet flow for `ownership history` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [TerritoryQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Queries/TerritoryQuery.php) | `public function rules(int $teamId): LengthAwarePaginator`<br>`public function history(int $teamId): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AssignOwner.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Actions/AssignOwner.php) | `public function execute(int $teamId, int $actorId, string $subjectType, int $subjectId, ?int $previousOwnerId, int $ownerId, string $reason): OwnershipHistory` |
| [CreateCoverage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Actions/CreateCoverage.php) | `public function execute(int $teamId, int $actorId, array $data): TerritoryCoverage` |
| [UpsertTerritoryRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Actions/UpsertTerritoryRule.php) | `public function execute(int $teamId, int $actorId, array $data): TerritoryRule` |
| [TerritoryPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Services/TerritoryPolicy.php) | `public function canManage(int $teamId, int $userId): bool`<br>`public function isTeamMember(int $teamId, int $userId, array $roles = [], bool $includeOwner = false): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [OwnershipHistory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Models/OwnershipHistory.php) | `team_id`, `subject_type`, `subject_id`, `previous_owner_id`, `owner_id`, `reason`, `actor_id` |
| [TerritoryCoverage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Models/TerritoryCoverage.php) | `team_id`, `rule_id`, `covered_user_id`, `substitute_user_id`, `starts_at`, `ends_at` |
| [TerritoryRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Models/TerritoryRule.php) | `team_id`, `name`, `book_of_business`, `criteria`, `members`, `capacity`, `round_robin_cursor`, `active` |

| Observed API controller | Handler signatures |
| --- | --- |
| [TerritoryController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership-api/src/Http/Controllers/TerritoryController.php) | `public function index(Request $r, TerritoryQuery $q): JsonResponse`<br>`public function history(Request $r, TerritoryQuery $q): JsonResponse`<br>`public function store(Request $r, UpsertTerritoryRule $a): JsonResponse`<br>`public function assign(Request $r, AssignOwner $a): JsonResponse`<br>`public function coverage(Request $r, CreateCoverage $a): JsonResponse` |

**Observed route declarations:**

[modules/crm-territories-and-ownership-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/territories-and-ownership')->group(function () {
Route::get('/rules', [TerritoryController::class, 'index']);
Route::post('/rules', [TerritoryController::class, 'store']);
Route::post('/ownership', [TerritoryController::class, 'assign']);
Route::post('/coverage', [TerritoryController::class, 'coverage']);
Route::get('/history', [TerritoryController::class, 'history']);
```
<!-- layer-implementation-plan:end -->
