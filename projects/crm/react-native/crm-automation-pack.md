# Crm Automation Pack React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-automation-pack). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-automation-pack-react-native
**Matching core package:** module-crm-crm-automation-pack ([implementation](../core/crm-automation-pack.md))
**Matching API package:** module-crm-crm-automation-pack-api ([contract](../api/crm-automation-pack.md))

## Implementation plan

This adapter presents Crm Automation Pack for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Automation Pack API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-automation-pack.md), and [API module](../api/crm-automation-pack.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-automation-pack`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-automation-pack.md)) |
| Capability React Native module skeleton | [`module-crm-automation-pack-react-native`](https://github.com/liberusoftware/module-crm-automation-pack-react-native) (`@liberusoftware/module-crm-automation-pack-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **CRM triggers/actions/conditions** | Progressive mobile list/detail/sheet flow for `crm triggers/actions/conditions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Recipes** | Progressive mobile list/detail/sheet flow for `recipes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Enrollment history** | Progressive mobile list/detail/sheet flow for `enrollment history` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Versioning** | Progressive mobile list/detail/sheet flow for `versioning` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Simulation** | Progressive mobile list/detail/sheet flow for `simulation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approval gates** | Progressive mobile list/detail/sheet flow for `approval gates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Generic Automation module adapters** | Progressive mobile list/detail/sheet flow for `generic automation module adapters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AutomationPackQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Queries/AutomationPackQuery.php) | `public function recipes(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/ApproveAutomationRecipe.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AutomationRecipe $recipe, string $decision, ?string $reason = null): AutomationApproval` |
| [CreateAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/CreateAutomationRecipe.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): AutomationRecipe` |
| [EnrollSubject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/EnrollSubject.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AutomationRecipe $recipe, array $input): AutomationEnrollment` |
| [PublishAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/PublishAutomationRecipe.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AutomationRecipe $recipe): AutomationRecipe` |
| [SimulateAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/SimulateAutomationRecipe.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AutomationRecipe $recipe, array $input): AutomationRun` |
| [AutomationPackPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Services/AutomationPackPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AutomationApproval.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Models/AutomationApproval.php) | No literal fillable array detected; inspect the model and API schema. |
| [AutomationEnrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Models/AutomationEnrollment.php) | No literal fillable array detected; inspect the model and API schema. |
| [AutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Models/AutomationRecipe.php) | No literal fillable array detected; inspect the model and API schema. |
| [AutomationRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Models/AutomationRun.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [AutomationPackController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack-api/src/Http/Controllers/AutomationPackController.php) | `public function __construct(private readonly AutomationPackQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(CreateAutomationRecipe $action): JsonResponse`<br>`public function publish(AutomationRecipe $recipe, PublishAutomationRecipe $action): JsonResponse`<br>`public function simulate(AutomationRecipe $recipe, SimulateAutomationRecipe $action): JsonResponse`<br>`public function approve(AutomationRecipe $recipe, ApproveAutomationRecipe $action): JsonResponse`<br>`public function enroll(AutomationRecipe $recipe, EnrollSubject $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-automation-pack-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/crm-automation-pack')->group(function (): void {
Route::get('recipes', [AutomationPackController::class, 'index']);
Route::post('recipes', [AutomationPackController::class, 'store']);
Route::post('recipes/{recipe}/publish', [AutomationPackController::class, 'publish']);
Route::post('recipes/{recipe}/simulate', [AutomationPackController::class, 'simulate']);
Route::post('recipes/{recipe}/approve', [AutomationPackController::class, 'approve']);
Route::post('recipes/{recipe}/enroll', [AutomationPackController::class, 'enroll']);
```
<!-- layer-implementation-plan:end -->
