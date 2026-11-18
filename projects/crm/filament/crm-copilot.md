# CRM: CRM Copilot Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-copilot). Observed identity: [`liberusoftware/module-crm-copilot-filament`](../../../modules/source/liberusoftware--module-crm-copilot-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-copilot-filament`  
**Matching domain module:** `crm-copilot`  
**Application:** CRM  
**Source feature:** [CRM Copilot](../features/crm-copilot.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-copilot` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Permission-bounded search:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Summaries:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Preparation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Drafting:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Record updates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Task creation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Action confirmation using the Automation AI Gateway:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-copilot-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `permission-bounded-search`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `summaries`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `preparation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `drafting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `record-updates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `task-creation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `action-confirmation-using-the-automation-ai-gateway`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-copilot` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-copilot-filament`](https://github.com/liberusoftware/module-crm-copilot-filament) (`liberusoftware/crm-copilot-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-copilot.md) · [API plan](../api/crm-copilot.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Permission-bounded search** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `permission-bounded search`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Summaries** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `summaries`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Preparation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `preparation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Drafting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `drafting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Record updates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `record updates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Task creation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `task creation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Action confirmation using the Automation AI Gateway** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `action confirmation using the automation ai gateway`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CopilotFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot-filament/src/CopilotFilamentServiceProvider.php) · [CopilotRequestResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot-filament/src/Resources/CopilotRequestResource.php) · [CreateCopilotRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot-filament/src/Resources/Pages/CreateCopilotRequest.php) · [EditCopilotRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot-filament/src/Resources/Pages/EditCopilotRequest.php) · [ListCopilotRequests.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot-filament/src/Resources/Pages/ListCopilotRequests.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CopilotQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Queries/CopilotQuery.php) | `public function requests(int $teamId, int $userId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AskCopilot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Actions/AskCopilot.php) | `public function __construct(private readonly CopilotPolicy $policy, private readonly AutomationGateway $gateway)`<br>`public function execute(int $teamId, int $userId, array $input): CopilotRequest` |
| [ConfirmCopilotAction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Actions/ConfirmCopilotAction.php) | `public function __construct(private readonly CopilotPolicy $policy)`<br>`public function execute(int $teamId, int $userId, CopilotAction $action): CopilotAction` |
| [ProposeCopilotAction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Actions/ProposeCopilotAction.php) | `public function __construct(private readonly CopilotPolicy $policy)`<br>`public function execute(int $teamId, int $userId, CopilotRequest $request, array $input): CopilotAction` |
| [AutomationGateway.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Contracts/AutomationGateway.php) | `public function complete(string $instruction, array $context): array` |
| [CopilotPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Services/CopilotPolicy.php) | `public function canUse(int $teamId, int $userId): bool` |
| [NullAutomationGateway.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Services/NullAutomationGateway.php) | `public function complete(string $instruction, array $context): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CopilotAction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Models/CopilotAction.php) | No literal fillable array detected; inspect the model and API schema. |
| [CopilotRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Models/CopilotRequest.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
