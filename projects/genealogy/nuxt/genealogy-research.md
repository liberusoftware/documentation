# Genealogy: Genealogy Research Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-research). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-genealogy-genealogy-research-nuxt`
**Matching domain module:** `genealogy-research`
**Application:** Genealogy
**Source feature:** [Genealogy Research](../features/genealogy-research.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/genealogy-research.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `genealogy-research` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Questions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Plans:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tasks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Logs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Correspondence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Negative searches:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Findings:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-genealogy-genealogy-research-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `questions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `plans`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tasks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `logs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `correspondence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `negative-searches`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `findings`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `genealogy-research` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-genealogy-nuxt-vue`](https://github.com/liberusoftware/project-genealogy-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/genealogy-research.md)) |
| Capability Nuxt module skeleton | [`module-genealogy-research-nuxt`](https://github.com/liberusoftware/module-genealogy-research-nuxt) (`@liberusoftware/module-genealogy-research-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Questions** | Expose composable and Vue 3 component for `questions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-research.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Plans** | Expose composable and Vue 3 component for `plans` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-research.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Tasks** | Expose composable and Vue 3 component for `tasks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-research.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Logs** | Expose composable and Vue 3 component for `logs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-research.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Correspondence** | Expose composable and Vue 3 component for `correspondence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-research.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Negative searches** | Expose composable and Vue 3 component for `negative searches` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-research.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Findings** | Expose composable and Vue 3 component for `findings` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-research.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateChecklist.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/CreateChecklist.php) | `public function execute(Model $user, string $name, ?ChecklistTemplate $template = null, array $attributes = []): UserChecklist` |
| [CreateResearchEntry.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/CreateResearchEntry.php) | `public function execute(array $attributes): ResearchEntry`<br>`public function validate(array $values): void` |
| [CreateResearchProject.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/CreateResearchProject.php) | `public function execute(array $attributes): ResearchProject`<br>`public function validate(array $values): void` |
| [DeleteResearchEntry.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/DeleteResearchEntry.php) | `public function execute(ResearchEntry $entry): void` |
| [DeleteResearchProject.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/DeleteResearchProject.php) | `public function execute(ResearchProject $project): void` |
| [UpdateResearchEntry.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/UpdateResearchEntry.php) | `public function execute(ResearchEntry $entry, array $attributes): ResearchEntry` |
| [UpdateResearchProject.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/UpdateResearchProject.php) | `public function execute(ResearchProject $project, array $attributes): ResearchProject` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ChecklistTemplate.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Models/ChecklistTemplate.php) | `team_id`, `created_by`, `name`, `description`, `category`, `is_public`, `is_default`, `tags`, `difficulty_level`, `estimated_time` |
| [ChecklistTemplateItem.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Models/ChecklistTemplateItem.php) | `checklist_template_id`, `title`, `description`, `sort_order`, `category`, `is_required`, `estimated_time`, `resources`, `tips` |
| [ResearchEntry.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Models/ResearchEntry.php) | `team_id`, `research_project_id`, `kind`, `title`, `body`, `status`, `due_date`, `completed_at`, `metadata` |
| [ResearchProject.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Models/ResearchProject.php) | `team_id`, `name`, `status`, `metadata` |
| [UserChecklist.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Models/UserChecklist.php) | `team_id`, `user_id`, `checklist_template_id`, `name`, `description`, `subject_type`, `subject_id`, `status`, `started_at`, `completed_at`, `notes`, `priority`, `due_date` |
| [UserChecklistItem.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Models/UserChecklistItem.php) | `checklist_id`, `template_item_id`, `title`, `description`, `sort_order`, `is_completed`, `completed_at`, `notes`, `estimated_time`, `actual_time`, `resources`, `tips` |
<!-- layer-implementation-plan:end -->
