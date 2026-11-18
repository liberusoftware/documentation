# Accounting: Accounting Intercompany Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-intercompany). Observed identity: [`liberusoftware/module-accounting-intercompany-filament`](../../../modules/source/liberusoftware--module-accounting-intercompany-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-intercompany-filament`  
**Matching domain module:** `accounting-intercompany`  
**Application:** Accounting  
**Source feature:** [Accounting Intercompany](../features/accounting-intercompany.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-intercompany` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Counterparties:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Trading rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Paired transactions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Confirmations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Settlement:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Differences:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Transfer-pricing evidence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-intercompany-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `counterparties`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `trading-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `paired-transactions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `confirmations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `settlement`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `differences`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `transfer-pricing-evidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-intercompany` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-intercompany-filament`](https://github.com/liberusoftware/module-accounting-intercompany-filament) (`liberusoftware/accounting-intercompany-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-intercompany.md) · [API plan](../api/accounting-intercompany.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Counterparties** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `counterparties`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Trading rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `trading rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Paired transactions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `paired transactions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Confirmations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `confirmations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Settlement** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `settlement`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Differences** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `differences`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Transfer-pricing evidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `transfer-pricing evidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [IntercompanyFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany-filament/src/IntercompanyFilamentPlugin.php) · [IntercompanyFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany-filament/src/IntercompanyFilamentServiceProvider.php) · [IntercompanyTransactionResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany-filament/src/Resources/IntercompanyTransactionResource.php) · [ListIntercompanyTransactions.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany-filament/src/Resources/Pages/ListIntercompanyTransactions.php).

| Observed core query | Public method signatures |
| --- | --- |
| [IntercompanyQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Queries/IntercompanyQuery.php) | `public function paginate(?int $teamId = null, ?TransactionStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function reconciliationSummary(IntercompanyTransaction $transaction): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddTransferPricingEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/AddTransferPricingEvidence.php) | `public function handle(IntercompanyTransaction $transaction, array $a): TransferPricingEvidence` |
| [ConfigureTradingRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/ConfigureTradingRule.php) | `public function handle(IntercompanyCounterparty $counterparty, array $a): TradingRule` |
| [ConfirmTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/ConfirmTransaction.php) | `public function handle(IntercompanyTransaction $transaction, string $entity, bool $confirmed, ?string $comment = null): IntercompanyTransaction` |
| [CreateCounterparty.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/CreateCounterparty.php) | `public function handle(array $a): IntercompanyCounterparty` |
| [CreateTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/CreateTransaction.php) | `public function handle(IntercompanyCounterparty $counterparty, array $a): IntercompanyTransaction` |
| [ReconcileIntercompany.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/ReconcileIntercompany.php) | `public function handle(array $a): IntercompanyReconciliation` |
| [RecordDifference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/RecordDifference.php) | `public function handle(IntercompanyTransaction $transaction, array $a): IntercompanyDifference` |
| [SettleTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/SettleTransaction.php) | `public function handle(IntercompanyTransaction $transaction, array $a): IntercompanyTransaction` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [IntercompanyConfirmation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanyConfirmation.php) | `transaction_id`, `entity_ref`, `status`, `confirmed_amount`, `comment`, `actor_ref`, `confirmed_at`, `metadata` |
| [IntercompanyCounterparty.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanyCounterparty.php) | `team_id`, `entity_ref`, `counterparty_ref`, `name`, `default_currency`, `active`, `metadata` |
| [IntercompanyDifference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanyDifference.php) | `transaction_id`, `difference_ref`, `amount`, `reason`, `status`, `actor_ref`, `resolved_at`, `metadata` |
| [IntercompanyReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanyReconciliation.php) | `team_id`, `reconciliation_ref`, `period_ref`, `entity_ref`, `counterparty_ref`, `transaction_count`, `source_total`, `counterparty_total`, `difference_total`, `status`, `actor_ref`, `reconciled_at`, `metadata` |
| [IntercompanySettlement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanySettlement.php) | `transaction_id`, `settlement_ref`, `amount`, `currency`, `settled_at`, `source_ref`, `metadata` |
| [IntercompanyTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanyTransaction.php) | `team_id`, `transaction_ref`, `counterparty_id`, `source_entity_ref`, `target_entity_ref`, `transaction_type`, `description`, `amount`, `currency`, `status`, `transaction_date`, `metadata` |
| [TradingRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/TradingRule.php) | `counterparty_id`, `rule_ref`, `description`, `pricing_method`, `markup_percent`, `currency`, `active`, `metadata` |
| [TransferPricingEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/TransferPricingEvidence.php) | `transaction_id`, `evidence_ref`, `kind`, `file_ref`, `description`, `arm_length_value`, `currency`, `captured_at`, `metadata` |
<!-- layer-implementation-plan:end -->
