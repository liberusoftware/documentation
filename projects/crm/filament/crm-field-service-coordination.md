# CRM: Crm Field Service Coordination Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-field-service-coordination). Observed identity: [`liberusoftware/module-crm-field-service-coordination-filament`](../../../modules/source/liberusoftware--module-crm-field-service-coordination-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-field-service-coordination-filament`  
**Matching domain module:** `crm-field-service-coordination`  
**Application:** CRM  
**Source feature:** [Crm Field Service Coordination](../features/crm-field-service-coordination.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-field-service-coordination` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Work types:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Service appointments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dispatch references:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Technician/contractor visibility:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Asset/service history:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Maintenance module handoff:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-field-service-coordination-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `work-types`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `service-appointments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dispatch-references`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `technician-contractor-visibility`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `asset-service-history`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `maintenance-module-handoff`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-field-service-coordination` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-field-service-coordination-filament`](https://github.com/liberusoftware/module-crm-field-service-coordination-filament) (`liberusoftware/crm-field-service-coordination-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-field-service-coordination.md) · [API plan](../api/crm-field-service-coordination.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Work types** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `work types`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Service appointments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `service appointments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dispatch references** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dispatch references`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Technician/contractor visibility** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `technician/contractor visibility`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Asset/service history** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `asset/service history`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Maintenance module handoff** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `maintenance module handoff`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [FieldServiceCoordinationFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination-filament/src/FieldServiceCoordinationFilamentServiceProvider.php) · [CreateServiceAppointment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination-filament/src/Resources/Pages/CreateServiceAppointment.php) · [EditServiceAppointment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination-filament/src/Resources/Pages/EditServiceAppointment.php) · [ListServiceAppointments.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination-filament/src/Resources/Pages/ListServiceAppointments.php) · [ServiceAppointmentResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination-filament/src/Resources/ServiceAppointmentResource.php).

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
<!-- layer-implementation-plan:end -->
