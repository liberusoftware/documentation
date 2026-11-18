# CMS: Cms Translation Management Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-translation-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-cms-cms-translation-management-vue-inertia`
**Matching domain module:** `cms-translation-management`
**Application:** CMS
**Source feature:** [Cms Translation Management](../features/cms-translation-management.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/cms-translation-management.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Jobs:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Source changes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Assignments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Vendor adapters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Machine translation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Review:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Memory/glossaries:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Status:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Cost:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reconciliation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-cms-cms-translation-management-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `jobs`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `source-changes`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `assignments`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `vendor-adapters`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `machine-translation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `review`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `memory-glossaries`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `status`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `cost`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `reconciliation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `cms-translation-management` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-cms-laravel-inertia-vue`](https://github.com/liberusoftware/project-cms-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-cms-translation-management-vue-inertia`](https://github.com/liberusoftware/module-cms-translation-management-vue-inertia) (`@liberusoftware/module-cms-translation-management-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/cms-translation-management.md) · [Core plan](../core/cms-translation-management.md) · [API plan](../api/cms-translation-management.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Jobs** | Render `jobs` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Source changes** | Render `source changes` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Assignments** | Render `assignments` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Vendor adapters** | Render `vendor adapters` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Machine translation** | Render `machine translation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Review** | Render `review` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Memory/glossaries** | Render `memory/glossaries` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Status** | Render `status` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Cost** | Render `cost` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Reconciliation** | Render `reconciliation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [TranslationJobQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Queries/TranslationJobQuery.php) | `public function paginate(int $perPage = 15, string $search = '', ?string $status = null): LengthAwarePaginator`<br>`public function find(string $publicId): ?TranslationJob` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [TranslationManagementService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Actions/TranslationManagementService.php) | `public function __construct(private TranslationVendorRegistry $vendors)`<br>`public function createJob(array $attributes): TranslationJob`<br>`public function addSourceChange(TranslationJob $job, array $attributes): TranslationSourceChange`<br>`public function queue(TranslationJob $job): TranslationJob`<br>`public function cancel(TranslationJob $job): TranslationJob`<br>`public function translate(TranslationSourceChange $change, string $vendorKey, array $context = []): TranslationSourceChange`<br>`public function assign(TranslationSourceChange $change, string $assigneeType, int\|string $assigneeId, string $role, ?string $dueAt = null): TranslationAssignment`<br>`public function review(TranslationSourceChange $change, string $decision, ?string $notes = null): TranslationSourceChange`<br>`public function addVendor(array $attributes): TranslationVendor`<br>`public function remember(string $sourceLocale, string $targetLocale, string $sourceText, string $translatedText, array $metadata = [], int\|string\|null $teamId = null): TranslationMemory`<br>`public function glossary(array $attributes): TranslationGlossary`<br>`public function reconcile(TranslationJob $job): TranslationJob` |
| [TranslationVendorInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Contracts/TranslationVendorInterface.php) | `public function key(): string`<br>`public function translate(string $source, string $sourceLocale, string $targetLocale, array $context = []): TranslationResult` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TranslationAssignment.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationAssignment.php) | `job_id`, `source_change_id`, `assignee_type`, `assignee_id`, `role`, `status`, `due_at`, `completed_at`, `team_id` |
| [TranslationGlossary.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationGlossary.php) | `source_locale`, `target_locale`, `source_term`, `preferred_term`, `forbidden_terms`, `team_id` |
| [TranslationJob.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationJob.php) | `public_id`, `external_key`, `name`, `source_locale`, `target_locale`, `status`, `vendor_key`, `total_units`, `completed_units`, `estimated_cost`, `actual_cost`, `currency`, `metadata`, `queued_at`, `completed_at`, `team_id` |
| [TranslationMemory.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationMemory.php) | `source_locale`, `target_locale`, `source_hash`, `source_text`, `translated_text`, `status`, `metadata`, `team_id` |
| [TranslationSourceChange.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationSourceChange.php) | `job_id`, `subject_type`, `subject_id`, `field`, `source_text`, `source_hash`, `source_version`, `translated_text`, `translated_hash`, `status`, `provider`, `model`, `cost`, `provenance`, `review_notes`, `translated_at`, `reviewed_at`, `team_id` |
| [TranslationVendor.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-management/src/Models/TranslationVendor.php) | `key`, `name`, `driver`, `settings`, `status`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [TranslationManagementController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-translation-management-api/src/Http/Controllers/TranslationManagementController.php) | `public function __construct(private TranslationJobQuery $jobs, private TranslationManagementService $service)`<br>`public function index(Request $request): AnonymousResourceCollection`<br>`public function show(string $publicId): TranslationJobResource`<br>`public function create(Request $request): TranslationJobResource`<br>`public function sourceChange(Request $request, string $publicId): TranslationSourceChangeResource`<br>`public function translate(Request $request, int $sourceChange): TranslationSourceChangeResource`<br>`public function review(Request $request, int $sourceChange): TranslationSourceChangeResource`<br>`public function reconcile(string $publicId): TranslationJobResource`<br>`public function queue(string $publicId): TranslationJobResource`<br>`public function cancel(string $publicId): TranslationJobResource`<br>`public function assign(Request $request, int $sourceChange): mixed`<br>`public function vendor(Request $request): TranslationVendorResource`<br>`public function memory(Request $request): TranslationMemoryResource`<br>`public function glossary(Request $request): TranslationGlossaryResource` |
<!-- layer-implementation-plan:end -->
