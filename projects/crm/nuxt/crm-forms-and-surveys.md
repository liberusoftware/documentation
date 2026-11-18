# CRM: Crm Forms And Surveys Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-forms-and-surveys). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-forms-and-surveys-nuxt`
**Matching domain module:** `crm-forms-and-surveys`
**Application:** CRM
**Source feature:** [Crm Forms And Surveys](../features/crm-forms-and-surveys.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-forms-and-surveys.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-forms-and-surveys` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Drag-and-drop schemas:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Conditional fields:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Progressive profiling:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Validation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Spam controls:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Consent:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Hidden attribution:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Embedding:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Submissions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Follow-up:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-forms-and-surveys-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `drag-and-drop-schemas`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `conditional-fields`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `progressive-profiling`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `validation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `spam-controls`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `consent`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `hidden-attribution`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `embedding`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `submissions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `follow-up`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-forms-and-surveys` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-forms-and-surveys.md)) |
| Capability Nuxt module skeleton | [`module-crm-forms-and-surveys-nuxt`](https://github.com/liberusoftware/module-crm-forms-and-surveys-nuxt) (`@liberusoftware/module-crm-forms-and-surveys-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Drag-and-drop schemas** | Expose composable and Vue 3 component for `drag-and-drop schemas` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-forms-and-surveys.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Conditional fields** | Expose composable and Vue 3 component for `conditional fields` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-forms-and-surveys.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Progressive profiling** | Expose composable and Vue 3 component for `progressive profiling` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-forms-and-surveys.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Validation** | Expose composable and Vue 3 component for `validation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-forms-and-surveys.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Spam controls** | Expose composable and Vue 3 component for `spam controls` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-forms-and-surveys.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Consent** | Expose composable and Vue 3 component for `consent` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-forms-and-surveys.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Hidden attribution** | Expose composable and Vue 3 component for `hidden attribution` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-forms-and-surveys.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Embedding** | Expose composable and Vue 3 component for `embedding` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-forms-and-surveys.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Submissions** | Expose composable and Vue 3 component for `submissions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-forms-and-surveys.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Follow-up** | Expose composable and Vue 3 component for `follow-up` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-forms-and-surveys.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [FormQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Queries/FormQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateSurveyForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Actions/CreateSurveyForm.php) | `public function __construct(private readonly FormPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): SurveyForm` |
| [RecordFollowUp.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Actions/RecordFollowUp.php) | `public function __construct(private readonly FormPolicy $policy)`<br>`public function execute(int $teamId, int $userId, FormSubmission $submission, array $input): FormFollowUp` |
| [SubmitForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Actions/SubmitForm.php) | `public function __construct(private readonly FormPolicy $policy)`<br>`public function execute(int $teamId, int $userId, SurveyForm $form, array $input): FormSubmission` |
| [FormPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Services/FormPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FormFollowUp.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Models/FormFollowUp.php) | No literal fillable array detected; inspect the model and API schema. |
| [FormSubmission.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Models/FormSubmission.php) | No literal fillable array detected; inspect the model and API schema. |
| [SurveyForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Models/SurveyForm.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [FormsController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys-api/src/Http/Controllers/FormsController.php) | `public function index(Request $r, FormQuery $q): JsonResponse`<br>`public function store(Request $r, CreateSurveyForm $a): JsonResponse`<br>`public function submit(Request $r, SurveyForm $form, SubmitForm $a): JsonResponse`<br>`public function followUp(Request $r, FormSubmission $submission, RecordFollowUp $a): JsonResponse` |
<!-- layer-implementation-plan:end -->
