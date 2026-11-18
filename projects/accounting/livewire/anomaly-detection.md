# Accounting: Anomaly Detection Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#anomaly-detection). Observed identity: [`liberusoftware/module-accounting-anomaly-detection-livewire`](../../../modules/source/liberusoftware--module-accounting-anomaly-detection-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-anomaly-detection-livewire`  
**Matching domain module:** `accounting-anomaly-detection`  
**Application:** Accounting  
**Source feature:** [Anomaly Detection](../features/anomaly-detection.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Duplicates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Unusual amounts/accounts/timing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Control breaches:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Missing sequences:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Fraud indicators:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Review queues:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-anomaly-detection-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-anomaly-detection::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `duplicates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `unusual-amounts-accounts-timing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `control-breaches`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `missing-sequences`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `fraud-indicators`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `review-queues`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-anomaly-detection` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/anomaly-detection.md) · [API plan](../api/anomaly-detection.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Duplicates** | Expose a focused Livewire 4 component and namespaced Blade default view for `duplicates` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Unusual amounts/accounts/timing** | Expose a focused Livewire 4 component and namespaced Blade default view for `unusual amounts/accounts/timing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Control breaches** | Expose a focused Livewire 4 component and namespaced Blade default view for `control breaches` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Missing sequences** | Expose a focused Livewire 4 component and namespaced Blade default view for `missing sequences` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Fraud indicators** | Expose a focused Livewire 4 component and namespaced Blade default view for `fraud indicators` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Review queues** | Expose a focused Livewire 4 component and namespaced Blade default view for `review queues` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Anomalies.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-anomaly-detection-livewire/src/Livewire/Anomalies.php) · [AnomalyDetectionLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-anomaly-detection-livewire/src/AnomalyDetectionLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AnomalyQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-anomaly-detection/src/Queries/AnomalyQuery.php) | `public function paginate(int $teamId, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordAnomaly.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-anomaly-detection/src/Actions/RecordAnomaly.php) | `public function handle(array $attributes): Anomaly` |
| [SendToReview.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-anomaly-detection/src/Actions/SendToReview.php) | `public function handle(Anomaly $anomaly): Anomaly` |
| [AnomalyPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-anomaly-detection-api/src/Policies/AnomalyPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function update(?object $user, object $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Anomaly.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-anomaly-detection/src/Models/Anomaly.php) | `team_id`, `kind`, `source_type`, `source_id`, `title`, `description`, `confidence`, `status`, `evidence`, `detected_at`, `resolved_at` |
<!-- layer-implementation-plan:end -->
