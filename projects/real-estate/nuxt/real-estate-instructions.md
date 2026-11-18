# Real Estate: Real Estate Instructions Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-instructions). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-real-estate-real-estate-instructions-nuxt`
**Matching domain module:** `real-estate-instructions`
**Application:** Real Estate
**Source feature:** [Real Estate Instructions](../features/real-estate-instructions.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/real-estate-instructions.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `real-estate-instructions` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Agency agreements:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Ownership checks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Terms:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Disclosures:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approvals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Withdrawal:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-real-estate-real-estate-instructions-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `agency-agreements`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `ownership-checks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `terms`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `disclosures`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approvals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `withdrawal`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `real-estate-instructions` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-real-estate-nuxt-vue`](https://github.com/liberusoftware/project-real-estate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/real-estate-instructions.md)) |
| Capability Nuxt module skeleton | [`module-real-estate-instructions-nuxt`](https://github.com/liberusoftware/module-real-estate-instructions-nuxt) (`@liberusoftware/module-real-estate-instructions-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Agency agreements** | Expose composable and Vue 3 component for `agency agreements` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-instructions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Ownership checks** | Expose composable and Vue 3 component for `ownership checks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-instructions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Terms** | Expose composable and Vue 3 component for `terms` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-instructions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Disclosures** | Expose composable and Vue 3 component for `disclosures` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-instructions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Approvals** | Expose composable and Vue 3 component for `approvals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-instructions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Withdrawal** | Expose composable and Vue 3 component for `withdrawal` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-instructions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [InstructionPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-instructions/src/Policies/InstructionPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Instruction $instruction): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Instruction $instruction): bool`<br>`public function delete(AuthUser $authUser, Instruction $instruction): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Instruction $instruction): bool`<br>`public function forceDelete(AuthUser $authUser, Instruction $instruction): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Instruction $instruction): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Instruction.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-instructions/src/Models/Instruction.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [InstructionController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-instructions-api/src/Http/Controllers/InstructionController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateInstruction $create): JsonResponse`<br>`public function show(Request $request, Instruction $instruction): JsonResponse`<br>`public function update(Request $request, Instruction $instruction, UpdateInstruction $update): JsonResponse`<br>`public function destroy(Request $request, Instruction $instruction, DeleteInstruction $delete): Response`<br>`public function transition(Request $request, Instruction $instruction, string $status, TransitionInstruction $transition): JsonResponse` |

**Observed route declarations:**

[modules/real-estate-instructions-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-instructions-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/instructions')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [InstructionController::class, 'index'])->name('real-estate.instructions.index');
Route::post('/', [InstructionController::class, 'store'])->name('real-estate.instructions.store');
Route::post('/{instruction}/transition/{status}', [InstructionController::class, 'transition'])->name('real-estate.instructions.transition');
Route::get('/{instruction}', [InstructionController::class, 'show'])->name('real-estate.instructions.show');
Route::delete('/{instruction}', [InstructionController::class, 'destroy'])->name('real-estate.instructions.destroy');
```
<!-- layer-implementation-plan:end -->
