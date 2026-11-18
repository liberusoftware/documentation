# Cms Web Delivery Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-web-delivery). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-cms-web-delivery-flutter
**Matching core package:** module-cms-cms-web-delivery ([implementation](../core/cms-web-delivery.md))
**Matching API package:** module-cms-cms-web-delivery-api ([contract](../api/cms-web-delivery.md))

## Implementation plan

This adapter presents Cms Web Delivery for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Cms Web Delivery API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/cms-web-delivery.md), and [API module](../api/cms-web-delivery.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `cms-web-delivery`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-cms-mobile-flutter`](https://github.com/liberusoftware/project-cms-mobile-flutter) | [`module-cms-web-delivery-flutter`](https://github.com/liberusoftware/module-cms-web-delivery-flutter) (`module_cms_web_delivery_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-cms-dart-mobile`](https://github.com/liberusoftware/project-cms-dart-mobile) | [`module-cms-web-delivery-dart-mobile`](https://github.com/liberusoftware/module-cms-web-delivery-dart-mobile) (`module_cms_web_delivery_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-cms-dart-desktop`](https://github.com/liberusoftware/project-cms-dart-desktop) | [`module-cms-web-delivery-dart-desktop`](https://github.com/liberusoftware/module-cms-web-delivery-dart-desktop) (`module_cms_web_delivery_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | [API plan](../api/cms-web-delivery.md) · [Core plan](../core/cms-web-delivery.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Canonical route rendering** | Adaptive mobile cards/sheets for `canonical route rendering` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `canonical route rendering` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Response metadata** | Adaptive mobile cards/sheets for `response metadata` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `response metadata` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Cache tags** | Adaptive mobile cards/sheets for `cache tags` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `cache tags` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Preview mode** | Adaptive mobile cards/sheets for `preview mode` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `preview mode` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Redirects** | Adaptive mobile cards/sheets for `redirects` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `redirects` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Errors** | Adaptive mobile cards/sheets for `errors` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `errors` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Maintenance** | Adaptive mobile cards/sheets for `maintenance` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `maintenance` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Edge invalidation** | Adaptive mobile cards/sheets for `edge invalidation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `edge invalidation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [DeliveryRouteQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Queries/DeliveryRouteQuery.php) | `public function paginate(int $perPage = 15, string $search = '', ?string $status = null): LengthAwarePaginator`<br>`public function find(string $path): ?DeliveryRoute` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [WebDeliveryService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Actions/WebDeliveryService.php) | `public function __construct(private EdgeInvalidationRegistry $edge)`<br>`public function registerRoute(array $attributes): DeliveryRoute`<br>`public function updateRoute(DeliveryRoute $route, array $attributes): DeliveryRoute`<br>`public function deleteRoute(DeliveryRoute $route): void`<br>`public function render(string $path, ?string $previewToken = null): DeliveryResult`<br>`public function issuePreviewToken(DeliveryRoute $route): string`<br>`public function setMaintenance(DeliveryRoute $route, bool $enabled): DeliveryRoute`<br>`public function invalidate(array $cacheTags, string $idempotencyKey, ?string $provider = null, int\|string\|null $teamId = null): DeliveryInvalidation` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DeliveryInvalidation.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Models/DeliveryInvalidation.php) | `idempotency_key`, `cache_tags`, `status`, `provider`, `failure_reason`, `completed_at`, `team_id` |
| [DeliveryRoute.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Models/DeliveryRoute.php) | `path`, `route_type`, `content_type`, `content_id`, `body`, `canonical_url`, `redirect_url`, `redirect_status`, `metadata`, `cache_tags`, `cache_ttl`, `preview_enabled`, `preview_token_hash`, `preview_expires_at`, `maintenance`, `status`, `error_status`, `error_message`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [WebDeliveryController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-web-delivery-api/src/Http/Controllers/WebDeliveryController.php) | `public function __construct(private DeliveryRouteQuery $routes, private WebDeliveryService $delivery)`<br>`public function index(Request $request): AnonymousResourceCollection`<br>`public function show(string $path): DeliveryRouteResource`<br>`public function create(Request $request): DeliveryRouteResource`<br>`public function update(Request $request, int $route): DeliveryRouteResource`<br>`public function destroy(int $route): JsonResponse`<br>`public function resolve(Request $request): JsonResponse`<br>`public function previewToken(int $route): JsonResponse`<br>`public function invalidate(Request $request): JsonResponse`<br>`public function maintenance(Request $request, int $route): DeliveryRouteResource` |
<!-- layer-implementation-plan:end -->
