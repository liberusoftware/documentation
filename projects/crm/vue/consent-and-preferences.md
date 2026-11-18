# CRM: Consent and Preferences Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#consent-and-preferences). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-crm-consent-and-preferences-vue-inertia`
**Matching domain module:** `crm-consent-and-preferences`
**Application:** CRM
**Source feature:** [Consent and Preferences](../features/consent-and-preferences.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/consent-and-preferences.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Lawful basis:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Subscriptions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Channel/topic preferences:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Suppression:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Quiet hours:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Recording consent:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Proof:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Expiry:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Withdrawal:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Policy evaluation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-crm-consent-and-preferences-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `lawful-basis`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `subscriptions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `channel-topic-preferences`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `suppression`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `quiet-hours`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `recording-consent`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `proof`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `expiry`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `withdrawal`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `policy-evaluation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-consent-and-preferences` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-crm-laravel-inertia-vue`](https://github.com/liberusoftware/project-crm-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-crm-consent-and-preferences-vue-inertia`](https://github.com/liberusoftware/module-crm-consent-and-preferences-vue-inertia) (`@liberusoftware/module-crm-consent-and-preferences-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/consent-and-preferences.md) · [Core plan](../core/consent-and-preferences.md) · [API plan](../api/consent-and-preferences.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Lawful basis** | Render `lawful basis` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Subscriptions** | Render `subscriptions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Channel/topic preferences** | Render `channel/topic preferences` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Suppression** | Render `suppression` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Quiet hours** | Render `quiet hours` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Recording consent** | Render `recording consent` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Proof** | Render `proof` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Expiry** | Render `expiry` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Withdrawal** | Render `withdrawal` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Policy evaluation** | Render `policy evaluation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [GrantConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Actions/GrantConsent.php) | `public function execute(int $teamId, string $subjectType, int $subjectId, array $attributes, ?int $actorId = null): ConsentRecord` |
| [SetPreference.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Actions/SetPreference.php) | `public function execute(int $teamId, string $subjectType, int $subjectId, string $channel, string $topic, array $values, ?int $actorId = null): PreferenceRecord` |
| [SuppressSubject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Actions/SuppressSubject.php) | `public function execute(int $teamId, string $subjectType, int $subjectId, array $attributes, ?int $actorId = null): SuppressionRecord` |
| [WithdrawConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Actions/WithdrawConsent.php) | `public function execute(ConsentRecord $record): ConsentRecord` |
| [PolicyEvaluator.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Services/PolicyEvaluator.php) | `public function evaluate(int $teamId, string $subjectType, int $subjectId, string $channel, string $topic = 'general', ?Carbon $at = null): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ConsentRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Models/ConsentRecord.php) | `team_id`, `subject_type`, `subject_id`, `channel`, `topic`, `lawful_basis`, `status`, `source`, `proof`, `consented_at`, `expires_at`, `withdrawn_at`, `actor_id` |
| [PolicyEvaluation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Models/PolicyEvaluation.php) | `team_id`, `subject_type`, `subject_id`, `channel`, `topic`, `allowed`, `reasons`, `evaluated_at` |
| [PreferenceRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Models/PreferenceRecord.php) | `team_id`, `subject_type`, `subject_id`, `channel`, `topic`, `state`, `quiet_hours`, `timezone`, `actor_id` |
| [SuppressionRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences/src/Models/SuppressionRecord.php) | `team_id`, `subject_type`, `subject_id`, `channel`, `topic`, `reason`, `source`, `expires_at`, `withdrawn_at`, `actor_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ConsentController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences-api/src/Http/Controllers/ConsentController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, GrantConsent $grant, SetPreference $preference): JsonResponse`<br>`public function show(Request $request, int $consent): JsonResponse`<br>`public function update(Request $request, int $consent): JsonResponse`<br>`public function withdraw(Request $request, int $consent, WithdrawConsent $withdraw): JsonResponse`<br>`public function evaluate(Request $request, PolicyEvaluator $evaluator): JsonResponse` |

**Observed route declarations:**

[modules/crm-consent-and-preferences-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-consent-and-preferences-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/consent-and-preferences')->group(function (): void {
Route::get('/', [ConsentController::class, 'index']);
Route::post('/', [ConsentController::class, 'store']);
Route::get('/{consent}', [ConsentController::class, 'show']);
Route::patch('/{consent}', [ConsentController::class, 'update']);
Route::post('/{consent}/withdraw', [ConsentController::class, 'withdraw']);
Route::post('/evaluate', [ConsentController::class, 'evaluate']);
```
<!-- layer-implementation-plan:end -->
