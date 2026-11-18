# Customer Data Model Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#customer-data-model). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-customer-data-model-flutter
**Matching core package:** module-crm-customer-data-model ([implementation](../core/customer-data-model.md))
**Matching API package:** module-crm-customer-data-model-api ([contract](../api/customer-data-model.md))

## Implementation plan

This adapter presents Customer Data Model for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Customer Data Model API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/customer-data-model.md), and [API module](../api/customer-data-model.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `customer-data-model`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-customer-data-model-flutter`](https://github.com/liberusoftware/module-crm-customer-data-model-flutter) (`module_crm_customer_data_model_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-customer-data-model-dart-mobile`](https://github.com/liberusoftware/module-crm-customer-data-model-dart-mobile) (`module_crm_customer_data_model_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-customer-data-model-dart-desktop`](https://github.com/liberusoftware/module-crm-customer-data-model-dart-desktop) (`module_crm_customer_data_model_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/customer-data-model.md) · [Core plan](../core/customer-data-model.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Standard/custom objects** | Adaptive mobile cards/sheets for `standard/custom objects` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `standard/custom objects` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Fields** | Adaptive mobile cards/sheets for `fields` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `fields` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Relationships** | Adaptive mobile cards/sheets for `relationships` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `relationships` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Layouts** | Adaptive mobile cards/sheets for `layouts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `layouts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Validation** | Adaptive mobile cards/sheets for `validation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `validation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Calculated fields** | Adaptive mobile cards/sheets for `calculated fields` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `calculated fields` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Required-by-stage fields** | Adaptive mobile cards/sheets for `required-by-stage fields` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `required-by-stage fields` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Schema versioning** | Adaptive mobile cards/sheets for `schema versioning` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `schema versioning` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateObject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Actions/CreateObject.php) | `public function execute(int $teamId, array $attributes): ObjectDefinition` |
| [PublishSchema.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Actions/PublishSchema.php) | `public function execute(ObjectDefinition $object, ?int $actorId = null): SchemaVersion` |
| [SchemaValidator.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Contracts/SchemaValidator.php) | `public function validate(ObjectDefinition $object, array $values, ?string $stage = null): array` |
| [SchemaValidationService.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Services/SchemaValidationService.php) | `public function validate(ObjectDefinition $object, array $values, ?string $stage = null): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FieldDefinition.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Models/FieldDefinition.php) | `object_id`, `key`, `label`, `type`, `description`, `config`, `is_required`, `is_calculated`, `calculation`, `required_stages`, `position` |
| [LayoutDefinition.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Models/LayoutDefinition.php) | `object_id`, `key`, `label`, `sections`, `is_default` |
| [ObjectDefinition.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Models/ObjectDefinition.php) | `team_id`, `key`, `label`, `description`, `is_standard`, `status`, `current_version` |
| [RelationshipDefinition.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Models/RelationshipDefinition.php) | `team_id`, `from_object_id`, `to_object_id`, `key`, `label`, `cardinality`, `config` |
| [SchemaVersion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Models/SchemaVersion.php) | `object_id`, `version`, `status`, `snapshot`, `published_by`, `published_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ObjectDefinitionController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model-api/src/Http/Controllers/ObjectDefinitionController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateObject $create): JsonResponse`<br>`public function show(Request $request, int $object): JsonResponse`<br>`public function update(Request $request, int $object): JsonResponse`<br>`public function publish(Request $request, int $object, PublishSchema $publish): JsonResponse` |

**Observed route declarations:**

[modules/crm-customer-data-model-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model-api/routes/api.php)

```php
Route::prefix('api/v1/crm/customer-data-model')->middleware(['auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [ObjectDefinitionController::class, 'index'])->name('crm.customer.data.model.list');
Route::post('/', [ObjectDefinitionController::class, 'store'])->name('crm.customer.data.model.create');
Route::get('/{object}', [ObjectDefinitionController::class, 'show'])->name('crm.customer.data.model.get');
Route::patch('/{object}', [ObjectDefinitionController::class, 'update'])->name('crm.customer.data.model.update');
Route::post('/{object}/publish', [ObjectDefinitionController::class, 'publish'])->name('crm.customer.data.model.publish');
```
<!-- layer-implementation-plan:end -->
