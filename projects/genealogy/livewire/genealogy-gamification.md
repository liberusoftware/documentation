# Genealogy: Genealogy Gamification Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-gamification). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-genealogy-genealogy-gamification-livewire`  
**Matching domain module:** `genealogy-gamification`  
**Application:** Genealogy  
**Source feature:** [Genealogy Gamification](../features/genealogy-gamification.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Genealogy gamification points:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Genealogy gamification achievements:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Genealogy gamification progress:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Genealogy gamification leaderboard:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-genealogy-genealogy-gamification-livewire` component namespace and service provider; use explicit aliases such as `<livewire:genealogyGenealogyGamification::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `genealogy-gamification-points`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `genealogy-gamification-achievements`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `genealogy-gamification-progress`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `genealogy-gamification-leaderboard`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `genealogy-gamification` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/genealogy-gamification.md) · [API plan](../api/genealogy-gamification.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Genealogy gamification points** | Expose a focused Livewire 4 component and namespaced Blade default view for `genealogy gamification points` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Genealogy gamification achievements** | Expose a focused Livewire 4 component and namespaced Blade default view for `genealogy gamification achievements` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Genealogy gamification progress** | Expose a focused Livewire 4 component and namespaced Blade default view for `genealogy gamification progress` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Genealogy gamification leaderboard** | Expose a focused Livewire 4 component and namespaced Blade default view for `genealogy gamification leaderboard` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AwardPoints.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-gamification/src/Actions/AwardPoints.php) | `public function execute(Model $user, string $activityType, int $points, ?string $description = null, array $metadata = [], ?Model $related = null): UserPoint` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Achievement.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-gamification/src/Models/Achievement.php) | `key`, `name`, `description`, `category`, `points`, `requirements`, `is_active`, `sort_order` |
| [UserAchievement.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-gamification/src/Models/UserAchievement.php) | `team_id`, `user_id`, `achievement_id`, `unlocked_at`, `progress_data` |
| [UserPoint.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-gamification/src/Models/UserPoint.php) | `team_id`, `user_id`, `activity_type`, `points`, `description`, `metadata`, `related_id`, `related_type` |
| [UserProgress.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-gamification/src/Models/UserProgress.php) | `team_id`, `user_id`, `achievement_id`, `current_progress`, `target_progress`, `progress_data`, `started_at`, `last_updated_at` |
<!-- layer-implementation-plan:end -->
