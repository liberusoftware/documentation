# Accounting: Collections Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#collections). Observed identity: [`liberusoftware/module-accounting-collections-livewire`](../../../modules/source/liberusoftware--module-accounting-collections-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-collections-livewire`  
**Matching domain module:** `accounting-collections`  
**Application:** Accounting  
**Source feature:** [Collections](../features/collections.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Reminder schedules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Statement runs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Promise-to-pay:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Disputes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Late fees/interest policy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Collection stages:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Write-offs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Agency adapters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-collections-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-collections::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `reminder-schedules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `statement-runs`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `promise-to-pay`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `disputes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `late-fees-interest-policy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `collection-stages`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `write-offs`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `agency-adapters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-collections` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/collections.md) · [API plan](../api/collections.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Reminder schedules** | Expose a focused Livewire 4 component and namespaced Blade default view for `reminder schedules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Statement runs** | Expose a focused Livewire 4 component and namespaced Blade default view for `statement runs` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Promise-to-pay** | Expose a focused Livewire 4 component and namespaced Blade default view for `promise-to-pay` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Disputes** | Expose a focused Livewire 4 component and namespaced Blade default view for `disputes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Late fees/interest policy** | Expose a focused Livewire 4 component and namespaced Blade default view for `late fees/interest policy` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Collection stages** | Expose a focused Livewire 4 component and namespaced Blade default view for `collection stages` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Write-offs** | Expose a focused Livewire 4 component and namespaced Blade default view for `write-offs` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Agency adapters** | Expose a focused Livewire 4 component and namespaced Blade default view for `agency adapters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CollectionsLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections-livewire/src/CollectionsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CollectionCaseQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Queries/CollectionCaseQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCollectionCase.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Actions/CreateCollectionCase.php) | `public function handle(array $attributes): CollectionCase` |
| [PrepareCollectionStatement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Actions/PrepareCollectionStatement.php) | `public function handle(CollectionCase $case, array $statement): CollectionCase` |
| [RecordCollectionActivity.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Actions/RecordCollectionActivity.php) | `public function reminder(CollectionCase $case, array $reminder): CollectionCase`<br>`public function promise(CollectionCase $case, array $promise): CollectionCase`<br>`public function dispute(CollectionCase $case, array $dispute): CollectionCase` |
| [SendToCollectionAgency.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Actions/SendToCollectionAgency.php) | `public function handle(CollectionCase $case, string $agency): CollectionCase` |
| [WriteOffCollectionCase.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Actions/WriteOffCollectionCase.php) | `public function handle(CollectionCase $case, array $writeOff): CollectionCase` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CollectionCase.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Models/CollectionCase.php) | `team_id`, `case_ref`, `customer_ref`, `balance`, `stage`, `interest_rate`, `reminders`, `statement_run`, `promise_to_pay`, `disputes`, `write_off`, `agency` |
<!-- layer-implementation-plan:end -->
