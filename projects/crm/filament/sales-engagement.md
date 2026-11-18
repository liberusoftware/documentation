# CRM: Sales Engagement Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sales-engagement). Observed identity: [`liberusoftware/module-crm-sales-engagement-filament`](../../../modules/source/liberusoftware--module-crm-sales-engagement-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-sales-engagement-filament`  
**Matching domain module:** `crm-sales-engagement`  
**Application:** CRM  
**Source feature:** [Sales Engagement](../features/sales-engagement.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-sales-engagement` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Sequences/cadences:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Multi-channel steps:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Templates/snippets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Task queues:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Enrollment/re-entry:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Throttles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Timezone windows:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reply/meeting stop rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Experiments:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-sales-engagement-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `sequences-cadences`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `multi-channel-steps`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `templates-snippets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `task-queues`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `enrollment-re-entry`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `throttles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `timezone-windows`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reply-meeting-stop-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `experiments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-sales-engagement` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-sales-engagement-filament`](https://github.com/liberusoftware/module-crm-sales-engagement-filament) (`liberusoftware/crm-sales-engagement-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/sales-engagement.md) · [API plan](../api/sales-engagement.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Sequences/cadences** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sequences/cadences`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Multi-channel steps** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `multi-channel steps`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Templates/snippets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `templates/snippets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Task queues** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `task queues`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Enrollment/re-entry** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `enrollment/re-entry`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Throttles** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `throttles`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Timezone windows** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `timezone windows`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reply/meeting stop rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reply/meeting stop rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Experiments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `experiments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [SequenceResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement-filament/src/Resources/SequenceResource.php) · [CreateSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement-filament/src/Resources/SequenceResource/Pages/CreateSequence.php) · [EditSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement-filament/src/Resources/SequenceResource/Pages/EditSequence.php) · [ListSequences.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement-filament/src/Resources/SequenceResource/Pages/ListSequences.php) · [SalesEngagementFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement-filament/src/SalesEngagementFilamentPlugin.php) · [SalesEngagementFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement-filament/src/SalesEngagementFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [EngagementQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Queries/EngagementQuery.php) | `public function sequences(int $teamId)`<br>`public function enrollments(int $teamId)`<br>`public function tasks(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddStep.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/AddStep.php) | `public function execute(int $teamId, int $actorId, array $data): EngagementStep` |
| [CreateSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/CreateSequence.php) | `public function execute(int $teamId, int $actorId, array $data): EngagementSequence` |
| [EnrollContact.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/EnrollContact.php) | `public function execute(int $teamId, int $actorId, array $data): Enrollment` |
| [RecordEngagementEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/RecordEngagementEvent.php) | `public function execute(int $teamId, int $actorId, array $data): EngagementEvent` |
| [StopEnrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/StopEnrollment.php) | `public function execute(int $teamId, int $actorId, int $id, string $reason): Enrollment` |
| [UpdateSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/UpdateSequence.php) | `public function execute(int $teamId, int $actorId, int $sequenceId, array $data): EngagementSequence` |
| [EngagementPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Services/EngagementPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EngagementEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/EngagementEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [EngagementSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/EngagementSequence.php) | No literal fillable array detected; inspect the model and API schema. |
| [EngagementStep.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/EngagementStep.php) | No literal fillable array detected; inspect the model and API schema. |
| [EngagementTask.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/EngagementTask.php) | No literal fillable array detected; inspect the model and API schema. |
| [Enrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/Enrollment.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
