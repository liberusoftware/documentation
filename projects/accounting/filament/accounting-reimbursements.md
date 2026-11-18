# Accounting: Accounting Reimbursements Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-reimbursements). Observed identity: [`liberusoftware/module-accounting-reimbursements-filament`](../../../modules/source/liberusoftware--module-accounting-reimbursements-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-reimbursements-filament`  
**Matching domain module:** `accounting-reimbursements`  
**Application:** Accounting  
**Source feature:** [Accounting Reimbursements](../features/accounting-reimbursements.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-reimbursements` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Approved expense/mileage liabilities:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payment batches:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bank export/provider status:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Remittance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Failure:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-reimbursements-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `approved-expense-mileage-liabilities`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payment-batches`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bank-export-provider-status`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `remittance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `failure`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-reimbursements` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-reimbursements-filament`](https://github.com/liberusoftware/module-accounting-reimbursements-filament) (`liberusoftware/accounting-reimbursements-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-reimbursements.md) · [API plan](../api/accounting-reimbursements.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Approved expense/mileage liabilities** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approved expense/mileage liabilities`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Payment batches** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payment batches`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bank export/provider status** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bank export/provider status`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Remittance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `remittance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Failure** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `failure`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ReimbursementsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements-filament/src/ReimbursementsFilamentPlugin.php) · [ReimbursementsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements-filament/src/ReimbursementsFilamentServiceProvider.php) · [ListReimbursementLiabilities.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements-filament/src/Resources/Pages/ListReimbursementLiabilities.php) · [ReimbursementLiabilityResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements-filament/src/Resources/ReimbursementLiabilityResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePaymentBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Actions/CreatePaymentBatch.php) | `public function handle(array $liabilityIds, ?int $teamId = null): ReimbursementBatch` |
| [CreateReimbursementLiability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Actions/CreateReimbursementLiability.php) | `public function handle(array $attributes): ReimbursementLiability` |
| [ReconcilePaymentBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Actions/ReconcilePaymentBatch.php) | `public function handle(ReimbursementBatch $batch, float $settledAmount, ?string $externalRef = null): ReimbursementReconciliation` |
| [UpdatePaymentProviderStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Actions/UpdatePaymentProviderStatus.php) | `public function handle(ReimbursementBatch $batch, array $attributes): ReimbursementBatch` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReimbursementBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Models/ReimbursementBatch.php) | `team_id`, `currency`, `total_amount`, `status`, `provider`, `provider_ref`, `exported_at`, `submitted_at`, `paid_at`, `failure_message`, `metadata` |
| [ReimbursementLiability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Models/ReimbursementLiability.php) | `team_id`, `payee_ref`, `source_type`, `source_id`, `kind`, `currency`, `amount`, `approved_at`, `status`, `batch_id`, `metadata` |
| [ReimbursementReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Models/ReimbursementReconciliation.php) | `batch_id`, `expected_amount`, `settled_amount`, `variance`, `status`, `external_ref`, `notes`, `metadata` |
| [ReimbursementRemittance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Models/ReimbursementRemittance.php) | `batch_id`, `payee_ref`, `amount`, `currency`, `status`, `document_ref`, `sent_at`, `metadata` |
<!-- layer-implementation-plan:end -->
