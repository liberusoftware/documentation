# Cms Views And Query Builder React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-views-and-query-builder). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-cms-views-and-query-builder-react-native
**Matching core package:** module-cms-cms-views-and-query-builder ([implementation](../core/cms-views-and-query-builder.md))
**Matching API package:** module-cms-cms-views-and-query-builder-api ([contract](../api/cms-views-and-query-builder.md))

## Implementation plan

This adapter presents Cms Views And Query Builder for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Cms Views And Query Builder API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/cms-views-and-query-builder.md), and [API module](../api/cms-views-and-query-builder.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `cms-views-and-query-builder`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-cms-mobile-react`](https://github.com/liberusoftware/project-cms-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/cms-views-and-query-builder.md)) |
| Capability React Native module skeleton | [`module-cms-views-and-query-builder-react-native`](https://github.com/liberusoftware/module-cms-views-and-query-builder-react-native) (`@liberusoftware/module-cms-views-and-query-builder-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Permission-safe listings from content/fields/relationships with filters** | Progressive mobile list/detail/sheet flow for `permission-safe listings from content/fields/relationships with filters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Sorting** | Progressive mobile list/detail/sheet flow for `sorting` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Grouping** | Progressive mobile list/detail/sheet flow for `grouping` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Exposed filters** | Progressive mobile list/detail/sheet flow for `exposed filters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Pagination** | Progressive mobile list/detail/sheet flow for `pagination` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Feeds** | Progressive mobile list/detail/sheet flow for `feeds` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Displays** | Progressive mobile list/detail/sheet flow for `displays` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListingQueryService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-views-and-query-builder/src/Queries/ListingQueryService.php) | `public function execute(ViewDefinition $view, int $perPage = 15, array $input = []): LengthAwarePaginator` |
| [ViewDefinitionQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-views-and-query-builder/src/Queries/ViewDefinitionQuery.php) | `public function list(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function find(string $slug): ?ViewDefinition`<br>`public function publishedList(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function findPublished(string $slug): ?ViewDefinition` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ViewDefinitionMutationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-views-and-query-builder/src/Actions/ViewDefinitionMutationService.php) | `public function create(array $attributes): ViewDefinition`<br>`public function update(ViewDefinition $view, array $attributes): ViewDefinition` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ViewDefinition.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-views-and-query-builder/src/Models/ViewDefinition.php) | `name`, `slug`, `source`, `description`, `definition`, `visibility`, `status`, `published_at`, `user_id`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ViewsAndQueryBuilderController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-views-and-query-builder-api/src/Http/Controllers/ViewsAndQueryBuilderController.php) | `public function __construct(private ViewDefinitionQuery $views, private ListingQueryService $listings)`<br>`public function index(Request $request): AnonymousResourceCollection`<br>`public function show(string $slug): ViewDefinitionResource`<br>`public function execute(Request $request, string $slug): AnonymousResourceCollection` |
<!-- layer-implementation-plan:end -->
