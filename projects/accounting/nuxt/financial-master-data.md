# Accounting: Financial Master Data Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#financial-master-data). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-financial-master-data-nuxt`
**Matching domain module:** `accounting-financial-master-data`
**Application:** Accounting
**Source feature:** [Financial Master Data](../features/financial-master-data.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/financial-master-data.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-financial-master-data` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Customers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Suppliers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Items/services:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Accounts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tax profiles:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Payment terms:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Addresses:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Bank details references:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Lifecycle:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Deduplication:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-financial-master-data-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `customers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `suppliers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `items-services`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `accounts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tax-profiles`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `payment-terms`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `addresses`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `bank-details-references`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `lifecycle`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `deduplication`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-financial-master-data` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/financial-master-data.md)) |
| Capability Nuxt module skeleton | [`module-accounting-financial-master-data-nuxt`](https://github.com/liberusoftware/module-accounting-financial-master-data-nuxt) (`@liberusoftware/module-accounting-financial-master-data-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Customers** | Expose composable and Vue 3 component for `customers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/financial-master-data.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Suppliers** | Expose composable and Vue 3 component for `suppliers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/financial-master-data.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Items/services** | Expose composable and Vue 3 component for `items/services` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/financial-master-data.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Accounts** | Expose composable and Vue 3 component for `accounts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/financial-master-data.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Tax profiles** | Expose composable and Vue 3 component for `tax profiles` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/financial-master-data.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Payment terms** | Expose composable and Vue 3 component for `payment terms` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/financial-master-data.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Addresses** | Expose composable and Vue 3 component for `addresses` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/financial-master-data.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Bank details references** | Expose composable and Vue 3 component for `bank details references` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/financial-master-data.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Lifecycle** | Expose composable and Vue 3 component for `lifecycle` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/financial-master-data.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Deduplication** | Expose composable and Vue 3 component for `deduplication` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/financial-master-data.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [FindDuplicateParties.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Queries/FindDuplicateParties.php) | `public function handle(int $legalEntityId, ?string $type = null): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ArchiveParty.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Actions/ArchiveParty.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(Party $party): Party` |
| [MergeDuplicateParties.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Actions/MergeDuplicateParties.php) | `public function handle(Party $survivor, Party $duplicate): Party` |
| [SaveParty.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Actions/SaveParty.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(array $attributes, ?Party $party = null): Party` |
| [SaveReferenceData.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Actions/SaveReferenceData.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(string $modelClass, array $attributes, ?Model $record = null): Model` |
| [PartyPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data-api/src/Policies/PartyPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, Party $party): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, Party $party): bool`<br>`public function delete(?Authenticatable $user, Party $party): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Address.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Models/Address.php) | `party_id`, `kind`, `line_one`, `line_two`, `city`, `region`, `postal_code`, `country_code`, `is_primary`, `metadata` |
| [BankDetailReference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Models/BankDetailReference.php) | `party_id`, `label`, `account_name`, `bank_name`, `country_code`, `currency_code`, `masked_account`, `credential_reference`, `is_primary`, `status`, `metadata` |
| [ItemService.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Models/ItemService.php) | `legal_entity_id`, `sku`, `name`, `description`, `kind`, `unit`, `sales_price`, `purchase_price`, `tax_profile_id`, `status`, `metadata` |
| [Party.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Models/Party.php) | `legal_entity_id`, `type`, `reference`, `name`, `email`, `phone`, `tax_identifier`, `payment_term_id`, `credit_limit`, `status`, `metadata` |
| [PaymentTerm.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Models/PaymentTerm.php) | `legal_entity_id`, `code`, `name`, `days`, `status`, `metadata` |
| [TaxProfile.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Models/TaxProfile.php) | `legal_entity_id`, `code`, `name`, `rate`, `inclusive`, `recoverable`, `status`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PartyController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data-api/src/Http/Controllers/PartyController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(string $party): PartyResource`<br>`public function store(StorePartyRequest $request, SaveParty $save): JsonResponse`<br>`public function update(UpdatePartyRequest $request, string $party, SaveParty $save): PartyResource`<br>`public function destroy(string $party, ArchiveParty $archive): Response` |
| [PartyDetailController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data-api/src/Http/Controllers/PartyDetailController.php) | `public function index(string $party, string $detail): JsonResponse`<br>`public function store(StorePartyDetailRequest $request, string $party, string $detail, SaveReferenceData $save): JsonResponse`<br>`public function destroy(string $party, string $detail, string $record): Response` |
| [ReferenceDataController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data-api/src/Http/Controllers/ReferenceDataController.php) | `public function index(Request $request, string $resource): JsonResponse`<br>`public function show(string $resource, string $record): ReferenceDataResource`<br>`public function store(StoreReferenceDataRequest $request, string $resource, SaveReferenceData $save): JsonResponse`<br>`public function update(UpdateReferenceDataRequest $request, string $resource, string $record, SaveReferenceData $save): ReferenceDataResource`<br>`public function destroy(string $resource, string $record): Response` |

**Observed route declarations:**

[modules/accounting-financial-master-data-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/financial-master-data')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('parties', [PartyController::class, 'index'])->middleware('ability:accounting.master-data.read');
Route::get('parties/{party}', [PartyController::class, 'show'])->middleware('ability:accounting.master-data.read');
Route::post('parties', [PartyController::class, 'store'])->middleware('ability:accounting.master-data.write');
Route::delete('parties/{party}', [PartyController::class, 'destroy'])->middleware('ability:accounting.master-data.write');
Route::get('parties/{party}/'.$detail, [PartyDetailController::class, 'index'])->defaults('detail', $detail)->middleware('ability:accounting.master-data.read');
Route::post('parties/{party}/'.$detail, [PartyDetailController::class, 'store'])->defaults('detail', $detail)->middleware('ability:accounting.master-data.write');
Route::delete('parties/{party}/'.$detail.'/{record}', [PartyDetailController::class, 'destroy'])->defaults('detail', $detail)->middleware('ability:accounting.master-data.write');
Route::get($resource, [ReferenceDataController::class, 'index'])->defaults('resource', $resource)->middleware('ability:accounting.master-data.read');
Route::get($resource.'/{record}', [ReferenceDataController::class, 'show'])->defaults('resource', $resource)->middleware('ability:accounting.master-data.read');
Route::post($resource, [ReferenceDataController::class, 'store'])->defaults('resource', $resource)->middleware('ability:accounting.master-data.write');
Route::delete($resource.'/{record}', [ReferenceDataController::class, 'destroy'])->defaults('resource', $resource)->middleware('ability:accounting.master-data.write');
```
<!-- layer-implementation-plan:end -->
