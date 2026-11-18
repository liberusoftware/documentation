# Billing: Module Billing Core Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-core). Observed identity: [`liberusoftware/module-billing-core-filament`](../../../modules/source/liberusoftware--module-billing-core-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-billing-module-billing-core-filament`  
**Matching domain module:** `module-billing-core`  
**Application:** Billing  
**Source feature:** [Module Billing Core](../features/module-billing-core.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-billing-core` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Accounts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Contacts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Currencies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tax profiles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sequences:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Terms:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Billing settings:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-billing-module-billing-core-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `accounts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `contacts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `currencies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tax-profiles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sequences`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `terms`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `billing-settings`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-billing-core` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-billing-module-billing-core-filament`](https://github.com/liberusoftware/module-billing-module-billing-core-filament) (`liberusoftware/billing-module-billing-core-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-billing-core.md) · [API plan](../api/module-billing-core.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Accounts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `accounts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Contacts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `contacts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Currencies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `currencies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tax profiles** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tax profiles`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sequences** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sequences`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Terms** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `terms`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Billing settings** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `billing settings`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [BillingCoreFilamentPlugin.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-filament/src/BillingCoreFilamentPlugin.php) · [BillingCoreFilamentServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-filament/src/BillingCoreFilamentServiceProvider.php) · [BillingAccountResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-filament/src/Resources/BillingAccountResource.php) · [CreateBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-filament/src/Resources/BillingAccountResource/Pages/CreateBillingAccount.php) · [EditBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-filament/src/Resources/BillingAccountResource/Pages/EditBillingAccount.php) · [ListBillingAccounts.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-filament/src/Resources/BillingAccountResource/Pages/ListBillingAccounts.php) · [BillingContactResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-filament/src/Resources/BillingContactResource.php) · [CreateBillingContact.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-filament/src/Resources/BillingContactResource/Pages/CreateBillingContact.php) · [EditBillingContact.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-filament/src/Resources/BillingContactResource/Pages/EditBillingContact.php) · [ListBillingContacts.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-filament/src/Resources/BillingContactResource/Pages/ListBillingContacts.php) · [BillingCoreResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-filament/src/Resources/BillingCoreResource.php) · [BillingCurrencyResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-filament/src/Resources/BillingCurrencyResource.php) · [CreateBillingCurrency.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-filament/src/Resources/BillingCurrencyResource/Pages/CreateBillingCurrency.php) · [EditBillingCurrency.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-filament/src/Resources/BillingCurrencyResource/Pages/EditBillingCurrency.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListBillingAccounts.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Queries/ListBillingAccounts.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ListBillingRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Queries/ListBillingRecords.php) | `public function execute(string $modelClass, ?int $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CalculateTax.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/CalculateTax.php) | `public function execute(int $teamId, float $amount, ?string $jurisdiction = null, ?int $customerId = null): array` |
| [ConvertCurrency.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/ConvertCurrency.php) | `public function execute(int $teamId, float $amount, string $from, string $to): array` |
| [CreateBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/CreateBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): BillingAccount` |
| [CreateBillingRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/CreateBillingRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(string $modelClass, array $attributes): Model` |
| [DeleteBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/DeleteBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(BillingAccount $account): void` |
| [DeleteBillingRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/DeleteBillingRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Model $record, string $recordType): void` |
| [TransitionBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/TransitionBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(BillingAccount $account, BillingAccountStatus $status): BillingAccount` |
| [UpdateBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/UpdateBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(BillingAccount $account, array $attributes): BillingAccount` |
| [UpdateBillingRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/UpdateBillingRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Model $record, array $attributes): Model` |
| [BillingAccountPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Policies/BillingAccountPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, BillingAccount $account): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, BillingAccount $account): bool`<br>`public function delete(object $user, BillingAccount $account): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingAccount.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingContact.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingContact.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingCurrency.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingCurrency.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingSequence.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingSequence.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingSetting.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingSetting.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingTaxExemption.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingTaxExemption.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingTaxProfile.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingTaxProfile.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingTerm.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingTerm.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
