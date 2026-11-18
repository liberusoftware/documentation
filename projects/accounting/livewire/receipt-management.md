# Accounting: Receipt Management Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#receipt-management). Observed identity: [`liberusoftware/module-accounting-receipt-management-livewire`](../../../modules/source/liberusoftware--module-accounting-receipt-management-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-receipt-management-livewire`  
**Matching domain module:** `accounting-receipt-management`  
**Application:** Accounting  
**Source feature:** [Receipt Management](../features/receipt-management.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Receipt inbox:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Matching to bank/card/expense/bill:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Missing-receipt requests:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Annotations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Retention:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Audit:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-receipt-management-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-receipt-management::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `receipt-inbox`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `matching-to-bank-card-expense-bill`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `missing-receipt-requests`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `annotations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `retention`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `audit`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-receipt-management` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/receipt-management.md) · [API plan](../api/receipt-management.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Receipt inbox** | Expose a focused Livewire 4 component and namespaced Blade default view for `receipt inbox` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Matching to bank/card/expense/bill** | Expose a focused Livewire 4 component and namespaced Blade default view for `matching to bank/card/expense/bill` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Missing-receipt requests** | Expose a focused Livewire 4 component and namespaced Blade default view for `missing-receipt requests` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Annotations** | Expose a focused Livewire 4 component and namespaced Blade default view for `annotations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Retention** | Expose a focused Livewire 4 component and namespaced Blade default view for `retention` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Audit** | Expose a focused Livewire 4 component and namespaced Blade default view for `audit` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Receipts.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-receipt-management-livewire/src/Livewire/Receipts.php) · [ReceiptManagementLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-receipt-management-livewire/src/ReceiptManagementLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [IngestReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-receipt-management/src/Actions/IngestReceipt.php) | `public function handle(array $attributes): Receipt` |
| [MatchReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-receipt-management/src/Actions/MatchReceipt.php) | `public function handle(Receipt $receipt, array $attributes): ReceiptMatch` |
| [RequestMissingReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-receipt-management/src/Actions/RequestMissingReceipt.php) | `public function handle(array $attributes): MissingReceiptRequest` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MissingReceiptRequest.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-receipt-management/src/Models/MissingReceiptRequest.php) | `team_id`, `receipt_id`, `requestee_ref`, `target_type`, `target_id`, `reason`, `status`, `due_on`, `fulfilled_at`, `metadata` |
| [Receipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-receipt-management/src/Models/Receipt.php) | `team_id`, `file_ref`, `source_type`, `source_id`, `merchant`, `amount`, `currency`, `receipt_date`, `status`, `retention_until`, `metadata` |
| [ReceiptAnnotation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-receipt-management/src/Models/ReceiptAnnotation.php) | `receipt_id`, `author_ref`, `body`, `visibility`, `metadata` |
| [ReceiptAudit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-receipt-management/src/Models/ReceiptAudit.php) | `receipt_id`, `action`, `actor_ref`, `evidence`, `created_at` |
| [ReceiptMatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-receipt-management/src/Models/ReceiptMatch.php) | `receipt_id`, `target_type`, `target_id`, `matched_amount`, `status`, `confidence`, `metadata` |
<!-- layer-implementation-plan:end -->
