# Crm Search React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-search). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-search-react-native
**Matching core package:** module-crm-crm-search ([implementation](../core/crm-search.md))
**Matching API package:** module-crm-crm-search-api ([contract](../api/crm-search.md))

## Implementation plan

This adapter presents Crm Search for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Search API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-search.md), and [API module](../api/crm-search.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-search`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-search.md)) |
| Capability React Native module skeleton | [`module-crm-search-react-native`](https://github.com/liberusoftware/module-crm-search-react-native) (`@liberusoftware/module-crm-search-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Permission-aware global search** | Progressive mobile list/detail/sheet flow for `permission-aware global search` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Saved views** | Progressive mobile list/detail/sheet flow for `saved views` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Filters** | Progressive mobile list/detail/sheet flow for `filters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Related-record search** | Progressive mobile list/detail/sheet flow for `related-record search` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Recents** | Progressive mobile list/detail/sheet flow for `recents` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Suggestions** | Progressive mobile list/detail/sheet flow for `suggestions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Index reconciliation** | Progressive mobile list/detail/sheet flow for `index reconciliation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CrmSearchQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-search/src/Queries/CrmSearchQuery.php) | `public function search(int $teamId, string $term)`<br>`public function views(int $teamId, int $userId)`<br>`public function recents(int $teamId, int $userId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [IndexSearchDocument.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-search/src/Actions/IndexSearchDocument.php) | `public function __construct(private readonly CrmSearchPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): SearchDocument` |
| [RecordSearchRecent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-search/src/Actions/RecordSearchRecent.php) | `public function __construct(private readonly CrmSearchPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): SearchRecent` |
| [SaveSearchView.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-search/src/Actions/SaveSearchView.php) | `public function __construct(private readonly CrmSearchPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): SearchView` |
| [CrmSearchPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-search/src/Services/CrmSearchPolicy.php) | `public function canSearch(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SearchDocument.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-search/src/Models/SearchDocument.php) | No literal fillable array detected; inspect the model and API schema. |
| [SearchRecent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-search/src/Models/SearchRecent.php) | No literal fillable array detected; inspect the model and API schema. |
| [SearchView.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-search/src/Models/SearchView.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CrmSearchController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-search-api/src/Http/Controllers/CrmSearchController.php) | `public function __construct(private readonly CrmSearchQuery $query)`<br>`public function search(): JsonResponse`<br>`public function index(IndexSearchDocument $action): JsonResponse`<br>`public function views(): JsonResponse`<br>`public function saveView(SaveSearchView $action): JsonResponse`<br>`public function recents(): JsonResponse`<br>`public function recent(RecordSearchRecent $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-search-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-search-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/crm-search')->group(function (): void {
Route::get('/', [CrmSearchController::class, 'search']);
Route::post('index', [CrmSearchController::class, 'index']);
Route::get('views', [CrmSearchController::class, 'views']);
Route::post('views', [CrmSearchController::class, 'saveView']);
Route::get('recents', [CrmSearchController::class, 'recents']);
Route::post('recents', [CrmSearchController::class, 'recent']);
```
<!-- layer-implementation-plan:end -->
