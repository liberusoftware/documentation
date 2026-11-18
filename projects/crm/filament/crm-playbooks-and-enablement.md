# CRM: Crm Playbooks And Enablement Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-playbooks-and-enablement). Observed identity: [`liberusoftware/module-crm-playbooks-and-enablement-filament`](../../../modules/source/liberusoftware--module-crm-playbooks-and-enablement-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-playbooks-and-enablement-filament`  
**Matching domain module:** `crm-playbooks-and-enablement`  
**Application:** CRM  
**Source feature:** [Crm Playbooks And Enablement](../features/crm-playbooks-and-enablement.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-playbooks-and-enablement` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Guided scripts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Qualification cards:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Battlecards:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Onboarding content:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Required evidence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Coaching checklists:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Document/content recommendations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Usage analytics:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-playbooks-and-enablement-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `guided-scripts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `qualification-cards`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `battlecards`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `onboarding-content`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `required-evidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `coaching-checklists`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `document-content-recommendations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `usage-analytics`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-playbooks-and-enablement` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-playbooks-and-enablement-filament`](https://github.com/liberusoftware/module-crm-playbooks-and-enablement-filament) (`liberusoftware/crm-playbooks-and-enablement-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-playbooks-and-enablement.md) · [API plan](../api/crm-playbooks-and-enablement.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Guided scripts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `guided scripts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Qualification cards** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `qualification cards`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Battlecards** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `battlecards`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Onboarding content** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `onboarding content`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Required evidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `required evidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Coaching checklists** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `coaching checklists`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Document/content recommendations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `document/content recommendations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Usage analytics** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `usage analytics`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PlaybooksAndEnablementFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement-filament/src/PlaybooksAndEnablementFilamentPlugin.php) · [PlaybooksAndEnablementFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement-filament/src/PlaybooksAndEnablementFilamentServiceProvider.php) · [PlaybookResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement-filament/src/Resources/PlaybookResource.php) · [CreatePlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement-filament/src/Resources/PlaybookResource/Pages/CreatePlaybook.php) · [EditPlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement-filament/src/Resources/PlaybookResource/Pages/EditPlaybook.php) · [ListPlaybooks.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement-filament/src/Resources/PlaybookResource/Pages/ListPlaybooks.php).

| Observed core query | Public method signatures |
| --- | --- |
| [PlaybookQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Queries/PlaybookQuery.php) | `public function playbooks(int $teamId)`<br>`public function assignments(int $teamId)`<br>`public function recommendations(int $teamId)`<br>`public function usage(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AssignPlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/AssignPlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PlaybookAssignment` |
| [CompletePlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/CompletePlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $assignmentId, array $input): PlaybookAssignment` |
| [CreatePlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/CreatePlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Playbook` |
| [RecommendPlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/RecommendPlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PlaybookRecommendation` |
| [RecordPlaybookUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/RecordPlaybookUsage.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PlaybookUsage` |
| [UpdatePlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/UpdatePlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $playbookId, array $input): Playbook` |
| [PlaybookPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Services/PlaybookPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Playbook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Models/Playbook.php) | No literal fillable array detected; inspect the model and API schema. |
| [PlaybookAssignment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Models/PlaybookAssignment.php) | No literal fillable array detected; inspect the model and API schema. |
| [PlaybookRecommendation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Models/PlaybookRecommendation.php) | No literal fillable array detected; inspect the model and API schema. |
| [PlaybookUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Models/PlaybookUsage.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
