# Genealogy: Liberu Executive Insights Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#liberu-executive-insights). Observed identity: [`liberusoftware/module-liberu-executive-insights-livewire`](../../../modules/source/liberusoftware--module-liberu-executive-insights-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-genealogy-liberu-executive-insights-livewire`  
**Matching domain module:** `liberu-executive-insights`  
**Application:** Genealogy  
**Source feature:** [Liberu Executive Insights](../features/liberu-executive-insights.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Metric registry:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cross-product projections:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Evidence drill-through:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Decision snapshots:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Data-quality operations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-genealogy-liberu-executive-insights-livewire` component namespace and service provider; use explicit aliases such as `<livewire:genealogyLiberuExecutiveInsights::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `metric-registry`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cross-product-projections`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `evidence-drill-through`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `decision-snapshots`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `data-quality-operations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `liberu-executive-insights` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/liberu-executive-insights.md) · [API plan](../api/liberu-executive-insights.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Metric registry** | Expose a focused Livewire 4 component and namespaced Blade default view for `metric registry` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cross-product projections** | Expose a focused Livewire 4 component and namespaced Blade default view for `cross-product projections` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Evidence drill-through** | Expose a focused Livewire 4 component and namespaced Blade default view for `evidence drill-through` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Decision snapshots** | Expose a focused Livewire 4 component and namespaced Blade default view for `decision snapshots` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Data-quality operations** | Expose a focused Livewire 4 component and namespaced Blade default view for `data-quality operations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ExecutiveInsightsLivewireServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-executive-insights-livewire/src/ExecutiveInsightsLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RegisterMetric.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-executive-insights/src/Actions/RegisterMetric.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(array $attributes): MetricDefinition` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MetricDefinition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-executive-insights/src/Models/MetricDefinition.php) | `team_id`, `key`, `name`, `formula`, `version`, `dimensions`, `currency`, `timezone`, `freshness_seconds`, `is_active` |
<!-- layer-implementation-plan:end -->
