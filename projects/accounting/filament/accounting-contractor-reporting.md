# Accounting: Accounting Contractor Reporting Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-contractor-reporting). Observed identity: [`liberusoftware/module-accounting-contractor-reporting-filament`](../../../modules/source/liberusoftware--module-accounting-contractor-reporting-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-contractor-reporting-filament`  
**Matching domain module:** `accounting-contractor-reporting`  
**Application:** Accounting  
**Source feature:** [Accounting Contractor Reporting](../features/accounting-contractor-reporting.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-contractor-reporting` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **1099-style thresholds:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Classifications:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payee validation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Forms:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Electronic filing adapters:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Corrections:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Evidence:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-contractor-reporting-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `1099-style-thresholds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `classifications`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payee-validation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `forms`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `electronic-filing-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `corrections`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `evidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-contractor-reporting` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-contractor-reporting-filament`](https://github.com/liberusoftware/module-accounting-contractor-reporting-filament) (`liberusoftware/accounting-contractor-reporting-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-contractor-reporting.md) · [API plan](../api/accounting-contractor-reporting.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **1099-style thresholds** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `1099-style thresholds`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Classifications** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `classifications`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Payee validation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payee validation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Forms** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `forms`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Electronic filing adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `electronic filing adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Corrections** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `corrections`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Evidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `evidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ContractorReportingFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-reporting-filament/src/ContractorReportingFilamentPlugin.php) · [ContractorReportingFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-reporting-filament/src/ContractorReportingFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ContractorReportQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-reporting/src/Queries/ContractorReportQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CorrectContractorReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-reporting/src/Actions/CorrectContractorReport.php) | `public function handle(ContractorReport $report, array $correction): ContractorReport` |
| [CreateContractorReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-reporting/src/Actions/CreateContractorReport.php) | `public function handle(array $attributes): ContractorReport` |
| [FileContractorReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-reporting/src/Actions/FileContractorReport.php) | `public function handle(ContractorReport $report, string $adapter): ContractorReport` |
| [ValidateContractorReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-reporting/src/Actions/ValidateContractorReport.php) | `public function handle(ContractorReport $report, array $validation): ContractorReport` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ContractorReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-reporting/src/Models/ContractorReport.php) | `team_id`, `payee_ref`, `tax_year`, `classification`, `threshold`, `reportable_amount`, `form_type`, `status`, `filing_adapter`, `payee_validation`, `correction`, `evidence` |
<!-- layer-implementation-plan:end -->
