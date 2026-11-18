# Crm Lead Qualification React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-lead-qualification). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-lead-qualification-react-native
**Matching core package:** module-crm-crm-lead-qualification ([implementation](../core/crm-lead-qualification.md))
**Matching API package:** module-crm-crm-lead-qualification-api ([contract](../api/crm-lead-qualification.md))

## Implementation plan

This adapter presents Crm Lead Qualification for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Lead Qualification API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-lead-qualification.md), and [API module](../api/crm-lead-qualification.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-lead-qualification`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-lead-qualification.md)) |
| Capability React Native module skeleton | [`module-crm-lead-qualification-react-native`](https://github.com/liberusoftware/module-crm-lead-qualification-react-native) (`@liberusoftware/module-crm-lead-qualification-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Lifecycle stages** | Progressive mobile list/detail/sheet flow for `lifecycle stages` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Fit/engagement scoring** | Progressive mobile list/detail/sheet flow for `fit/engagement scoring` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **MQL/PQL/SQL/service-qualified rules** | Progressive mobile list/detail/sheet flow for `mql/pql/sql/service-qualified rules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Qualification frameworks** | Progressive mobile list/detail/sheet flow for `qualification frameworks` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Disqualification** | Progressive mobile list/detail/sheet flow for `disqualification` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Nurture** | Progressive mobile list/detail/sheet flow for `nurture` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Conversion** | Progressive mobile list/detail/sheet flow for `conversion` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
