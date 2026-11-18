# Accounting: Close Management Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#close-management). Observed identity: [`liberusoftware/module-accounting-close-management-livewire`](../../../modules/source/liberusoftware--module-accounting-close-management-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-close-management-livewire`  
**Matching domain module:** `accounting-close-management`  
**Application:** Accounting  
**Source feature:** [Close Management](../features/close-management.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Checklist:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Owners:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Dependencies:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Due dates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Evidence:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reconciliations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Adjustments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Review:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Certification:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Lock:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reopen:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-close-management-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-close-management::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `checklist`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `owners`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `dependencies`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `due-dates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `evidence`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reconciliations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `adjustments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `review`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `certification`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `lock`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reopen`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-close-management` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/close-management.md) · [API plan](../api/close-management.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Checklist** | Expose a focused Livewire 4 component and namespaced Blade default view for `checklist` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Owners** | Expose a focused Livewire 4 component and namespaced Blade default view for `owners` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Dependencies** | Expose a focused Livewire 4 component and namespaced Blade default view for `dependencies` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Due dates** | Expose a focused Livewire 4 component and namespaced Blade default view for `due dates` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Evidence** | Expose a focused Livewire 4 component and namespaced Blade default view for `evidence` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reconciliations** | Expose a focused Livewire 4 component and namespaced Blade default view for `reconciliations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Adjustments** | Expose a focused Livewire 4 component and namespaced Blade default view for `adjustments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Review** | Expose a focused Livewire 4 component and namespaced Blade default view for `review` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Certification** | Expose a focused Livewire 4 component and namespaced Blade default view for `certification` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Lock** | Expose a focused Livewire 4 component and namespaced Blade default view for `lock` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reopen** | Expose a focused Livewire 4 component and namespaced Blade default view for `reopen` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CloseManagementLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management-livewire/src/CloseManagementLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CloseCycleQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Queries/CloseCycleQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CertifyCloseCycle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Actions/CertifyCloseCycle.php) | `public function handle(CloseCycle $cycle, array $certification): CloseCycle` |
| [CreateCloseCycle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Actions/CreateCloseCycle.php) | `public function handle(array $attributes): CloseCycle` |
| [LockCloseCycle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Actions/LockCloseCycle.php) | `public function handle(CloseCycle $cycle): CloseCycle` |
| [RecordCloseEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Actions/RecordCloseEvidence.php) | `public function handle(CloseCycle $cycle, array $evidence): CloseCycle` |
| [ReopenCloseCycle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Actions/ReopenCloseCycle.php) | `public function handle(CloseCycle $cycle, string $reason): CloseCycle` |
| [UpdateCloseChecklist.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Actions/UpdateCloseChecklist.php) | `public function handle(CloseCycle $cycle, array $checklist): CloseCycle` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CloseCycle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Models/CloseCycle.php) | `team_id`, `cycle_ref`, `period`, `due_date`, `status`, `checklist`, `owners`, `dependencies`, `evidence`, `reconciliations`, `adjustments`, `review`, `certification` |
<!-- layer-implementation-plan:end -->
