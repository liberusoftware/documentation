# Mileage React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#mileage). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-mileage-react-native
**Matching core package:** module-accounting-mileage ([implementation](../core/mileage.md))
**Matching API package:** module-accounting-mileage-api ([contract](../api/mileage.md))

## Implementation plan

This adapter presents Mileage for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Mileage API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/mileage.md), and [API module](../api/mileage.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `mileage`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/mileage.md)) |
| Capability React Native module skeleton | [`module-accounting-mileage-react-native`](https://github.com/liberusoftware/module-accounting-mileage-react-native) (`@liberusoftware/module-accounting-mileage-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Vehicles/rates** | Progressive mobile list/detail/sheet flow for `vehicles/rates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Trip capture/import** | Progressive mobile list/detail/sheet flow for `trip capture/import` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Distance** | Progressive mobile list/detail/sheet flow for `distance` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Business purpose** | Progressive mobile list/detail/sheet flow for `business purpose` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Projects** | Progressive mobile list/detail/sheet flow for `projects` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Policy** | Progressive mobile list/detail/sheet flow for `policy` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approval** | Progressive mobile list/detail/sheet flow for `approval` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reimbursement** | Progressive mobile list/detail/sheet flow for `reimbursement` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Regional reporting** | Progressive mobile list/detail/sheet flow for `regional reporting` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [MileageQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Queries/MileageQuery.php) | `public function trips(?int $teamId = null, int $perPage = 25): LengthAwarePaginator`<br>`public function rates(?int $teamId = null, int $perPage = 25): LengthAwarePaginator`<br>`public function regionalReport(?int $teamId = null, ?string $region = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveTrip.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/ApproveTrip.php) | `public function handle(MileageTrip $trip, string $actor, bool $approved = true, ?string $reason = null): MileageTrip` |
| [CaptureTrip.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/CaptureTrip.php) | `public function handle(array $attributes): MileageTrip` |
| [CreateVehicle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/CreateVehicle.php) | `public function handle(array $attributes): Vehicle` |
| [RecordMileageRate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/RecordMileageRate.php) | `public function handle(array $attributes): MileageRate` |
| [ReimburseTrip.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/ReimburseTrip.php) | `public function handle(MileageTrip $trip, string $payee, ?string $externalRef = null): MileageReimbursement` |
| [SubmitTrip.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/SubmitTrip.php) | `public function handle(MileageTrip $trip): MileageTrip` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MileageApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileageApproval.php) | `trip_id`, `actor_ref`, `decision`, `reason`, `decided_at`, `metadata` |
| [MileagePolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileagePolicy.php) | `team_id`, `name`, `region`, `max_distance_per_trip`, `max_distance_per_day`, `requires_purpose`, `requires_project`, `approval_threshold`, `currency`, `active`, `metadata` |
| [MileageRate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileageRate.php) | `team_id`, `region`, `vehicle_type`, `currency`, `rate_per_distance`, `effective_from`, `effective_until`, `active`, `metadata` |
| [MileageReimbursement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileageReimbursement.php) | `trip_id`, `payee_ref`, `currency`, `amount`, `status`, `external_ref`, `failure_message`, `paid_at`, `metadata` |
| [MileageTrip.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileageTrip.php) | `team_id`, `trip_ref`, `employee_ref`, `vehicle_id`, `rate_id`, `policy_id`, `project_ref`, `origin`, `destination`, `trip_date`, `distance`, `distance_unit`, `business_purpose`, `region`, `currency`, `reimbursement_amount`, `status`, `source`, `source_hash`, `submitted_at`, `approved_at`, `reimbursed_at`, `metadata` |
| [Vehicle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/Vehicle.php) | `team_id`, `owner_ref`, `registration`, `make`, `model`, `fuel_type`, `co2_g_per_km`, `active`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MileageController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage-api/src/Http/Controllers/MileageController.php) | `public function index(Request $request, MileageQuery $query): mixed`<br>`public function store(Request $request, CaptureTrip $action): MileageResource`<br>`public function show(MileageTrip $trip): MileageResource`<br>`public function vehicles(Request $request): mixed`<br>`public function vehicle(Request $request, CreateVehicle $action): JsonResponse`<br>`public function rate(Request $request, RecordMileageRate $action): JsonResponse`<br>`public function submit(MileageTrip $trip, SubmitTrip $action): MileageResource`<br>`public function approve(Request $request, MileageTrip $trip, ApproveTrip $action): MileageResource`<br>`public function reimburse(Request $request, MileageTrip $trip, ReimburseTrip $action): JsonResponse`<br>`public function report(Request $request, MileageQuery $query): array` |

**Observed route declarations:**

[modules/accounting-mileage-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/mileage')->group(function (): void {
Route::get('/', [MileageController::class, 'index'])->name('accounting.mileage.list');
Route::post('/', [MileageController::class, 'store'])->name('accounting.mileage.create');
Route::get('/vehicles', [MileageController::class, 'vehicles'])->name('accounting.mileage.vehicles');
Route::post('/vehicles', [MileageController::class, 'vehicle'])->name('accounting.mileage.vehicle');
Route::post('/rates', [MileageController::class, 'rate'])->name('accounting.mileage.rate');
Route::get('/report/regional', [MileageController::class, 'report'])->name('accounting.mileage.report');
Route::get('/{trip}', [MileageController::class, 'show'])->name('accounting.mileage.get');
Route::post('/{trip}/submit', [MileageController::class, 'submit'])->name('accounting.mileage.submit');
Route::post('/{trip}/approve', [MileageController::class, 'approve'])->name('accounting.mileage.approve');
Route::post('/{trip}/reimburse', [MileageController::class, 'reimburse'])->name('accounting.mileage.reimburse');
```
<!-- layer-implementation-plan:end -->
