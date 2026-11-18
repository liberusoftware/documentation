# CRM: Contracts Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#contracts). Observed identity: [`liberusoftware/module-crm-contracts-filament`](../../../modules/source/liberusoftware--module-crm-contracts-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-contracts-filament`  
**Matching domain module:** `crm-contracts`  
**Application:** CRM  
**Source feature:** [Contracts](../features/contracts.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-contracts` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Parties:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Terms:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Clauses:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Obligations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Versions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Negotiation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approvals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Signatures:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Amendments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Renewals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Notices:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Repository links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Compliance dates:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-contracts-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `parties`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `terms`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `clauses`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `obligations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `versions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `negotiation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approvals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `signatures`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `amendments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `renewals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `notices`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `repository-links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `compliance-dates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-contracts` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-contracts-filament`](https://github.com/liberusoftware/module-crm-contracts-filament) (`liberusoftware/crm-contracts-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/contracts.md) · [API plan](../api/contracts.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Parties** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `parties`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Terms** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `terms`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Clauses** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `clauses`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Obligations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `obligations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Versions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `versions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Negotiation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `negotiation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approvals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approvals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Signatures** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `signatures`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Amendments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `amendments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Renewals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `renewals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Notices** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `notices`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Repository links** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `repository links`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Compliance dates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `compliance dates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ContractsFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contracts-filament/src/ContractsFilamentPlugin.php) · [ContractsFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contracts-filament/src/ContractsFilamentServiceProvider.php) · [ContractResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contracts-filament/src/Resources/ContractResource.php) · [CreateContractPage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contracts-filament/src/Resources/ContractResource/Pages/CreateContractPage.php) · [ListContracts.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contracts-filament/src/Resources/ContractResource/Pages/ListContracts.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ContractQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contracts/src/Queries/ContractQuery.php) | `public function contracts(int $teamId): Builder`<br>`public function complianceDates(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateContract.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contracts/src/Actions/CreateContract.php) | `public function execute(int $teamId, int $userId, array $input): Contract` |
| [TransitionContract.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contracts/src/Actions/TransitionContract.php) | `public function execute(int $teamId, int $userId, Contract $contract, string $type, string $status = 'completed', array $payload = []): ContractEvent` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Contract.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contracts/src/Models/Contract.php) | No literal fillable array detected; inspect the model and API schema. |
| [ContractEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contracts/src/Models/ContractEvent.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
