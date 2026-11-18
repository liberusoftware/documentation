# Accounting: Accounting Bank Accounts Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-bank-accounts). Observed identity: [`liberusoftware/module-accounting-bank-accounts-filament`](../../../modules/source/liberusoftware--module-accounting-bank-accounts-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-bank-accounts-filament`  
**Matching domain module:** `accounting-bank-accounts`  
**Application:** Accounting  
**Source feature:** [Accounting Bank Accounts](../features/accounting-bank-accounts.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-bank-accounts` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Bank/current/savings/credit/loan/cash accounts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Ownership:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Currency:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Opening data:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Feeds:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Lifecycle:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Restricted details:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-bank-accounts-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `bank-current-savings-credit-loan-cash-accounts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ownership`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `currency`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `opening-data`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `feeds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `lifecycle`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `restricted-details`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-bank-accounts` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-bank-accounts-filament`](https://github.com/liberusoftware/module-accounting-bank-accounts-filament) (`liberusoftware/accounting-bank-accounts-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-bank-accounts.md) · [API plan](../api/accounting-bank-accounts.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Bank/current/savings/credit/loan/cash accounts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bank/current/savings/credit/loan/cash accounts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Ownership** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ownership`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Currency** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `currency`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Opening data** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `opening data`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Feeds** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `feeds`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Lifecycle** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lifecycle`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Restricted details** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `restricted details`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [BankAccountsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts-filament/src/BankAccountsFilamentPlugin.php) · [BankAccountsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts-filament/src/BankAccountsFilamentServiceProvider.php) · [BankAccountResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts-filament/src/Resources/BankAccountResource.php) · [CreateBankAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts-filament/src/Resources/BankAccountResource/Pages/CreateBankAccount.php) · [ListBankAccounts.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts-filament/src/Resources/BankAccountResource/Pages/ListBankAccounts.php).

| Observed core query | Public method signatures |
| --- | --- |
| [BankAccountBalanceQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts/src/Queries/BankAccountBalanceQuery.php) | `public function handle(?int $legalEntityId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateBankAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts/src/Actions/CreateBankAccount.php) | `public function handle(array $attributes): BankAccount` |
| [SetBankAccountStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts/src/Actions/SetBankAccountStatus.php) | `public function handle(BankAccount $account, BankAccountStatus $status): BankAccount` |
| [UpdateBankAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts/src/Actions/UpdateBankAccount.php) | `public function handle(BankAccount $account, array $attributes): BankAccount` |
| [BankAccountsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts-api/src/Policies/BankAccountsPolicy.php) | `public function viewAny(?object $user = null): bool`<br>`public function view(?object $user, object $account): bool`<br>`public function create(?object $user = null): bool`<br>`public function update(?object $user, object $account): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BankAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts/src/Models/BankAccount.php) | `legal_entity_id`, `owner_type`, `owner_id`, `name`, `institution_name`, `account_type`, `currency`, `opening_balance`, `opening_date`, `current_balance`, `account_number`, `routing_number`, `feed_reference`, `status`, `closed_at`, `metadata` |
<!-- layer-implementation-plan:end -->
