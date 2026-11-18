# CMS: Migration Framework Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#migration-framework). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-migration-framework-nuxt`
**Matching domain module:** `cms-migration-framework`
**Application:** CMS
**Source feature:** [Migration Framework](../features/migration-framework.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/migration-framework.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `cms-migration-framework` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Source adapters:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Inventories:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Mapping:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dry run:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Transforms:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Identity/media/link resolution:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Batches:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Resume:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-migration-framework-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `source-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `inventories`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `mapping`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dry-run`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `transforms`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `identity-media-link-resolution`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `batches`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `resume`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reconciliation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `cms-migration-framework` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/migration-framework.md)) |
| Capability Nuxt module skeleton | [`module-cms-migration-framework-nuxt`](https://github.com/liberusoftware/module-cms-migration-framework-nuxt) (`@liberusoftware/module-cms-migration-framework-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Source adapters** | Expose composable and Vue 3 component for `source adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/migration-framework.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Inventories** | Expose composable and Vue 3 component for `inventories` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/migration-framework.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Mapping** | Expose composable and Vue 3 component for `mapping` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/migration-framework.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Dry run** | Expose composable and Vue 3 component for `dry run` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/migration-framework.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Transforms** | Expose composable and Vue 3 component for `transforms` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/migration-framework.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Identity/media/link resolution** | Expose composable and Vue 3 component for `identity/media/link resolution` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/migration-framework.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Batches** | Expose composable and Vue 3 component for `batches` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/migration-framework.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Resume** | Expose composable and Vue 3 component for `resume` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/migration-framework.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Reconciliation** | Expose composable and Vue 3 component for `reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/migration-framework.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [MigrationFrameworkService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-migration-framework/src/Services/MigrationFrameworkService.php) | `public function start(string $source, array $options = [], ?int $teamId = null): MigrationJob`<br>`public function add(MigrationJob $job, string $recordType, string $sourceId, array $payload = []): MigrationRecord`<br>`public function process(MigrationRecord $record, bool $success, ?string $failureReason = null): MigrationRecord`<br>`public function complete(MigrationJob $job): MigrationJob` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MigrationJob.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-migration-framework/src/Models/MigrationJob.php) | `public_id`, `source`, `status`, `total_records`, `processed_records`, `failed_records`, `options`, `failure_reason`, `started_at`, `completed_at`, `team_id` |
| [MigrationRecord.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-migration-framework/src/Models/MigrationRecord.php) | `job_id`, `record_type`, `source_id`, `status`, `payload`, `failure_reason`, `processed_at`, `team_id` |
<!-- layer-implementation-plan:end -->
