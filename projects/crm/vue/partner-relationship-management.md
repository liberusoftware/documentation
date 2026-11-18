# CRM: Partner Relationship Management Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#partner-relationship-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-crm-partner-relationship-management-vue-inertia`
**Matching domain module:** `crm-partner-relationship-management`
**Application:** CRM
**Source feature:** [Partner Relationship Management](../features/partner-relationship-management.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/partner-relationship-management.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Partner accounts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Contacts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Tiers:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Recruitment:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Onboarding:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Competencies:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Agreements:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Enablement:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Certification:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Plans:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Performance:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-crm-partner-relationship-management-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `partner-accounts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `contacts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `tiers`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `recruitment`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `onboarding`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `competencies`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `agreements`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `enablement`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `certification`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `plans`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `performance`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-partner-relationship-management` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-crm-laravel-inertia-vue`](https://github.com/liberusoftware/project-crm-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-crm-partner-relationship-management-vue-inertia`](https://github.com/liberusoftware/module-crm-partner-relationship-management-vue-inertia) (`@liberusoftware/module-crm-partner-relationship-management-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/partner-relationship-management.md) · [Core plan](../core/partner-relationship-management.md) · [API plan](../api/partner-relationship-management.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Partner accounts** | Render `partner accounts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Contacts** | Render `contacts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Tiers** | Render `tiers` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Recruitment** | Render `recruitment` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Onboarding** | Render `onboarding` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Competencies** | Render `competencies` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Agreements** | Render `agreements` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Enablement** | Render `enablement` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Certification** | Render `certification` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Plans** | Render `plans` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Performance** | Render `performance` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PartnerQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Queries/PartnerQuery.php) | `public function partners(int $teamId)`<br>`public function contacts(int $teamId)`<br>`public function activities(int $teamId)`<br>`public function performance(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddPartnerContact.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Actions/AddPartnerContact.php) | `public function __construct(private readonly PartnerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PartnerContact` |
| [ChangePartnerStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Actions/ChangePartnerStatus.php) | `public function __construct(private readonly PartnerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $partnerId, string $status): PartnerAccount` |
| [CreatePartner.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Actions/CreatePartner.php) | `public function __construct(private readonly PartnerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PartnerAccount` |
| [RecordPartnerActivity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Actions/RecordPartnerActivity.php) | `public function __construct(private readonly PartnerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PartnerActivity` |
| [RecordPartnerPerformance.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Actions/RecordPartnerPerformance.php) | `public function __construct(private readonly PartnerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PartnerPerformance` |
| [PartnerPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Services/PartnerPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PartnerAccount.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Models/PartnerAccount.php) | No literal fillable array detected; inspect the model and API schema. |
| [PartnerActivity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Models/PartnerActivity.php) | No literal fillable array detected; inspect the model and API schema. |
| [PartnerContact.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Models/PartnerContact.php) | No literal fillable array detected; inspect the model and API schema. |
| [PartnerPerformance.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Models/PartnerPerformance.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [PartnerRelationshipManagementController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management-api/src/Http/Controllers/PartnerRelationshipManagementController.php) | `public function partners(Request $r, PartnerQuery $q)`<br>`public function partner(Request $r, CreatePartner $a)`<br>`public function contact(Request $r, AddPartnerContact $a)`<br>`public function status(Request $r, int $partner, string $status, ChangePartnerStatus $a)`<br>`public function activity(Request $r, RecordPartnerActivity $a)`<br>`public function performance(Request $r, RecordPartnerPerformance $a)` |

**Observed route declarations:**

[modules/crm-partner-relationship-management-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/partner-relationship-management')->group(function (): void {
Route::get('/partners', [PartnerRelationshipManagementController::class, 'partners']);
Route::post('/partners', [PartnerRelationshipManagementController::class, 'partner']);
Route::post('/contacts', [PartnerRelationshipManagementController::class, 'contact']);
Route::post('/partners/{partner}/{status}', [PartnerRelationshipManagementController::class, 'status'])->whereIn('status', ['prospect', 'onboarding', 'active', 'suspended', 'inactive']);
Route::post('/activities', [PartnerRelationshipManagementController::class, 'activity']);
Route::post('/performance', [PartnerRelationshipManagementController::class, 'performance']);
```
<!-- layer-implementation-plan:end -->
