# CMS: CMS Core Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-core). Observed identity: [`liberusoftware/module-cms-core-filament`](../../../modules/source/liberusoftware--module-cms-core-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-core-filament`  
**Matching domain module:** `cms-core`  
**Application:** CMS  
**Source feature:** [CMS Core](../features/cms-core.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-core` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Sites:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Channels:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Content identity:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Aliases:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Ownership:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Shared terminology:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Settings:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Domain events:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-core-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `sites`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `channels`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `content-identity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `aliases`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ownership`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `shared-terminology`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `settings`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `domain-events`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-core` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-core-filament`](https://github.com/liberusoftware/module-cms-core-filament) (`liberusoftware/cms-core-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-core.md) · [API plan](../api/cms-core.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Sites** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sites`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Channels** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `channels`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Content identity** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `content identity`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Aliases** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `aliases`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Ownership** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ownership`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Shared terminology** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `shared terminology`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Settings** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `settings`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Domain events** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `domain events`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AuthorizesWithPermissions.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Filament/Concerns/AuthorizesWithPermissions.php) · [CoreFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-core-filament/src/CoreFilamentServiceProvider.php) · [ChannelResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-core-filament/src/Resources/ChannelResource.php) · [ListChannels.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-core-filament/src/Resources/Pages/ListChannels.php) · [ListSites.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-core-filament/src/Resources/Pages/ListSites.php) · [SiteResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-core-filament/src/Resources/SiteResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CoreQueryService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Queries/CoreQueryService.php) | `public function sites(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function site(string $key): ?Site`<br>`public function channels(string $siteKey, int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function alias(string $siteKey, string $alias): ?ContentAlias`<br>`public function aliases(string $siteKey, int $perPage = 15): LengthAwarePaginator`<br>`public function identities(string $siteKey, int $perPage = 15): LengthAwarePaginator`<br>`public function settings(string $siteKey, int $perPage = 15, string $environment = 'production'): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CoreMutationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Actions/CoreMutationService.php) | `public function createSite(array $attributes): Site`<br>`public function createChannel(Site\|int\|string $site, array $attributes): Channel`<br>`public function updateSite(Site $site, array $attributes): Site`<br>`public function updateChannel(Channel $channel, array $attributes): Channel`<br>`public function deleteSite(Site $site): void`<br>`public function deleteChannel(Channel $channel): void`<br>`public function createIdentity(Site\|int\|string $site, array $attributes): ContentIdentity`<br>`public function createAlias(Site\|int\|string $site, array $attributes): ContentAlias`<br>`public function putSetting(?Site $site, string $key, array $value, string $environment = 'production'): Setting` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Channel.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/Channel.php) | `site_id`, `key`, `name`, `type`, `settings`, `team_id` |
| [ContentAlias.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/ContentAlias.php) | `site_id`, `channel_id`, `alias`, `target_type`, `target_id`, `redirect_status`, `team_id` |
| [ContentIdentity.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/ContentIdentity.php) | `site_id`, `channel_id`, `content_type`, `content_id`, `canonical_path`, `status`, `owner_type`, `owner_id`, `metadata`, `team_id` |
| [Setting.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/Setting.php) | `site_id`, `key`, `value`, `environment` |
| [Site.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/Site.php) | `key`, `name`, `domain`, `default_locale`, `timezone`, `status`, `settings`, `team_id` |
<!-- layer-implementation-plan:end -->
