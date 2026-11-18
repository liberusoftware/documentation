# CMS: Multisite Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#multisite). Observed identity: [`liberusoftware/module-cms-multisite-livewire`](../../../modules/source/liberusoftware--module-cms-multisite-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-multisite-livewire`  
**Matching domain module:** `cms-multisite`  
**Application:** CMS  
**Source feature:** [Multisite](../features/multisite.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Site network:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Shared/isolated content:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Domains:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Site admins:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Quotas:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Site lifecycle:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Network operations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Safe cross-site references:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-multisite-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-cms-multisite::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `site-network`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `shared-isolated-content`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `domains`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `site-admins`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `quotas`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `site-lifecycle`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `network-operations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `safe-cross-site-references`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-multisite` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/multisite.md) · [API plan](../api/multisite.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Site network** | Expose a focused Livewire 4 component and namespaced Blade default view for `site network` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Shared/isolated content** | Expose a focused Livewire 4 component and namespaced Blade default view for `shared/isolated content` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Domains** | Expose a focused Livewire 4 component and namespaced Blade default view for `domains` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Site admins** | Expose a focused Livewire 4 component and namespaced Blade default view for `site admins` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Quotas** | Expose a focused Livewire 4 component and namespaced Blade default view for `quotas` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Site lifecycle** | Expose a focused Livewire 4 component and namespaced Blade default view for `site lifecycle` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Network operations** | Expose a focused Livewire 4 component and namespaced Blade default view for `network operations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Safe cross-site references** | Expose a focused Livewire 4 component and namespaced Blade default view for `safe cross-site references` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [SiteNetwork.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-multisite-livewire/src/Livewire/SiteNetwork.php) · [MultisiteLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-multisite-livewire/src/MultisiteLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [MultisiteService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-multisite/src/Services/MultisiteService.php) | `public function __construct(private SiteFactoryService $factory)`<br>`public function createSite(string $key, string $name, ?string $domain = null, ?int $teamId = null): Site`<br>`public function transition(Site $site, string $status): Site`<br>`public function setQuota(Site $site, array $limits): SiteQuota`<br>`public function recordUsage(SiteQuota $quota, array $delta): SiteQuota`<br>`public function assignAdmin(Site $site, int $userId, string $role = 'editor'): SiteAdmin`<br>`public function removeAdmin(SiteAdmin $admin): void`<br>`public function reference(Site $source, Site $target, string $contentType, string $contentId, string $mode = 'shared'): SiteReference`<br>`public function networkTransition(array $siteIds, string $status): int` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SiteAdmin.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-multisite/src/Models/SiteAdmin.php) | `site_id`, `user_id`, `role`, `active`, `team_id` |
| [SiteQuota.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-multisite/src/Models/SiteQuota.php) | `site_id`, `limits`, `usage`, `team_id` |
| [SiteReference.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-multisite/src/Models/SiteReference.php) | `source_site_id`, `target_site_id`, `content_type`, `content_id`, `mode`, `status`, `team_id` |
<!-- layer-implementation-plan:end -->
