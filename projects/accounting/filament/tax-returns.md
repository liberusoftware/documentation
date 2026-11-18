# Accounting: Tax Returns Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#tax-returns). Observed identity: [`liberusoftware/module-accounting-tax-returns-filament`](../../../modules/source/liberusoftware--module-accounting-tax-returns-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-tax-returns-filament`  
**Matching domain module:** `accounting-tax-returns`  
**Application:** Accounting  
**Source feature:** [Tax Returns](../features/tax-returns.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-tax-returns` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Return preparation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Source reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Diagnostics:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Review:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approval:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Submission adapter:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Receipt/status:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payment:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Amendments:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-tax-returns-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `return-preparation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `source-reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `diagnostics`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `review`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approval`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `submission-adapter`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `receipt-status`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payment`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `amendments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-tax-returns` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-tax-returns-filament`](https://github.com/liberusoftware/module-accounting-tax-returns-filament) (`liberusoftware/accounting-tax-returns-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/tax-returns.md) · [API plan](../api/tax-returns.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Return preparation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `return preparation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Source reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `source reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Diagnostics** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `diagnostics`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Review** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `review`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approval** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approval`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Submission adapter** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `submission adapter`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Receipt/status** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `receipt/status`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Payment** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payment`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Amendments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `amendments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListTaxReturns.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns-filament/src/Resources/Pages/ListTaxReturns.php) · [TaxReturnResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns-filament/src/Resources/TaxReturnResource.php) · [TaxReturnsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns-filament/src/TaxReturnsFilamentPlugin.php) · [TaxReturnsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns-filament/src/TaxReturnsFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AmendTaxReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns/src/Actions/AmendTaxReturn.php) | `public function handle(TaxReturn $taxReturn): TaxReturn` |
| [CreateTaxReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns/src/Actions/CreateTaxReturn.php) | `public function handle(array $attributes): TaxReturn` |
| [SubmitTaxReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns/src/Actions/SubmitTaxReturn.php) | `public function handle(TaxReturn $taxReturn, string $externalReference): TaxReturn` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TaxReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns/src/Models/TaxReturn.php) | `team_id`, `tax_type`, `jurisdiction`, `period_start`, `period_end`, `due_on`, `status`, `external_reference`, `submitted_at`, `metadata` |
| [TaxReturnLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns/src/Models/TaxReturnLine.php) | `team_id`, `tax_return_id`, `code`, `amount`, `currency`, `metadata` |
<!-- layer-implementation-plan:end -->
