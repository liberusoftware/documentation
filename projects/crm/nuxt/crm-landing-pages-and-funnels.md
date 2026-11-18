# CRM: Crm Landing Pages And Funnels Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-landing-pages-and-funnels). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-landing-pages-and-funnels-nuxt`
**Matching domain module:** `crm-landing-pages-and-funnels`
**Application:** CRM
**Source feature:** [Crm Landing Pages And Funnels](../features/crm-landing-pages-and-funnels.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-landing-pages-and-funnels.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-landing-pages-and-funnels` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Multi-step funnels:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Landing/thank-you pages:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Templates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Domains:** page/component/composable/API-action behavior for this module's authorized workflow.
- **SEO metadata:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Personalization:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Forms:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Order links:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Preview:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Publish:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Conversion tracking:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-landing-pages-and-funnels-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `multi-step-funnels`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `landing-thank-you-pages`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `templates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `domains`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `seo-metadata`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `personalization`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `forms`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `order-links`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `preview`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `publish`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `conversion-tracking`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-landing-pages-and-funnels` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-landing-pages-and-funnels.md)) |
| Capability Nuxt module skeleton | [`module-crm-landing-pages-and-funnels-nuxt`](https://github.com/liberusoftware/module-crm-landing-pages-and-funnels-nuxt) (`@liberusoftware/module-crm-landing-pages-and-funnels-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Multi-step funnels** | Expose composable and Vue 3 component for `multi-step funnels` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-landing-pages-and-funnels.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Landing/thank-you pages** | Expose composable and Vue 3 component for `landing/thank-you pages` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-landing-pages-and-funnels.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Templates** | Expose composable and Vue 3 component for `templates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-landing-pages-and-funnels.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Domains** | Expose composable and Vue 3 component for `domains` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-landing-pages-and-funnels.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **SEO metadata** | Expose composable and Vue 3 component for `seo metadata` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-landing-pages-and-funnels.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Personalization** | Expose composable and Vue 3 component for `personalization` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-landing-pages-and-funnels.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Forms** | Expose composable and Vue 3 component for `forms` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-landing-pages-and-funnels.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Order links** | Expose composable and Vue 3 component for `order links` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-landing-pages-and-funnels.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Preview** | Expose composable and Vue 3 component for `preview` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-landing-pages-and-funnels.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Publish** | Expose composable and Vue 3 component for `publish` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-landing-pages-and-funnels.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Conversion tracking** | Expose composable and Vue 3 component for `conversion tracking` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-landing-pages-and-funnels.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [FunnelQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels/src/Queries/FunnelQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddFunnelPage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels/src/Actions/AddFunnelPage.php) | `public function __construct(private readonly FunnelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Funnel $funnel, array $input): FunnelPage` |
| [CreateFunnel.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels/src/Actions/CreateFunnel.php) | `public function __construct(private readonly FunnelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Funnel` |
| [PublishFunnel.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels/src/Actions/PublishFunnel.php) | `public function __construct(private readonly FunnelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Funnel $funnel, array $input): Funnel` |
| [RecordFunnelEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels/src/Actions/RecordFunnelEvent.php) | `public function __construct(private readonly FunnelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Funnel $funnel, array $input): FunnelEvent` |
| [FunnelPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels/src/Services/FunnelPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Funnel.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels/src/Models/Funnel.php) | No literal fillable array detected; inspect the model and API schema. |
| [FunnelEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels/src/Models/FunnelEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [FunnelPage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels/src/Models/FunnelPage.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [FunnelController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-landing-pages-and-funnels-api/src/Http/Controllers/FunnelController.php) | `public function index(Request $r, FunnelQuery $q): JsonResponse`<br>`public function store(Request $r, CreateFunnel $a): JsonResponse`<br>`public function page(Request $r, Funnel $funnel, AddFunnelPage $a): JsonResponse`<br>`public function publish(Request $r, Funnel $funnel, PublishFunnel $a): JsonResponse`<br>`public function event(Request $r, Funnel $funnel, RecordFunnelEvent $a): JsonResponse` |
<!-- layer-implementation-plan:end -->
