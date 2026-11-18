# CMS: Cms Recommendations Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-recommendations). Observed identity: [`liberusoftware/module-cms-recommendations-livewire`](../../../modules/source/liberusoftware--module-cms-recommendations-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-cms-recommendations-livewire`  
**Matching domain module:** `cms-recommendations`  
**Application:** CMS  
**Source feature:** [Cms Recommendations](../features/cms-recommendations.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Popular/latest/related/trending/editorial lists:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Pluggable ranking:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Audience context:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Exclusions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Explanation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-cms-recommendations-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsCmsRecommendations::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `popular-latest-related-trending-editorial-lists`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `pluggable-ranking`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `audience-context`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `exclusions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `explanation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-recommendations` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/cms-recommendations.md) · [API plan](../api/cms-recommendations.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Popular/latest/related/trending/editorial lists** | Expose a focused Livewire 4 component and namespaced Blade default view for `popular/latest/related/trending/editorial lists` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Pluggable ranking** | Expose a focused Livewire 4 component and namespaced Blade default view for `pluggable ranking` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Audience context** | Expose a focused Livewire 4 component and namespaced Blade default view for `audience context` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Exclusions** | Expose a focused Livewire 4 component and namespaced Blade default view for `exclusions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Explanation** | Expose a focused Livewire 4 component and namespaced Blade default view for `explanation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [RecommendationList.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-recommendations-livewire/src/Livewire/RecommendationList.php) · [RecommendationsLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-recommendations-livewire/src/RecommendationsLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [Ranker.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-recommendations/src/Contracts/Ranker.php) | `public function score(iterable $items, array $context = []): array` |
| [DefaultRanker.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-recommendations/src/Services/DefaultRanker.php) | `public function score(iterable $items, array $context = []): array` |
| [RecommendationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-recommendations/src/Services/RecommendationService.php) | `public function createList(string $key, string $name, string $kind = 'latest', array $audienceRules = [], array $exclusions = [], ?int $teamId = null): RecommendationList`<br>`public function addItem(RecommendationList $list, array $attributes): RecommendationItem`<br>`public function updateList(RecommendationList $list, array $attributes): RecommendationList`<br>`public function removeList(RecommendationList $list): RecommendationList`<br>`public function exclude(RecommendationList $list, string $itemKey): RecommendationList`<br>`public function recommend(string $listKey, array $context = [], ?string $excludeKey = null, int $limit = 10): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RecommendationItem.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-recommendations/src/Models/RecommendationItem.php) | `list_id`, `item_type`, `item_key`, `title`, `summary`, `context`, `popularity_score`, `editorial_score`, `published_at`, `position` |
| [RecommendationList.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-recommendations/src/Models/RecommendationList.php) | `name`, `key`, `kind`, `ranker`, `audience_rules`, `exclusions`, `active`, `team_id` |
<!-- layer-implementation-plan:end -->
