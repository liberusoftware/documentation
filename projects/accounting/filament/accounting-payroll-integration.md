# Accounting: Accounting Payroll Integration Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-payroll-integration). Observed identity: [`liberusoftware/module-accounting-payroll-integration-filament`](../../../modules/source/liberusoftware--module-accounting-payroll-integration-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-payroll-integration-filament`  
**Matching domain module:** `accounting-payroll-integration`  
**Application:** Accounting  
**Source feature:** [Accounting Payroll Integration](../features/accounting-payroll-integration.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-payroll-integration` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Provider/period/run identity:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Employee/contractor references:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Import validation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dimensions/projects:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Provider adapters:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-payroll-integration-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `provider-period-run-identity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `employee-contractor-references`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `import-validation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dimensions-projects`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `provider-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-payroll-integration` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-payroll-integration-filament`](https://github.com/liberusoftware/module-accounting-payroll-integration-filament) (`liberusoftware/accounting-payroll-integration-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-payroll-integration.md) · [API plan](../api/accounting-payroll-integration.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Provider/period/run identity** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provider/period/run identity`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Employee/contractor references** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `employee/contractor references`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Import validation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `import validation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dimensions/projects** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dimensions/projects`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Provider adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provider adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PayrollIntegrationFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration-filament/src/PayrollIntegrationFilamentPlugin.php) · [PayrollIntegrationFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration-filament/src/PayrollIntegrationFilamentServiceProvider.php) · [PayrollImportResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration-filament/src/Resources/PayrollImportResource.php) · [ListPayrollImports.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration-filament/src/Resources/PayrollImportResource/Pages/ListPayrollImports.php).

| Observed core query | Public method signatures |
| --- | --- |
| [PayrollImportSummary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration/src/Queries/PayrollImportSummary.php) | `public function forTeam(?int $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ImportPayrollRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration/src/Actions/ImportPayrollRun.php) | `public function handle(array $attributes): PayrollImport` |
| [MarkPayrollImport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration/src/Actions/MarkPayrollImport.php) | `public function handle(PayrollImport $import, ImportStatus $status): PayrollImport` |
| [PayrollProviderAdapter.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration/src/Contracts/PayrollProviderAdapter.php) | `public function validateImport(array $payload): array`<br>`public function import(array $payload): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PayrollImport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration/src/Models/PayrollImport.php) | `team_id`, `provider`, `period_start`, `period_end`, `run_ref`, `currency`, `employee_refs`, `contractor_refs`, `dimensions`, `project_refs`, `payload_hash`, `validation_errors`, `adapter_ref`, `status`, `imported_at`, `reconciled_at`, `metadata` |
| [Payroll.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration-api/src/Models/Payroll.php) | `employee_id`, `base_salary`, `overtime_hours`, `overtime_rate`, `tax_deductions`, `other_deductions`, `net_salary`, `pay_period_start`, `pay_period_end`, `payment_date`, `payment_status` |
<!-- layer-implementation-plan:end -->
