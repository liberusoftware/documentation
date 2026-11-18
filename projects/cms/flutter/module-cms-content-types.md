# Module Cms Content Types Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-content-types). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-module-cms-content-types-flutter
**Matching core package:** module-cms-module-cms-content-types ([implementation](../core/module-cms-content-types.md))
**Matching API package:** module-cms-module-cms-content-types-api ([contract](../api/module-cms-content-types.md))

## Implementation plan

This adapter presents Module Cms Content Types for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Cms Content Types API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/module-cms-content-types.md), and [API module](../api/module-cms-content-types.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `module-cms-content-types`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-cms-mobile-flutter`](https://github.com/liberusoftware/project-cms-mobile-flutter) | [`module-cms-content-types-flutter`](https://github.com/liberusoftware/module-cms-content-types-flutter) (`module_cms_content_types_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-cms-dart-mobile`](https://github.com/liberusoftware/project-cms-dart-mobile) | [`module-cms-content-types-dart-mobile`](https://github.com/liberusoftware/module-cms-content-types-dart-mobile) (`module_cms_content_types_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-cms-dart-desktop`](https://github.com/liberusoftware/project-cms-dart-desktop) | [`module-cms-content-types-dart-desktop`](https://github.com/liberusoftware/module-cms-content-types-dart-desktop) (`module_cms_content_types_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | [API plan](../api/module-cms-content-types.md) · [Core plan](../core/module-cms-content-types.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Content type definitions** | Adaptive mobile cards/sheets for `content type definitions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `content type definitions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Typed field groups and repeaters** | Adaptive mobile cards/sheets for `typed field groups and repeaters` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `typed field groups and repeaters` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Validation and reference rules** | Adaptive mobile cards/sheets for `validation and reference rules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `validation and reference rules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Schema versioning and migrations** | Adaptive mobile cards/sheets for `schema versioning and migrations` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `schema versioning and migrations` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **API projection rules** | Adaptive mobile cards/sheets for `api projection rules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `api projection rules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [FieldSchemaQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-types/src/Queries/FieldSchemaQuery.php) | `public function find(string $key): ?array` |
| [PublishedEntityQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-types/src/Queries/PublishedEntityQuery.php) | `public function find(string $type, string $slug): ?ContentEntry`<br>`public function forType(string $type, int $perPage = 15, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ContentEntryMutationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-types/src/Actions/ContentEntryMutationService.php) | `public function clone(ContentEntry $entry, ?string $title = null): ContentEntry` |
| [ContentEntryRepositoryInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-types/src/Contracts/ContentEntryRepositoryInterface.php) | `public function find(int $id): ?ContentEntry`<br>`public function findBySlug(string $slug): ?ContentEntry`<br>`public function ofType(string $typeKey): array`<br>`public function published(): array`<br>`public function search(string $query, int $limit): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ContentEntry.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-types/src/Models/ContentEntry.php) | `content_type_id`, `title`, `slug`, `data`, `status`, `published_at`, `author_id`, `team_id` |
| [ContentType.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-types/src/Models/ContentType.php) | `key`, `name`, `singular_label`, `plural_label`, `fields`, `schema_version`, `schema_history` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ContentEntryApiController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-types/src/Http/Controllers/ContentEntryApiController.php) | `public function __construct(private ContentEntryRepositoryInterface $entries)`<br>`public function index(string $type): AnonymousResourceCollection`<br>`public function show(string $type, string $slug): ContentEntryResource` |
| [ContentEntryWriteController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-types/src/Http/Controllers/ContentEntryWriteController.php) | `public function __construct(private ContentEntryRepositoryInterface $entries)`<br>`public function store(StoreContentEntryRequest $request): JsonResponse`<br>`public function update(UpdateContentEntryRequest $request, int $id): ContentEntryResource`<br>`public function destroy(int $id): Response` |
<!-- layer-implementation-plan:end -->
