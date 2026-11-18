# CRM: Agency Workspace Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#agency-workspace). Observed identity: [`liberusoftware/module-crm-agency-workspace-filament`](../../../modules/source/liberusoftware--module-crm-agency-workspace-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-agency-workspace-filament`  
**Matching domain module:** `crm-agency-workspace`  
**Application:** CRM  
**Source feature:** [Agency Workspace](../features/agency-workspace.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-agency-workspace` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Agency/client hierarchy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sub-accounts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Delegated administration:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Usage visibility:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Support access:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Branding:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cross-account operations:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-agency-workspace-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `agency-client-hierarchy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sub-accounts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `delegated-administration`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `usage-visibility`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `support-access`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `branding`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cross-account-operations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-agency-workspace` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-agency-workspace-filament`](https://github.com/liberusoftware/module-crm-agency-workspace-filament) (`liberusoftware/crm-agency-workspace-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/agency-workspace.md) · [API plan](../api/agency-workspace.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Agency/client hierarchy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `agency/client hierarchy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sub-accounts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sub-accounts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Delegated administration** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `delegated administration`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Usage visibility** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `usage visibility`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Support access** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `support access`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Branding** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `branding`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cross-account operations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cross-account operations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AgencyWorkspaceFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace-filament/src/AgencyWorkspaceFilamentPlugin.php) · [AgencyWorkspaceFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace-filament/src/AgencyWorkspaceFilamentServiceProvider.php) · [AgencyAccountResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace-filament/src/Resources/AgencyAccountResource.php) · [CreateAgencyAccountPage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace-filament/src/Resources/AgencyAccountResource/Pages/CreateAgencyAccountPage.php) · [EditAgencyAccount.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace-filament/src/Resources/AgencyAccountResource/Pages/EditAgencyAccount.php) · [ListAgencyAccounts.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace-filament/src/Resources/AgencyAccountResource/Pages/ListAgencyAccounts.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AgencyQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Queries/AgencyQuery.php) | `public function accounts(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAgencyAccount.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Actions/CreateAgencyAccount.php) | `public function execute(int $teamId, int $ownerId, array $input): AgencyAccount` |
| [GrantAgencyAccess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Actions/GrantAgencyAccess.php) | `public function execute(int $teamId, int $actorId, AgencyAccount $account, array $input): AgencyAccess` |
| [UpdateAgencyUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Actions/UpdateAgencyUsage.php) | `public function execute(int $teamId, int $actorId, AgencyAccount $account, array $input): AgencyAccount` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AgencyAccess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Models/AgencyAccess.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgencyAccount.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Models/AgencyAccount.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgencyAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-agency-workspace/src/Models/AgencyAudit.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
