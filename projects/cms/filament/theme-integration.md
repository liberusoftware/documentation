# CMS: Theme Integration Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#theme-integration). Observed identity: [`liberusoftware/module-cms-theme-integration-filament`](../../../modules/source/liberusoftware--module-cms-theme-integration-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-theme-integration-filament`  
**Matching domain module:** `cms-theme-integration`  
**Application:** CMS  
**Source feature:** [Theme Integration](../features/theme-integration.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-theme-integration` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Theme selection by site/channel:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Regions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **View contracts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Component registry:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Inheritance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Preview:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Safe fallback:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-theme-integration-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `theme-selection-by-site-channel`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `regions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `view-contracts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `component-registry`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `inheritance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `preview`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `safe-fallback`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-theme-integration` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-theme-integration-filament`](https://github.com/liberusoftware/module-cms-theme-integration-filament) (`liberusoftware/cms-theme-integration-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/theme-integration.md) · [API plan](../api/theme-integration.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Theme selection by site/channel** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `theme selection by site/channel`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Regions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `regions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **View contracts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `view contracts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Component registry** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `component registry`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Inheritance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `inheritance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Preview** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `preview`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Safe fallback** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `safe fallback`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListThemeBindings.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-theme-integration-filament/src/Resources/Pages/ListThemeBindings.php) · [ThemeBindingResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-theme-integration-filament/src/Resources/ThemeBindingResource.php) · [ThemeIntegrationFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-theme-integration-filament/src/ThemeIntegrationFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ThemeIntegrationQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-integration/src/Queries/ThemeIntegrationQuery.php) | `public function __construct(private TenantContextInterface $tenant)`<br>`public function bindings(int $perPage = 15, ?int $teamId = null): LengthAwarePaginator`<br>`public function binding(string $siteKey, ?string $channelKey = null, ?int $teamId = null): ?ThemeBinding`<br>`public function bindingById(int\|string $id, ?int $teamId = null): ?ThemeBinding`<br>`public function components(string $themeKey, ?string $region = null, ?int $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ThemeIntegrationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-integration/src/Services/ThemeIntegrationService.php) | `public function __construct(private ThemeIntegrationQuery $query)`<br>`public function bind(string $siteKey, ?string $channelKey, string $themeKey, string $fallbackThemeKey = 'default', ?int $teamId = null): ThemeBinding`<br>`public function updateBinding(ThemeBinding $binding, array $attributes): ThemeBinding`<br>`public function removeBinding(ThemeBinding $binding): void`<br>`public function select(?string $siteKey, ?string $channelKey = null, ?int $teamId = null): ?ThemeBinding`<br>`public function effectiveTheme(?string $siteKey, ?string $channelKey = null, ?int $teamId = null): string`<br>`public function registerComponent(string $themeKey, string $region, string $componentKey, array $viewContract = [], array $configuration = [], ?int $teamId = null): ThemeComponent`<br>`public function components(string $themeKey, ?string $region = null, ?int $teamId = null): array`<br>`public function previewToken(ThemeBinding $binding): string`<br>`public function preview(ThemeBinding $binding, string $token): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ThemeBinding.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-integration/src/Models/ThemeBinding.php) | `site_key`, `channel_key`, `theme_key`, `fallback_theme_key`, `preview_token`, `preview_expires_at`, `active`, `team_id` |
| [ThemeComponent.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-integration/src/Models/ThemeComponent.php) | `theme_key`, `region`, `component_key`, `view_contract`, `configuration`, `team_id` |
<!-- layer-implementation-plan:end -->
