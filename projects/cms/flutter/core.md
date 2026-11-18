# Core Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-core-flutter
**Matching core package:** module-cms-core ([implementation](../core/core.md))
**Matching API package:** module-cms-core-api ([contract](../api/core.md))

## Implementation plan

This adapter presents Core for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Core API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/core.md), and [API module](../api/core.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `core`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-cms-mobile-flutter`](https://github.com/liberusoftware/project-cms-mobile-flutter) | [`module-cms-core-flutter`](https://github.com/liberusoftware/module-cms-core-flutter) (`module_cms_core_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-cms-dart-mobile`](https://github.com/liberusoftware/project-cms-dart-mobile) | [`module-cms-core-dart-mobile`](https://github.com/liberusoftware/module-cms-core-dart-mobile) (`module_cms_core_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-cms-dart-desktop`](https://github.com/liberusoftware/project-cms-dart-desktop) | [`module-cms-core-dart-desktop`](https://github.com/liberusoftware/module-cms-core-dart-desktop) (`module_cms_core_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | [API plan](../api/core.md) · [Core plan](../core/core.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Sites** | Adaptive mobile cards/sheets for `sites` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `sites` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Channels** | Adaptive mobile cards/sheets for `channels` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `channels` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Content identity** | Adaptive mobile cards/sheets for `content identity` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `content identity` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Aliases** | Adaptive mobile cards/sheets for `aliases` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `aliases` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Ownership** | Adaptive mobile cards/sheets for `ownership` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `ownership` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Shared terminology** | Adaptive mobile cards/sheets for `shared terminology` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `shared terminology` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Settings** | Adaptive mobile cards/sheets for `settings` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `settings` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Domain events** | Adaptive mobile cards/sheets for `domain events` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `domain events` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CoreQueryService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Queries/CoreQueryService.php) | `public function sites(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function site(string $key): ?Site`<br>`public function channels(string $siteKey, int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function alias(string $siteKey, string $alias): ?ContentAlias`<br>`public function aliases(string $siteKey, int $perPage = 15): LengthAwarePaginator`<br>`public function identities(string $siteKey, int $perPage = 15): LengthAwarePaginator`<br>`public function settings(string $siteKey, int $perPage = 15, string $environment = 'production'): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CoreMutationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Actions/CoreMutationService.php) | `public function createSite(array $attributes): Site`<br>`public function createChannel(Site\|int\|string $site, array $attributes): Channel`<br>`public function updateSite(Site $site, array $attributes): Site`<br>`public function updateChannel(Channel $channel, array $attributes): Channel`<br>`public function deleteSite(Site $site): void`<br>`public function deleteChannel(Channel $channel): void`<br>`public function createIdentity(Site\|int\|string $site, array $attributes): ContentIdentity`<br>`public function createAlias(Site\|int\|string $site, array $attributes): ContentAlias`<br>`public function putSetting(?Site $site, string $key, array $value, string $environment = 'production'): Setting` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Channel.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/Channel.php) | `site_id`, `key`, `name`, `type`, `settings`, `team_id` |
| [ContentAlias.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/ContentAlias.php) | `site_id`, `channel_id`, `alias`, `target_type`, `target_id`, `redirect_status`, `team_id` |
| [ContentIdentity.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/ContentIdentity.php) | `site_id`, `channel_id`, `content_type`, `content_id`, `canonical_path`, `status`, `owner_type`, `owner_id`, `metadata`, `team_id` |
| [Setting.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/Setting.php) | `site_id`, `key`, `value`, `environment` |
| [Site.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/Site.php) | `key`, `name`, `domain`, `default_locale`, `timezone`, `status`, `settings`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CoreApiController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-core-api/src/Http/Controllers/CoreApiController.php) | `public function __construct( private CoreQueryService $queries, private CoreMutationService $mutations, )`<br>`public function createSite(Request $request): JsonResponse`<br>`public function createChannel(Request $request, string $site): JsonResponse`<br>`public function sites(): AnonymousResourceCollection`<br>`public function site(string $site): CoreSiteResource`<br>`public function channels(string $site): AnonymousResourceCollection`<br>`public function alias(string $site, string $alias): CoreAliasResource`<br>`public function aliases(string $site): AnonymousResourceCollection`<br>`public function identities(string $site): AnonymousResourceCollection`<br>`public function updateSite(Request $request, string $site): CoreSiteResource`<br>`public function destroySite(string $site): JsonResponse`<br>`public function updateChannel(Request $request, string $site, string $channel): CoreChannelResource`<br>`public function destroyChannel(string $site, string $channel): JsonResponse`<br>`public function createIdentity(Request $request, string $site): JsonResponse`<br>`public function createAlias(Request $request, string $site): JsonResponse`<br>`public function settings(string $site): AnonymousResourceCollection`<br>`public function putSetting(Request $request, string $site, string $key): CoreSettingResource` |
<!-- layer-implementation-plan:end -->
