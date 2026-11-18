# Real Estate Core Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-real-estate-core-flutter
**Matching core package:** module-real-estate-real-estate-core ([implementation](../core/real-estate-core.md))
**Matching API package:** module-real-estate-real-estate-core-api ([contract](../api/real-estate-core.md))

## Implementation plan

This adapter presents Real Estate Core for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Real Estate Core API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/real-estate-core.md), and [API module](../api/real-estate-core.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `real-estate-core`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-real-estate-mobile-flutter`](https://github.com/liberusoftware/project-real-estate-mobile-flutter) | [`module-real-estate-core-flutter`](https://github.com/liberusoftware/module-real-estate-core-flutter) (`module_real_estate_core_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-real-estate-dart-mobile`](https://github.com/liberusoftware/project-real-estate-dart-mobile) | [`module-real-estate-core-dart-mobile`](https://github.com/liberusoftware/module-real-estate-core-dart-mobile) (`module_real_estate_core_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-real-estate-dart-desktop`](https://github.com/liberusoftware/project-real-estate-dart-desktop) | [`module-real-estate-core-dart-desktop`](https://github.com/liberusoftware/module-real-estate-core-dart-desktop) (`module_real_estate_core_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | [API plan](../api/real-estate-core.md) · [Core plan](../core/real-estate-core.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Agencies** | Adaptive mobile cards/sheets for `agencies` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `agencies` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Branches** | Adaptive mobile cards/sheets for `branches` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `branches` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Teams** | Adaptive mobile cards/sheets for `teams` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `teams` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Territories** | Adaptive mobile cards/sheets for `territories` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `territories` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Terminology** | Adaptive mobile cards/sheets for `terminology` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `terminology` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Statuses** | Adaptive mobile cards/sheets for `statuses` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `statuses` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Numbering** | Adaptive mobile cards/sheets for `numbering` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `numbering` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Audit** | Adaptive mobile cards/sheets for `audit` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `audit` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AgencyPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Policies/AgencyPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Agency $agency): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Agency $agency): bool`<br>`public function delete(AuthUser $authUser, Agency $agency): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Agency $agency): bool`<br>`public function forceDelete(AuthUser $authUser, Agency $agency): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Agency $agency): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [BranchPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Policies/BranchPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Branch $branch): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Branch $branch): bool`<br>`public function delete(AuthUser $authUser, Branch $branch): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Branch $branch): bool`<br>`public function forceDelete(AuthUser $authUser, Branch $branch): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Branch $branch): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [StatusDefinitionPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Policies/StatusDefinitionPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function delete(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function forceDelete(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [TerritoryPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Policies/TerritoryPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Territory $territory): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Territory $territory): bool`<br>`public function delete(AuthUser $authUser, Territory $territory): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Territory $territory): bool`<br>`public function forceDelete(AuthUser $authUser, Territory $territory): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Territory $territory): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Agency.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Agency.php) | No literal fillable array detected; inspect the model and API schema. |
| [AuditEntry.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/AuditEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [Branch.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Branch.php) | No literal fillable array detected; inspect the model and API schema. |
| [CalendarEntry.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/CalendarEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [Communication.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Communication.php) | No literal fillable array detected; inspect the model and API schema. |
| [NumberSequence.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/NumberSequence.php) | No literal fillable array detected; inspect the model and API schema. |
| [StatusDefinition.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/StatusDefinition.php) | No literal fillable array detected; inspect the model and API schema. |
| [Terminology.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Terminology.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [AgencyController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/AgencyController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateAgency $create): JsonResponse`<br>`public function show(Request $request, Agency $agency): JsonResponse`<br>`public function update(Request $request, Agency $agency, UpdateAgency $update): JsonResponse`<br>`public function destroy(Request $request, Agency $agency, DeleteAgency $delete): Response` |
| [BranchController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/BranchController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateBranch $create): JsonResponse`<br>`public function show(Request $request, Branch $branch): JsonResponse`<br>`public function update(Request $request, Branch $branch, UpdateBranch $update): JsonResponse`<br>`public function destroy(Request $request, Branch $branch, DeleteBranch $delete): Response` |
| [CalendarEntryController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/CalendarEntryController.php) | `public function store(Request $request, CreateCalendarEntry $create): JsonResponse`<br>`public function update(Request $request, CalendarEntry $calendarEntry): JsonResponse`<br>`public function destroy(Request $request, CalendarEntry $calendarEntry): Response` |
| [CommunicationController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/CommunicationController.php) | `public function store(Request $request, RecordCommunication $record): JsonResponse`<br>`public function update(Request $request, Communication $communication): JsonResponse`<br>`public function destroy(Request $request, Communication $communication): Response` |
| [CoreConfigurationController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/CoreConfigurationController.php) | `public function terminology(Request $request, string $key, SetTerminology $set): JsonResponse`<br>`public function status(Request $request, DefineStatus $define): JsonResponse`<br>`public function audit(Request $request, RecordAuditEntry $record): JsonResponse`<br>`public function list(Request $request, string $kind): JsonResponse` |
| [NumberingController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/NumberingController.php) | `public function next(Request $request, string $key, NextNumber $nextNumber): JsonResponse` |
| [PublicTerritoryController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/PublicTerritoryController.php) | `public function index(): JsonResponse` |
| [TerritoryController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/TerritoryController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateTerritory $create): JsonResponse`<br>`public function show(Request $request, Territory $territory): JsonResponse`<br>`public function update(Request $request, Territory $territory, UpdateTerritory $update): JsonResponse`<br>`public function destroy(Request $request, Territory $territory, DeleteTerritory $delete): Response` |

**Observed route declarations:**

[modules/real-estate-core-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/routes/api.php)

```php
Route::get('api/v1/public/territories', [PublicTerritoryController::class, 'index'])
Route::prefix('api/v1/real-estate/calendar-entries')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::post('/', [CalendarEntryController::class, 'store']);
Route::delete('/{calendarEntry}', [CalendarEntryController::class, 'destroy']);
Route::prefix('api/v1/real-estate/communications')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::post('/', [CommunicationController::class, 'store']);
Route::delete('/{communication}', [CommunicationController::class, 'destroy']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('api/v1/real-estate/core/{kind}', [CoreConfigurationController::class, 'list'])->whereIn('kind', ['terminology', 'statuses', 'audit']);
Route::put('api/v1/real-estate/core/terminology/{key}', [CoreConfigurationController::class, 'terminology']);
Route::post('api/v1/real-estate/core/statuses', [CoreConfigurationController::class, 'status']);
Route::post('api/v1/real-estate/core/audit', [CoreConfigurationController::class, 'audit']);
Route::post('api/v1/real-estate/numbering/{key}/next', [NumberingController::class, 'next'])
Route::prefix('api/v1/real-estate/branches')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [BranchController::class, 'index'])->name('real-estate.branches.index');
Route::post('/', [BranchController::class, 'store'])->name('real-estate.branches.store');
Route::get('/{branch}', [BranchController::class, 'show'])->name('real-estate.branches.show');
Route::delete('/{branch}', [BranchController::class, 'destroy'])->name('real-estate.branches.destroy');
Route::prefix('api/v1/real-estate/agencies')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [AgencyController::class, 'index']);
Route::post('/', [AgencyController::class, 'store']);
Route::get('/{agency}', [AgencyController::class, 'show']);
Route::delete('/{agency}', [AgencyController::class, 'destroy']);
Route::prefix('api/v1/real-estate/territories')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [TerritoryController::class, 'index']);
Route::post('/', [TerritoryController::class, 'store']);
Route::get('/{territory}', [TerritoryController::class, 'show']);
Route::delete('/{territory}', [TerritoryController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
