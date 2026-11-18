# CMS: Configuration Management Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#configuration-management). Observed identity: [`liberusoftware/module-cms-configuration-management-livewire`](../../../modules/source/liberusoftware--module-cms-configuration-management-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-configuration-management-livewire`  
**Matching domain module:** `cms-configuration-management`  
**Application:** CMS  
**Source feature:** [Configuration Management](../features/configuration-management.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Exportable versioned CMS configuration:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Environment comparison:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Dependency validation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Promotion:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Secrets exclusion:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Rollback:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-configuration-management-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-cms-configuration-management::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `exportable-versioned-cms-configuration`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `environment-comparison`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `dependency-validation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `promotion`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `secrets-exclusion`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `rollback`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-configuration-management` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/configuration-management.md) · [API plan](../api/configuration-management.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Exportable versioned CMS configuration** | Expose a focused Livewire 4 component and namespaced Blade default view for `exportable versioned cms configuration` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Environment comparison** | Expose a focused Livewire 4 component and namespaced Blade default view for `environment comparison` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Dependency validation** | Expose a focused Livewire 4 component and namespaced Blade default view for `dependency validation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Promotion** | Expose a focused Livewire 4 component and namespaced Blade default view for `promotion` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Secrets exclusion** | Expose a focused Livewire 4 component and namespaced Blade default view for `secrets exclusion` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Rollback** | Expose a focused Livewire 4 component and namespaced Blade default view for `rollback` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ConfigurationReleases.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-configuration-management-livewire/src/Livewire/ConfigurationReleases.php) · [ConfigurationManagementLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-configuration-management-livewire/src/ConfigurationManagementLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfigurationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-configuration-management/src/Services/ConfigurationService.php) | `public function __construct(private DatabaseManager $db)`<br>`public function releases(?int $teamId, string $environment, int $perPage = 25): LengthAwarePaginator`<br>`public function export(array $payload, string $version, string $environment, ?int $actorId = null, ?int $teamId = null, array $dependencies = []): ConfigurationRelease`<br>`public function compare(ConfigurationRelease $from, ConfigurationRelease $to): array`<br>`public function validateDependencies(ConfigurationRelease $release, array $available): array`<br>`public function promote(ConfigurationRelease $release, array $available = []): ConfigurationRelease`<br>`public function rollback(ConfigurationRelease $release): ConfigurationRelease` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ConfigurationRelease.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-configuration-management/src/Models/ConfigurationRelease.php) | `team_id`, `version`, `environment`, `payload`, `dependencies`, `checksum`, `status`, `created_by`, `promoted_at`, `rolled_back_at` |
<!-- layer-implementation-plan:end -->
