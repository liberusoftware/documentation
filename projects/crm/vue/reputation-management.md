# CRM: Reputation Management Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#reputation-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-crm-reputation-management-vue-inertia`
**Matching domain module:** `crm-reputation-management`
**Application:** CRM
**Source feature:** [Reputation Management](../features/reputation-management.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/reputation-management.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Review requests:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Review-site connections:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Monitoring:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Response workflow:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Templates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Escalation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Sentiment:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Location rollups:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reputation reporting:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-crm-reputation-management-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `review-requests`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `review-site-connections`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `monitoring`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `response-workflow`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `templates`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `escalation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `sentiment`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `location-rollups`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `reputation-reporting`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-reputation-management` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-crm-laravel-inertia-vue`](https://github.com/liberusoftware/project-crm-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-crm-reputation-management-vue-inertia`](https://github.com/liberusoftware/module-crm-reputation-management-vue-inertia) (`@liberusoftware/module-crm-reputation-management-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/reputation-management.md) · [Core plan](../core/reputation-management.md) · [API plan](../api/reputation-management.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Review requests** | Render `review requests` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Review-site connections** | Render `review-site connections` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Monitoring** | Render `monitoring` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Response workflow** | Render `response workflow` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Templates** | Render `templates` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Escalation** | Render `escalation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Sentiment** | Render `sentiment` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Location rollups** | Render `location rollups` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Reputation reporting** | Render `reputation reporting` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ReputationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Queries/ReputationQuery.php) | `public function connections(int $teamId)`<br>`public function requests(int $teamId)`<br>`public function reviews(int $teamId)`<br>`public function templates(int $teamId)`<br>`public function rollups(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConnectReviewSite.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/ConnectReviewSite.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReputationConnection` |
| [CreateReviewRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/CreateReviewRequest.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReputationRequest` |
| [EscalateReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/EscalateReview.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $reviewId): ReputationReview` |
| [RecordReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/RecordReview.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReputationReview` |
| [RespondToReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/RespondToReview.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $reviewId, array $input): ReputationReview` |
| [SaveTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/SaveTemplate.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReputationTemplate` |
| [UpdateReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/UpdateReview.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $reviewId, array $input): ReputationReview` |
| [ReputationPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Services/ReputationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReputationConnection.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationConnection.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReputationRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationRequest.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReputationReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationReview.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReputationRollup.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationRollup.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReputationTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationTemplate.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ReputationManagementController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management-api/src/Http/Controllers/ReputationManagementController.php) | `public function connections(Request $r, ReputationQuery $q)`<br>`public function connection(Request $r, ConnectReviewSite $a)`<br>`public function requests(Request $r, ReputationQuery $q)`<br>`public function request(Request $r, CreateReviewRequest $a)`<br>`public function reviews(Request $r, ReputationQuery $q)`<br>`public function review(Request $r, RecordReview $a)`<br>`public function respond(Request $r, int $review, RespondToReview $a)`<br>`public function template(Request $r, SaveTemplate $a)` |

**Observed route declarations:**

[modules/crm-reputation-management-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/reputation-management')->group(function (): void {
Route::get('/connections', [ReputationManagementController::class, 'connections']);
Route::post('/connections', [ReputationManagementController::class, 'connection']);
Route::get('/requests', [ReputationManagementController::class, 'requests']);
Route::post('/requests', [ReputationManagementController::class, 'request']);
Route::get('/reviews', [ReputationManagementController::class, 'reviews']);
Route::post('/reviews', [ReputationManagementController::class, 'review']);
Route::post('/reviews/{review}/respond', [ReputationManagementController::class, 'respond']);
Route::post('/templates', [ReputationManagementController::class, 'template']);
```
<!-- layer-implementation-plan:end -->
