# Billing: Communications Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#communications). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-billing-communications-vue-inertia`
**Matching domain module:** `billing-communications`
**Application:** Billing
**Source feature:** [Communications](../features/communications.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/communications.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **VoIP/SMS service inventory:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Number lifecycle:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Usage/rating imports:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Provider adapters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-billing-communications-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `voip-sms-service-inventory`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `number-lifecycle`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `usage-rating-imports`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `provider-adapters`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `billing-communications` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-billing-laravel-inertia-vue`](https://github.com/liberusoftware/project-billing-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-billing-communications-vue-inertia`](https://github.com/liberusoftware/module-billing-communications-vue-inertia) (`@liberusoftware/module-billing-communications-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/communications.md) · [Core plan](../core/communications.md) · [API plan](../api/communications.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **VoIP/SMS service inventory** | Render `voip/sms service inventory` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Number lifecycle** | Render `number lifecycle` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Usage/rating imports** | Render `usage/rating imports` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Provider adapters** | Render `provider adapters` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListCommunicationRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Queries/ListCommunicationRecords.php) | `public function handle(string $model, int $teamId): Collection` |
| [ListCommunicationsRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Queries/ListCommunicationsRecords.php) | `public function handle(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCallRateRule.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/CreateCallRateRule.php) | `public function handle(int $teamId, array $attributes): CallRateRule` |
| [CreateCommunicationProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/CreateCommunicationProvider.php) | `public function handle(int $teamId, array $attributes): CommunicationProvider` |
| [CreateCommunicationService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/CreateCommunicationService.php) | `public function handle(int $teamId, array $attributes): CommunicationService` |
| [CreateVoipAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/CreateVoipAccount.php) | `public function handle(int $teamId, array $attributes): VoipAccount` |
| [ImportCommunicationUsage.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/ImportCommunicationUsage.php) | `public function handle(int $teamId, array $attributes): CommunicationUsageImport` |
| [IngestCallDetailRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/IngestCallDetailRecord.php) | `public function handle(VoipAccount $account, array $attributes): CallDetailRecord` |
| [ProvisionCommunicationNumber.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/ProvisionCommunicationNumber.php) | `public function handle(int $teamId, array $attributes): CommunicationNumber` |
| [ProvisionVoipAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/ProvisionVoipAccount.php) | `public function __construct(private VoiceProviderRegistry $providers)`<br>`public function handle(VoipAccount $account): VoipAccount` |
| [TransitionCommunicationNumber.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/TransitionCommunicationNumber.php) | `public function handle(CommunicationNumber $number, string $status): CommunicationNumber` |
| [TransitionCommunicationService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/TransitionCommunicationService.php) | `public function handle(CommunicationService $service, string $status): CommunicationService` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CallDetailRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/CallDetailRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [CallRateRule.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/CallRateRule.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommunicationNumber.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/CommunicationNumber.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommunicationProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/CommunicationProvider.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommunicationService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/CommunicationService.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommunicationUsageImport.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/CommunicationUsageImport.php) | No literal fillable array detected; inspect the model and API schema. |
| [VoipAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/VoipAccount.php) | No literal fillable array detected; inspect the model and API schema. |
| [VoipFraudAlert.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/VoipFraudAlert.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CommunicationsController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-api/src/Http/Controllers/CommunicationsController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, int $record): JsonResponse`<br>`public function createService(Request $request, CreateCommunicationService $create): JsonResponse`<br>`public function numbers(Request $request): JsonResponse`<br>`public function providers(Request $request): JsonResponse`<br>`public function usageImports(Request $request): JsonResponse`<br>`public function provisionNumber(Request $request, ProvisionCommunicationNumber $provision): JsonResponse`<br>`public function importUsage(Request $request, ImportCommunicationUsage $import): JsonResponse`<br>`public function transitionNumber(Request $request, int $number, TransitionCommunicationNumber $transition): JsonResponse`<br>`public function transitionService(Request $request, int $service, TransitionCommunicationService $transition): JsonResponse`<br>`public function createProvider(Request $request, CreateCommunicationProvider $create): JsonResponse`<br>`public function voiceAccounts(Request $request): JsonResponse`<br>`public function createVoiceAccount(Request $request, CreateVoipAccount $create): JsonResponse`<br>`public function provisionVoiceAccount(Request $request, int $account, ProvisionVoipAccount $provision): JsonResponse`<br>`public function rates(Request $request): JsonResponse`<br>`public function createRate(Request $request, CreateCallRateRule $create): JsonResponse`<br>`public function callRecords(Request $request, int $account): JsonResponse`<br>`public function ingestCallRecord(Request $request, int $account, IngestCallDetailRecord $ingest): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-communications-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.communications.read'])->prefix('api/v1/billing/communications')->group(function (): void {
Route::get('/voice/accounts', [CommunicationsController::class, 'voiceAccounts'])->name('billing.communications.voice.accounts.index');
Route::get('/voice/accounts/{account}/cdrs', [CommunicationsController::class, 'callRecords'])->whereNumber('account')->name('billing.communications.voice.cdrs.index');
Route::get('/voice/rates', [CommunicationsController::class, 'rates'])->name('billing.communications.voice.rates.index');
Route::get('/', [CommunicationsController::class, 'index'])->name('billing.communications.index');
Route::get('/numbers', [CommunicationsController::class, 'numbers'])->name('numbers');
Route::get('/providers', [CommunicationsController::class, 'providers'])->name('providers');
Route::get('/usage-imports', [CommunicationsController::class, 'usageImports'])->name('usage-imports');
Route::get('/{record}', [CommunicationsController::class, 'show'])->whereNumber('record')->name('billing.communications.show');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.communications.write', 'idempotency'])->prefix('api/v1/billing/communications')->group(function (): void {
Route::post('/voice/accounts', [CommunicationsController::class, 'createVoiceAccount'])->name('billing.communications.voice.accounts.store');
Route::post('/voice/accounts/{account}/provision', [CommunicationsController::class, 'provisionVoiceAccount'])->whereNumber('account')->name('billing.communications.voice.accounts.provision');
Route::post('/voice/accounts/{account}/cdrs', [CommunicationsController::class, 'ingestCallRecord'])->whereNumber('account')->name('billing.communications.voice.cdrs.store');
Route::post('/voice/rates', [CommunicationsController::class, 'createRate'])->name('billing.communications.voice.rates.store');
Route::post('/', [CommunicationsController::class, 'createService'])->name('billing.communications.store');
Route::patch('/{service}/lifecycle', [CommunicationsController::class, 'transitionService'])->whereNumber('service')->name('billing.communications.services.lifecycle');
Route::post('/numbers', [CommunicationsController::class, 'provisionNumber'])->name('billing.communications.numbers.store');
Route::patch('/numbers/{number}/status', [CommunicationsController::class, 'transitionNumber'])->whereNumber('number')->name('billing.communications.numbers.status');
Route::post('/providers', [CommunicationsController::class, 'createProvider'])->name('billing.communications.providers.store');
Route::post('/usage-imports', [CommunicationsController::class, 'importUsage'])->name('billing.communications.usage-imports.store');
```
<!-- layer-implementation-plan:end -->
