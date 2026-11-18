# Real Estate Offers Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-offers). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-real-estate-offers-flutter
**Matching core package:** module-real-estate-real-estate-offers ([implementation](../core/real-estate-offers.md))
**Matching API package:** module-real-estate-real-estate-offers-api ([contract](../api/real-estate-offers.md))

## Implementation plan

This adapter presents Real Estate Offers for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Real Estate Offers API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/real-estate-offers.md), and [API module](../api/real-estate-offers.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `real-estate-offers`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-real-estate-mobile-flutter`](https://github.com/liberusoftware/project-real-estate-mobile-flutter) | [`module-real-estate-offers-flutter`](https://github.com/liberusoftware/module-real-estate-offers-flutter) (`module_real_estate_offers_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-real-estate-dart-mobile`](https://github.com/liberusoftware/project-real-estate-dart-mobile) | [`module-real-estate-offers-dart-mobile`](https://github.com/liberusoftware/module-real-estate-offers-dart-mobile) (`module_real_estate_offers_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-real-estate-dart-desktop`](https://github.com/liberusoftware/project-real-estate-dart-desktop) | [`module-real-estate-offers-dart-desktop`](https://github.com/liberusoftware/module-real-estate-offers-dart-desktop) (`module_real_estate_offers_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | [API plan](../api/real-estate-offers.md) · [Core plan](../core/real-estate-offers.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Terms** | Adaptive mobile cards/sheets for `terms` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `terms` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Qualification** | Adaptive mobile cards/sheets for `qualification` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `qualification` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Negotiation** | Adaptive mobile cards/sheets for `negotiation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `negotiation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Proof** | Adaptive mobile cards/sheets for `proof` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `proof` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Decision history** | Adaptive mobile cards/sheets for `decision history` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `decision history` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Accepted-offer controls** | Adaptive mobile cards/sheets for `accepted-offer controls` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `accepted-offer controls` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
