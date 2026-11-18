# Billing: Communications Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#communications). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-billing-communications-nuxt`
**Matching domain module:** `billing-communications`
**Application:** Billing
**Source feature:** [Communications](../features/communications.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/communications.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `billing-communications` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **VoIP/SMS service inventory:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Number lifecycle:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Usage/rating imports:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Provider adapters:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-billing-communications-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `voip-sms-service-inventory`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `number-lifecycle`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `usage-rating-imports`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `provider-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `billing-communications` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-billing-nuxt-vue`](https://github.com/liberusoftware/project-billing-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/communications.md)) |
| Capability Nuxt module skeleton | [`module-billing-communications-nuxt`](https://github.com/liberusoftware/module-billing-communications-nuxt) (`@liberusoftware/module-billing-communications-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **VoIP/SMS service inventory** | Expose composable and Vue 3 component for `voip/sms service inventory` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/communications.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Number lifecycle** | Expose composable and Vue 3 component for `number lifecycle` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/communications.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Usage/rating imports** | Expose composable and Vue 3 component for `usage/rating imports` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/communications.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Provider adapters** | Expose composable and Vue 3 component for `provider adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/communications.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |

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
