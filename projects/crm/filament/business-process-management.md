# CRM: Business Process Management Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#business-process-management). Observed identity: [`liberusoftware/module-crm-business-process-management-filament`](../../../modules/source/liberusoftware--module-crm-business-process-management-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-business-process-management-filament`  
**Matching domain module:** `crm-business-process-management`  
**Application:** CRM  
**Source feature:** [Business Process Management](../features/business-process-management.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-business-process-management` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Guided stages:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Required steps/data:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approvals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Validations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Service processes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Exception routing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Process versioning:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-business-process-management-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `guided-stages`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `required-steps-data`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approvals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `validations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `service-processes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `exception-routing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `process-versioning`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-business-process-management` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-business-process-management-filament`](https://github.com/liberusoftware/module-crm-business-process-management-filament) (`liberusoftware/crm-business-process-management-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/business-process-management.md) · [API plan](../api/business-process-management.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Guided stages** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `guided stages`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Required steps/data** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `required steps/data`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approvals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approvals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Validations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `validations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Service processes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `service processes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Exception routing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exception routing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Process versioning** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `process versioning`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [BusinessProcessManagementFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management-filament/src/BusinessProcessManagementFilamentPlugin.php) · [BusinessProcessManagementFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management-filament/src/BusinessProcessManagementFilamentServiceProvider.php) · [ProcessResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management-filament/src/Resources/ProcessResource.php) · [CreateProcessPage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management-filament/src/Resources/ProcessResource/Pages/CreateProcessPage.php) · [ListProcesses.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management-filament/src/Resources/ProcessResource/Pages/ListProcesses.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ProcessQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Queries/ProcessQuery.php) | `public function processes(int $teamId): Builder`<br>`public function runs(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AdvanceProcess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Actions/AdvanceProcess.php) | `public function execute(int $teamId, int $actorId, ProcessRun $run, array $context = []): ProcessRun` |
| [CreateProcess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Actions/CreateProcess.php) | `public function execute(int $teamId, int $ownerId, array $input): Process` |
| [PublishProcess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Actions/PublishProcess.php) | `public function execute(int $teamId, int $actorId, Process $process): Process` |
| [StartProcess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Actions/StartProcess.php) | `public function execute(int $teamId, int $actorId, Process $process, array $context = []): ProcessRun` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Process.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Models/Process.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProcessEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Models/ProcessEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProcessRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Models/ProcessRun.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
