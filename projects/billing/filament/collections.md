# Billing: Collections Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#collections). Observed identity: [`liberusoftware/module-billing-collections-filament`](../../../modules/source/liberusoftware--module-billing-collections-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-billing-collections-filament`  
**Matching domain module:** `billing-collections`  
**Application:** Billing  
**Source feature:** [Collections](../features/collections.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `billing-collections` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Retries:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dunning:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reminders:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Promises:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Credit control:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Suspension:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Write-off:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recovery:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-billing-collections-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `retries`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dunning`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reminders`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `promises`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `credit-control`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `suspension`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `write-off`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recovery`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `billing-collections` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-billing-collections-filament`](https://github.com/liberusoftware/module-billing-collections-filament) (`liberusoftware/billing-collections-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/collections.md) · [API plan](../api/collections.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Retries** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `retries`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dunning** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dunning`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reminders** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reminders`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Promises** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `promises`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Credit control** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `credit control`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Suspension** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `suspension`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Write-off** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `write-off`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recovery** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recovery`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CollectionsFilamentPlugin.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections-filament/src/CollectionsFilamentPlugin.php) · [CollectionsFilamentServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections-filament/src/CollectionsFilamentServiceProvider.php) · [CollectionCaseResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections-filament/src/Resources/CollectionCaseResource.php) · [CreateCollectionCase.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections-filament/src/Resources/CollectionCaseResource/Pages/CreateCollectionCase.php) · [ListCollectionCases.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections-filament/src/Resources/CollectionCaseResource/Pages/ListCollectionCases.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListCollectionCases.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Queries/ListCollectionCases.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApplyCreditControl.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/ApplyCreditControl.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, string $level, ?string $reason = null): CollectionCase` |
| [OpenCollectionCase.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/OpenCollectionCase.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): CollectionCase` |
| [PromisePayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/PromisePayment.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, \DateTimeInterface $dueAt): CollectionCase` |
| [RecoverCollectionCase.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/RecoverCollectionCase.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case): CollectionCase` |
| [RetryCollectionCase.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/RetryCollectionCase.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, \DateTimeInterface $nextActionAt): CollectionCase` |
| [ScheduleDunning.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/ScheduleDunning.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, \DateTimeInterface $nextActionAt): CollectionCase` |
| [ScheduleReminder.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/ScheduleReminder.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, \DateTimeInterface $nextActionAt): CollectionCase` |
| [SuspendCollectionCase.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/SuspendCollectionCase.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, string $reason): CollectionCase` |
| [WriteOffCollectionCase.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Actions/WriteOffCollectionCase.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CollectionCase $case, string $reason): CollectionCase` |
| [CollectionCasePolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Policies/CollectionCasePolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, CollectionCase $case): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CollectionCase.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections/src/Models/CollectionCase.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
