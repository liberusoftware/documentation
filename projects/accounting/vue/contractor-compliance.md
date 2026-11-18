# Accounting: Contractor Compliance Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#contractor-compliance). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-contractor-compliance-vue-inertia`
**Matching domain module:** `accounting-contractor-compliance`
**Application:** Accounting
**Source feature:** [Contractor Compliance](../features/contractor-compliance.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/contractor-compliance.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Contractor records:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Status/evidence:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Withholding schemes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **CIS/1099-style classifications:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Deductions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Statements:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Regional exports:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-contractor-compliance-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `contractor-records`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `status-evidence`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `withholding-schemes`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `cis-1099-style-classifications`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `deductions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `statements`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `regional-exports`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-contractor-compliance` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-contractor-compliance-vue-inertia`](https://github.com/liberusoftware/module-accounting-contractor-compliance-vue-inertia) (`@liberusoftware/module-accounting-contractor-compliance-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/contractor-compliance.md) · [Core plan](../core/contractor-compliance.md) · [API plan](../api/contractor-compliance.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Contractor records** | Render `contractor records` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Status/evidence** | Render `status/evidence` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Withholding schemes** | Render `withholding schemes` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **CIS/1099-style classifications** | Render `cis/1099-style classifications` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Deductions** | Render `deductions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Statements** | Render `statements` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Regional exports** | Render `regional exports` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ContractorQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Queries/ContractorQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ExportContractorCompliance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Actions/ExportContractorCompliance.php) | `public function handle(Contractor $contractor, string $region): Contractor` |
| [IssueContractorStatement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Actions/IssueContractorStatement.php) | `public function handle(Contractor $contractor, array $statement): Contractor` |
| [RecordContractorEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Actions/RecordContractorEvidence.php) | `public function handle(Contractor $contractor, array $evidence): Contractor` |
| [RegisterContractor.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Actions/RegisterContractor.php) | `public function handle(array $attributes): Contractor` |
| [UpdateContractorCompliance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Actions/UpdateContractorCompliance.php) | `public function handle(Contractor $contractor, array $attributes): Contractor` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Contractor.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Models/Contractor.php) | `team_id`, `contractor_ref`, `legal_name`, `classification`, `status`, `withholding_scheme`, `deductions`, `evidence`, `statement`, `regional_export` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ContractorsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance-api/src/Http/Controllers/ContractorsController.php) | `public function index(ContractorQuery $query): JsonResponse`<br>`public function store(Request $request, RegisterContractor $action): JsonResponse`<br>`public function evidence(Request $request, string $contractor, RecordContractorEvidence $action): JsonResponse`<br>`public function statement(Request $request, string $contractor, IssueContractorStatement $action): JsonResponse`<br>`public function export(Request $request, string $contractor, ExportContractorCompliance $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-contractor-compliance-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/contractor-compliance')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.contractor-compliance.read')->get('/', [ContractorsController::class, 'index']);
Route::middleware('ability:accounting.contractor-compliance.write')->group(function (): void {
Route::post('/', [ContractorsController::class, 'store']);
Route::post('/{contractor}/evidence', [ContractorsController::class, 'evidence']);
Route::post('/{contractor}/statement', [ContractorsController::class, 'statement']);
Route::post('/{contractor}/export', [ContractorsController::class, 'export']);
```
<!-- layer-implementation-plan:end -->
