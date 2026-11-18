# Accounting: Accountant Workspace Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accountant-workspace). Observed identity: [`liberusoftware/module-accounting-accountant-workspace-livewire`](../../../modules/source/liberusoftware--module-accounting-accountant-workspace-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-accountant-workspace-livewire`  
**Matching domain module:** `accounting-accountant-workspace`  
**Application:** Accounting  
**Source feature:** [Accountant Workspace](../features/accountant-workspace.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Client/entity portfolio:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Status:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Deadlines:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Alerts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Access:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Notes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Requests:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Recent changes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Drill-through:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-accountant-workspace-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-accountant-workspace::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `client-entity-portfolio`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `status`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `deadlines`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `alerts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `access`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `notes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `requests`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `recent-changes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `drill-through`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-accountant-workspace` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accountant-workspace.md) · [API plan](../api/accountant-workspace.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Client/entity portfolio** | Expose a focused Livewire 4 component and namespaced Blade default view for `client/entity portfolio` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Status** | Expose a focused Livewire 4 component and namespaced Blade default view for `status` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Deadlines** | Expose a focused Livewire 4 component and namespaced Blade default view for `deadlines` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Alerts** | Expose a focused Livewire 4 component and namespaced Blade default view for `alerts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Access** | Expose a focused Livewire 4 component and namespaced Blade default view for `access` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Notes** | Expose a focused Livewire 4 component and namespaced Blade default view for `notes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Requests** | Expose a focused Livewire 4 component and namespaced Blade default view for `requests` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Recent changes** | Expose a focused Livewire 4 component and namespaced Blade default view for `recent changes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Drill-through** | Expose a focused Livewire 4 component and namespaced Blade default view for `drill-through` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Workspace.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accountant-workspace-livewire/src/Livewire/Workspace.php) · [AccountantWorkspaceLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accountant-workspace-livewire/src/AccountantWorkspaceLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [WorkspaceQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accountant-workspace/src/Queries/WorkspaceQuery.php) | `public function paginate(int $teamId, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateWorkspaceItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accountant-workspace/src/Actions/CreateWorkspaceItem.php) | `public function handle(array $attributes): WorkspaceItem` |
| [WorkspacePolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accountant-workspace-api/src/Policies/WorkspacePolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WorkspaceItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accountant-workspace/src/Models/WorkspaceItem.php) | `team_id`, `subject_type`, `subject_id`, `name`, `status`, `next_deadline`, `alerts`, `notes`, `requests`, `metadata` |
<!-- layer-implementation-plan:end -->
