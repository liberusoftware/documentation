# CRM: Crm Proposals And Quotes Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-proposals-and-quotes). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-proposals-and-quotes-nuxt`
**Matching domain module:** `crm-proposals-and-quotes`
**Application:** CRM
**Source feature:** [Crm Proposals And Quotes](../features/crm-proposals-and-quotes.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-proposals-and-quotes.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-proposals-and-quotes` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Branded templates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Sections:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Scope:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Line items:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Optional choices:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Versions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Comments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approvals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Delivery:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Engagement:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Acceptance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Expiry:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-proposals-and-quotes-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `branded-templates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sections`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `scope`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `line-items`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `optional-choices`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `versions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `comments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approvals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `delivery`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `engagement`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `acceptance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `expiry`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-proposals-and-quotes` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-proposals-and-quotes.md)) |
| Capability Nuxt module skeleton | [`module-crm-proposals-and-quotes-nuxt`](https://github.com/liberusoftware/module-crm-proposals-and-quotes-nuxt) (`@liberusoftware/module-crm-proposals-and-quotes-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Branded templates** | Expose composable and Vue 3 component for `branded templates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-proposals-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Sections** | Expose composable and Vue 3 component for `sections` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-proposals-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Scope** | Expose composable and Vue 3 component for `scope` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-proposals-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Line items** | Expose composable and Vue 3 component for `line items` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-proposals-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Optional choices** | Expose composable and Vue 3 component for `optional choices` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-proposals-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Versions** | Expose composable and Vue 3 component for `versions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-proposals-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Comments** | Expose composable and Vue 3 component for `comments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-proposals-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Approvals** | Expose composable and Vue 3 component for `approvals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-proposals-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Delivery** | Expose composable and Vue 3 component for `delivery` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-proposals-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Engagement** | Expose composable and Vue 3 component for `engagement` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-proposals-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Acceptance** | Expose composable and Vue 3 component for `acceptance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-proposals-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Expiry** | Expose composable and Vue 3 component for `expiry` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-proposals-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ProposalQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Queries/ProposalQuery.php) | `public function templates(int $teamId)`<br>`public function proposals(int $teamId)`<br>`public function versions(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddProposalComment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/AddProposalComment.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProposalEvent` |
| [ChangeProposalStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/ChangeProposalStatus.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $proposalId, string $status): Proposal` |
| [CreateProposal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/CreateProposal.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Proposal` |
| [CreateProposalTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/CreateProposalTemplate.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProposalTemplate` |
| [CreateProposalVersion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/CreateProposalVersion.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProposalVersion` |
| [UpdateProposal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/UpdateProposal.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $proposalId, array $input): Proposal` |
| [ProposalPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Services/ProposalPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Proposal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/Proposal.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProposalEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/ProposalEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProposalTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/ProposalTemplate.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProposalVersion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/ProposalVersion.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProposalsAndQuotesController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes-api/src/Http/Controllers/ProposalsAndQuotesController.php) | `public function templates(Request $r, ProposalQuery $q)`<br>`public function template(Request $r, CreateProposalTemplate $a)`<br>`public function proposals(Request $r, ProposalQuery $q)`<br>`public function proposal(Request $r, CreateProposal $a)`<br>`public function version(Request $r, CreateProposalVersion $a)`<br>`public function status(Request $r, int $proposal, string $status, ChangeProposalStatus $a)`<br>`public function comment(Request $r, AddProposalComment $a)` |

**Observed route declarations:**

[modules/crm-proposals-and-quotes-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/proposals-and-quotes')->group(function (): void {
Route::get('/templates', [ProposalsAndQuotesController::class, 'templates']);
Route::post('/templates', [ProposalsAndQuotesController::class, 'template']);
Route::get('/proposals', [ProposalsAndQuotesController::class, 'proposals']);
Route::post('/proposals', [ProposalsAndQuotesController::class, 'proposal']);
Route::post('/versions', [ProposalsAndQuotesController::class, 'version']);
Route::post('/proposals/{proposal}/{status}', [ProposalsAndQuotesController::class, 'status'])->whereIn('status', ['approved', 'delivered', 'accepted', 'rejected', 'expired']);
Route::post('/comments', [ProposalsAndQuotesController::class, 'comment']);
```
<!-- layer-implementation-plan:end -->
