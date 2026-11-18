# CMS: Module Cms Posts Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-posts). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-module-cms-posts-filament`  
**Matching domain module:** `module-cms-posts`  
**Application:** CMS  
**Source feature:** [Module Cms Posts](../features/module-cms-posts.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-cms-posts` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Articles and editorial posts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Authors and contributor attribution:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Series and category assignments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Scheduled publication and feeds:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reading metadata and SEO:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-module-cms-posts-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `articles-and-editorial-posts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `authors-and-contributor-attribution`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `series-and-category-assignments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `scheduled-publication-and-feeds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reading-metadata-and-seo`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-cms-posts` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-posts-filament`](https://github.com/liberusoftware/module-cms-posts-filament) (`liberusoftware/cms-posts-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-cms-posts.md) · [API plan](../api/module-cms-posts.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Articles and editorial posts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `articles and editorial posts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Authors and contributor attribution** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `authors and contributor attribution`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Series and category assignments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `series and category assignments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Scheduled publication and feeds** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `scheduled publication and feeds`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reading metadata and SEO** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reading metadata and seo`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListPosts.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Filament/Pages/ListPosts.php) · [PostResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Filament/PostResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [PostRepositoryInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Contracts/PostRepositoryInterface.php) | `public function find(int $id): ?Post`<br>`public function findBySlug(string $slug): ?Post`<br>`public function published(): array`<br>`public function featured(): array`<br>`public function byCategory(string $categorySlug): array`<br>`public function byTag(string $tagSlug): array`<br>`public function search(string $query, int $limit): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Category.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Models/Category.php) | `name`, `slug`, `description`, `team_id` |
| [Post.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Models/Post.php) | `title`, `slug`, `content`, `excerpt`, `status`, `published_at`, `is_featured`, `featured_media_id`, `author_id`, `team_id` |
| [Tag.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-posts/src/Models/Tag.php) | `name`, `slug`, `team_id` |
<!-- layer-implementation-plan:end -->
