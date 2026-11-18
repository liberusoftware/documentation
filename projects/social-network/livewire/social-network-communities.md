# Social Network: Social Network Communities Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-communities). Observed identity: [`liberusoftware/module-social-network-communities-livewire`](../../../modules/source/liberusoftware--module-social-network-communities-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-social-network-social-network-communities-livewire`  
**Matching domain module:** `social-network-communities`  
**Application:** Social Network  
**Source feature:** [Social Network Communities](../features/social-network-communities.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Groups/pages:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Memberships:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Roles:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Rules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Feeds:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Files:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Questions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Moderation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-social-network-social-network-communities-livewire` component namespace and service provider; use explicit aliases such as `<livewire:socialnetworkSocialNetworkCommunities::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `groups-pages`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `memberships`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `roles`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `rules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `feeds`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `files`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `questions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `moderation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `social-network-communities` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/social-network-communities.md) · [API plan](../api/social-network-communities.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Groups/pages** | Expose a focused Livewire 4 component and namespaced Blade default view for `groups/pages` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Memberships** | Expose a focused Livewire 4 component and namespaced Blade default view for `memberships` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Roles** | Expose a focused Livewire 4 component and namespaced Blade default view for `roles` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Rules** | Expose a focused Livewire 4 component and namespaced Blade default view for `rules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Feeds** | Expose a focused Livewire 4 component and namespaced Blade default view for `feeds` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Files** | Expose a focused Livewire 4 component and namespaced Blade default view for `files` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Questions** | Expose a focused Livewire 4 component and namespaced Blade default view for `questions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Moderation** | Expose a focused Livewire 4 component and namespaced Blade default view for `moderation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CommunitiesLivewireServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities-livewire/src/CommunitiesLivewireServiceProvider.php) · [Creator.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities-livewire/src/Components/Creator.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCommunity.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Actions/CreateCommunity.php) | `public function __construct(private CommunityAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $owner, array $attributes): Community` |
| [JoinCommunity.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Actions/JoinCommunity.php) | `public function __construct(private CommunityAuthorizer $authorizer)`<br>`public function handle(Profile $member, Community $community): Membership` |
| [LeaveCommunity.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Actions/LeaveCommunity.php) | `public function handle(Profile $member, Community $community): void` |
| [ListCommunities.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Actions/ListCommunities.php) | `public function handle(Profile $viewer, int $limit = 25): Collection` |
| [CommunityAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Contracts/CommunityAuthorizer.php) | `public function create(Profile $owner): void`<br>`public function join(Profile $member): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Community.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Models/Community.php) | `id`, `owner_profile_id`, `name`, `slug`, `description`, `visibility`, `rules` |
| [Membership.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Models/Membership.php) | `community_id`, `profile_id`, `role`, `status` |
<!-- layer-implementation-plan:end -->
