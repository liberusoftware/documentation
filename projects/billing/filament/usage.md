# Billing: Usage Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#usage). Observed identity: [`liberusoftware/module-billing-usage-filament`](../../../modules/source/liberusoftware--module-billing-usage-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-billing-usage-filament`  
**Matching domain module:** `billing-usage`  
**Application:** Billing  
**Source feature:** [Usage](../features/usage.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `billing-usage` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Meter definitions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Ingestion:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Deduplication:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Aggregation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rating:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Corrections:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Thresholds:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-billing-usage-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `meter-definitions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ingestion`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `deduplication`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `aggregation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rating`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `corrections`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `thresholds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `billing-usage` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-billing-usage-filament`](https://github.com/liberusoftware/module-billing-usage-filament) (`liberusoftware/billing-usage-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/usage.md) · [API plan](../api/usage.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Meter definitions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `meter definitions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Ingestion** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ingestion`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Deduplication** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `deduplication`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Aggregation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `aggregation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rating** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rating`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Corrections** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `corrections`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Thresholds** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `thresholds`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [MeterResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage-filament/src/Resources/MeterResource.php) · [CreateMeter.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage-filament/src/Resources/MeterResource/Pages/CreateMeter.php) · [ListMeters.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage-filament/src/Resources/MeterResource/Pages/ListMeters.php) · [UsageRecordResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage-filament/src/Resources/UsageRecordResource.php) · [CreateUsageRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage-filament/src/Resources/UsageRecordResource/Pages/CreateUsageRecord.php) · [ListUsageRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage-filament/src/Resources/UsageRecordResource/Pages/ListUsageRecords.php) · [UsageFilamentPlugin.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage-filament/src/UsageFilamentPlugin.php) · [UsageFilamentServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage-filament/src/UsageFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AggregateUsage.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Queries/AggregateUsage.php) | `public function execute(int $meterId, ?int $customerId = null): object` |
| [ListMeters.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Queries/ListMeters.php) | `public function execute(?int $teamId = null): Collection` |
| [ListUsageRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Queries/ListUsageRecords.php) | `public function execute(?int $teamId = null, ?int $meterId = null): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CheckUsageThreshold.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Actions/CheckUsageThreshold.php) | `public function execute(Meter $meter, float $quantity): bool` |
| [CorrectUsage.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Actions/CorrectUsage.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(UsageRecord $record, float $quantity, string $eventKey): UsageRecord` |
| [DefineMeter.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Actions/DefineMeter.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): Meter` |
| [IngestUsage.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Actions/IngestUsage.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Meter $meter, array $attributes): UsageRecord` |
| [RateUsage.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Actions/RateUsage.php) | `public function execute(Meter $meter, float $quantity): int` |
| [TransitionMeter.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Actions/TransitionMeter.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Meter $meter, bool $active): Meter` |
| [UsagePolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Policies/UsagePolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, Meter $meter): bool`<br>`public function update(?Authenticatable $user, Meter $meter): bool` |
| [UsageRecordPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Policies/UsageRecordPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function create(?object $user): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Meter.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Models/Meter.php) | No literal fillable array detected; inspect the model and API schema. |
| [UsageRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage/src/Models/UsageRecord.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
