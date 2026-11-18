# Social Network: Social Network Feed Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-feed). Observed identity: [`liberusoftware/module-social-network-feed-livewire`](../../../modules/source/liberusoftware--module-social-network-feed-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-social-network-social-network-feed-livewire`  
**Matching domain module:** `social-network-feed`  
**Application:** Social Network  
**Source feature:** [Social Network Feed](../features/social-network-feed.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Candidate generation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Ranking:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Chronological mode:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Filters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Pagination:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Explanations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Controls:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-social-network-social-network-feed-livewire` component namespace and service provider; use explicit aliases such as `<livewire:socialnetworkSocialNetworkFeed::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `candidate-generation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `ranking`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `chronological-mode`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `filters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `pagination`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `explanations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `controls`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `social-network-feed` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/social-network-feed.md) · [API plan](../api/social-network-feed.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Candidate generation** | Expose a focused Livewire 4 component and namespaced Blade default view for `candidate generation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Ranking** | Expose a focused Livewire 4 component and namespaced Blade default view for `ranking` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Chronological mode** | Expose a focused Livewire 4 component and namespaced Blade default view for `chronological mode` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Filters** | Expose a focused Livewire 4 component and namespaced Blade default view for `filters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Pagination** | Expose a focused Livewire 4 component and namespaced Blade default view for `pagination` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Explanations** | Expose a focused Livewire 4 component and namespaced Blade default view for `explanations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Controls** | Expose a focused Livewire 4 component and namespaced Blade default view for `controls` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Timeline.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-feed-livewire/src/Components/Timeline.php) · [FeedLivewireServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-feed-livewire/src/FeedLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddFeedEntry.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-feed/src/Actions/AddFeedEntry.php) | `public function __construct(private Dispatcher $events, private FeedAuthorizer $authorizer)`<br>`public function handle(Profile $viewer, string $itemType, string $itemId, float $rank = 0): FeedEntry` |
| [GetFeed.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-feed/src/Actions/GetFeed.php) | `public function __construct(private FeedAuthorizer $authorizer)`<br>`public function handle(Profile $viewer, int $limit = 20, ?string $after = null): Collection` |
| [UpdateFeedControls.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-feed/src/Actions/UpdateFeedControls.php) | `public function __construct(private FeedAuthorizer $authorizer)`<br>`public function handle(Profile $profile, array $data): array` |
| [FeedAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-feed/src/Contracts/FeedAuthorizer.php) | `public function view(Profile $viewer): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FeedEntry.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-feed/src/Models/FeedEntry.php) | `id`, `viewer_profile_id`, `item_type`, `item_id`, `rank`, `visible_at` |
<!-- layer-implementation-plan:end -->
