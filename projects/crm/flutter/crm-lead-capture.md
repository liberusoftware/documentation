# Crm Lead Capture Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-lead-capture). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-lead-capture-flutter
**Matching core package:** module-crm-crm-lead-capture ([implementation](../core/crm-lead-capture.md))
**Matching API package:** module-crm-crm-lead-capture-api ([contract](../api/crm-lead-capture.md))

## Implementation plan

This adapter presents Crm Lead Capture for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Lead Capture API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/crm-lead-capture.md), and [API module](../api/crm-lead-capture.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `crm-lead-capture`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-lead-capture-flutter`](https://github.com/liberusoftware/module-crm-lead-capture-flutter) (`module_crm_lead_capture_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-lead-capture-dart-mobile`](https://github.com/liberusoftware/module-crm-lead-capture-dart-mobile) (`module_crm_lead_capture_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-lead-capture-dart-desktop`](https://github.com/liberusoftware/module-crm-lead-capture-dart-desktop) (`module_crm_lead_capture_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/crm-lead-capture.md) · [Core plan](../core/crm-lead-capture.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Leads inbox** | Adaptive mobile cards/sheets for `leads inbox` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `leads inbox` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Manual/import/API capture** | Adaptive mobile cards/sheets for `manual/import/api capture` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `manual/import/api capture` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Forms** | Adaptive mobile cards/sheets for `forms` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `forms` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Surveys** | Adaptive mobile cards/sheets for `surveys` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `surveys` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **QR codes** | Adaptive mobile cards/sheets for `qr codes` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `qr codes` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Chat** | Adaptive mobile cards/sheets for `chat` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `chat` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Calls** | Adaptive mobile cards/sheets for `calls` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `calls` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Advertisements** | Adaptive mobile cards/sheets for `advertisements` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `advertisements` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Events** | Adaptive mobile cards/sheets for `events` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `events` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Referrals** | Adaptive mobile cards/sheets for `referrals` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `referrals` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Source metadata** | Adaptive mobile cards/sheets for `source metadata` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `source metadata` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CaptureQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Queries/CaptureQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CaptureLead.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/CaptureLead.php) | `public function __construct(private readonly LeadCapturePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CapturedLead`<br>`public function executeLegacy(int $teamId, ?int $actorId, array $input): LeadCapture` |
| [CreateCaptureForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/CreateCaptureForm.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): CaptureForm` |
| [CreateCaptureQrCode.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/CreateCaptureQrCode.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): CaptureQrCode` |
| [RecordCaptureEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/RecordCaptureEvent.php) | `public function __construct(private readonly LeadCapturePolicy $policy)`<br>`public function execute(int $teamId, int $userId, CapturedLead $lead, array $input): CaptureEvent` |
| [RecordReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/RecordReferral.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): CaptureReferral` |
| [SubmitCaptureForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/SubmitCaptureForm.php) | `public function execute(CaptureForm $form, ?int $actorId, array $payload): LeadCapture` |
| [UpdateCaptureStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/UpdateCaptureStatus.php) | `public function execute(LeadCapture $capture, string $status, ?string $failureReason = null): LeadCapture` |
| [CaptureDeduplicator.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Services/CaptureDeduplicator.php) | `public function key(array $attributes): string`<br>`public function find(int $teamId, string $key): ?LeadCapture` |
| [CaptureReport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Services/CaptureReport.php) | `public function summarize(int $teamId, Carbon $from, Carbon $until): array` |
| [LeadCapturePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Services/LeadCapturePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CaptureEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CaptureEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [CaptureForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CaptureForm.php) | `team_id`, `actor_id`, `kind`, `name`, `slug`, `status`, `schema`, `settings`, `submissions_count` |
| [CaptureQrCode.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CaptureQrCode.php) | `team_id`, `actor_id`, `name`, `code`, `destination`, `status`, `metadata`, `scan_count` |
| [CaptureReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CaptureReferral.php) | `team_id`, `actor_id`, `code`, `referrer_type`, `referrer_id`, `referred_type`, `referred_id`, `status`, `metadata` |
| [CapturedLead.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CapturedLead.php) | No literal fillable array detected; inspect the model and API schema. |
| [LeadCapture.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/LeadCapture.php) | `team_id`, `actor_id`, `kind`, `status`, `name`, `email`, `phone`, `source`, `source_medium`, `source_campaign`, `external_id`, `dedupe_key`, `source_metadata`, `payload`, `provenance`, `captured_at`, `processed_at`, `failure_reason` |

| Observed API controller | Handler signatures |
| --- | --- |
| [LeadCaptureController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture-api/src/Http/Controllers/LeadCaptureController.php) | `public function index(Request $r, CaptureQuery $q): JsonResponse`<br>`public function store(Request $r, CaptureLead $a): JsonResponse`<br>`public function event(Request $r, CapturedLead $lead, RecordCaptureEvent $a): JsonResponse` |

**Observed route declarations:**

[modules/crm-lead-capture-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/lead-capture')->group(function (): void {
Route::get('/', [LeadCaptureController::class, 'index']);
Route::post('/', [LeadCaptureController::class, 'store']);
Route::post('{lead}/events', [LeadCaptureController::class, 'event']);
```
<!-- layer-implementation-plan:end -->
