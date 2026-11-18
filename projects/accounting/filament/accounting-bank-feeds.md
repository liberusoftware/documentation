# Accounting: Accounting Bank Feeds Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-bank-feeds). Observed identity: [`liberusoftware/module-accounting-bank-feeds-filament`](../../../modules/source/liberusoftware--module-accounting-bank-feeds-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-bank-feeds-filament`  
**Matching domain module:** `accounting-bank-feeds`  
**Application:** Accounting  
**Source feature:** [Accounting Bank Feeds](../features/accounting-bank-feeds.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-bank-feeds` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Consent/connections:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Institutions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Account mapping:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cursors:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Imports:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Duplicates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Pending/posted state:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Health:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Provider adapters:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-bank-feeds-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `consent-connections`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `institutions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `account-mapping`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cursors`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `imports`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `duplicates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `pending-posted-state`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `health`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `provider-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-bank-feeds` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-bank-feeds-filament`](https://github.com/liberusoftware/module-accounting-bank-feeds-filament) (`liberusoftware/accounting-bank-feeds-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-bank-feeds.md) · [API plan](../api/accounting-bank-feeds.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Consent/connections** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `consent/connections`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Institutions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `institutions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Account mapping** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `account mapping`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cursors** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cursors`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Imports** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `imports`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Duplicates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `duplicates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Pending/posted state** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `pending/posted state`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Health** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `health`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Provider adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provider adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [BankFeedsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds-filament/src/BankFeedsFilamentPlugin.php) · [BankFeedsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds-filament/src/BankFeedsFilamentServiceProvider.php) · [BankFeedConnectionResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds-filament/src/Resources/BankFeedConnectionResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [BankFeedQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Queries/BankFeedQuery.php) | `public function connections(?int $teamId = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateBankFeedConnection.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/CreateBankFeedConnection.php) | `public function handle(array $attributes): BankFeedConnection` |
| [ImportBankFeedTransactions.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/ImportBankFeedTransactions.php) | `public function handle(BankFeedConnection $connection, array $batch): array` |
| [MapBankFeedAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/MapBankFeedAccount.php) | `public function handle(BankFeedConnection $connection, array $attributes): BankFeedAccountMapping` |
| [SetBankFeedTransactionStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/SetBankFeedTransactionStatus.php) | `public function handle(BankFeedTransaction $transaction, FeedTransactionStatus $status): BankFeedTransaction` |
| [UpdateBankFeedHealth.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/UpdateBankFeedHealth.php) | `public function handle(BankFeedConnection $connection, ?string $error = null): BankFeedConnection` |
| [UpsertBankFeedInstitution.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/UpsertBankFeedInstitution.php) | `public function handle(array $attributes): BankFeedInstitution` |
| [BankFeedAdapter.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Contracts/BankFeedAdapter.php) | `public function fetch(BankFeedConnection $connection): array` |
| [BankFeedsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds-api/src/Policies/BankFeedsPolicy.php) | `public function viewAny(?object $user = null): bool`<br>`public function view(?object $user, object $connection): bool`<br>`public function create(?object $user = null): bool`<br>`public function update(?object $user, object $connection): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BankFeedAccountMapping.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Models/BankFeedAccountMapping.php) | `team_id`, `connection_id`, `bank_account_id`, `external_account_id`, `name`, `currency`, `metadata` |
| [BankFeedConnection.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Models/BankFeedConnection.php) | `team_id`, `user_id`, `institution_id`, `provider`, `name`, `external_reference`, `access_token`, `credentials`, `cursor`, `status`, `last_synced_at`, `last_error`, `last_error_at`, `metadata` |
| [BankFeedInstitution.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Models/BankFeedInstitution.php) | `provider`, `external_id`, `name`, `country`, `logo_url`, `metadata` |
| [BankFeedTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Models/BankFeedTransaction.php) | `team_id`, `connection_id`, `mapping_id`, `external_id`, `transaction_date`, `posted_date`, `description`, `amount`, `currency`, `status`, `category`, `raw_data`, `metadata` |
<!-- layer-implementation-plan:end -->
