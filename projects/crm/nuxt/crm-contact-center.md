# CRM: Crm Contact Center Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-contact-center). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-contact-center-nuxt`
**Matching domain module:** `crm-contact-center`
**Application:** CRM
**Source feature:** [Crm Contact Center](../features/crm-contact-center.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-contact-center.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-contact-center` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Agent presence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Capacity:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Skills:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Routing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Supervisor views:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Whisper/barge policy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Quality review:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Workforce demand:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Queue SLA:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Overflow:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-contact-center-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `agent-presence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `capacity`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `skills`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `routing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `supervisor-views`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `whisper-barge-policy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `quality-review`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `workforce-demand`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `queue-sla`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `overflow`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-contact-center` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-contact-center.md)) |
| Capability Nuxt module skeleton | [`module-crm-contact-center-nuxt`](https://github.com/liberusoftware/module-crm-contact-center-nuxt) (`@liberusoftware/module-crm-contact-center-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Agent presence** | Expose composable and Vue 3 component for `agent presence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-contact-center.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Capacity** | Expose composable and Vue 3 component for `capacity` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-contact-center.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Skills** | Expose composable and Vue 3 component for `skills` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-contact-center.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Routing** | Expose composable and Vue 3 component for `routing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-contact-center.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Supervisor views** | Expose composable and Vue 3 component for `supervisor views` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-contact-center.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Whisper/barge policy** | Expose composable and Vue 3 component for `whisper/barge policy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-contact-center.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Quality review** | Expose composable and Vue 3 component for `quality review` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-contact-center.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Workforce demand** | Expose composable and Vue 3 component for `workforce demand` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-contact-center.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Queue SLA** | Expose composable and Vue 3 component for `queue sla` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-contact-center.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Overflow** | Expose composable and Vue 3 component for `overflow` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-contact-center.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ContactCenterQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Queries/ContactCenterQuery.php) | `public function agents(int $teamId): Builder`<br>`public function supervisorView(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ReviewQuality.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Actions/ReviewQuality.php) | `public function execute(int $teamId, int $eventId, int $reviewerId, array $scorecard): ContactCenterEvent` |
| [RouteInteraction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Actions/RouteInteraction.php) | `public function execute(int $teamId, string $queueKey, string $requiredSkill, int $slaSeconds = 300): ContactCenterEvent` |
| [SetAgentPresence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Actions/SetAgentPresence.php) | `public function execute(int $teamId, int $userId, string $presence, int $capacity = 1, array $skills = []): ContactCenterAgent` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ContactCenterAgent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Models/ContactCenterAgent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ContactCenterEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Models/ContactCenterEvent.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ContactCenterController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center-api/src/Http/Controllers/ContactCenterController.php) | `public function __construct(private readonly ContactCenterQuery $query)`<br>`public function agents(): JsonResponse`<br>`public function presence(SetAgentPresence $a): JsonResponse`<br>`public function route(RouteInteraction $a): JsonResponse`<br>`public function supervisor(): JsonResponse` |

**Observed route declarations:**

[modules/crm-contact-center-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/contact-center')->group(function (): void {
Route::get('agents', [ContactCenterController::class, 'agents']);
Route::post('presence', [ContactCenterController::class, 'presence']);
Route::post('route', [ContactCenterController::class, 'route']);
Route::get('supervisor', [ContactCenterController::class, 'supervisor']);
```
<!-- layer-implementation-plan:end -->
