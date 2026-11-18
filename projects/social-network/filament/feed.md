# Social Network: Feed Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#feed). Observed identity: [`liberusoftware/module-social-network-feed-filament`](../../../modules/source/liberusoftware--module-social-network-feed-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-social-network-feed-filament`  
**Matching domain module:** `social-network-feed`  
**Application:** Social Network  
**Source feature:** [Feed](../features/feed.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `social-network-feed` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Candidate generation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Ranking:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Chronological mode:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Filters:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Pagination:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Explanations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Controls:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-social-network-feed-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `candidate-generation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ranking`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `chronological-mode`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `filters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `pagination`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `explanations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `controls`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `social-network-feed` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-social-network-feed-filament`](https://github.com/liberusoftware/module-social-network-feed-filament) (`liberusoftware/social-network-feed-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/feed.md) · [API plan](../api/feed.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Candidate generation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `candidate generation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Ranking** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ranking`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Chronological mode** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `chronological mode`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Filters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `filters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Pagination** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `pagination`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Explanations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `explanations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Controls** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `controls`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [FeedFilamentPlugin.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-feed-filament/src/FeedFilamentPlugin.php) · [FeedFilamentServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-feed-filament/src/FeedFilamentServiceProvider.php) · [Entries.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-feed-filament/src/Pages/Entries.php).

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
