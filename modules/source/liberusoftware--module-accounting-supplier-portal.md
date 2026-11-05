# liberusoftware/module-accounting-supplier-portal: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Accounting supplier portal domain module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-supplier-portal](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-accounting-erp-laravel-filament, `accounting-supplier-portal`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-supplier-portal` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-supplier-portal` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\SupplierPortal\\SupplierPortalServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\SupplierPortal\\SupplierPortalServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/module.json).

**Declared capabilities:** accounting.supplier-portal

**Declared features:** Profile/bank-change requests, Purchase orders, Invoices, Statements, Disputes, Payment status, Secure documents

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\SupplierPortal\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AttachPortalDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Actions/AttachPortalDocument.php) | `public function handle(PortalResource $resource, array $attributes): PortalDocument` |
| [src/Actions/CreatePortalResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Actions/CreatePortalResource.php) | `public function handle(array $attributes): PortalResource` |
| [src/Actions/TransitionPortalResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Actions/TransitionPortalResource.php) | `public function handle(PortalResource $resource, PortalStatus\|string $status, ?string $reason = null): PortalResource` |
| [src/Queries/PortalResourceQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Queries/PortalResourceQuery.php) | `public function paginate(?string $supplierId = null, ?string $type = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

Other non-legacy PHP sources: [src/Enums/PortalResourceType.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Enums/PortalResourceType.php) · [src/Enums/PortalStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Enums/PortalStatus.php) · [src/Events/PortalDocumentAttached.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Events/PortalDocumentAttached.php) · [src/Events/PortalResourceCreated.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Events/PortalResourceCreated.php) · [src/Events/PortalResourceStatusChanged.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Events/PortalResourceStatusChanged.php) · [src/Exceptions/InvalidPortalResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Exceptions/InvalidPortalResource.php) · [src/Models/PortalDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Models/PortalDocument.php) · [src/Models/PortalResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Models/PortalResource.php) · [src/SupplierPortalServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/SupplierPortalServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_130000_create_accounting_supplier_portal_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/database/migrations/2026_08_25_130000_create_accounting_supplier_portal_tables.php)

[src/Enums/PortalResourceType.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Enums/PortalResourceType.php): `ProfileChange = 'profile_change'`, `PurchaseOrder = 'purchase_order'`, `Invoice = 'invoice'`, `Statement = 'statement'`, `Dispute = 'dispute'`, `PaymentStatus = 'payment_status'`, `Document = 'document'`.

[src/Enums/PortalStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Enums/PortalStatus.php): `Draft = 'draft'`, `Submitted = 'submitted'`, `UnderReview = 'under_review'`, `Approved = 'approved'`, `Rejected = 'rejected'`, `Paid = 'paid'`, `Disputed = 'disputed'`, `Archived = 'archived'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
