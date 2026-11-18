# Genealogy: Genealogy Discovery Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-discovery). Observed identity: [`liberusoftware/module-genealogy-discovery-filament`](../../../modules/source/liberusoftware--module-genealogy-discovery-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-genealogy-genealogy-discovery-filament`  
**Matching domain module:** `genealogy-discovery`  
**Application:** Genealogy  
**Source feature:** [Genealogy Discovery](../features/genealogy-discovery.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `genealogy-discovery` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Person/place/source search:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Hints:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Duplicates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Relationship paths:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Privacy-aware indexes:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-genealogy-genealogy-discovery-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `person-place-source-search`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `hints`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `duplicates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `relationship-paths`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `privacy-aware-indexes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `genealogy-discovery` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-genealogy-discovery-filament`](https://github.com/liberusoftware/module-genealogy-discovery-filament) (`liberusoftware/genealogy-discovery-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/genealogy-discovery.md) · [API plan](../api/genealogy-discovery.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Person/place/source search** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `person/place/source search`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Hints** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `hints`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Duplicates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `duplicates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Relationship paths** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `relationship paths`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Privacy-aware indexes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `privacy-aware indexes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [DiscoveryFilamentServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery-filament/src/DiscoveryFilamentServiceProvider.php) · [DiscoveryMatchResource.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery-filament/src/Resources/DiscoveryMatchResource.php) · [CreateDiscoveryMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery-filament/src/Resources/DiscoveryMatchResource/Pages/CreateDiscoveryMatch.php) · [EditDiscoveryMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery-filament/src/Resources/DiscoveryMatchResource/Pages/EditDiscoveryMatch.php) · [ListDiscoveryMatchs.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery-filament/src/Resources/DiscoveryMatchResource/Pages/ListDiscoveryMatchs.php).

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
