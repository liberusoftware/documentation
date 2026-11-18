# CMS: Module Cms Integration Directory Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-integration-directory). Observed identity: [`liberusoftware/module-cms-integration-directory-livewire`](../../../modules/source/liberusoftware--module-cms-integration-directory-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-module-cms-integration-directory-livewire`  
**Matching domain module:** `module-cms-integration-directory`  
**Application:** CMS  
**Source feature:** [Module Cms Integration Directory](../features/module-cms-integration-directory.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Provider connections:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Capability discovery:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Credentials:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Configuration tests:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Sync health:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Extension links:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-module-cms-integration-directory-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsModuleCmsIntegrationDirectory::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `provider-connections`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `capability-discovery`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `credentials`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `configuration-tests`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sync-health`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `extension-links`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-cms-integration-directory` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-cms-integration-directory.md) · [API plan](../api/module-cms-integration-directory.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Provider connections** | Expose a focused Livewire 4 component and namespaced Blade default view for `provider connections` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Capability discovery** | Expose a focused Livewire 4 component and namespaced Blade default view for `capability discovery` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Credentials** | Expose a focused Livewire 4 component and namespaced Blade default view for `credentials` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Configuration tests** | Expose a focused Livewire 4 component and namespaced Blade default view for `configuration tests` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Sync health** | Expose a focused Livewire 4 component and namespaced Blade default view for `sync health` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Extension links** | Expose a focused Livewire 4 component and namespaced Blade default view for `extension links` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [IntegrationList.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-integration-directory-livewire/src/Livewire/IntegrationList.php) · [IntegrationDirectoryLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-integration-directory-livewire/src/IntegrationDirectoryLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [IntegrationDirectoryService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-integration-directory/src/Services/IntegrationDirectoryService.php) | `public function register(string $key, string $name, string $provider, array $configuration = [], ?int $teamId = null): Integration`<br>`public function enable(Integration $integration): Integration`<br>`public function disable(Integration $integration): Integration`<br>`public function health(Integration $integration, string $status, ?string $message = null): Integration`<br>`public function enabled(?string $category = null): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Integration.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-integration-directory/src/Models/Integration.php) | `key`, `name`, `provider`, `category`, `configuration`, `status`, `health_status`, `health_message`, `last_checked_at`, `team_id` |
<!-- layer-implementation-plan:end -->
