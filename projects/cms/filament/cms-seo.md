# CMS: Cms Seo Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-seo). Observed identity: [`liberusoftware/module-cms-seo-filament`](../../../modules/source/liberusoftware--module-cms-seo-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-cms-seo-filament`  
**Matching domain module:** `cms-seo`  
**Application:** CMS  
**Source feature:** [Cms Seo](../features/cms-seo.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-seo` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Titles/descriptions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Canonical URLs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Robots:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Structured data:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Social cards:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Hreflang:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Index controls:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Content checks:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-cms-seo-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `titles-descriptions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `canonical-urls`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `robots`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `structured-data`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `social-cards`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `hreflang`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `index-controls`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `content-checks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-seo` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-seo-filament`](https://github.com/liberusoftware/module-cms-seo-filament) (`liberusoftware/cms-seo-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-seo.md) · [API plan](../api/cms-seo.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Titles/descriptions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `titles/descriptions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Canonical URLs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `canonical urls`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Robots** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `robots`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Structured data** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `structured data`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Social cards** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `social cards`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Hreflang** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `hreflang`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Index controls** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `index controls`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Content checks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `content checks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListSeoMetadata.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-seo-filament/src/Resources/Pages/ListSeoMetadata.php) · [SeoMetadataResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-seo-filament/src/Resources/SeoMetadataResource.php) · [SeoFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-seo-filament/src/SeoFilamentServiceProvider.php).

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SeoMetadata.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-seo/src/Models/SeoMetadata.php) | `seoable_type`, `seoable_id`, `title`, `description`, `canonical_url`, `robots`, `structured_data`, `social_cards`, `hreflang`, `noindex`, `noarchive`, `team_id` |
<!-- layer-implementation-plan:end -->
