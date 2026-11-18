# Accounting: Accounting Contractor Compliance Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-contractor-compliance). Observed identity: [`liberusoftware/module-accounting-contractor-compliance-filament`](../../../modules/source/liberusoftware--module-accounting-contractor-compliance-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-contractor-compliance-filament`  
**Matching domain module:** `accounting-contractor-compliance`  
**Application:** Accounting  
**Source feature:** [Accounting Contractor Compliance](../features/accounting-contractor-compliance.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-contractor-compliance` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Contractor records:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Status/evidence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Withholding schemes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **CIS/1099-style classifications:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Deductions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Statements:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Regional exports:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-contractor-compliance-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `contractor-records`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `status-evidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `withholding-schemes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cis-1099-style-classifications`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `deductions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `statements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `regional-exports`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-contractor-compliance` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-contractor-compliance-filament`](https://github.com/liberusoftware/module-accounting-contractor-compliance-filament) (`liberusoftware/accounting-contractor-compliance-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-contractor-compliance.md) · [API plan](../api/accounting-contractor-compliance.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Contractor records** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `contractor records`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Status/evidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `status/evidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Withholding schemes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `withholding schemes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **CIS/1099-style classifications** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cis/1099-style classifications`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Deductions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `deductions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Statements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `statements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Regional exports** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `regional exports`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ContractorComplianceFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance-filament/src/ContractorComplianceFilamentPlugin.php) · [ContractorComplianceFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance-filament/src/ContractorComplianceFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ContractorQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Queries/ContractorQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ExportContractorCompliance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Actions/ExportContractorCompliance.php) | `public function handle(Contractor $contractor, string $region): Contractor` |
| [IssueContractorStatement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Actions/IssueContractorStatement.php) | `public function handle(Contractor $contractor, array $statement): Contractor` |
| [RecordContractorEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Actions/RecordContractorEvidence.php) | `public function handle(Contractor $contractor, array $evidence): Contractor` |
| [RegisterContractor.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Actions/RegisterContractor.php) | `public function handle(array $attributes): Contractor` |
| [UpdateContractorCompliance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Actions/UpdateContractorCompliance.php) | `public function handle(Contractor $contractor, array $attributes): Contractor` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Contractor.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Models/Contractor.php) | `team_id`, `contractor_ref`, `legal_name`, `classification`, `status`, `withholding_scheme`, `deductions`, `evidence`, `statement`, `regional_export` |
<!-- layer-implementation-plan:end -->
