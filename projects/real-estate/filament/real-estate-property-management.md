# Real Estate: Real Estate Property Management Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-property-management). Observed identity: [`liberusoftware/real-estate-property-management-filament`](../../../modules/source/liberusoftware--real-estate-property-management-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-real-estate-real-estate-property-management-filament`  
**Matching domain module:** `real-estate-property-management`  
**Application:** Real Estate  
**Source feature:** [Real Estate Property Management](../features/real-estate-property-management.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `real-estate-property-management` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Rent schedule:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Statements:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Inspections:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Compliance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Maintenance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Contractors:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Owner approvals:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-real-estate-real-estate-property-management-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `rent-schedule`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `statements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `inspections`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `compliance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `maintenance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `contractors`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `owner-approvals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `real-estate-property-management` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-real-estate-laravel-filament`](https://github.com/liberusoftware/project-real-estate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-real-estate-property-management-filament`](https://github.com/liberusoftware/module-real-estate-property-management-filament) (`liberusoftware/real-estate-property-management-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/real-estate-property-management.md) · [API plan](../api/real-estate-property-management.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Rent schedule** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rent schedule`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Statements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `statements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Inspections** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `inspections`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Compliance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `compliance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Maintenance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `maintenance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Contractors** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `contractors`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Owner approvals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `owner approvals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PropertyManagementFilamentPlugin.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/PropertyManagementFilamentPlugin.php) · [PropertyManagementFilamentServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/PropertyManagementFilamentServiceProvider.php) · [InspectionResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/InspectionResource.php) · [CreateInspection.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/InspectionResource/Pages/CreateInspection.php) · [EditInspection.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/InspectionResource/Pages/EditInspection.php) · [ListInspections.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/InspectionResource/Pages/ListInspections.php) · [MaintenanceRequestResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/MaintenanceRequestResource.php) · [CreateMaintenanceRequest.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/MaintenanceRequestResource/Pages/CreateMaintenanceRequest.php) · [EditMaintenanceRequest.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/MaintenanceRequestResource/Pages/EditMaintenanceRequest.php) · [ListMaintenanceRequests.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/MaintenanceRequestResource/Pages/ListMaintenanceRequests.php) · [ManagementRecordResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/ManagementRecordResource.php) · [CreateManagementRecord.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/ManagementRecordResource/Pages/CreateManagementRecord.php) · [EditManagementRecord.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/ManagementRecordResource/Pages/EditManagementRecord.php) · [ListManagementRecords.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-filament/src/Resources/ManagementRecordResource/Pages/ListManagementRecords.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListManagementRecords.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Queries/ListManagementRecords.php) | `public function handle(int\|string $teamId, ?string $capability = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ManagementRecordPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Policies/ManagementRecordPolicy.php) | `public function view($user, ManagementRecord $record): bool`<br>`public function update($user, ManagementRecord $record): bool`<br>`public function delete($user, ManagementRecord $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Inspection.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/Inspection.php) | No literal fillable array detected; inspect the model and API schema. |
| [MaintenanceRequest.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/MaintenanceRequest.php) | No literal fillable array detected; inspect the model and API schema. |
| [ManagementRecord.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/ManagementRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [VendorQuote.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/VendorQuote.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkOrder.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/WorkOrder.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkOrderUpdate.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/WorkOrderUpdate.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
