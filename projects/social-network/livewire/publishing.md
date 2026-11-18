# Social Network: Publishing Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#publishing). Observed identity: [`liberusoftware/module-social-network-publishing-livewire`](../../../modules/source/liberusoftware--module-social-network-publishing-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-social-network-publishing-livewire`  
**Matching domain module:** `social-network-publishing`  
**Application:** Social Network  
**Source feature:** [Publishing](../features/publishing.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Posts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Articles:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Drafts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Audiences:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Edits:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Mentions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Hashtags:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Polls:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Links:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Schedules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-social-network-publishing-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-social-network-publishing::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `posts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `articles`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `drafts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `audiences`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `edits`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `mentions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `hashtags`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `polls`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `links`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `schedules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `social-network-publishing` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/publishing.md) · [API plan](../api/publishing.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Posts** | Expose a focused Livewire 4 component and namespaced Blade default view for `posts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Articles** | Expose a focused Livewire 4 component and namespaced Blade default view for `articles` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Drafts** | Expose a focused Livewire 4 component and namespaced Blade default view for `drafts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Audiences** | Expose a focused Livewire 4 component and namespaced Blade default view for `audiences` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Edits** | Expose a focused Livewire 4 component and namespaced Blade default view for `edits` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Mentions** | Expose a focused Livewire 4 component and namespaced Blade default view for `mentions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Hashtags** | Expose a focused Livewire 4 component and namespaced Blade default view for `hashtags` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Polls** | Expose a focused Livewire 4 component and namespaced Blade default view for `polls` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Links** | Expose a focused Livewire 4 component and namespaced Blade default view for `links` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Schedules** | Expose a focused Livewire 4 component and namespaced Blade default view for `schedules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Articles.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing-livewire/src/Components/Articles.php) · [Audiences.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing-livewire/src/Components/Audiences.php) · [Composer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing-livewire/src/Components/Composer.php) · [Drafts.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing-livewire/src/Components/Drafts.php) · [Edits.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing-livewire/src/Components/Edits.php) · [Hashtags.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing-livewire/src/Components/Hashtags.php) · [Links.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing-livewire/src/Components/Links.php) · [Mentions.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing-livewire/src/Components/Mentions.php) · [Polls.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing-livewire/src/Components/Polls.php) · [Posts.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing-livewire/src/Components/Posts.php) · [Schedules.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing-livewire/src/Components/Schedules.php) · [PublishingLivewireServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing-livewire/src/PublishingLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePublication.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/CreatePublication.php) | `public function __construct(private PublishingAuthorizer $authorizer)`<br>`public function handle(Profile $author, array $attributes): Publication` |
| [DeletePublication.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/DeletePublication.php) | `public function __construct(private PublishingAuthorizer $authorizer)`<br>`public function handle(Profile $author, Publication $publication): void` |
| [ListPublications.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/ListPublications.php) | `public function handle(Profile $viewer, int $limit = 25): Collection` |
| [PublishPublication.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/PublishPublication.php) | `public function __construct(private PublishingAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $author, Publication $publication): Publication` |
| [PublishScheduledPublications.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/PublishScheduledPublications.php) | `public function __construct(private Dispatcher $events)`<br>`public function handle(?Carbon $now = null, int $limit = 100): int` |
| [UpdatePublication.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/UpdatePublication.php) | `public function __construct(private PublishingAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $author, Publication $publication, array $attributes): Publication` |
| [UpdatePublicationEnrichments.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/UpdatePublicationEnrichments.php) | `public function __construct(private PublishingAuthorizer $authorizer)`<br>`public function handle(Profile $author, Publication $publication, array $data): Publication` |
| [PublishingAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Contracts/PublishingAuthorizer.php) | `public function create(Profile $author): void`<br>`public function update(Profile $author, Publication $publication): void`<br>`public function publish(Profile $author, Publication $publication): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Publication.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Models/Publication.php) | `id`, `author_profile_id`, `kind`, `state`, `audience`, `title`, `body`, `metadata`, `scheduled_at`, `published_at` |
<!-- layer-implementation-plan:end -->
