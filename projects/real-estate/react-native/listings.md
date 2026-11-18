# Listings React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#listings). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-listings-react-native
**Matching core package:** module-real-estate-listings ([implementation](../core/listings.md))
**Matching API package:** module-real-estate-listings-api ([contract](../api/listings.md))

## Implementation plan

This adapter presents Listings for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Listings API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/listings.md), and [API module](../api/listings.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `listings`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-real-estate-mobile-react`](https://github.com/liberusoftware/project-real-estate-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/listings.md)) |
| Capability React Native module skeleton | [`module-real-estate-listings-react-native`](https://github.com/liberusoftware/module-real-estate-listings-react-native) (`@liberusoftware/module-real-estate-listings-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Channel content** | Progressive mobile list/detail/sheet flow for `channel content` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Pricing** | Progressive mobile list/detail/sheet flow for `pricing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Availability** | Progressive mobile list/detail/sheet flow for `availability` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Publication rules** | Progressive mobile list/detail/sheet flow for `publication rules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Portal feeds** | Progressive mobile list/detail/sheet flow for `portal feeds` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reconciliation** | Progressive mobile list/detail/sheet flow for `reconciliation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ListingPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-listings/src/Policies/ListingPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Listing $listing): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Listing $listing): bool`<br>`public function delete(AuthUser $authUser, Listing $listing): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Listing $listing): bool`<br>`public function forceDelete(AuthUser $authUser, Listing $listing): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Listing $listing): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Listing.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-listings/src/Models/Listing.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ListingController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-listings-api/src/Http/Controllers/ListingController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateListing $create): JsonResponse`<br>`public function show(Request $request, Listing $listing): JsonResponse`<br>`public function update(Request $request, Listing $listing, UpdateListing $update): JsonResponse`<br>`public function destroy(Request $request, Listing $listing, DeleteListing $delete): Response`<br>`public function transition(Request $request, Listing $listing, string $status, TransitionListing $transition): JsonResponse`<br>`public function updateSection(Request $request, Listing $listing, string $section, UpdateListingSection $update): JsonResponse` |

**Observed route declarations:**

[modules/real-estate-listings-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-listings-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/listings')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [ListingController::class, 'index'])->name('real-estate.listings.index');
Route::post('/', [ListingController::class, 'store'])->name('real-estate.listings.store');
Route::post('/{listing}/transition/{status}', [ListingController::class, 'transition'])->name('real-estate.listings.transition');
Route::patch('/{listing}/{section}', [ListingController::class, 'updateSection'])->whereIn('section', ['channel_content', 'publication_rules', 'portal_feeds', 'reconciliation'])->name('real-estate.listings.section');
Route::get('/{listing}', [ListingController::class, 'show'])->name('real-estate.listings.show');
Route::delete('/{listing}', [ListingController::class, 'destroy'])->name('real-estate.listings.destroy');
```
<!-- layer-implementation-plan:end -->
