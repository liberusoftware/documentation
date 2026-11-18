# CMS: Cms Pages Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-pages). Observed identity: [`liberusoftware/module-cms-pages-filament`](../../../modules/source/liberusoftware--module-cms-pages-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-cms-pages-filament`  
**Matching domain module:** `cms-pages`  
**Application:** CMS  
**Source feature:** [Cms Pages](../features/cms-pages.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-pages` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Hierarchy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Slugs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Routing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Home/error pages:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Aliases:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Redirects:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Breadcrumbs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Templates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Previews:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-cms-pages-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `hierarchy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `slugs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `routing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `home-error-pages`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `aliases`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `redirects`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `breadcrumbs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `templates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `previews`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-pages` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-pages-filament`](https://github.com/liberusoftware/module-cms-pages-filament) (`liberusoftware/cms-pages-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-pages.md) · [API plan](../api/cms-pages.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Hierarchy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `hierarchy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Slugs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `slugs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Routing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `routing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Home/error pages** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `home/error pages`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Aliases** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `aliases`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Redirects** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `redirects`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Breadcrumbs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `breadcrumbs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Templates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `templates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Previews** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `previews`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PageResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Filament/PageResource.php) · [ListPages.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Filament/Pages/ListPages.php) · [PagesFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-pages-filament/src/PagesFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [PageTreeQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Queries/PageTreeQuery.php) | `public function roots(string $search = ''): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [PageRepositoryInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Contracts/PageRepositoryInterface.php) | `public function find(int $id): ?Page`<br>`public function findBySlug(string $slug): ?Page`<br>`public function findByPath(string $path): ?Page`<br>`public function redirectForPath(string $path): ?PageRedirect`<br>`public function published(): array`<br>`public function roots(): array`<br>`public function search(string $query, int $limit): array` |
| [PageRoutingService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Services/PageRoutingService.php) | `public function addAlias(Page $page, string $path): PageAlias`<br>`public function createRedirect(array $attributes): PageRedirect`<br>`public function updateRedirect(PageRedirect $redirect, array $attributes): PageRedirect`<br>`public function deleteRedirect(PageRedirect $redirect): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Page.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Models/Page.php) | `title`, `slug`, `content`, `excerpt`, `template`, `status`, `published_at`, `parent_id`, `featured_media_id`, `team_id`, `user_id`, `is_home`, `is_error` |
| [PageAlias.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Models/PageAlias.php) | `page_id`, `path`, `team_id` |
| [PageRedirect.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Models/PageRedirect.php) | `from_path`, `to_path`, `status_code`, `active`, `team_id` |
<!-- layer-implementation-plan:end -->
