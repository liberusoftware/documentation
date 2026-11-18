# Accounting: Xero Migration React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#xero-migration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-accounting-xero-migration-react-inertia`
**Matching domain module:** `accounting-xero-migration`
**Application:** Accounting
**Source feature:** [Xero Migration](../features/xero-migration.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/xero-migration.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Chart/tracking categories:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Contacts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Items:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Invoices/bills/credits/payments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Bank:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Tax:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Assets:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Projects:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Expense claims:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Attachments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Source IDs:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-accounting-xero-migration-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `chart-tracking-categories`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `contacts`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `items`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `invoices-bills-credits-payments`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `bank`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `tax`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `assets`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `projects`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `expense-claims`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `attachments`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `source-ids`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-xero-migration` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-accounting-erp-laravel-inertia-react`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-accounting-xero-migration-react-inertia`](https://github.com/liberusoftware/module-accounting-xero-migration-react-inertia) (`@liberusoftware/module-accounting-xero-migration-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/xero-migration.md) · [Core plan](../core/xero-migration.md) · [API plan](../api/xero-migration.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Chart/tracking categories** | Render `chart/tracking categories` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Contacts** | Render `contacts` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Items** | Render `items` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Invoices/bills/credits/payments** | Render `invoices/bills/credits/payments` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Bank** | Render `bank` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Tax** | Render `tax` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Assets** | Render `assets` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Projects** | Render `projects` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Expense claims** | Render `expense claims` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Attachments** | Render `attachments` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Source IDs** | Render `source ids` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConnectXeroTenant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration/src/Actions/ConnectXeroTenant.php) | `public function handle(array $attributes): XeroConnection` |
| [RecordMigration.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration/src/Actions/RecordMigration.php) | `public function handle(XeroConnection $connection, array $attributes): XeroMigrationRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [XeroConnection.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration/src/Models/XeroConnection.php) | `team_id`, `tenant_ref`, `access_token`, `refresh_token`, `token_expires_at`, `status`, `last_synced_at`, `metadata` |
| [XeroMigrationRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration/src/Models/XeroMigrationRecord.php) | `team_id`, `connection_id`, `source_type`, `source_id`, `target_type`, `target_id`, `status`, `error`, `payload` |

| Observed API controller | Handler signatures |
| --- | --- |
| [XeroMigrationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration-api/src/Http/Controllers/XeroMigrationController.php) | `public function connections(Request $request): mixed`<br>`public function connect(Request $request, ConnectXeroTenant $action): mixed`<br>`public function record(Request $request, string $connection, RecordMigration $action): mixed` |

**Observed route declarations:**

[modules/accounting-xero-migration-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/xero-migration')->middleware(['auth:sanctum'])->group(function (): void {
Route::get('/connections', [XeroMigrationController::class, 'connections'])->middleware('ability:accounting.xero-migration.read');
Route::post('/connections', [XeroMigrationController::class, 'connect'])->middleware('ability:accounting.xero-migration.write');
Route::post('/connections/{connection}/records', [XeroMigrationController::class, 'record'])->middleware('ability:accounting.xero-migration.write');
```
<!-- layer-implementation-plan:end -->
