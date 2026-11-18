# Cms Site Recipes Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-site-recipes). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-cms-site-recipes-flutter
**Matching core package:** module-cms-cms-site-recipes ([implementation](../core/cms-site-recipes.md))
**Matching API package:** module-cms-cms-site-recipes-api ([contract](../api/cms-site-recipes.md))

## Implementation plan

This adapter presents Cms Site Recipes for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Cms Site Recipes API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/cms-site-recipes.md), and [API module](../api/cms-site-recipes.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `cms-site-recipes`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-cms-mobile-flutter`](https://github.com/liberusoftware/project-cms-mobile-flutter) | [`module-cms-site-recipes-flutter`](https://github.com/liberusoftware/module-cms-site-recipes-flutter) (`module_cms_site_recipes_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-cms-dart-mobile`](https://github.com/liberusoftware/project-cms-dart-mobile) | [`module-cms-site-recipes-dart-mobile`](https://github.com/liberusoftware/module-cms-site-recipes-dart-mobile) (`module_cms_site_recipes_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-cms-dart-desktop`](https://github.com/liberusoftware/project-cms-dart-desktop) | [`module-cms-site-recipes-dart-desktop`](https://github.com/liberusoftware/module-cms-site-recipes-dart-desktop) (`module_cms_site_recipes_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | [API plan](../api/cms-site-recipes.md) · [Core plan](../core/cms-site-recipes.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Versioned bundles of modules** | Adaptive mobile cards/sheets for `versioned bundles of modules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `versioned bundles of modules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Configuration** | Adaptive mobile cards/sheets for `configuration` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `configuration` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Content types** | Adaptive mobile cards/sheets for `content types` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `content types` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Workflows** | Adaptive mobile cards/sheets for `workflows` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `workflows` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Menus** | Adaptive mobile cards/sheets for `menus` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `menus` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Blocks** | Adaptive mobile cards/sheets for `blocks` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `blocks` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Themes** | Adaptive mobile cards/sheets for `themes` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `themes` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Starter content** | Adaptive mobile cards/sheets for `starter content` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `starter content` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

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
