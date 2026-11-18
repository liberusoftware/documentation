# Maintenance Core Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#maintenance-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-maintenance-maintenance-core-flutter
**Matching core package:** module-maintenance-maintenance-core ([implementation](../core/maintenance-core.md))
**Matching API package:** module-maintenance-maintenance-core-api ([contract](../api/maintenance-core.md))

## Implementation plan

This adapter presents Maintenance Core for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Maintenance Core API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/maintenance-core.md), and [API module](../api/maintenance-core.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `maintenance-core`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-maintenance-mobile-flutter`](https://github.com/liberusoftware/project-maintenance-mobile-flutter) | [`module-maintenance-maintenance-core-flutter`](https://github.com/liberusoftware/module-maintenance-maintenance-core-flutter) (`module_maintenance_maintenance_core_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-maintenance-dart-mobile`](https://github.com/liberusoftware/project-maintenance-dart-mobile) | [`module-maintenance-maintenance-core-dart-mobile`](https://github.com/liberusoftware/module-maintenance-maintenance-core-dart-mobile) (`module_maintenance_maintenance_core_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-maintenance-dart-desktop`](https://github.com/liberusoftware/project-maintenance-dart-desktop) | [`module-maintenance-maintenance-core-dart-desktop`](https://github.com/liberusoftware/module-maintenance-maintenance-core-dart-desktop) (`module_maintenance_maintenance_core_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | [API plan](../api/maintenance-core.md) · [Core plan](../core/maintenance-core.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Organizations** | Adaptive mobile cards/sheets for `organizations` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `organizations` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Service settings** | Adaptive mobile cards/sheets for `service settings` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `service settings` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Statuses** | Adaptive mobile cards/sheets for `statuses` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `statuses` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Numbering** | Adaptive mobile cards/sheets for `numbering` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `numbering` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Priorities** | Adaptive mobile cards/sheets for `priorities` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `priorities` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Shared events** | Adaptive mobile cards/sheets for `shared events` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `shared events` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfigureNumbering.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/ConfigureNumbering.php) | `public function execute(int $teamId, string $documentType, string $prefix, int $padding = 6): NumberingSequence` |
| [CreateOrganization.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/CreateOrganization.php) | `public function execute(int $teamId, string $name, string $code, ?string $description = null): Organization` |
| [CreatePriority.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/CreatePriority.php) | `public function execute(int $teamId, array $attributes): Priority` |
| [CreateStatus.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/CreateStatus.php) | `public function execute(int $teamId, array $attributes): Status` |
| [DeleteOrganization.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/DeleteOrganization.php) | `public function execute(Organization $organization): void` |
| [DeletePriority.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/DeletePriority.php) | `public function execute(Priority $priority): void` |
| [DeleteServiceSetting.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/DeleteServiceSetting.php) | `public function execute(ServiceSetting $setting): void` |
| [DeleteStatus.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/DeleteStatus.php) | `public function execute(Status $status): void` |
| [IssueNumber.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/IssueNumber.php) | `public function execute(int $teamId, string $documentType): string` |
| [SetServiceSetting.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/SetServiceSetting.php) | `public function execute(int $teamId, string $key, ?string $value, bool $encrypted = false): ServiceSetting` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [NumberingSequence.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Models/NumberingSequence.php) | `team_id`, `document_type`, `prefix`, `next_number`, `padding` |
| [Organization.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Models/Organization.php) | `team_id`, `name`, `code`, `description`, `state` |
| [Priority.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Models/Priority.php) | `team_id`, `name`, `code`, `color`, `sort_order`, `is_default`, `is_active` |
| [ServiceSetting.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Models/ServiceSetting.php) | `team_id`, `key`, `value`, `is_encrypted` |
| [Status.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Models/Status.php) | `team_id`, `name`, `code`, `color`, `sort_order`, `is_default`, `is_active` |

| Observed API controller | Handler signatures |
| --- | --- |
| [NumberingController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-api/src/Http/Controllers/NumberingController.php) | `public function configure(Request $request, ConfigureNumbering $configure): JsonResponse`<br>`public function issue(Request $request, IssueNumber $issue): JsonResponse` |
| [OrganizationController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-api/src/Http/Controllers/OrganizationController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateOrganization $create): JsonResponse`<br>`public function show(Request $request, Organization $organization): JsonResponse`<br>`public function update(Request $request, Organization $organization, UpdateOrganization $update): JsonResponse`<br>`public function destroy(Request $request, Organization $organization, DeleteOrganization $delete): Response` |
| [PriorityController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-api/src/Http/Controllers/PriorityController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreatePriority $create): JsonResponse`<br>`public function update(Request $request, Priority $priority, UpdatePriority $update): JsonResponse`<br>`public function destroy(Request $request, Priority $priority, DeletePriority $delete): Response` |
| [ServiceSettingController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-api/src/Http/Controllers/ServiceSettingController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, SetServiceSetting $set): JsonResponse` |
| [StatusController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-api/src/Http/Controllers/StatusController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateStatus $create): JsonResponse`<br>`public function update(Request $request, Status $status, UpdateStatus $update): JsonResponse`<br>`public function destroy(Request $request, Status $status, DeleteStatus $delete): Response` |

**Observed route declarations:**

[modules/module-maintenance-core-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-api/routes/api.php)

```php
Route::middleware('api')
Route::middleware('auth:sanctum')->group(function (): void {
Route::get('organizations', [OrganizationController::class, 'index'])->name('organizations.index');
Route::post('organizations', [OrganizationController::class, 'store'])->name('organizations.store');
Route::get('organizations/{organization}', [OrganizationController::class, 'show'])->name('organizations.show');
Route::patch('organizations/{organization}', [OrganizationController::class, 'update'])->name('organizations.update');
Route::delete('organizations/{organization}', [OrganizationController::class, 'destroy'])->name('organizations.destroy');
Route::get('statuses', [StatusController::class, 'index'])->name('statuses.index');
Route::post('statuses', [StatusController::class, 'store'])->name('statuses.store');
Route::patch('statuses/{status}', [StatusController::class, 'update'])->name('statuses.update');
Route::delete('statuses/{status}', [StatusController::class, 'destroy'])->name('statuses.destroy');
Route::get('priorities', [PriorityController::class, 'index'])->name('priorities.index');
Route::post('priorities', [PriorityController::class, 'store'])->name('priorities.store');
Route::patch('priorities/{priority}', [PriorityController::class, 'update'])->name('priorities.update');
Route::delete('priorities/{priority}', [PriorityController::class, 'destroy'])->name('priorities.destroy');
Route::get('settings', [ServiceSettingController::class, 'index'])->name('settings.index');
Route::post('settings', [ServiceSettingController::class, 'store'])->name('settings.store');
Route::post('numbering/configure', [NumberingController::class, 'configure'])->name('numbering.configure');
Route::post('numbering/issue', [NumberingController::class, 'issue'])->name('numbering.issue');
```
<!-- layer-implementation-plan:end -->
