# CMS: Cms Field System Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-field-system). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-cms-field-system-nuxt`
**Matching domain module:** `cms-field-system`
**Application:** CMS
**Source feature:** [Cms Field System](../features/cms-field-system.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/cms-field-system.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `cms-field-system` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Reusable typed fields:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cardinality:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Defaults:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Validation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Computed fields:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Conditional fields:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Field groups:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Schema migrations:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-cms-field-system-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `reusable-typed-fields`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cardinality`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `defaults`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `validation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `computed-fields`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `conditional-fields`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `field-groups`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `schema-migrations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `cms-field-system` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/cms-field-system.md)) |
| Capability Nuxt module skeleton | [`module-cms-field-system-nuxt`](https://github.com/liberusoftware/module-cms-field-system-nuxt) (`@liberusoftware/module-cms-field-system-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Reusable typed fields** | Expose composable and Vue 3 component for `reusable typed fields` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-field-system.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Cardinality** | Expose composable and Vue 3 component for `cardinality` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-field-system.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Defaults** | Expose composable and Vue 3 component for `defaults` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-field-system.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Validation** | Expose composable and Vue 3 component for `validation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-field-system.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Computed fields** | Expose composable and Vue 3 component for `computed fields` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-field-system.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Conditional fields** | Expose composable and Vue 3 component for `conditional fields` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-field-system.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Field groups** | Expose composable and Vue 3 component for `field groups` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-field-system.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Schema migrations** | Expose composable and Vue 3 component for `schema migrations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-field-system.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [FieldSystemService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-field-system/src/Services/FieldSystemService.php) | `public function __construct(private FieldTypeRegistryInterface $types)`<br>`public function saveSchema(?int $teamId, string $key, string $name, array $fields, ?string $reason = null): FieldSchema`<br>`public function validateData(FieldSchema $schema, array $data): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FieldSchema.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-field-system/src/Models/FieldSchema.php) | `team_id`, `key`, `name`, `version`, `fields`, `history` |

| Observed API controller | Handler signatures |
| --- | --- |
| [FieldSchemaController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-field-system-api/src/Http/Controllers/FieldSchemaController.php) | `public function __construct(private FieldSchemaQuery $schemas)`<br>`public function show(string $type): JsonResource` |
<!-- layer-implementation-plan:end -->
