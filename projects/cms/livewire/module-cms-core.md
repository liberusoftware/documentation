# CMS: Module Cms Core Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-core). Observed identity: [`liberusoftware/module-cms-core-livewire`](../../../modules/source/liberusoftware--module-cms-core-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-module-cms-core-livewire`  
**Matching domain module:** `module-cms-core`  
**Application:** CMS  
**Source feature:** [Module Cms Core](../features/module-cms-core.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Sites:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Channels:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Content identity:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Aliases:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Ownership:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Shared terminology:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Settings:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Domain events:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-module-cms-core-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsModuleCmsCore::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `sites`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `channels`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `content-identity`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `aliases`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `ownership`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `shared-terminology`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `settings`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `domain-events`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-cms-core` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-cms-core.md) · [API plan](../api/module-cms-core.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Sites** | Expose a focused Livewire 4 component and namespaced Blade default view for `sites` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Channels** | Expose a focused Livewire 4 component and namespaced Blade default view for `channels` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Content identity** | Expose a focused Livewire 4 component and namespaced Blade default view for `content identity` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Aliases** | Expose a focused Livewire 4 component and namespaced Blade default view for `aliases` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Ownership** | Expose a focused Livewire 4 component and namespaced Blade default view for `ownership` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Shared terminology** | Expose a focused Livewire 4 component and namespaced Blade default view for `shared terminology` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Settings** | Expose a focused Livewire 4 component and namespaced Blade default view for `settings` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Domain events** | Expose a focused Livewire 4 component and namespaced Blade default view for `domain events` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ChannelList.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-core-livewire/src/Livewire/ChannelList.php) · [SiteList.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-core-livewire/src/Livewire/SiteList.php) · [CoreLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-core-livewire/src/CoreLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CoreQueryService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Queries/CoreQueryService.php) | `public function sites(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function site(string $key): ?Site`<br>`public function channels(string $siteKey, int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function alias(string $siteKey, string $alias): ?ContentAlias`<br>`public function aliases(string $siteKey, int $perPage = 15): LengthAwarePaginator`<br>`public function identities(string $siteKey, int $perPage = 15): LengthAwarePaginator`<br>`public function settings(string $siteKey, int $perPage = 15, string $environment = 'production'): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CoreMutationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Actions/CoreMutationService.php) | `public function createSite(array $attributes): Site`<br>`public function createChannel(Site\|int\|string $site, array $attributes): Channel`<br>`public function updateSite(Site $site, array $attributes): Site`<br>`public function updateChannel(Channel $channel, array $attributes): Channel`<br>`public function deleteSite(Site $site): void`<br>`public function deleteChannel(Channel $channel): void`<br>`public function createIdentity(Site\|int\|string $site, array $attributes): ContentIdentity`<br>`public function createAlias(Site\|int\|string $site, array $attributes): ContentAlias`<br>`public function putSetting(?Site $site, string $key, array $value, string $environment = 'production'): Setting` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Channel.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/Channel.php) | `site_id`, `key`, `name`, `type`, `settings`, `team_id` |
| [ContentAlias.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/ContentAlias.php) | `site_id`, `channel_id`, `alias`, `target_type`, `target_id`, `redirect_status`, `team_id` |
| [ContentIdentity.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/ContentIdentity.php) | `site_id`, `channel_id`, `content_type`, `content_id`, `canonical_path`, `status`, `owner_type`, `owner_id`, `metadata`, `team_id` |
| [Setting.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/Setting.php) | `site_id`, `key`, `value`, `environment` |
| [Site.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/Site.php) | `key`, `name`, `domain`, `default_locale`, `timezone`, `status`, `settings`, `team_id` |
<!-- layer-implementation-plan:end -->
