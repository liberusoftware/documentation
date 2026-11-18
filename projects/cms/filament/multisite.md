# CMS: Multisite Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#multisite). Observed identity: [`liberusoftware/module-cms-multisite-filament`](../../../modules/source/liberusoftware--module-cms-multisite-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-multisite-filament`  
**Matching domain module:** `cms-multisite`  
**Application:** CMS  
**Source feature:** [Multisite](../features/multisite.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-multisite` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Site network:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Shared/isolated content:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Domains:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Site admins:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Quotas:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Site lifecycle:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Network operations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Safe cross-site references:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-multisite-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `site-network`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `shared-isolated-content`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `domains`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `site-admins`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `quotas`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `site-lifecycle`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `network-operations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `safe-cross-site-references`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-multisite` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-multisite-filament`](https://github.com/liberusoftware/module-cms-multisite-filament) (`liberusoftware/cms-multisite-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/multisite.md) · [API plan](../api/multisite.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Site network** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `site network`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Shared/isolated content** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `shared/isolated content`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Domains** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `domains`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Site admins** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `site admins`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Quotas** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `quotas`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Site lifecycle** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `site lifecycle`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Network operations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `network operations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Safe cross-site references** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `safe cross-site references`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [MultisiteFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-multisite-filament/src/MultisiteFilamentServiceProvider.php) · [MultisiteSiteResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-multisite-filament/src/Resources/MultisiteSiteResource.php) · [ListSites.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-multisite-filament/src/Resources/MultisiteSiteResource/Pages/ListSites.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [MultisiteService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-multisite/src/Services/MultisiteService.php) | `public function __construct(private SiteFactoryService $factory)`<br>`public function createSite(string $key, string $name, ?string $domain = null, ?int $teamId = null): Site`<br>`public function transition(Site $site, string $status): Site`<br>`public function setQuota(Site $site, array $limits): SiteQuota`<br>`public function recordUsage(SiteQuota $quota, array $delta): SiteQuota`<br>`public function assignAdmin(Site $site, int $userId, string $role = 'editor'): SiteAdmin`<br>`public function removeAdmin(SiteAdmin $admin): void`<br>`public function reference(Site $source, Site $target, string $contentType, string $contentId, string $mode = 'shared'): SiteReference`<br>`public function networkTransition(array $siteIds, string $status): int` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SiteAdmin.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-multisite/src/Models/SiteAdmin.php) | `site_id`, `user_id`, `role`, `active`, `team_id` |
| [SiteQuota.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-multisite/src/Models/SiteQuota.php) | `site_id`, `limits`, `usage`, `team_id` |
| [SiteReference.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-multisite/src/Models/SiteReference.php) | `source_site_id`, `target_site_id`, `content_type`, `content_id`, `mode`, `status`, `team_id` |
<!-- layer-implementation-plan:end -->
