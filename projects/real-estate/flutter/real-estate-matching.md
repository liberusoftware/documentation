# Real Estate Matching Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-matching). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-real-estate-matching-flutter
**Matching core package:** module-real-estate-real-estate-matching ([implementation](../core/real-estate-matching.md))
**Matching API package:** module-real-estate-real-estate-matching-api ([contract](../api/real-estate-matching.md))

## Implementation plan

This adapter presents Real Estate Matching for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Real Estate Matching API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/real-estate-matching.md), and [API module](../api/real-estate-matching.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `real-estate-matching`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-real-estate-mobile-flutter`](https://github.com/liberusoftware/project-real-estate-mobile-flutter) | [`module-real-estate-matching-flutter`](https://github.com/liberusoftware/module-real-estate-matching-flutter) (`module_real_estate_matching_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-real-estate-dart-mobile`](https://github.com/liberusoftware/project-real-estate-dart-mobile) | [`module-real-estate-matching-dart-mobile`](https://github.com/liberusoftware/module-real-estate-matching-dart-mobile) (`module_real_estate_matching_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-real-estate-dart-desktop`](https://github.com/liberusoftware/project-real-estate-dart-desktop) | [`module-real-estate-matching-dart-desktop`](https://github.com/liberusoftware/module-real-estate-matching-dart-desktop) (`module_real_estate_matching_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | [API plan](../api/real-estate-matching.md) · [Core plan](../core/real-estate-matching.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Applicant requirements** | Adaptive mobile cards/sheets for `applicant requirements` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `applicant requirements` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Affordability** | Adaptive mobile cards/sheets for `affordability` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `affordability` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Preferences** | Adaptive mobile cards/sheets for `preferences` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `preferences` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Scoring** | Adaptive mobile cards/sheets for `scoring` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `scoring` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Alerts** | Adaptive mobile cards/sheets for `alerts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `alerts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Feedback** | Adaptive mobile cards/sheets for `feedback` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `feedback` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Exclusions** | Adaptive mobile cards/sheets for `exclusions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `exclusions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [MatchProfilePolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-matching/src/Policies/MatchProfilePolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, MatchProfile $matchProfile): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, MatchProfile $matchProfile): bool`<br>`public function delete(AuthUser $authUser, MatchProfile $matchProfile): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, MatchProfile $matchProfile): bool`<br>`public function forceDelete(AuthUser $authUser, MatchProfile $matchProfile): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, MatchProfile $matchProfile): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MatchProfile.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-matching/src/Models/MatchProfile.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [MatchProfileController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-matching-api/src/Http/Controllers/MatchProfileController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateMatchProfile $create): JsonResponse`<br>`public function show(Request $request, MatchProfile $matchProfile): JsonResponse`<br>`public function update(Request $request, MatchProfile $matchProfile, UpdateMatchProfile $update): JsonResponse`<br>`public function updateSection(Request $request, MatchProfile $matchProfile, string $section, UpdateMatchProfileSection $update): JsonResponse`<br>`public function calculateScore(Request $request, CalculateMatchScore $calculate): JsonResponse`<br>`public function recommendProperties(Request $request, RankPropertyRecommendations $rank): JsonResponse`<br>`public function destroy(Request $request, MatchProfile $matchProfile, DeleteMatchProfile $delete): Response` |

**Observed route declarations:**

[modules/real-estate-matching-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-matching-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/matching')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [MatchProfileController::class, 'index'])->name('real-estate.matching.index');
Route::post('/', [MatchProfileController::class, 'store'])->name('real-estate.matching.store');
Route::post('/calculate-score', [MatchProfileController::class, 'calculateScore'])->name('real-estate.matching.calculate-score');
Route::post('/recommend-properties', [MatchProfileController::class, 'recommendProperties'])->name('real-estate.matching.recommend-properties');
Route::get('/{matchProfile}', [MatchProfileController::class, 'show'])->name('real-estate.matching.show');
Route::patch('/{matchProfile}/{section}', [MatchProfileController::class, 'updateSection'])->whereIn('section', ['requirements', 'affordability', 'preferences', 'scoring', 'alerts', 'feedback', 'exclusions'])->name('real-estate.matching.section');
Route::delete('/{matchProfile}', [MatchProfileController::class, 'destroy'])->name('real-estate.matching.destroy');
```
<!-- layer-implementation-plan:end -->
