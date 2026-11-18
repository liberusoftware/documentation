# CRM: Quotas and Incentives Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#quotas-and-incentives). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-crm-quotas-and-incentives-vue-inertia`
**Matching domain module:** `crm-quotas-and-incentives`
**Application:** CRM
**Source feature:** [Quotas and Incentives](../features/quotas-and-incentives.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/quotas-and-incentives.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Quotas:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Ramps:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Crediting:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Splits:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Territories:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Attainment:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Commission plans:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Accelerators:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Adjustments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Disputes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Approvals:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Payroll/export adapters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-crm-quotas-and-incentives-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `quotas`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `ramps`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `crediting`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `splits`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `territories`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `attainment`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `commission-plans`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `accelerators`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `adjustments`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `disputes`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `approvals`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `payroll-export-adapters`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-quotas-and-incentives` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-crm-laravel-inertia-vue`](https://github.com/liberusoftware/project-crm-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-crm-quotas-and-incentives-vue-inertia`](https://github.com/liberusoftware/module-crm-quotas-and-incentives-vue-inertia) (`@liberusoftware/module-crm-quotas-and-incentives-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/quotas-and-incentives.md) · [Core plan](../core/quotas-and-incentives.md) · [API plan](../api/quotas-and-incentives.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Quotas** | Render `quotas` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Ramps** | Render `ramps` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Crediting** | Render `crediting` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Splits** | Render `splits` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Territories** | Render `territories` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Attainment** | Render `attainment` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Commission plans** | Render `commission plans` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Accelerators** | Render `accelerators` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Adjustments** | Render `adjustments` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Disputes** | Render `disputes` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Approvals** | Render `approvals` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Payroll/export adapters** | Render `payroll/export adapters` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [QuotaQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Queries/QuotaQuery.php) | `public function quotas(int $teamId)`<br>`public function plans(int $teamId)`<br>`public function credits(int $teamId)`<br>`public function disputes(int $teamId)`<br>`public function exports(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCommissionPlan.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/CreateCommissionPlan.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CommissionPlan` |
| [CreateQuota.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/CreateQuota.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Quota` |
| [CreditCommission.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/CreditCommission.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CommissionCredit` |
| [ExportCommissions.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/ExportCommissions.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CommissionExport` |
| [OpenDispute.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/OpenDispute.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CommissionDispute` |
| [ResolveDispute.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/ResolveDispute.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $disputeId, array $input): CommissionDispute` |
| [UpdateQuota.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/UpdateQuota.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $quotaId, array $input): Quota` |
| [QuotaPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Services/QuotaPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CommissionCredit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Models/CommissionCredit.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommissionDispute.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Models/CommissionDispute.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommissionExport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Models/CommissionExport.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommissionPlan.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Models/CommissionPlan.php) | No literal fillable array detected; inspect the model and API schema. |
| [Quota.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Models/Quota.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [QuotasAndIncentivesController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives-api/src/Http/Controllers/QuotasAndIncentivesController.php) | `public function quotas(Request $r, QuotaQuery $q)`<br>`public function quota(Request $r, CreateQuota $a)`<br>`public function plans(Request $r, QuotaQuery $q)`<br>`public function plan(Request $r, CreateCommissionPlan $a)`<br>`public function credits(Request $r, QuotaQuery $q)`<br>`public function credit(Request $r, CreditCommission $a)`<br>`public function dispute(Request $r, OpenDispute $a)`<br>`public function resolve(Request $r, int $dispute, ResolveDispute $a)`<br>`public function export(Request $r, ExportCommissions $a)` |

**Observed route declarations:**

[modules/crm-quotas-and-incentives-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/quotas-and-incentives')->group(function (): void {
Route::get('/quotas', [QuotasAndIncentivesController::class, 'quotas']);
Route::post('/quotas', [QuotasAndIncentivesController::class, 'quota']);
Route::get('/plans', [QuotasAndIncentivesController::class, 'plans']);
Route::post('/plans', [QuotasAndIncentivesController::class, 'plan']);
Route::get('/credits', [QuotasAndIncentivesController::class, 'credits']);
Route::post('/credits', [QuotasAndIncentivesController::class, 'credit']);
Route::post('/disputes', [QuotasAndIncentivesController::class, 'dispute']);
Route::post('/disputes/{dispute}/resolve', [QuotasAndIncentivesController::class, 'resolve']);
Route::post('/exports', [QuotasAndIncentivesController::class, 'export']);
```
<!-- layer-implementation-plan:end -->
