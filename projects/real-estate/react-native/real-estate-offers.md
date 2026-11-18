# Real Estate Offers React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-offers). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-real-estate-offers-react-native
**Matching core package:** module-real-estate-real-estate-offers ([implementation](../core/real-estate-offers.md))
**Matching API package:** module-real-estate-real-estate-offers-api ([contract](../api/real-estate-offers.md))

## Implementation plan

This adapter presents Real Estate Offers for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Real Estate Offers API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/real-estate-offers.md), and [API module](../api/real-estate-offers.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `real-estate-offers`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-real-estate-mobile-react`](https://github.com/liberusoftware/project-real-estate-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/real-estate-offers.md)) |
| Capability React Native module skeleton | [`module-real-estate-offers-react-native`](https://github.com/liberusoftware/module-real-estate-offers-react-native) (`@liberusoftware/module-real-estate-offers-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Terms** | Progressive mobile list/detail/sheet flow for `terms` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Qualification** | Progressive mobile list/detail/sheet flow for `qualification` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Negotiation** | Progressive mobile list/detail/sheet flow for `negotiation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Proof** | Progressive mobile list/detail/sheet flow for `proof` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Decision history** | Progressive mobile list/detail/sheet flow for `decision history` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Accepted-offer controls** | Progressive mobile list/detail/sheet flow for `accepted-offer controls` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [OfferPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-offers/src/Policies/OfferPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Offer $offer): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Offer $offer): bool`<br>`public function delete(AuthUser $authUser, Offer $offer): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Offer $offer): bool`<br>`public function forceDelete(AuthUser $authUser, Offer $offer): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Offer $offer): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Offer.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-offers/src/Models/Offer.php) | No literal fillable array detected; inspect the model and API schema. |
| [OfferEvent.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-offers/src/Models/OfferEvent.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [OfferController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-offers-api/src/Http/Controllers/OfferController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateOffer $create): JsonResponse`<br>`public function show(Request $request, Offer $offer): JsonResponse`<br>`public function update(Request $request, Offer $offer, UpdateOffer $update): JsonResponse`<br>`public function destroy(Request $request, Offer $offer, DeleteOffer $delete): Response`<br>`public function transition(Request $request, Offer $offer, string $status, TransitionOffer $transition): JsonResponse`<br>`public function proof(Request $request, Offer $offer, RecordOfferProof $record): JsonResponse`<br>`public function timeline(Request $request, Offer $offer): JsonResponse` |

**Observed route declarations:**

[modules/real-estate-offers-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-offers-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/offers')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [OfferController::class, 'index'])->name('real-estate.offers.index');
Route::post('/', [OfferController::class, 'store'])->name('real-estate.offers.store');
Route::post('/{offer}/transition/{status}', [OfferController::class, 'transition'])->name('real-estate.offers.transition');
Route::post('/{offer}/proof', [OfferController::class, 'proof'])->name('real-estate.offers.proof');
Route::get('/{offer}/timeline', [OfferController::class, 'timeline'])->name('real-estate.offers.timeline');
Route::get('/{offer}', [OfferController::class, 'show'])->name('real-estate.offers.show');
Route::delete('/{offer}', [OfferController::class, 'destroy'])->name('real-estate.offers.destroy');
```
<!-- layer-implementation-plan:end -->
