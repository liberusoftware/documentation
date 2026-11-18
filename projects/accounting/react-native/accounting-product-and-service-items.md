# Accounting Product And Service Items React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-product-and-service-items). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-product-and-service-items-react-native
**Matching core package:** module-accounting-accounting-product-and-service-items ([implementation](../core/accounting-product-and-service-items.md))
**Matching API package:** module-accounting-accounting-product-and-service-items-api ([contract](../api/accounting-product-and-service-items.md))

## Implementation plan

This adapter presents Accounting Product And Service Items for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Product And Service Items API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-product-and-service-items.md), and [API module](../api/accounting-product-and-service-items.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-product-and-service-items`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-product-and-service-items.md)) |
| Capability React Native module skeleton | [`module-accounting-product-and-service-items-react-native`](https://github.com/liberusoftware/module-accounting-product-and-service-items-react-native) (`@liberusoftware/module-accounting-product-and-service-items-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Items/services** | Progressive mobile list/detail/sheet flow for `items/services` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Codes** | Progressive mobile list/detail/sheet flow for `codes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Purchase/sales descriptions** | Progressive mobile list/detail/sheet flow for `purchase/sales descriptions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Accounts** | Progressive mobile list/detail/sheet flow for `accounts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tax defaults** | Progressive mobile list/detail/sheet flow for `tax defaults` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Units** | Progressive mobile list/detail/sheet flow for `units` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Costs/prices** | Progressive mobile list/detail/sheet flow for `costs/prices` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Ecommerce references** | Progressive mobile list/detail/sheet flow for `ecommerce references` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [FindAccountingItems.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items/src/Queries/FindAccountingItems.php) | `public function search(?string $term = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SaveAccountingItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items/src/Actions/SaveAccountingItem.php) | `public function handle(array $attributes): AccountingItem` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccountingItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items/src/Models/AccountingItem.php) | `team_id`, `code`, `name`, `kind`, `purchase_description`, `sales_description`, `sales_account_ref`, `purchase_account_ref`, `tax_default_ref`, `unit`, `purchase_price`, `sales_price`, `currency`, `status`, `ecommerce_refs`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProductAndServiceItemsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items-api/src/Http/Controllers/ProductAndServiceItemsController.php) | `public function index(Request $request, FindAccountingItems $query): AnonymousResourceCollection`<br>`public function store(Request $request, SaveAccountingItem $action): JsonResponse`<br>`public function show(Request $request, AccountingItem $accountingItem): AccountingItemResource` |

**Observed route declarations:**

[modules/accounting-product-and-service-items-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/product-and-service-items')->group(function (): void {
Route::middleware('ability:accounting.product-and-service-items.read')->group(function (): void {
Route::get('/', [ProductAndServiceItemsController::class, 'index']);
Route::get('/{accountingItem}', [ProductAndServiceItemsController::class, 'show']);
Route::post('/', [ProductAndServiceItemsController::class, 'store'])->middleware('ability:accounting.product-and-service-items.write');
```
<!-- layer-implementation-plan:end -->
