# Accounting: Accounting Withholding Tax Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-withholding-tax). Observed identity: [`liberusoftware/module-accounting-withholding-tax-filament`](../../../modules/source/liberusoftware--module-accounting-withholding-tax-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-withholding-tax-filament`  
**Matching domain module:** `accounting-withholding-tax`  
**Application:** Accounting  
**Source feature:** [Accounting Withholding Tax](../features/accounting-withholding-tax.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-withholding-tax` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Certificates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Supplier/customer deductions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Liabilities:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Remittance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Statements:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Regional filing adapters:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-withholding-tax-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `certificates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `supplier-customer-deductions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `liabilities`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `remittance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `statements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `regional-filing-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-withholding-tax` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-withholding-tax-filament`](https://github.com/liberusoftware/module-accounting-withholding-tax-filament) (`liberusoftware/accounting-withholding-tax-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-withholding-tax.md) · [API plan](../api/accounting-withholding-tax.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Certificates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `certificates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Supplier/customer deductions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `supplier/customer deductions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Liabilities** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `liabilities`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Remittance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `remittance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Statements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `statements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Regional filing adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `regional filing adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListWithholdingTaxRules.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax-filament/src/Resources/Pages/ListWithholdingTaxRules.php) · [WithholdingTaxRuleResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax-filament/src/Resources/WithholdingTaxRuleResource.php) · [WithholdingTaxFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax-filament/src/WithholdingTaxFilamentPlugin.php) · [WithholdingTaxFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax-filament/src/WithholdingTaxFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CalculateWithholdingTax.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Actions/CalculateWithholdingTax.php) | `public function handle(WithholdingTaxRule $rule, array $attributes): WithholdingTaxDeduction` |
| [CreateWithholdingTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Actions/CreateWithholdingTaxRule.php) | `public function handle(array $attributes): WithholdingTaxRule` |
| [RemitWithholdingTax.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Actions/RemitWithholdingTax.php) | `public function handle(WithholdingTaxLiability $liability, array $attributes): WithholdingTaxRemittance` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WithholdingTaxCertificate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxCertificate.php) | `team_id`, `rule_id`, `party_type`, `party_id`, `certificate_ref`, `valid_from`, `valid_until`, `status`, `metadata` |
| [WithholdingTaxDeduction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxDeduction.php) | `team_id`, `rule_id`, `party_type`, `party_id`, `source_ref`, `currency`, `gross_amount`, `withheld_amount`, `status`, `metadata` |
| [WithholdingTaxFilingAdapter.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxFilingAdapter.php) | `team_id`, `jurisdiction`, `provider`, `status`, `configuration` |
| [WithholdingTaxLiability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxLiability.php) | `team_id`, `deduction_id`, `amount`, `due_on`, `status`, `metadata` |
| [WithholdingTaxRemittance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxRemittance.php) | `team_id`, `liability_id`, `amount`, `remitted_on`, `reference`, `status`, `metadata` |
| [WithholdingTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxRule.php) | `team_id`, `code`, `name`, `jurisdiction`, `rate`, `threshold`, `effective_from`, `effective_until`, `status`, `metadata` |
| [WithholdingTaxStatement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxStatement.php) | `team_id`, `jurisdiction`, `period_start`, `period_end`, `total_amount`, `status`, `payload` |
<!-- layer-implementation-plan:end -->
