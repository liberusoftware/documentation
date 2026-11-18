# Accounting: Projects and Jobs Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#projects-and-jobs). Observed identity: [`liberusoftware/module-accounting-projects-and-jobs-filament`](../../../modules/source/liberusoftware--module-accounting-projects-and-jobs-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-projects-and-jobs-filament`  
**Matching domain module:** `accounting-projects-and-jobs`  
**Application:** Accounting  
**Source feature:** [Projects and Jobs](../features/projects-and-jobs.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-projects-and-jobs` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Customers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Project/job hierarchy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Status:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Managers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Budgets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dimensions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Source links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Lifecycle:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-projects-and-jobs-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `customers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `project-job-hierarchy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `status`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `managers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `budgets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dimensions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `source-links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `lifecycle`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-projects-and-jobs` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-projects-and-jobs-filament`](https://github.com/liberusoftware/module-accounting-projects-and-jobs-filament) (`liberusoftware/accounting-projects-and-jobs-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/projects-and-jobs.md) · [API plan](../api/projects-and-jobs.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Customers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `customers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Project/job hierarchy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `project/job hierarchy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Status** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `status`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Managers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `managers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Budgets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `budgets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dimensions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dimensions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Source links** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `source links`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Lifecycle** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lifecycle`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ProjectsAndJobsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs-filament/src/ProjectsAndJobsFilamentPlugin.php) · [ProjectsAndJobsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs-filament/src/ProjectsAndJobsFilamentServiceProvider.php) · [ListProjectJobs.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs-filament/src/Resources/Pages/ListProjectJobs.php) · [ProjectJobResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs-filament/src/Resources/ProjectJobResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateProjectJob.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs/src/Actions/CreateProjectJob.php) | `public function handle(array $attributes): ProjectJob` |
| [TransitionProject.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs/src/Actions/TransitionProject.php) | `public function handle(ProjectJob $project, ProjectStatus $status): ProjectJob` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ProjectCustomer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs/src/Models/ProjectCustomer.php) | `team_id`, `customer_ref`, `name`, `status`, `metadata` |
| [ProjectJob.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs/src/Models/ProjectJob.php) | `team_id`, `customer_id`, `parent_id`, `name`, `code`, `description`, `start_date`, `end_date`, `status`, `manager_ref`, `budget_amount`, `budget_currency`, `dimensions`, `source_links`, `metadata` |
<!-- layer-implementation-plan:end -->
