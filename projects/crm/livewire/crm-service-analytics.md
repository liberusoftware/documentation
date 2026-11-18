# CRM: Crm Service Analytics Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-service-analytics). Observed identity: [`liberusoftware/module-crm-service-analytics-livewire`](../../../modules/source/liberusoftware--module-crm-service-analytics-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-service-analytics-livewire`  
**Matching domain module:** `crm-service-analytics`  
**Application:** CRM  
**Source feature:** [Crm Service Analytics](../features/crm-service-analytics.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Volume:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Backlog:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Deflection:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **First response:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Resolution:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reopen:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Transfer:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **SLA:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Satisfaction:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Quality:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Staffing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cost-to-serve:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-service-analytics-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmServiceAnalytics::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `volume`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `backlog`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `deflection`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `first-response`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `resolution`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reopen`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `transfer`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sla`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `satisfaction`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `quality`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `staffing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cost-to-serve`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-service-analytics` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-service-analytics.md) · [API plan](../api/crm-service-analytics.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Volume** | Expose a focused Livewire 4 component and namespaced Blade default view for `volume` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Backlog** | Expose a focused Livewire 4 component and namespaced Blade default view for `backlog` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Deflection** | Expose a focused Livewire 4 component and namespaced Blade default view for `deflection` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **First response** | Expose a focused Livewire 4 component and namespaced Blade default view for `first response` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Resolution** | Expose a focused Livewire 4 component and namespaced Blade default view for `resolution` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reopen** | Expose a focused Livewire 4 component and namespaced Blade default view for `reopen` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Transfer** | Expose a focused Livewire 4 component and namespaced Blade default view for `transfer` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **SLA** | Expose a focused Livewire 4 component and namespaced Blade default view for `sla` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Satisfaction** | Expose a focused Livewire 4 component and namespaced Blade default view for `satisfaction` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Quality** | Expose a focused Livewire 4 component and namespaced Blade default view for `quality` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Staffing** | Expose a focused Livewire 4 component and namespaced Blade default view for `staffing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cost-to-serve** | Expose a focused Livewire 4 component and namespaced Blade default view for `cost-to-serve` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [AnalyticsDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics-livewire/src/Components/AnalyticsDashboard.php) · [ServiceAnalyticsLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics-livewire/src/ServiceAnalyticsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AnalyticsQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Queries/AnalyticsQuery.php) | `public function snapshots(int $teamId)`<br>`public function metric(int $teamId, string $metric, $from = null, $to = null)`<br>`public function summary(int $teamId, $from = null, $to = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordMetric.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Actions/RecordMetric.php) | `public function execute(int $teamId, int $actorId, array $data): AnalyticsSnapshot` |
| [RecordServiceMetrics.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Actions/RecordServiceMetrics.php) | `public function execute(int $teamId, int $actorId, array $metrics): int` |
| [AnalyticsAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Services/AnalyticsAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): Audit` |
| [AnalyticsPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Services/AnalyticsPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AnalyticsAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Models/AnalyticsAudit.php) | No literal fillable array detected; inspect the model and API schema. |
| [AnalyticsSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Models/AnalyticsSnapshot.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
