# CRM: Crm Customer Success Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-customer-success). Observed identity: [`liberusoftware/module-crm-customer-success-filament`](../../../modules/source/liberusoftware--module-crm-customer-success-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-customer-success-filament`  
**Matching domain module:** `crm-customer-success`  
**Application:** CRM  
**Source feature:** [Crm Customer Success](../features/crm-customer-success.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-customer-success` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Customer segments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Lifecycle:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Onboarding plans:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Success plans:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Objectives:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Health scores:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Product/usage signals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Risks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Playbooks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Touchpoints:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Renewals:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-customer-success-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `customer-segments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `lifecycle`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `onboarding-plans`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `success-plans`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `objectives`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `health-scores`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `product-usage-signals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `risks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `playbooks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `touchpoints`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `renewals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-customer-success` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-customer-success-filament`](https://github.com/liberusoftware/module-crm-customer-success-filament) (`liberusoftware/crm-customer-success-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-customer-success.md) · [API plan](../api/crm-customer-success.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Customer segments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `customer segments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Lifecycle** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lifecycle`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Onboarding plans** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `onboarding plans`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Success plans** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `success plans`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Objectives** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `objectives`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Health scores** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `health scores`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Product/usage signals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `product/usage signals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Risks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `risks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Playbooks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `playbooks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Touchpoints** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `touchpoints`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Renewals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `renewals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CustomerSuccessFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success-filament/src/CustomerSuccessFilamentServiceProvider.php) · [CreateSuccessCustomer.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success-filament/src/Resources/Pages/CreateSuccessCustomer.php) · [EditSuccessCustomer.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success-filament/src/Resources/Pages/EditSuccessCustomer.php) · [ListSuccessCustomers.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success-filament/src/Resources/Pages/ListSuccessCustomers.php) · [SuccessCustomerResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success-filament/src/Resources/SuccessCustomerResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CustomerSuccessQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Queries/CustomerSuccessQuery.php) | `public function customers(int $teamId)`<br>`public function risks(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [OpenSuccessRisk.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Actions/OpenSuccessRisk.php) | `public function __construct(private readonly CustomerSuccessPolicy $policy)`<br>`public function execute(int $teamId, int $userId, SuccessCustomer $customer, array $input): SuccessRisk` |
| [PlanRenewal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Actions/PlanRenewal.php) | `public function __construct(private readonly CustomerSuccessPolicy $policy)`<br>`public function execute(int $teamId, int $userId, SuccessCustomer $customer, array $input): SuccessRenewal` |
| [RecordHealthSignal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Actions/RecordHealthSignal.php) | `public function __construct(private readonly CustomerSuccessPolicy $policy)`<br>`public function execute(int $teamId, int $userId, SuccessCustomer $customer, array $input): SuccessSignal` |
| [UpsertSuccessCustomer.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Actions/UpsertSuccessCustomer.php) | `public function __construct(private readonly CustomerSuccessPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): SuccessCustomer` |
| [CustomerSuccessPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Services/CustomerSuccessPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SuccessCustomer.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Models/SuccessCustomer.php) | No literal fillable array detected; inspect the model and API schema. |
| [SuccessRenewal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Models/SuccessRenewal.php) | No literal fillable array detected; inspect the model and API schema. |
| [SuccessRisk.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Models/SuccessRisk.php) | No literal fillable array detected; inspect the model and API schema. |
| [SuccessSignal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Models/SuccessSignal.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
