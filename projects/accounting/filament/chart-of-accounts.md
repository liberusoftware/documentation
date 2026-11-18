# Accounting: Chart of Accounts Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#chart-of-accounts). Observed identity: [`liberusoftware/module-accounting-chart-of-accounts-filament`](../../../modules/source/liberusoftware--module-accounting-chart-of-accounts-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-chart-of-accounts-filament`  
**Matching domain module:** `accounting-chart-of-accounts`  
**Application:** Accounting  
**Source feature:** [Chart of Accounts](../features/chart-of-accounts.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-chart-of-accounts` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Account types:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Codes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Hierarchies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Control accounts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Normal balances:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Templates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Restrictions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Localization:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Lifecycle:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-chart-of-accounts-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `account-types`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `codes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `hierarchies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `control-accounts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `normal-balances`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `templates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `restrictions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `localization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `lifecycle`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-chart-of-accounts` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-chart-of-accounts-filament`](https://github.com/liberusoftware/module-accounting-chart-of-accounts-filament) (`liberusoftware/accounting-chart-of-accounts-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/chart-of-accounts.md) · [API plan](../api/chart-of-accounts.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Account types** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `account types`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Codes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `codes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Hierarchies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `hierarchies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Control accounts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `control accounts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Normal balances** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `normal balances`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Templates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `templates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Restrictions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `restrictions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Localization** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `localization`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Lifecycle** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lifecycle`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ChartOfAccountsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-chart-of-accounts-filament/src/ChartOfAccountsFilamentPlugin.php) · [ChartOfAccountsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-chart-of-accounts-filament/src/ChartOfAccountsFilamentServiceProvider.php) · [AccountResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-chart-of-accounts-filament/src/Resources/AccountResource.php) · [CreateAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-chart-of-accounts-filament/src/Resources/AccountResource/Pages/CreateAccount.php) · [EditAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-chart-of-accounts-filament/src/Resources/AccountResource/Pages/EditAccount.php) · [ListAccounts.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-chart-of-accounts-filament/src/Resources/AccountResource/Pages/ListAccounts.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ArchiveAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-chart-of-accounts/src/Actions/ArchiveAccount.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(Account $account): Account` |
| [SaveAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-chart-of-accounts/src/Actions/SaveAccount.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(array $attributes, ?Account $account = null): Account` |
| [AccountPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-chart-of-accounts-api/src/Policies/AccountPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, Account $account): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, Account $account): bool`<br>`public function delete(?Authenticatable $user, Account $account): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Account.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-chart-of-accounts/src/Models/Account.php) | `legal_entity_id`, `code`, `name`, `description`, `type`, `normal_balance`, `parent_id`, `is_control_account`, `allow_manual_entry`, `is_active`, `locale`, `metadata` |
<!-- layer-implementation-plan:end -->
