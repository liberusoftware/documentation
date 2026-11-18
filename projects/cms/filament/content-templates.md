# CMS: Content Templates Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#content-templates). Observed identity: [`liberusoftware/module-cms-content-templates-filament`](../../../modules/source/liberusoftware--module-cms-content-templates-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-content-templates-filament`  
**Matching domain module:** `cms-content-templates`  
**Application:** CMS  
**Source feature:** [Content Templates](../features/content-templates.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-content-templates` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Starter content:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Presets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Default fields/blocks/layouts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Template locking:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Versioning:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Controlled rollout:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-content-templates-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `starter-content`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `presets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `default-fields-blocks-layouts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `template-locking`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `versioning`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `controlled-rollout`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-content-templates` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-content-templates-filament`](https://github.com/liberusoftware/module-cms-content-templates-filament) (`liberusoftware/cms-content-templates-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/content-templates.md) · [API plan](../api/content-templates.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Starter content** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `starter content`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Presets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `presets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Default fields/blocks/layouts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `default fields/blocks/layouts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Template locking** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `template locking`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Versioning** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `versioning`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Controlled rollout** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `controlled rollout`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ContentTemplatesFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-templates-filament/src/ContentTemplatesFilamentServiceProvider.php) · [ContentTemplateResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-templates-filament/src/Resources/ContentTemplateResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ContentTemplatesService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-templates/src/Services/ContentTemplatesService.php) | `public function templates(?int $teamId, ?string $contentType = null, int $perPage = 25): LengthAwarePaginator`<br>`public function create(array $data, ?int $teamId = null): ContentTemplate`<br>`public function publish(ContentTemplate $template): ContentTemplate`<br>`public function lock(ContentTemplate $template): ContentTemplate`<br>`public function select(string $contentType, ?int $teamId, int $bucket = 0): ?ContentTemplate` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ContentTemplate.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-templates/src/Models/ContentTemplate.php) | `team_id`, `name`, `slug`, `content_type`, `version`, `schema`, `defaults`, `locked`, `published`, `rollout_percent` |
<!-- layer-implementation-plan:end -->
