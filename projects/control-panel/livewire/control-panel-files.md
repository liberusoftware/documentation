# Control Panel: Control Panel Files Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-files). Observed identity: [`liberusoftware/module-control-panel-files-livewire`](../../../modules/source/liberusoftware--module-control-panel-files-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-control-panel-control-panel-files-livewire`  
**Matching domain module:** `control-panel-files`  
**Application:** Control Panel  
**Source feature:** [Control Panel Files](../features/control-panel-files.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Home directories:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Permissions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **SFTP:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **File operations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Quotas:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Scanning:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Retention:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-control-panel-control-panel-files-livewire` component namespace and service provider; use explicit aliases such as `<livewire:controlpanelControlPanelFiles::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `home-directories`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `permissions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sftp`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `file-operations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `quotas`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `scanning`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `retention`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `control-panel-files` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-control-panel-laravel-filament`](https://github.com/liberusoftware/project-control-panel-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/control-panel-files.md) · [API plan](../api/control-panel-files.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Home directories** | Expose a focused Livewire 4 component and namespaced Blade default view for `home directories` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Permissions** | Expose a focused Livewire 4 component and namespaced Blade default view for `permissions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **SFTP** | Expose a focused Livewire 4 component and namespaced Blade default view for `sftp` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **File operations** | Expose a focused Livewire 4 component and namespaced Blade default view for `file operations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Quotas** | Expose a focused Livewire 4 component and namespaced Blade default view for `quotas` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Scanning** | Expose a focused Livewire 4 component and namespaced Blade default view for `scanning` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Retention** | Expose a focused Livewire 4 component and namespaced Blade default view for `retention` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [FileInventory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files-livewire/src/Components/FileInventory.php) · [QuotaInventory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files-livewire/src/Components/QuotaInventory.php) · [SftpInventory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files-livewire/src/Components/SftpInventory.php) · [FilesLivewireServiceProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files-livewire/src/FilesLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListFiles.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Queries/ListFiles.php) | `public function execute(string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateHomeDirectory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/CreateHomeDirectory.php) | `public function execute(array $attributes): HomeDirectory` |
| [CreateSftpAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/CreateSftpAccount.php) | `public function execute(array $attributes): SftpAccount` |
| [DeleteFile.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/DeleteFile.php) | `public function execute(FileEntry $file): FileEntry` |
| [DeleteSftpAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/DeleteSftpAccount.php) | `public function execute(SftpAccount $account): void` |
| [GrantFilePermission.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/GrantFilePermission.php) | `public function execute(array $attributes): FilePermission` |
| [MarkFileScanned.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/MarkFileScanned.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(FileEntry $file, bool $clean): FileEntry` |
| [RecordFileOperation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/RecordFileOperation.php) | `public function execute(array $a): FileOperation` |
| [RegenerateSftpKeyPair.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/RegenerateSftpKeyPair.php) | `public function execute(SftpAccount $account, ?int $bits = null): array` |
| [RegisterFile.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/RegisterFile.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(array $attributes): FileEntry` |
| [SetFileQuota.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Actions/SetFileQuota.php) | `public function execute(array $attributes): FileQuota` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FileEntry.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/FileEntry.php) | `team_id`, `owner_id`, `path`, `disk`, `mime_type`, `size_bytes`, `checksum`, `status`, `scanned_at`, `retention_until`, `metadata` |
| [FileOperation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/FileOperation.php) | `id`, `team_id`, `file_id`, `operation`, `status`, `details` |
| [FilePermission.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/FilePermission.php) | `id`, `team_id`, `file_id`, `home_directory_id`, `subject_id`, `subject_type`, `mode`, `recursive` |
| [FileQuota.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/FileQuota.php) | `id`, `team_id`, `owner_id`, `limit_bytes`, `used_bytes`, `files_count` |
| [FileRetention.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/FileRetention.php) | `id`, `team_id`, `file_id`, `retention_until`, `policy`, `active` |
| [HomeDirectory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/HomeDirectory.php) | `id`, `team_id`, `owner_id`, `path`, `disk`, `mode`, `status`, `metadata` |
| [SftpAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-files/src/Models/SftpAccount.php) | `id`, `team_id`, `owner_id`, `username`, `password`, `home_directory`, `quota_mb`, `bandwidth_limit_mb`, `active`, `last_login_at`, `ssh_key_auth_enabled`, `ssh_public_key`, `ssh_private_key`, `ssh_key_type`, `ssh_key_bits` |
<!-- layer-implementation-plan:end -->
