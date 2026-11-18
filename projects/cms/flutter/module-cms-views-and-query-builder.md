# Module Cms Views And Query Builder Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-views-and-query-builder). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-module-cms-views-and-query-builder-flutter
**Matching core package:** module-cms-module-cms-views-and-query-builder ([implementation](../core/module-cms-views-and-query-builder.md))
**Matching API package:** module-cms-module-cms-views-and-query-builder-api ([contract](../api/module-cms-views-and-query-builder.md))

## Implementation plan

This adapter presents Module Cms Views And Query Builder for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Cms Views And Query Builder API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/module-cms-views-and-query-builder.md), and [API module](../api/module-cms-views-and-query-builder.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `module-cms-views-and-query-builder`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-cms-mobile-flutter`](https://github.com/liberusoftware/project-cms-mobile-flutter) | [`module-cms-views-and-query-builder-flutter`](https://github.com/liberusoftware/module-cms-views-and-query-builder-flutter) (`module_cms_views_and_query_builder_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-cms-dart-mobile`](https://github.com/liberusoftware/project-cms-dart-mobile) | [`module-cms-views-and-query-builder-dart-mobile`](https://github.com/liberusoftware/module-cms-views-and-query-builder-dart-mobile) (`module_cms_views_and_query_builder_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-cms-dart-desktop`](https://github.com/liberusoftware/project-cms-dart-desktop) | [`module-cms-views-and-query-builder-dart-desktop`](https://github.com/liberusoftware/module-cms-views-and-query-builder-dart-desktop) (`module_cms_views_and_query_builder_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | [API plan](../api/module-cms-views-and-query-builder.md) · [Core plan](../core/module-cms-views-and-query-builder.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Permission-safe listings from content/fields/relationships with filters** | Adaptive mobile cards/sheets for `permission-safe listings from content/fields/relationships with filters` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `permission-safe listings from content/fields/relationships with filters` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Sorting** | Adaptive mobile cards/sheets for `sorting` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `sorting` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Grouping** | Adaptive mobile cards/sheets for `grouping` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `grouping` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Exposed filters** | Adaptive mobile cards/sheets for `exposed filters` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `exposed filters` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Pagination** | Adaptive mobile cards/sheets for `pagination` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `pagination` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Feeds** | Adaptive mobile cards/sheets for `feeds` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `feeds` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Displays** | Adaptive mobile cards/sheets for `displays` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `displays` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
