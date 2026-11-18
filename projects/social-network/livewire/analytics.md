# Social Network: Analytics Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#analytics). Observed identity: [`liberusoftware/module-social-network-analytics-livewire`](../../../modules/source/liberusoftware--module-social-network-analytics-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-social-network-analytics-livewire`  
**Matching domain module:** `social-network-analytics`  
**Application:** Social Network  
**Source feature:** [Analytics](../features/analytics.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Growth:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Engagement:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Retention:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Health:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Moderation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Delivery:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Privacy-governed insights:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-social-network-analytics-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-social-network-analytics::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `growth`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `engagement`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `retention`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `health`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `moderation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `delivery`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `privacy-governed-insights`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `social-network-analytics` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/analytics.md) · [API plan](../api/analytics.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Growth** | Expose a focused Livewire 4 component and namespaced Blade default view for `growth` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Engagement** | Expose a focused Livewire 4 component and namespaced Blade default view for `engagement` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Retention** | Expose a focused Livewire 4 component and namespaced Blade default view for `retention` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Health** | Expose a focused Livewire 4 component and namespaced Blade default view for `health` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Moderation** | Expose a focused Livewire 4 component and namespaced Blade default view for `moderation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Delivery** | Expose a focused Livewire 4 component and namespaced Blade default view for `delivery` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Privacy-governed insights** | Expose a focused Livewire 4 component and namespaced Blade default view for `privacy-governed insights` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [AnalyticsLivewireServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics-livewire/src/AnalyticsLivewireServiceProvider.php) · [Dashboard.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics-livewire/src/Components/Dashboard.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [BuildSnapshot.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Actions/BuildSnapshot.php) | `public function __construct( private AnalyticsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(object $actor, string $metric, string $periodStart, string $periodEnd, int $cohortSize, float $value, array $dimensions = []): MetricSnapshot` |
| [GetMetrics.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Actions/GetMetrics.php) | `public function __construct(private AnalyticsAuthorizer $authorizer)`<br>`public function handle(object $actor, string $metric, int $limit = 30): Collection` |
| [RecordMetric.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Actions/RecordMetric.php) | `public function __construct( private AnalyticsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(object $actor, string $name, array $dimensions = [], int $value = 1): AnalyticsEvent` |
| [AnalyticsAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Contracts/AnalyticsAuthorizer.php) | `public function view(object $actor, string $metric): void`<br>`public function record(object $actor, string $metric): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AnalyticsEvent.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Models/AnalyticsEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [MetricSnapshot.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Models/MetricSnapshot.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
