# Accounting Job Estimates React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-job-estimates). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-job-estimates-react-native
**Matching core package:** module-accounting-accounting-job-estimates ([implementation](../core/accounting-job-estimates.md))
**Matching API package:** module-accounting-accounting-job-estimates-api ([contract](../api/accounting-job-estimates.md))

## Implementation plan

This adapter presents Accounting Job Estimates for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Job Estimates API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-job-estimates.md), and [API module](../api/accounting-job-estimates.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-job-estimates`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-job-estimates.md)) |
| Capability React Native module skeleton | [`module-accounting-job-estimates-react-native`](https://github.com/liberusoftware/module-accounting-job-estimates-react-native) (`@liberusoftware/module-accounting-job-estimates-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Cost/revenue estimates** | Progressive mobile list/detail/sheet flow for `cost/revenue estimates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Quantities/rates** | Progressive mobile list/detail/sheet flow for `quantities/rates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Versions** | Progressive mobile list/detail/sheet flow for `versions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approvals** | Progressive mobile list/detail/sheet flow for `approvals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Actual comparison** | Progressive mobile list/detail/sheet flow for `actual comparison` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Estimate-at-completion** | Progressive mobile list/detail/sheet flow for `estimate-at-completion` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [JobEstimateQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Queries/JobEstimateQuery.php) | `public function paginate(?int $teamId = null, ?EstimateStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function comparison(JobEstimate $estimate): array`<br>`public function estimateAtCompletion(JobEstimate $estimate): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddEstimateLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/AddEstimateLine.php) | `public function handle(JobEstimate $estimate, array $attributes): EstimateLine` |
| [CreateEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/CreateEstimate.php) | `public function handle(array $attributes): JobEstimate` |
| [CreateVersion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/CreateVersion.php) | `public function handle(JobEstimate $estimate, ?string $notes = null): EstimateVersion` |
| [DecideEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/DecideEstimate.php) | `public function handle(JobEstimate $estimate, string $actor, bool $approved, ?string $comment = null): JobEstimate` |
| [RecordActual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/RecordActual.php) | `public function handle(JobEstimate $estimate, array $attributes): EstimateActual` |
| [SubmitEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/SubmitEstimate.php) | `public function handle(JobEstimate $estimate): JobEstimate` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EstimateActual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Models/EstimateActual.php) | `estimate_id`, `version_id`, `line_ref`, `category`, `amount`, `source_ref`, `occurred_at`, `metadata` |
| [EstimateApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Models/EstimateApproval.php) | `estimate_id`, `version_id`, `actor_ref`, `decision`, `comment`, `decided_at`, `metadata` |
| [EstimateLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Models/EstimateLine.php) | `estimate_id`, `version_id`, `line_ref`, `line_type`, `category`, `description`, `quantity`, `rate`, `amount`, `actual_amount`, `metadata` |
| [EstimateVersion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Models/EstimateVersion.php) | `estimate_id`, `version_no`, `status`, `notes`, `total_cost`, `total_revenue`, `metadata` |
| [JobEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Models/JobEstimate.php) | `team_id`, `estimate_ref`, `project_ref`, `title`, `currency`, `status`, `version_no`, `total_cost`, `total_revenue`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [JobEstimatesController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates-api/src/Http/Controllers/JobEstimatesController.php) | `public function __construct(private readonly JobEstimateQuery $query)`<br>`public function index(Request $request): AnonymousResourceCollection`<br>`public function store(Request $request, CreateEstimate $action): JsonResponse`<br>`public function show(Request $request, JobEstimate $estimate): JobEstimateResource`<br>`public function line(Request $request, JobEstimate $estimate, AddEstimateLine $action): JobEstimateResource`<br>`public function submit(JobEstimate $estimate, SubmitEstimate $action): JobEstimateResource`<br>`public function decide(Request $request, JobEstimate $estimate, DecideEstimate $action): JobEstimateResource`<br>`public function version(Request $request, JobEstimate $estimate, CreateVersion $action): JobEstimateResource`<br>`public function actual(Request $request, JobEstimate $estimate, RecordActual $action): JobEstimateResource`<br>`public function comparison(JobEstimate $estimate, JobEstimateQuery $query): JsonResponse`<br>`public function eac(JobEstimate $estimate, JobEstimateQuery $query): JsonResponse` |

**Observed route declarations:**

[modules/accounting-job-estimates-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/job-estimates')->group(function (): void {
Route::middleware('ability:accounting.job-estimates.read')->group(function (): void {
Route::get('/', [JobEstimatesController::class, 'index'])->name('accounting.job-estimates.list');
Route::get('/{estimate}/comparison', [JobEstimatesController::class, 'comparison'])->name('accounting.job-estimates.comparison');
Route::get('/{estimate}/eac', [JobEstimatesController::class, 'eac'])->name('accounting.job-estimates.eac');
Route::get('/{estimate}', [JobEstimatesController::class, 'show'])->name('accounting.job-estimates.show');
Route::middleware('ability:accounting.job-estimates.write')->group(function (): void {
Route::post('/', [JobEstimatesController::class, 'store'])->name('accounting.job-estimates.create');
Route::post('/{estimate}/lines', [JobEstimatesController::class, 'line'])->name('accounting.job-estimates.line');
Route::post('/{estimate}/submit', [JobEstimatesController::class, 'submit'])->name('accounting.job-estimates.submit');
Route::post('/{estimate}/decide', [JobEstimatesController::class, 'decide'])->name('accounting.job-estimates.decide');
Route::post('/{estimate}/versions', [JobEstimatesController::class, 'version'])->name('accounting.job-estimates.version');
Route::post('/{estimate}/actuals', [JobEstimatesController::class, 'actual'])->name('accounting.job-estimates.actual');
```
<!-- layer-implementation-plan:end -->
