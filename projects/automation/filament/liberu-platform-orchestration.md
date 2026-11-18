# Automation: Liberu Platform Orchestration Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#liberu-platform-orchestration). Observed identity: [`liberusoftware/liberu-platform-orchestration-filament`](../../../modules/source/liberusoftware--liberu-platform-orchestration-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-automation-liberu-platform-orchestration-filament`  
**Matching domain module:** `liberu-platform-orchestration`  
**Application:** Automation  
**Source feature:** [Liberu Platform Orchestration](../features/liberu-platform-orchestration.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `liberu-platform-orchestration` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Composition manifest:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Capability graph:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Lifecycle coordination:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Release gates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Ownership registry:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-automation-liberu-platform-orchestration-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `composition-manifest`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `capability-graph`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `lifecycle-coordination`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `release-gates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ownership-registry`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `liberu-platform-orchestration` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-automation-laravel-filament`](https://github.com/liberusoftware/project-automation-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-liberu-platform-orchestration-7f7db377-filament`](https://github.com/liberusoftware/module-liberu-platform-orchestration-7f7db377-filament) (`liberusoftware/liberu-platform-orchestration-7f7db377-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/liberu-platform-orchestration.md) · [API plan](../api/liberu-platform-orchestration.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Composition manifest** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `composition manifest`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Capability graph** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `capability graph`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Lifecycle coordination** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lifecycle coordination`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Release gates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `release gates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Ownership registry** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ownership registry`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PlatformOrchestrationFilamentServiceProvider.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-platform-orchestration-filament/src/PlatformOrchestrationFilamentServiceProvider.php) · [PlatformWorkflowResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-platform-orchestration-filament/src/Resources/PlatformWorkflowResource.php) · [CreatePlatformWorkflow.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-platform-orchestration-filament/src/Resources/PlatformWorkflowResource/Pages/CreatePlatformWorkflow.php) · [EditPlatformWorkflow.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-platform-orchestration-filament/src/Resources/PlatformWorkflowResource/Pages/EditPlatformWorkflow.php) · [ListPlatformWorkflows.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-platform-orchestration-filament/src/Resources/PlatformWorkflowResource/Pages/ListPlatformWorkflows.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePlatformWorkflow.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-platform-orchestration/src/Actions/CreatePlatformWorkflow.php) | `public function execute(array $attributes): PlatformWorkflow` |
| [TransitionPlatformWorkflow.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-platform-orchestration/src/Actions/TransitionPlatformWorkflow.php) | `public function execute(PlatformWorkflow $record, LifecycleStatus $to): PlatformWorkflow` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PlatformWorkflow.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-platform-orchestration/src/Models/PlatformWorkflow.php) | `tenant_id`, `idempotency_key`, `name`, `status`, `metadata` |
<!-- layer-implementation-plan:end -->
