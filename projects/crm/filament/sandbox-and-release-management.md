# CRM: Sandbox and Release Management Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sandbox-and-release-management). Observed identity: [`liberusoftware/module-crm-sandbox-and-release-management-filament`](../../../modules/source/liberusoftware--module-crm-sandbox-and-release-management-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-sandbox-and-release-management-filament`  
**Matching domain module:** `crm-sandbox-and-release-management`  
**Application:** CRM  
**Source feature:** [Sandbox and Release Management](../features/sandbox-and-release-management.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-sandbox-and-release-management` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Configuration snapshots:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Test data policy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Change sets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Validation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dependency analysis:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Promotion:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rollback:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Environment comparison:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-sandbox-and-release-management-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `configuration-snapshots`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `test-data-policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `change-sets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `validation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dependency-analysis`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `promotion`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rollback`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `environment-comparison`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-sandbox-and-release-management` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-sandbox-and-release-management-filament`](https://github.com/liberusoftware/module-crm-sandbox-and-release-management-filament) (`liberusoftware/crm-sandbox-and-release-management-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/sandbox-and-release-management.md) · [API plan](../api/sandbox-and-release-management.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Configuration snapshots** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `configuration snapshots`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Test data policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `test data policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Change sets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `change sets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Validation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `validation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dependency analysis** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dependency analysis`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Promotion** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `promotion`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rollback** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rollback`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Environment comparison** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `environment comparison`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ReleaseResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management-filament/src/Resources/ReleaseResource.php) · [ListReleases.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management-filament/src/Resources/ReleaseResource/Pages/ListReleases.php) · [SandboxAndReleaseManagementFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management-filament/src/SandboxAndReleaseManagementFilamentPlugin.php) · [SandboxAndReleaseManagementFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management-filament/src/SandboxAndReleaseManagementFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ReleaseQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Queries/ReleaseQuery.php) | `public function snapshots(int $teamId)`<br>`public function changesets(int $teamId)`<br>`public function deployments(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/CreateChangeset.php) | `public function execute(int $teamId, int $actorId, array $data): ReleaseChangeset` |
| [CreateSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/CreateSnapshot.php) | `public function execute(int $teamId, int $actorId, array $data): ReleaseSnapshot` |
| [PromoteChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/PromoteChangeset.php) | `public function execute(int $teamId, int $actorId, int $id, array $data = []): ReleaseDeployment` |
| [RollbackChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/RollbackChangeset.php) | `public function execute(int $teamId, int $actorId, int $id, array $data = []): ReleaseDeployment` |
| [ValidateChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/ValidateChangeset.php) | `public function execute(int $teamId, int $actorId, int $id): ReleaseChangeset` |
| [ReleaseAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Services/ReleaseAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): void` |
| [ReleasePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Services/ReleasePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReleaseChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Models/ReleaseChangeset.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReleaseDeployment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Models/ReleaseDeployment.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReleaseSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Models/ReleaseSnapshot.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
