# Accounting Periods Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-periods). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-periods-flutter
**Matching core package:** module-accounting-accounting-periods ([implementation](../core/accounting-periods.md))
**Matching API package:** module-accounting-accounting-periods-api ([contract](../api/accounting-periods.md))

## Implementation plan

This adapter presents Accounting Periods for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Periods API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/accounting-periods.md), and [API module](../api/accounting-periods.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `accounting-periods`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-periods-flutter`](https://github.com/liberusoftware/module-accounting-periods-flutter) (`module_accounting_periods_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-periods-dart-mobile`](https://github.com/liberusoftware/module-accounting-periods-dart-mobile) (`module_accounting_periods_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-periods-dart-desktop`](https://github.com/liberusoftware/module-accounting-periods-dart-desktop) (`module_accounting_periods_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/accounting-periods.md) · [Core plan](../core/accounting-periods.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Open/soft-close/hard-close states** | Adaptive mobile cards/sheets for `open/soft-close/hard-close states` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `open/soft-close/hard-close states` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Transaction-date controls** | Adaptive mobile cards/sheets for `transaction-date controls` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `transaction-date controls` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Module dependencies** | Adaptive mobile cards/sheets for `module dependencies` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `module dependencies` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Locks** | Adaptive mobile cards/sheets for `locks` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `locks` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Reopen approval** | Adaptive mobile cards/sheets for `reopen approval` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `reopen approval` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Evidence** | Adaptive mobile cards/sheets for `evidence` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `evidence` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods/src/Actions/CreatePeriod.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(array $attributes): AccountingPeriod` |
| [LockPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods/src/Actions/LockPeriod.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(AccountingPeriod $period, ?string $actor): AccountingPeriod` |
| [TransitionPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods/src/Actions/TransitionPeriod.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(AccountingPeriod $period, PeriodState $to, ?string $actor = null, ?string $reason = null): AccountingPeriod` |
| [UnlockPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods/src/Actions/UnlockPeriod.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(AccountingPeriod $period, ?string $actor, ?string $reason): AccountingPeriod` |
| [AccountingPeriodsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods-api/src/Policies/AccountingPeriodsPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccountingPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods/src/Models/AccountingPeriod.php) | `book_id`, `starts_on`, `ends_on`, `state`, `posting_ends_on`, `locked_by`, `locked_at`, `reopened_by`, `reopen_reason`, `evidence` |

| Observed API controller | Handler signatures |
| --- | --- |
| [AccountingPeriodController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods-api/src/Http/Controllers/AccountingPeriodController.php) | `public function index(Request $request)`<br>`public function show(string $period): AccountingPeriodResource`<br>`public function store(Request $request, CreatePeriod $create)`<br>`public function transition(Request $request, string $period, TransitionPeriod $transition): AccountingPeriodResource`<br>`public function lock(Request $request, string $period, LockPeriod $lock): AccountingPeriodResource`<br>`public function unlock(Request $request, string $period, UnlockPeriod $unlock): AccountingPeriodResource`<br>`public function postingAllowed(Request $request, string $period): JsonResponse`<br>`public function destroy(string $period): Response` |

**Observed route declarations:**

[modules/accounting-periods-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/accounting-periods')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('periods', [AccountingPeriodController::class, 'index'])->middleware('ability:accounting.periods.read');
Route::get('periods/{period}', [AccountingPeriodController::class, 'show'])->middleware('ability:accounting.periods.read');
Route::post('periods', [AccountingPeriodController::class, 'store'])->middleware('ability:accounting.periods.write');
Route::post('periods/{period}/transition', [AccountingPeriodController::class, 'transition'])->middleware('ability:accounting.periods.write');
Route::post('periods/{period}/lock', [AccountingPeriodController::class, 'lock'])->middleware('ability:accounting.periods.write');
Route::post('periods/{period}/unlock', [AccountingPeriodController::class, 'unlock'])->middleware('ability:accounting.periods.write');
Route::get('periods/{period}/posting-allowed', [AccountingPeriodController::class, 'postingAllowed'])->middleware('ability:accounting.periods.read');
Route::delete('periods/{period}', [AccountingPeriodController::class, 'destroy'])->middleware('ability:accounting.periods.write');
```
<!-- layer-implementation-plan:end -->
