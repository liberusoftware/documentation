# Accounting: Accounting Payment Reconciliation React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-payment-reconciliation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-accounting-accounting-payment-reconciliation-react-inertia`
**Matching domain module:** `accounting-payment-reconciliation`
**Application:** Accounting
**Source feature:** [Accounting Payment Reconciliation](../features/accounting-payment-reconciliation.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-payment-reconciliation.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Gateway/merchant settlement imports:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Gross-to-net fees/refunds/disputes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Matching:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Missing items:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Provider drift:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-accounting-accounting-payment-reconciliation-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `gateway-merchant-settlement-imports`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `gross-to-net-fees-refunds-disputes`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `matching`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `missing-items`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `provider-drift`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-payment-reconciliation` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-accounting-erp-laravel-inertia-react`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-accounting-payment-reconciliation-react-inertia`](https://github.com/liberusoftware/module-accounting-payment-reconciliation-react-inertia) (`@liberusoftware/module-accounting-payment-reconciliation-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/accounting-payment-reconciliation.md) · [Core plan](../core/accounting-payment-reconciliation.md) · [API plan](../api/accounting-payment-reconciliation.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Gateway/merchant settlement imports** | Render `gateway/merchant settlement imports` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Gross-to-net fees/refunds/disputes** | Render `gross-to-net fees/refunds/disputes` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Matching** | Render `matching` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Missing items** | Render `missing items` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Provider drift** | Render `provider drift` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [SettlementQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Queries/SettlementQuery.php) | `public function paginate(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function summary(?int $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [IdentifyMissingItems.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/IdentifyMissingItems.php) | `public function handle(SettlementRun $run, array $expected): array` |
| [ImportSettlement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/ImportSettlement.php) | `public function handle(array $attributes, array $items): SettlementRun` |
| [MatchSettlementItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/MatchSettlementItem.php) | `public function handle(SettlementItem $item, string $referenceType, string $referenceId, float $amount, ?int $actorId = null, ?string $idempotencyKey = null): SettlementMatch` |
| [RecordProviderDrift.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/RecordProviderDrift.php) | `public function handle(SettlementRun $run, string $field, mixed $expected, mixed $actual, string $severity = 'warning'): ProviderDrift` |
| [ResolveReconciliationException.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/ResolveReconciliationException.php) | `public function handle(ReconciliationException $exception, int $actorId, string $resolution, bool $waive = false): ReconciliationException` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AuditEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/AuditEvidence.php) | `run_id`, `event_type`, `actor_id`, `payload`, `payload_hash`, `created_at` |
| [ProviderDrift.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/ProviderDrift.php) | `run_id`, `field`, `expected_value`, `actual_value`, `severity`, `status`, `resolution`, `resolved_by`, `resolved_at`, `metadata` |
| [ReconciliationException.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/ReconciliationException.php) | `run_id`, `kind`, `external_ref`, `expected_amount`, `actual_amount`, `currency`, `status`, `severity`, `resolution`, `resolved_by`, `resolved_at`, `metadata` |
| [SettlementItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/SettlementItem.php) | `run_id`, `external_ref`, `type`, `currency`, `gross_amount`, `fee_amount`, `refund_amount`, `dispute_amount`, `net_amount`, `status`, `reference_type`, `reference_id`, `source_payload`, `source_hash`, `metadata` |
| [SettlementMatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/SettlementMatch.php) | `run_id`, `item_id`, `reference_type`, `reference_id`, `matched_amount`, `confidence`, `status`, `matched_by`, `matched_at`, `idempotency_key`, `metadata` |
| [SettlementRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/SettlementRun.php) | `team_id`, `provider`, `merchant_ref`, `settlement_ref`, `period_start`, `period_end`, `currency`, `gross_amount`, `fee_amount`, `refund_amount`, `dispute_amount`, `net_amount`, `status`, `idempotency_key`, `source_hash`, `failure_message`, `metadata` |
| [Payment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-api/src/Models/Payment.php) | `invoice_id`, `payment_date`, `payment_amount`, `qbo_id`, `qbo_sync_token`, `xero_id`, `sage_id`, `journal_entry_id`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PaymentReconciliationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-api/src/Http/Controllers/PaymentReconciliationController.php) | `public function index(Request $request, SettlementQuery $query): mixed`<br>`public function store(Request $request, ImportSettlement $action): JsonResponse`<br>`public function show(SettlementRun $settlementRun): SettlementResource`<br>`public function match(Request $request, SettlementItem $settlementItem, MatchSettlementItem $action): JsonResponse`<br>`public function missing(Request $request, SettlementRun $settlementRun, IdentifyMissingItems $action): JsonResponse`<br>`public function drift(Request $request, SettlementRun $settlementRun, RecordProviderDrift $action): JsonResponse`<br>`public function summary(Request $request, SettlementQuery $query): array` |

**Observed route declarations:**

[modules/accounting-payment-reconciliation-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/payment-reconciliation')->group(function (): void {
Route::get('/', [PaymentReconciliationController::class, 'index'])->name('accounting.payment-reconciliation.list');
Route::post('/', [PaymentReconciliationController::class, 'store'])->name('accounting.payment-reconciliation.create');
Route::get('/summary', [PaymentReconciliationController::class, 'summary'])->name('accounting.payment-reconciliation.summary');
Route::get('/{settlementRun}', [PaymentReconciliationController::class, 'show'])->name('accounting.payment-reconciliation.show');
Route::post('/{settlementRun}/missing-items', [PaymentReconciliationController::class, 'missing'])->name('accounting.payment-reconciliation.missing');
Route::post('/{settlementRun}/provider-drift', [PaymentReconciliationController::class, 'drift'])->name('accounting.payment-reconciliation.drift');
Route::post('/items/{settlementItem}/match', [PaymentReconciliationController::class, 'match'])->name('accounting.payment-reconciliation.match');
```
<!-- layer-implementation-plan:end -->
