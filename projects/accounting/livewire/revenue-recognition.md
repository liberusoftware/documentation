# Accounting: Revenue Recognition Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#revenue-recognition). Observed identity: [`liberusoftware/module-accounting-revenue-recognition-livewire`](../../../modules/source/liberusoftware--module-accounting-revenue-recognition-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-revenue-recognition-livewire`  
**Matching domain module:** `accounting-revenue-recognition`  
**Application:** Accounting  
**Source feature:** [Revenue Recognition](../features/revenue-recognition.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Obligations/schedules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Allocation references:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Deferred/accrued revenue:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Recognition runs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Modifications:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reconciliation (optional):** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-revenue-recognition-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-revenue-recognition::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `obligations-schedules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `allocation-references`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `deferred-accrued-revenue`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `recognition-runs`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `modifications`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reconciliation-optional`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-revenue-recognition` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/revenue-recognition.md) · [API plan](../api/revenue-recognition.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Obligations/schedules** | Expose a focused Livewire 4 component and namespaced Blade default view for `obligations/schedules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Allocation references** | Expose a focused Livewire 4 component and namespaced Blade default view for `allocation references` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Deferred/accrued revenue** | Expose a focused Livewire 4 component and namespaced Blade default view for `deferred/accrued revenue` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Recognition runs** | Expose a focused Livewire 4 component and namespaced Blade default view for `recognition runs` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Modifications** | Expose a focused Livewire 4 component and namespaced Blade default view for `modifications` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reconciliation (optional)** | Expose a focused Livewire 4 component and namespaced Blade default view for `reconciliation (optional)` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [RevenueSchedules.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition-livewire/src/Livewire/RevenueSchedules.php) · [RevenueRecognitionLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition-livewire/src/RevenueRecognitionLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateRevenueSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Actions/CreateRevenueSchedule.php) | `public function handle(array $attributes): RevenueSchedule` |
| [ModifyRevenueSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Actions/ModifyRevenueSchedule.php) | `public function handle(RevenueSchedule $schedule, array $attributes): RevenueModification` |
| [RecognizeDueRevenue.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Actions/RecognizeDueRevenue.php) | `public function handle(RevenueSchedule $schedule, string $asOfDate, ?int $teamId = null): RevenueRecognitionRun` |
| [ReconcileRevenueRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Actions/ReconcileRevenueRun.php) | `public function handle(RevenueRecognitionRun $run, array $references = []): RevenueRecognitionRun` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RevenueAllocationReference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueAllocationReference.php) | `team_id`, `reference_type`, `reference_id`, `allocation`, `status`, `metadata` |
| [RevenueModification.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueModification.php) | `schedule_id`, `effective_date`, `amount_delta`, `reason`, `status`, `metadata` |
| [RevenueObligation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueObligation.php) | `team_id`, `source_type`, `source_id`, `description`, `currency`, `total_amount`, `start_date`, `periods`, `status`, `metadata` |
| [RevenueRecognitionRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueRecognitionRun.php) | `team_id`, `as_of_date`, `status`, `processed_entries`, `failed_entries`, `errors`, `metadata`, `started_at`, `finished_at` |
| [RevenueReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueReconciliation.php) | `run_id`, `reference_type`, `reference_id`, `expected_amount`, `recognized_amount`, `variance`, `status`, `notes`, `metadata` |
| [RevenueSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueSchedule.php) | `obligation_id`, `allocation_reference_id`, `total_amount`, `start_date`, `periods`, `deferred_account_ref`, `revenue_account_ref`, `status`, `funded`, `metadata` |
| [RevenueScheduleEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueScheduleEntry.php) | `schedule_id`, `period_number`, `recognition_date`, `amount`, `status`, `recognized_at`, `ledger_reference`, `metadata` |
<!-- layer-implementation-plan:end -->
