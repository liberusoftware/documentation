# CMS: Module Cms Content Intelligence Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-content-intelligence). Observed identity: [`liberusoftware/module-cms-content-intelligence-livewire`](../../../modules/source/liberusoftware--module-cms-content-intelligence-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-module-cms-content-intelligence-livewire`  
**Matching domain module:** `module-cms-content-intelligence`  
**Application:** CMS  
**Source feature:** [Module Cms Content Intelligence](../features/module-cms-content-intelligence.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Inventory:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Quality:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Readability:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Accessibility:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **SEO:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Freshness:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Duplication:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Gaps:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Performance:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Improvement queues:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-module-cms-content-intelligence-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsModuleCmsContentIntelligence::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `inventory`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `quality`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `readability`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `accessibility`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `seo`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `freshness`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `duplication`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `gaps`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `performance`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `improvement-queues`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-cms-content-intelligence` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-cms-content-intelligence.md) · [API plan](../api/module-cms-content-intelligence.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Inventory** | Expose a focused Livewire 4 component and namespaced Blade default view for `inventory` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Quality** | Expose a focused Livewire 4 component and namespaced Blade default view for `quality` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Readability** | Expose a focused Livewire 4 component and namespaced Blade default view for `readability` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Accessibility** | Expose a focused Livewire 4 component and namespaced Blade default view for `accessibility` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **SEO** | Expose a focused Livewire 4 component and namespaced Blade default view for `seo` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Freshness** | Expose a focused Livewire 4 component and namespaced Blade default view for `freshness` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Duplication** | Expose a focused Livewire 4 component and namespaced Blade default view for `duplication` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Gaps** | Expose a focused Livewire 4 component and namespaced Blade default view for `gaps` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Performance** | Expose a focused Livewire 4 component and namespaced Blade default view for `performance` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Improvement queues** | Expose a focused Livewire 4 component and namespaced Blade default view for `improvement queues` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [InsightQueue.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-intelligence-livewire/src/Livewire/InsightQueue.php) · [ContentIntelligenceLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-intelligence-livewire/src/ContentIntelligenceLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ContentIntelligenceService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-intelligence/src/Services/ContentIntelligenceService.php) | `public function insights(?int $teamId, ?string $metric = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function analyze(array $data, ?int $teamId = null): ContentInsight`<br>`public function review(ContentInsight $insight, string $status): ContentInsight` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ContentInsight.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-intelligence/src/Models/ContentInsight.php) | `team_id`, `subject_type`, `subject_key`, `metric`, `score`, `severity`, `summary`, `rationale`, `context`, `status`, `reviewed_at` |
<!-- layer-implementation-plan:end -->
