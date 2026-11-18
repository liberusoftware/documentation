# CMS: Content Locking Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#content-locking). Observed identity: [`liberusoftware/module-cms-content-locking-livewire`](../../../modules/source/liberusoftware--module-cms-content-locking-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-content-locking-livewire`  
**Matching domain module:** `cms-content-locking`  
**Application:** CMS  
**Source feature:** [Content Locking](../features/content-locking.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Optimistic concurrency:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Edit presence:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Takeover policy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Conflict comparison:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Merge:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Recovery:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-content-locking-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-cms-content-locking::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `optimistic-concurrency`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `edit-presence`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `takeover-policy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `conflict-comparison`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `merge`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `recovery`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-content-locking` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/content-locking.md) · [API plan](../api/content-locking.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Optimistic concurrency** | Expose a focused Livewire 4 component and namespaced Blade default view for `optimistic concurrency` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Edit presence** | Expose a focused Livewire 4 component and namespaced Blade default view for `edit presence` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Takeover policy** | Expose a focused Livewire 4 component and namespaced Blade default view for `takeover policy` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Conflict comparison** | Expose a focused Livewire 4 component and namespaced Blade default view for `conflict comparison` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Merge** | Expose a focused Livewire 4 component and namespaced Blade default view for `merge` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Recovery** | Expose a focused Livewire 4 component and namespaced Blade default view for `recovery` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [LockPresence.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-locking-livewire/src/Livewire/LockPresence.php) · [ContentLockingLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-locking-livewire/src/ContentLockingLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ContentLockingService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-locking/src/Services/ContentLockingService.php) | `public function acquire(string $subjectType, string $subjectKey, ?int $teamId, ?int $holderId, array $snapshot = [], ?int $ttlMinutes = null): ContentLock`<br>`public function renew(ContentLock $lock, string $token, ?int $ttlMinutes = null): ContentLock`<br>`public function release(ContentLock $lock, string $token): void`<br>`public function compare(ContentLock $lock, array $current): array`<br>`public function merge(ContentLock $lock, array $current, string $token): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ContentLock.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-locking/src/Models/ContentLock.php) | `team_id`, `subject_type`, `subject_key`, `holder_id`, `token`, `version`, `snapshot`, `expires_at` |
<!-- layer-implementation-plan:end -->
