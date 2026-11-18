# Accounting: Accountant Workspace Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accountant-workspace). Observed identity: [`liberusoftware/module-accounting-accountant-workspace-filament`](../../../modules/source/liberusoftware--module-accounting-accountant-workspace-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accountant-workspace-filament`  
**Matching domain module:** `accounting-accountant-workspace`  
**Application:** Accounting  
**Source feature:** [Accountant Workspace](../features/accountant-workspace.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-accountant-workspace` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Client/entity portfolio:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Status:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Deadlines:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Alerts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Access:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Notes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Requests:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recent changes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Drill-through:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accountant-workspace-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `client-entity-portfolio`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `status`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `deadlines`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `alerts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `access`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `notes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `requests`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recent-changes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `drill-through`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-accountant-workspace` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-accountant-workspace-filament`](https://github.com/liberusoftware/module-accounting-accountant-workspace-filament) (`liberusoftware/accounting-accountant-workspace-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accountant-workspace.md) · [API plan](../api/accountant-workspace.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Client/entity portfolio** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `client/entity portfolio`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Status** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `status`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Deadlines** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `deadlines`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Alerts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `alerts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Access** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `access`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Notes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `notes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Requests** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `requests`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recent changes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recent changes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Drill-through** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `drill-through`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AccountantWorkspaceFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accountant-workspace-filament/src/AccountantWorkspaceFilamentServiceProvider.php) · [CreateWorkspaceItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accountant-workspace-filament/src/Resources/Pages/CreateWorkspaceItem.php) · [ListWorkspaceItems.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accountant-workspace-filament/src/Resources/Pages/ListWorkspaceItems.php) · [WorkspaceItemResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accountant-workspace-filament/src/Resources/WorkspaceItemResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [WorkspaceQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accountant-workspace/src/Queries/WorkspaceQuery.php) | `public function paginate(int $teamId, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateWorkspaceItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accountant-workspace/src/Actions/CreateWorkspaceItem.php) | `public function handle(array $attributes): WorkspaceItem` |
| [WorkspacePolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accountant-workspace-api/src/Policies/WorkspacePolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WorkspaceItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accountant-workspace/src/Models/WorkspaceItem.php) | `team_id`, `subject_type`, `subject_id`, `name`, `status`, `next_deadline`, `alerts`, `notes`, `requests`, `metadata` |
<!-- layer-implementation-plan:end -->
