# Cms Site Recipes React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-site-recipes). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-cms-site-recipes-react-native
**Matching core package:** module-cms-cms-site-recipes ([implementation](../core/cms-site-recipes.md))
**Matching API package:** module-cms-cms-site-recipes-api ([contract](../api/cms-site-recipes.md))

## Implementation plan

This adapter presents Cms Site Recipes for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Cms Site Recipes API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/cms-site-recipes.md), and [API module](../api/cms-site-recipes.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `cms-site-recipes`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-cms-mobile-react`](https://github.com/liberusoftware/project-cms-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/cms-site-recipes.md)) |
| Capability React Native module skeleton | [`module-cms-site-recipes-react-native`](https://github.com/liberusoftware/module-cms-site-recipes-react-native) (`@liberusoftware/module-cms-site-recipes-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Versioned bundles of modules** | Progressive mobile list/detail/sheet flow for `versioned bundles of modules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Configuration** | Progressive mobile list/detail/sheet flow for `configuration` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Content types** | Progressive mobile list/detail/sheet flow for `content types` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Workflows** | Progressive mobile list/detail/sheet flow for `workflows` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Menus** | Progressive mobile list/detail/sheet flow for `menus` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Blocks** | Progressive mobile list/detail/sheet flow for `blocks` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Themes** | Progressive mobile list/detail/sheet flow for `themes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Starter content** | Progressive mobile list/detail/sheet flow for `starter content` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
