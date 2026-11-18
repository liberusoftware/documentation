# CMS: Module Cms Sitemaps Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-sitemaps). Observed identity: [`liberusoftware/module-cms-sitemaps-livewire`](../../../modules/source/liberusoftware--module-cms-sitemaps-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-module-cms-sitemaps-livewire`  
**Matching domain module:** `module-cms-sitemaps`  
**Application:** CMS  
**Source feature:** [Module Cms Sitemaps](../features/module-cms-sitemaps.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Site/type/locale-aware indexes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Exclusions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Images/video/news extensions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Chunking:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cache:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Search-engine notification adapters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-module-cms-sitemaps-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsModuleCmsSitemaps::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `site-type-locale-aware-indexes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `exclusions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `images-video-news-extensions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `chunking`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cache`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `search-engine-notification-adapters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-cms-sitemaps` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-cms-sitemaps.md) · [API plan](../api/module-cms-sitemaps.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Site/type/locale-aware indexes** | Expose a focused Livewire 4 component and namespaced Blade default view for `site/type/locale-aware indexes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Exclusions** | Expose a focused Livewire 4 component and namespaced Blade default view for `exclusions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Images/video/news extensions** | Expose a focused Livewire 4 component and namespaced Blade default view for `images/video/news extensions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Chunking** | Expose a focused Livewire 4 component and namespaced Blade default view for `chunking` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cache** | Expose a focused Livewire 4 component and namespaced Blade default view for `cache` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Search-engine notification adapters** | Expose a focused Livewire 4 component and namespaced Blade default view for `search-engine notification adapters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [SitemapPreview.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-sitemaps-livewire/src/Livewire/SitemapPreview.php) · [SitemapsLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-sitemaps-livewire/src/SitemapsLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SitemapService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-sitemaps/src/Services/SitemapService.php) | `public function __construct(private readonly TenantContextInterface $tenant)`<br>`public function add(string $url, ?int $siteId = null, string $type = 'web', ?string $locale = null, float $priority = .5, array $extensions = [], ?int $teamId = null): SitemapEntry`<br>`public function exclude(string $url, ?int $siteId = null): int`<br>`public function update(SitemapEntry $entry, array $attributes): SitemapEntry`<br>`public function remove(SitemapEntry $entry): void`<br>`public function entries(?int $siteId = null, ?string $type = null, ?string $locale = null): array`<br>`public function chunks(?int $siteId = null, int $size = 50000, ?string $type = null, ?string $locale = null): array`<br>`public function notify(string $engine, ?int $siteId = null): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SitemapEntry.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-sitemaps/src/Models/SitemapEntry.php) | `site_id`, `type`, `locale`, `url`, `last_modified`, `priority`, `change_frequency`, `images`, `video`, `news`, `excluded`, `team_id` |
<!-- layer-implementation-plan:end -->
