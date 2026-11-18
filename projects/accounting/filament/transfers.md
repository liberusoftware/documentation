# Accounting: Transfers Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#transfers). Observed identity: [`liberusoftware/module-accounting-transfers-filament`](../../../modules/source/liberusoftware--module-accounting-transfers-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-transfers-filament`  
**Matching domain module:** `accounting-transfers`  
**Application:** Accounting  
**Source feature:** [Transfers](../features/transfers.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-transfers` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Inter-account/entity transfers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Currency conversion:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Fees:** resource/table/form/action or page behavior for this module's authorized workflow.
- **In-transit state:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Paired posting:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-transfers-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `inter-account-entity-transfers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `currency-conversion`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `fees`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `in-transit-state`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `paired-posting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-transfers` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-transfers-filament`](https://github.com/liberusoftware/module-accounting-transfers-filament) (`liberusoftware/accounting-transfers-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/transfers.md) · [API plan](../api/transfers.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Inter-account/entity transfers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `inter-account/entity transfers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Currency conversion** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `currency conversion`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Fees** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `fees`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **In-transit state** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `in-transit state`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Paired posting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `paired posting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListTransfers.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers-filament/src/Resources/Pages/ListTransfers.php) · [TransferResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers-filament/src/Resources/TransferResource.php) · [TransfersFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers-filament/src/TransfersFilamentPlugin.php) · [TransfersFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers-filament/src/TransfersFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CompleteTransfer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers/src/Actions/CompleteTransfer.php) | `public function handle(Transfer $transfer): Transfer` |
| [CreateTransfer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers/src/Actions/CreateTransfer.php) | `public function handle(array $attributes): Transfer` |
| [ReconcileTransfer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers/src/Actions/ReconcileTransfer.php) | `public function handle(Transfer $transfer, array $attributes): TransferReconciliation` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Transfer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers/src/Models/Transfer.php) | `team_id`, `source_account_ref`, `destination_account_ref`, `source_currency`, `destination_currency`, `source_amount`, `destination_amount`, `exchange_rate`, `fee_amount`, `status`, `reference`, `metadata` |
| [TransferReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers/src/Models/TransferReconciliation.php) | `team_id`, `transfer_id`, `external_ref`, `amount`, `reconciled_on`, `status`, `metadata` |
<!-- layer-implementation-plan:end -->
