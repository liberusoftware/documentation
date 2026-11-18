# Social Network: Social Network Communities Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-communities). Observed identity: [`liberusoftware/module-social-network-communities-filament`](../../../modules/source/liberusoftware--module-social-network-communities-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-social-network-social-network-communities-filament`  
**Matching domain module:** `social-network-communities`  
**Application:** Social Network  
**Source feature:** [Social Network Communities](../features/social-network-communities.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `social-network-communities` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Groups/pages:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Memberships:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Roles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Feeds:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Files:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Questions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Moderation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-social-network-social-network-communities-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `groups-pages`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `memberships`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `roles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `feeds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `files`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `questions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `moderation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `social-network-communities` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-social-network-communities-filament`](https://github.com/liberusoftware/module-social-network-communities-filament) (`liberusoftware/social-network-communities-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/social-network-communities.md) · [API plan](../api/social-network-communities.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Groups/pages** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `groups/pages`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Memberships** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `memberships`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Roles** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `roles`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Feeds** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `feeds`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Files** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `files`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Questions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `questions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Moderation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `moderation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CommunitiesFilamentPlugin.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities-filament/src/CommunitiesFilamentPlugin.php) · [CommunitiesFilamentServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities-filament/src/CommunitiesFilamentServiceProvider.php) · [Communities.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities-filament/src/Pages/Communities.php).

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
