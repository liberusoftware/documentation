# CMS: Sitemaps Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sitemaps). Observed identity: [`liberusoftware/module-cms-sitemaps-filament`](../../../modules/source/liberusoftware--module-cms-sitemaps-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-sitemaps-filament`  
**Matching domain module:** `cms-sitemaps`  
**Application:** CMS  
**Source feature:** [Sitemaps](../features/sitemaps.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-sitemaps` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Site/type/locale-aware indexes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Exclusions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Images/video/news extensions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Chunking:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cache:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Search-engine notification adapters:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-sitemaps-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `site-type-locale-aware-indexes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `exclusions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `images-video-news-extensions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `chunking`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cache`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `search-engine-notification-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-sitemaps` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-sitemaps-filament`](https://github.com/liberusoftware/module-cms-sitemaps-filament) (`liberusoftware/cms-sitemaps-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/sitemaps.md) · [API plan](../api/sitemaps.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Site/type/locale-aware indexes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `site/type/locale-aware indexes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Exclusions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exclusions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Images/video/news extensions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `images/video/news extensions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Chunking** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `chunking`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cache** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cache`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Search-engine notification adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `search-engine notification adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListSitemapEntries.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-sitemaps-filament/src/Resources/Pages/ListSitemapEntries.php) · [SitemapEntryResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-sitemaps-filament/src/Resources/SitemapEntryResource.php) · [SitemapsFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-sitemaps-filament/src/SitemapsFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SitemapService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-sitemaps/src/Services/SitemapService.php) | `public function __construct(private readonly TenantContextInterface $tenant)`<br>`public function add(string $url, ?int $siteId = null, string $type = 'web', ?string $locale = null, float $priority = .5, array $extensions = [], ?int $teamId = null): SitemapEntry`<br>`public function exclude(string $url, ?int $siteId = null): int`<br>`public function update(SitemapEntry $entry, array $attributes): SitemapEntry`<br>`public function remove(SitemapEntry $entry): void`<br>`public function entries(?int $siteId = null, ?string $type = null, ?string $locale = null): array`<br>`public function chunks(?int $siteId = null, int $size = 50000, ?string $type = null, ?string $locale = null): array`<br>`public function notify(string $engine, ?int $siteId = null): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SitemapEntry.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-sitemaps/src/Models/SitemapEntry.php) | `site_id`, `type`, `locale`, `url`, `last_modified`, `priority`, `change_frequency`, `images`, `video`, `news`, `excluded`, `team_id` |
<!-- layer-implementation-plan:end -->
