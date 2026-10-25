# liberusoftware/module-billing-invoicing: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral invoicing schedules, lines, tax, credits, adjustments, PDFs, delivery, and finalization.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [module-billing-invoicing](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: billing-laravel, `module-billing-invoicing`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-billing-invoicing` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-billing-invoicing` |
| Module version field | `0.1.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Billing\\Invoicing\\InvoicingServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/composer.json) · [module.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/module.json).

**Declared capabilities:** billing.invoicing

**Declared features:** Schedules, Line generation, Tax, Credits, Adjustments, PDFs, Delivery, Finalization

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `barryvdh/laravel-dompdf` | `^3.1` |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Billing\\Invoicing\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AddInvoiceLine.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/AddInvoiceLine.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, string $description, int $quantity, int $unitAmountMinor, float $taxRate = 0): InvoiceLine` |
| [src/Actions/ApplyInvoiceAdjustment.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/ApplyInvoiceAdjustment.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, int $amountMinor, string $reason, string $type = 'adjustment'): Invoice` |
| [src/Actions/ApplyInvoiceLateFee.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/ApplyInvoiceLateFee.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, int $amountMinor, ?CarbonInterface $at = null): Invoice` |
| [src/Actions/CreateInvoice.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/CreateInvoice.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): Invoice` |
| [src/Actions/CreateInvoiceSchedule.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/CreateInvoiceSchedule.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): InvoiceSchedule` |
| [src/Actions/CreateInvoiceSupport.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/CreateInvoiceSupport.php) | `public function execute(int $teamId, array $attributes): InvoiceSupport` |
| [src/Actions/CreatePaymentPlan.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/CreatePaymentPlan.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, int $totalInstallments, string $frequency = 'monthly', ?CarbonInterface $startAt = null): PaymentPlan` |
| [src/Actions/DeliverInvoice.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/DeliverInvoice.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, string $destination, ?int $documentId = null): InvoiceSupport` |
| [src/Actions/FinalizeInvoice.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/FinalizeInvoice.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice): Invoice` |
| [src/Actions/GenerateInvoiceDocument.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/GenerateInvoiceDocument.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, string $format = 'pdf'): InvoiceSupport` |
| [src/Actions/RunInvoiceSchedule.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/RunInvoiceSchedule.php) | `public function __construct( private DatabaseManager $database, private CreateInvoice $createInvoice, private AddInvoiceLine $addInvoiceLine, private FinalizeInvoice $finalizeInvoice, )`<br>`public function execute(InvoiceSchedule $schedule, ?CarbonInterface $at = null): Invoice` |
| [src/Actions/RunPaymentPlan.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/RunPaymentPlan.php) | `public function __construct( private DatabaseManager $database, private CreateInvoice $createInvoice, private AddInvoiceLine $addInvoiceLine, private FinalizeInvoice $finalizeInvoice, )`<br>`public function execute(PaymentPlan $paymentPlan, ?CarbonInterface $at = null): Invoice` |
| [src/Policies/InvoicePolicy.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Policies/InvoicePolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, Invoice $invoice): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, Invoice $invoice): bool` |
| [src/Policies/InvoiceSchedulePolicy.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Policies/InvoiceSchedulePolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function view(?object $user, InvoiceSchedule $schedule): bool`<br>`public function update(?object $user, InvoiceSchedule $schedule): bool` |
| [src/Policies/InvoiceSupportPolicy.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Policies/InvoiceSupportPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function view(?object $user, object $record): bool` |
| [src/Queries/ListInvoices.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Queries/ListInvoices.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [src/Support/CustomerReference.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Support/CustomerReference.php) | `public static function assertBelongsToTeam(DatabaseManager $database, mixed $customerId, mixed $teamId): ?int` |

Other non-legacy PHP sources: [src/Enums/InvoiceStatus.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Enums/InvoiceStatus.php) · [src/Events/InvoiceAdjusted.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Events/InvoiceAdjusted.php) · [src/Events/InvoiceCreated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Events/InvoiceCreated.php) · [src/Events/InvoiceDelivered.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Events/InvoiceDelivered.php) · [src/Events/InvoiceDocumentGenerated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Events/InvoiceDocumentGenerated.php) · [src/Events/InvoiceFinalized.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Events/InvoiceFinalized.php) · [src/Events/InvoiceLateFeeApplied.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Events/InvoiceLateFeeApplied.php) · [src/Events/InvoiceLineAdded.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Events/InvoiceLineAdded.php) · [src/Events/InvoiceScheduleCreated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Events/InvoiceScheduleCreated.php) · [src/Events/InvoiceScheduleRun.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Events/InvoiceScheduleRun.php) · [src/Events/InvoiceSupportCreated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Events/InvoiceSupportCreated.php) · [src/Events/PaymentPlanCreated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Events/PaymentPlanCreated.php) · [src/Events/PaymentPlanInstallmentGenerated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Events/PaymentPlanInstallmentGenerated.php) · [src/InvoicingServiceProvider.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/InvoicingServiceProvider.php) · [src/Models/Invoice.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/Invoice.php) · [src/Models/InvoiceLine.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/InvoiceLine.php) · [src/Models/InvoiceSchedule.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/InvoiceSchedule.php) · [src/Models/InvoiceSupport.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/InvoiceSupport.php) · [src/Models/PaymentPlan.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/PaymentPlan.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_050000_create_billing_invoicing_tables.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/database/migrations/2026_08_24_050000_create_billing_invoicing_tables.php)
- [database/migrations/2026_08_24_200000_create_billing_invoice_support_table.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/database/migrations/2026_08_24_200000_create_billing_invoice_support_table.php)
- [database/migrations/2026_08_29_010000_create_billing_payment_plans_table.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/database/migrations/2026_08_29_010000_create_billing_payment_plans_table.php)

[src/Enums/InvoiceStatus.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Enums/InvoiceStatus.php): `Draft = 'draft'`, `Finalized = 'finalized'`, `PartiallyPaid = 'partially_paid'`, `Paid = 'paid'`, `Void = 'void'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
