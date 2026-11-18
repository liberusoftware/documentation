# CMS: Module Cms Joomla Migration Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-joomla-migration). Observed identity: [`liberusoftware/module-cms-joomla-migration-livewire`](../../../modules/source/liberusoftware--module-cms-joomla-migration-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-module-cms-joomla-migration-livewire`  
**Matching domain module:** `module-cms-joomla-migration`  
**Application:** CMS  
**Source feature:** [Module Cms Joomla Migration](../features/module-cms-joomla-migration.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Articles/categories:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Custom fields:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Contacts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Menus:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Modules/positions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Media:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Users/authors:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Tags:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Languages:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Redirects:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-module-cms-joomla-migration-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsModuleCmsJoomlaMigration::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `articles-categories`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `custom-fields`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `contacts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `menus`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `modules-positions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `media`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `users-authors`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `tags`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `languages`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `redirects`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-cms-joomla-migration` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-cms-joomla-migration.md) · [API plan](../api/module-cms-joomla-migration.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Articles/categories** | Expose a focused Livewire 4 component and namespaced Blade default view for `articles/categories` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Custom fields** | Expose a focused Livewire 4 component and namespaced Blade default view for `custom fields` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Contacts** | Expose a focused Livewire 4 component and namespaced Blade default view for `contacts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Menus** | Expose a focused Livewire 4 component and namespaced Blade default view for `menus` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Modules/positions** | Expose a focused Livewire 4 component and namespaced Blade default view for `modules/positions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Media** | Expose a focused Livewire 4 component and namespaced Blade default view for `media` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Users/authors** | Expose a focused Livewire 4 component and namespaced Blade default view for `users/authors` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Tags** | Expose a focused Livewire 4 component and namespaced Blade default view for `tags` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Languages** | Expose a focused Livewire 4 component and namespaced Blade default view for `languages` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Redirects** | Expose a focused Livewire 4 component and namespaced Blade default view for `redirects` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [JoomlaMigrationList.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-joomla-migration-livewire/src/Livewire/JoomlaMigrationList.php) · [JoomlaMigrationLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-joomla-migration-livewire/src/JoomlaMigrationLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [JoomlaMigrationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-joomla-migration/src/Services/JoomlaMigrationService.php) | `public function __construct(private MigrationFrameworkService $framework)`<br>`public function start(string $source, array $options = [], ?int $teamId = null): MigrationJob`<br>`public function add(MigrationJob $job, string $type, string $sourceId, array $payload = []): MigrationRecord`<br>`public function process(MigrationRecord $record, bool $success, ?string $reason = null): MigrationRecord`<br>`public function complete(MigrationJob $job): MigrationJob` |
<!-- layer-implementation-plan:end -->
