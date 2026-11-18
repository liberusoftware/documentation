# Social Network: Publishing React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#publishing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-social-network-publishing-react-inertia`
**Matching domain module:** `social-network-publishing`
**Application:** Social Network
**Source feature:** [Publishing](../features/publishing.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/publishing.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Posts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Articles:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Drafts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Audiences:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Edits:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Mentions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Hashtags:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Polls:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Links:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Schedules:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-social-network-publishing-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `posts`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `articles`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `drafts`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `audiences`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `edits`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `mentions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `hashtags`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `polls`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `links`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `schedules`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, React Testing Library, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `social-network-publishing` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-social-network-laravel-inertia-react`](https://github.com/liberusoftware/project-social-network-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-social-network-publishing-react-inertia`](https://github.com/liberusoftware/module-social-network-publishing-react-inertia) (`@liberusoftware/module-social-network-publishing-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/publishing.md) · [Core plan](../core/publishing.md) · [API plan](../api/publishing.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Posts** | Render `posts` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Articles** | Render `articles` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Drafts** | Render `drafts` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Audiences** | Render `audiences` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Edits** | Render `edits` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Mentions** | Render `mentions` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Hashtags** | Render `hashtags` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Polls** | Render `polls` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Links** | Render `links` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Schedules** | Render `schedules` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

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
