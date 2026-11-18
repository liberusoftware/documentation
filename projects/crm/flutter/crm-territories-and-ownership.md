# Crm Territories And Ownership Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-territories-and-ownership). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-territories-and-ownership-flutter
**Matching core package:** module-crm-crm-territories-and-ownership ([implementation](../core/crm-territories-and-ownership.md))
**Matching API package:** module-crm-crm-territories-and-ownership-api ([contract](../api/crm-territories-and-ownership.md))

## Implementation plan

This adapter presents Crm Territories And Ownership for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Territories And Ownership API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/crm-territories-and-ownership.md), and [API module](../api/crm-territories-and-ownership.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `crm-territories-and-ownership`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-territories-and-ownership-flutter`](https://github.com/liberusoftware/module-crm-territories-and-ownership-flutter) (`module_crm_territories_and_ownership_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-territories-and-ownership-dart-mobile`](https://github.com/liberusoftware/module-crm-territories-and-ownership-dart-mobile) (`module_crm_territories_and_ownership_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-territories-and-ownership-dart-desktop`](https://github.com/liberusoftware/module-crm-territories-and-ownership-dart-desktop) (`module_crm_territories_and_ownership_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/crm-territories-and-ownership.md) · [Core plan](../core/crm-territories-and-ownership.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Territories** | Adaptive mobile cards/sheets for `territories` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `territories` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Books of business** | Adaptive mobile cards/sheets for `books of business` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `books of business` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Teams** | Adaptive mobile cards/sheets for `teams` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `teams` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Queues** | Adaptive mobile cards/sheets for `queues` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `queues` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Assignment rules** | Adaptive mobile cards/sheets for `assignment rules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `assignment rules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Round-robin/capacity routing** | Adaptive mobile cards/sheets for `round-robin/capacity routing` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `round-robin/capacity routing` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Temporary coverage** | Adaptive mobile cards/sheets for `temporary coverage` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `temporary coverage` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Ownership history** | Adaptive mobile cards/sheets for `ownership history` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `ownership history` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
