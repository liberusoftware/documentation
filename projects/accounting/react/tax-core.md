# Accounting: Tax Core React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#tax-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-accounting-tax-core-react-inertia`
**Matching domain module:** `accounting-tax-core`
**Application:** Accounting
**Source feature:** [Tax Core](../features/tax-core.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/tax-core.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Tax types/codes/rates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Inclusive/exclusive treatment:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Jurisdictions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Effective dates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Exemptions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Rounding:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Evidence:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Control accounts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-accounting-tax-core-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `tax-types-codes-rates`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `inclusive-exclusive-treatment`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `jurisdictions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `effective-dates`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `exemptions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `rounding`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `evidence`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `control-accounts`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-tax-core` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-accounting-erp-laravel-inertia-react`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-accounting-tax-core-react-inertia`](https://github.com/liberusoftware/module-accounting-tax-core-react-inertia) (`@liberusoftware/module-accounting-tax-core-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/tax-core.md) · [Core plan](../core/tax-core.md) · [API plan](../api/tax-core.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Tax types/codes/rates** | Render `tax types/codes/rates` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Inclusive/exclusive treatment** | Render `inclusive/exclusive treatment` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Jurisdictions** | Render `jurisdictions` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Effective dates** | Render `effective dates` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Exemptions** | Render `exemptions` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Rounding** | Render `rounding` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Evidence** | Render `evidence` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Control accounts** | Render `control accounts` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ActiveTaxRuleQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Queries/ActiveTaxRuleQuery.php) | `public function handle(string $code, ?string $jurisdiction = null, ?string $on = null): ?TaxRule` |
| [TaxRuleQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Queries/TaxRuleQuery.php) | `public function paginate(?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/ActivateTaxRule.php) | `public function handle(TaxRule $rule): TaxRule` |
| [ArchiveTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/ArchiveTaxRule.php) | `public function handle(TaxRule $rule): TaxRule` |
| [CalculateTax.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/CalculateTax.php) | `public function handle(TaxRule $rule, float $amount): array` |
| [CaptureTaxEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/CaptureTaxEvidence.php) | `public function handle(TaxRule $rule, string $sourceType, string $sourceId, array $snapshot, ?int $actorId = null): TaxEvidence` |
| [CreateTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/CreateTaxRule.php) | `public function handle(array $attributes): TaxRule` |
| [UpdateTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/UpdateTaxRule.php) | `public function handle(TaxRule $rule, array $attributes): TaxRule` |
| [TaxCorePolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core-api/src/Policies/TaxCorePolicy.php) | `public function viewAny($user): bool`<br>`public function view($user, TaxRule $rule): bool`<br>`public function create($user): bool`<br>`public function update($user, TaxRule $rule): bool`<br>`public function delete($user, TaxRule $rule): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TaxEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Models/TaxEvidence.php) | `tax_rule_id`, `source_type`, `source_id`, `snapshot_hash`, `snapshot`, `captured_by`, `metadata` |
| [TaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Models/TaxRule.php) | `code`, `name`, `tax_type`, `jurisdiction_code`, `rate`, `treatment`, `effective_from`, `effective_until`, `status`, `exemption_code`, `control_account_code`, `rounding_method`, `rounding_scale`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [TaxRuleController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core-api/src/Http/Controllers/TaxRuleController.php) | `public function index(Request $request): mixed`<br>`public function show(TaxRule $taxRule): TaxRuleResource`<br>`public function store(Request $request, CreateTaxRule $action): mixed`<br>`public function update(Request $request, TaxRule $taxRule, UpdateTaxRule $action): TaxRuleResource`<br>`public function activate(TaxRule $taxRule, ActivateTaxRule $action): TaxRuleResource`<br>`public function archive(TaxRule $taxRule, ArchiveTaxRule $action): TaxRuleResource` |

**Observed route declarations:**

[modules/accounting-tax-core-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/tax-core')->group(function (): void {
Route::middleware('ability:accounting.tax-core.read')->group(function (): void {
Route::get('/', [TaxRuleController::class, 'index']);
Route::get('/{taxRule}', [TaxRuleController::class, 'show']);
Route::middleware('ability:accounting.tax-core.write')->group(function (): void {
Route::post('/', [TaxRuleController::class, 'store']);
Route::patch('/{taxRule}', [TaxRuleController::class, 'update']);
Route::post('/{taxRule}/activate', [TaxRuleController::class, 'activate']);
Route::post('/{taxRule}/archive', [TaxRuleController::class, 'archive']);
```
<!-- layer-implementation-plan:end -->
