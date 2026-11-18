# CMS: Cms Integration Directory Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-integration-directory). Observed identity: [`liberusoftware/module-cms-integration-directory-filament`](../../../modules/source/liberusoftware--module-cms-integration-directory-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-cms-integration-directory-filament`  
**Matching domain module:** `cms-integration-directory`  
**Application:** CMS  
**Source feature:** [Cms Integration Directory](../features/cms-integration-directory.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-integration-directory` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Provider connections:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Capability discovery:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Credentials:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Configuration tests:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sync health:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Extension links:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-cms-integration-directory-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `provider-connections`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `capability-discovery`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `credentials`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `configuration-tests`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sync-health`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `extension-links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-integration-directory` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-integration-directory-filament`](https://github.com/liberusoftware/module-cms-integration-directory-filament) (`liberusoftware/cms-integration-directory-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-integration-directory.md) · [API plan](../api/cms-integration-directory.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Provider connections** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provider connections`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Capability discovery** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `capability discovery`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Credentials** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `credentials`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Configuration tests** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `configuration tests`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sync health** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sync health`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Extension links** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `extension links`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [IntegrationDirectoryFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-integration-directory-filament/src/IntegrationDirectoryFilamentServiceProvider.php) · [IntegrationResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-integration-directory-filament/src/Resources/IntegrationResource.php) · [ListIntegrations.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-integration-directory-filament/src/Resources/Pages/ListIntegrations.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [IntegrationDirectoryService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-integration-directory/src/Services/IntegrationDirectoryService.php) | `public function register(string $key, string $name, string $provider, array $configuration = [], ?int $teamId = null): Integration`<br>`public function enable(Integration $integration): Integration`<br>`public function disable(Integration $integration): Integration`<br>`public function health(Integration $integration, string $status, ?string $message = null): Integration`<br>`public function enabled(?string $category = null): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Integration.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-integration-directory/src/Models/Integration.php) | `key`, `name`, `provider`, `category`, `configuration`, `status`, `health_status`, `health_message`, `last_checked_at`, `team_id` |
<!-- layer-implementation-plan:end -->
