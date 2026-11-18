# Social Network: Social Network Discovery Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-discovery). Observed identity: [`liberusoftware/module-social-network-discovery-filament`](../../../modules/source/liberusoftware--module-social-network-discovery-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-social-network-social-network-discovery-filament`  
**Matching domain module:** `social-network-discovery`  
**Application:** Social Network  
**Source feature:** [Social Network Discovery](../features/social-network-discovery.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `social-network-discovery` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Search:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Hashtags:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Trends:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recommendations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Directories:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Privacy-aware indexing:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-social-network-social-network-discovery-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `search`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `hashtags`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `trends`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recommendations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `directories`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `privacy-aware-indexing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `social-network-discovery` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-social-network-discovery-filament`](https://github.com/liberusoftware/module-social-network-discovery-filament) (`liberusoftware/social-network-discovery-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/social-network-discovery.md) · [API plan](../api/social-network-discovery.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Search** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `search`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Hashtags** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `hashtags`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Trends** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `trends`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recommendations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recommendations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Directories** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `directories`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Privacy-aware indexing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `privacy-aware indexing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [DiscoveryFilamentPlugin.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery-filament/src/DiscoveryFilamentPlugin.php) · [DiscoveryFilamentServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery-filament/src/DiscoveryFilamentServiceProvider.php) · [Search.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-discovery-filament/src/Pages/Search.php).

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
