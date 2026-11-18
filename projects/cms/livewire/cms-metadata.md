# CMS: Cms Metadata Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-metadata). Observed identity: [`liberusoftware/module-cms-metadata-livewire`](../../../modules/source/liberusoftware--module-cms-metadata-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-cms-metadata-livewire`  
**Matching domain module:** `cms-metadata`  
**Application:** CMS  
**Source feature:** [Cms Metadata](../features/cms-metadata.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Arbitrary governed metadata:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Definitions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Inheritance:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Validation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Provenance:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Indexing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **API exposure:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-cms-metadata-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsCmsMetadata::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `arbitrary-governed-metadata`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `definitions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `inheritance`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `validation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `provenance`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `indexing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `api-exposure`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-metadata` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/cms-metadata.md) · [API plan](../api/cms-metadata.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Arbitrary governed metadata** | Expose a focused Livewire 4 component and namespaced Blade default view for `arbitrary governed metadata` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Definitions** | Expose a focused Livewire 4 component and namespaced Blade default view for `definitions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Inheritance** | Expose a focused Livewire 4 component and namespaced Blade default view for `inheritance` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Validation** | Expose a focused Livewire 4 component and namespaced Blade default view for `validation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Provenance** | Expose a focused Livewire 4 component and namespaced Blade default view for `provenance` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Indexing** | Expose a focused Livewire 4 component and namespaced Blade default view for `indexing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **API exposure** | Expose a focused Livewire 4 component and namespaced Blade default view for `api exposure` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [MetadataBrowser.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-metadata-livewire/src/Livewire/MetadataBrowser.php) · [MetadataLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-metadata-livewire/src/MetadataLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [MetadataService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-metadata/src/Services/MetadataService.php) | `public function all(string $subjectType, int\|string $subjectId): array`<br>`public function get(string $subjectType, int\|string $subjectId, string $key, mixed $default = null): mixed`<br>`public function set(string $subjectType, int\|string $subjectId, string $key, mixed $value, ?int $teamId = null): MetadataEntry`<br>`public function remove(string $subjectType, int\|string $subjectId, string $key): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MetadataEntry.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-metadata/src/Models/MetadataEntry.php) | `subject_type`, `subject_id`, `key`, `value`, `value_type`, `team_id` |
<!-- layer-implementation-plan:end -->
