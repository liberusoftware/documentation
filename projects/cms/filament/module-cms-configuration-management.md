# CMS: Module Cms Configuration Management Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-configuration-management). Observed identity: [`liberusoftware/module-cms-configuration-management-filament`](../../../modules/source/liberusoftware--module-cms-configuration-management-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-module-cms-configuration-management-filament`  
**Matching domain module:** `module-cms-configuration-management`  
**Application:** CMS  
**Source feature:** [Module Cms Configuration Management](../features/module-cms-configuration-management.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-cms-configuration-management` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Exportable versioned CMS configuration:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Environment comparison:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dependency validation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Promotion:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Secrets exclusion:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rollback:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-module-cms-configuration-management-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `exportable-versioned-cms-configuration`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `environment-comparison`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dependency-validation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `promotion`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `secrets-exclusion`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rollback`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-cms-configuration-management` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-configuration-management-filament`](https://github.com/liberusoftware/module-cms-configuration-management-filament) (`liberusoftware/cms-configuration-management-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-cms-configuration-management.md) · [API plan](../api/module-cms-configuration-management.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Exportable versioned CMS configuration** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exportable versioned cms configuration`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Environment comparison** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `environment comparison`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dependency validation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dependency validation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Promotion** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `promotion`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Secrets exclusion** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `secrets exclusion`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rollback** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rollback`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ConfigurationManagementFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-configuration-management-filament/src/ConfigurationManagementFilamentServiceProvider.php) · [ConfigurationReleaseResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-configuration-management-filament/src/Resources/ConfigurationReleaseResource.php) · [ListConfigurationReleases.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-configuration-management-filament/src/Resources/Pages/ListConfigurationReleases.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfigurationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-configuration-management/src/Services/ConfigurationService.php) | `public function __construct(private DatabaseManager $db)`<br>`public function releases(?int $teamId, string $environment, int $perPage = 25): LengthAwarePaginator`<br>`public function export(array $payload, string $version, string $environment, ?int $actorId = null, ?int $teamId = null, array $dependencies = []): ConfigurationRelease`<br>`public function compare(ConfigurationRelease $from, ConfigurationRelease $to): array`<br>`public function validateDependencies(ConfigurationRelease $release, array $available): array`<br>`public function promote(ConfigurationRelease $release, array $available = []): ConfigurationRelease`<br>`public function rollback(ConfigurationRelease $release): ConfigurationRelease` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ConfigurationRelease.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-configuration-management/src/Models/ConfigurationRelease.php) | `team_id`, `version`, `environment`, `payload`, `dependencies`, `checksum`, `status`, `created_by`, `promoted_at`, `rolled_back_at` |
<!-- layer-implementation-plan:end -->
