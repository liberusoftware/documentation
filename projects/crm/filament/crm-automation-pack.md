# CRM: CRM Automation Pack Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-automation-pack). Observed identity: [`liberusoftware/module-crm-automation-pack-filament`](../../../modules/source/liberusoftware--module-crm-automation-pack-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-automation-pack-filament`  
**Matching domain module:** `crm-automation-pack`  
**Application:** CRM  
**Source feature:** [CRM Automation Pack](../features/crm-automation-pack.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-automation-pack` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **CRM triggers/actions/conditions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recipes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Enrollment history:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Versioning:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Simulation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approval gates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Generic Automation module adapters:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-automation-pack-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `crm-triggers-actions-conditions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recipes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `enrollment-history`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `versioning`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `simulation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approval-gates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `generic-automation-module-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-automation-pack` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-automation-pack-filament`](https://github.com/liberusoftware/module-crm-automation-pack-filament) (`liberusoftware/crm-automation-pack-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-automation-pack.md) · [API plan](../api/crm-automation-pack.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **CRM triggers/actions/conditions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `crm triggers/actions/conditions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recipes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recipes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Enrollment history** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `enrollment history`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Versioning** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `versioning`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Simulation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `simulation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approval gates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approval gates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Generic Automation module adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `generic automation module adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AutomationPackFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack-filament/src/AutomationPackFilamentServiceProvider.php) · [AutomationRecipeResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack-filament/src/Resources/AutomationRecipeResource.php) · [CreateAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack-filament/src/Resources/Pages/CreateAutomationRecipe.php) · [EditAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack-filament/src/Resources/Pages/EditAutomationRecipe.php) · [ListAutomationRecipes.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack-filament/src/Resources/Pages/ListAutomationRecipes.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AutomationPackQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Queries/AutomationPackQuery.php) | `public function recipes(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/ApproveAutomationRecipe.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AutomationRecipe $recipe, string $decision, ?string $reason = null): AutomationApproval` |
| [CreateAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/CreateAutomationRecipe.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): AutomationRecipe` |
| [EnrollSubject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/EnrollSubject.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AutomationRecipe $recipe, array $input): AutomationEnrollment` |
| [PublishAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/PublishAutomationRecipe.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AutomationRecipe $recipe): AutomationRecipe` |
| [SimulateAutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Actions/SimulateAutomationRecipe.php) | `public function __construct(private readonly AutomationPackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, AutomationRecipe $recipe, array $input): AutomationRun` |
| [AutomationPackPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Services/AutomationPackPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AutomationApproval.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Models/AutomationApproval.php) | No literal fillable array detected; inspect the model and API schema. |
| [AutomationEnrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Models/AutomationEnrollment.php) | No literal fillable array detected; inspect the model and API schema. |
| [AutomationRecipe.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Models/AutomationRecipe.php) | No literal fillable array detected; inspect the model and API schema. |
| [AutomationRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-automation-pack/src/Models/AutomationRun.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
