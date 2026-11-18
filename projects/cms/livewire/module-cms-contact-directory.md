# CMS: Module Cms Contact Directory Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-contact-directory). Observed identity: [`liberusoftware/module-cms-contact-directory-livewire`](../../../modules/source/liberusoftware--module-cms-contact-directory-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-module-cms-contact-directory-livewire`  
**Matching domain module:** `module-cms-contact-directory`  
**Application:** CMS  
**Source feature:** [Module Cms Contact Directory](../features/module-cms-contact-directory.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **People/departments/contact records:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Categories:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Locations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Contact forms:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Protected fields:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Directory views:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-module-cms-contact-directory-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsModuleCmsContactDirectory::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `people-departments-contact-records`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `categories`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `locations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `contact-forms`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `protected-fields`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `directory-views`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-cms-contact-directory` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-cms-contact-directory.md) · [API plan](../api/module-cms-contact-directory.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **People/departments/contact records** | Expose a focused Livewire 4 component and namespaced Blade default view for `people/departments/contact records` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Categories** | Expose a focused Livewire 4 component and namespaced Blade default view for `categories` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Locations** | Expose a focused Livewire 4 component and namespaced Blade default view for `locations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Contact forms** | Expose a focused Livewire 4 component and namespaced Blade default view for `contact forms` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Protected fields** | Expose a focused Livewire 4 component and namespaced Blade default view for `protected fields` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Directory views** | Expose a focused Livewire 4 component and namespaced Blade default view for `directory views` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ContactDirectory.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-contact-directory-livewire/src/Livewire/ContactDirectory.php) · [ContactDirectoryLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-contact-directory-livewire/src/ContactDirectoryLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ContactDirectoryService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-contact-directory/src/Services/ContactDirectoryService.php) | `public function contacts(?int $teamId, bool $publicOnly = false, int $perPage = 25): LengthAwarePaginator`<br>`public function saveContact(array $data, ?int $teamId = null): Contact`<br>`public function category(array $data, ?int $teamId = null): ContactCategory`<br>`public function location(array $data, ?int $teamId = null): ContactLocation`<br>`public function form(array $data, ?int $teamId = null): ContactForm` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Contact.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-contact-directory/src/Models/Contact.php) | `team_id`, `category_id`, `location_id`, `name`, `department`, `email`, `phone`, `details`, `is_public` |
| [ContactCategory.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-contact-directory/src/Models/ContactCategory.php) | `team_id`, `name`, `slug` |
| [ContactForm.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-contact-directory/src/Models/ContactForm.php) | `team_id`, `name`, `schema`, `is_active` |
| [ContactLocation.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-contact-directory/src/Models/ContactLocation.php) | `team_id`, `name`, `address`, `city`, `country` |
<!-- layer-implementation-plan:end -->
