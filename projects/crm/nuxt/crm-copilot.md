# CRM: CRM Copilot Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-copilot). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-copilot-nuxt`
**Matching domain module:** `crm-copilot`
**Application:** CRM
**Source feature:** [CRM Copilot](../features/crm-copilot.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-copilot.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-copilot` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Permission-bounded search:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Summaries:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Preparation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Drafting:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Record updates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Task creation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Action confirmation using the Automation AI Gateway:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-copilot-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `permission-bounded-search`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `summaries`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `preparation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `drafting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `record-updates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `task-creation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `action-confirmation-using-the-automation-ai-gateway`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-copilot` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-copilot.md)) |
| Capability Nuxt module skeleton | [`module-crm-copilot-nuxt`](https://github.com/liberusoftware/module-crm-copilot-nuxt) (`@liberusoftware/module-crm-copilot-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Permission-bounded search** | Expose composable and Vue 3 component for `permission-bounded search` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-copilot.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Summaries** | Expose composable and Vue 3 component for `summaries` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-copilot.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Preparation** | Expose composable and Vue 3 component for `preparation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-copilot.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Drafting** | Expose composable and Vue 3 component for `drafting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-copilot.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Record updates** | Expose composable and Vue 3 component for `record updates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-copilot.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Task creation** | Expose composable and Vue 3 component for `task creation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-copilot.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Action confirmation using the Automation AI Gateway** | Expose composable and Vue 3 component for `action confirmation using the automation ai gateway` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-copilot.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CopilotQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Queries/CopilotQuery.php) | `public function requests(int $teamId, int $userId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AskCopilot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Actions/AskCopilot.php) | `public function __construct(private readonly CopilotPolicy $policy, private readonly AutomationGateway $gateway)`<br>`public function execute(int $teamId, int $userId, array $input): CopilotRequest` |
| [ConfirmCopilotAction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Actions/ConfirmCopilotAction.php) | `public function __construct(private readonly CopilotPolicy $policy)`<br>`public function execute(int $teamId, int $userId, CopilotAction $action): CopilotAction` |
| [ProposeCopilotAction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Actions/ProposeCopilotAction.php) | `public function __construct(private readonly CopilotPolicy $policy)`<br>`public function execute(int $teamId, int $userId, CopilotRequest $request, array $input): CopilotAction` |
| [AutomationGateway.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Contracts/AutomationGateway.php) | `public function complete(string $instruction, array $context): array` |
| [CopilotPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Services/CopilotPolicy.php) | `public function canUse(int $teamId, int $userId): bool` |
| [NullAutomationGateway.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Services/NullAutomationGateway.php) | `public function complete(string $instruction, array $context): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CopilotAction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Models/CopilotAction.php) | No literal fillable array detected; inspect the model and API schema. |
| [CopilotRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot/src/Models/CopilotRequest.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CopilotController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot-api/src/Http/Controllers/CopilotController.php) | `public function __construct(private readonly CopilotQuery $query)`<br>`public function ask(AskCopilot $action): JsonResponse`<br>`public function propose(CopilotRequest $request, ProposeCopilotAction $action): JsonResponse`<br>`public function confirm(CopilotAction $action, ConfirmCopilotAction $confirm): JsonResponse`<br>`public function requests(): JsonResponse` |

**Observed route declarations:**

[modules/crm-copilot-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-copilot-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/crm-copilot')->group(function (): void {
Route::post('ask', [CopilotController::class, 'ask']);
Route::post('requests/{request}/actions', [CopilotController::class, 'propose']);
Route::post('actions/{action}/confirm', [CopilotController::class, 'confirm']);
Route::get('requests', [CopilotController::class, 'requests']);
```
<!-- layer-implementation-plan:end -->
