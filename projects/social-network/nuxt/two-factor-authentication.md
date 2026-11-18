# Social Network: Two Factor Authentication Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#two-factor-authentication). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-social-network-two-factor-authentication-nuxt`
**Matching domain module:** `two-factor-authentication`
**Application:** Social Network
**Source feature:** [Two Factor Authentication](../features/two-factor-authentication.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/two-factor-authentication.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `two-factor-authentication` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **TOTP enrollment:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Recovery codes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Enforcement:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Trusted devices:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Recovery:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Audit:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-social-network-two-factor-authentication-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `totp-enrollment`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `recovery-codes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `enforcement`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `trusted-devices`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `recovery`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `audit`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `two-factor-authentication` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-social-network-nuxt-vue`](https://github.com/liberusoftware/project-social-network-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/two-factor-authentication.md)) |
| Capability Nuxt module skeleton | [`module-two-factor-authentication-nuxt`](https://github.com/liberusoftware/module-two-factor-authentication-nuxt) (`@liberusoftware/module-two-factor-authentication-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **TOTP enrollment** | Expose composable and Vue 3 component for `totp enrollment` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/two-factor-authentication.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Recovery codes** | Expose composable and Vue 3 component for `recovery codes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/two-factor-authentication.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Enforcement** | Expose composable and Vue 3 component for `enforcement` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/two-factor-authentication.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Trusted devices** | Expose composable and Vue 3 component for `trusted devices` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/two-factor-authentication.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Recovery** | Expose composable and Vue 3 component for `recovery` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/two-factor-authentication.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Audit** | Expose composable and Vue 3 component for `audit` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/two-factor-authentication.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [TwoFactorRecovery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/two-factor-authentication/src/Contracts/TwoFactorRecovery.php) | `public function recover(Authenticatable $subject, Authenticatable $administrator, string $reason): void` |

**Observed route declarations:**

[modules/two-factor-authentication-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/two-factor-authentication-api/routes/api.php)

```php
Route::prefix('api/v1/two-factor-authentication')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('two-factor-authentication-api.status');
```
<!-- layer-implementation-plan:end -->
