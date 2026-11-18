# Matching Intelligence React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#matching-intelligence). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-matching-intelligence-react-native
**Matching core package:** module-accounting-matching-intelligence ([implementation](../core/matching-intelligence.md))
**Matching API package:** module-accounting-matching-intelligence-api ([contract](../api/matching-intelligence.md))

## Implementation plan

This adapter presents Matching Intelligence for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Matching Intelligence API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/matching-intelligence.md), and [API module](../api/matching-intelligence.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `matching-intelligence`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/matching-intelligence.md)) |
| Capability React Native module skeleton | [`module-accounting-matching-intelligence-react-native`](https://github.com/liberusoftware/module-accounting-matching-intelligence-react-native) (`@liberusoftware/module-accounting-matching-intelligence-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Bank/document/payment/settlement matching suggestions** | Progressive mobile list/detail/sheet flow for `bank/document/payment/settlement matching suggestions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Confidence** | Progressive mobile list/detail/sheet flow for `confidence` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Evidence** | Progressive mobile list/detail/sheet flow for `evidence` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Feedback** | Progressive mobile list/detail/sheet flow for `feedback` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Safe automation thresholds** | Progressive mobile list/detail/sheet flow for `safe automation thresholds` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [MatchingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Queries/MatchingQuery.php) | `public function suggestions(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function automationEligible(?int $teamId = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfigureThreshold.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Actions/ConfigureThreshold.php) | `public function handle(array $attributes): AutomationThreshold` |
| [CreateSuggestion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Actions/CreateSuggestion.php) | `public function handle(array $attributes, array $evidence = []): MatchingSuggestion` |
| [DecideSuggestion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Actions/DecideSuggestion.php) | `public function handle(MatchingSuggestion $suggestion, string $actor, bool $accept = true, bool $automate = false): MatchingSuggestion` |
| [RecordFeedback.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Actions/RecordFeedback.php) | `public function handle(MatchingSuggestion $suggestion, string $actor, string $type, ?string $comment = null): MatchingFeedback` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AutomationThreshold.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Models/AutomationThreshold.php) | `team_id`, `match_type`, `minimum_confidence`, `maximum_amount`, `require_evidence`, `active`, `metadata` |
| [MatchingEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Models/MatchingEvidence.php) | `suggestion_id`, `kind`, `field`, `source_value`, `target_value`, `weight`, `metadata` |
| [MatchingFeedback.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Models/MatchingFeedback.php) | `suggestion_id`, `actor_ref`, `feedback_type`, `comment`, `features`, `metadata` |
| [MatchingSuggestion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Models/MatchingSuggestion.php) | `team_id`, `suggestion_ref`, `source_type`, `source_id`, `target_type`, `target_id`, `match_type`, `confidence`, `score`, `status`, `automation_threshold`, `explanation`, `algorithm_version`, `expires_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MatchingIntelligenceController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence-api/src/Http/Controllers/MatchingIntelligenceController.php) | `public function index(Request $request, MatchingQuery $query): mixed`<br>`public function store(Request $request, CreateSuggestion $action): MatchingSuggestionResource`<br>`public function show(MatchingSuggestion $suggestion): MatchingSuggestionResource`<br>`public function decide(Request $request, MatchingSuggestion $suggestion, DecideSuggestion $action): MatchingSuggestionResource`<br>`public function feedback(Request $request, MatchingSuggestion $suggestion, RecordFeedback $action): JsonResponse`<br>`public function threshold(Request $request, ConfigureThreshold $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-matching-intelligence-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/matching-intelligence')->group(function (): void {
Route::get('/suggestions', [MatchingIntelligenceController::class, 'index'])->name('accounting.matching-intelligence.list');
Route::post('/suggestions', [MatchingIntelligenceController::class, 'store'])->name('accounting.matching-intelligence.create');
Route::get('/suggestions/{suggestion}', [MatchingIntelligenceController::class, 'show'])->name('accounting.matching-intelligence.show');
Route::post('/suggestions/{suggestion}/decide', [MatchingIntelligenceController::class, 'decide'])->name('accounting.matching-intelligence.decide');
Route::post('/suggestions/{suggestion}/feedback', [MatchingIntelligenceController::class, 'feedback'])->name('accounting.matching-intelligence.feedback');
Route::post('/thresholds', [MatchingIntelligenceController::class, 'threshold'])->name('accounting.matching-intelligence.threshold');
```
<!-- layer-implementation-plan:end -->
