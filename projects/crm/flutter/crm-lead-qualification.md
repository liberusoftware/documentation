# Crm Lead Qualification Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-lead-qualification). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-lead-qualification-flutter
**Matching core package:** module-crm-crm-lead-qualification ([implementation](../core/crm-lead-qualification.md))
**Matching API package:** module-crm-crm-lead-qualification-api ([contract](../api/crm-lead-qualification.md))

## Implementation plan

This adapter presents Crm Lead Qualification for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Lead Qualification API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/crm-lead-qualification.md), and [API module](../api/crm-lead-qualification.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `crm-lead-qualification`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-lead-qualification-flutter`](https://github.com/liberusoftware/module-crm-lead-qualification-flutter) (`module_crm_lead_qualification_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-lead-qualification-dart-mobile`](https://github.com/liberusoftware/module-crm-lead-qualification-dart-mobile) (`module_crm_lead_qualification_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-lead-qualification-dart-desktop`](https://github.com/liberusoftware/module-crm-lead-qualification-dart-desktop) (`module_crm_lead_qualification_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/crm-lead-qualification.md) · [Core plan](../core/crm-lead-qualification.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Lifecycle stages** | Adaptive mobile cards/sheets for `lifecycle stages` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `lifecycle stages` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Fit/engagement scoring** | Adaptive mobile cards/sheets for `fit/engagement scoring` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `fit/engagement scoring` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **MQL/PQL/SQL/service-qualified rules** | Adaptive mobile cards/sheets for `mql/pql/sql/service-qualified rules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `mql/pql/sql/service-qualified rules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Qualification frameworks** | Adaptive mobile cards/sheets for `qualification frameworks` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `qualification frameworks` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Disqualification** | Adaptive mobile cards/sheets for `disqualification` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `disqualification` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Nurture** | Adaptive mobile cards/sheets for `nurture` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `nurture` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Conversion** | Adaptive mobile cards/sheets for `conversion` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `conversion` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [LeadQualificationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Queries/LeadQualificationQuery.php) | `public function forTeam(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConvertQualification.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/ConvertQualification.php) | `public function execute(LeadQualification $qualification, ?int $actorId, ?string $reason = null): LeadQualification` |
| [CreateFramework.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/CreateFramework.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): QualificationFramework` |
| [CreateQualification.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/CreateQualification.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): LeadQualification` |
| [DisqualifyQualification.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/DisqualifyQualification.php) | `public function execute(LeadQualification $qualification, ?int $actorId, string $reason): LeadQualification` |
| [EnrollNurture.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/EnrollNurture.php) | `public function execute(LeadQualification $qualification, ?int $actorId, array $attributes): NurtureEnrollment` |
| [EvaluateQualification.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/EvaluateQualification.php) | `public function execute(LeadQualification $qualification, ?int $actorId): LeadQualification` |
| [RecordQualificationEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/RecordQualificationEvent.php) | `public function __construct(private readonly LeadQualificationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, QualifiedLead $lead, array $input): QualificationEvent` |
| [ScoreLead.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/ScoreLead.php) | `public function __construct(private readonly LeadQualificationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, QualifiedLead $lead, array $input): QualifiedLead` |
| [TransitionLifecycle.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/TransitionLifecycle.php) | `public function execute(LeadQualification $qualification, ?int $actorId, string $stage, ?string $reason = null): LeadQualification` |
| [UpdateScores.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/UpdateScores.php) | `public function execute(LeadQualification $qualification, ?int $actorId, array $scores): LeadQualification` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [LeadQualification.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/LeadQualification.php) | `team_id`, `actor_id`, `subject_type`, `subject_id`, `framework_id`, `lifecycle_stage`, `fit_score`, `engagement_score`, `total_score`, `qualification_status`, `disqualification_reason`, `nurture_until`, `converted_at`, `version`, `metadata` |
| [NurtureEnrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/NurtureEnrollment.php) | `team_id`, `qualification_id`, `actor_id`, `status`, `sequence`, `starts_at`, `ends_at`, `metadata` |
| [QualificationEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/QualificationEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [QualificationFramework.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/QualificationFramework.php) | `team_id`, `actor_id`, `name`, `status`, `mql_threshold`, `pql_threshold`, `sql_threshold`, `service_qualified_threshold`, `rules`, `settings` |
| [QualificationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/QualificationRule.php) | No literal fillable array detected; inspect the model and API schema. |
| [QualifiedLead.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/QualifiedLead.php) | No literal fillable array detected; inspect the model and API schema. |
| [StageHistory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/StageHistory.php) | `team_id`, `qualification_id`, `actor_id`, `from_stage`, `to_stage`, `reason` |

| Observed API controller | Handler signatures |
| --- | --- |
| [LeadQualificationController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification-api/src/Http/Controllers/LeadQualificationController.php) | `public function index(Request $r, LeadQualificationQuery $q): JsonResponse`<br>`public function store(Request $r, UpsertLead $a): JsonResponse`<br>`public function score(Request $r, QualifiedLead $lead, ScoreLead $a): JsonResponse`<br>`public function event(Request $r, QualifiedLead $lead, RecordQualificationEvent $a): JsonResponse` |

**Observed route declarations:**

[modules/crm-lead-qualification-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/lead-qualification')->group(function (): void {
Route::get('/', [LeadQualificationController::class, 'index']);
Route::post('/', [LeadQualificationController::class, 'store']);
Route::post('{lead}/score', [LeadQualificationController::class, 'score']);
Route::post('{lead}/events', [LeadQualificationController::class, 'event']);
```
<!-- layer-implementation-plan:end -->
