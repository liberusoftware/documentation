# Genealogy: Discovery Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#discovery). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-genealogy-discovery-vue-inertia`
**Matching domain module:** `genealogy-discovery`
**Application:** Genealogy
**Source feature:** [Discovery](../features/discovery.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/discovery.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Person/place/source search:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Hints:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Duplicates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Relationship paths:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Privacy-aware indexes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-genealogy-discovery-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `person-place-source-search`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `hints`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `duplicates`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `relationship-paths`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `privacy-aware-indexes`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `genealogy-discovery` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-genealogy-laravel-inertia-vue`](https://github.com/liberusoftware/project-genealogy-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-genealogy-discovery-vue-inertia`](https://github.com/liberusoftware/module-genealogy-discovery-vue-inertia) (`@liberusoftware/module-genealogy-discovery-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/discovery.md) · [Core plan](../core/discovery.md) · [API plan](../api/discovery.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Person/place/source search** | Render `person/place/source search` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Hints** | Render `hints` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Duplicates** | Render `duplicates` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Relationship paths** | Render `relationship paths` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Privacy-aware indexes** | Render `privacy-aware indexes` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [DiscoverySearch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Queries/DiscoverySearch.php) | `public function execute(string $term, array $options = []): array` |
| [DuplicateCandidates.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Queries/DuplicateCandidates.php) | `public function execute(int $limit = 100, int $minimumConfidence = 70): array` |
| [RelationshipPath.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Queries/RelationshipPath.php) | `public function execute(string $from, string $to, int $maxDepth = 6, bool $publicOnly = false): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDiscoveryMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Actions/CreateDiscoveryMatch.php) | `public function execute(array $attributes): DiscoveryMatch` |
| [DeleteDiscoveryMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Actions/DeleteDiscoveryMatch.php) | `public function execute(DiscoveryMatch $match): void` |
| [ReviewDiscoveryMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Actions/ReviewDiscoveryMatch.php) | `public function execute(DiscoveryMatch $match, string $status): DiscoveryMatch` |
| [ScanDuplicateCandidates.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Actions/ScanDuplicateCandidates.php) | `public function __construct( private readonly DuplicateCandidates $candidates, private readonly CreateDiscoveryMatch $create, )`<br>`public function execute(float $threshold = 0.7, int $limit = 100): array` |
| [UpdateDiscoveryMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Actions/UpdateDiscoveryMatch.php) | `public function execute(DiscoveryMatch $match, array $attributes): DiscoveryMatch` |
| [ExternalRecordProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Contracts/ExternalRecordProvider.php) | `public function key(): string`<br>`public function isAvailable(): bool`<br>`public function search(array $person): array` |
| [ExternalRecordMatcher.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Services/ExternalRecordMatcher.php) | `public function __construct(private readonly ?ExternalRecordProvider $provider = null)`<br>`public function execute(array $person, array $weights = []): array`<br>`public function scoreCandidates(array $person, array $candidates, array $weights = []): array` |
| [SmartMatchingService.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Services/SmartMatchingService.php) | `public function findMatches(Person $person, iterable $providers, int $minimumConfidence = 60, int $limit = 10): array`<br>`public function persist(Model $user, Person $person, array $matches): Collection` |
| [SocialFamilyDiscovery.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Services/SocialFamilyDiscovery.php) | `public function enable(ConnectedAccount $account): bool`<br>`public function disable(ConnectedAccount $account): bool`<br>`public function sync(ConnectedAccount $account): bool`<br>`public function privacy(int\|string $userId): SocialConnectionPrivacy`<br>`public function updatePrivacy(int\|string $userId, array $settings): SocialConnectionPrivacy`<br>`public function needsSync(ConnectedAccount $account): bool`<br>`public function findPotentialConnections(Model $user): Collection`<br>`public function processMatches(Model $user): int` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DiscoveryMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Models/DiscoveryMatch.php) | `team_id`, `kind`, `name`, `subject_id`, `related_id`, `confidence`, `rationale`, `source_type`, `detected_at`, `reviewed_at`, `status`, `metadata` |
| [SmartMatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Models/SmartMatch.php) | `team_id`, `user_id`, `person_id`, `external_tree_id`, `external_person_id`, `match_source`, `record_category`, `match_data`, `search_criteria`, `confidence_score`, `status`, `reviewed_at` |
| [SocialConnectionPrivacy.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Models/SocialConnectionPrivacy.php) | `user_id`, `allow_family_discovery`, `show_profile_to_matches`, `share_tree_with_matches`, `allow_contact_from_matches`, `blocked_users` |
| [SocialFamilyConnection.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-discovery/src/Models/SocialFamilyConnection.php) | `user_id`, `connected_account_id`, `matched_social_id`, `matched_name`, `matched_email`, `relationship_type`, `confidence_score`, `matching_criteria`, `status` |
<!-- layer-implementation-plan:end -->
