# Crm Agency Workspace React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-agency-workspace). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-agency-workspace-react-native
**Matching core package:** module-crm-crm-agency-workspace ([implementation](../core/crm-agency-workspace.md))
**Matching API package:** module-crm-crm-agency-workspace-api ([contract](../api/crm-agency-workspace.md))

## Implementation plan

This adapter presents Crm Agency Workspace for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Agency Workspace API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-agency-workspace.md), and [API module](../api/crm-agency-workspace.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-agency-workspace`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-agency-workspace.md)) |
| Capability React Native module skeleton | [`module-crm-agency-workspace-react-native`](https://github.com/liberusoftware/module-crm-agency-workspace-react-native) (`@liberusoftware/module-crm-agency-workspace-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Agency/client hierarchy** | Progressive mobile list/detail/sheet flow for `agency/client hierarchy` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Sub-accounts** | Progressive mobile list/detail/sheet flow for `sub-accounts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Delegated administration** | Progressive mobile list/detail/sheet flow for `delegated administration` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Usage visibility** | Progressive mobile list/detail/sheet flow for `usage visibility` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Support access** | Progressive mobile list/detail/sheet flow for `support access` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Branding** | Progressive mobile list/detail/sheet flow for `branding` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Cross-account operations** | Progressive mobile list/detail/sheet flow for `cross-account operations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
