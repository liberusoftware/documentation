# CRM: Crm Segmentation Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-segmentation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-crm-crm-segmentation-vue-inertia`
**Matching domain module:** `crm-segmentation`
**Application:** CRM
**Source feature:** [Crm Segmentation](../features/crm-segmentation.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-segmentation.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Static/dynamic audiences:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Nested conditions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Behavioral events:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Calculated attributes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Exclusions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Estimated counts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Refresh:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Lineage:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-crm-crm-segmentation-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `static-dynamic-audiences`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `nested-conditions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `behavioral-events`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `calculated-attributes`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `exclusions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `estimated-counts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `refresh`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `lineage`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-segmentation` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-crm-laravel-inertia-vue`](https://github.com/liberusoftware/project-crm-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-crm-segmentation-vue-inertia`](https://github.com/liberusoftware/module-crm-segmentation-vue-inertia) (`@liberusoftware/module-crm-segmentation-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/crm-segmentation.md) · [Core plan](../core/crm-segmentation.md) · [API plan](../api/crm-segmentation.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Static/dynamic audiences** | Render `static/dynamic audiences` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Nested conditions** | Render `nested conditions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Behavioral events** | Render `behavioral events` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Calculated attributes** | Render `calculated attributes` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Exclusions** | Render `exclusions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Estimated counts** | Render `estimated counts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Refresh** | Render `refresh` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Lineage** | Render `lineage` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [SegmentationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Queries/SegmentationQuery.php) | `public function audiences(int $teamId)`<br>`public function members(int $teamId, int $audienceId)`<br>`public function events(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Actions/CreateAudience.php) | `public function execute(int $teamId, int $actorId, array $data): Audience` |
| [RecordBehaviorEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Actions/RecordBehaviorEvent.php) | `public function execute(int $teamId, int $actorId, array $data): BehaviorEvent` |
| [RefreshAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Actions/RefreshAudience.php) | `public function execute(int $teamId, int $actorId, int $audienceId, array $data = []): Audience` |
| [UpdateAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Actions/UpdateAudience.php) | `public function execute(int $teamId, int $actorId, int $audienceId, array $data): Audience` |
| [SegmentationAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Services/SegmentationAudit.php) | `public function record(int $teamId, ?int $actorId, int $audienceId, string $operation, array $details = []): SegmentationLineage` |
| [SegmentationPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Services/SegmentationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Audience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Models/Audience.php) | No literal fillable array detected; inspect the model and API schema. |
| [AudienceMember.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Models/AudienceMember.php) | No literal fillable array detected; inspect the model and API schema. |
| [BehaviorEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Models/BehaviorEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [SegmentationLineage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Models/SegmentationLineage.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [SegmentationController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation-api/src/Http/Controllers/SegmentationController.php) | `public function index(Request $r, SegmentationQuery $q)`<br>`public function store(Request $r, CreateAudience $a)`<br>`public function update(Request $r, int $audience, UpdateAudience $a)`<br>`public function members(Request $r, int $audience, SegmentationQuery $q)`<br>`public function refresh(Request $r, int $audience, RefreshAudience $a)`<br>`public function event(Request $r, RecordBehaviorEvent $a)` |

**Observed route declarations:**

[modules/crm-segmentation-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/segmentation')->group(function (): void {
Route::get('/audiences', [SegmentationController::class, 'index']);
Route::post('/audiences', [SegmentationController::class, 'store']);
Route::patch('/audiences/{audience}', [SegmentationController::class, 'update']);
Route::get('/audiences/{audience}/members', [SegmentationController::class, 'members']);
Route::post('/audiences/{audience}/refresh', [SegmentationController::class, 'refresh']);
Route::post('/events', [SegmentationController::class, 'event']);
```
<!-- layer-implementation-plan:end -->
