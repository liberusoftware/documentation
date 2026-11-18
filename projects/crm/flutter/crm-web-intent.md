# Crm Web Intent Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-web-intent). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-web-intent-flutter
**Matching core package:** module-crm-crm-web-intent ([implementation](../core/crm-web-intent.md))
**Matching API package:** module-crm-crm-web-intent-api ([contract](../api/crm-web-intent.md))

## Implementation plan

This adapter presents Crm Web Intent for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Web Intent API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/crm-web-intent.md), and [API module](../api/crm-web-intent.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `crm-web-intent`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-web-intent-flutter`](https://github.com/liberusoftware/module-crm-web-intent-flutter) (`module_crm_web_intent_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-web-intent-dart-mobile`](https://github.com/liberusoftware/module-crm-web-intent-dart-mobile) (`module_crm_web_intent_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-web-intent-dart-desktop`](https://github.com/liberusoftware/module-crm-web-intent-dart-desktop) (`module_crm_web_intent_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/crm-web-intent.md) · [Core plan](../core/crm-web-intent.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **First-party visits** | Adaptive mobile cards/sheets for `first-party visits` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `first-party visits` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Account identification adapters** | Adaptive mobile cards/sheets for `account identification adapters` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `account identification adapters` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Page/content engagement** | Adaptive mobile cards/sheets for `page/content engagement` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `page/content engagement` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Scoring signals** | Adaptive mobile cards/sheets for `scoring signals` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `scoring signals` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Alerts** | Adaptive mobile cards/sheets for `alerts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `alerts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Buyer intent** | Adaptive mobile cards/sheets for `buyer intent` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `buyer intent` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Consent** | Adaptive mobile cards/sheets for `consent` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `consent` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Lead/account conversion** | Adaptive mobile cards/sheets for `lead/account conversion` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `lead/account conversion` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [WebIntentQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Queries/WebIntentQuery.php) | `public function visits(int $teamId): Builder`<br>`public function alerts(int $teamId): Builder`<br>`public function summary(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConvertIntent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/ConvertIntent.php) | `public function execute(int $teamId, int $actorId, string $visitorKey, string $targetType, int $targetId, ?int $visitId, array $metadata, WebIntentPolicy $policy): WebIntentConversion` |
| [CreateAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/CreateAlert.php) | `public function execute(int $teamId, int $actorId, string $visitorKey, string $title, string $severity, ?int $visitId, ?string $details, WebIntentPolicy $policy): WebIntentAlert` |
| [IdentifyAccount.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/IdentifyAccount.php) | `public function execute(int $teamId, int $actorId, string $visitorKey, string $adapter, ?string $accountName, ?string $accountDomain, int $confidence, array $metadata, WebIntentPolicy $policy): WebIntentIdentification` |
| [RecordEngagement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/RecordEngagement.php) | `public function execute(WebIntentVisit $visit, array $attributes, WebIntentScorer $scorer): WebIntentEngagement` |
| [RecordVisit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/RecordVisit.php) | `public function execute(int $teamId, string $visitorKey, array $attributes = []): WebIntentVisit` |
| [ResolveAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/ResolveAlert.php) | `public function execute(WebIntentAlert $alert, int $actorId, WebIntentPolicy $policy): WebIntentAlert` |
| [SetConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/SetConsent.php) | `public function execute(int $teamId, string $visitorKey, string $purpose, string $status, ?string $policyVersion = null): WebIntentConsent` |
| [WebIntentAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Services/WebIntentAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $data = []): void` |
| [WebIntentPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Services/WebIntentPolicy.php) | `public function canManage(int $teamId, int $actorId): bool` |
| [WebIntentScorer.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Services/WebIntentScorer.php) | `public function points(string $eventType, ?int $durationSeconds = null): int`<br>`public function level(int $score): string` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WebIntentAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentAlert.php) | `team_id`, `visitor_key`, `visit_id`, `severity`, `title`, `details`, `status`, `triggered_at`, `resolved_at`, `resolved_by` |
| [WebIntentConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentConsent.php) | `team_id`, `visitor_key`, `purpose`, `status`, `policy_version`, `granted_at`, `revoked_at` |
| [WebIntentConversion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentConversion.php) | `team_id`, `visitor_key`, `visit_id`, `target_type`, `target_id`, `actor_id`, `status`, `metadata` |
| [WebIntentEngagement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentEngagement.php) | `team_id`, `visit_id`, `visitor_key`, `event_type`, `page_url`, `content_type`, `content_id`, `points`, `duration_seconds`, `dedupe_key`, `metadata`, `occurred_at` |
| [WebIntentIdentification.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentIdentification.php) | `team_id`, `visitor_key`, `adapter`, `account_name`, `account_domain`, `confidence`, `status`, `metadata` |
| [WebIntentSignal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentSignal.php) | `team_id`, `visit_id`, `visitor_key`, `signal`, `points`, `metadata`, `occurred_at` |
| [WebIntentVisit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentVisit.php) | `team_id`, `visitor_key`, `session_key`, `ip_hash`, `user_agent_hash`, `landing_url`, `referrer`, `consent_status`, `score`, `intent_level`, `status`, `started_at`, `ended_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [WebIntentController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent-api/src/Http/Controllers/WebIntentController.php) | `public function index(Request $request, WebIntentQuery $query): JsonResponse`<br>`public function store(Request $request, RecordVisit $record): JsonResponse`<br>`public function show(Request $request, int $visit): JsonResponse`<br>`public function engagement(Request $request, int $visit, RecordEngagement $record, WebIntentScorer $scorer): JsonResponse`<br>`public function consent(Request $request, SetConsent $set): JsonResponse`<br>`public function identification(Request $request, IdentifyAccount $identify, WebIntentPolicy $policy): JsonResponse`<br>`public function alerts(Request $request, WebIntentQuery $query): JsonResponse`<br>`public function createAlert(Request $request, CreateAlert $create, WebIntentPolicy $policy): JsonResponse`<br>`public function resolveAlert(Request $request, int $alert, ResolveAlert $resolve, WebIntentPolicy $policy): JsonResponse`<br>`public function convert(Request $request, ConvertIntent $convert, WebIntentPolicy $policy): JsonResponse`<br>`public function summary(Request $request, WebIntentQuery $query): JsonResponse` |

**Observed route declarations:**

[modules/crm-web-intent-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/web-intent')->group(function (): void {
Route::get('/summary', [WebIntentController::class, 'summary'])->name('crm.web-intent.summary');
Route::get('/alerts', [WebIntentController::class, 'alerts'])->name('crm.web-intent.alerts');
Route::get('/visits', [WebIntentController::class, 'index'])->name('crm.web-intent.visits.index');
Route::post('/visits', [WebIntentController::class, 'store'])->name('crm.web-intent.visits.store');
Route::get('/visits/{visit}', [WebIntentController::class, 'show'])->name('crm.web-intent.visits.show');
Route::post('/visits/{visit}/engagements', [WebIntentController::class, 'engagement'])->name('crm.web-intent.engagements.store');
Route::post('/consents', [WebIntentController::class, 'consent'])->name('crm.web-intent.consents.store');
Route::post('/identifications', [WebIntentController::class, 'identification'])->name('crm.web-intent.identifications.store');
Route::post('/alerts', [WebIntentController::class, 'createAlert'])->name('crm.web-intent.alerts.store');
Route::post('/alerts/{alert}/resolve', [WebIntentController::class, 'resolveAlert'])->name('crm.web-intent.alerts.resolve');
Route::post('/conversions', [WebIntentController::class, 'convert'])->name('crm.web-intent.conversions.store');
```
<!-- layer-implementation-plan:end -->
