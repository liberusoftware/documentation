# Accounting: Accounting Financial Master Data Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-financial-master-data). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-accounting-financial-master-data-vue-inertia`
**Matching domain module:** `accounting-financial-master-data`
**Application:** Accounting
**Source feature:** [Accounting Financial Master Data](../features/accounting-financial-master-data.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-financial-master-data.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Customers:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Suppliers:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Items/services:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Accounts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Tax profiles:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Payment terms:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Addresses:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Bank details references:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Lifecycle:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Deduplication:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-accounting-financial-master-data-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `customers`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `suppliers`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `items-services`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `accounts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `tax-profiles`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `payment-terms`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `addresses`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `bank-details-references`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `lifecycle`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `deduplication`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-financial-master-data` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-financial-master-data-vue-inertia`](https://github.com/liberusoftware/module-accounting-financial-master-data-vue-inertia) (`@liberusoftware/module-accounting-financial-master-data-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/accounting-financial-master-data.md) · [Core plan](../core/accounting-financial-master-data.md) · [API plan](../api/accounting-financial-master-data.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Customers** | Render `customers` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Suppliers** | Render `suppliers` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Items/services** | Render `items/services` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Accounts** | Render `accounts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Tax profiles** | Render `tax profiles` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Payment terms** | Render `payment terms` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Addresses** | Render `addresses` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Bank details references** | Render `bank details references` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Lifecycle** | Render `lifecycle` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Deduplication** | Render `deduplication` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
