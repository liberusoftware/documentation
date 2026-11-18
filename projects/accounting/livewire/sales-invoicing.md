# Accounting: Sales Invoicing Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sales-invoicing). Observed identity: [`liberusoftware/module-accounting-sales-invoicing-livewire`](../../../modules/source/liberusoftware--module-accounting-sales-invoicing-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-sales-invoicing-livewire`  
**Matching domain module:** `accounting-sales-invoicing`  
**Application:** Accounting  
**Source feature:** [Sales Invoicing](../features/sales-invoicing.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Draft/approved/final invoices:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Line items:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Tax:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Discounts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Deposits:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Recurring sources:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Branding:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **PDFs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Delivery:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Immutability:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-sales-invoicing-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-sales-invoicing::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `draft-approved-final-invoices`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `line-items`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `tax`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `discounts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `deposits`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `recurring-sources`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `branding`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `pdfs`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `delivery`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `immutability`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-sales-invoicing` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/sales-invoicing.md) · [API plan](../api/sales-invoicing.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Draft/approved/final invoices** | Expose a focused Livewire 4 component and namespaced Blade default view for `draft/approved/final invoices` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Line items** | Expose a focused Livewire 4 component and namespaced Blade default view for `line items` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Tax** | Expose a focused Livewire 4 component and namespaced Blade default view for `tax` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Discounts** | Expose a focused Livewire 4 component and namespaced Blade default view for `discounts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Deposits** | Expose a focused Livewire 4 component and namespaced Blade default view for `deposits` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Recurring sources** | Expose a focused Livewire 4 component and namespaced Blade default view for `recurring sources` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Branding** | Expose a focused Livewire 4 component and namespaced Blade default view for `branding` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **PDFs** | Expose a focused Livewire 4 component and namespaced Blade default view for `pdfs` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Delivery** | Expose a focused Livewire 4 component and namespaced Blade default view for `delivery` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Immutability** | Expose a focused Livewire 4 component and namespaced Blade default view for `immutability` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Invoices.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-livewire/src/Livewire/Invoices.php) · [SalesInvoicingLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-livewire/src/SalesInvoicingLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/ApproveInvoice.php) | `public function handle(SalesInvoice $invoice): SalesInvoice` |
| [CreateInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/CreateInvoice.php) | `public function handle(array $attributes, array $lines): SalesInvoice` |
| [FinalizeInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/FinalizeInvoice.php) | `public function handle(SalesInvoice $invoice, ?string $actor = null): SalesInvoice` |
| [GenerateInvoicePdf.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/GenerateInvoicePdf.php) | `public function handle(SalesInvoice $invoice, string $format = 'pdf'): array` |
| [MarkInvoiceDelivered.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/MarkInvoiceDelivered.php) | `public function handle(SalesInvoice $invoice): SalesInvoice` |
| [RecordDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/RecordDeposit.php) | `public function handle(SalesInvoice $invoice, array $attributes): SalesInvoice` |
| [SetInvoiceBranding.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/SetInvoiceBranding.php) | `public function handle(SalesInvoice $invoice, array $branding): SalesInvoice` |
| [SetRecurringSource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/SetRecurringSource.php) | `public function handle(SalesInvoice $invoice, array $source): SalesInvoice` |
| [SalesInvoicingPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-api/src/Policies/SalesInvoicingPolicy.php) | `public function viewAny(?Authenticatable $u): bool`<br>`public function view(?Authenticatable $u, SalesInvoice $i): bool`<br>`public function create(?Authenticatable $u): bool`<br>`public function update(?Authenticatable $u, SalesInvoice $i): bool`<br>`public function delete(?Authenticatable $u, SalesInvoice $i): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SalesInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Models/SalesInvoice.php) | `invoice_number`, `party_id`, `invoice_date`, `due_on`, `status`, `subtotal`, `discount_total`, `tax_total`, `total`, `currency`, `notes`, `branding`, `recurring_source`, `delivery_status`, `delivered_at`, `metadata` |
| [SalesInvoiceDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Models/SalesInvoiceDeposit.php) | `invoice_id`, `amount`, `currency`, `reference`, `received_by` |
| [SalesInvoiceLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Models/SalesInvoiceLine.php) | `invoice_id`, `description`, `quantity`, `unit_price`, `discount_rate`, `tax_rate`, `net_amount`, `tax_amount`, `metadata` |
<!-- layer-implementation-plan:end -->
