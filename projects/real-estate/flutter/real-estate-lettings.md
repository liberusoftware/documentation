# Real Estate Lettings Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-lettings). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-real-estate-lettings-flutter
**Matching core package:** module-real-estate-real-estate-lettings ([implementation](../core/real-estate-lettings.md))
**Matching API package:** module-real-estate-real-estate-lettings-api ([contract](../api/real-estate-lettings.md))

## Implementation plan

This adapter presents Real Estate Lettings for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Real Estate Lettings API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/real-estate-lettings.md), and [API module](../api/real-estate-lettings.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `real-estate-lettings`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-real-estate-mobile-flutter`](https://github.com/liberusoftware/project-real-estate-mobile-flutter) | [`module-real-estate-lettings-flutter`](https://github.com/liberusoftware/module-real-estate-lettings-flutter) (`module_real_estate_lettings_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-real-estate-dart-mobile`](https://github.com/liberusoftware/project-real-estate-dart-mobile) | [`module-real-estate-lettings-dart-mobile`](https://github.com/liberusoftware/module-real-estate-lettings-dart-mobile) (`module_real_estate_lettings_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-real-estate-dart-desktop`](https://github.com/liberusoftware/project-real-estate-dart-desktop) | [`module-real-estate-lettings-dart-desktop`](https://github.com/liberusoftware/module-real-estate-lettings-dart-desktop) (`module_real_estate_lettings_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | [API plan](../api/real-estate-lettings.md) · [Core plan](../core/real-estate-lettings.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Applications** | Adaptive mobile cards/sheets for `applications` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `applications` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Referencing** | Adaptive mobile cards/sheets for `referencing` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `referencing` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Deposits** | Adaptive mobile cards/sheets for `deposits` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `deposits` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Agreements** | Adaptive mobile cards/sheets for `agreements` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `agreements` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Move-in/out** | Adaptive mobile cards/sheets for `move-in/out` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `move-in/out` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Renewals** | Adaptive mobile cards/sheets for `renewals` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `renewals` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Rent changes** | Adaptive mobile cards/sheets for `rent changes` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `rent changes` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Notices** | Adaptive mobile cards/sheets for `notices` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `notices` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListLettings.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Queries/ListLettings.php) | `public function handle(int\|string $teamId, ?string $capability = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [LettingPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Policies/LettingPolicy.php) | `public function view($user, Letting $letting): bool`<br>`public function update($user, Letting $letting): bool`<br>`public function delete($user, Letting $letting): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [LeaseAgreement.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Models/LeaseAgreement.php) | No literal fillable array detected; inspect the model and API schema. |
| [Letting.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Models/Letting.php) | No literal fillable array detected; inspect the model and API schema. |
| [RentalApplication.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Models/RentalApplication.php) | No literal fillable array detected; inspect the model and API schema. |
| [RentalCharge.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Models/RentalCharge.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [LeaseAgreementController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-api/src/Http/Controllers/LeaseAgreementController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateLeaseAgreement $create): JsonResponse`<br>`public function show(Request $request, LeaseAgreement $tenancyAgreement): JsonResponse`<br>`public function update(Request $request, LeaseAgreement $tenancyAgreement): JsonResponse`<br>`public function renew(Request $request, LeaseAgreement $tenancyAgreement, RenewLeaseAgreement $renew): JsonResponse`<br>`public function notice(Request $request, LeaseAgreement $tenancyAgreement, ServeLeaseNotice $notice): JsonResponse` |
| [LettingController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-api/src/Http/Controllers/LettingController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateLetting $create): JsonResponse`<br>`public function show(Request $request, Letting $letting): JsonResponse`<br>`public function update(Request $request, Letting $letting, TransitionLetting $transition): JsonResponse`<br>`public function updateDetails(Request $request, Letting $letting, UpdateLettingDetails $update): JsonResponse`<br>`public function recordFailure(Request $request, Letting $letting, RecordLettingFailure $failure): JsonResponse` |
| [RentalApplicationController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-api/src/Http/Controllers/RentalApplicationController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateRentalApplication $create): JsonResponse`<br>`public function show(Request $request, RentalApplication $rentalApplication): JsonResponse`<br>`public function update(Request $request, RentalApplication $rentalApplication, UpdateRentalApplicationScreening $update): JsonResponse`<br>`public function screening(Request $request, RentalApplication $rentalApplication, UpdateRentalApplicationScreening $update): JsonResponse`<br>`public function decide(Request $request, RentalApplication $rentalApplication, DecideRentalApplication $decide): JsonResponse` |
| [RentalChargeController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-api/src/Http/Controllers/RentalChargeController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateRentalCharge $create): JsonResponse`<br>`public function show(Request $request, RentalCharge $rentalCharge): JsonResponse`<br>`public function update(Request $request, RentalCharge $rentalCharge, UpdateRentalCharge $update): JsonResponse`<br>`public function destroy(Request $request, RentalCharge $rentalCharge): JsonResponse` |

**Observed route declarations:**

[modules/real-estate-lettings-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/lettings')->group(function (): void {
Route::get('/', [LettingController::class, 'index']);
Route::post('/', [LettingController::class, 'store']);
Route::get('/{letting}', [LettingController::class, 'show']);
Route::patch('/{letting}', [LettingController::class, 'update']);
Route::patch('/{letting}/details', [LettingController::class, 'updateDetails']);
Route::post('/{letting}/failure', [LettingController::class, 'recordFailure']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/rental-charges')->group(function (): void {
Route::get('/', [RentalChargeController::class, 'index']);
Route::post('/', [RentalChargeController::class, 'store']);
Route::get('/{rentalCharge}', [RentalChargeController::class, 'show']);
Route::patch('/{rentalCharge}', [RentalChargeController::class, 'update']);
Route::delete('/{rentalCharge}', [RentalChargeController::class, 'destroy']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/tenancy-agreements')->group(function (): void {
Route::get('/', [LeaseAgreementController::class, 'index']);
Route::post('/', [LeaseAgreementController::class, 'store']);
Route::get('/{tenancyAgreement}', [LeaseAgreementController::class, 'show']);
Route::patch('/{tenancyAgreement}', [LeaseAgreementController::class, 'update']);
Route::post('/{tenancyAgreement}/renew', [LeaseAgreementController::class, 'renew']);
Route::post('/{tenancyAgreement}/notice', [LeaseAgreementController::class, 'notice']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/rental-applications')->group(function (): void {
Route::get('/', [RentalApplicationController::class, 'index']);
Route::post('/', [RentalApplicationController::class, 'store']);
Route::get('/{rentalApplication}', [RentalApplicationController::class, 'show']);
Route::patch('/{rentalApplication}', [RentalApplicationController::class, 'update']);
Route::patch('/{rentalApplication}/screening', [RentalApplicationController::class, 'screening']);
Route::post('/{rentalApplication}/decision', [RentalApplicationController::class, 'decide']);
```
<!-- layer-implementation-plan:end -->
