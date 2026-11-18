# CMS: Module Cms Experimentation Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-experimentation). Observed identity: [`liberusoftware/module-cms-experimentation-livewire`](../../../modules/source/liberusoftware--module-cms-experimentation-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-module-cms-experimentation-livewire`  
**Matching domain module:** `module-cms-experimentation`  
**Application:** CMS  
**Source feature:** [Module Cms Experimentation](../features/module-cms-experimentation.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **A/B/multivariate content tests:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Allocation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Goals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Guardrails:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Analysis policy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Winner promotion:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **History:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-module-cms-experimentation-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsModuleCmsExperimentation::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `a-b-multivariate-content-tests`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `allocation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `goals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `guardrails`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `analysis-policy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `winner-promotion`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `history`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-cms-experimentation` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-cms-experimentation.md) · [API plan](../api/module-cms-experimentation.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **A/B/multivariate content tests** | Expose a focused Livewire 4 component and namespaced Blade default view for `a/b/multivariate content tests` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Allocation** | Expose a focused Livewire 4 component and namespaced Blade default view for `allocation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Goals** | Expose a focused Livewire 4 component and namespaced Blade default view for `goals` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Guardrails** | Expose a focused Livewire 4 component and namespaced Blade default view for `guardrails` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Analysis policy** | Expose a focused Livewire 4 component and namespaced Blade default view for `analysis policy` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Winner promotion** | Expose a focused Livewire 4 component and namespaced Blade default view for `winner promotion` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **History** | Expose a focused Livewire 4 component and namespaced Blade default view for `history` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ExperimentList.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-experimentation-livewire/src/Livewire/ExperimentList.php) · [ExperimentationLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-experimentation-livewire/src/ExperimentationLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ExperimentationQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/src/Queries/ExperimentationQuery.php) | `public function list(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function find(string $key): ?Experiment`<br>`public function active(string $key): ?Experiment` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ExperimentationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/src/Services/ExperimentationService.php) | `public function create(array $attributes, ?int $teamId = null): Experiment`<br>`public function start(Experiment $experiment): Experiment`<br>`public function stop(Experiment $experiment): Experiment`<br>`public function allocate(Experiment $experiment, string $subjectKey): ?ExperimentVariant`<br>`public function observe(Experiment $experiment, ExperimentVariant $variant, string $subjectKey, ?string $goalKey, float $value = 1): ExperimentObservation`<br>`public function promote(Experiment $experiment, ExperimentVariant $variant, ?string $reason = null, ?string $actorType = null, int\|string\|null $actorId = null): Experiment` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Experiment.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/src/Models/Experiment.php) | `key`, `name`, `type`, `status`, `allocation_percentage`, `goals`, `guardrails`, `analysis_policy`, `winner_variant_key`, `team_id` |
| [ExperimentObservation.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/src/Models/ExperimentObservation.php) | `experiment_id`, `variant_id`, `subject_key`, `goal_key`, `value`, `observed_at` |
| [ExperimentPromotion.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/src/Models/ExperimentPromotion.php) | `experiment_id`, `variant_id`, `actor_type`, `actor_id`, `reason`, `promoted_at` |
| [ExperimentVariant.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/src/Models/ExperimentVariant.php) | `experiment_id`, `key`, `name`, `content`, `weight` |
<!-- layer-implementation-plan:end -->
