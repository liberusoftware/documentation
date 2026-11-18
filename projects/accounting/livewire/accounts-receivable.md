# Accounting: Accounts Receivable Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounts-receivable). Observed identity: [`liberusoftware/module-accounting-accounts-receivable-livewire`](../../../modules/source/liberusoftware--module-accounting-accounts-receivable-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-accounts-receivable-livewire`  
**Matching domain module:** `accounting-accounts-receivable`  
**Application:** Accounting  
**Source feature:** [Accounts Receivable](../features/accounts-receivable.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Customer subledger:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Open items:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Statements:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Aging:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Balances:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Unapplied cash:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Disputes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Credit limits/holds:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Control-account reconciliation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-accounts-receivable-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-accounts-receivable::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `customer-subledger`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `open-items`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `statements`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `aging`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `balances`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `unapplied-cash`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `disputes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `credit-limits-holds`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `control-account-reconciliation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-accounts-receivable` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accounts-receivable.md) · [API plan](../api/accounts-receivable.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Customer subledger** | Expose a focused Livewire 4 component and namespaced Blade default view for `customer subledger` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Open items** | Expose a focused Livewire 4 component and namespaced Blade default view for `open items` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Statements** | Expose a focused Livewire 4 component and namespaced Blade default view for `statements` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Aging** | Expose a focused Livewire 4 component and namespaced Blade default view for `aging` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Balances** | Expose a focused Livewire 4 component and namespaced Blade default view for `balances` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Unapplied cash** | Expose a focused Livewire 4 component and namespaced Blade default view for `unapplied cash` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Disputes** | Expose a focused Livewire 4 component and namespaced Blade default view for `disputes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Credit limits/holds** | Expose a focused Livewire 4 component and namespaced Blade default view for `credit limits/holds` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Control-account reconciliation** | Expose a focused Livewire 4 component and namespaced Blade default view for `control-account reconciliation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Aging.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-livewire/src/Livewire/Aging.php) · [Receivables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-livewire/src/Livewire/Receivables.php) · [Statement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-livewire/src/Livewire/Statement.php) · [AccountsReceivableLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-livewire/src/AccountsReceivableLivewireServiceProvider.php).

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
