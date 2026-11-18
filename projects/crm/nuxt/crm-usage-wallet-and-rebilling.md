# CRM: Crm Usage Wallet And Rebilling Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-usage-wallet-and-rebilling). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-usage-wallet-and-rebilling-nuxt`
**Matching domain module:** `crm-usage-wallet-and-rebilling`
**Application:** CRM
**Source feature:** [Crm Usage Wallet And Rebilling](../features/crm-usage-wallet-and-rebilling.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-usage-wallet-and-rebilling.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-usage-wallet-and-rebilling` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Provider usage imports:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Wallets/credits:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Threshold reloads:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cost/markup rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Client charges:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Exceptions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Billing/Accounting handoff:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-usage-wallet-and-rebilling-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `provider-usage-imports`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `wallets-credits`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `threshold-reloads`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cost-markup-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `client-charges`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `exceptions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reconciliation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `billing-accounting-handoff`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-usage-wallet-and-rebilling` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-usage-wallet-and-rebilling.md)) |
| Capability Nuxt module skeleton | [`module-crm-usage-wallet-and-rebilling-nuxt`](https://github.com/liberusoftware/module-crm-usage-wallet-and-rebilling-nuxt) (`@liberusoftware/module-crm-usage-wallet-and-rebilling-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Provider usage imports** | Expose composable and Vue 3 component for `provider usage imports` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-usage-wallet-and-rebilling.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Wallets/credits** | Expose composable and Vue 3 component for `wallets/credits` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-usage-wallet-and-rebilling.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Threshold reloads** | Expose composable and Vue 3 component for `threshold reloads` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-usage-wallet-and-rebilling.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Cost/markup rules** | Expose composable and Vue 3 component for `cost/markup rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-usage-wallet-and-rebilling.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Client charges** | Expose composable and Vue 3 component for `client charges` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-usage-wallet-and-rebilling.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Exceptions** | Expose composable and Vue 3 component for `exceptions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-usage-wallet-and-rebilling.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Reconciliation** | Expose composable and Vue 3 component for `reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-usage-wallet-and-rebilling.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Billing/Accounting handoff** | Expose composable and Vue 3 component for `billing/accounting handoff` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-usage-wallet-and-rebilling.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [UsageWalletQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Queries/UsageWalletQuery.php) | `public function wallet(int $teamId): ?UsageWallet`<br>`public function imports(int $teamId)`<br>`public function charges(int $teamId)`<br>`public function summary(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCharge.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Actions/CreateCharge.php) | `public function execute(int $teamId, int $actorId, array $data): UsageCharge` |
| [ImportProviderUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Actions/ImportProviderUsage.php) | `public function execute(int $teamId, int $actorId, array $data): UsageImport` |
| [ResolveUsageException.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Actions/ResolveUsageException.php) | `public function execute(int $teamId, int $actorId, int $exceptionId): void` |
| [UpsertWallet.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Actions/UpsertWallet.php) | `public function execute(int $teamId, int $actorId, array $data): UsageWallet` |
| [UsageAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Services/UsageAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): void` |
| [UsagePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Services/UsagePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [UsageAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Models/UsageAudit.php) | `team_id`, `actor_id`, `event`, `details`, `request_id` |
| [UsageCharge.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Models/UsageCharge.php) | `team_id`, `usage_import_id`, `wallet_id`, `client_reference`, `cost`, `charge`, `currency`, `status` |
| [UsageImport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Models/UsageImport.php) | `team_id`, `provider`, `external_id`, `amount`, `currency`, `status`, `failure_reason`, `payload` |
| [UsageWallet.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Models/UsageWallet.php) | `team_id`, `currency`, `balance`, `threshold`, `reload_amount`, `status`, `version` |

| Observed API controller | Handler signatures |
| --- | --- |
| [UsageWalletController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling-api/src/Http/Controllers/UsageWalletController.php) | `public function summary(Request $r, UsageWalletQuery $q): JsonResponse`<br>`public function imports(Request $r, UsageWalletQuery $q): JsonResponse`<br>`public function charges(Request $r, UsageWalletQuery $q): JsonResponse`<br>`public function import(Request $r, ImportProviderUsage $a): JsonResponse`<br>`public function charge(Request $r, CreateCharge $a): JsonResponse`<br>`public function wallet(Request $r, UpsertWallet $a): JsonResponse` |

**Observed route declarations:**

[modules/crm-usage-wallet-and-rebilling-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/usage-wallet-and-rebilling')->group(function () {
Route::get('/summary', [UsageWalletController::class, 'summary']);
Route::get('/imports', [UsageWalletController::class, 'imports']);
Route::post('/imports', [UsageWalletController::class, 'import']);
Route::get('/charges', [UsageWalletController::class, 'charges']);
Route::post('/charges', [UsageWalletController::class, 'charge']);
Route::put('/wallet', [UsageWalletController::class, 'wallet']);
```
<!-- layer-implementation-plan:end -->
