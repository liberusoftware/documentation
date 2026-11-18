# Job Estimates Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#job-estimates). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-job-estimates-flutter
**Matching core package:** module-accounting-job-estimates ([implementation](../core/job-estimates.md))
**Matching API package:** module-accounting-job-estimates-api ([contract](../api/job-estimates.md))

## Implementation plan

This adapter presents Job Estimates for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Job Estimates API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/job-estimates.md), and [API module](../api/job-estimates.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `job-estimates`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-job-estimates-flutter`](https://github.com/liberusoftware/module-accounting-job-estimates-flutter) (`module_accounting_job_estimates_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-job-estimates-dart-mobile`](https://github.com/liberusoftware/module-accounting-job-estimates-dart-mobile) (`module_accounting_job_estimates_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-job-estimates-dart-desktop`](https://github.com/liberusoftware/module-accounting-job-estimates-dart-desktop) (`module_accounting_job_estimates_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/job-estimates.md) · [Core plan](../core/job-estimates.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Cost/revenue estimates** | Adaptive mobile cards/sheets for `cost/revenue estimates` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `cost/revenue estimates` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Quantities/rates** | Adaptive mobile cards/sheets for `quantities/rates` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `quantities/rates` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Versions** | Adaptive mobile cards/sheets for `versions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `versions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Approvals** | Adaptive mobile cards/sheets for `approvals` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `approvals` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Actual comparison** | Adaptive mobile cards/sheets for `actual comparison` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `actual comparison` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Estimate-at-completion** | Adaptive mobile cards/sheets for `estimate-at-completion` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `estimate-at-completion` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
