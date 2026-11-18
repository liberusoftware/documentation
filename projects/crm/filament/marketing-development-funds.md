# CRM: Marketing Development Funds Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#marketing-development-funds). Observed identity: [`liberusoftware/module-crm-marketing-development-funds-filament`](../../../modules/source/liberusoftware--module-crm-marketing-development-funds-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-marketing-development-funds-filament`  
**Matching domain module:** `crm-marketing-development-funds`  
**Application:** CRM  
**Source feature:** [Marketing Development Funds](../features/marketing-development-funds.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-marketing-development-funds` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Requests:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Budgets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Plans:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approvals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Evidence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Claims:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reimbursements:** resource/table/form/action or page behavior for this module's authorized workflow.
- **ROI:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-marketing-development-funds-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `requests`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `budgets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `plans`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approvals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `evidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `claims`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reimbursements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `roi`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-marketing-development-funds` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-marketing-development-funds-filament`](https://github.com/liberusoftware/module-crm-marketing-development-funds-filament) (`liberusoftware/crm-marketing-development-funds-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/marketing-development-funds.md) · [API plan](../api/marketing-development-funds.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Requests** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `requests`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Budgets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `budgets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Plans** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `plans`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approvals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approvals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Evidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `evidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Claims** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `claims`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reimbursements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reimbursements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **ROI** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `roi`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [MarketingDevelopmentFundsFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds-filament/src/MarketingDevelopmentFundsFilamentServiceProvider.php) · [MdfFundResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds-filament/src/Resources/MdfFundResource.php) · [CreateMdfFund.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds-filament/src/Resources/Pages/CreateMdfFund.php) · [EditMdfFund.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds-filament/src/Resources/Pages/EditMdfFund.php) · [ListMdfFunds.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds-filament/src/Resources/Pages/ListMdfFunds.php).

| Observed core query | Public method signatures |
| --- | --- |
| [MdfQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Queries/MdfQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateFund.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Actions/CreateFund.php) | `public function __construct(private readonly MdfPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): MdfFund` |
| [CreateMdfRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Actions/CreateMdfRequest.php) | `public function __construct(private readonly MdfPolicy $policy)`<br>`public function execute(int $teamId, int $userId, MdfFund $fund, array $input): MdfRequest` |
| [RecordMdfEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Actions/RecordMdfEvent.php) | `public function __construct(private readonly MdfPolicy $policy)`<br>`public function execute(int $teamId, int $userId, MdfRequest $request, array $input): MdfRequestEvent` |
| [MdfPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Services/MdfPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MdfFund.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Models/MdfFund.php) | No literal fillable array detected; inspect the model and API schema. |
| [MdfRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Models/MdfRequest.php) | No literal fillable array detected; inspect the model and API schema. |
| [MdfRequestEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Models/MdfRequestEvent.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
