# Accounting: Accounting Account Reconciliations Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-account-reconciliations). Observed identity: [`liberusoftware/module-accounting-account-reconciliations-filament`](../../../modules/source/liberusoftware--module-accounting-account-reconciliations-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-account-reconciliations-filament`  
**Matching domain module:** `accounting-account-reconciliations`  
**Application:** Accounting  
**Source feature:** [Accounting Account Reconciliations](../features/accounting-account-reconciliations.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-account-reconciliations` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **GL account templates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Source balances:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Supporting items:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Preparer/reviewer:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Aging:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Certification:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Carry-forward:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-account-reconciliations-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `gl-account-templates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `source-balances`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `supporting-items`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `preparer-reviewer`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `aging`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `certification`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `carry-forward`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-account-reconciliations` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-account-reconciliations-filament`](https://github.com/liberusoftware/module-accounting-account-reconciliations-filament) (`liberusoftware/accounting-account-reconciliations-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-account-reconciliations.md) · [API plan](../api/accounting-account-reconciliations.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **GL account templates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `gl account templates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Source balances** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `source balances`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Supporting items** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `supporting items`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Preparer/reviewer** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `preparer/reviewer`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Aging** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `aging`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Certification** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `certification`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Carry-forward** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `carry-forward`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AccountReconciliationsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations-filament/src/AccountReconciliationsFilamentPlugin.php) · [AccountReconciliationsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations-filament/src/AccountReconciliationsFilamentServiceProvider.php) · [AccountReconciliationResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations-filament/src/Resources/AccountReconciliationResource.php) · [ListAccountReconciliations.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations-filament/src/Resources/AccountReconciliationResource/Pages/ListAccountReconciliations.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AccountReconciliationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Queries/AccountReconciliationQuery.php) | `public function paginate(?int $teamId, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CarryForwardAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/CarryForwardAccountReconciliation.php) | `public function handle(AccountReconciliation $reconciliation, array $carryForward): AccountReconciliation` |
| [CertifyAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/CertifyAccountReconciliation.php) | `public function handle(AccountReconciliation $reconciliation, array $certification): AccountReconciliation` |
| [CreateAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/CreateAccountReconciliation.php) | `public function handle(array $attributes): AccountReconciliation` |
| [PrepareAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/PrepareAccountReconciliation.php) | `public function handle(AccountReconciliation $reconciliation, array $preparer, array $sourceBalance, array $supportingItems = []): AccountReconciliation` |
| [ReviewAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/ReviewAccountReconciliation.php) | `public function handle(AccountReconciliation $reconciliation, array $reviewer): AccountReconciliation` |
| [AccountReconciliationsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations-api/src/Policies/AccountReconciliationsPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function create(?object $user): bool`<br>`public function update(?object $user, object $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Models/AccountReconciliation.php) | `team_id`, `book_id`, `account_id`, `period_start`, `period_end`, `status`, `template`, `source_balance`, `supporting_items`, `preparer`, `reviewer`, `aging`, `certification`, `carry_forward` |
| [Account.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations-api/src/Models/Account.php) | `account_number`, `account_name`, `account_type`, `normal_balance`, `balance`, `opening_balance`, `description`, `currency_id`, `parent_id`, `industry_type`, `is_active`, `allow_manual_entry`, `user_id`, `team_id`, `qbo_id`, `qbo_sync_token`, `xero_id`, `sage_id` |
<!-- layer-implementation-plan:end -->
