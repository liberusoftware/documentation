# CMS: Module Cms Site Recipes Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-site-recipes). Observed identity: [`liberusoftware/module-cms-site-recipes-livewire`](../../../modules/source/liberusoftware--module-cms-site-recipes-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-module-cms-site-recipes-livewire`  
**Matching domain module:** `module-cms-site-recipes`  
**Application:** CMS  
**Source feature:** [Module Cms Site Recipes](../features/module-cms-site-recipes.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Versioned bundles of modules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Configuration:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Content types:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Workflows:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Menus:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Blocks:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Themes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Starter content:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-module-cms-site-recipes-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsModuleCmsSiteRecipes::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `versioned-bundles-of-modules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `configuration`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `content-types`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `workflows`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `menus`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `blocks`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `themes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `starter-content`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-cms-site-recipes` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-cms-site-recipes.md) · [API plan](../api/module-cms-site-recipes.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Versioned bundles of modules** | Expose a focused Livewire 4 component and namespaced Blade default view for `versioned bundles of modules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Configuration** | Expose a focused Livewire 4 component and namespaced Blade default view for `configuration` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Content types** | Expose a focused Livewire 4 component and namespaced Blade default view for `content types` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Workflows** | Expose a focused Livewire 4 component and namespaced Blade default view for `workflows` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Menus** | Expose a focused Livewire 4 component and namespaced Blade default view for `menus` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Blocks** | Expose a focused Livewire 4 component and namespaced Blade default view for `blocks` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Themes** | Expose a focused Livewire 4 component and namespaced Blade default view for `themes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Starter content** | Expose a focused Livewire 4 component and namespaced Blade default view for `starter content` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [RecipePreview.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-site-recipes-livewire/src/Livewire/RecipePreview.php) · [SiteRecipesLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-site-recipes-livewire/src/SiteRecipesLivewireServiceProvider.php).

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
