# Social Network Publishing React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-publishing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-social-network-social-network-publishing-react-native
**Matching core package:** module-social-network-social-network-publishing ([implementation](../core/social-network-publishing.md))
**Matching API package:** module-social-network-social-network-publishing-api ([contract](../api/social-network-publishing.md))

## Implementation plan

This adapter presents Social Network Publishing for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Social Network Publishing API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/social-network-publishing.md), and [API module](../api/social-network-publishing.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `social-network-publishing`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-social-network-mobile-react`](https://github.com/liberusoftware/project-social-network-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/social-network-publishing.md)) |
| Capability React Native module skeleton | [`module-social-network-publishing-react-native`](https://github.com/liberusoftware/module-social-network-publishing-react-native) (`@liberusoftware/module-social-network-publishing-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Posts** | Progressive mobile list/detail/sheet flow for `posts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Articles** | Progressive mobile list/detail/sheet flow for `articles` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Drafts** | Progressive mobile list/detail/sheet flow for `drafts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Audiences** | Progressive mobile list/detail/sheet flow for `audiences` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Edits** | Progressive mobile list/detail/sheet flow for `edits` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Mentions** | Progressive mobile list/detail/sheet flow for `mentions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Hashtags** | Progressive mobile list/detail/sheet flow for `hashtags` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Polls** | Progressive mobile list/detail/sheet flow for `polls` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Links** | Progressive mobile list/detail/sheet flow for `links` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Schedules** | Progressive mobile list/detail/sheet flow for `schedules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
