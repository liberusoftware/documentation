# Real Estate: Matching React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#matching). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-real-estate-matching-react-inertia`
**Matching domain module:** `real-estate-matching`
**Application:** Real Estate
**Source feature:** [Matching](../features/matching.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/matching.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Applicant requirements:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Affordability:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Preferences:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Scoring:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Alerts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Feedback:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Exclusions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-real-estate-matching-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `applicant-requirements`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `affordability`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `preferences`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `scoring`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `alerts`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `feedback`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `exclusions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `real-estate-matching` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-real-estate-laravel-inertia-react`](https://github.com/liberusoftware/project-real-estate-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-real-estate-matching-react-inertia`](https://github.com/liberusoftware/module-real-estate-matching-react-inertia) (`@liberusoftware/module-real-estate-matching-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/matching.md) · [Core plan](../core/matching.md) · [API plan](../api/matching.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Applicant requirements** | Render `applicant requirements` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Affordability** | Render `affordability` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Preferences** | Render `preferences` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Scoring** | Render `scoring` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Alerts** | Render `alerts` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Feedback** | Render `feedback` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Exclusions** | Render `exclusions` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [MatchProfilePolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-matching/src/Policies/MatchProfilePolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, MatchProfile $matchProfile): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, MatchProfile $matchProfile): bool`<br>`public function delete(AuthUser $authUser, MatchProfile $matchProfile): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, MatchProfile $matchProfile): bool`<br>`public function forceDelete(AuthUser $authUser, MatchProfile $matchProfile): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, MatchProfile $matchProfile): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MatchProfile.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-matching/src/Models/MatchProfile.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [MatchProfileController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-matching-api/src/Http/Controllers/MatchProfileController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateMatchProfile $create): JsonResponse`<br>`public function show(Request $request, MatchProfile $matchProfile): JsonResponse`<br>`public function update(Request $request, MatchProfile $matchProfile, UpdateMatchProfile $update): JsonResponse`<br>`public function updateSection(Request $request, MatchProfile $matchProfile, string $section, UpdateMatchProfileSection $update): JsonResponse`<br>`public function calculateScore(Request $request, CalculateMatchScore $calculate): JsonResponse`<br>`public function recommendProperties(Request $request, RankPropertyRecommendations $rank): JsonResponse`<br>`public function destroy(Request $request, MatchProfile $matchProfile, DeleteMatchProfile $delete): Response` |

**Observed route declarations:**

[modules/real-estate-matching-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-matching-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/matching')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [MatchProfileController::class, 'index'])->name('real-estate.matching.index');
Route::post('/', [MatchProfileController::class, 'store'])->name('real-estate.matching.store');
Route::post('/calculate-score', [MatchProfileController::class, 'calculateScore'])->name('real-estate.matching.calculate-score');
Route::post('/recommend-properties', [MatchProfileController::class, 'recommendProperties'])->name('real-estate.matching.recommend-properties');
Route::get('/{matchProfile}', [MatchProfileController::class, 'show'])->name('real-estate.matching.show');
Route::patch('/{matchProfile}/{section}', [MatchProfileController::class, 'updateSection'])->whereIn('section', ['requirements', 'affordability', 'preferences', 'scoring', 'alerts', 'feedback', 'exclusions'])->name('real-estate.matching.section');
Route::delete('/{matchProfile}', [MatchProfileController::class, 'destroy'])->name('real-estate.matching.destroy');
```
<!-- layer-implementation-plan:end -->
