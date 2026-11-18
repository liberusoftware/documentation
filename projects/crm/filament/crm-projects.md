# CRM: Crm Projects Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-projects). Observed identity: [`liberusoftware/module-crm-projects-filament`](../../../modules/source/liberusoftware--module-crm-projects-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-projects-filament`  
**Matching domain module:** `crm-projects`  
**Application:** CRM  
**Source feature:** [Crm Projects](../features/crm-projects.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-projects` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Post-sale projects:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Templates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Milestones:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tasks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dependencies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Owners:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Time:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Files:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Status:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Risks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Client visibility:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Opportunity handoff:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-projects-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `post-sale-projects`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `templates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `milestones`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tasks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dependencies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `owners`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `time`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `files`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `status`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `risks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `client-visibility`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `opportunity-handoff`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-projects` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-projects-filament`](https://github.com/liberusoftware/module-crm-projects-filament) (`liberusoftware/crm-projects-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-projects.md) · [API plan](../api/crm-projects.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Post-sale projects** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `post-sale projects`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Templates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `templates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Milestones** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `milestones`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tasks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tasks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dependencies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dependencies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Owners** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `owners`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Time** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `time`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Files** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `files`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Status** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `status`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Risks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `risks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Client visibility** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `client visibility`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Opportunity handoff** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `opportunity handoff`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ProjectsFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects-filament/src/ProjectsFilamentPlugin.php) · [ProjectsFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects-filament/src/ProjectsFilamentServiceProvider.php) · [ProjectResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects-filament/src/Resources/ProjectResource.php) · [CreateProject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects-filament/src/Resources/ProjectResource/Pages/CreateProject.php) · [EditProject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects-filament/src/Resources/ProjectResource/Pages/EditProject.php) · [ListProjects.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects-filament/src/Resources/ProjectResource/Pages/ListProjects.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ProjectQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Queries/ProjectQuery.php) | `public function templates(int $teamId)`<br>`public function projects(int $teamId)`<br>`public function tasks(int $teamId)`<br>`public function risks(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ChangeProjectStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/ChangeProjectStatus.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $projectId, string $status): Project` |
| [CreateProject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/CreateProject.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Project` |
| [CreateProjectTask.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/CreateProjectTask.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProjectTask` |
| [HandoffOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/HandoffOpportunity.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $projectId, int $opportunityId): Project` |
| [LogProjectTime.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/LogProjectTime.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProjectTime` |
| [RecordProjectRisk.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/RecordProjectRisk.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProjectRisk` |
| [UpdateProject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Actions/UpdateProject.php) | `public function __construct(private readonly ProjectPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $projectId, array $input): Project` |
| [ProjectPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Services/ProjectPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Project.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/Project.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProjectEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/ProjectEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProjectRisk.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/ProjectRisk.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProjectTask.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/ProjectTask.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProjectTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/ProjectTemplate.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProjectTime.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-projects/src/Models/ProjectTime.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
