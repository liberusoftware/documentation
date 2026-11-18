# Sales Workspace React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sales-workspace). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-sales-workspace-react-native
**Matching core package:** module-crm-sales-workspace ([implementation](../core/sales-workspace.md))
**Matching API package:** module-crm-sales-workspace-api ([contract](../api/sales-workspace.md))

## Implementation plan

This adapter presents Sales Workspace for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Sales Workspace API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/sales-workspace.md), and [API module](../api/sales-workspace.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `sales-workspace`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/sales-workspace.md)) |
| Capability React Native module skeleton | [`module-crm-sales-workspace-react-native`](https://github.com/liberusoftware/module-crm-sales-workspace-react-native) (`@liberusoftware/module-crm-sales-workspace-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Prioritized seller feed** | Progressive mobile list/detail/sheet flow for `prioritized seller feed` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Leads/deals inbox** | Progressive mobile list/detail/sheet flow for `leads/deals inbox` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Overdue/risk indicators** | Progressive mobile list/detail/sheet flow for `overdue/risk indicators` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Next best action** | Progressive mobile list/detail/sheet flow for `next best action` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Daily agenda** | Progressive mobile list/detail/sheet flow for `daily agenda` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Quick updates** | Progressive mobile list/detail/sheet flow for `quick updates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Contextual customer history** | Progressive mobile list/detail/sheet flow for `contextual customer history` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
