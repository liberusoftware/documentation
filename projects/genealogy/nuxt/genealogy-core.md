# Genealogy: Genealogy Core Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-genealogy-core-nuxt`
**Matching domain module:** `genealogy-core`
**Application:** Genealogy
**Source feature:** [Genealogy Core](../features/genealogy-core.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/genealogy-core.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `genealogy-core` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Trees:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Ownership:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Identifiers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Privacy defaults:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Terminology:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Shared events:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-genealogy-core-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `trees`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `ownership`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `identifiers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `privacy-defaults`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `terminology`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `shared-events`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `genealogy-core` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-genealogy-nuxt-vue`](https://github.com/liberusoftware/project-genealogy-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/genealogy-core.md)) |
| Capability Nuxt module skeleton | [`module-genealogy-core-nuxt`](https://github.com/liberusoftware/module-genealogy-core-nuxt) (`@liberusoftware/module-genealogy-core-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Trees** | Expose composable and Vue 3 component for `trees` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Ownership** | Expose composable and Vue 3 component for `ownership` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Identifiers** | Expose composable and Vue 3 component for `identifiers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Privacy defaults** | Expose composable and Vue 3 component for `privacy defaults` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Terminology** | Expose composable and Vue 3 component for `terminology` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Shared events** | Expose composable and Vue 3 component for `shared events` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [TreeStatistics.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Queries/TreeStatistics.php) | `public function __construct(private readonly ?ParentGraphReader $graph = null)`<br>`public function for(Tree $tree): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateTree.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Actions/CreateTree.php) | `public function __construct(private readonly ?PersonReferenceResolver $personReference = null)`<br>`public function execute(array $attributes): Tree` |
| [DeleteTree.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Actions/DeleteTree.php) | `public function execute(Tree $tree): void` |
| [SetTreeOwner.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Actions/SetTreeOwner.php) | `public function execute(Tree $tree, string\|int\|null $userId): Tree` |
| [SetTreeVisibility.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Actions/SetTreeVisibility.php) | `public function execute(Tree $tree, bool $isPublic): Tree` |
| [UpdateTree.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Actions/UpdateTree.php) | `public function __construct(private readonly ?PersonReferenceResolver $personReference = null)`<br>`public function execute(Tree $tree, array $attributes): Tree` |
| [ParentGraphReader.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Contracts/ParentGraphReader.php) | `public function relatedPeople(string $teamId, array $personIds, bool $ancestors): array` |
| [PersonReferenceResolver.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Contracts/PersonReferenceResolver.php) | `public function existsForTeam(mixed $personId, string $teamId): bool` |
| [TeamOwnedPolicy.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Policies/TeamOwnedPolicy.php) | `public function viewAny(?object $actor): bool`<br>`public function view(?object $actor, object $record): bool`<br>`public function create(?object $actor): bool`<br>`public function update(?object $actor, object $record): bool`<br>`public function delete(?object $actor, object $record): bool` |
| [TreePolicy.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Policies/TreePolicy.php) | `public function view(?object $actor, Tree $tree): bool`<br>`public function manage(?object $actor, Tree $tree): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Tree.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core/src/Models/Tree.php) | `team_id`, `name`, `status`, `description`, `root_person_id`, `is_public`, `metadata`, `user_id`, `identifier`, `terminology` |

| Observed API controller | Handler signatures |
| --- | --- |
| [TreeController.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core-api/src/Http/Controllers/TreeController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, Tree $tree): TreeResource`<br>`public function store(Request $request, CreateTree $createTree): TreeResource`<br>`public function update(Request $request, Tree $tree, UpdateTree $updateTree): TreeResource`<br>`public function visibility(Request $request, Tree $tree, SetTreeVisibility $visibility): TreeResource`<br>`public function owner(Request $request, Tree $tree, SetTreeOwner $owner): TreeResource`<br>`public function destroy(Request $request, Tree $tree, DeleteTree $delete): void` |

**Observed route declarations:**

[modules/genealogy-core-api/routes/api.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-core-api/routes/api.php)

```php
Route::get('/', [TreeController::class, 'index'])->name('genealogy.core.index');
Route::get('/{tree}', [TreeController::class, 'show'])->name('genealogy.core.show');
Route::middleware('auth:sanctum')->group(function (): void {
Route::post('/', [TreeController::class, 'store'])->name('genealogy.core.store');
Route::patch('/{tree}/visibility', [TreeController::class, 'visibility'])->name('genealogy.core.visibility');
Route::patch('/{tree}/owner', [TreeController::class, 'owner'])->name('genealogy.core.owner');
Route::patch('/{tree}', [TreeController::class, 'update'])->name('genealogy.core.update');
Route::delete('/{tree}', [TreeController::class, 'destroy'])->name('genealogy.core.destroy');
```
<!-- layer-implementation-plan:end -->
