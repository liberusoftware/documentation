# Pages React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#pages). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-pages-react-native
**Matching core package:** module-cms-pages ([implementation](../core/pages.md))
**Matching API package:** module-cms-pages-api ([contract](../api/pages.md))

## Implementation plan

This adapter presents Pages for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Pages API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/pages.md), and [API module](../api/pages.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `pages`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-cms-mobile-react`](https://github.com/liberusoftware/project-cms-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/pages.md)) |
| Capability React Native module skeleton | `module-cms-pages-react-native` (`@liberusoftware/module-cms-pages-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Hierarchy** | Progressive mobile list/detail/sheet flow for `hierarchy` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Slugs** | Progressive mobile list/detail/sheet flow for `slugs` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Routing** | Progressive mobile list/detail/sheet flow for `routing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Home/error pages** | Progressive mobile list/detail/sheet flow for `home/error pages` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Aliases** | Progressive mobile list/detail/sheet flow for `aliases` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Redirects** | Progressive mobile list/detail/sheet flow for `redirects` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Breadcrumbs** | Progressive mobile list/detail/sheet flow for `breadcrumbs` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Templates** | Progressive mobile list/detail/sheet flow for `templates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Previews** | Progressive mobile list/detail/sheet flow for `previews` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

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

| Observed API controller | Handler signatures |
| --- | --- |
| [PageApiController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Http/Controllers/PageApiController.php) | `public function __construct(private PageRepositoryInterface $pages)`<br>`public function index(): AnonymousResourceCollection`<br>`public function show(string $slug): PageResource` |
| [PageWriteController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Http/Controllers/PageWriteController.php) | `public function __construct(private PageRepositoryInterface $pages)`<br>`public function store(StorePageRequest $request): JsonResponse`<br>`public function update(UpdatePageRequest $request, int $id): PageResource`<br>`public function destroy(int $id): Response` |
| [PageRoutingController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-pages-api/src/Http/Controllers/PageRoutingController.php) | `public function __construct(private PageRoutingService $routing)`<br>`public function alias(Request $request, int $id): JsonResponse`<br>`public function redirect(Request $request): JsonResponse`<br>`public function deleteRedirect(int $id): JsonResponse` |
<!-- layer-implementation-plan:end -->
