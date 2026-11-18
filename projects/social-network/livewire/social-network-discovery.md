# Social Network: Social Network Discovery Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-discovery). Observed identity: [`liberusoftware/module-social-network-discovery-livewire`](../../../modules/source/liberusoftware--module-social-network-discovery-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-social-network-social-network-discovery-livewire`  
**Matching domain module:** `social-network-discovery`  
**Application:** Social Network  
**Source feature:** [Social Network Discovery](../features/social-network-discovery.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Search:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Hashtags:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Trends:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Recommendations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Directories:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Privacy-aware indexing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-social-network-social-network-discovery-livewire` component namespace and service provider; use explicit aliases such as `<livewire:socialnetworkSocialNetworkDiscovery::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `search`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `hashtags`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `trends`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `recommendations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `directories`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `privacy-aware-indexing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `social-network-discovery` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/social-network-discovery.md) · [API plan](../api/social-network-discovery.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Search** | Expose a focused Livewire 4 component and namespaced Blade default view for `search` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Hashtags** | Expose a focused Livewire 4 component and namespaced Blade default view for `hashtags` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Trends** | Expose a focused Livewire 4 component and namespaced Blade default view for `trends` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Recommendations** | Expose a focused Livewire 4 component and namespaced Blade default view for `recommendations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Directories** | Expose a focused Livewire 4 component and namespaced Blade default view for `directories` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Privacy-aware indexing** | Expose a focused Livewire 4 component and namespaced Blade default view for `privacy-aware indexing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Search.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery-livewire/src/Components/Search.php) · [DiscoveryLivewireServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery-livewire/src/DiscoveryLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [IndexResource.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/src/Actions/IndexResource.php) | `public function __construct(private DiscoveryAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $owner, array $attributes): DiscoveryIndex` |
| [ListTrends.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/src/Actions/ListTrends.php) | `public function __construct(private DiscoveryAuthorizer $authorizer)`<br>`public function handle(Profile $viewer, int $limit = 20): array` |
| [SearchDiscovery.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/src/Actions/SearchDiscovery.php) | `public function __construct(private DiscoveryAuthorizer $authorizer)`<br>`public function handle(Profile $viewer, string $query, int $limit = 25): Collection` |
| [DiscoveryAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/src/Contracts/DiscoveryAuthorizer.php) | `public function search(Profile $viewer): void`<br>`public function index(Profile $owner): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DiscoveryIndex.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery/src/Models/DiscoveryIndex.php) | `id`, `resource_type`, `resource_id`, `owner_profile_id`, `visibility`, `body`, `terms`, `engagement_score`, `published_at` |
<!-- layer-implementation-plan:end -->
