# Genealogy: Evidence Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#evidence). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-genealogy-evidence-vue-inertia`
**Matching domain module:** `genealogy-evidence`
**Application:** Genealogy
**Source feature:** [Evidence](../features/evidence.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/evidence.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Sources:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Repositories:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Citations:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Extracts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Assertions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Confidence:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Proof conclusions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-genealogy-evidence-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `sources`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `repositories`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `citations`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `extracts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `assertions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `confidence`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `proof-conclusions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `genealogy-evidence` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-genealogy-laravel-inertia-vue`](https://github.com/liberusoftware/project-genealogy-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-genealogy-evidence-vue-inertia`](https://github.com/liberusoftware/module-genealogy-evidence-vue-inertia) (`@liberusoftware/module-genealogy-evidence-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/evidence.md) · [Core plan](../core/evidence.md) · [API plan](../api/evidence.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Sources** | Render `sources` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Repositories** | Render `repositories` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Citations** | Render `citations` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Extracts** | Render `extracts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Assertions** | Render `assertions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Confidence** | Render `confidence` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Proof conclusions** | Render `proof conclusions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
