# CRM: Agency Workspace Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#agency-workspace). Observed identity: [`liberusoftware/module-crm-agency-workspace-livewire`](../../../modules/source/liberusoftware--module-crm-agency-workspace-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-agency-workspace-livewire`  
**Matching domain module:** `crm-agency-workspace`  
**Application:** CRM  
**Source feature:** [Agency Workspace](../features/agency-workspace.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Agency/client hierarchy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Sub-accounts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Delegated administration:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Usage visibility:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Support access:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Branding:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cross-account operations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-agency-workspace-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-agency-workspace::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `agency-client-hierarchy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sub-accounts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `delegated-administration`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `usage-visibility`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `support-access`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `branding`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cross-account-operations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-agency-workspace` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/agency-workspace.md) · [API plan](../api/agency-workspace.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Agency/client hierarchy** | Expose a focused Livewire 4 component and namespaced Blade default view for `agency/client hierarchy` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Sub-accounts** | Expose a focused Livewire 4 component and namespaced Blade default view for `sub-accounts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Delegated administration** | Expose a focused Livewire 4 component and namespaced Blade default view for `delegated administration` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Usage visibility** | Expose a focused Livewire 4 component and namespaced Blade default view for `usage visibility` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Support access** | Expose a focused Livewire 4 component and namespaced Blade default view for `support access` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Branding** | Expose a focused Livewire 4 component and namespaced Blade default view for `branding` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cross-account operations** | Expose a focused Livewire 4 component and namespaced Blade default view for `cross-account operations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [AgencyWorkspaceLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace-livewire/src/AgencyWorkspaceLivewireServiceProvider.php) · [AgencyAccountBrowser.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace-livewire/src/Components/AgencyAccountBrowser.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AgencyQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Queries/AgencyQuery.php) | `public function accounts(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAgencyAccount.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Actions/CreateAgencyAccount.php) | `public function execute(int $teamId, int $ownerId, array $input): AgencyAccount` |
| [GrantAgencyAccess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Actions/GrantAgencyAccess.php) | `public function execute(int $teamId, int $actorId, AgencyAccount $account, array $input): AgencyAccess` |
| [UpdateAgencyUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Actions/UpdateAgencyUsage.php) | `public function execute(int $teamId, int $actorId, AgencyAccount $account, array $input): AgencyAccount` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AgencyAccess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Models/AgencyAccess.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgencyAccount.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Models/AgencyAccount.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgencyAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Models/AgencyAudit.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
