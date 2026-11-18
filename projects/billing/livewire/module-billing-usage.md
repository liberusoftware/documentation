# Billing: Module Billing Usage Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-usage). Observed identity: [`liberusoftware/module-billing-usage-livewire`](../../../modules/source/liberusoftware--module-billing-usage-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-billing-module-billing-usage-livewire`  
**Matching domain module:** `module-billing-usage`  
**Application:** Billing  
**Source feature:** [Module Billing Usage](../features/module-billing-usage.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Meter definitions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Ingestion:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Deduplication:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Aggregation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Rating:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Corrections:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Thresholds:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-billing-module-billing-usage-livewire` component namespace and service provider; use explicit aliases such as `<livewire:billingModuleBillingUsage::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `meter-definitions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `ingestion`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `deduplication`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `aggregation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `rating`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `corrections`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `thresholds`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-billing-usage` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-billing-usage.md) · [API plan](../api/module-billing-usage.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Meter definitions** | Expose a focused Livewire 4 component and namespaced Blade default view for `meter definitions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Ingestion** | Expose a focused Livewire 4 component and namespaced Blade default view for `ingestion` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Deduplication** | Expose a focused Livewire 4 component and namespaced Blade default view for `deduplication` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Aggregation** | Expose a focused Livewire 4 component and namespaced Blade default view for `aggregation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Rating** | Expose a focused Livewire 4 component and namespaced Blade default view for `rating` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Corrections** | Expose a focused Livewire 4 component and namespaced Blade default view for `corrections` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Thresholds** | Expose a focused Livewire 4 component and namespaced Blade default view for `thresholds` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [MeterList.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage-livewire/src/Components/MeterList.php) · [UsageDashboard.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage-livewire/src/Components/UsageDashboard.php) · [UsageRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage-livewire/src/Components/UsageRecords.php) · [UsageLivewireServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-usage-livewire/src/UsageLivewireServiceProvider.php).

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
