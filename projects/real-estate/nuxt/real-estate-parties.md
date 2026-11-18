# Real Estate: Real Estate Parties Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-parties). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-real-estate-real-estate-parties-nuxt`
**Matching domain module:** `real-estate-parties`
**Application:** Real Estate
**Source feature:** [Real Estate Parties](../features/real-estate-parties.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/real-estate-parties.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `real-estate-parties` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Applicants:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Vendors:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Landlords:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tenants:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Buyers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Solicitors:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Contractors:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Relationships:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Consent:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-real-estate-real-estate-parties-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `applicants`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `vendors`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `landlords`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tenants`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `buyers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `solicitors`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `contractors`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `relationships`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `consent`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `real-estate-parties` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-real-estate-nuxt-vue`](https://github.com/liberusoftware/project-real-estate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/real-estate-parties.md)) |
| Capability Nuxt module skeleton | [`module-real-estate-parties-nuxt`](https://github.com/liberusoftware/module-real-estate-parties-nuxt) (`@liberusoftware/module-real-estate-parties-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Applicants** | Expose composable and Vue 3 component for `applicants` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-parties.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Vendors** | Expose composable and Vue 3 component for `vendors` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-parties.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Landlords** | Expose composable and Vue 3 component for `landlords` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-parties.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Tenants** | Expose composable and Vue 3 component for `tenants` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-parties.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Buyers** | Expose composable and Vue 3 component for `buyers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-parties.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Solicitors** | Expose composable and Vue 3 component for `solicitors` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-parties.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Contractors** | Expose composable and Vue 3 component for `contractors` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-parties.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Relationships** | Expose composable and Vue 3 component for `relationships` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-parties.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Consent** | Expose composable and Vue 3 component for `consent` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-parties.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [PartyPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Policies/PartyPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Party $party): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Party $party): bool`<br>`public function delete(AuthUser $authUser, Party $party): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Party $party): bool`<br>`public function forceDelete(AuthUser $authUser, Party $party): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Party $party): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Contact.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/Contact.php) | No literal fillable array detected; inspect the model and API schema. |
| [ContactMessage.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/ContactMessage.php) | No literal fillable array detected; inspect the model and API schema. |
| [Party.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/Party.php) | No literal fillable array detected; inspect the model and API schema. |
| [PartyRelationship.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/PartyRelationship.php) | No literal fillable array detected; inspect the model and API schema. |
| [PartyReview.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/PartyReview.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ContactController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties-api/src/Http/Controllers/ContactController.php) | `public function store(Request $request, CreateContact $create): JsonResponse`<br>`public function update(Request $request, Contact $contact): JsonResponse`<br>`public function show(Request $request, Contact $contact): JsonResponse`<br>`public function destroy(Request $request, Contact $contact): Response` |
| [PartyController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties-api/src/Http/Controllers/PartyController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateParty $create): JsonResponse`<br>`public function show(Request $request, Party $party): JsonResponse`<br>`public function update(Request $request, Party $party, UpdateParty $update): JsonResponse`<br>`public function consent(Request $request, Party $party, ManagePartyConsent $manage): JsonResponse`<br>`public function relationships(Request $request, Party $party): JsonResponse`<br>`public function relationship(Request $request, Party $party, CreatePartyRelationship $create): JsonResponse`<br>`public function destroyRelationship(Request $request, Party $party, PartyRelationship $relationship, DeletePartyRelationship $delete): Response`<br>`public function destroy(Request $request, Party $party, DeleteParty $delete): Response` |
| [ContactEnquiryController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties-livewire/src/Http/Controllers/ContactEnquiryController.php) | `public function store(Request $request, CreateContactMessage $createContactMessage): RedirectResponse` |

**Observed route declarations:**

[modules/real-estate-parties-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/parties')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [PartyController::class, 'index'])->name('real-estate.parties.index');
Route::post('/', [PartyController::class, 'store'])->name('real-estate.parties.store');
Route::get('/{party}', [PartyController::class, 'show'])->name('real-estate.parties.show');
Route::post('/{party}/consent', [PartyController::class, 'consent'])->name('real-estate.parties.consent');
Route::get('/{party}/relationships', [PartyController::class, 'relationships'])->name('real-estate.parties.relationships');
Route::post('/{party}/relationships', [PartyController::class, 'relationship'])->name('real-estate.parties.relationships.store');
Route::delete('/{party}/relationships/{relationship}', [PartyController::class, 'destroyRelationship'])->name('real-estate.parties.relationships.destroy');
Route::delete('/{party}', [PartyController::class, 'destroy'])->name('real-estate.parties.destroy');
Route::prefix('api/v1/real-estate/contacts')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::post('/', [ContactController::class, 'store'])->name('real-estate.contacts.store');
Route::get('/{contact}', [ContactController::class, 'show'])->name('real-estate.contacts.show');
Route::delete('/{contact}', [ContactController::class, 'destroy'])->name('real-estate.contacts.destroy');
```
<!-- layer-implementation-plan:end -->
