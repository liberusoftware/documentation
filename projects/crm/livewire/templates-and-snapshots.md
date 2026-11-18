# CRM: Templates and Snapshots Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#templates-and-snapshots). Observed identity: [`liberusoftware/module-crm-templates-and-snapshots-livewire`](../../../modules/source/liberusoftware--module-crm-templates-and-snapshots-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-templates-and-snapshots-livewire`  
**Matching domain module:** `crm-templates-and-snapshots`  
**Application:** CRM  
**Source feature:** [Templates and Snapshots](../features/templates-and-snapshots.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Versioned bundles of fields:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Pipelines:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Workflows:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Forms:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Funnels:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Calendars:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Templates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Dashboards:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Settings with preview:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Protected sharing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Install:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Update:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Rollback:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-templates-and-snapshots-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-templates-and-snapshots::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `versioned-bundles-of-fields`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `pipelines`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `workflows`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `forms`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `funnels`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `calendars`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `templates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `dashboards`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `settings-with-preview`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `protected-sharing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `install`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `update`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `rollback`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-templates-and-snapshots` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/templates-and-snapshots.md) · [API plan](../api/templates-and-snapshots.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Versioned bundles of fields** | Expose a focused Livewire 4 component and namespaced Blade default view for `versioned bundles of fields` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Pipelines** | Expose a focused Livewire 4 component and namespaced Blade default view for `pipelines` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Workflows** | Expose a focused Livewire 4 component and namespaced Blade default view for `workflows` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Forms** | Expose a focused Livewire 4 component and namespaced Blade default view for `forms` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Funnels** | Expose a focused Livewire 4 component and namespaced Blade default view for `funnels` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Calendars** | Expose a focused Livewire 4 component and namespaced Blade default view for `calendars` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Templates** | Expose a focused Livewire 4 component and namespaced Blade default view for `templates` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Dashboards** | Expose a focused Livewire 4 component and namespaced Blade default view for `dashboards` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Settings with preview** | Expose a focused Livewire 4 component and namespaced Blade default view for `settings with preview` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Protected sharing** | Expose a focused Livewire 4 component and namespaced Blade default view for `protected sharing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Install** | Expose a focused Livewire 4 component and namespaced Blade default view for `install` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Update** | Expose a focused Livewire 4 component and namespaced Blade default view for `update` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Rollback** | Expose a focused Livewire 4 component and namespaced Blade default view for `rollback` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [SnapshotDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots-livewire/src/Components/SnapshotDashboard.php) · [TemplatesAndSnapshotsLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots-livewire/src/TemplatesAndSnapshotsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [SnapshotQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Queries/SnapshotQuery.php) | `public function list(int $teamId)`<br>`public function find(int $teamId, int $id): SnapshotBundle`<br>`public function preview(int $teamId, int $id): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Actions/CreateSnapshot.php) | `public function execute(int $teamId, int $actorId, array $data): SnapshotBundle` |
| [InstallSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Actions/InstallSnapshot.php) | `public function execute(int $teamId, int $actorId, int $bundleId): SnapshotInstall` |
| [RollbackSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Actions/RollbackSnapshot.php) | `public function execute(int $teamId, int $actorId, int $bundleId, int $version): SnapshotInstall` |
| [ShareSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Actions/ShareSnapshot.php) | `public function execute(int $teamId, int $actorId, int $bundleId): string` |
| [UpdateSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Actions/UpdateSnapshot.php) | `public function execute(int $teamId, int $actorId, int $bundleId, array $data): SnapshotBundle` |
| [SnapshotAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Services/SnapshotAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): void` |
| [SnapshotPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Services/SnapshotPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SnapshotAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Models/SnapshotAudit.php) | `team_id`, `actor_id`, `event`, `details` |
| [SnapshotBundle.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Models/SnapshotBundle.php) | `team_id`, `name`, `version`, `status`, `payload`, `checksum`, `share_token_hash`, `shared_at`, `created_by` |
| [SnapshotInstall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots/src/Models/SnapshotInstall.php) | `team_id`, `bundle_id`, `version`, `status`, `installed_by` |
<!-- layer-implementation-plan:end -->
