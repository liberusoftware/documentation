# CRM: Crm Quotas And Incentives Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-quotas-and-incentives). Observed identity: [`liberusoftware/module-crm-quotas-and-incentives-filament`](../../../modules/source/liberusoftware--module-crm-quotas-and-incentives-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-quotas-and-incentives-filament`  
**Matching domain module:** `crm-quotas-and-incentives`  
**Application:** CRM  
**Source feature:** [Crm Quotas And Incentives](../features/crm-quotas-and-incentives.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-quotas-and-incentives` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Quotas:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Ramps:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Crediting:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Splits:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Territories:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Attainment:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Commission plans:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Accelerators:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Adjustments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Disputes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approvals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payroll/export adapters:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-quotas-and-incentives-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `quotas`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ramps`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `crediting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `splits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `territories`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `attainment`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `commission-plans`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `accelerators`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `adjustments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `disputes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approvals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payroll-export-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-quotas-and-incentives` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-quotas-and-incentives-filament`](https://github.com/liberusoftware/module-crm-quotas-and-incentives-filament) (`liberusoftware/crm-quotas-and-incentives-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-quotas-and-incentives.md) · [API plan](../api/crm-quotas-and-incentives.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Quotas** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `quotas`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Ramps** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ramps`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Crediting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `crediting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Splits** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `splits`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Territories** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `territories`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Attainment** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `attainment`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Commission plans** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `commission plans`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Accelerators** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `accelerators`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Adjustments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `adjustments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Disputes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `disputes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approvals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approvals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Payroll/export adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payroll/export adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [QuotasAndIncentivesFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives-filament/src/QuotasAndIncentivesFilamentPlugin.php) · [QuotasAndIncentivesFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives-filament/src/QuotasAndIncentivesFilamentServiceProvider.php) · [QuotaResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives-filament/src/Resources/QuotaResource.php) · [CreateQuota.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives-filament/src/Resources/QuotaResource/Pages/CreateQuota.php) · [EditQuota.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives-filament/src/Resources/QuotaResource/Pages/EditQuota.php) · [ListQuotas.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives-filament/src/Resources/QuotaResource/Pages/ListQuotas.php).

| Observed core query | Public method signatures |
| --- | --- |
| [QuotaQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Queries/QuotaQuery.php) | `public function quotas(int $teamId)`<br>`public function plans(int $teamId)`<br>`public function credits(int $teamId)`<br>`public function disputes(int $teamId)`<br>`public function exports(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCommissionPlan.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/CreateCommissionPlan.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CommissionPlan` |
| [CreateQuota.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/CreateQuota.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Quota` |
| [CreditCommission.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/CreditCommission.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CommissionCredit` |
| [ExportCommissions.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/ExportCommissions.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CommissionExport` |
| [OpenDispute.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/OpenDispute.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CommissionDispute` |
| [ResolveDispute.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/ResolveDispute.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $disputeId, array $input): CommissionDispute` |
| [UpdateQuota.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/UpdateQuota.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $quotaId, array $input): Quota` |
| [QuotaPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Services/QuotaPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CommissionCredit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Models/CommissionCredit.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommissionDispute.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Models/CommissionDispute.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommissionExport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Models/CommissionExport.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommissionPlan.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Models/CommissionPlan.php) | No literal fillable array detected; inspect the model and API schema. |
| [Quota.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Models/Quota.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
