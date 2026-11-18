# Real Estate: Real Estate Core Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-core). Observed identity: [`liberusoftware/real-estate-core-filament`](../../../modules/source/liberusoftware--real-estate-core-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-real-estate-core-filament`  
**Matching domain module:** `real-estate-core`  
**Application:** Real Estate  
**Source feature:** [Real Estate Core](../features/real-estate-core.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `real-estate-core` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Agencies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Branches:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Teams:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Territories:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Terminology:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Statuses:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Numbering:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Audit:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-real-estate-core-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `agencies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `branches`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `teams`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `territories`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `terminology`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `statuses`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `numbering`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `audit`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `real-estate-core` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-real-estate-laravel-filament`](https://github.com/liberusoftware/project-real-estate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-real-estate-core-filament`](https://github.com/liberusoftware/module-real-estate-core-filament) (`liberusoftware/real-estate-core-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/real-estate-core.md) · [API plan](../api/real-estate-core.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Agencies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `agencies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Branches** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `branches`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Teams** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `teams`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Territories** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `territories`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Terminology** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `terminology`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Statuses** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `statuses`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Numbering** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `numbering`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Audit** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `audit`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [RealEstateCoreFilamentPlugin.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/RealEstateCoreFilamentPlugin.php) · [RealEstateCoreFilamentServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/RealEstateCoreFilamentServiceProvider.php) · [AgencyResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/AgencyResource.php) · [CreateAgency.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/AgencyResource/Pages/CreateAgency.php) · [EditAgency.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/AgencyResource/Pages/EditAgency.php) · [ListAgencies.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/AgencyResource/Pages/ListAgencies.php) · [BranchResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/BranchResource.php) · [CreateBranch.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/BranchResource/Pages/CreateBranch.php) · [EditBranch.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/BranchResource/Pages/EditBranch.php) · [ListBranches.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/BranchResource/Pages/ListBranches.php) · [StatusDefinitionResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/StatusDefinitionResource.php) · [CreateStatusDefinition.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/StatusDefinitionResource/Pages/CreateStatusDefinition.php) · [EditStatusDefinition.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/StatusDefinitionResource/Pages/EditStatusDefinition.php) · [ListStatusDefinitions.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-filament/src/Resources/StatusDefinitionResource/Pages/ListStatusDefinitions.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AgencyPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Policies/AgencyPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Agency $agency): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Agency $agency): bool`<br>`public function delete(AuthUser $authUser, Agency $agency): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Agency $agency): bool`<br>`public function forceDelete(AuthUser $authUser, Agency $agency): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Agency $agency): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [BranchPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Policies/BranchPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Branch $branch): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Branch $branch): bool`<br>`public function delete(AuthUser $authUser, Branch $branch): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Branch $branch): bool`<br>`public function forceDelete(AuthUser $authUser, Branch $branch): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Branch $branch): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [StatusDefinitionPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Policies/StatusDefinitionPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function delete(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function forceDelete(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, StatusDefinition $statusDefinition): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [TerritoryPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Policies/TerritoryPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Territory $territory): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Territory $territory): bool`<br>`public function delete(AuthUser $authUser, Territory $territory): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Territory $territory): bool`<br>`public function forceDelete(AuthUser $authUser, Territory $territory): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Territory $territory): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Agency.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Agency.php) | No literal fillable array detected; inspect the model and API schema. |
| [AuditEntry.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/AuditEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [Branch.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Branch.php) | No literal fillable array detected; inspect the model and API schema. |
| [CalendarEntry.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/CalendarEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [Communication.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Communication.php) | No literal fillable array detected; inspect the model and API schema. |
| [NumberSequence.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/NumberSequence.php) | No literal fillable array detected; inspect the model and API schema. |
| [StatusDefinition.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/StatusDefinition.php) | No literal fillable array detected; inspect the model and API schema. |
| [Terminology.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core/src/Models/Terminology.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
