# CRM: Communities Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#communities). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-crm-communities-vue-inertia`
**Matching domain module:** `crm-communities`
**Application:** CRM
**Source feature:** [Communities](../features/communities.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/communities.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Customer/partner groups:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Spaces:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Memberships:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Posts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Comments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Events:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Moderation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Gamification:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Knowledge links:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **CRM profile activity:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-crm-communities-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `customer-partner-groups`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `spaces`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `memberships`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `posts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `comments`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `events`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `moderation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `gamification`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `knowledge-links`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `crm-profile-activity`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-communities` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-crm-laravel-inertia-vue`](https://github.com/liberusoftware/project-crm-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-crm-communities-vue-inertia`](https://github.com/liberusoftware/module-crm-communities-vue-inertia) (`@liberusoftware/module-crm-communities-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/communities.md) · [Core plan](../core/communities.md) · [API plan](../api/communities.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Customer/partner groups** | Render `customer/partner groups` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Spaces** | Render `spaces` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Memberships** | Render `memberships` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Posts** | Render `posts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Comments** | Render `comments` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Events** | Render `events` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Moderation** | Render `moderation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Gamification** | Render `gamification` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Knowledge links** | Render `knowledge links` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **CRM profile activity** | Render `crm profile activity` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CommunityQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Queries/CommunityQuery.php) | `public function spaces(int $teamId): Builder`<br>`public function feed(int $teamId, int $spaceId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCommunitySpace.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Actions/CreateCommunitySpace.php) | `public function execute(int $teamId, int $ownerId, string $name, string $kind = 'customer', array $settings = []): CommunitySpace` |
| [JoinCommunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Actions/JoinCommunity.php) | `public function execute(int $teamId, CommunitySpace $space, string $subjectKey, string $role = 'member'): CommunityMembership` |
| [PublishCommunityContent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Actions/PublishCommunityContent.php) | `public function execute(int $teamId, CommunitySpace $space, string $authorKey, string $body, string $kind = 'post', ?int $parentId = null, array $metadata = []): CommunityContent` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CommunityContent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Models/CommunityContent.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommunityMembership.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Models/CommunityMembership.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommunitySpace.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Models/CommunitySpace.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CommunitiesController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities-api/src/Http/Controllers/CommunitiesController.php) | `public function __construct(private readonly CommunityQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(CreateCommunitySpace $a): JsonResponse`<br>`public function join(CommunitySpace $space, JoinCommunity $a): JsonResponse`<br>`public function content(CommunitySpace $space, PublishCommunityContent $a): JsonResponse`<br>`public function feed(CommunitySpace $space): JsonResponse` |

**Observed route declarations:**

[modules/crm-communities-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/communities')->group(function (): void {
Route::get('spaces', [CommunitiesController::class, 'index']);
Route::post('spaces', [CommunitiesController::class, 'store']);
Route::post('spaces/{space}/join', [CommunitiesController::class, 'join']);
Route::post('spaces/{space}/content', [CommunitiesController::class, 'content']);
Route::get('spaces/{space}/feed', [CommunitiesController::class, 'feed']);
```
<!-- layer-implementation-plan:end -->
