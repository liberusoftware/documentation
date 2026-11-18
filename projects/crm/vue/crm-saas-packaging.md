# CRM: Crm Saas Packaging Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-saas-packaging). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-crm-crm-saas-packaging-vue-inertia`
**Matching domain module:** `crm-saas-packaging`
**Application:** CRM
**Source feature:** [Crm Saas Packaging](../features/crm-saas-packaging.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-saas-packaging.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Plans:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Feature/module entitlements:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Limits:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Trials:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Signup provisioning:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Upgrade/downgrade:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Suspension:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Cancellation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Billing integration:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-crm-crm-saas-packaging-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `plans`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `feature-module-entitlements`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `limits`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `trials`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `signup-provisioning`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `upgrade-downgrade`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `suspension`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `cancellation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `billing-integration`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-saas-packaging` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-crm-laravel-inertia-vue`](https://github.com/liberusoftware/project-crm-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-crm-saas-packaging-vue-inertia`](https://github.com/liberusoftware/module-crm-saas-packaging-vue-inertia) (`@liberusoftware/module-crm-saas-packaging-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/crm-saas-packaging.md) · [Core plan](../core/crm-saas-packaging.md) · [API plan](../api/crm-saas-packaging.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Plans** | Render `plans` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Feature/module entitlements** | Render `feature/module entitlements` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Limits** | Render `limits` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Trials** | Render `trials` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Signup provisioning** | Render `signup provisioning` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Upgrade/downgrade** | Render `upgrade/downgrade` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Suspension** | Render `suspension` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Cancellation** | Render `cancellation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Billing integration** | Render `billing integration` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [SaasQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Queries/SaasQuery.php) | `public function plans()`<br>`public function subscription(int $teamId): ?SaasSubscription`<br>`public function usage(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ChangeSubscriptionStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Actions/ChangeSubscriptionStatus.php) | `public function execute(int $teamId, int $actorId, string $status): SaasSubscription` |
| [ProvisionSubscription.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Actions/ProvisionSubscription.php) | `public function execute(int $teamId, int $actorId, array $data): SaasSubscription` |
| [RecordUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Actions/RecordUsage.php) | `public function execute(int $teamId, int $actorId, array $data): SaasUsage` |
| [UpdateSubscription.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Actions/UpdateSubscription.php) | `public function execute(int $teamId, int $actorId, array $data): SaasSubscription` |
| [SaasPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Services/SaasPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SaasPlan.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Models/SaasPlan.php) | No literal fillable array detected; inspect the model and API schema. |
| [SaasSubscription.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Models/SaasSubscription.php) | No literal fillable array detected; inspect the model and API schema. |
| [SaasUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Models/SaasUsage.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [SaasController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging-api/src/Http/Controllers/SaasController.php) | `public function plans(SaasQuery $q)`<br>`public function subscription(Request $r, SaasQuery $q)`<br>`public function provision(Request $r, ProvisionSubscription $a)`<br>`public function status(Request $r, string $status, ChangeSubscriptionStatus $a)`<br>`public function usage(Request $r, SaasQuery $q)`<br>`public function recordUsage(Request $r, RecordUsage $a)` |

**Observed route declarations:**

[modules/crm-saas-packaging-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/saas-packaging')->group(function (): void {
Route::get('/plans', [SaasController::class, 'plans']);
Route::get('/subscription', [SaasController::class, 'subscription']);
Route::post('/subscription', [SaasController::class, 'provision']);
Route::post('/subscription/{status}', [SaasController::class, 'status'])->whereIn('status', ['active', 'suspended', 'cancelled']);
Route::get('/usage', [SaasController::class, 'usage']);
Route::post('/usage', [SaasController::class, 'recordUsage']);
```
<!-- layer-implementation-plan:end -->
