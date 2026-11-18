# Accounting: VAT React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#vat). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-accounting-vat-react-inertia`
**Matching domain module:** `accounting-vat`
**Application:** Accounting
**Source feature:** [VAT](../features/vat.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/vat.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Input/output VAT:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reverse charge:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Partial exemption hooks:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Import/export:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Schemes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Boxes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Adjustments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Digital records:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Audit trail:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-accounting-vat-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `input-output-vat`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `reverse-charge`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `partial-exemption-hooks`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `import-export`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `schemes`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `boxes`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `adjustments`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `digital-records`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `audit-trail`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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
- Test observable behavior with TypeScript, ESLint, Vitest, React Testing Library, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `accounting-vat` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-accounting-erp-laravel-inertia-react`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-accounting-vat-react-inertia`](https://github.com/liberusoftware/module-accounting-vat-react-inertia) (`@liberusoftware/module-accounting-vat-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/vat.md) · [Core plan](../core/vat.md) · [API plan](../api/vat.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Input/output VAT** | Render `input/output vat` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Reverse charge** | Render `reverse charge` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Partial exemption hooks** | Render `partial exemption hooks` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Import/export** | Render `import/export` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Schemes** | Render `schemes` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Boxes** | Render `boxes` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Adjustments** | Render `adjustments` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Digital records** | Render `digital records` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Audit trail** | Render `audit trail` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

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
