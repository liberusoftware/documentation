# CRM: Crm Collaboration Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-collaboration). Observed identity: [`liberusoftware/module-crm-collaboration-filament`](../../../modules/source/liberusoftware--module-crm-collaboration-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-collaboration-filament`  
**Matching domain module:** `crm-collaboration`  
**Application:** CRM  
**Source feature:** [Crm Collaboration](../features/crm-collaboration.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-collaboration` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Record comments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Mentions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Followers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Shared work queues:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approvals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Handoffs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Internal channels:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Collaboration-provider adapters:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-collaboration-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `record-comments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `mentions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `followers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `shared-work-queues`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approvals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `handoffs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `internal-channels`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `collaboration-provider-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-collaboration` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-collaboration-filament`](https://github.com/liberusoftware/module-crm-collaboration-filament) (`liberusoftware/crm-collaboration-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-collaboration.md) · [API plan](../api/crm-collaboration.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Record comments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `record comments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Mentions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `mentions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Followers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `followers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Shared work queues** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `shared work queues`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approvals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approvals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Handoffs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `handoffs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Internal channels** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `internal channels`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Collaboration-provider adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `collaboration-provider adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CollaborationFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-collaboration-filament/src/CollaborationFilamentPlugin.php) · [CollaborationFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-collaboration-filament/src/CollaborationFilamentServiceProvider.php) · [CollaborationWorkResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-collaboration-filament/src/Resources/CollaborationWorkResource.php) · [CreateCollaborationWork.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-collaboration-filament/src/Resources/CollaborationWorkResource/Pages/CreateCollaborationWork.php) · [ListCollaborationWork.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-collaboration-filament/src/Resources/CollaborationWorkResource/Pages/ListCollaborationWork.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CollaborationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-collaboration/src/Queries/CollaborationQuery.php) | `public function records(int $teamId, string $recordKey): Builder`<br>`public function queue(int $teamId, string $queueKey): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddCollaborationRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-collaboration/src/Actions/AddCollaborationRecord.php) | `public function execute(int $teamId, string $recordKey, string $authorKey, string $body, string $kind = 'comment', array $mentions = []): CollaborationRecord` |
| [AssignCollaborationWork.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-collaboration/src/Actions/AssignCollaborationWork.php) | `public function execute(int $teamId, string $queueKey, string $subjectKey, ?string $assigneeKey = null, array $metadata = []): CollaborationWork` |
| [HandoffCollaborationWork.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-collaboration/src/Actions/HandoffCollaborationWork.php) | `public function execute(int $teamId, CollaborationWork $work, string $assigneeKey, string $reason): CollaborationWork` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CollaborationRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-collaboration/src/Models/CollaborationRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [CollaborationWork.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-collaboration/src/Models/CollaborationWork.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
