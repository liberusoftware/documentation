# CMS: Module Cms Posts Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-posts). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-module-cms-posts-livewire`  
**Matching domain module:** `module-cms-posts`  
**Application:** CMS  
**Source feature:** [Module Cms Posts](../features/module-cms-posts.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Articles and editorial posts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Authors and contributor attribution:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Series and category assignments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Scheduled publication and feeds:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reading metadata and SEO:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-module-cms-posts-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsModuleCmsPosts::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `articles-and-editorial-posts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `authors-and-contributor-attribution`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `series-and-category-assignments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `scheduled-publication-and-feeds`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reading-metadata-and-seo`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-cms-posts` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-cms-posts.md) · [API plan](../api/module-cms-posts.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Articles and editorial posts** | Expose a focused Livewire 4 component and namespaced Blade default view for `articles and editorial posts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Authors and contributor attribution** | Expose a focused Livewire 4 component and namespaced Blade default view for `authors and contributor attribution` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Series and category assignments** | Expose a focused Livewire 4 component and namespaced Blade default view for `series and category assignments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Scheduled publication and feeds** | Expose a focused Livewire 4 component and namespaced Blade default view for `scheduled publication and feeds` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reading metadata and SEO** | Expose a focused Livewire 4 component and namespaced Blade default view for `reading metadata and seo` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [PostRepositoryInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Contracts/PostRepositoryInterface.php) | `public function find(int $id): ?Post`<br>`public function findBySlug(string $slug): ?Post`<br>`public function published(): array`<br>`public function featured(): array`<br>`public function byCategory(string $categorySlug): array`<br>`public function byTag(string $tagSlug): array`<br>`public function search(string $query, int $limit): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Category.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Models/Category.php) | `name`, `slug`, `description`, `team_id` |
| [Post.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Models/Post.php) | `title`, `slug`, `content`, `excerpt`, `status`, `published_at`, `is_featured`, `featured_media_id`, `author_id`, `team_id` |
| [Tag.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Models/Tag.php) | `name`, `slug`, `team_id` |
<!-- layer-implementation-plan:end -->
