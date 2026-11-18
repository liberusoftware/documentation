# Publishing Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#publishing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-social-network-publishing-flutter
**Matching core package:** module-social-network-publishing ([implementation](../core/publishing.md))
**Matching API package:** module-social-network-publishing-api ([contract](../api/publishing.md))

## Implementation plan

This adapter presents Publishing for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Publishing API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/publishing.md), and [API module](../api/publishing.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `publishing`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-social-network-mobile-flutter`](https://github.com/liberusoftware/project-social-network-mobile-flutter) | [`module-social-network-publishing-flutter`](https://github.com/liberusoftware/module-social-network-publishing-flutter) (`module_social_network_publishing_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-social-network-dart-mobile`](https://github.com/liberusoftware/project-social-network-dart-mobile) | [`module-social-network-publishing-dart-mobile`](https://github.com/liberusoftware/module-social-network-publishing-dart-mobile) (`module_social_network_publishing_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-social-network-dart-desktop`](https://github.com/liberusoftware/project-social-network-dart-desktop) | [`module-social-network-publishing-dart-desktop`](https://github.com/liberusoftware/module-social-network-publishing-dart-desktop) (`module_social_network_publishing_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | [API plan](../api/publishing.md) · [Core plan](../core/publishing.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Posts** | Adaptive mobile cards/sheets for `posts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `posts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Articles** | Adaptive mobile cards/sheets for `articles` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `articles` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Drafts** | Adaptive mobile cards/sheets for `drafts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `drafts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Audiences** | Adaptive mobile cards/sheets for `audiences` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `audiences` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Edits** | Adaptive mobile cards/sheets for `edits` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `edits` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Mentions** | Adaptive mobile cards/sheets for `mentions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `mentions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Hashtags** | Adaptive mobile cards/sheets for `hashtags` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `hashtags` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Polls** | Adaptive mobile cards/sheets for `polls` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `polls` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Links** | Adaptive mobile cards/sheets for `links` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `links` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Schedules** | Adaptive mobile cards/sheets for `schedules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `schedules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePublication.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/CreatePublication.php) | `public function __construct(private PublishingAuthorizer $authorizer)`<br>`public function handle(Profile $author, array $attributes): Publication` |
| [DeletePublication.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/DeletePublication.php) | `public function __construct(private PublishingAuthorizer $authorizer)`<br>`public function handle(Profile $author, Publication $publication): void` |
| [ListPublications.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/ListPublications.php) | `public function handle(Profile $viewer, int $limit = 25): Collection` |
| [PublishPublication.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/PublishPublication.php) | `public function __construct(private PublishingAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $author, Publication $publication): Publication` |
| [PublishScheduledPublications.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/PublishScheduledPublications.php) | `public function __construct(private Dispatcher $events)`<br>`public function handle(?Carbon $now = null, int $limit = 100): int` |
| [UpdatePublication.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/UpdatePublication.php) | `public function __construct(private PublishingAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $author, Publication $publication, array $attributes): Publication` |
| [UpdatePublicationEnrichments.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Actions/UpdatePublicationEnrichments.php) | `public function __construct(private PublishingAuthorizer $authorizer)`<br>`public function handle(Profile $author, Publication $publication, array $data): Publication` |
| [PublishingAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Contracts/PublishingAuthorizer.php) | `public function create(Profile $author): void`<br>`public function update(Profile $author, Publication $publication): void`<br>`public function publish(Profile $author, Publication $publication): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Publication.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing/src/Models/Publication.php) | `id`, `author_profile_id`, `kind`, `state`, `audience`, `title`, `body`, `metadata`, `scheduled_at`, `published_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PublishingController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing-api/src/Http/Controllers/PublishingController.php) | `public function store(Request $request, GetProfile $get, CreatePublication $create): JsonResponse`<br>`public function publish(string $publication, Request $request, GetProfile $get, PublishPublication $publish): JsonResponse`<br>`public function index(Request $request, GetProfile $get, ListPublications $list): JsonResponse`<br>`public function show(string $publication, Request $request, GetProfile $get, ListPublications $list): JsonResponse`<br>`public function update(string $publication, Request $request, GetProfile $get, UpdatePublication $update): JsonResponse`<br>`public function destroy(string $publication, Request $request, GetProfile $get, DeletePublication $delete): JsonResponse`<br>`public function enrichments(string $publication, Request $request, GetProfile $get, UpdatePublicationEnrichments $update): JsonResponse` |

**Observed route declarations:**

[modules/social-network-publishing-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-publishing-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/publishing')->middleware(['auth:sanctum', 'throttle:60,1'])->name('social-network.publishing.api.')->group(function (): void {
Route::get('/publications', [PublishingController::class, 'index'])->name('index');
Route::post('/publications', [PublishingController::class, 'store'])->name('store');
Route::get('/publications/{publication}', [PublishingController::class, 'show'])->name('show');
Route::patch('/publications/{publication}', [PublishingController::class, 'update'])->name('update');
Route::patch('/publications/{publication}/enrichments', [PublishingController::class, 'enrichments'])->name('enrichments');
Route::delete('/publications/{publication}', [PublishingController::class, 'destroy'])->name('destroy');
Route::post('/publications/{publication}/publish', [PublishingController::class, 'publish'])->name('publish');
```
<!-- layer-implementation-plan:end -->
