# CMS: Cms Backup And Restore Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-backup-and-restore). Observed identity: [`liberusoftware/module-cms-backup-and-restore-livewire`](../../../modules/source/liberusoftware--module-cms-backup-and-restore-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-cms-backup-and-restore-livewire`  
**Matching domain module:** `cms-backup-and-restore`  
**Application:** CMS  
**Source feature:** [Cms Backup And Restore](../features/cms-backup-and-restore.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Content/configuration/database/file backup contracts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Schedules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Encryption:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Retention:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Verification:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Restore preview:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Evidence:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-cms-backup-and-restore-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsCmsBackupAndRestore::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `content-configuration-database-file-backup-contracts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `schedules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `encryption`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `retention`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `verification`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `restore-preview`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `evidence`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-backup-and-restore` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/cms-backup-and-restore.md) · [API plan](../api/cms-backup-and-restore.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Content/configuration/database/file backup contracts** | Expose a focused Livewire 4 component and namespaced Blade default view for `content/configuration/database/file backup contracts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Schedules** | Expose a focused Livewire 4 component and namespaced Blade default view for `schedules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Encryption** | Expose a focused Livewire 4 component and namespaced Blade default view for `encryption` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Retention** | Expose a focused Livewire 4 component and namespaced Blade default view for `retention` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Verification** | Expose a focused Livewire 4 component and namespaced Blade default view for `verification` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Restore preview** | Expose a focused Livewire 4 component and namespaced Blade default view for `restore preview` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Evidence** | Expose a focused Livewire 4 component and namespaced Blade default view for `evidence` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [BackupPreview.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-backup-and-restore-livewire/src/Livewire/BackupPreview.php) · [BackupAndRestoreLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-backup-and-restore-livewire/src/BackupAndRestoreLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [BackupAndRestoreService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-backup-and-restore/src/Services/BackupAndRestoreService.php) | `public function createArtifact(?int $teamId, array $data): BackupArtifact`<br>`public function verify(BackupArtifact $artifact): BackupArtifact`<br>`public function restorePreview(BackupArtifact $artifact): array`<br>`public function schedule(?int $teamId, array $data): BackupSchedule` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BackupArtifact.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-backup-and-restore/src/Models/BackupArtifact.php) | `team_id`, `name`, `artifact_type`, `status`, `disk`, `path`, `size`, `checksum`, `encrypted`, `metadata`, `verified_at`, `expires_at` |
| [BackupSchedule.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-backup-and-restore/src/Models/BackupSchedule.php) | `team_id`, `name`, `frequency`, `artifact_types`, `retention_days`, `enabled`, `next_run_at`, `last_run_at` |
<!-- layer-implementation-plan:end -->
