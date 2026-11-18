# CMS: Theme Marketplace Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#theme-marketplace). Observed identity: [`liberusoftware/module-cms-theme-marketplace-filament`](../../../modules/source/liberusoftware--module-cms-theme-marketplace-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-theme-marketplace-filament`  
**Matching domain module:** `cms-theme-marketplace`  
**Application:** CMS  
**Source feature:** [Theme Marketplace](../features/theme-marketplace.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-theme-marketplace` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Theme manifests:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Compatibility:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Previews:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Licenses:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Child themes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Installation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Updates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Security review:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Ratings:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-theme-marketplace-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `theme-manifests`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `compatibility`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `previews`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `licenses`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `child-themes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `installation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `updates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `security-review`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ratings`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-theme-marketplace` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-theme-marketplace-filament`](https://github.com/liberusoftware/module-cms-theme-marketplace-filament) (`liberusoftware/cms-theme-marketplace-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/theme-marketplace.md) · [API plan](../api/theme-marketplace.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Theme manifests** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `theme manifests`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Compatibility** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `compatibility`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Previews** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `previews`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Licenses** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `licenses`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Child themes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `child themes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Installation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `installation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Updates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `updates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Security review** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `security review`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Ratings** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ratings`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [MarketplaceThemeResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-theme-marketplace-filament/src/Resources/MarketplaceThemeResource.php) · [ListMarketplaceThemes.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-theme-marketplace-filament/src/Resources/Pages/ListMarketplaceThemes.php) · [ThemeMarketplaceFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-theme-marketplace-filament/src/ThemeMarketplaceFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ThemeMarketplaceQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-marketplace/src/Queries/ThemeMarketplaceQuery.php) | `public function catalog(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function find(string $key, ?string $version = null): ?MarketplaceTheme`<br>`public function installation(string $siteKey, string $themeKey): ?ThemeInstallation` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ThemeMarketplaceService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-marketplace/src/Services/ThemeMarketplaceService.php) | `public function publish(array $manifest, ?int $teamId = null): MarketplaceTheme`<br>`public function reviewSecurity(MarketplaceTheme $theme, string $status): MarketplaceTheme`<br>`public function compatible(MarketplaceTheme $theme, string $cmsVersion, array $features = []): bool`<br>`public function install(MarketplaceTheme $theme, string $siteKey, string $cmsVersion, array $features = [], ?int $teamId = null): ThemeInstallation`<br>`public function update(ThemeInstallation $installation, MarketplaceTheme $theme, string $cmsVersion, array $features = []): ThemeInstallation`<br>`public function rate(MarketplaceTheme $theme, string $reviewerType, int\|string $reviewerId, int $rating, ?string $review = null, ?int $teamId = null): ThemeRating`<br>`public function ratingSummary(MarketplaceTheme $theme): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MarketplaceTheme.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-marketplace/src/Models/MarketplaceTheme.php) | `key`, `name`, `version`, `author`, `description`, `manifest`, `compatibility`, `preview_url`, `license`, `parent_key`, `status`, `security_status`, `team_id` |
| [ThemeInstallation.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-marketplace/src/Models/ThemeInstallation.php) | `theme_id`, `site_key`, `installed_version`, `status`, `installed_at`, `updated_at_version`, `team_id` |
| [ThemeRating.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-marketplace/src/Models/ThemeRating.php) | `theme_id`, `reviewer_type`, `reviewer_id`, `rating`, `review`, `team_id` |
<!-- layer-implementation-plan:end -->
