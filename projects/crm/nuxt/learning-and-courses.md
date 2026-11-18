# CRM: Learning and Courses Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#learning-and-courses). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-learning-and-courses-nuxt`
**Matching domain module:** `crm-learning-and-courses`
**Application:** CRM
**Source feature:** [Learning and Courses](../features/learning-and-courses.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/learning-and-courses.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-learning-and-courses` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Courses:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Lessons:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Media:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cohorts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Enrollment:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Access:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Progress:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Assessments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Certificates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Drip schedules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Product/contract entitlements:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-learning-and-courses-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `courses`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `lessons`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `media`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cohorts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `enrollment`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `access`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `progress`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `assessments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `certificates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `drip-schedules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `product-contract-entitlements`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-learning-and-courses` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/learning-and-courses.md)) |
| Capability Nuxt module skeleton | [`module-crm-learning-and-courses-nuxt`](https://github.com/liberusoftware/module-crm-learning-and-courses-nuxt) (`@liberusoftware/module-crm-learning-and-courses-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Courses** | Expose composable and Vue 3 component for `courses` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/learning-and-courses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Lessons** | Expose composable and Vue 3 component for `lessons` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/learning-and-courses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Media** | Expose composable and Vue 3 component for `media` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/learning-and-courses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Cohorts** | Expose composable and Vue 3 component for `cohorts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/learning-and-courses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Enrollment** | Expose composable and Vue 3 component for `enrollment` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/learning-and-courses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Access** | Expose composable and Vue 3 component for `access` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/learning-and-courses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Progress** | Expose composable and Vue 3 component for `progress` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/learning-and-courses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Assessments** | Expose composable and Vue 3 component for `assessments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/learning-and-courses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Certificates** | Expose composable and Vue 3 component for `certificates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/learning-and-courses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Drip schedules** | Expose composable and Vue 3 component for `drip schedules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/learning-and-courses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Product/contract entitlements** | Expose composable and Vue 3 component for `product/contract entitlements` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/learning-and-courses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [LearningQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Queries/LearningQuery.php) | `public function forTeam(int $teamId)`<br>`public function records(int $teamId, int $enrollmentId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCourse.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Actions/CreateCourse.php) | `public function __construct(private readonly LearningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): LearningCourse` |
| [EnrollLearner.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Actions/EnrollLearner.php) | `public function __construct(private readonly LearningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, LearningCourse $course, array $input): LearningEnrollment` |
| [RecordLearningProgress.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Actions/RecordLearningProgress.php) | `public function __construct(private readonly LearningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, LearningEnrollment $enrollment, array $input): LearningRecord` |
| [LearningPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Services/LearningPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [LearningCourse.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Models/LearningCourse.php) | No literal fillable array detected; inspect the model and API schema. |
| [LearningEnrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Models/LearningEnrollment.php) | No literal fillable array detected; inspect the model and API schema. |
| [LearningLesson.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Models/LearningLesson.php) | No literal fillable array detected; inspect the model and API schema. |
| [LearningRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Models/LearningRecord.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [LearningController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses-api/src/Http/Controllers/LearningController.php) | `public function index(Request $r, LearningQuery $q): JsonResponse`<br>`public function store(Request $r, CreateCourse $a): JsonResponse`<br>`public function enroll(Request $r, LearningCourse $course, EnrollLearner $a): JsonResponse`<br>`public function record(Request $r, LearningEnrollment $enrollment, RecordLearningProgress $a): JsonResponse`<br>`public function records(Request $r, LearningEnrollment $enrollment, LearningQuery $q): JsonResponse` |
<!-- layer-implementation-plan:end -->
