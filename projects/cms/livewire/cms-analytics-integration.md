# CMS: Cms Analytics Integration Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-analytics-integration). Observed identity: [`liberusoftware/module-cms-analytics-integration-livewire`](../../../modules/source/liberusoftware--module-cms-analytics-integration-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-cms-analytics-integration-livewire`  
**Matching domain module:** `cms-analytics-integration`  
**Application:** CMS  
**Source feature:** [Cms Analytics Integration](../features/cms-analytics-integration.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Canonical content/view/conversion events:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Consent-aware analytics mappings:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Dashboards:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Boilerplate analytics adapters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-cms-analytics-integration-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsCmsAnalyticsIntegration::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `canonical-content-view-conversion-events`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `consent-aware-analytics-mappings`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `dashboards`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `boilerplate-analytics-adapters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-analytics-integration` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/cms-analytics-integration.md) · [API plan](../api/cms-analytics-integration.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Canonical content/view/conversion events** | Expose a focused Livewire 4 component and namespaced Blade default view for `canonical content/view/conversion events` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Consent-aware analytics mappings** | Expose a focused Livewire 4 component and namespaced Blade default view for `consent-aware analytics mappings` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Dashboards** | Expose a focused Livewire 4 component and namespaced Blade default view for `dashboards` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Boilerplate analytics adapters** | Expose a focused Livewire 4 component and namespaced Blade default view for `boilerplate analytics adapters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [AnalyticsDashboard.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-analytics-integration-livewire/src/Livewire/AnalyticsDashboard.php) · [AnalyticsIntegrationLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-analytics-integration-livewire/src/AnalyticsIntegrationLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AnalyticsAdapterInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-analytics-integration/src/Contracts/AnalyticsAdapterInterface.php) | `public function key(): string`<br>`public function payload(AnalyticsEvent $event, array $mapping): array` |
| [AnalyticsIntegrationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-analytics-integration/src/Services/AnalyticsIntegrationService.php) | `public function recordEvent(?int $teamId, array $data): AnalyticsEvent`<br>`public function saveMapping(?int $teamId, array $data): AnalyticsMapping`<br>`public function dashboard(?int $teamId, ?string $from = null, ?string $to = null): array`<br>`public function registerAdapter(AnalyticsAdapterInterface $adapter): void`<br>`public function adapterPayload(string $provider, AnalyticsEvent $event, AnalyticsMapping $mapping): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AnalyticsEvent.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-analytics-integration/src/Models/AnalyticsEvent.php) | `team_id`, `event_type`, `event_name`, `subject_type`, `subject_id`, `consent_category`, `consent_granted`, `status`, `idempotency_key`, `payload`, `occurred_at` |
| [AnalyticsMapping.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-analytics-integration/src/Models/AnalyticsMapping.php) | `team_id`, `event_type`, `provider`, `measurement_key`, `consent_category`, `config`, `enabled` |
<!-- layer-implementation-plan:end -->
