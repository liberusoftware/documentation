# Accounting: Leases Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#leases). Observed identity: [`liberusoftware/module-accounting-leases-livewire`](../../../modules/source/liberusoftware--module-accounting-leases-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-leases-livewire`  
**Matching domain module:** `accounting-leases`  
**Application:** Accounting  
**Source feature:** [Leases](../features/leases.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Lease records:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Payment schedules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Right-of-use assets:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Liabilities:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Interest/depreciation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Modifications:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Disclosures (optional):** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-leases-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-leases::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `lease-records`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `payment-schedules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `right-of-use-assets`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `liabilities`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `interest-depreciation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `modifications`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `disclosures-optional`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-leases` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/leases.md) · [API plan](../api/leases.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Lease records** | Expose a focused Livewire 4 component and namespaced Blade default view for `lease records` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Payment schedules** | Expose a focused Livewire 4 component and namespaced Blade default view for `payment schedules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Right-of-use assets** | Expose a focused Livewire 4 component and namespaced Blade default view for `right-of-use assets` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Liabilities** | Expose a focused Livewire 4 component and namespaced Blade default view for `liabilities` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Interest/depreciation** | Expose a focused Livewire 4 component and namespaced Blade default view for `interest/depreciation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Modifications** | Expose a focused Livewire 4 component and namespaced Blade default view for `modifications` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Disclosures (optional)** | Expose a focused Livewire 4 component and namespaced Blade default view for `disclosures (optional)` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Leases.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases-livewire/src/Livewire/Leases.php) · [LeasesLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases-livewire/src/LeasesLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [LeaseQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Queries/LeaseQuery.php) | `public function leases(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function disclosure(Lease $lease): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDisclosure.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/CreateDisclosure.php) | `public function handle(Lease $lease, string $asOfDate): LeaseDisclosure` |
| [CreateLease.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/CreateLease.php) | `public function handle(array $attributes): Lease` |
| [GenerateSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/GenerateSchedule.php) | `public function handle(Lease $lease): Lease` |
| [ModifyLease.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/ModifyLease.php) | `public function handle(Lease $lease, array $attributes): Lease` |
| [PostPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/PostPayment.php) | `public function handle(LeasePayment $payment): LeasePayment` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Lease.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Models/Lease.php) | `team_id`, `lease_ref`, `name`, `lessor_ref`, `asset_ref`, `commencement_date`, `end_date`, `currency`, `payment_amount`, `payment_frequency`, `interest_rate`, `discount_rate`, `useful_life_months`, `status`, `right_of_use_asset`, `lease_liability`, `accumulated_depreciation`, `metadata` |
| [LeaseDisclosure.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Models/LeaseDisclosure.php) | `lease_id`, `as_of_date`, `remaining_liability`, `current_liability`, `non_current_liability`, `future_payments`, `notes`, `metadata` |
| [LeaseModification.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Models/LeaseModification.php) | `lease_id`, `modification_ref`, `effective_date`, `kind`, `old_term_end`, `new_term_end`, `old_payment_amount`, `new_payment_amount`, `adjustment_amount`, `reason`, `metadata` |
| [LeasePayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Models/LeasePayment.php) | `lease_id`, `payment_ref`, `due_date`, `amount`, `principal_amount`, `interest_amount`, `depreciation_amount`, `status`, `posted_at`, `metadata` |
<!-- layer-implementation-plan:end -->
