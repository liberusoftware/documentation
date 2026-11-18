# Browser Game: Moderation and Analytics Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#moderation-and-analytics). Observed identity: [`liberusoftware/module-browser-game-moderation-and-analytics-livewire`](../../../modules/source/liberusoftware--module-browser-game-moderation-and-analytics-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-browser-game-moderation-and-analytics-livewire`  
**Matching domain module:** `browser-game-moderation-and-analytics`  
**Application:** Browser Game  
**Source feature:** [Moderation and Analytics](../features/moderation-and-analytics.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Reports:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Sanctions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Appeals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Telemetry:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Funnels:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Balance:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Economy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Fraud:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Health:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-browser-game-moderation-and-analytics-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-browser-game-moderation-and-analytics::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `reports`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sanctions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `appeals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `telemetry`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `funnels`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `balance`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `economy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `fraud`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `health`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `browser-game-moderation-and-analytics` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-browser-game-laravel-filament`](https://github.com/liberusoftware/project-browser-game-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/moderation-and-analytics.md) · [API plan](../api/moderation-and-analytics.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Reports** | Expose a focused Livewire 4 component and namespaced Blade default view for `reports` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Sanctions** | Expose a focused Livewire 4 component and namespaced Blade default view for `sanctions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Appeals** | Expose a focused Livewire 4 component and namespaced Blade default view for `appeals` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Telemetry** | Expose a focused Livewire 4 component and namespaced Blade default view for `telemetry` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Funnels** | Expose a focused Livewire 4 component and namespaced Blade default view for `funnels` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Balance** | Expose a focused Livewire 4 component and namespaced Blade default view for `balance` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Economy** | Expose a focused Livewire 4 component and namespaced Blade default view for `economy` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Fraud** | Expose a focused Livewire 4 component and namespaced Blade default view for `fraud` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Health** | Expose a focused Livewire 4 component and namespaced Blade default view for `health` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ModerationAndAnalyticsCatalog.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics-livewire/src/Livewire/ModerationAndAnalyticsCatalog.php) · [ModerationAndAnalyticsLivewireServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics-livewire/src/ModerationAndAnalyticsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ModerationAndAnalyticsQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/src/Queries/ModerationAndAnalyticsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ModerationAndAnalyticsRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/src/Models/ModerationAndAnalyticsRecord.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
