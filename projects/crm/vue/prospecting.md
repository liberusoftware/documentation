# CRM: Prospecting Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#prospecting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-crm-prospecting-vue-inertia`
**Matching domain module:** `crm-prospecting`
**Application:** CRM
**Source feature:** [Prospecting](../features/prospecting.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/prospecting.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Ideal-customer profiles:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Prospect searches:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **List building:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Research queues:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Contact reveal/credits:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Provider provenance:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Compliant export/outreach handoff:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-crm-prospecting-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `ideal-customer-profiles`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `prospect-searches`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `list-building`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `research-queues`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `contact-reveal-credits`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `provider-provenance`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `compliant-export-outreach-handoff`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-prospecting` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-crm-laravel-inertia-vue`](https://github.com/liberusoftware/project-crm-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-crm-prospecting-vue-inertia`](https://github.com/liberusoftware/module-crm-prospecting-vue-inertia) (`@liberusoftware/module-crm-prospecting-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/prospecting.md) · [Core plan](../core/prospecting.md) · [API plan](../api/prospecting.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Ideal-customer profiles** | Render `ideal-customer profiles` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Prospect searches** | Render `prospect searches` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **List building** | Render `list building` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Research queues** | Render `research queues` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Contact reveal/credits** | Render `contact reveal/credits` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Provider provenance** | Render `provider provenance` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Compliant export/outreach handoff** | Render `compliant export/outreach handoff` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ProspectingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Queries/ProspectingQuery.php) | `public function profiles(int $teamId)`<br>`public function searches(int $teamId)`<br>`public function prospects(int $teamId)`<br>`public function queue(int $teamId)`<br>`public function exports(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateIdealCustomerProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/CreateIdealCustomerProfile.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): IdealCustomerProfile` |
| [CreateProspectSearch.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/CreateProspectSearch.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProspectSearch` |
| [ImportProspect.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/ImportProspect.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Prospect` |
| [QueueExport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/QueueExport.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProspectExport` |
| [QueueResearch.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/QueueResearch.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProspectResearchItem` |
| [RevealContact.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/RevealContact.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProspectCredit` |
| [UpdateProspect.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/UpdateProspect.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $prospectId, array $input): Prospect` |
| [ProspectingPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Services/ProspectingPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [IdealCustomerProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/IdealCustomerProfile.php) | No literal fillable array detected; inspect the model and API schema. |
| [Prospect.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/Prospect.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProspectCredit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectCredit.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProspectExport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectExport.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProspectResearchItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectResearchItem.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProspectSearch.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectSearch.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProspectingController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-api/src/Http/Controllers/ProspectingController.php) | `public function profiles(Request $r, ProspectingQuery $q)`<br>`public function profile(Request $r, CreateIdealCustomerProfile $a)`<br>`public function searches(Request $r, ProspectingQuery $q)`<br>`public function search(Request $r, CreateProspectSearch $a)`<br>`public function prospects(Request $r, ProspectingQuery $q)`<br>`public function prospect(Request $r, ImportProspect $a)`<br>`public function research(Request $r, QueueResearch $a)`<br>`public function reveal(Request $r, RevealContact $a)`<br>`public function export(Request $r, QueueExport $a)` |

**Observed route declarations:**

[modules/crm-prospecting-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/prospecting')->group(function (): void {
Route::get('/profiles', [ProspectingController::class, 'profiles']);
Route::post('/profiles', [ProspectingController::class, 'profile']);
Route::get('/searches', [ProspectingController::class, 'searches']);
Route::post('/searches', [ProspectingController::class, 'search']);
Route::get('/prospects', [ProspectingController::class, 'prospects']);
Route::post('/prospects', [ProspectingController::class, 'prospect']);
Route::post('/research', [ProspectingController::class, 'research']);
Route::post('/reveal', [ProspectingController::class, 'reveal']);
Route::post('/exports', [ProspectingController::class, 'export']);
```
<!-- layer-implementation-plan:end -->
