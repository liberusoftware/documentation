# Coding Suggestions Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#coding-suggestions). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-coding-suggestions-flutter
**Matching core package:** module-accounting-coding-suggestions ([implementation](../core/coding-suggestions.md))
**Matching API package:** module-accounting-coding-suggestions-api ([contract](../api/coding-suggestions.md))

## Implementation plan

This adapter presents Coding Suggestions for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Coding Suggestions API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/coding-suggestions.md), and [API module](../api/coding-suggestions.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `coding-suggestions`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-coding-suggestions-flutter`](https://github.com/liberusoftware/module-accounting-coding-suggestions-flutter) (`module_accounting_coding_suggestions_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-coding-suggestions-dart-mobile`](https://github.com/liberusoftware/module-accounting-coding-suggestions-dart-mobile) (`module_accounting_coding_suggestions_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-coding-suggestions-dart-desktop`](https://github.com/liberusoftware/module-accounting-coding-suggestions-dart-desktop) (`module_accounting_coding_suggestions_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/coding-suggestions.md) · [Core plan](../core/coding-suggestions.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Account/tax/dimension/payee suggestions** | Adaptive mobile cards/sheets for `account/tax/dimension/payee suggestions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `account/tax/dimension/payee suggestions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Confidence** | Adaptive mobile cards/sheets for `confidence` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `confidence` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Explanations** | Adaptive mobile cards/sheets for `explanations` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `explanations` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **User feedback** | Adaptive mobile cards/sheets for `user feedback` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `user feedback` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Policy thresholds** | Adaptive mobile cards/sheets for `policy thresholds` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `policy thresholds` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Review** | Adaptive mobile cards/sheets for `review` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `review` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CodingSuggestionQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Queries/CodingSuggestionQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApplySuggestionFeedback.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Actions/ApplySuggestionFeedback.php) | `public function handle(CodingSuggestion $suggestion, array $feedback): CodingSuggestion` |
| [CreateCodingSuggestion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Actions/CreateCodingSuggestion.php) | `public function handle(array $attributes): CodingSuggestion` |
| [ReviewCodingSuggestion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Actions/ReviewCodingSuggestion.php) | `public function handle(CodingSuggestion $suggestion, array $review): CodingSuggestion` |
| [SetSuggestionPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Actions/SetSuggestionPolicy.php) | `public function handle(CodingSuggestion $suggestion, array $policy): CodingSuggestion` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CodingSuggestion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Models/CodingSuggestion.php) | `team_id`, `source_ref`, `target_type`, `target_ref`, `confidence`, `explanation`, `status`, `feedback`, `policy`, `review` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CodingSuggestionsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions-api/src/Http/Controllers/CodingSuggestionsController.php) | `public function index(CodingSuggestionQuery $query): JsonResponse`<br>`public function store(Request $request, CreateCodingSuggestion $action): JsonResponse`<br>`public function feedback(Request $request, string $suggestion, ApplySuggestionFeedback $action): JsonResponse`<br>`public function review(Request $request, string $suggestion, ReviewCodingSuggestion $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-coding-suggestions-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/coding-suggestions')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.coding-suggestions.read')->get('/', [CodingSuggestionsController::class, 'index']);
Route::middleware('ability:accounting.coding-suggestions.write')->group(function (): void {
Route::post('/', [CodingSuggestionsController::class, 'store']);
Route::post('/{suggestion}/feedback', [CodingSuggestionsController::class, 'feedback']);
Route::post('/{suggestion}/review', [CodingSuggestionsController::class, 'review']);
```
<!-- layer-implementation-plan:end -->
