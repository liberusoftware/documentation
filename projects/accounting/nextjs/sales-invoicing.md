# Sales Invoicing: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter over a published capability skeleton, not a certified npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-sales-invoicing`.<br>
**Matching domain module:** `sales-invoicing`

**Proposed design identifier:** `module-accounting-sales-invoicing-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope, skeleton repositories, and backend ownership

The [domain specification](../features/sales-invoicing.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Next.js host skeleton | [`project-accounting-erp-next-react`](https://github.com/liberusoftware/project-accounting-erp-next-react) | Application App Router shell, session/BFF boundary, layout, and route composition ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Product HTTP composition root publishing versioned `/api/v1` contracts ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/sales-invoicing.md)) |
| Capability Next.js module skeleton | [module-accounting-sales-invoicing-nextjs](https://github.com/liberusoftware/module-accounting-sales-invoicing-nextjs) (`@liberusoftware/module-accounting-sales-invoicing-nextjs`) | Reusable React Server/Client component and typed DTO adapter ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-sales-invoicing](../../../modules/source/liberusoftware--module-accounting-sales-invoicing.md) |
| API | [liberusoftware/module-accounting-sales-invoicing-api](../../../modules/source/liberusoftware--module-accounting-sales-invoicing-api.md) |

## Module surfaces and component contracts

| Capability / feature aspect | Next.js Server & Client Component boundary | API transport, caching & recovery contract |
| --- | --- | --- |
| **Draft/approved/final invoices** | Server Component loads authorized `draft/approved/final invoices` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-accounting-erp-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Line items** | Server Component loads authorized `line items` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-accounting-erp-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Tax** | Server Component loads authorized `tax` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-accounting-erp-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Discounts** | Server Component loads authorized `discounts` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-accounting-erp-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Deposits** | Server Component loads authorized `deposits` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-accounting-erp-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Recurring sources** | Server Component loads authorized `recurring sources` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-accounting-erp-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Branding** | Server Component loads authorized `branding` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-accounting-erp-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **PDFs** | Server Component loads authorized `pdfs` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-accounting-erp-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Delivery** | Server Component loads authorized `delivery` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-accounting-erp-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Immutability** | Server Component loads authorized `immutability` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-accounting-erp-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [ApproveInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/ApproveInvoice.php) | `public function handle(SalesInvoice $invoice): SalesInvoice` |
| [CreateInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/CreateInvoice.php) | `public function handle(array $attributes, array $lines): SalesInvoice` |
| [FinalizeInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/FinalizeInvoice.php) | `public function handle(SalesInvoice $invoice, ?string $actor = null): SalesInvoice` |
| [GenerateInvoicePdf.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/GenerateInvoicePdf.php) | `public function handle(SalesInvoice $invoice, string $format = 'pdf'): array` |
| [MarkInvoiceDelivered.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/MarkInvoiceDelivered.php) | `public function handle(SalesInvoice $invoice): SalesInvoice` |
| [RecordDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/RecordDeposit.php) | `public function handle(SalesInvoice $invoice, array $attributes): SalesInvoice` |
| [SetInvoiceBranding.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/SetInvoiceBranding.php) | `public function handle(SalesInvoice $invoice, array $branding): SalesInvoice` |
| [SetRecurringSource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/SetRecurringSource.php) | `public function handle(SalesInvoice $invoice, array $source): SalesInvoice` |
| [SalesInvoicingPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-api/src/Policies/SalesInvoicingPolicy.php) | `public function viewAny(?Authenticatable $u): bool`<br>`public function view(?Authenticatable $u, SalesInvoice $i): bool`<br>`public function create(?Authenticatable $u): bool`<br>`public function update(?Authenticatable $u, SalesInvoice $i): bool`<br>`public function delete(?Authenticatable $u, SalesInvoice $i): bool` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [SalesInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Models/SalesInvoice.php) | `invoice_number`, `party_id`, `invoice_date`, `due_on`, `status`, `subtotal`, `discount_total`, `tax_total`, `total`, `currency`, `notes`, `branding`, `recurring_source`, `delivery_status`, `delivered_at`, `metadata` |
| [SalesInvoiceDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Models/SalesInvoiceDeposit.php) | `invoice_id`, `amount`, `currency`, `reference`, `received_by` |
| [SalesInvoiceLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Models/SalesInvoiceLine.php) | `invoice_id`, `description`, `quantity`, `unit_price`, `discount_rate`, `tax_rate`, `net_amount`, `tax_amount`, `metadata` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-sales-invoicing-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:60,1'])->prefix('api/v1/accounting/sales-invoicing')->group(function (): void {
Route::get('/', [SalesInvoicingController::class, 'index'])->middleware('ability:accounting.invoices.read');
Route::post('/', [SalesInvoicingController::class, 'store'])->middleware('ability:accounting.invoices.write');
Route::get('/{invoice}', [SalesInvoicingController::class, 'show'])->middleware('ability:accounting.invoices.read');
Route::post('/{invoice}/approve', [SalesInvoicingController::class, 'approve'])->middleware('ability:accounting.invoices.write');
Route::post('/{invoice}/finalize', [SalesInvoicingController::class, 'finalize'])->middleware('ability:accounting.invoices.write');
Route::post('/{invoice}/deposit', [SalesInvoicingController::class, 'deposit'])->middleware('ability:accounting.invoices.write');
Route::post('/{invoice}/deliver', [SalesInvoicingController::class, 'deliver'])->middleware('ability:accounting.invoices.write');
Route::delete('/{invoice}', [SalesInvoicingController::class, 'destroy'])->middleware('ability:accounting.invoices.write');
```

## Server/client and React reuse

Keep API credentials and session forwarding in server-only exports. A Server Component may load authorized serializable data and compose a Client Component for interaction. Put ordinary event callbacks inside the client boundary; server-to-client props must follow the framework serialization/action rules.

Share framework-independent React cards, tables, labels, formatting and field primitives with Inertia. Keep `next/link`, Next.js navigation, server actions and cache invalidation in this adapter, and Inertia visits, page props and redirects in its wrapper. Reuse domain/API DTOs without importing PHP models or another application's private frontend state.

## State, failures and verification

| Situation | User-facing behavior and integration requirement |
| --- | --- |
| Loading or empty authorized query | Accessible progress/empty copy; preserve filters and avoid displaying stale records from another scope |
| Expired session or denied permission | Reauthenticate or show a scoped denial; discard protected cached data and do not retry as a broader service identity |
| Invalid command input | Preserve safe draft values, announce field errors and use the authoritative API validation outcome |
| Stale record / concurrent change | Reload/review the current version; do not overwrite silently or invent an ETag contract the API does not support |
| Timeout after a write | Query the operation/current record when supported before retrying; an idempotency key works only if the owning API actually stores/enforces it |
| Long-running or partly failed operation | Show a durable operation reference, progress, last error and a permitted retry/recovery action |

Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware caching policy exists. Refresh affected read models after confirmed mutations; pending transport acceptance is not a completed business transition. Recheck access for evidence/export downloads.

Verify the actual supported query/command journeys, invalid and denied paths, tenant switching, stale state, retry recovery, keyboard/focus behavior and secret exclusion from browser bundles. Build/test the packed adapter in a clean consuming Next.js application using its declared versions and API contract. No npm package or application suite was executed by this plan generator.

See the [Next.js standard](../../../standards/NEXTJS.md), [npm lifecycle guide](../../../guides/NPM.md), [API architecture](../../../architecture/API.md), and [shared ownership guide](../../../architecture/SHARED-MODULES.md).
