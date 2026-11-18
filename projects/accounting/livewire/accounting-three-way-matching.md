# Accounting: Accounting Three Way Matching Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-three-way-matching). Observed identity: [`liberusoftware/module-accounting-three-way-matching-livewire`](../../../modules/source/liberusoftware--module-accounting-three-way-matching-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-accounting-three-way-matching-livewire`  
**Matching domain module:** `accounting-three-way-matching`  
**Application:** Accounting  
**Source feature:** [Accounting Three Way Matching](../features/accounting-three-way-matching.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **PO/receipt/bill matching:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Quantity/price/tax tolerances:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Exceptions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Approval:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Partial matching:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Evidence:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-accounting-three-way-matching-livewire` component namespace and service provider; use explicit aliases such as `<livewire:accountingAccountingThreeWayMatching::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `po-receipt-bill-matching`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `quantity-price-tax-tolerances`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `exceptions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `approval`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `partial-matching`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `evidence`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-three-way-matching` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accounting-three-way-matching.md) · [API plan](../api/accounting-three-way-matching.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **PO/receipt/bill matching** | Expose a focused Livewire 4 component and namespaced Blade default view for `po/receipt/bill matching` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Quantity/price/tax tolerances** | Expose a focused Livewire 4 component and namespaced Blade default view for `quantity/price/tax tolerances` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Exceptions** | Expose a focused Livewire 4 component and namespaced Blade default view for `exceptions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Approval** | Expose a focused Livewire 4 component and namespaced Blade default view for `approval` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Partial matching** | Expose a focused Livewire 4 component and namespaced Blade default view for `partial matching` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Evidence** | Expose a focused Livewire 4 component and namespaced Blade default view for `evidence` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Matches.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching-livewire/src/Livewire/Matches.php) · [ThreeWayMatchingLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching-livewire/src/ThreeWayMatchingLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ExceptionQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Queries/ExceptionQuery.php) | `public function open(?int $matchId = null): Collection` |
| [MatchQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Queries/MatchQuery.php) | `public function paginate(?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveMatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Actions/ApproveMatch.php) | `public function handle(MatchRecord $match, int $actorId, ?string $overrideReason = null): MatchRecord` |
| [CaptureMatchEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Actions/CaptureMatchEvidence.php) | `public function handle(MatchRecord $match, string $sourceType, string $sourceId, array $snapshot, ?int $actorId = null): MatchEvidence` |
| [EvaluateMatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Actions/EvaluateMatch.php) | `public function handle(array $attributes): MatchRecord` |
| [RejectMatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Actions/RejectMatch.php) | `public function handle(MatchRecord $match, string $reason): MatchRecord` |
| [ResolveMatchException.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Actions/ResolveMatchException.php) | `public function handle(MatchException $exception, int $actorId, string $resolution, bool $waive = false): MatchException` |
| [ThreeWayMatchingPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching-api/src/Policies/ThreeWayMatchingPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, object $match): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, object $match): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MatchEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Models/MatchEvidence.php) | `match_id`, `source_type`, `source_id`, `snapshot_hash`, `snapshot`, `captured_by`, `metadata` |
| [MatchException.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Models/MatchException.php) | `match_id`, `kind`, `severity`, `status`, `expected_value`, `actual_value`, `tolerance`, `resolution`, `resolved_by`, `resolved_at`, `metadata` |
| [MatchRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Models/MatchRecord.php) | `purchase_order_type`, `purchase_order_id`, `receipt_type`, `receipt_id`, `bill_type`, `bill_id`, `currency`, `ordered_quantity`, `received_quantity`, `billed_quantity`, `ordered_unit_price`, `billed_unit_price`, `expected_tax`, `billed_tax`, `quantity_tolerance`, `price_tolerance`, `tax_tolerance`, `status`, `approved_by`, `approved_at`, `rejected_reason`, `metadata` |
<!-- layer-implementation-plan:end -->
