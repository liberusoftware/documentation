# CMS: Cms Forms Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-forms). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-cms-forms-nuxt`
**Matching domain module:** `cms-forms`
**Application:** CMS
**Source feature:** [Cms Forms](../features/cms-forms.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/cms-forms.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `cms-forms` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Form schema builder:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Multi-step and conditional fields:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Spam and rate-limit protection:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Consent and retention tracking:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Submission inbox and exports:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-cms-forms-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `form-schema-builder`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `multi-step-and-conditional-fields`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `spam-and-rate-limit-protection`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `consent-and-retention-tracking`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `submission-inbox-and-exports`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `cms-forms` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/cms-forms.md)) |
| Capability Nuxt module skeleton | [`module-cms-forms-nuxt`](https://github.com/liberusoftware/module-cms-forms-nuxt) (`@liberusoftware/module-cms-forms-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Form schema builder** | Expose composable and Vue 3 component for `form schema builder` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-forms.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Multi-step and conditional fields** | Expose composable and Vue 3 component for `multi-step and conditional fields` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-forms.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Spam and rate-limit protection** | Expose composable and Vue 3 component for `spam and rate-limit protection` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-forms.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Consent and retention tracking** | Expose composable and Vue 3 component for `consent and retention tracking` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-forms.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Submission inbox and exports** | Expose composable and Vue 3 component for `submission inbox and exports` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-forms.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

### Observed domain and transport source evidence

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Form.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/Models/Form.php) | `name`, `slug`, `fields`, `team_id` |
| [FormSubmission.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/Models/FormSubmission.php) | `form_id`, `data`, `meta`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [FormSubmissionController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/src/Http/Controllers/FormSubmissionController.php) | `public function __construct( private EventBusInterface $events, private SubmissionValidator $validator, )`<br>`public function __invoke(Request $request, string $slug): JsonResponse` |

**Observed route declarations:**

[modules/cms-forms/routes/web.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-forms/routes/web.php)

```php
Route::post('/forms/{slug}', FormSubmissionController::class)
```
<!-- layer-implementation-plan:end -->
