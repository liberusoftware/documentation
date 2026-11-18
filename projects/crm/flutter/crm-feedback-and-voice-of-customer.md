# Crm Feedback And Voice Of Customer Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-feedback-and-voice-of-customer). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-feedback-and-voice-of-customer-flutter
**Matching core package:** module-crm-crm-feedback-and-voice-of-customer ([implementation](../core/crm-feedback-and-voice-of-customer.md))
**Matching API package:** module-crm-crm-feedback-and-voice-of-customer-api ([contract](../api/crm-feedback-and-voice-of-customer.md))

## Implementation plan

This adapter presents Crm Feedback And Voice Of Customer for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Feedback And Voice Of Customer API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/crm-feedback-and-voice-of-customer.md), and [API module](../api/crm-feedback-and-voice-of-customer.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `crm-feedback-and-voice-of-customer`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-feedback-and-voice-of-customer-flutter`](https://github.com/liberusoftware/module-crm-feedback-and-voice-of-customer-flutter) (`module_crm_feedback_and_voice_of_customer_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-feedback-and-voice-of-customer-dart-mobile`](https://github.com/liberusoftware/module-crm-feedback-and-voice-of-customer-dart-mobile) (`module_crm_feedback_and_voice_of_customer_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-feedback-and-voice-of-customer-dart-desktop`](https://github.com/liberusoftware/module-crm-feedback-and-voice-of-customer-dart-desktop) (`module_crm_feedback_and_voice_of_customer_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/crm-feedback-and-voice-of-customer.md) · [Core plan](../core/crm-feedback-and-voice-of-customer.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **CSAT** | Adaptive mobile cards/sheets for `csat` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `csat` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **NPS** | Adaptive mobile cards/sheets for `nps` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `nps` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **CES** | Adaptive mobile cards/sheets for `ces` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `ces` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Custom surveys** | Adaptive mobile cards/sheets for `custom surveys` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `custom surveys` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Sampling** | Adaptive mobile cards/sheets for `sampling` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `sampling` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Delivery** | Adaptive mobile cards/sheets for `delivery` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `delivery` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Responses** | Adaptive mobile cards/sheets for `responses` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `responses` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Text analysis** | Adaptive mobile cards/sheets for `text analysis` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `text analysis` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Alerts** | Adaptive mobile cards/sheets for `alerts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `alerts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Close-the-loop cases** | Adaptive mobile cards/sheets for `close-the-loop cases` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `close-the-loop cases` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Trend reporting** | Adaptive mobile cards/sheets for `trend reporting` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `trend reporting` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [FeedbackQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Queries/FeedbackQuery.php) | `public function surveys(int $teamId)`<br>`public function responses(int $teamId, int $surveyId)`<br>`public function trend(int $teamId, int $surveyId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateFeedbackSurvey.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/CreateFeedbackSurvey.php) | `public function __construct(private readonly FeedbackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): FeedbackSurvey` |
| [DeliverFeedbackSurvey.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/DeliverFeedbackSurvey.php) | `public function __construct(private readonly FeedbackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, FeedbackSurvey $survey, ?int $recipientId, string $channel = 'email'): FeedbackDelivery` |
| [OpenFeedbackCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/OpenFeedbackCase.php) | `public function __construct(private readonly FeedbackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, FeedbackResponse $response, ?int $ownerId = null): FeedbackCase` |
| [RecordFeedbackResponse.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/RecordFeedbackResponse.php) | `public function execute(int $teamId, FeedbackDelivery $delivery, array $input): FeedbackResponse` |
| [ResolveFeedbackAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/ResolveFeedbackAlert.php) | `public function __construct(private readonly FeedbackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, FeedbackAlert $alert): FeedbackAlert` |
| [FeedbackPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Services/FeedbackPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FeedbackAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackAlert.php) | No literal fillable array detected; inspect the model and API schema. |
| [FeedbackCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackCase.php) | No literal fillable array detected; inspect the model and API schema. |
| [FeedbackDelivery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackDelivery.php) | No literal fillable array detected; inspect the model and API schema. |
| [FeedbackResponse.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackResponse.php) | No literal fillable array detected; inspect the model and API schema. |
| [FeedbackSurvey.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackSurvey.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [FeedbackController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer-api/src/Http/Controllers/FeedbackController.php) | `public function __construct(private readonly FeedbackQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(CreateFeedbackSurvey $action): JsonResponse`<br>`public function deliver(FeedbackSurvey $survey, DeliverFeedbackSurvey $action): JsonResponse`<br>`public function respond(FeedbackDelivery $delivery, RecordFeedbackResponse $action): JsonResponse`<br>`public function trend(FeedbackSurvey $survey): JsonResponse`<br>`public function openCase(FeedbackResponse $response, OpenFeedbackCase $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-feedback-and-voice-of-customer-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/feedback-and-voice-of-customer')->group(function (): void {
Route::get('surveys', [FeedbackController::class, 'index']);
Route::post('surveys', [FeedbackController::class, 'store']);
Route::post('surveys/{survey}/deliver', [FeedbackController::class, 'deliver']);
Route::post('deliveries/{delivery}/responses', [FeedbackController::class, 'respond']);
Route::get('surveys/{survey}/trend', [FeedbackController::class, 'trend']);
Route::post('responses/{response}/cases', [FeedbackController::class, 'openCase']);
```
<!-- layer-implementation-plan:end -->
