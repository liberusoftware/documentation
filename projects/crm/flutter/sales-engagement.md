# Sales Engagement Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sales-engagement). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-sales-engagement-flutter
**Matching core package:** module-crm-sales-engagement ([implementation](../core/sales-engagement.md))
**Matching API package:** module-crm-sales-engagement-api ([contract](../api/sales-engagement.md))

## Implementation plan

This adapter presents Sales Engagement for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Sales Engagement API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/sales-engagement.md), and [API module](../api/sales-engagement.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `sales-engagement`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-sales-engagement-flutter`](https://github.com/liberusoftware/module-crm-sales-engagement-flutter) (`module_crm_sales_engagement_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-sales-engagement-dart-mobile`](https://github.com/liberusoftware/module-crm-sales-engagement-dart-mobile) (`module_crm_sales_engagement_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-sales-engagement-dart-desktop`](https://github.com/liberusoftware/module-crm-sales-engagement-dart-desktop) (`module_crm_sales_engagement_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/sales-engagement.md) · [Core plan](../core/sales-engagement.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Sequences/cadences** | Adaptive mobile cards/sheets for `sequences/cadences` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `sequences/cadences` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Multi-channel steps** | Adaptive mobile cards/sheets for `multi-channel steps` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `multi-channel steps` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Templates/snippets** | Adaptive mobile cards/sheets for `templates/snippets` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `templates/snippets` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Task queues** | Adaptive mobile cards/sheets for `task queues` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `task queues` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Enrollment/re-entry** | Adaptive mobile cards/sheets for `enrollment/re-entry` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `enrollment/re-entry` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Throttles** | Adaptive mobile cards/sheets for `throttles` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `throttles` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Timezone windows** | Adaptive mobile cards/sheets for `timezone windows` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `timezone windows` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Reply/meeting stop rules** | Adaptive mobile cards/sheets for `reply/meeting stop rules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `reply/meeting stop rules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Experiments** | Adaptive mobile cards/sheets for `experiments` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `experiments` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EngagementQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Queries/EngagementQuery.php) | `public function sequences(int $teamId)`<br>`public function enrollments(int $teamId)`<br>`public function tasks(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddStep.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/AddStep.php) | `public function execute(int $teamId, int $actorId, array $data): EngagementStep` |
| [CreateSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/CreateSequence.php) | `public function execute(int $teamId, int $actorId, array $data): EngagementSequence` |
| [EnrollContact.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/EnrollContact.php) | `public function execute(int $teamId, int $actorId, array $data): Enrollment` |
| [RecordEngagementEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/RecordEngagementEvent.php) | `public function execute(int $teamId, int $actorId, array $data): EngagementEvent` |
| [StopEnrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/StopEnrollment.php) | `public function execute(int $teamId, int $actorId, int $id, string $reason): Enrollment` |
| [UpdateSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/UpdateSequence.php) | `public function execute(int $teamId, int $actorId, int $sequenceId, array $data): EngagementSequence` |
| [EngagementPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Services/EngagementPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EngagementEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/EngagementEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [EngagementSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/EngagementSequence.php) | No literal fillable array detected; inspect the model and API schema. |
| [EngagementStep.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/EngagementStep.php) | No literal fillable array detected; inspect the model and API schema. |
| [EngagementTask.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/EngagementTask.php) | No literal fillable array detected; inspect the model and API schema. |
| [Enrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/Enrollment.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [EngagementController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement-api/src/Http/Controllers/EngagementController.php) | `public function sequences(Request $r, EngagementQuery $q)`<br>`public function sequence(Request $r, CreateSequence $a)`<br>`public function step(Request $r, AddStep $a)`<br>`public function enrollments(Request $r, EngagementQuery $q)`<br>`public function enroll(Request $r, EnrollContact $a)`<br>`public function stop(Request $r, int $enrollment, string $reason, StopEnrollment $a)`<br>`public function tasks(Request $request, EngagementQuery $query)`<br>`public function complete(Request $request, int $task, CompleteEngagementTask $action)`<br>`public function event(Request $r, RecordEngagementEvent $a)` |

**Observed route declarations:**

[modules/crm-sales-engagement-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/sales-engagement')->group(function (): void {
Route::get('/sequences', [EngagementController::class, 'sequences']);
Route::post('/sequences', [EngagementController::class, 'sequence']);
Route::post('/steps', [EngagementController::class, 'step']);
Route::get('/enrollments', [EngagementController::class, 'enrollments']);
Route::post('/enrollments', [EngagementController::class, 'enroll']);
Route::post('/enrollments/{enrollment}/stop/{reason}', [EngagementController::class, 'stop']);
Route::get('/tasks', [EngagementController::class, 'tasks']);
Route::post('/tasks/{task}/complete', [EngagementController::class, 'complete']);
Route::post('/events', [EngagementController::class, 'event']);
```
<!-- layer-implementation-plan:end -->
