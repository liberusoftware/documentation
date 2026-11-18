# Estimates And Quotes React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#estimates-and-quotes). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-estimates-and-quotes-react-native
**Matching core package:** module-accounting-estimates-and-quotes ([implementation](../core/estimates-and-quotes.md))
**Matching API package:** module-accounting-estimates-and-quotes-api ([contract](../api/estimates-and-quotes.md))

## Implementation plan

This adapter presents Estimates And Quotes for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Estimates And Quotes API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/estimates-and-quotes.md), and [API module](../api/estimates-and-quotes.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `estimates-and-quotes`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/estimates-and-quotes.md)) |
| Capability React Native module skeleton | [`module-accounting-estimates-and-quotes-react-native`](https://github.com/liberusoftware/module-accounting-estimates-and-quotes-react-native) (`@liberusoftware/module-accounting-estimates-and-quotes-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Branded estimates/quotes** | Progressive mobile list/detail/sheet flow for `branded estimates/quotes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Items** | Progressive mobile list/detail/sheet flow for `items` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Terms** | Progressive mobile list/detail/sheet flow for `terms` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Versions** | Progressive mobile list/detail/sheet flow for `versions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Delivery** | Progressive mobile list/detail/sheet flow for `delivery` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Acceptance/decline** | Progressive mobile list/detail/sheet flow for `acceptance/decline` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Expiry** | Progressive mobile list/detail/sheet flow for `expiry` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Conversion** | Progressive mobile list/detail/sheet flow for `conversion` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **History** | Progressive mobile list/detail/sheet flow for `history` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EstimateQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Queries/EstimateQuery.php) | `public function paginate(?int $legalEntityId = null, ?EstimateStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function total(Estimate $e): float` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddEstimateItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/AddEstimateItem.php) | `public function handle(Estimate $e, array $a): EstimateItem` |
| [ConvertEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/ConvertEstimate.php) | `public function handle(Estimate $e, string $convertedRef, ?string $actor = null): Estimate` |
| [CreateEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/CreateEstimate.php) | `public function handle(array $a): Estimate` |
| [DecideEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/DecideEstimate.php) | `public function handle(Estimate $e, bool $accepted, ?string $reason = null, ?string $actor = null): Estimate` |
| [ExpireEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/ExpireEstimate.php) | `public function handle(Estimate $e, ?string $actor = null): Estimate` |
| [SendEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/SendEstimate.php) | `public function handle(Estimate $e, ?string $actor = null): Estimate` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Estimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Models/Estimate.php) | `legal_entity_id`, `customer_ref`, `quote_ref`, `name`, `currency`, `status`, `issue_date`, `expires_on`, `version`, `terms`, `brand`, `accepted_at`, `declined_reason`, `converted_ref`, `metadata` |
| [EstimateHistory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Models/EstimateHistory.php) | `estimate_id`, `event`, `actor_ref`, `metadata` |
| [EstimateItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Models/EstimateItem.php) | `estimate_id`, `item_ref`, `description`, `quantity`, `unit_price`, `tax_rate`, `amount`, `metadata` |
| [EstimateVersion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Models/EstimateVersion.php) | `estimate_id`, `version`, `snapshot`, `created_by` |

| Observed API controller | Handler signatures |
| --- | --- |
| [EstimatesController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes-api/src/Http/Controllers/EstimatesController.php) | `public function __construct(private readonly EstimateQuery $query)`<br>`public function index(Request $r): mixed`<br>`public function store(Request $r, CreateEstimate $a): EstimateResource`<br>`public function show(Estimate $e): EstimateResource`<br>`public function item(Request $r, Estimate $e, AddEstimateItem $a): EstimateResource`<br>`public function send(Request $r, Estimate $e, SendEstimate $a): EstimateResource`<br>`public function decide(Request $r, Estimate $e, DecideEstimate $a): EstimateResource`<br>`public function expire(Request $r, Estimate $e, ExpireEstimate $a): EstimateResource`<br>`public function convert(Request $r, Estimate $e, ConvertEstimate $a): EstimateResource` |

**Observed route declarations:**

[modules/accounting-estimates-and-quotes-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/estimates-and-quotes')->group(function (): void {
Route::middleware('ability:accounting.estimates-and-quotes.read')->group(function (): void {
Route::get('/', [EstimatesController::class, 'index']);
Route::get('/{estimate}', [EstimatesController::class, 'show']);
Route::middleware('ability:accounting.estimates-and-quotes.write')->group(function (): void {
Route::post('/', [EstimatesController::class, 'store']);
Route::post('/{estimate}/items', [EstimatesController::class, 'item']);
Route::post('/{estimate}/send', [EstimatesController::class, 'send']);
Route::post('/{estimate}/decide', [EstimatesController::class, 'decide']);
Route::post('/{estimate}/expire', [EstimatesController::class, 'expire']);
Route::post('/{estimate}/convert', [EstimatesController::class, 'convert']);
```
<!-- layer-implementation-plan:end -->
