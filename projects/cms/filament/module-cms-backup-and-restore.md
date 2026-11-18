# CMS: Module Cms Backup And Restore Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-backup-and-restore). Observed identity: [`liberusoftware/module-cms-backup-and-restore-filament`](../../../modules/source/liberusoftware--module-cms-backup-and-restore-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-module-cms-backup-and-restore-filament`  
**Matching domain module:** `module-cms-backup-and-restore`  
**Application:** CMS  
**Source feature:** [Module Cms Backup And Restore](../features/module-cms-backup-and-restore.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-cms-backup-and-restore` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Content/configuration/database/file backup contracts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Schedules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Encryption:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Retention:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Verification:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Restore preview:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Evidence:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-module-cms-backup-and-restore-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `content-configuration-database-file-backup-contracts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `schedules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `encryption`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `retention`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `verification`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `restore-preview`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `evidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-cms-backup-and-restore` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-backup-and-restore-filament`](https://github.com/liberusoftware/module-cms-backup-and-restore-filament) (`liberusoftware/cms-backup-and-restore-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-cms-backup-and-restore.md) · [API plan](../api/module-cms-backup-and-restore.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Content/configuration/database/file backup contracts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `content/configuration/database/file backup contracts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Schedules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `schedules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Encryption** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `encryption`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Retention** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `retention`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Verification** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `verification`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Restore preview** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `restore preview`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Evidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `evidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [BackupAndRestoreFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-backup-and-restore-filament/src/BackupAndRestoreFilamentServiceProvider.php) · [BackupArtifactResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-backup-and-restore-filament/src/Resources/BackupArtifactResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [BackupAndRestoreService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-backup-and-restore/src/Services/BackupAndRestoreService.php) | `public function createArtifact(?int $teamId, array $data): BackupArtifact`<br>`public function verify(BackupArtifact $artifact): BackupArtifact`<br>`public function restorePreview(BackupArtifact $artifact): array`<br>`public function schedule(?int $teamId, array $data): BackupSchedule` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BackupArtifact.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-backup-and-restore/src/Models/BackupArtifact.php) | `team_id`, `name`, `artifact_type`, `status`, `disk`, `path`, `size`, `checksum`, `encrypted`, `metadata`, `verified_at`, `expires_at` |
| [BackupSchedule.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-backup-and-restore/src/Models/BackupSchedule.php) | `team_id`, `name`, `frequency`, `artifact_types`, `retention_days`, `enabled`, `next_run_at`, `last_run_at` |
<!-- layer-implementation-plan:end -->
