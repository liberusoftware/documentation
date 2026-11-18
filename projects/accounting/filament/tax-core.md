# Accounting: Tax Core Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#tax-core). Observed identity: [`liberusoftware/module-accounting-tax-core-filament`](../../../modules/source/liberusoftware--module-accounting-tax-core-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-tax-core-filament`  
**Matching domain module:** `accounting-tax-core`  
**Application:** Accounting  
**Source feature:** [Tax Core](../features/tax-core.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-tax-core` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Tax types/codes/rates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Inclusive/exclusive treatment:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Jurisdictions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Effective dates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Exemptions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rounding:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Evidence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Control accounts:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-tax-core-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `tax-types-codes-rates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `inclusive-exclusive-treatment`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `jurisdictions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `effective-dates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `exemptions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rounding`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `evidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `control-accounts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-tax-core` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-tax-core-filament`](https://github.com/liberusoftware/module-accounting-tax-core-filament) (`liberusoftware/accounting-tax-core-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/tax-core.md) · [API plan](../api/tax-core.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Tax types/codes/rates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tax types/codes/rates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Inclusive/exclusive treatment** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `inclusive/exclusive treatment`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Jurisdictions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `jurisdictions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Effective dates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `effective dates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Exemptions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exemptions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rounding** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rounding`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Evidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `evidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Control accounts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `control accounts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [TaxRuleResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core-filament/src/Resources/TaxRuleResource.php) · [ListTaxRules.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core-filament/src/Resources/TaxRuleResource/Pages/ListTaxRules.php) · [TaxCoreFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core-filament/src/TaxCoreFilamentPlugin.php) · [TaxCoreFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core-filament/src/TaxCoreFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ActiveTaxRuleQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Queries/ActiveTaxRuleQuery.php) | `public function handle(string $code, ?string $jurisdiction = null, ?string $on = null): ?TaxRule` |
| [TaxRuleQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Queries/TaxRuleQuery.php) | `public function paginate(?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/ActivateTaxRule.php) | `public function handle(TaxRule $rule): TaxRule` |
| [ArchiveTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/ArchiveTaxRule.php) | `public function handle(TaxRule $rule): TaxRule` |
| [CalculateTax.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/CalculateTax.php) | `public function handle(TaxRule $rule, float $amount): array` |
| [CaptureTaxEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/CaptureTaxEvidence.php) | `public function handle(TaxRule $rule, string $sourceType, string $sourceId, array $snapshot, ?int $actorId = null): TaxEvidence` |
| [CreateTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/CreateTaxRule.php) | `public function handle(array $attributes): TaxRule` |
| [UpdateTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/UpdateTaxRule.php) | `public function handle(TaxRule $rule, array $attributes): TaxRule` |
| [TaxCorePolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core-api/src/Policies/TaxCorePolicy.php) | `public function viewAny($user): bool`<br>`public function view($user, TaxRule $rule): bool`<br>`public function create($user): bool`<br>`public function update($user, TaxRule $rule): bool`<br>`public function delete($user, TaxRule $rule): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TaxEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Models/TaxEvidence.php) | `tax_rule_id`, `source_type`, `source_id`, `snapshot_hash`, `snapshot`, `captured_by`, `metadata` |
| [TaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Models/TaxRule.php) | `code`, `name`, `tax_type`, `jurisdiction_code`, `rate`, `treatment`, `effective_from`, `effective_until`, `status`, `exemption_code`, `control_account_code`, `rounding_method`, `rounding_scale`, `metadata` |
<!-- layer-implementation-plan:end -->
