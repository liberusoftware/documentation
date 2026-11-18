# Module Maintenance Customers And Sites React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-maintenance-customers-and-sites). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-maintenance-module-maintenance-customers-and-sites-react-native
**Matching core package:** module-maintenance-module-maintenance-customers-and-sites ([implementation](../core/module-maintenance-customers-and-sites.md))
**Matching API package:** module-maintenance-module-maintenance-customers-and-sites-api ([contract](../api/module-maintenance-customers-and-sites.md))

## Implementation plan

This adapter presents Module Maintenance Customers And Sites for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Maintenance Customers And Sites API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/module-maintenance-customers-and-sites.md), and [API module](../api/module-maintenance-customers-and-sites.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `module-maintenance-customers-and-sites`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-maintenance-mobile-react`](https://github.com/liberusoftware/project-maintenance-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-maintenance-customers-and-sites.md)) |
| Capability React Native module skeleton | [`module-maintenance-customers-and-sites-react-native`](https://github.com/liberusoftware/module-maintenance-customers-and-sites-react-native) (`@liberusoftware/module-maintenance-customers-and-sites-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Customers** | Progressive mobile list/detail/sheet flow for `customers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Contacts** | Progressive mobile list/detail/sheet flow for `contacts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Sites** | Progressive mobile list/detail/sheet flow for `sites` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Locations** | Progressive mobile list/detail/sheet flow for `locations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Access details** | Progressive mobile list/detail/sheet flow for `access details` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Hazards** | Progressive mobile list/detail/sheet flow for `hazards` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Service windows** | Progressive mobile list/detail/sheet flow for `service windows` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCustomer.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/CreateCustomer.php) | `public function handle(int $teamId, array $attributes): Customer` |
| [CreateSite.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/CreateSite.php) | `public function handle(int $teamId, array $attributes): Site` |
| [DeleteCustomer.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/DeleteCustomer.php) | `public function handle(int $teamId, Customer $customer): void` |
| [DeleteSite.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/DeleteSite.php) | `public function handle(int $teamId, Site $site): void` |
| [UpdateCustomer.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/UpdateCustomer.php) | `public function handle(int $teamId, Customer $customer, array $attributes): Customer` |
| [UpdateSite.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/UpdateSite.php) | `public function handle(int $teamId, Site $site, array $attributes): Site` |
| [CustomerPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Policies/CustomerPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Customer $customer): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Customer $customer): bool`<br>`public function delete(object $user, Customer $customer): bool` |
| [SitePolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Policies/SitePolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Site $site): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Site $site): bool`<br>`public function delete(object $user, Site $site): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Customer.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Models/Customer.php) | `team_id`, `name`, `code`, `email`, `phone`, `address`, `city`, `state`, `zip`, `website`, `industry`, `description`, `type`, `contact_person`, `payment_terms`, `notes`, `is_active` |
| [Site.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Models/Site.php) | `team_id`, `customer_id`, `name`, `code`, `address`, `access_details`, `hazards`, `is_active` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CustomersAndSitesController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-api/src/Http/Controllers/CustomersAndSitesController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateCustomer $create): JsonResponse`<br>`public function show(Request $request, Customer $customer): JsonResponse`<br>`public function update(Request $request, Customer $customer, UpdateCustomer $update): JsonResponse`<br>`public function destroy(Request $request, Customer $customer, DeleteCustomer $delete): JsonResponse`<br>`public function sites(Request $request): JsonResponse`<br>`public function storeSite(Request $request, CreateSite $create): JsonResponse`<br>`public function updateSite(Request $request, Site $site, UpdateSite $update): JsonResponse`<br>`public function destroySite(Request $request, Site $site, DeleteSite $delete): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-customers-and-sites-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/customers-and-sites')->group(function (): void {
Route::get('/', [CustomersAndSitesController::class, 'index']);
Route::post('/', [CustomersAndSitesController::class, 'store']);
Route::get('/sites', [CustomersAndSitesController::class, 'sites']);
Route::post('/sites', [CustomersAndSitesController::class, 'storeSite']);
Route::patch('/sites/{site}', [CustomersAndSitesController::class, 'updateSite']);
Route::delete('/sites/{site}', [CustomersAndSitesController::class, 'destroySite']);
Route::get('/{customer}', [CustomersAndSitesController::class, 'show']);
Route::patch('/{customer}', [CustomersAndSitesController::class, 'update']);
Route::delete('/{customer}', [CustomersAndSitesController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
