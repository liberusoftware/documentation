# Marketing React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#marketing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-marketing-react-native
**Matching core package:** module-real-estate-marketing ([implementation](../core/marketing.md))
**Matching API package:** module-real-estate-marketing-api ([contract](../api/marketing.md))

## Implementation plan

This adapter presents Marketing for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Marketing API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/marketing.md), and [API module](../api/marketing.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `marketing`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-real-estate-mobile-react`](https://github.com/liberusoftware/project-real-estate-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/marketing.md)) |
| Capability React Native module skeleton | [`module-real-estate-marketing-react-native`](https://github.com/liberusoftware/module-real-estate-marketing-react-native) (`@liberusoftware/module-real-estate-marketing-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Campaigns** | Progressive mobile list/detail/sheet flow for `campaigns` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Boards** | Progressive mobile list/detail/sheet flow for `boards` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Brochures** | Progressive mobile list/detail/sheet flow for `brochures` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Portals** | Progressive mobile list/detail/sheet flow for `portals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Website** | Progressive mobile list/detail/sheet flow for `website` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Social/email** | Progressive mobile list/detail/sheet flow for `social/email` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Attribution** | Progressive mobile list/detail/sheet flow for `attribution` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Consent** | Progressive mobile list/detail/sheet flow for `consent` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [MarketingCampaignPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing/src/Policies/MarketingCampaignPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, MarketingCampaign $marketingCampaign): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, MarketingCampaign $marketingCampaign): bool`<br>`public function delete(AuthUser $authUser, MarketingCampaign $marketingCampaign): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, MarketingCampaign $marketingCampaign): bool`<br>`public function forceDelete(AuthUser $authUser, MarketingCampaign $marketingCampaign): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, MarketingCampaign $marketingCampaign): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MarketingCampaign.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing/src/Models/MarketingCampaign.php) | No literal fillable array detected; inspect the model and API schema. |
| [NewsArticle.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing/src/Models/NewsArticle.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [MarketingCampaignController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing-api/src/Http/Controllers/MarketingCampaignController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateMarketingCampaign $create): JsonResponse`<br>`public function show(Request $request, MarketingCampaign $marketingCampaign): JsonResponse`<br>`public function update(Request $request, MarketingCampaign $marketingCampaign, UpdateMarketingCampaign $update): JsonResponse`<br>`public function transition(Request $request, MarketingCampaign $marketingCampaign, string $status, TransitionMarketingCampaign $transition): JsonResponse`<br>`public function updateSection(Request $request, MarketingCampaign $marketingCampaign, string $section, UpdateMarketingCampaignSection $update): JsonResponse`<br>`public function destroy(Request $request, MarketingCampaign $marketingCampaign, DeleteMarketingCampaign $delete): Response` |
| [NewsArticleController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing-api/src/Http/Controllers/NewsArticleController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, string $slug): JsonResponse`<br>`public function latest(Request $request): JsonResponse`<br>`public function featured(Request $request): JsonResponse` |

**Observed route declarations:**

[modules/real-estate-marketing-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/news')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [NewsArticleController::class, 'index']);
Route::get('/featured', [NewsArticleController::class, 'featured']);
Route::get('/{slug}', [NewsArticleController::class, 'show']);
Route::prefix('api/v1/real-estate/marketing')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [MarketingCampaignController::class, 'index']);
Route::post('/', [MarketingCampaignController::class, 'store']);
Route::get('/{marketingCampaign}', [MarketingCampaignController::class, 'show']);
Route::post('/{marketingCampaign}/transition/{status}', [MarketingCampaignController::class, 'transition']);
Route::patch('/{marketingCampaign}/{section}', [MarketingCampaignController::class, 'updateSection'])->whereIn('section', ['audience', 'content', 'schedule', 'metrics']);
Route::delete('/{marketingCampaign}', [MarketingCampaignController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
