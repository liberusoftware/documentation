# Genealogy: Discovery Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#discovery). Observed identity: [`liberusoftware/module-genealogy-discovery-livewire`](../../../modules/source/liberusoftware--module-genealogy-discovery-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-genealogy-discovery-livewire`  
**Matching domain module:** `genealogy-discovery`  
**Application:** Genealogy  
**Source feature:** [Discovery](../features/discovery.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Person/place/source search:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Hints:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Duplicates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Relationship paths:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Privacy-aware indexes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-genealogy-discovery-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-genealogy-discovery::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `person-place-source-search`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `hints`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `duplicates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `relationship-paths`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `privacy-aware-indexes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `genealogy-discovery` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/discovery.md) · [API plan](../api/discovery.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Person/place/source search** | Expose a focused Livewire 4 component and namespaced Blade default view for `person/place/source search` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Hints** | Expose a focused Livewire 4 component and namespaced Blade default view for `hints` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Duplicates** | Expose a focused Livewire 4 component and namespaced Blade default view for `duplicates` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Relationship paths** | Expose a focused Livewire 4 component and namespaced Blade default view for `relationship paths` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Privacy-aware indexes** | Expose a focused Livewire 4 component and namespaced Blade default view for `privacy-aware indexes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [DiscoveryLivewireServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery-livewire/src/DiscoveryLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [DiscoverySearch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Queries/DiscoverySearch.php) | `public function execute(string $term, array $options = []): array` |
| [DuplicateCandidates.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Queries/DuplicateCandidates.php) | `public function execute(int $limit = 100, int $minimumConfidence = 70): array` |
| [RelationshipPath.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Queries/RelationshipPath.php) | `public function execute(string $from, string $to, int $maxDepth = 6, bool $publicOnly = false): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDiscoveryMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Actions/CreateDiscoveryMatch.php) | `public function execute(array $attributes): DiscoveryMatch` |
| [DeleteDiscoveryMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Actions/DeleteDiscoveryMatch.php) | `public function execute(DiscoveryMatch $match): void` |
| [ReviewDiscoveryMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Actions/ReviewDiscoveryMatch.php) | `public function execute(DiscoveryMatch $match, string $status): DiscoveryMatch` |
| [ScanDuplicateCandidates.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Actions/ScanDuplicateCandidates.php) | `public function __construct( private readonly DuplicateCandidates $candidates, private readonly CreateDiscoveryMatch $create, )`<br>`public function execute(float $threshold = 0.7, int $limit = 100): array` |
| [UpdateDiscoveryMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Actions/UpdateDiscoveryMatch.php) | `public function execute(DiscoveryMatch $match, array $attributes): DiscoveryMatch` |
| [ExternalRecordProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Contracts/ExternalRecordProvider.php) | `public function key(): string`<br>`public function isAvailable(): bool`<br>`public function search(array $person): array` |
| [ExternalRecordMatcher.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Services/ExternalRecordMatcher.php) | `public function __construct(private readonly ?ExternalRecordProvider $provider = null)`<br>`public function execute(array $person, array $weights = []): array`<br>`public function scoreCandidates(array $person, array $candidates, array $weights = []): array` |
| [SmartMatchingService.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Services/SmartMatchingService.php) | `public function findMatches(Person $person, iterable $providers, int $minimumConfidence = 60, int $limit = 10): array`<br>`public function persist(Model $user, Person $person, array $matches): Collection` |
| [SocialFamilyDiscovery.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Services/SocialFamilyDiscovery.php) | `public function enable(ConnectedAccount $account): bool`<br>`public function disable(ConnectedAccount $account): bool`<br>`public function sync(ConnectedAccount $account): bool`<br>`public function privacy(int\|string $userId): SocialConnectionPrivacy`<br>`public function updatePrivacy(int\|string $userId, array $settings): SocialConnectionPrivacy`<br>`public function needsSync(ConnectedAccount $account): bool`<br>`public function findPotentialConnections(Model $user): Collection`<br>`public function processMatches(Model $user): int` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DiscoveryMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Models/DiscoveryMatch.php) | `team_id`, `kind`, `name`, `subject_id`, `related_id`, `confidence`, `rationale`, `source_type`, `detected_at`, `reviewed_at`, `status`, `metadata` |
| [SmartMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Models/SmartMatch.php) | `team_id`, `user_id`, `person_id`, `external_tree_id`, `external_person_id`, `match_source`, `record_category`, `match_data`, `search_criteria`, `confidence_score`, `status`, `reviewed_at` |
| [SocialConnectionPrivacy.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Models/SocialConnectionPrivacy.php) | `user_id`, `allow_family_discovery`, `show_profile_to_matches`, `share_tree_with_matches`, `allow_contact_from_matches`, `blocked_users` |
| [SocialFamilyConnection.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Models/SocialFamilyConnection.php) | `user_id`, `connected_account_id`, `matched_social_id`, `matched_name`, `matched_email`, `relationship_type`, `confidence_score`, `matching_criteria`, `status` |
<!-- layer-implementation-plan:end -->
