# CMS: Content Integrity Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#content-integrity). Observed identity: [`liberusoftware/module-cms-content-integrity-livewire`](../../../modules/source/liberusoftware--module-cms-content-integrity-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-content-integrity-livewire`  
**Matching domain module:** `cms-content-integrity`  
**Application:** CMS  
**Source feature:** [Content Integrity](../features/content-integrity.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Broken links/embeds/media:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Orphan detection:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Schema validation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Duplicate content:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Scheduled scans:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Repair queues:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reports:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-content-integrity-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-cms-content-integrity::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `broken-links-embeds-media`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `orphan-detection`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `schema-validation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `duplicate-content`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `scheduled-scans`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `repair-queues`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reports`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-content-integrity` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/content-integrity.md) · [API plan](../api/content-integrity.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Broken links/embeds/media** | Expose a focused Livewire 4 component and namespaced Blade default view for `broken links/embeds/media` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Orphan detection** | Expose a focused Livewire 4 component and namespaced Blade default view for `orphan detection` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Schema validation** | Expose a focused Livewire 4 component and namespaced Blade default view for `schema validation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Duplicate content** | Expose a focused Livewire 4 component and namespaced Blade default view for `duplicate content` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Scheduled scans** | Expose a focused Livewire 4 component and namespaced Blade default view for `scheduled scans` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Repair queues** | Expose a focused Livewire 4 component and namespaced Blade default view for `repair queues` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reports** | Expose a focused Livewire 4 component and namespaced Blade default view for `reports` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [IntegrityReport.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-integrity-livewire/src/Livewire/IntegrityReport.php) · [ContentIntegrityLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-integrity-livewire/src/ContentIntegrityLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ContentIntegrityService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-integrity/src/Services/ContentIntegrityService.php) | `public function findings(?int $teamId, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function startScan(?int $teamId, string $scope = 'all'): IntegrityScan`<br>`public function finding(IntegrityScan $scan, array $data): IntegrityFinding`<br>`public function completeScan(IntegrityScan $scan): IntegrityScan`<br>`public function resolve(IntegrityFinding $finding): IntegrityFinding` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [IntegrityFinding.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-integrity/src/Models/IntegrityFinding.php) | `scan_id`, `team_id`, `subject_type`, `subject_key`, `kind`, `severity`, `message`, `context`, `status`, `resolved_at` |
| [IntegrityScan.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-integrity/src/Models/IntegrityScan.php) | `team_id`, `scope`, `status`, `finding_count`, `started_at`, `completed_at` |
<!-- layer-implementation-plan:end -->
