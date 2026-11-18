# Accounting: Accounting Supplier Portal Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-supplier-portal). Observed identity: [`liberusoftware/module-accounting-supplier-portal-filament`](../../../modules/source/liberusoftware--module-accounting-supplier-portal-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-supplier-portal-filament`  
**Matching domain module:** `accounting-supplier-portal`  
**Application:** Accounting  
**Source feature:** [Accounting Supplier Portal](../features/accounting-supplier-portal.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-supplier-portal` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Profile/bank-change requests:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Purchase orders:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Invoices:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Statements:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Disputes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payment status:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Secure documents:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-supplier-portal-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `profile-bank-change-requests`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `purchase-orders`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `invoices`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `statements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `disputes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payment-status`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `secure-documents`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-supplier-portal` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-supplier-portal-filament`](https://github.com/liberusoftware/module-accounting-supplier-portal-filament) (`liberusoftware/accounting-supplier-portal-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-supplier-portal.md) · [API plan](../api/accounting-supplier-portal.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Profile/bank-change requests** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `profile/bank-change requests`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Purchase orders** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `purchase orders`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Invoices** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `invoices`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Statements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `statements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Disputes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `disputes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Payment status** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payment status`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Secure documents** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `secure documents`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PortalResourceResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal-filament/src/Resources/PortalResourceResource.php) · [ListPortalResources.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal-filament/src/Resources/PortalResourceResource/Pages/ListPortalResources.php) · [SupplierPortalFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal-filament/src/SupplierPortalFilamentPlugin.php) · [SupplierPortalFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal-filament/src/SupplierPortalFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [PortalResourceQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Queries/PortalResourceQuery.php) | `public function paginate(?string $supplierId = null, ?string $type = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AttachPortalDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Actions/AttachPortalDocument.php) | `public function handle(PortalResource $resource, array $attributes): PortalDocument` |
| [CreatePortalResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Actions/CreatePortalResource.php) | `public function handle(array $attributes): PortalResource` |
| [TransitionPortalResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Actions/TransitionPortalResource.php) | `public function handle(PortalResource $resource, PortalStatus\|string $status, ?string $reason = null): PortalResource` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PortalDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Models/PortalDocument.php) | `resource_id`, `path`, `original_name`, `mime_type`, `sha256`, `uploaded_by`, `metadata` |
| [PortalResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-supplier-portal/src/Models/PortalResource.php) | `supplier_id`, `type`, `reference`, `status`, `currency`, `amount`, `payload`, `submitted_at`, `approved_at`, `rejected_reason`, `metadata` |
<!-- layer-implementation-plan:end -->
