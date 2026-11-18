# Crm Sales Workspace Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-sales-workspace). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-sales-workspace-flutter
**Matching core package:** module-crm-crm-sales-workspace ([implementation](../core/crm-sales-workspace.md))
**Matching API package:** module-crm-crm-sales-workspace-api ([contract](../api/crm-sales-workspace.md))

## Implementation plan

This adapter presents Crm Sales Workspace for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Sales Workspace API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/crm-sales-workspace.md), and [API module](../api/crm-sales-workspace.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `crm-sales-workspace`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-sales-workspace-flutter`](https://github.com/liberusoftware/module-crm-sales-workspace-flutter) (`module_crm_sales_workspace_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-sales-workspace-dart-mobile`](https://github.com/liberusoftware/module-crm-sales-workspace-dart-mobile) (`module_crm_sales_workspace_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-sales-workspace-dart-desktop`](https://github.com/liberusoftware/module-crm-sales-workspace-dart-desktop) (`module_crm_sales_workspace_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/crm-sales-workspace.md) · [Core plan](../core/crm-sales-workspace.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Prioritized seller feed** | Adaptive mobile cards/sheets for `prioritized seller feed` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `prioritized seller feed` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Leads/deals inbox** | Adaptive mobile cards/sheets for `leads/deals inbox` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `leads/deals inbox` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Overdue/risk indicators** | Adaptive mobile cards/sheets for `overdue/risk indicators` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `overdue/risk indicators` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Next best action** | Adaptive mobile cards/sheets for `next best action` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `next best action` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Daily agenda** | Adaptive mobile cards/sheets for `daily agenda` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `daily agenda` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Quick updates** | Adaptive mobile cards/sheets for `quick updates` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `quick updates` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Contextual customer history** | Adaptive mobile cards/sheets for `contextual customer history` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `contextual customer history` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [WorkspaceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace/src/Queries/WorkspaceQuery.php) | `public function feed(int $teamId)`<br>`public function overdue(int $teamId)`<br>`public function agenda(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateWorkspaceItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace/src/Actions/CreateWorkspaceItem.php) | `public function execute(int $teamId, int $actorId, array $data): WorkspaceItem` |
| [QuickUpdate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace/src/Actions/QuickUpdate.php) | `public function execute(int $teamId, int $actorId, int $id, array $data): WorkspaceUpdate` |
| [WorkspacePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace/src/Services/WorkspacePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WorkspaceItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace/src/Models/WorkspaceItem.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkspaceUpdate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace/src/Models/WorkspaceUpdate.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [WorkspaceController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace-api/src/Http/Controllers/WorkspaceController.php) | `public function feed(Request $r, WorkspaceQuery $q)`<br>`public function overdue(Request $r, WorkspaceQuery $q)`<br>`public function agenda(Request $r, WorkspaceQuery $q)`<br>`public function store(Request $r, CreateWorkspaceItem $a)`<br>`public function update(Request $r, int $item, QuickUpdate $a)` |

**Observed route declarations:**

[modules/crm-sales-workspace-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/sales-workspace')->group(function (): void {
Route::get('/feed', [WorkspaceController::class, 'feed']);
Route::get('/overdue', [WorkspaceController::class, 'overdue']);
Route::get('/agenda', [WorkspaceController::class, 'agenda']);
Route::post('/items', [WorkspaceController::class, 'store']);
Route::patch('/items/{item}', [WorkspaceController::class, 'update']);
```
<!-- layer-implementation-plan:end -->
