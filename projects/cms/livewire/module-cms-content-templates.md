# CMS: Module Cms Content Templates Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-content-templates). Observed identity: [`liberusoftware/module-cms-content-templates-livewire`](../../../modules/source/liberusoftware--module-cms-content-templates-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-module-cms-content-templates-livewire`  
**Matching domain module:** `module-cms-content-templates`  
**Application:** CMS  
**Source feature:** [Module Cms Content Templates](../features/module-cms-content-templates.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Starter content:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Presets:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Default fields/blocks/layouts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Template locking:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Versioning:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Controlled rollout:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-module-cms-content-templates-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsModuleCmsContentTemplates::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `starter-content`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `presets`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `default-fields-blocks-layouts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `template-locking`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `versioning`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `controlled-rollout`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-cms-content-templates` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-cms-content-templates.md) · [API plan](../api/module-cms-content-templates.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Starter content** | Expose a focused Livewire 4 component and namespaced Blade default view for `starter content` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Presets** | Expose a focused Livewire 4 component and namespaced Blade default view for `presets` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Default fields/blocks/layouts** | Expose a focused Livewire 4 component and namespaced Blade default view for `default fields/blocks/layouts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Template locking** | Expose a focused Livewire 4 component and namespaced Blade default view for `template locking` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Versioning** | Expose a focused Livewire 4 component and namespaced Blade default view for `versioning` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Controlled rollout** | Expose a focused Livewire 4 component and namespaced Blade default view for `controlled rollout` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [TemplatePicker.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-templates-livewire/src/Livewire/TemplatePicker.php) · [ContentTemplatesLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-templates-livewire/src/ContentTemplatesLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ContentTemplatesService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-templates/src/Services/ContentTemplatesService.php) | `public function templates(?int $teamId, ?string $contentType = null, int $perPage = 25): LengthAwarePaginator`<br>`public function create(array $data, ?int $teamId = null): ContentTemplate`<br>`public function publish(ContentTemplate $template): ContentTemplate`<br>`public function lock(ContentTemplate $template): ContentTemplate`<br>`public function select(string $contentType, ?int $teamId, int $bucket = 0): ?ContentTemplate` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ContentTemplate.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-templates/src/Models/ContentTemplate.php) | `team_id`, `name`, `slug`, `content_type`, `version`, `schema`, `defaults`, `locked`, `published`, `rollout_percent` |
<!-- layer-implementation-plan:end -->
