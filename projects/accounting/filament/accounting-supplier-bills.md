# Accounting: Accounting Supplier Bills Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-supplier-bills). Observed identity: [`liberusoftware/module-accounting-supplier-bills-filament`](../../../modules/source/liberusoftware--module-accounting-supplier-bills-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-supplier-bills-filament`  
**Matching domain module:** `accounting-supplier-bills`  
**Application:** Accounting  
**Source feature:** [Accounting Supplier Bills](../features/accounting-supplier-bills.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-supplier-bills` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Draft/approved/posted bills:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Capture sources:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Line coding:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tax:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Due dates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Duplicate detection:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Matching:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Credits:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Documents:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-supplier-bills-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `draft-approved-posted-bills`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `capture-sources`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `line-coding`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tax`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `due-dates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `duplicate-detection`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `matching`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `credits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `documents`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-supplier-bills` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-supplier-bills-filament`](https://github.com/liberusoftware/module-accounting-supplier-bills-filament) (`liberusoftware/accounting-supplier-bills-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-supplier-bills.md) · [API plan](../api/accounting-supplier-bills.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Draft/approved/posted bills** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `draft/approved/posted bills`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Capture sources** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `capture sources`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Line coding** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `line coding`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tax** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tax`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Due dates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `due dates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Duplicate detection** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `duplicate detection`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Matching** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `matching`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Credits** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `credits`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Documents** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `documents`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CreateSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills-filament/src/Resources/Pages/CreateSupplierBill.php) · [EditSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills-filament/src/Resources/Pages/EditSupplierBill.php) · [ListSupplierBills.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills-filament/src/Resources/Pages/ListSupplierBills.php) · [SupplierBillResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills-filament/src/Resources/SupplierBillResource.php) · [SupplierBillsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills-filament/src/SupplierBillsFilamentPlugin.php) · [SupplierBillsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills-filament/src/SupplierBillsFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [DuplicateSupplierBillQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Queries/DuplicateSupplierBillQuery.php) | `public function handle(int $partyId, string $billNumber, ?int $exceptId = null): Collection` |
| [SupplierBillAgingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Queries/SupplierBillAgingQuery.php) | `public function handle(?int $partyId = null, ?\DateTimeInterface $asOf = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddSupplierBillCredit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/AddSupplierBillCredit.php) | `public function handle(SupplierBill $bill, array $attributes): SupplierBill` |
| [ApproveSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/ApproveSupplierBill.php) | `public function handle(SupplierBill $bill, ?int $actorId = null): SupplierBill` |
| [AttachSupplierBillDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/AttachSupplierBillDocument.php) | `public function handle(SupplierBill $bill, array $attributes): SupplierBillDocument` |
| [CreateSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/CreateSupplierBill.php) | `public function handle(array $attributes, array $lines): SupplierBill` |
| [MatchSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/MatchSupplierBill.php) | `public function handle(SupplierBill $bill, array $attributes): SupplierBill` |
| [PostSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/PostSupplierBill.php) | `public function __construct(private readonly CreateOpenItem $createOpenItem)`<br>`public function handle(SupplierBill $bill): SupplierBill` |
| [RejectSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/RejectSupplierBill.php) | `public function handle(SupplierBill $bill, string $reason): SupplierBill` |
| [UpdateSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/UpdateSupplierBill.php) | `public function handle(SupplierBill $bill, array $attributes, array $lines): SupplierBill` |
| [VoidSupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Actions/VoidSupplierBill.php) | `public function handle(SupplierBill $bill, string $reason): SupplierBill` |
| [SupplierBillsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills-api/src/Policies/SupplierBillsPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, object $bill): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, object $bill): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SupplierBill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Models/SupplierBill.php) | `party_id`, `bill_number`, `bill_date`, `due_on`, `status`, `payment_status`, `subtotal`, `tax_total`, `total`, `amount_paid`, `currency`, `capture_source`, `purchase_order_reference`, `reference_number`, `notes`, `approval_status`, `approved_by`, `approved_at`, `rejection_reason`, `recurring`, `recurrence_frequency`, `recurrence_start`, `recurrence_end`, `last_generated`, `external_ids`, `metadata` |
| [SupplierBillCredit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Models/SupplierBillCredit.php) | `bill_id`, `amount`, `currency`, `reason`, `reference`, `metadata` |
| [SupplierBillDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Models/SupplierBillDocument.php) | `bill_id`, `path`, `original_name`, `mime_type`, `sha256`, `metadata` |
| [SupplierBillLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Models/SupplierBillLine.php) | `bill_id`, `account_code`, `description`, `quantity`, `unit_price`, `discount_rate`, `tax_rate`, `net_amount`, `tax_amount`, `metadata` |
| [SupplierBillMatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills/src/Models/SupplierBillMatch.php) | `bill_id`, `match_type`, `matched_type`, `matched_id`, `quantity`, `amount`, `status`, `metadata` |
| [Supplier.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-bills-api/src/Models/Supplier.php) | `payment_term_id`, `supplier_first_name`, `supplier_last_name`, `supplier_email`, `supplier_address`, `supplier_phone_number`, `supplier_limit_credit`, `supplier_tin` |
<!-- layer-implementation-plan:end -->
