# CRM: Crm Templates And Snapshots Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-templates-and-snapshots). Observed identity: [`liberusoftware/module-crm-templates-and-snapshots-filament`](../../../modules/source/liberusoftware--module-crm-templates-and-snapshots-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-templates-and-snapshots-filament`  
**Matching domain module:** `crm-templates-and-snapshots`  
**Application:** CRM  
**Source feature:** [Crm Templates And Snapshots](../features/crm-templates-and-snapshots.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-templates-and-snapshots` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Versioned bundles of fields:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Pipelines:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Workflows:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Forms:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Funnels:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Calendars:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Templates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dashboards:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Settings with preview:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Protected sharing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Install:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Update:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rollback:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-templates-and-snapshots-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `versioned-bundles-of-fields`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `pipelines`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `workflows`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `forms`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `funnels`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `calendars`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `templates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dashboards`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `settings-with-preview`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `protected-sharing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `install`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `update`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rollback`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-templates-and-snapshots` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-templates-and-snapshots-filament`](https://github.com/liberusoftware/module-crm-templates-and-snapshots-filament) (`liberusoftware/crm-templates-and-snapshots-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-templates-and-snapshots.md) · [API plan](../api/crm-templates-and-snapshots.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Versioned bundles of fields** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `versioned bundles of fields`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Pipelines** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `pipelines`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Workflows** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `workflows`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Forms** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `forms`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Funnels** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `funnels`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Calendars** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `calendars`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Templates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `templates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dashboards** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dashboards`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Settings with preview** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `settings with preview`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Protected sharing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `protected sharing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Install** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `install`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Update** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `update`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rollback** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rollback`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [SnapshotResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots-filament/src/Resources/SnapshotResource.php) · [CreateSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots-filament/src/Resources/SnapshotResource/Pages/CreateSnapshot.php) · [EditSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots-filament/src/Resources/SnapshotResource/Pages/EditSnapshot.php) · [ListSnapshots.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots-filament/src/Resources/SnapshotResource/Pages/ListSnapshots.php) · [TemplatesAndSnapshotsFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-templates-and-snapshots-filament/src/TemplatesAndSnapshotsFilamentServiceProvider.php).

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
