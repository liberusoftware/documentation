# CMS: Module Cms Offline And Pwa Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-offline-and-pwa). Observed identity: [`liberusoftware/module-cms-offline-and-pwa-filament`](../../../modules/source/liberusoftware--module-cms-offline-and-pwa-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-module-cms-offline-and-pwa-filament`  
**Matching domain module:** `module-cms-offline-and-pwa`  
**Application:** CMS  
**Source feature:** [Module Cms Offline And Pwa](../features/module-cms-offline-and-pwa.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-cms-offline-and-pwa` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Manifest/service-worker integration points:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Content caching policy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Offline pages:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Update behavior:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Install metadata:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-module-cms-offline-and-pwa-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `manifest-service-worker-integration-points`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `content-caching-policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `offline-pages`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `update-behavior`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `install-metadata`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-cms-offline-and-pwa` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-offline-and-pwa-filament`](https://github.com/liberusoftware/module-cms-offline-and-pwa-filament) (`liberusoftware/cms-offline-and-pwa-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-cms-offline-and-pwa.md) · [API plan](../api/module-cms-offline-and-pwa.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Manifest/service-worker integration points** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `manifest/service-worker integration points`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Content caching policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `content caching policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Offline pages** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `offline pages`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Update behavior** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `update behavior`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Install metadata** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `install metadata`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [OfflineAndPwaFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-offline-and-pwa-filament/src/OfflineAndPwaFilamentServiceProvider.php) · [ListPwaConfigurations.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-offline-and-pwa-filament/src/Resources/Pages/ListPwaConfigurations.php) · [PwaConfigurationResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-offline-and-pwa-filament/src/Resources/PwaConfigurationResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [OfflineAndPwaService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-offline-and-pwa/src/Services/OfflineAndPwaService.php) | `public function configure(string $siteKey, string $name, string $shortName, ?int $teamId = null, array $attributes = []): PwaConfiguration`<br>`public function update(PwaConfiguration $configuration, array $attributes): PwaConfiguration`<br>`public function setCachePolicy(PwaConfiguration $configuration, array $policy): PwaConfiguration`<br>`public function publishUpdate(PwaConfiguration $configuration, ?string $version = null): PwaConfiguration`<br>`public function manifest(PwaConfiguration $configuration): array`<br>`public function serviceWorker(PwaConfiguration $configuration): string` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PwaConfiguration.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-offline-and-pwa/src/Models/PwaConfiguration.php) | `site_key`, `name`, `short_name`, `start_url`, `scope`, `display`, `theme_color`, `background_color`, `icon_url`, `offline_url`, `cache_policy`, `service_worker_version`, `last_updated_at`, `team_id` |
<!-- layer-implementation-plan:end -->
