# Accounting: Accounting Deposits And Clearing Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-deposits-and-clearing). Observed identity: [`liberusoftware/module-accounting-deposits-and-clearing-filament`](../../../modules/source/liberusoftware--module-accounting-deposits-and-clearing-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-deposits-and-clearing-filament`  
**Matching domain module:** `accounting-deposits-and-clearing`  
**Application:** Accounting  
**Source feature:** [Accounting Deposits And Clearing](../features/accounting-deposits-and-clearing.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-deposits-and-clearing` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Undeposited funds:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Grouped deposits:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payment-provider clearing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Fees:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payouts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Timing differences:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-deposits-and-clearing-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `undeposited-funds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `grouped-deposits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payment-provider-clearing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `fees`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payouts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `timing-differences`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-deposits-and-clearing` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-deposits-and-clearing-filament`](https://github.com/liberusoftware/module-accounting-deposits-and-clearing-filament) (`liberusoftware/accounting-deposits-and-clearing-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-deposits-and-clearing.md) · [API plan](../api/accounting-deposits-and-clearing.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Undeposited funds** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `undeposited funds`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Grouped deposits** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `grouped deposits`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Payment-provider clearing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payment-provider clearing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Fees** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `fees`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Payouts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payouts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Timing differences** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `timing differences`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [DepositsAndClearingFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing-filament/src/DepositsAndClearingFilamentPlugin.php) · [DepositsAndClearingFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing-filament/src/DepositsAndClearingFilamentServiceProvider.php) · [ClearingDepositResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing-filament/src/Resources/ClearingDepositResource.php) · [ListClearingDeposits.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing-filament/src/Resources/ClearingDepositResource/Pages/ListClearingDeposits.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ClearingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Queries/ClearingQuery.php) | `public function undeposited(int $teamId): Collection`<br>`public function deposits(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateGroupedDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Actions/CreateGroupedDeposit.php) | `public function handle(array $attributes, array $fundIds): ClearingDeposit` |
| [ReconcileDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Actions/ReconcileDeposit.php) | `public function handle(ClearingDeposit $deposit, float $payoutAmount, float $feeAmount = 0): ClearingDeposit` |
| [RecordUndepositedFund.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Actions/RecordUndepositedFund.php) | `public function handle(array $attributes): ClearingFund` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ClearingDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Models/ClearingDeposit.php) | `team_id`, `deposit_ref`, `provider`, `account_ref`, `currency`, `gross_amount`, `fee_amount`, `payout_amount`, `deposit_date`, `status`, `metadata` |
| [ClearingFund.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Models/ClearingFund.php) | `team_id`, `deposit_id`, `source_type`, `source_id`, `amount`, `currency`, `received_on`, `status`, `metadata` |
<!-- layer-implementation-plan:end -->
