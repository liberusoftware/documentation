# Accounting: General Ledger Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#general-ledger). Observed identity: [`liberusoftware/module-accounting-general-ledger-filament`](../../../modules/source/liberusoftware--module-accounting-general-ledger-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-general-ledger-filament`  
**Matching domain module:** `accounting-general-ledger`  
**Application:** Accounting  
**Source feature:** [General Ledger](../features/general-ledger.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-general-ledger` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Journals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Balanced postings:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recurring journals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reversals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Corrections:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Allocations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Accruals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Prepayments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Balances:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-general-ledger-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `journals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `balanced-postings`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recurring-journals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reversals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `corrections`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `allocations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `accruals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `prepayments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `balances`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-general-ledger` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-general-ledger-filament`](https://github.com/liberusoftware/module-accounting-general-ledger-filament) (`liberusoftware/accounting-general-ledger-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/general-ledger.md) · [API plan](../api/general-ledger.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Journals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `journals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Balanced postings** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `balanced postings`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recurring journals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recurring journals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reversals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reversals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Corrections** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `corrections`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Allocations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `allocations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Accruals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `accruals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Prepayments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `prepayments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Balances** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `balances`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [GeneralLedgerFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger-filament/src/GeneralLedgerFilamentPlugin.php) · [GeneralLedgerFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger-filament/src/GeneralLedgerFilamentServiceProvider.php) · [JournalResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger-filament/src/Resources/JournalResource.php) · [CreateJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger-filament/src/Resources/JournalResource/Pages/CreateJournal.php) · [ListJournals.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger-filament/src/Resources/JournalResource/Pages/ListJournals.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AccountBalances.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Queries/AccountBalances.php) | `public function handle(int $bookId, ?string $through = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAccrual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreateAccrual.php) | `public function handle(array $attributes, array $lines): JournalEntry` |
| [CreateAllocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreateAllocation.php) | `public function handle(array $attributes, array $lines): JournalEntry` |
| [CreateCorrection.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreateCorrection.php) | `public function handle(array $attributes, array $lines): JournalEntry` |
| [CreateJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreateJournal.php) | `public function handle(array $attributes, array $lines): JournalEntry` |
| [CreatePrepayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreatePrepayment.php) | `public function handle(array $attributes, array $lines): JournalEntry` |
| [CreateTypedJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreateTypedJournal.php) | `public function handle(JournalType $type, array $attributes, array $lines): JournalEntry` |
| [GenerateRecurringJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/GenerateRecurringJournal.php) | `public function handle(RecurringJournal $template, ?string $actor = null): JournalEntry` |
| [PostJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/PostJournal.php) | `public function handle(JournalEntry $journal, ?string $actor = null): JournalEntry` |
| [ReverseJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/ReverseJournal.php) | `public function handle(JournalEntry $journal, array $attributes = [], ?string $actor = null): JournalEntry` |
| [SaveRecurringJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/SaveRecurringJournal.php) | `public function handle(array $attributes, ?RecurringJournal $template = null): RecurringJournal` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [JournalEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Models/JournalEntry.php) | `book_id`, `entry_number`, `entry_date`, `journal_type`, `status`, `description`, `source_type`, `source_id`, `reversal_of_id`, `posted_by`, `posted_at`, `metadata` |
| [JournalLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Models/JournalLine.php) | `journal_entry_id`, `account_id`, `debit`, `credit`, `description`, `dimensions` |
| [RecurringJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Models/RecurringJournal.php) | `book_id`, `name`, `frequency`, `next_run_on`, `end_on`, `is_active`, `description`, `lines`, `metadata` |
<!-- layer-implementation-plan:end -->
