# Accounting: Accounting Branch And Location Accounting Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-branch-and-location-accounting). Observed identity: [`liberusoftware/module-accounting-branch-and-location-accounting-livewire`](../../../modules/source/liberusoftware--module-accounting-branch-and-location-accounting-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-accounting-branch-and-location-accounting-livewire`  
**Matching domain module:** `accounting-branch-and-location-accounting`  
**Application:** Accounting  
**Source feature:** [Accounting Branch And Location Accounting](../features/accounting-branch-and-location-accounting.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Branch/location dimensions or books:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Local sequences/tax:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Allocations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Performance:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Statutory requirements:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-accounting-branch-and-location-accounting-livewire` component namespace and service provider; use explicit aliases such as `<livewire:accountingAccountingBranchAndLocationAccounting::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `branch-location-dimensions-or-books`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `local-sequences-tax`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `allocations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `performance`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `statutory-requirements`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-branch-and-location-accounting` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accounting-branch-and-location-accounting.md) · [API plan](../api/accounting-branch-and-location-accounting.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Branch/location dimensions or books** | Expose a focused Livewire 4 component and namespaced Blade default view for `branch/location dimensions or books` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Local sequences/tax** | Expose a focused Livewire 4 component and namespaced Blade default view for `local sequences/tax` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Allocations** | Expose a focused Livewire 4 component and namespaced Blade default view for `allocations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Performance** | Expose a focused Livewire 4 component and namespaced Blade default view for `performance` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Statutory requirements** | Expose a focused Livewire 4 component and namespaced Blade default view for `statutory requirements` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Branches.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting-livewire/src/Livewire/Branches.php) · [BranchLocationAccountingLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting-livewire/src/BranchLocationAccountingLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [BranchQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting/src/Queries/BranchQuery.php) | `public function forTeam(int $teamId, ?string $status = null): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocateBranchValue.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting/src/Actions/AllocateBranchValue.php) | `public function handle(Branch $branch, float $amount): array` |
| [CreateBranch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting/src/Actions/CreateBranch.php) | `public function handle(array $attributes): Branch` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Branch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting/src/Models/Branch.php) | `team_id`, `code`, `name`, `location`, `local_tax_code`, `sequence_prefix`, `allocation_rule`, `performance_target`, `statutory_reference`, `status`, `metadata` |
<!-- layer-implementation-plan:end -->
