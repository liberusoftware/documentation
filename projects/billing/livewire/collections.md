# Billing: Collections Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#collections). Observed identity: [`liberusoftware/module-billing-collections-livewire`](../../../modules/source/liberusoftware--module-billing-collections-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-billing-collections-livewire`  
**Matching domain module:** `billing-collections`  
**Application:** Billing  
**Source feature:** [Collections](../features/collections.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Retries:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Dunning:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reminders:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Promises:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Credit control:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Suspension:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Write-off:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Recovery:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-billing-collections-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-billing-collections::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `retries`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `dunning`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reminders`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `promises`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `credit-control`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `suspension`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `write-off`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `recovery`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `billing-collections` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/collections.md) · [API plan](../api/collections.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Retries** | Expose a focused Livewire 4 component and namespaced Blade default view for `retries` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Dunning** | Expose a focused Livewire 4 component and namespaced Blade default view for `dunning` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reminders** | Expose a focused Livewire 4 component and namespaced Blade default view for `reminders` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Promises** | Expose a focused Livewire 4 component and namespaced Blade default view for `promises` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Credit control** | Expose a focused Livewire 4 component and namespaced Blade default view for `credit control` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Suspension** | Expose a focused Livewire 4 component and namespaced Blade default view for `suspension` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Write-off** | Expose a focused Livewire 4 component and namespaced Blade default view for `write-off` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Recovery** | Expose a focused Livewire 4 component and namespaced Blade default view for `recovery` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CollectionsLivewireServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections-livewire/src/CollectionsLivewireServiceProvider.php) · [CollectionCaseList.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-collections-livewire/src/Components/CollectionCaseList.php).

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
