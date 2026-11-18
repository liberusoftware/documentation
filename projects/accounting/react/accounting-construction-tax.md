# Accounting: Accounting Construction Tax React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-construction-tax). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-accounting-accounting-construction-tax-react-inertia`
**Matching domain module:** `accounting-construction-tax`
**Application:** Accounting
**Source feature:** [Accounting Construction Tax](../features/accounting-construction-tax.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-construction-tax.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **CIS-style subcontractor verification:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Deduction rates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Statements:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Monthly returns:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Corrections:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Filing adapters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-accounting-accounting-construction-tax-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `cis-style-subcontractor-verification`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `deduction-rates`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `statements`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `monthly-returns`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `corrections`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `filing-adapters`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-construction-tax` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-accounting-erp-laravel-inertia-react`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-accounting-construction-tax-react-inertia`](https://github.com/liberusoftware/module-accounting-construction-tax-react-inertia) (`@liberusoftware/module-accounting-construction-tax-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/accounting-construction-tax.md) · [Core plan](../core/accounting-construction-tax.md) · [API plan](../api/accounting-construction-tax.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **CIS-style subcontractor verification** | Render `cis-style subcontractor verification` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Deduction rates** | Render `deduction rates` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Statements** | Render `statements` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Monthly returns** | Render `monthly returns` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Corrections** | Render `corrections` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Filing adapters** | Render `filing adapters` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ConstructionTaxQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Queries/ConstructionTaxQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CorrectConstructionTaxReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Actions/CorrectConstructionTaxReturn.php) | `public function handle(ConstructionTaxRecord $record, array $correction): ConstructionTaxRecord` |
| [CreateConstructionTaxRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Actions/CreateConstructionTaxRecord.php) | `public function handle(array $attributes): ConstructionTaxRecord` |
| [IssueConstructionTaxStatement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Actions/IssueConstructionTaxStatement.php) | `public function handle(ConstructionTaxRecord $record, array $statement): ConstructionTaxRecord` |
| [SubmitConstructionTaxReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Actions/SubmitConstructionTaxReturn.php) | `public function handle(ConstructionTaxRecord $record, string $adapter): ConstructionTaxRecord` |
| [VerifySubcontractor.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Actions/VerifySubcontractor.php) | `public function handle(ConstructionTaxRecord $record, array $verification): ConstructionTaxRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ConstructionTaxRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Models/ConstructionTaxRecord.php) | `team_id`, `subcontractor_ref`, `verification_status`, `deduction_rate`, `tax_period`, `gross_amount`, `deduction_amount`, `return_status`, `filing_adapter`, `verification`, `statement`, `correction` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ConstructionTaxController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax-api/src/Http/Controllers/ConstructionTaxController.php) | `public function index(ConstructionTaxQuery $query): JsonResponse`<br>`public function store(Request $request, CreateConstructionTaxRecord $action): JsonResponse`<br>`public function verify(Request $request, string $record, VerifySubcontractor $action): JsonResponse`<br>`public function submit(Request $request, string $record, SubmitConstructionTaxReturn $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-construction-tax-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/construction-tax')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.construction-tax.read')->get('/', [ConstructionTaxController::class, 'index']);
Route::middleware('ability:accounting.construction-tax.write')->group(function (): void {
Route::post('/', [ConstructionTaxController::class, 'store']);
Route::post('/{record}/verify', [ConstructionTaxController::class, 'verify']);
Route::post('/{record}/submit', [ConstructionTaxController::class, 'submit']);
```
<!-- layer-implementation-plan:end -->
