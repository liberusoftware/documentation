# Accounting: Accounting Periods Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-periods). Observed identity: [`liberusoftware/module-accounting-periods-filament`](../../../modules/source/liberusoftware--module-accounting-periods-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-periods-filament`  
**Matching domain module:** `accounting-periods`  
**Application:** Accounting  
**Source feature:** [Accounting Periods](../features/accounting-periods.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-periods` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Open/soft-close/hard-close states:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Transaction-date controls:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Module dependencies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Locks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reopen approval:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Evidence:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-periods-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `open-soft-close-hard-close-states`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `transaction-date-controls`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `module-dependencies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `locks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reopen-approval`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `evidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-periods` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-periods-filament`](https://github.com/liberusoftware/module-accounting-periods-filament) (`liberusoftware/accounting-periods-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-periods.md) · [API plan](../api/accounting-periods.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Open/soft-close/hard-close states** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `open/soft-close/hard-close states`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Transaction-date controls** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `transaction-date controls`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Module dependencies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `module dependencies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Locks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `locks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reopen approval** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reopen approval`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Evidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `evidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AccountingPeriodsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods-filament/src/AccountingPeriodsFilamentPlugin.php) · [AccountingPeriodsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods-filament/src/AccountingPeriodsFilamentServiceProvider.php) · [AccountingPeriodResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods-filament/src/Resources/AccountingPeriodResource.php) · [ListAccountingPeriods.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods-filament/src/Resources/AccountingPeriodResource/Pages/ListAccountingPeriods.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods/src/Actions/CreatePeriod.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(array $attributes): AccountingPeriod` |
| [LockPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods/src/Actions/LockPeriod.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(AccountingPeriod $period, ?string $actor): AccountingPeriod` |
| [TransitionPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods/src/Actions/TransitionPeriod.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(AccountingPeriod $period, PeriodState $to, ?string $actor = null, ?string $reason = null): AccountingPeriod` |
| [UnlockPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods/src/Actions/UnlockPeriod.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(AccountingPeriod $period, ?string $actor, ?string $reason): AccountingPeriod` |
| [AccountingPeriodsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods-api/src/Policies/AccountingPeriodsPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccountingPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods/src/Models/AccountingPeriod.php) | `book_id`, `starts_on`, `ends_on`, `state`, `posting_ends_on`, `locked_by`, `locked_at`, `reopened_by`, `reopen_reason`, `evidence` |
<!-- layer-implementation-plan:end -->
