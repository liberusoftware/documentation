# Accounting: Accounting Accounts Receivable Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-accounts-receivable). Observed identity: [`liberusoftware/module-accounting-accounts-receivable-filament`](../../../modules/source/liberusoftware--module-accounting-accounts-receivable-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-accounts-receivable-filament`  
**Matching domain module:** `accounting-accounts-receivable`  
**Application:** Accounting  
**Source feature:** [Accounting Accounts Receivable](../features/accounting-accounts-receivable.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-accounts-receivable` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Customer subledger:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Open items:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Statements:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Aging:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Balances:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Unapplied cash:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Disputes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Credit limits/holds:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Control-account reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-accounts-receivable-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `customer-subledger`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `open-items`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `statements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `aging`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `balances`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `unapplied-cash`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `disputes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `credit-limits-holds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `control-account-reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-accounts-receivable` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-accounts-receivable-filament`](https://github.com/liberusoftware/module-accounting-accounts-receivable-filament) (`liberusoftware/accounting-accounts-receivable-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-accounts-receivable.md) · [API plan](../api/accounting-accounts-receivable.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Customer subledger** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `customer subledger`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Open items** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `open items`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Statements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `statements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Aging** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `aging`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Balances** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `balances`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Unapplied cash** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `unapplied cash`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Disputes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `disputes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Credit limits/holds** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `credit limits/holds`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Control-account reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `control-account reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AccountsReceivableFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-filament/src/AccountsReceivableFilamentPlugin.php) · [AccountsReceivableFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-filament/src/AccountsReceivableFilamentServiceProvider.php) · [ListReceivables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-filament/src/Resources/Pages/ListReceivables.php) · [ReceivableOpenItemResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-filament/src/Resources/ReceivableOpenItemResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AgingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Queries/AgingQuery.php) | `public function handle(?int $partyId = null, ?\DateTimeInterface $asOf = null): array` |
| [ControlAccountReconciliationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Queries/ControlAccountReconciliationQuery.php) | `public function handle(?float $controlBalance = null): array` |
| [CustomerSubledgerQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Queries/CustomerSubledgerQuery.php) | `public function handle(int $partyId): array` |
| [StatementQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Queries/StatementQuery.php) | `public function handle(int $partyId, ?\DateTimeInterface $from = null, ?\DateTimeInterface $to = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApplyReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/ApplyReceipt.php) | `public function handle(ReceivableReceipt $receipt, ReceivableOpenItem $item, float $amount): ReceivableReceipt` |
| [CreateOpenItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/CreateOpenItem.php) | `public function handle(array $attributes): ReceivableOpenItem` |
| [EnsureAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/EnsureAccount.php) | `public function handle(int $partyId): ReceivableAccount` |
| [OpenDispute.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/OpenDispute.php) | `public function handle(ReceivableOpenItem $item, string $reason, ?float $amount = null): ReceivableDispute` |
| [RecalculateAccountBalance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/RecalculateAccountBalance.php) | `public function handle(int $partyId): ReceivableAccount` |
| [RecordReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/RecordReceipt.php) | `public function handle(array $attributes): ReceivableReceipt` |
| [ResolveDispute.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/ResolveDispute.php) | `public function handle(ReceivableDispute $dispute, string $resolution, bool $accepted = false): ReceivableDispute` |
| [SetCreditControl.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/SetCreditControl.php) | `public function handle(int $partyId, ?float $creditLimit = null, ?bool $hold = null, ?string $reason = null): ReceivableAccount` |
| [SyncFinalizedInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/SyncFinalizedInvoice.php) | `public function handle(SalesInvoice $invoice): ReceivableOpenItem` |
| [AccountsReceivablePolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-api/src/Policies/AccountsReceivablePolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, object $model): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, object $model): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReceiptApplication.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Models/ReceiptApplication.php) | `receipt_id`, `open_item_id`, `amount` |
| [ReceivableAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Models/ReceivableAccount.php) | `party_id`, `credit_limit`, `current_balance`, `credit_hold`, `hold_reason`, `control_account_code`, `status`, `metadata` |
| [ReceivableDispute.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Models/ReceivableDispute.php) | `open_item_id`, `amount`, `reason`, `status`, `opened_at`, `resolved_at`, `resolution`, `metadata` |
| [ReceivableOpenItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Models/ReceivableOpenItem.php) | `party_id`, `source_type`, `source_id`, `reference`, `issued_on`, `due_on`, `original_amount`, `applied_amount`, `currency`, `status`, `metadata` |
| [ReceivableReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Models/ReceivableReceipt.php) | `party_id`, `received_on`, `amount`, `applied_amount`, `currency`, `reference`, `status`, `metadata` |
<!-- layer-implementation-plan:end -->
