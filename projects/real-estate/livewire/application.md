# Real Estate: Application Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#application). Observed identity: [`liberusoftware/application-livewire`](../../../modules/source/liberusoftware--application-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-real-estate-application-livewire`  
**Matching domain module:** `application`  
**Application:** Real Estate  
**Source feature:** [Application](../features/application.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Environment validation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Application metadata:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Health/readiness:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Maintenance mode:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Identifiers:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Clocks:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Shared service contracts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-real-estate-application-livewire` component namespace and service provider; use explicit aliases such as `<livewire:realestateApplication::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `environment-validation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `application-metadata`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `health-readiness`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `maintenance-mode`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `identifiers`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `clocks`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `shared-service-contracts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `application` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-real-estate-laravel-filament`](https://github.com/liberusoftware/project-real-estate-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/application.md) · [API plan](../api/application.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Environment validation** | Expose a focused Livewire 4 component and namespaced Blade default view for `environment validation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Application metadata** | Expose a focused Livewire 4 component and namespaced Blade default view for `application metadata` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Health/readiness** | Expose a focused Livewire 4 component and namespaced Blade default view for `health/readiness` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Maintenance mode** | Expose a focused Livewire 4 component and namespaced Blade default view for `maintenance mode` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Identifiers** | Expose a focused Livewire 4 component and namespaced Blade default view for `identifiers` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Clocks** | Expose a focused Livewire 4 component and namespaced Blade default view for `clocks` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Shared service contracts** | Expose a focused Livewire 4 component and namespaced Blade default view for `shared service contracts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Overview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application-livewire/src/Livewire/Overview.php) · [ApplicationLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application-livewire/src/ApplicationLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [Clock.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/src/Contracts/Clock.php) | `public function now(): \DateTimeImmutable` |
| [IdentifierFactory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/src/Contracts/IdentifierFactory.php) | `public function make(): string` |
<!-- layer-implementation-plan:end -->
