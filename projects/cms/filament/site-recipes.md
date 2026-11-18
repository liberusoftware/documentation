# CMS: Site Recipes Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#site-recipes). Observed identity: [`liberusoftware/module-cms-site-recipes-filament`](../../../modules/source/liberusoftware--module-cms-site-recipes-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-site-recipes-filament`  
**Matching domain module:** `cms-site-recipes`  
**Application:** CMS  
**Source feature:** [Site Recipes](../features/site-recipes.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-site-recipes` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Versioned bundles of modules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Configuration:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Content types:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Workflows:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Menus:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Blocks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Themes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Starter content:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-site-recipes-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `versioned-bundles-of-modules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `configuration`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `content-types`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `workflows`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `menus`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `blocks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `themes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `starter-content`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-site-recipes` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-site-recipes-filament`](https://github.com/liberusoftware/module-cms-site-recipes-filament) (`liberusoftware/cms-site-recipes-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/site-recipes.md) · [API plan](../api/site-recipes.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Versioned bundles of modules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `versioned bundles of modules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Configuration** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `configuration`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Content types** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `content types`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Workflows** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `workflows`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Menus** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `menus`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Blocks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `blocks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Themes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `themes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Starter content** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `starter content`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListSiteRecipes.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-site-recipes-filament/src/Resources/Pages/ListSiteRecipes.php) · [SiteRecipeResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-site-recipes-filament/src/Resources/SiteRecipeResource.php) · [SiteRecipesFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-site-recipes-filament/src/SiteRecipesFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [SiteRecipeQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-site-recipes/src/Queries/SiteRecipeQuery.php) | `public function recipes(int $perPage = 15, bool $publishedOnly = false): LengthAwarePaginator`<br>`public function find(string $key, bool $publishedOnly = false): ?SiteRecipe` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SiteRecipeService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-site-recipes/src/Services/SiteRecipeService.php) | `public function create(string $key, string $name, ?string $description = null, ?int $teamId = null): SiteRecipe`<br>`public function version(SiteRecipe $recipe, array $bundle, ?int $authorId = null): SiteRecipeVersion`<br>`public function update(SiteRecipe $recipe, array $attributes): SiteRecipe`<br>`public function publish(SiteRecipe $recipe): SiteRecipe`<br>`public function archive(SiteRecipe $recipe): SiteRecipe`<br>`public function export(SiteRecipe $recipe): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SiteRecipe.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-site-recipes/src/Models/SiteRecipe.php) | `key`, `name`, `description`, `status`, `team_id` |
| [SiteRecipeVersion.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-site-recipes/src/Models/SiteRecipeVersion.php) | `recipe_id`, `version`, `modules`, `configuration`, `content_types`, `workflows`, `menus`, `blocks`, `themes`, `starter_content`, `checksum`, `author_id` |
<!-- layer-implementation-plan:end -->
