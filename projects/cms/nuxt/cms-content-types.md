# CMS: Cms Content Types Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-content-types). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-cms-content-types-nuxt`
**Matching domain module:** `cms-content-types`
**Application:** CMS
**Source feature:** [Cms Content Types](../features/cms-content-types.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/cms-content-types.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `cms-content-types` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Content type definitions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Typed field groups and repeaters:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Validation and reference rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Schema versioning and migrations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **API projection rules:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-cms-content-types-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `content-type-definitions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `typed-field-groups-and-repeaters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `validation-and-reference-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `schema-versioning-and-migrations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `api-projection-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `cms-content-types` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/cms-content-types.md)) |
| Capability Nuxt module skeleton | [`module-cms-content-types-nuxt`](https://github.com/liberusoftware/module-cms-content-types-nuxt) (`@liberusoftware/module-cms-content-types-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Content type definitions** | Expose composable and Vue 3 component for `content type definitions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-content-types.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Typed field groups and repeaters** | Expose composable and Vue 3 component for `typed field groups and repeaters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-content-types.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Validation and reference rules** | Expose composable and Vue 3 component for `validation and reference rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-content-types.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Schema versioning and migrations** | Expose composable and Vue 3 component for `schema versioning and migrations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-content-types.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **API projection rules** | Expose composable and Vue 3 component for `api projection rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-content-types.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

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
