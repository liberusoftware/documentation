# Accounting: Bank Reconciliation Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#bank-reconciliation). Observed identity: [`liberusoftware/module-accounting-bank-reconciliation-filament`](../../../modules/source/liberusoftware--module-accounting-bank-reconciliation-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-bank-reconciliation-filament`  
**Matching domain module:** `accounting-bank-reconciliation`  
**Application:** Accounting  
**Source feature:** [Bank Reconciliation](../features/bank-reconciliation.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-bank-reconciliation` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Suggested/exact matches:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Transfers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Grouped receipts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Fees/interest:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Adjustments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Statement balance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Exceptions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sign-off:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-bank-reconciliation-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `suggested-exact-matches`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `transfers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `grouped-receipts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `fees-interest`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `adjustments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `statement-balance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `exceptions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sign-off`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-bank-reconciliation` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-bank-reconciliation-filament`](https://github.com/liberusoftware/module-accounting-bank-reconciliation-filament) (`liberusoftware/accounting-bank-reconciliation-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/bank-reconciliation.md) · [API plan](../api/bank-reconciliation.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Suggested/exact matches** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `suggested/exact matches`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Transfers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `transfers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Grouped receipts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `grouped receipts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Fees/interest** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `fees/interest`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Adjustments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `adjustments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Statement balance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `statement balance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Exceptions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exceptions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sign-off** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sign-off`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [BankReconciliationFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation-filament/src/BankReconciliationFilamentPlugin.php) · [BankReconciliationFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation-filament/src/BankReconciliationFilamentServiceProvider.php) · [ReconciliationSessionResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation-filament/src/Resources/ReconciliationSessionResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ReconciliationSummaryQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Queries/ReconciliationSummaryQuery.php) | `public function handle(ReconciliationSession $session): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddReconciliationEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Actions/AddReconciliationEntry.php) | `public function handle(ReconciliationSession $session, array $attributes): ReconciliationEntry` |
| [ConfirmReconciliationEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Actions/ConfirmReconciliationEntry.php) | `public function handle(ReconciliationEntry $entry): ReconciliationEntry` |
| [CreateReconciliationSession.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Actions/CreateReconciliationSession.php) | `public function handle(array $attributes): ReconciliationSession` |
| [SignOffReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Actions/SignOffReconciliation.php) | `public function handle(ReconciliationSession $session): ReconciliationSession` |
| [BankReconciliationPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation-api/src/Policies/BankReconciliationPolicy.php) | `public function viewAny(?object $user = null): bool`<br>`public function view(?object $user, object $session): bool`<br>`public function create(?object $user = null): bool`<br>`public function update(?object $user, object $session): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReconciliationEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Models/ReconciliationEntry.php) | `team_id`, `session_id`, `source_type`, `source_id`, `kind`, `status`, `amount`, `currency`, `confidence`, `description`, `metadata`, `exception_reason`, `confirmed_at`, `confirmed_by` |
| [ReconciliationSession.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Models/ReconciliationSession.php) | `team_id`, `user_id`, `bank_account_id`, `period_start`, `period_end`, `opening_balance`, `statement_balance`, `status`, `signed_off_at`, `signed_off_by`, `metadata` |
<!-- layer-implementation-plan:end -->
