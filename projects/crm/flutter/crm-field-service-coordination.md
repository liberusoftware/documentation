# Crm Field Service Coordination Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-field-service-coordination). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-field-service-coordination-flutter
**Matching core package:** module-crm-crm-field-service-coordination ([implementation](../core/crm-field-service-coordination.md))
**Matching API package:** module-crm-crm-field-service-coordination-api ([contract](../api/crm-field-service-coordination.md))

## Implementation plan

This adapter presents Crm Field Service Coordination for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Field Service Coordination API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/crm-field-service-coordination.md), and [API module](../api/crm-field-service-coordination.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `crm-field-service-coordination`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-field-service-coordination-flutter`](https://github.com/liberusoftware/module-crm-field-service-coordination-flutter) (`module_crm_field_service_coordination_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-field-service-coordination-dart-mobile`](https://github.com/liberusoftware/module-crm-field-service-coordination-dart-mobile) (`module_crm_field_service_coordination_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-field-service-coordination-dart-desktop`](https://github.com/liberusoftware/module-crm-field-service-coordination-dart-desktop) (`module_crm_field_service_coordination_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/crm-field-service-coordination.md) · [Core plan](../core/crm-field-service-coordination.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Work types** | Adaptive mobile cards/sheets for `work types` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `work types` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Service appointments** | Adaptive mobile cards/sheets for `service appointments` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `service appointments` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Dispatch references** | Adaptive mobile cards/sheets for `dispatch references` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `dispatch references` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Technician/contractor visibility** | Adaptive mobile cards/sheets for `technician/contractor visibility` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `technician/contractor visibility` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Asset/service history** | Adaptive mobile cards/sheets for `asset/service history` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `asset/service history` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Maintenance module handoff** | Adaptive mobile cards/sheets for `maintenance module handoff` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `maintenance module handoff` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [FieldServiceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Queries/FieldServiceQuery.php) | `public function workTypes(int $teamId)`<br>`public function appointments(int $teamId)`<br>`public function assets(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateWorkType.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Actions/CreateWorkType.php) | `public function __construct(private readonly FieldServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): WorkType` |
| [HandOffMaintenance.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Actions/HandOffMaintenance.php) | `public function __construct(private readonly FieldServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, ServiceAppointment $appointment, array $input): MaintenanceHandoff` |
| [RecordServiceHistory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Actions/RecordServiceHistory.php) | `public function __construct(private readonly FieldServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, ServiceAppointment $appointment, array $input): ServiceHistory` |
| [ScheduleAppointment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Actions/ScheduleAppointment.php) | `public function __construct(private readonly FieldServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ServiceAppointment` |
| [FieldServicePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Services/FieldServicePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MaintenanceHandoff.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Models/MaintenanceHandoff.php) | No literal fillable array detected; inspect the model and API schema. |
| [ServiceAppointment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Models/ServiceAppointment.php) | No literal fillable array detected; inspect the model and API schema. |
| [ServiceAsset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Models/ServiceAsset.php) | No literal fillable array detected; inspect the model and API schema. |
| [ServiceHistory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Models/ServiceHistory.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkType.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Models/WorkType.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [FieldServiceController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination-api/src/Http/Controllers/FieldServiceController.php) | `public function __construct(private readonly FieldServiceQuery $query)`<br>`public function workTypes(): JsonResponse`<br>`public function appointments(): JsonResponse`<br>`public function storeWorkType(CreateWorkType $action): JsonResponse`<br>`public function schedule(ScheduleAppointment $action): JsonResponse`<br>`public function history(ServiceAppointment $appointment, RecordServiceHistory $action): JsonResponse`<br>`public function handoff(ServiceAppointment $appointment, HandOffMaintenance $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-field-service-coordination-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/field-service-coordination')->group(function (): void {
Route::get('work-types', [FieldServiceController::class, 'workTypes']);
Route::get('appointments', [FieldServiceController::class, 'appointments']);
Route::post('work-types', [FieldServiceController::class, 'storeWorkType']);
Route::post('appointments', [FieldServiceController::class, 'schedule']);
Route::post('appointments/{appointment}/history', [FieldServiceController::class, 'history']);
Route::post('appointments/{appointment}/maintenance-handoff', [FieldServiceController::class, 'handoff']);
```
<!-- layer-implementation-plan:end -->
