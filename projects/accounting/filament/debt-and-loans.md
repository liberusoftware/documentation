# Accounting: Debt and Loans Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#debt-and-loans). Observed identity: [`liberusoftware/module-accounting-debt-and-loans-filament`](../../../modules/source/liberusoftware--module-accounting-debt-and-loans-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-debt-and-loans-filament`  
**Matching domain module:** `accounting-debt-and-loans`  
**Application:** Accounting  
**Source feature:** [Debt and Loans](../features/debt-and-loans.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-debt-and-loans` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Facilities:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Drawdowns:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Repayments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Interest/fees:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Schedules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Covenants:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Current/non-current split:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-debt-and-loans-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `facilities`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `drawdowns`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `repayments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `interest-fees`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `schedules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `covenants`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `current-non-current-split`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-debt-and-loans` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-debt-and-loans-filament`](https://github.com/liberusoftware/module-accounting-debt-and-loans-filament) (`liberusoftware/accounting-debt-and-loans-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/debt-and-loans.md) · [API plan](../api/debt-and-loans.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Facilities** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `facilities`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Drawdowns** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `drawdowns`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Repayments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `repayments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Interest/fees** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `interest/fees`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Schedules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `schedules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Covenants** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `covenants`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Current/non-current split** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `current/non-current split`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [DebtAndLoansFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans-filament/src/DebtAndLoansFilamentPlugin.php) · [DebtAndLoansFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans-filament/src/DebtAndLoansFilamentServiceProvider.php) · [DebtFacilityResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans-filament/src/Resources/DebtFacilityResource.php) · [ListDebtFacilities.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans-filament/src/Resources/DebtFacilityResource/Pages/ListDebtFacilities.php).

| Observed core query | Public method signatures |
| --- | --- |
| [DebtQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Queries/DebtQuery.php) | `public function facilities(int $teamId): Collection`<br>`public function position(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDebtFacility.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Actions/CreateDebtFacility.php) | `public function handle(array $attributes): DebtFacility` |
| [ReconcileDebtMovement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Actions/ReconcileDebtMovement.php) | `public function handle(DebtMovement $movement, string $journalReference): DebtMovement` |
| [RecordDebtMovement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Actions/RecordDebtMovement.php) | `public function handle(DebtFacility $facility, string\|DebtMovementKind $kind, array $attributes): DebtMovement` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DebtCovenant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Models/DebtCovenant.php) | `facility_id`, `team_id`, `covenant_ref`, `metric`, `threshold`, `operator`, `last_value`, `status`, `metadata` |
| [DebtFacility.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Models/DebtFacility.php) | `team_id`, `facility_ref`, `lender_ref`, `currency`, `limit_amount`, `drawn_amount`, `interest_rate`, `start_date`, `maturity_date`, `status`, `metadata` |
| [DebtMovement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Models/DebtMovement.php) | `facility_id`, `team_id`, `kind`, `principal_amount`, `interest_amount`, `fee_amount`, `movement_date`, `due_date`, `status`, `journal_ref`, `metadata` |
<!-- layer-implementation-plan:end -->
