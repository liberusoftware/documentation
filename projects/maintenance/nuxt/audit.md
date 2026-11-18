# Maintenance: Audit Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#audit). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-maintenance-audit-nuxt`
**Matching domain module:** `audit`
**Application:** Maintenance
**Source feature:** [Audit](../features/audit.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/audit.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `audit` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Actor:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tenant:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Request context:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Material changes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Privileged actions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Retention:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tamper evidence:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-maintenance-audit-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `actor`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tenant`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `request-context`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `material-changes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `privileged-actions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `retention`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tamper-evidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `audit` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-maintenance-nuxt-vue`](https://github.com/liberusoftware/project-maintenance-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/audit.md)) |
| Capability Nuxt module skeleton | [`module-audit-nuxt`](https://github.com/liberusoftware/module-audit-nuxt) (`@liberusoftware/module-audit-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Actor** | Expose composable and Vue 3 component for `actor` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/audit.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Tenant** | Expose composable and Vue 3 component for `tenant` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/audit.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Request context** | Expose composable and Vue 3 component for `request context` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/audit.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Material changes** | Expose composable and Vue 3 component for `material changes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/audit.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Privileged actions** | Expose composable and Vue 3 component for `privileged actions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/audit.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Retention** | Expose composable and Vue 3 component for `retention` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/audit.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Tamper evidence** | Expose composable and Vue 3 component for `tamper evidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/audit.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AuditRecorder.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/audit/src/Contracts/AuditRecorder.php) | `public function record(string $event, string $subjectType, string\|int\|null $subjectId, array $before, array $after, AuditContext $context): void` |

**Observed route declarations:**

[modules/audit-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/audit-api/routes/api.php)

```php
Route::prefix('api/v1/audit')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('audit-api.status');
```
<!-- layer-implementation-plan:end -->
