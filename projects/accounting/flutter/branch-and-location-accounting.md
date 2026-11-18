# Branch And Location Accounting Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#branch-and-location-accounting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-branch-and-location-accounting-flutter
**Matching core package:** module-accounting-branch-and-location-accounting ([implementation](../core/branch-and-location-accounting.md))
**Matching API package:** module-accounting-branch-and-location-accounting-api ([contract](../api/branch-and-location-accounting.md))

## Implementation plan

This adapter presents Branch And Location Accounting for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Branch And Location Accounting API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/branch-and-location-accounting.md), and [API module](../api/branch-and-location-accounting.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `branch-and-location-accounting`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-branch-and-location-accounting-flutter`](https://github.com/liberusoftware/module-accounting-branch-and-location-accounting-flutter) (`module_accounting_branch_and_location_accounting_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-branch-and-location-accounting-dart-mobile`](https://github.com/liberusoftware/module-accounting-branch-and-location-accounting-dart-mobile) (`module_accounting_branch_and_location_accounting_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-branch-and-location-accounting-dart-desktop`](https://github.com/liberusoftware/module-accounting-branch-and-location-accounting-dart-desktop) (`module_accounting_branch_and_location_accounting_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/branch-and-location-accounting.md) · [Core plan](../core/branch-and-location-accounting.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Branch/location dimensions or books** | Adaptive mobile cards/sheets for `branch/location dimensions or books` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `branch/location dimensions or books` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Local sequences/tax** | Adaptive mobile cards/sheets for `local sequences/tax` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `local sequences/tax` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Allocations** | Adaptive mobile cards/sheets for `allocations` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `allocations` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Performance** | Adaptive mobile cards/sheets for `performance` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `performance` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Statutory requirements** | Adaptive mobile cards/sheets for `statutory requirements` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `statutory requirements` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [BranchQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting/src/Queries/BranchQuery.php) | `public function forTeam(int $teamId, ?string $status = null): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocateBranchValue.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting/src/Actions/AllocateBranchValue.php) | `public function handle(Branch $branch, float $amount): array` |
| [CreateBranch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting/src/Actions/CreateBranch.php) | `public function handle(array $attributes): Branch` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Branch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting/src/Models/Branch.php) | `team_id`, `code`, `name`, `location`, `local_tax_code`, `sequence_prefix`, `allocation_rule`, `performance_target`, `statutory_reference`, `status`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [BranchController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting-api/src/Http/Controllers/BranchController.php) | `public function index(Request $request, BranchQuery $query): mixed`<br>`public function store(Request $request, CreateBranch $action): mixed`<br>`public function allocate(Request $request, string $branch, AllocateBranchValue $action): mixed` |

**Observed route declarations:**

[modules/accounting-branch-and-location-accounting-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/branches')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [BranchController::class, 'index'])->middleware('ability:accounting.branch-and-location-accounting.read');
Route::post('/', [BranchController::class, 'store'])->middleware('ability:accounting.branch-and-location-accounting.write');
Route::post('/{branch}/allocate', [BranchController::class, 'allocate'])->middleware('ability:accounting.branch-and-location-accounting.write');
```
<!-- layer-implementation-plan:end -->
