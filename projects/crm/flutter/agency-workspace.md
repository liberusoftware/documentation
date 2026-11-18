# Agency Workspace Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#agency-workspace). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-agency-workspace-flutter
**Matching core package:** module-crm-agency-workspace ([implementation](../core/agency-workspace.md))
**Matching API package:** module-crm-agency-workspace-api ([contract](../api/agency-workspace.md))

## Implementation plan

This adapter presents Agency Workspace for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Agency Workspace API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/agency-workspace.md), and [API module](../api/agency-workspace.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `agency-workspace`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-agency-workspace-flutter`](https://github.com/liberusoftware/module-crm-agency-workspace-flutter) (`module_crm_agency_workspace_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-agency-workspace-dart-mobile`](https://github.com/liberusoftware/module-crm-agency-workspace-dart-mobile) (`module_crm_agency_workspace_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-agency-workspace-dart-desktop`](https://github.com/liberusoftware/module-crm-agency-workspace-dart-desktop) (`module_crm_agency_workspace_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/agency-workspace.md) · [Core plan](../core/agency-workspace.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Agency/client hierarchy** | Adaptive mobile cards/sheets for `agency/client hierarchy` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `agency/client hierarchy` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Sub-accounts** | Adaptive mobile cards/sheets for `sub-accounts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `sub-accounts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Delegated administration** | Adaptive mobile cards/sheets for `delegated administration` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `delegated administration` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Usage visibility** | Adaptive mobile cards/sheets for `usage visibility` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `usage visibility` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Support access** | Adaptive mobile cards/sheets for `support access` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `support access` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Branding** | Adaptive mobile cards/sheets for `branding` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `branding` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Cross-account operations** | Adaptive mobile cards/sheets for `cross-account operations` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `cross-account operations` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AgencyQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Queries/AgencyQuery.php) | `public function accounts(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAgencyAccount.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Actions/CreateAgencyAccount.php) | `public function execute(int $teamId, int $ownerId, array $input): AgencyAccount` |
| [GrantAgencyAccess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Actions/GrantAgencyAccess.php) | `public function execute(int $teamId, int $actorId, AgencyAccount $account, array $input): AgencyAccess` |
| [UpdateAgencyUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Actions/UpdateAgencyUsage.php) | `public function execute(int $teamId, int $actorId, AgencyAccount $account, array $input): AgencyAccount` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AgencyAccess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Models/AgencyAccess.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgencyAccount.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Models/AgencyAccount.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgencyAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Models/AgencyAudit.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [AgencyWorkspaceController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace-api/src/Http/Controllers/AgencyWorkspaceController.php) | `public function __construct(private readonly AgencyQuery $query)`<br>`public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateAgencyAccount $action): JsonResponse`<br>`public function grantAccess(Request $request, AgencyAccount $account, GrantAgencyAccess $action): JsonResponse`<br>`public function usage(Request $request, AgencyAccount $account, UpdateAgencyUsage $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-agency-workspace-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/agency-workspace')->group(function (): void {
Route::get('accounts', [AgencyWorkspaceController::class, 'index']);
Route::post('accounts', [AgencyWorkspaceController::class, 'store']);
Route::post('accounts/{account}/access', [AgencyWorkspaceController::class, 'grantAccess']);
Route::post('accounts/{account}/usage', [AgencyWorkspaceController::class, 'usage']);
```
<!-- layer-implementation-plan:end -->
