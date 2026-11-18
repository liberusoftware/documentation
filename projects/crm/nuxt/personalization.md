# CRM: Personalization Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#personalization). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-personalization-nuxt`
**Matching domain module:** `crm-personalization`
**Application:** CRM
**Source feature:** [Personalization](../features/personalization.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/personalization.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-personalization` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Rules and decisioning for content:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Offer:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Channel:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Send time:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Locale:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Lifecycle:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Customer attributes with holdouts and fallback:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-personalization-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `rules-and-decisioning-for-content`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `offer`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `channel`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `send-time`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `locale`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `lifecycle`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `customer-attributes-with-holdouts-and-fallback`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-personalization` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/personalization.md)) |
| Capability Nuxt module skeleton | [`module-crm-personalization-nuxt`](https://github.com/liberusoftware/module-crm-personalization-nuxt) (`@liberusoftware/module-crm-personalization-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Rules and decisioning for content** | Expose composable and Vue 3 component for `rules and decisioning for content` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/personalization.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Offer** | Expose composable and Vue 3 component for `offer` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/personalization.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Channel** | Expose composable and Vue 3 component for `channel` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/personalization.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Send time** | Expose composable and Vue 3 component for `send time` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/personalization.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Locale** | Expose composable and Vue 3 component for `locale` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/personalization.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Lifecycle** | Expose composable and Vue 3 component for `lifecycle` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/personalization.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Customer attributes with holdouts and fallback** | Expose composable and Vue 3 component for `customer attributes with holdouts and fallback` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/personalization.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PersonalizationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Queries/PersonalizationQuery.php) | `public function rules(int $teamId)`<br>`public function decisions(int $teamId)`<br>`public function outcomes(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePersonalizationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Actions/CreatePersonalizationRule.php) | `public function __construct(private readonly PersonalizationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PersonalizationRule` |
| [DecidePersonalization.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Actions/DecidePersonalization.php) | `public function __construct(private readonly PersonalizationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PersonalizationDecision` |
| [RecordPersonalizationOutcome.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Actions/RecordPersonalizationOutcome.php) | `public function __construct(private readonly PersonalizationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PersonalizationOutcome` |
| [UpdatePersonalizationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Actions/UpdatePersonalizationRule.php) | `public function __construct(private readonly PersonalizationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $ruleId, array $input): PersonalizationRule` |
| [PersonalizationPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Services/PersonalizationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PersonalizationDecision.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Models/PersonalizationDecision.php) | No literal fillable array detected; inspect the model and API schema. |
| [PersonalizationOutcome.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Models/PersonalizationOutcome.php) | No literal fillable array detected; inspect the model and API schema. |
| [PersonalizationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Models/PersonalizationRule.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [PersonalizationController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization-api/src/Http/Controllers/PersonalizationController.php) | `public function rules(Request $r, PersonalizationQuery $q)`<br>`public function rule(Request $r, CreatePersonalizationRule $a)`<br>`public function decision(Request $r, DecidePersonalization $a)`<br>`public function outcome(Request $r, RecordPersonalizationOutcome $a)` |

**Observed route declarations:**

[modules/crm-personalization-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/personalization')->group(function (): void {
Route::get('/rules', [PersonalizationController::class, 'rules']);
Route::post('/rules', [PersonalizationController::class, 'rule']);
Route::post('/decisions', [PersonalizationController::class, 'decision']);
Route::post('/outcomes', [PersonalizationController::class, 'outcome']);
```
<!-- layer-implementation-plan:end -->
