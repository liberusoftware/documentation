# Accounting: Sales Invoicing Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sales-invoicing). Observed identity: [`liberusoftware/module-accounting-sales-invoicing-filament`](../../../modules/source/liberusoftware--module-accounting-sales-invoicing-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-sales-invoicing-filament`  
**Matching domain module:** `accounting-sales-invoicing`  
**Application:** Accounting  
**Source feature:** [Sales Invoicing](../features/sales-invoicing.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-sales-invoicing` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Draft/approved/final invoices:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Line items:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tax:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Discounts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Deposits:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recurring sources:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Branding:** resource/table/form/action or page behavior for this module's authorized workflow.
- **PDFs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Delivery:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Immutability:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-sales-invoicing-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `draft-approved-final-invoices`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `line-items`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tax`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `discounts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `deposits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recurring-sources`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `branding`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `pdfs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `delivery`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `immutability`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-sales-invoicing` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-sales-invoicing-filament`](https://github.com/liberusoftware/module-accounting-sales-invoicing-filament) (`liberusoftware/accounting-sales-invoicing-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/sales-invoicing.md) · [API plan](../api/sales-invoicing.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Draft/approved/final invoices** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `draft/approved/final invoices`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Line items** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `line items`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tax** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tax`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Discounts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `discounts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Deposits** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `deposits`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recurring sources** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recurring sources`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Branding** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `branding`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **PDFs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `pdfs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Delivery** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `delivery`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Immutability** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `immutability`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [SalesInvoiceResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-filament/src/Resources/SalesInvoiceResource.php) · [ListSalesInvoices.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-filament/src/Resources/SalesInvoiceResource/Pages/ListSalesInvoices.php) · [SalesInvoicingFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-filament/src/SalesInvoicingFilamentPlugin.php) · [SalesInvoicingFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-filament/src/SalesInvoicingFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
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

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SalesInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Models/SalesInvoice.php) | `invoice_number`, `party_id`, `invoice_date`, `due_on`, `status`, `subtotal`, `discount_total`, `tax_total`, `total`, `currency`, `notes`, `branding`, `recurring_source`, `delivery_status`, `delivered_at`, `metadata` |
| [SalesInvoiceDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Models/SalesInvoiceDeposit.php) | `invoice_id`, `amount`, `currency`, `reference`, `received_by` |
| [SalesInvoiceLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Models/SalesInvoiceLine.php) | `invoice_id`, `description`, `quantity`, `unit_price`, `discount_rate`, `tax_rate`, `net_amount`, `tax_amount`, `metadata` |
<!-- layer-implementation-plan:end -->
