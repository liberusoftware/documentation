# CRM: Sales Workspace Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sales-workspace). Observed identity: [`liberusoftware/module-crm-sales-workspace-filament`](../../../modules/source/liberusoftware--module-crm-sales-workspace-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-sales-workspace-filament`  
**Matching domain module:** `crm-sales-workspace`  
**Application:** CRM  
**Source feature:** [Sales Workspace](../features/sales-workspace.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-sales-workspace` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Prioritized seller feed:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Leads/deals inbox:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Overdue/risk indicators:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Next best action:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Daily agenda:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Quick updates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Contextual customer history:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-sales-workspace-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `prioritized-seller-feed`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `leads-deals-inbox`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `overdue-risk-indicators`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `next-best-action`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `daily-agenda`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `quick-updates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `contextual-customer-history`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-sales-workspace` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-sales-workspace-filament`](https://github.com/liberusoftware/module-crm-sales-workspace-filament) (`liberusoftware/crm-sales-workspace-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/sales-workspace.md) · [API plan](../api/sales-workspace.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Prioritized seller feed** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `prioritized seller feed`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Leads/deals inbox** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `leads/deals inbox`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Overdue/risk indicators** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `overdue/risk indicators`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Next best action** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `next best action`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Daily agenda** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `daily agenda`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Quick updates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `quick updates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Contextual customer history** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `contextual customer history`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [WorkspaceItemResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace-filament/src/Resources/WorkspaceItemResource.php) · [ListWorkspaceItems.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace-filament/src/Resources/WorkspaceItemResource/Pages/ListWorkspaceItems.php) · [SalesWorkspaceFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace-filament/src/SalesWorkspaceFilamentPlugin.php) · [SalesWorkspaceFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace-filament/src/SalesWorkspaceFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [WorkspaceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace/src/Queries/WorkspaceQuery.php) | `public function feed(int $teamId)`<br>`public function overdue(int $teamId)`<br>`public function agenda(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateWorkspaceItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace/src/Actions/CreateWorkspaceItem.php) | `public function execute(int $teamId, int $actorId, array $data): WorkspaceItem` |
| [QuickUpdate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace/src/Actions/QuickUpdate.php) | `public function execute(int $teamId, int $actorId, int $id, array $data): WorkspaceUpdate` |
| [WorkspacePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace/src/Services/WorkspacePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WorkspaceItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace/src/Models/WorkspaceItem.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkspaceUpdate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-workspace/src/Models/WorkspaceUpdate.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
