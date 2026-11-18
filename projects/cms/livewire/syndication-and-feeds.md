# CMS: Syndication and Feeds Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#syndication-and-feeds). Observed identity: [`liberusoftware/module-cms-syndication-and-feeds-livewire`](../../../modules/source/liberusoftware--module-cms-syndication-and-feeds-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-syndication-and-feeds-livewire`  
**Matching domain module:** `cms-syndication-and-feeds`  
**Application:** CMS  
**Source feature:** [Syndication and Feeds](../features/syndication-and-feeds.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **RSS/Atom and structured feeds:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Outbound syndication:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Inbound feed imports:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Mappings:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Deduplication:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Attribution:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Schedules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-syndication-and-feeds-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-cms-syndication-and-feeds::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `rss-atom-and-structured-feeds`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `outbound-syndication`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `inbound-feed-imports`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `mappings`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `deduplication`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `attribution`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `schedules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-syndication-and-feeds` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/syndication-and-feeds.md) · [API plan](../api/syndication-and-feeds.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **RSS/Atom and structured feeds** | Expose a focused Livewire 4 component and namespaced Blade default view for `rss/atom and structured feeds` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Outbound syndication** | Expose a focused Livewire 4 component and namespaced Blade default view for `outbound syndication` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Inbound feed imports** | Expose a focused Livewire 4 component and namespaced Blade default view for `inbound feed imports` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Mappings** | Expose a focused Livewire 4 component and namespaced Blade default view for `mappings` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Deduplication** | Expose a focused Livewire 4 component and namespaced Blade default view for `deduplication` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Attribution** | Expose a focused Livewire 4 component and namespaced Blade default view for `attribution` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Schedules** | Expose a focused Livewire 4 component and namespaced Blade default view for `schedules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [FeedPreview.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-syndication-and-feeds-livewire/src/Livewire/FeedPreview.php) · [SyndicationAndFeedsLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-syndication-and-feeds-livewire/src/SyndicationAndFeedsLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [FeedService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-syndication-and-feeds/src/Services/FeedService.php) | `public function create(string $key, string $title, string $format = 'rss', ?string $sourceUrl = null, array $mapping = []): Feed`<br>`public function addItem(Feed $feed, array $item): FeedItem`<br>`public function update(Feed $feed, array $attributes): Feed`<br>`public function remove(Feed $feed): void`<br>`public function import(Feed $feed, string $xml): int`<br>`public function render(Feed $feed): string`<br>`public function syndicate(Feed $feed, string $destination): SyndicationDelivery` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Feed.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-syndication-and-feeds/src/Models/Feed.php) | `key`, `title`, `format`, `source_url`, `mapping`, `scheduled_at`, `active` |
| [FeedItem.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-syndication-and-feeds/src/Models/FeedItem.php) | `feed_id`, `external_id`, `title`, `url`, `summary`, `content`, `attribution`, `dedupe_hash`, `payload`, `published_at` |
| [SyndicationDelivery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-syndication-and-feeds/src/Models/SyndicationDelivery.php) | `feed_id`, `destination`, `status`, `response`, `delivered_at` |
<!-- layer-implementation-plan:end -->
