# CMS: Cms Migration Framework Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-migration-framework). Observed identity: [`liberusoftware/module-cms-migration-framework-livewire`](../../../modules/source/liberusoftware--module-cms-migration-framework-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-cms-migration-framework-livewire`  
**Matching domain module:** `cms-migration-framework`  
**Application:** CMS  
**Source feature:** [Cms Migration Framework](../features/cms-migration-framework.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Source adapters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Inventories:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Mapping:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Dry run:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Transforms:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Identity/media/link resolution:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Batches:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Resume:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reconciliation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-cms-migration-framework-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsCmsMigrationFramework::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `source-adapters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `inventories`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `mapping`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `dry-run`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `transforms`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `identity-media-link-resolution`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `batches`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `resume`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reconciliation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-migration-framework` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/cms-migration-framework.md) · [API plan](../api/cms-migration-framework.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Source adapters** | Expose a focused Livewire 4 component and namespaced Blade default view for `source adapters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Inventories** | Expose a focused Livewire 4 component and namespaced Blade default view for `inventories` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Mapping** | Expose a focused Livewire 4 component and namespaced Blade default view for `mapping` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Dry run** | Expose a focused Livewire 4 component and namespaced Blade default view for `dry run` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Transforms** | Expose a focused Livewire 4 component and namespaced Blade default view for `transforms` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Identity/media/link resolution** | Expose a focused Livewire 4 component and namespaced Blade default view for `identity/media/link resolution` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Batches** | Expose a focused Livewire 4 component and namespaced Blade default view for `batches` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Resume** | Expose a focused Livewire 4 component and namespaced Blade default view for `resume` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reconciliation** | Expose a focused Livewire 4 component and namespaced Blade default view for `reconciliation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [MigrationJobList.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-migration-framework-livewire/src/Livewire/MigrationJobList.php) · [MigrationFrameworkLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-migration-framework-livewire/src/MigrationFrameworkLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [MigrationFrameworkService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-migration-framework/src/Services/MigrationFrameworkService.php) | `public function start(string $source, array $options = [], ?int $teamId = null): MigrationJob`<br>`public function add(MigrationJob $job, string $recordType, string $sourceId, array $payload = []): MigrationRecord`<br>`public function process(MigrationRecord $record, bool $success, ?string $failureReason = null): MigrationRecord`<br>`public function complete(MigrationJob $job): MigrationJob` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MigrationJob.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-migration-framework/src/Models/MigrationJob.php) | `public_id`, `source`, `status`, `total_records`, `processed_records`, `failed_records`, `options`, `failure_reason`, `started_at`, `completed_at`, `team_id` |
| [MigrationRecord.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-migration-framework/src/Models/MigrationRecord.php) | `job_id`, `record_type`, `source_id`, `status`, `payload`, `failure_reason`, `processed_at`, `team_id` |
<!-- layer-implementation-plan:end -->
