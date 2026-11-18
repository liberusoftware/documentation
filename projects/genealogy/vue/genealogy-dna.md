# Genealogy: Genealogy Dna Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-dna). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-genealogy-genealogy-dna-vue-inertia`
**Matching domain module:** `genealogy-dna`
**Application:** Genealogy
**Source feature:** [Genealogy Dna](../features/genealogy-dna.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/genealogy-dna.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Kits:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Providers:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Consent:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Match segments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Relationships:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Groups:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Notes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Revocation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-genealogy-genealogy-dna-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `kits`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `providers`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `consent`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `match-segments`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `relationships`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `groups`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `notes`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `revocation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `genealogy-dna` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-genealogy-laravel-inertia-vue`](https://github.com/liberusoftware/project-genealogy-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-genealogy-dna-vue-inertia`](https://github.com/liberusoftware/module-genealogy-dna-vue-inertia) (`@liberusoftware/module-genealogy-dna-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/genealogy-dna.md) · [Core plan](../core/genealogy-dna.md) · [API plan](../api/genealogy-dna.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Kits** | Render `kits` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Providers** | Render `providers` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Consent** | Render `consent` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Match segments** | Render `match segments` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Relationships** | Render `relationships` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Groups** | Render `groups` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Notes** | Render `notes` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Revocation** | Render `revocation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDnaGroup.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaGroup.php) | `public function execute(array $attributes): DnaGroup`<br>`public function validate(array $values): void` |
| [CreateDnaKit.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaKit.php) | `public function execute(array $attributes): DnaKit` |
| [CreateDnaMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaMatch.php) | `public function execute(array $attributes): DnaMatch` |
| [CreateDnaNote.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaNote.php) | `public function execute(array $attributes): DnaNote` |
| [CreateDnaProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaProvider.php) | `public function execute(array $attributes): DnaProvider` |
| [CreateDnaRelationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaRelationship.php) | `public function execute(array $attributes): DnaRelationship` |
| [CreateDnaSegment.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaSegment.php) | `public function execute(array $attributes): DnaSegment` |
| [DeleteDnaGroup.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaGroup.php) | `public function execute(DnaGroup $group): void` |
| [DeleteDnaKit.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaKit.php) | `public function __construct(private readonly DnaFileVault $vault)`<br>`public function execute(DnaKit $kit): void` |
| [DeleteDnaMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaMatch.php) | `public function execute(DnaMatch $match): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DnaConsent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaConsent.php) | `team_id`, `kit_id`, `scope`, `granted`, `policy_version`, `granted_at`, `revoked_at`, `revocation_reason`, `metadata` |
| [DnaGroup.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaGroup.php) | `team_id`, `name`, `description`, `status`, `metadata` |
| [DnaKit.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaKit.php) | `team_id`, `name`, `provider`, `provider_id`, `external_id`, `person_id`, `test_type`, `consent_status`, `consented_at`, `revoked_at`, `revocation_reason`, `status`, `metadata`, `file_path`, `file_hash`, `file_format`, `snp_count` |
| [DnaMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaMatch.php) | `team_id`, `kit_id`, `external_id`, `display_name`, `predicted_relationship`, `confidence`, `total_cm`, `shared_segments`, `status`, `is_private`, `notes`, `metadata` |
| [DnaNote.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaNote.php) | `team_id`, `noteable_type`, `noteable_id`, `body` |
| [DnaProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaProvider.php) | `team_id`, `name`, `slug`, `status`, `website`, `metadata` |
| [DnaRelationship.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaRelationship.php) | `team_id`, `match_id`, `person_id`, `relationship_type`, `confidence`, `status`, `rationale`, `metadata` |
| [DnaSegment.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaSegment.php) | `team_id`, `match_id`, `chromosome`, `start_position`, `end_position`, `centimorgans`, `snps`, `side`, `metadata` |
<!-- layer-implementation-plan:end -->
