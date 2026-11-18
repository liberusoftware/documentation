# Accounting: Accounting Dashboards Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-dashboards). Observed identity: [`liberusoftware/module-accounting-dashboards-filament`](../../../modules/source/liberusoftware--module-accounting-dashboards-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-dashboards-filament`  
**Matching domain module:** `accounting-dashboards`  
**Application:** Accounting  
**Source feature:** [Accounting Dashboards](../features/accounting-dashboards.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-dashboards` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Role-specific KPIs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Widgets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Periods:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dimensions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Targets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Drill-through:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Refresh status:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sharing:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-dashboards-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `role-specific-kpis`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `widgets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `periods`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dimensions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `targets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `drill-through`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `refresh-status`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sharing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-dashboards` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-dashboards-filament`](https://github.com/liberusoftware/module-accounting-dashboards-filament) (`liberusoftware/accounting-dashboards-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-dashboards.md) · [API plan](../api/accounting-dashboards.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Role-specific KPIs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `role-specific kpis`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Widgets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `widgets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Periods** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `periods`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dimensions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dimensions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Targets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `targets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Drill-through** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `drill-through`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Refresh status** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `refresh status`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sharing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sharing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [DashboardsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dashboards-filament/src/DashboardsFilamentPlugin.php) · [DashboardsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dashboards-filament/src/DashboardsFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [DashboardQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dashboards/src/Queries/DashboardQuery.php) | `public function forTeam(int $teamId): Collection`<br>`public function findForTeam(int $teamId, int\|string $id): Dashboard` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDashboard.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dashboards/src/Actions/CreateDashboard.php) | `public function handle(array $attributes): Dashboard` |
| [ShareDashboard.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dashboards/src/Actions/ShareDashboard.php) | `public function handle(Dashboard $dashboard, array $attributes): DashboardShare` |
| [UpsertKpi.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dashboards/src/Actions/UpsertKpi.php) | `public function handle(Dashboard $dashboard, array $attributes): DashboardKpi` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Dashboard.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dashboards/src/Models/Dashboard.php) | `team_id`, `dashboard_ref`, `name`, `role`, `period`, `dimensions`, `metadata` |
| [DashboardKpi.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dashboards/src/Models/DashboardKpi.php) | `dashboard_id`, `team_id`, `kpi_ref`, `label`, `value`, `target`, `unit`, `refreshed_at`, `drill_through` |
| [DashboardShare.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dashboards/src/Models/DashboardShare.php) | `dashboard_id`, `team_id`, `shared_with_user_id`, `shared_with_role`, `token`, `expires_at` |
<!-- layer-implementation-plan:end -->
