# CMS: CMS Copilot Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-copilot). Observed identity: [`liberusoftware/module-cms-copilot-livewire`](../../../modules/source/liberusoftware--module-cms-copilot-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-copilot-livewire`  
**Matching domain module:** `cms-copilot`  
**Application:** CMS  
**Source feature:** [CMS Copilot](../features/cms-copilot.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Permission-bounded search:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Summaries:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Drafting:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Transforms:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Metadata:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Internal links:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Action confirmation via Automation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-copilot-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-cms-copilot::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `permission-bounded-search`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `summaries`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `drafting`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `transforms`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `metadata`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `internal-links`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `action-confirmation-via-automation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-copilot` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/cms-copilot.md) · [API plan](../api/cms-copilot.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Permission-bounded search** | Expose a focused Livewire 4 component and namespaced Blade default view for `permission-bounded search` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Summaries** | Expose a focused Livewire 4 component and namespaced Blade default view for `summaries` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Drafting** | Expose a focused Livewire 4 component and namespaced Blade default view for `drafting` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Transforms** | Expose a focused Livewire 4 component and namespaced Blade default view for `transforms` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Metadata** | Expose a focused Livewire 4 component and namespaced Blade default view for `metadata` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Internal links** | Expose a focused Livewire 4 component and namespaced Blade default view for `internal links` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Action confirmation via Automation** | Expose a focused Livewire 4 component and namespaced Blade default view for `action confirmation via automation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CopilotConsole.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-copilot-livewire/src/Livewire/CopilotConsole.php) · [CopilotLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-copilot-livewire/src/CopilotLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CopilotHandlerInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-copilot/src/Contracts/CopilotHandlerInterface.php) | `public function capability(): string`<br>`public function handle(string $prompt, array $input): array` |
| [CopilotService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-copilot/src/Services/CopilotService.php) | `public function submit(?int $teamId, string $capability, string $prompt, array $input = [], ?string $idempotencyKey = null): CopilotRequest`<br>`public function execute(CopilotRequest $request): CopilotRequest`<br>`public function requireConfirmation(CopilotRequest $request): string`<br>`public function confirm(CopilotRequest $request, string $token): CopilotRequest`<br>`public function registerHandler(CopilotHandlerInterface $handler): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CopilotRequest.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-copilot/src/Models/CopilotRequest.php) | `team_id`, `capability`, `prompt`, `input`, `result`, `status`, `idempotency_key`, `confirmation_hash`, `confirmed_at`, `failure_reason` |
<!-- layer-implementation-plan:end -->
