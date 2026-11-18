# CMS: Module Cms Field System Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-field-system). Observed identity: [`liberusoftware/module-cms-field-system-livewire`](../../../modules/source/liberusoftware--module-cms-field-system-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-module-cms-field-system-livewire`  
**Matching domain module:** `module-cms-field-system`  
**Application:** CMS  
**Source feature:** [Module Cms Field System](../features/module-cms-field-system.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Reusable typed fields:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cardinality:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Defaults:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Validation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Computed fields:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Conditional fields:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Field groups:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Schema migrations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-module-cms-field-system-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsModuleCmsFieldSystem::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `reusable-typed-fields`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cardinality`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `defaults`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `validation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `computed-fields`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `conditional-fields`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `field-groups`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `schema-migrations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-cms-field-system` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-cms-field-system.md) · [API plan](../api/module-cms-field-system.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Reusable typed fields** | Expose a focused Livewire 4 component and namespaced Blade default view for `reusable typed fields` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cardinality** | Expose a focused Livewire 4 component and namespaced Blade default view for `cardinality` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Defaults** | Expose a focused Livewire 4 component and namespaced Blade default view for `defaults` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Validation** | Expose a focused Livewire 4 component and namespaced Blade default view for `validation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Computed fields** | Expose a focused Livewire 4 component and namespaced Blade default view for `computed fields` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Conditional fields** | Expose a focused Livewire 4 component and namespaced Blade default view for `conditional fields` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Field groups** | Expose a focused Livewire 4 component and namespaced Blade default view for `field groups` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Schema migrations** | Expose a focused Livewire 4 component and namespaced Blade default view for `schema migrations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [SchemaBrowser.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-field-system-livewire/src/Livewire/SchemaBrowser.php) · [FieldSystemLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-field-system-livewire/src/FieldSystemLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [FieldSystemService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-field-system/src/Services/FieldSystemService.php) | `public function __construct(private FieldTypeRegistryInterface $types)`<br>`public function saveSchema(?int $teamId, string $key, string $name, array $fields, ?string $reason = null): FieldSchema`<br>`public function validateData(FieldSchema $schema, array $data): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FieldSchema.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-field-system/src/Models/FieldSchema.php) | `team_id`, `key`, `name`, `version`, `fields`, `history` |
<!-- layer-implementation-plan:end -->
