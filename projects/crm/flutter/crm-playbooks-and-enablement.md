# Crm Playbooks And Enablement Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-playbooks-and-enablement). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-playbooks-and-enablement-flutter
**Matching core package:** module-crm-crm-playbooks-and-enablement ([implementation](../core/crm-playbooks-and-enablement.md))
**Matching API package:** module-crm-crm-playbooks-and-enablement-api ([contract](../api/crm-playbooks-and-enablement.md))

## Implementation plan

This adapter presents Crm Playbooks And Enablement for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Playbooks And Enablement API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/crm-playbooks-and-enablement.md), and [API module](../api/crm-playbooks-and-enablement.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `crm-playbooks-and-enablement`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-playbooks-and-enablement-flutter`](https://github.com/liberusoftware/module-crm-playbooks-and-enablement-flutter) (`module_crm_playbooks_and_enablement_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-playbooks-and-enablement-dart-mobile`](https://github.com/liberusoftware/module-crm-playbooks-and-enablement-dart-mobile) (`module_crm_playbooks_and_enablement_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-playbooks-and-enablement-dart-desktop`](https://github.com/liberusoftware/module-crm-playbooks-and-enablement-dart-desktop) (`module_crm_playbooks_and_enablement_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/crm-playbooks-and-enablement.md) · [Core plan](../core/crm-playbooks-and-enablement.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Guided scripts** | Adaptive mobile cards/sheets for `guided scripts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `guided scripts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Qualification cards** | Adaptive mobile cards/sheets for `qualification cards` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `qualification cards` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Battlecards** | Adaptive mobile cards/sheets for `battlecards` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `battlecards` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Onboarding content** | Adaptive mobile cards/sheets for `onboarding content` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `onboarding content` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Required evidence** | Adaptive mobile cards/sheets for `required evidence` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `required evidence` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Coaching checklists** | Adaptive mobile cards/sheets for `coaching checklists` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `coaching checklists` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Document/content recommendations** | Adaptive mobile cards/sheets for `document/content recommendations` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `document/content recommendations` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Usage analytics** | Adaptive mobile cards/sheets for `usage analytics` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `usage analytics` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PlaybookQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Queries/PlaybookQuery.php) | `public function playbooks(int $teamId)`<br>`public function assignments(int $teamId)`<br>`public function recommendations(int $teamId)`<br>`public function usage(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AssignPlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/AssignPlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PlaybookAssignment` |
| [CompletePlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/CompletePlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $assignmentId, array $input): PlaybookAssignment` |
| [CreatePlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/CreatePlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Playbook` |
| [RecommendPlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/RecommendPlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PlaybookRecommendation` |
| [RecordPlaybookUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/RecordPlaybookUsage.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PlaybookUsage` |
| [UpdatePlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/UpdatePlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $playbookId, array $input): Playbook` |
| [PlaybookPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Services/PlaybookPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Playbook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Models/Playbook.php) | No literal fillable array detected; inspect the model and API schema. |
| [PlaybookAssignment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Models/PlaybookAssignment.php) | No literal fillable array detected; inspect the model and API schema. |
| [PlaybookRecommendation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Models/PlaybookRecommendation.php) | No literal fillable array detected; inspect the model and API schema. |
| [PlaybookUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Models/PlaybookUsage.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [PlaybooksAndEnablementController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement-api/src/Http/Controllers/PlaybooksAndEnablementController.php) | `public function playbooks(Request $r, PlaybookQuery $q)`<br>`public function playbook(Request $r, CreatePlaybook $a)`<br>`public function assignment(Request $r, AssignPlaybook $a)`<br>`public function complete(Request $r, int $assignment, CompletePlaybook $a)`<br>`public function recommendation(Request $r, RecommendPlaybook $a)`<br>`public function usage(Request $r, RecordPlaybookUsage $a)` |

**Observed route declarations:**

[modules/crm-playbooks-and-enablement-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/playbooks-and-enablement')->group(function (): void {
Route::get('/playbooks', [PlaybooksAndEnablementController::class, 'playbooks']);
Route::post('/playbooks', [PlaybooksAndEnablementController::class, 'playbook']);
Route::post('/assignments', [PlaybooksAndEnablementController::class, 'assignment']);
Route::post('/assignments/{assignment}/complete', [PlaybooksAndEnablementController::class, 'complete']);
Route::post('/recommendations', [PlaybooksAndEnablementController::class, 'recommendation']);
Route::post('/usage', [PlaybooksAndEnablementController::class, 'usage']);
```
<!-- layer-implementation-plan:end -->
