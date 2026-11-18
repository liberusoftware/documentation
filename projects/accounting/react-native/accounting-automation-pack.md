# Accounting Automation Pack React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-automation-pack). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-automation-pack-react-native
**Matching core package:** module-accounting-accounting-automation-pack ([implementation](../core/accounting-automation-pack.md))
**Matching API package:** module-accounting-accounting-automation-pack-api ([contract](../api/accounting-automation-pack.md))

## Implementation plan

This adapter presents Accounting Automation Pack for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Automation Pack API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-automation-pack.md), and [API module](../api/accounting-automation-pack.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-automation-pack`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-automation-pack.md)) |
| Capability React Native module skeleton | [`module-accounting-automation-pack-react-native`](https://github.com/liberusoftware/module-accounting-automation-pack-react-native) (`@liberusoftware/module-accounting-automation-pack-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Financial triggers/actions/recipes** | Progressive mobile list/detail/sheet flow for `financial triggers/actions/recipes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approvals** | Progressive mobile list/detail/sheet flow for `approvals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Schedules** | Progressive mobile list/detail/sheet flow for `schedules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Simulation** | Progressive mobile list/detail/sheet flow for `simulation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Idempotency** | Progressive mobile list/detail/sheet flow for `idempotency` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Generic Automation integration** | Progressive mobile list/detail/sheet flow for `generic automation integration` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAutomationRecipe.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-automation-pack/src/Actions/CreateAutomationRecipe.php) | `public function handle(array $attributes): AutomationRecipe` |
| [SimulateAutomationRecipe.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-automation-pack/src/Actions/SimulateAutomationRecipe.php) | `public function handle(AutomationRecipe $recipe, array $payload = []): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AutomationRecipe.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-automation-pack/src/Models/AutomationRecipe.php) | `team_id`, `name`, `trigger`, `action`, `schedule`, `status`, `idempotency_key`, `configuration` |

| Observed API controller | Handler signatures |
| --- | --- |
| [AutomationRecipeController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-automation-pack-api/src/Http/Controllers/AutomationRecipeController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateAutomationRecipe $action): mixed`<br>`public function simulate(Request $request, string $recipe, SimulateAutomationRecipe $action): mixed` |

**Observed route declarations:**

[modules/accounting-automation-pack-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-automation-pack-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/automation')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/recipes', [AutomationRecipeController::class, 'index'])->middleware('ability:accounting.automation-pack.read');
Route::post('/recipes', [AutomationRecipeController::class, 'store'])->middleware('ability:accounting.automation-pack.write');
Route::post('/recipes/{recipe}/simulate', [AutomationRecipeController::class, 'simulate'])->middleware('ability:accounting.automation-pack.read');
```
<!-- layer-implementation-plan:end -->
