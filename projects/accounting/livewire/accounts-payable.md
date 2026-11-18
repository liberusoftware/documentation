# Accounting: Accounts Payable Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounts-payable). Observed identity: [`liberusoftware/module-accounting-accounts-payable-livewire`](../../../modules/source/liberusoftware--module-accounting-accounts-payable-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-accounts-payable-livewire`  
**Matching domain module:** `accounting-accounts-payable`  
**Application:** Accounting  
**Source feature:** [Accounts Payable](../features/accounts-payable.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Supplier subledger:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Open items:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Aging:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Balances:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Credits:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Disputes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Holds:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Payment terms:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Control-account reconciliation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-accounts-payable-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-accounts-payable::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `supplier-subledger`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `open-items`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `aging`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `balances`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `credits`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `disputes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `holds`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `payment-terms`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `control-account-reconciliation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-accounts-payable` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accounts-payable.md) · [API plan](../api/accounts-payable.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Supplier subledger** | Expose a focused Livewire 4 component and namespaced Blade default view for `supplier subledger` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Open items** | Expose a focused Livewire 4 component and namespaced Blade default view for `open items` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Aging** | Expose a focused Livewire 4 component and namespaced Blade default view for `aging` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Balances** | Expose a focused Livewire 4 component and namespaced Blade default view for `balances` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Credits** | Expose a focused Livewire 4 component and namespaced Blade default view for `credits` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Disputes** | Expose a focused Livewire 4 component and namespaced Blade default view for `disputes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Holds** | Expose a focused Livewire 4 component and namespaced Blade default view for `holds` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Payment terms** | Expose a focused Livewire 4 component and namespaced Blade default view for `payment terms` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Control-account reconciliation** | Expose a focused Livewire 4 component and namespaced Blade default view for `control-account reconciliation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Aging.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-livewire/src/Livewire/Aging.php) · [Payables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-livewire/src/Livewire/Payables.php) · [Reconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-livewire/src/Livewire/Reconciliation.php) · [AccountsPayableLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-livewire/src/AccountsPayableLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AgingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Queries/AgingQuery.php) | `public function handle(?int $partyId = null, ?\DateTimeInterface $asOf = null): array` |
| [ControlAccountReconciliationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Queries/ControlAccountReconciliationQuery.php) | `public function handle(): array` |
| [SupplierSubledgerQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Queries/SupplierSubledgerQuery.php) | `public function handle(int $partyId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApplyPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/ApplyPayment.php) | `public function handle(PayablePayment $payment, PayableOpenItem $item, float $amount): PayablePayment` |
| [CreateOpenItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/CreateOpenItem.php) | `public function handle(array $attributes): PayableOpenItem` |
| [EnsureAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/EnsureAccount.php) | `public function handle(int $partyId): PayableAccount` |
| [OpenDispute.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/OpenDispute.php) | `public function handle(PayableOpenItem $item, string $reason, ?float $amount = null): PayableDispute` |
| [RecalculateAccountBalance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/RecalculateAccountBalance.php) | `public function handle(int $partyId): PayableAccount` |
| [RecordPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/RecordPayment.php) | `public function handle(array $attributes): PayablePayment` |
| [ResolveDispute.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/ResolveDispute.php) | `public function handle(PayableDispute $dispute, string $resolution, bool $accepted = false): PayableDispute` |
| [SetPaymentControl.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/SetPaymentControl.php) | `public function handle(int $partyId, ?bool $paymentHold = null, ?string $holdReason = null): PayableAccount` |
| [AccountingAccountsPayablePolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-api/src/Policies/AccountingAccountsPayablePolicy.php) | `public function viewAny(?object $user = null): bool`<br>`public function view(?object $user, object $item): bool`<br>`public function create(?object $user = null): bool`<br>`public function update(?object $user, object $item): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PayableAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Models/PayableAccount.php) | `party_id`, `current_balance`, `payment_hold`, `hold_reason`, `control_account_code`, `status`, `metadata` |
| [PayableDispute.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Models/PayableDispute.php) | `open_item_id`, `amount`, `reason`, `status`, `opened_at`, `resolved_at`, `resolution`, `metadata` |
| [PayableOpenItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Models/PayableOpenItem.php) | `party_id`, `source_type`, `source_id`, `reference`, `issued_on`, `due_on`, `original_amount`, `paid_amount`, `currency`, `payment_terms`, `status`, `metadata` |
| [PayablePayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Models/PayablePayment.php) | `party_id`, `paid_on`, `amount`, `applied_amount`, `currency`, `reference`, `status`, `metadata` |
| [PaymentApplication.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Models/PaymentApplication.php) | `payment_id`, `open_item_id`, `amount` |
<!-- layer-implementation-plan:end -->
