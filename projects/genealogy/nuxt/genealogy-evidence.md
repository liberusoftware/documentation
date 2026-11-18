# Genealogy: Genealogy Evidence Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-evidence). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-genealogy-genealogy-evidence-nuxt`
**Matching domain module:** `genealogy-evidence`
**Application:** Genealogy
**Source feature:** [Genealogy Evidence](../features/genealogy-evidence.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/genealogy-evidence.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `genealogy-evidence` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Sources:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Repositories:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Citations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Extracts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Assertions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Confidence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Proof conclusions:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-genealogy-genealogy-evidence-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `sources`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `repositories`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `citations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `extracts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `assertions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `confidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `proof-conclusions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `genealogy-evidence` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-genealogy-nuxt-vue`](https://github.com/liberusoftware/project-genealogy-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/genealogy-evidence.md)) |
| Capability Nuxt module skeleton | [`module-genealogy-evidence-nuxt`](https://github.com/liberusoftware/module-genealogy-evidence-nuxt) (`@liberusoftware/module-genealogy-evidence-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Sources** | Expose composable and Vue 3 component for `sources` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-evidence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Repositories** | Expose composable and Vue 3 component for `repositories` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-evidence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Citations** | Expose composable and Vue 3 component for `citations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-evidence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Extracts** | Expose composable and Vue 3 component for `extracts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-evidence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Assertions** | Expose composable and Vue 3 component for `assertions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-evidence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Confidence** | Expose composable and Vue 3 component for `confidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-evidence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Proof conclusions** | Expose composable and Vue 3 component for `proof conclusions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-evidence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ArchiveEvidenceRecord.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/ArchiveEvidenceRecord.php) | `public function execute(EvidenceRecord $record): EvidenceRecord` |
| [CreateAssertion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateAssertion.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): Assertion` |
| [CreateCitation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateCitation.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): Citation` |
| [CreateCitationLink.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateCitationLink.php) | `public function execute(array $attributes): CitationLink` |
| [CreateEvidenceEntity.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateEvidenceEntity.php) | `public function execute(string $modelClass, array $attributes): Model`<br>`public function validate(array $values, string $modelClass): void` |
| [CreateEvidenceRecord.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateEvidenceRecord.php) | `public function execute(array $attributes): EvidenceRecord`<br>`public function validate(array $values): void` |
| [CreateExtract.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateExtract.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): Extract` |
| [CreateProofConclusion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateProofConclusion.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): ProofConclusion` |
| [CreateRepository.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateRepository.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): Repository` |
| [CreateSource.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateSource.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): Source` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Assertion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/Assertion.php) | `subject_person_id`, `citation_id`, `extract_id`, `statement`, `confidence`, `status`, `metadata` |
| [Citation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/Citation.php) | `source_id`, `repository_id`, `title`, `volume`, `page`, `text`, `confidence`, `event_date`, `metadata` |
| [CitationLink.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/CitationLink.php) | `team_id`, `citation_id`, `subject_person_id`, `group`, `page`, `quality`, `text`, `metadata` |
| [EvidenceRecord.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/EvidenceRecord.php) | `team_id`, `name`, `kind`, `repository`, `citation`, `extract`, `assertion`, `proof_conclusion`, `confidence`, `source_url`, `event_date`, `subject_person_id`, `reviewed_at`, `status`, `metadata` |
| [Extract.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/Extract.php) | `citation_id`, `content`, `transcription`, `page`, `metadata` |
| [ProofConclusion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/ProofConclusion.php) | `assertion_id`, `conclusion`, `confidence`, `status`, `metadata` |
| [Repository.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/Repository.php) | `source_id`, `name`, `description`, `address`, `url`, `email`, `is_active`, `metadata` |
| [Source.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/Source.php) | `name`, `description`, `url`, `archive_metadata`, `record_type`, `is_active`, `metadata` |
<!-- layer-implementation-plan:end -->
