# Multi Entity React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#multi-entity). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-multi-entity-react-native
**Matching core package:** module-accounting-multi-entity ([implementation](../core/multi-entity.md))
**Matching API package:** module-accounting-multi-entity-api ([contract](../api/multi-entity.md))

## Implementation plan

This adapter presents Multi Entity for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Multi Entity API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/multi-entity.md), and [API module](../api/multi-entity.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `multi-entity`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/multi-entity.md)) |
| Capability React Native module skeleton | [`module-accounting-multi-entity-react-native`](https://github.com/liberusoftware/module-accounting-multi-entity-react-native) (`@liberusoftware/module-accounting-multi-entity-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Entity books** | Progressive mobile list/detail/sheet flow for `entity books` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Shared master-data policy** | Progressive mobile list/detail/sheet flow for `shared master-data policy` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Access** | Progressive mobile list/detail/sheet flow for `access` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Entity switching** | Progressive mobile list/detail/sheet flow for `entity switching` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Separate periods/tax** | Progressive mobile list/detail/sheet flow for `separate periods/tax` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Standardized mappings** | Progressive mobile list/detail/sheet flow for `standardized mappings` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reporting** | Progressive mobile list/detail/sheet flow for `reporting` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EntityQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Queries/EntityQuery.php) | `public function paginate(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function report(EntityBook $entity): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateEntityBook.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Actions/CreateEntityBook.php) | `public function handle(array $attributes): EntityBook` |
| [CreateEntityMapping.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Actions/CreateEntityMapping.php) | `public function handle(EntityBook $entity, string $type, string $source, string $target): EntityMapping` |
| [CreateEntityPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Actions/CreateEntityPeriod.php) | `public function handle(EntityBook $entity, array $attributes): EntityPeriod` |
| [GrantEntityAccess.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Actions/GrantEntityAccess.php) | `public function handle(EntityBook $entity, string $userRef, string $role, array $permissions = [], bool $default = false): EntityAccess` |
| [SetMasterDataPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Actions/SetMasterDataPolicy.php) | `public function handle(EntityBook $entity, string $key, string $mode, array $configuration = []): MasterDataPolicy` |
| [SwitchEntity.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Actions/SwitchEntity.php) | `public function handle(EntityBook $entity, string $userRef, string $sessionRef): EntitySwitch` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EntityAccess.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Models/EntityAccess.php) | `entity_id`, `user_ref`, `role`, `permissions`, `is_default`, `metadata` |
| [EntityBook.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Models/EntityBook.php) | `team_id`, `entity_ref`, `code`, `name`, `base_currency`, `timezone`, `tax_registration`, `status`, `metadata` |
| [EntityMapping.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Models/EntityMapping.php) | `entity_id`, `mapping_type`, `source_ref`, `target_ref`, `description`, `is_active`, `metadata` |
| [EntityPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Models/EntityPeriod.php) | `entity_id`, `period_ref`, `starts_on`, `ends_on`, `tax_configuration`, `status`, `closed_by`, `closed_at`, `metadata` |
| [EntitySwitch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Models/EntitySwitch.php) | `entity_id`, `user_ref`, `session_ref`, `switched_at`, `metadata` |
| [MasterDataPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Models/MasterDataPolicy.php) | `entity_id`, `policy_key`, `mode`, `configuration`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MultiEntityController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity-api/src/Http/Controllers/MultiEntityController.php) | `public function index(Request $request, EntityQuery $query): mixed`<br>`public function store(Request $request, CreateEntityBook $action): JsonResponse`<br>`public function show(EntityBook $entityBook): EntityResource`<br>`public function access(Request $request, EntityBook $entityBook, GrantEntityAccess $action): JsonResponse`<br>`public function switch(Request $request, EntityBook $entityBook, SwitchEntity $action): JsonResponse`<br>`public function period(Request $request, EntityBook $entityBook, CreateEntityPeriod $action): JsonResponse`<br>`public function policy(Request $request, EntityBook $entityBook, SetMasterDataPolicy $action): JsonResponse`<br>`public function mapping(Request $request, EntityBook $entityBook, CreateEntityMapping $action): JsonResponse`<br>`public function report(EntityBook $entityBook, EntityQuery $query): array` |

**Observed route declarations:**

[modules/accounting-multi-entity-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/multi-entity')->group(function (): void {
Route::get('/', [MultiEntityController::class, 'index'])->name('accounting.multi-entity.list');
Route::post('/', [MultiEntityController::class, 'store'])->name('accounting.multi-entity.create');
Route::get('/{entityBook}', [MultiEntityController::class, 'show'])->name('accounting.multi-entity.show');
Route::post('/{entityBook}/access', [MultiEntityController::class, 'access'])->name('accounting.multi-entity.access');
Route::post('/{entityBook}/switch', [MultiEntityController::class, 'switch'])->name('accounting.multi-entity.switch');
Route::post('/{entityBook}/periods', [MultiEntityController::class, 'period'])->name('accounting.multi-entity.period');
Route::post('/{entityBook}/policy', [MultiEntityController::class, 'policy'])->name('accounting.multi-entity.policy');
Route::post('/{entityBook}/mappings', [MultiEntityController::class, 'mapping'])->name('accounting.multi-entity.mapping');
Route::get('/{entityBook}/report', [MultiEntityController::class, 'report'])->name('accounting.multi-entity.report');
```
<!-- layer-implementation-plan:end -->
