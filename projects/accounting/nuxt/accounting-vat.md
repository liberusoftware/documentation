# Accounting: Accounting Vat Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-vat). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-vat-nuxt`
**Matching domain module:** `accounting-vat`
**Application:** Accounting
**Source feature:** [Accounting Vat](../features/accounting-vat.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-vat.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-vat` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Input/output VAT:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reverse charge:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Partial exemption hooks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Import/export:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Schemes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Boxes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Adjustments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Digital records:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Audit trail:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-vat-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `input-output-vat`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reverse-charge`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `partial-exemption-hooks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `import-export`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `schemes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `boxes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `adjustments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `digital-records`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `audit-trail`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-vat` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-vat.md)) |
| Capability Nuxt module skeleton | [`module-accounting-vat-nuxt`](https://github.com/liberusoftware/module-accounting-vat-nuxt) (`@liberusoftware/module-accounting-vat-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Input/output VAT** | Expose composable and Vue 3 component for `input/output vat` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-vat.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reverse charge** | Expose composable and Vue 3 component for `reverse charge` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-vat.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Partial exemption hooks** | Expose composable and Vue 3 component for `partial exemption hooks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-vat.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Import/export** | Expose composable and Vue 3 component for `import/export` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-vat.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Schemes** | Expose composable and Vue 3 component for `schemes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-vat.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Boxes** | Expose composable and Vue 3 component for `boxes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-vat.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Adjustments** | Expose composable and Vue 3 component for `adjustments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-vat.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Digital records** | Expose composable and Vue 3 component for `digital records` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-vat.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Audit trail** | Expose composable and Vue 3 component for `audit trail` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-vat.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [VatReturnBoxes.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat/src/Queries/VatReturnBoxes.php) | `public function handle(VatReturn $vatReturn): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddVatAdjustment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat/src/Actions/AddVatAdjustment.php) | `public function handle(VatReturn $vatReturn, array $attributes): VatAdjustment` |
| [CreateVatReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat/src/Actions/CreateVatReturn.php) | `public function handle(array $attributes): VatReturn` |
| [RecordVatDigitalEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat/src/Actions/RecordVatDigitalEvidence.php) | `public function handle(VatRecord $vatRecord, array $payload): VatDigitalRecord` |
| [RecordVatTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat/src/Actions/RecordVatTransaction.php) | `public function handle(array $attributes): VatRecord` |
| [SubmitVatReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat/src/Actions/SubmitVatReturn.php) | `public function handle(VatReturn $vatReturn, ?string $submissionRef = null): VatReturn` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [VatAdjustment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat/src/Models/VatAdjustment.php) | `vat_return_id`, `box`, `amount`, `reason`, `created_by` |
| [VatDigitalRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat/src/Models/VatDigitalRecord.php) | `vat_record_id`, `record_hash`, `payload`, `recorded_at` |
| [VatRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat/src/Models/VatRecord.php) | `team_id`, `direction`, `tax_code`, `net_amount`, `tax_amount`, `tax_rate`, `reverse_charge`, `scheme`, `box`, `source_type`, `source_id`, `status`, `occurred_on`, `evidence`, `metadata` |
| [VatReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat/src/Models/VatReturn.php) | `team_id`, `period_start`, `period_end`, `scheme`, `status`, `boxes`, `submitted_at`, `submission_ref`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [VatController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat-api/src/Http/Controllers/VatController.php) | `public function records(Request $request): mixed`<br>`public function record(Request $request, RecordVatTransaction $action): mixed`<br>`public function digitalEvidence(Request $request, string $record, RecordVatDigitalEvidence $action): mixed`<br>`public function returns(Request $request, VatReturnBoxes $boxes): mixed`<br>`public function createReturn(Request $request, CreateVatReturn $action): mixed`<br>`public function adjustment(Request $request, string $vatReturn, AddVatAdjustment $action): mixed`<br>`public function submit(Request $request, string $vatReturn, SubmitVatReturn $action): mixed` |

**Observed route declarations:**

[modules/accounting-vat-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/vat')->middleware('auth:sanctum')->group(function (): void {
Route::get('/records', [VatController::class, 'records'])->middleware('ability:accounting.vat.read');
Route::post('/records', [VatController::class, 'record'])->middleware('ability:accounting.vat.write');
Route::post('/records/{record}/digital-evidence', [VatController::class, 'digitalEvidence'])->middleware('ability:accounting.vat.write');
Route::get('/returns', [VatController::class, 'returns'])->middleware('ability:accounting.vat.read');
Route::post('/returns', [VatController::class, 'createReturn'])->middleware('ability:accounting.vat.write');
Route::post('/returns/{vatReturn}/adjustments', [VatController::class, 'adjustment'])->middleware('ability:accounting.vat.write');
Route::post('/returns/{vatReturn}/submit', [VatController::class, 'submit'])->middleware('ability:accounting.vat.write');
```
<!-- layer-implementation-plan:end -->
