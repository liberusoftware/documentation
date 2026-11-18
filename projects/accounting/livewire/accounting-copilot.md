# Accounting: Accounting Copilot Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-copilot). Observed identity: [`liberusoftware/module-accounting-copilot-livewire`](../../../modules/source/liberusoftware--module-accounting-copilot-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-copilot-livewire`  
**Matching domain module:** `accounting-copilot`  
**Application:** Accounting  
**Source feature:** [Accounting Copilot](../features/accounting-copilot.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Permission-bounded search:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Explanations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Summaries:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Report narratives:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Draft transactions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Explicit action confirmation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-copilot-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-copilot::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `permission-bounded-search`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `explanations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `summaries`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `report-narratives`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `draft-transactions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `explicit-action-confirmation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-copilot` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accounting-copilot.md) · [API plan](../api/accounting-copilot.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Permission-bounded search** | Expose a focused Livewire 4 component and namespaced Blade default view for `permission-bounded search` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Explanations** | Expose a focused Livewire 4 component and namespaced Blade default view for `explanations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Summaries** | Expose a focused Livewire 4 component and namespaced Blade default view for `summaries` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Report narratives** | Expose a focused Livewire 4 component and namespaced Blade default view for `report narratives` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Draft transactions** | Expose a focused Livewire 4 component and namespaced Blade default view for `draft transactions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Explicit action confirmation** | Expose a focused Livewire 4 component and namespaced Blade default view for `explicit action confirmation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Requests.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-copilot-livewire/src/Livewire/Requests.php) · [CopilotLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-copilot-livewire/src/CopilotLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CopilotRequestQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-copilot/src/Queries/CopilotRequestQuery.php) | `public function forTeam(int $teamId, ?string $kind = null): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfirmCopilotRequest.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-copilot/src/Actions/ConfirmCopilotRequest.php) | `public function handle(CopilotRequest $request, string $confirmationKey): CopilotRequest` |
| [CreateCopilotRequest.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-copilot/src/Actions/CreateCopilotRequest.php) | `public function handle(array $attributes): CopilotRequest` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CopilotRequest.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-copilot/src/Models/CopilotRequest.php) | `team_id`, `actor_id`, `kind`, `prompt`, `result`, `status`, `confirmation_key`, `metadata` |
<!-- layer-implementation-plan:end -->
