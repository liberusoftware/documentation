# CRM: Crm Account Planning Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-account-planning). Observed identity: [`liberusoftware/module-crm-account-planning-livewire`](../../../modules/source/liberusoftware--module-crm-account-planning-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-account-planning-livewire`  
**Matching domain module:** `crm-account-planning`  
**Application:** CRM  
**Source feature:** [Crm Account Planning](../features/crm-account-planning.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Account hierarchies:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Stakeholders:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Influence maps:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Whitespace:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Account plans:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Objectives:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Risks:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Mutual action plans:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Account-based coordination:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-account-planning-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmAccountPlanning::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `account-hierarchies`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `stakeholders`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `influence-maps`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `whitespace`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `account-plans`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `objectives`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `risks`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `mutual-action-plans`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `account-based-coordination`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-account-planning` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-account-planning.md) · [API plan](../api/crm-account-planning.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Account hierarchies** | Expose a focused Livewire 4 component and namespaced Blade default view for `account hierarchies` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Stakeholders** | Expose a focused Livewire 4 component and namespaced Blade default view for `stakeholders` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Influence maps** | Expose a focused Livewire 4 component and namespaced Blade default view for `influence maps` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Whitespace** | Expose a focused Livewire 4 component and namespaced Blade default view for `whitespace` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Account plans** | Expose a focused Livewire 4 component and namespaced Blade default view for `account plans` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Objectives** | Expose a focused Livewire 4 component and namespaced Blade default view for `objectives` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Risks** | Expose a focused Livewire 4 component and namespaced Blade default view for `risks` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Mutual action plans** | Expose a focused Livewire 4 component and namespaced Blade default view for `mutual action plans` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Account-based coordination** | Expose a focused Livewire 4 component and namespaced Blade default view for `account-based coordination` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [AccountPlanningLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning-livewire/src/AccountPlanningLivewireServiceProvider.php) · [AccountPlanningWorkspace.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning-livewire/src/Components/AccountPlanningWorkspace.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AccountPlanningQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning/src/Queries/AccountPlanningQuery.php) | `public function records(int $teamId, ?string $kind = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [TransitionRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning/src/Actions/TransitionRecord.php) | `public function execute(int $teamId, int $id, string $status): AccountPlanningRecord` |
| [UpsertRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning/src/Actions/UpsertRecord.php) | `public function execute(int $teamId, array $attributes, ?int $id = null): AccountPlanningRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccountPlanningRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning/src/Models/AccountPlanningRecord.php) | `team_id`, `kind`, `name`, `status`, `account_id`, `owner_id`, `payload`, `starts_at`, `ends_at`, `completed_at` |
<!-- layer-implementation-plan:end -->
