# Accounting: Accounting Financial Master Data Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-financial-master-data). Observed identity: [`liberusoftware/module-accounting-financial-master-data-filament`](../../../modules/source/liberusoftware--module-accounting-financial-master-data-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-financial-master-data-filament`  
**Matching domain module:** `accounting-financial-master-data`  
**Application:** Accounting  
**Source feature:** [Accounting Financial Master Data](../features/accounting-financial-master-data.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-financial-master-data` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Customers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Suppliers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Items/services:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Accounts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tax profiles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payment terms:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Addresses:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bank details references:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Lifecycle:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Deduplication:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-financial-master-data-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `customers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `suppliers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `items-services`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `accounts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tax-profiles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payment-terms`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `addresses`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bank-details-references`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `lifecycle`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `deduplication`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-financial-master-data` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-financial-master-data-filament`](https://github.com/liberusoftware/module-accounting-financial-master-data-filament) (`liberusoftware/accounting-financial-master-data-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-financial-master-data.md) · [API plan](../api/accounting-financial-master-data.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Customers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `customers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Suppliers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `suppliers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Items/services** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `items/services`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Accounts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `accounts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tax profiles** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tax profiles`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Payment terms** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payment terms`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Addresses** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `addresses`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bank details references** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bank details references`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Lifecycle** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lifecycle`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Deduplication** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `deduplication`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [FinancialMasterDataFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data-filament/src/FinancialMasterDataFilamentPlugin.php) · [FinancialMasterDataFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data-filament/src/FinancialMasterDataFilamentServiceProvider.php) · [ItemServiceResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data-filament/src/Resources/ItemServiceResource.php) · [CreateItemService.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data-filament/src/Resources/ItemServiceResource/Pages/CreateItemService.php) · [EditItemService.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data-filament/src/Resources/ItemServiceResource/Pages/EditItemService.php) · [ListItemServices.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data-filament/src/Resources/ItemServiceResource/Pages/ListItemServices.php) · [PartyResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data-filament/src/Resources/PartyResource.php) · [CreateParty.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data-filament/src/Resources/PartyResource/Pages/CreateParty.php) · [EditParty.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data-filament/src/Resources/PartyResource/Pages/EditParty.php) · [ListParties.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data-filament/src/Resources/PartyResource/Pages/ListParties.php).

| Observed core query | Public method signatures |
| --- | --- |
| [FindDuplicateParties.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Queries/FindDuplicateParties.php) | `public function handle(int $legalEntityId, ?string $type = null): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ArchiveParty.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Actions/ArchiveParty.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(Party $party): Party` |
| [MergeDuplicateParties.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Actions/MergeDuplicateParties.php) | `public function handle(Party $survivor, Party $duplicate): Party` |
| [SaveParty.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Actions/SaveParty.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(array $attributes, ?Party $party = null): Party` |
| [SaveReferenceData.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Actions/SaveReferenceData.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(string $modelClass, array $attributes, ?Model $record = null): Model` |
| [PartyPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data-api/src/Policies/PartyPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, Party $party): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, Party $party): bool`<br>`public function delete(?Authenticatable $user, Party $party): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Address.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Models/Address.php) | `party_id`, `kind`, `line_one`, `line_two`, `city`, `region`, `postal_code`, `country_code`, `is_primary`, `metadata` |
| [BankDetailReference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Models/BankDetailReference.php) | `party_id`, `label`, `account_name`, `bank_name`, `country_code`, `currency_code`, `masked_account`, `credential_reference`, `is_primary`, `status`, `metadata` |
| [ItemService.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Models/ItemService.php) | `legal_entity_id`, `sku`, `name`, `description`, `kind`, `unit`, `sales_price`, `purchase_price`, `tax_profile_id`, `status`, `metadata` |
| [Party.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Models/Party.php) | `legal_entity_id`, `type`, `reference`, `name`, `email`, `phone`, `tax_identifier`, `payment_term_id`, `credit_limit`, `status`, `metadata` |
| [PaymentTerm.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Models/PaymentTerm.php) | `legal_entity_id`, `code`, `name`, `days`, `status`, `metadata` |
| [TaxProfile.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Models/TaxProfile.php) | `legal_entity_id`, `code`, `name`, `rate`, `inclusive`, `recoverable`, `status`, `metadata` |
<!-- layer-implementation-plan:end -->
