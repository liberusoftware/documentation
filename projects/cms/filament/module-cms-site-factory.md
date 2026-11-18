# CMS: Module Cms Site Factory Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-site-factory). Observed identity: [`liberusoftware/module-cms-site-factory-filament`](../../../modules/source/liberusoftware--module-cms-site-factory-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-module-cms-site-factory-filament`  
**Matching domain module:** `module-cms-site-factory`  
**Application:** CMS  
**Source feature:** [Module Cms Site Factory](../features/module-cms-site-factory.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-cms-site-factory` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Site templates/recipes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Provisioning:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Domain verification:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Initial content/configuration:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cloning:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Suspension:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Archival:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Teardown:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-module-cms-site-factory-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `site-templates-recipes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `provisioning`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `domain-verification`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `initial-content-configuration`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cloning`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `suspension`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `archival`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `teardown`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-cms-site-factory` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-site-factory-filament`](https://github.com/liberusoftware/module-cms-site-factory-filament) (`liberusoftware/cms-site-factory-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-cms-site-factory.md) · [API plan](../api/module-cms-site-factory.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Site templates/recipes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `site templates/recipes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Provisioning** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provisioning`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Domain verification** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `domain verification`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Initial content/configuration** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `initial content/configuration`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cloning** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cloning`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Suspension** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `suspension`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Archival** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `archival`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Teardown** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `teardown`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListSiteTemplates.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-site-factory-filament/src/Resources/Pages/ListSiteTemplates.php) · [SiteTemplateResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-site-factory-filament/src/Resources/SiteTemplateResource.php) · [SiteFactoryFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-site-factory-filament/src/SiteFactoryFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SiteFactoryService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-site-factory/src/Services/SiteFactoryService.php) | `public function templates(): Collection`<br>`public function template(string $key, string $name, array $configuration = [], array $initialContent = [], ?int $teamId = null): SiteTemplate`<br>`public function updateTemplate(SiteTemplate $template, string $name, array $configuration, array $initialContent): SiteTemplate`<br>`public function activateTemplate(SiteTemplate $template): SiteTemplate`<br>`public function deactivateTemplate(SiteTemplate $template): SiteTemplate`<br>`public function provision(string $key, string $name, ?string $templateKey = null, ?string $domain = null, ?int $teamId = null): Site`<br>`public function addDomain(Site $site, string $domain): SiteDomain`<br>`public function verifyDomain(SiteDomain $domain, string $token): SiteDomain`<br>`public function clone(Site $source, string $key, string $name): Site`<br>`public function suspend(Site $site): Site`<br>`public function archive(Site $site): Site`<br>`public function transition(Site $site, string $status): Site`<br>`public function teardown(Site $site, bool $confirm = false): void`<br>`public function operations(?Site $site = null): Collection` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SiteDomain.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-site-factory/src/Models/SiteDomain.php) | `site_id`, `domain`, `verification_token`, `verified_at`, `team_id` |
| [SiteFactoryOperation.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-site-factory/src/Models/SiteFactoryOperation.php) | `site_id`, `team_id`, `operation`, `status`, `payload`, `error`, `completed_at` |
| [SiteTemplate.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-site-factory/src/Models/SiteTemplate.php) | `key`, `name`, `configuration`, `initial_content`, `active`, `team_id` |
<!-- layer-implementation-plan:end -->
