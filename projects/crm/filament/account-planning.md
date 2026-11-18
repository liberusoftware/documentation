# CRM: Account Planning Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#account-planning). Observed identity: [`liberusoftware/module-crm-account-planning-filament`](../../../modules/source/liberusoftware--module-crm-account-planning-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-account-planning-filament`  
**Matching domain module:** `crm-account-planning`  
**Application:** CRM  
**Source feature:** [Account Planning](../features/account-planning.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-account-planning` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Account hierarchies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Stakeholders:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Influence maps:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Whitespace:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Account plans:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Objectives:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Risks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Mutual action plans:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Account-based coordination:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-account-planning-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `account-hierarchies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `stakeholders`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `influence-maps`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `whitespace`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `account-plans`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `objectives`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `risks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `mutual-action-plans`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `account-based-coordination`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-account-planning` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-account-planning-filament`](https://github.com/liberusoftware/module-crm-account-planning-filament) (`liberusoftware/crm-account-planning-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/account-planning.md) · [API plan](../api/account-planning.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Account hierarchies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `account hierarchies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Stakeholders** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `stakeholders`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Influence maps** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `influence maps`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Whitespace** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `whitespace`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Account plans** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `account plans`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Objectives** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `objectives`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Risks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `risks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Mutual action plans** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `mutual action plans`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Account-based coordination** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `account-based coordination`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AccountPlanningFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning-filament/src/AccountPlanningFilamentPlugin.php) · [AccountPlanningFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning-filament/src/AccountPlanningFilamentServiceProvider.php) · [AccountPlanningRecordResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning-filament/src/Resources/AccountPlanningRecordResource.php) · [CreateAccountPlanningRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning-filament/src/Resources/AccountPlanningRecordResource/Pages/CreateAccountPlanningRecord.php) · [EditAccountPlanningRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning-filament/src/Resources/AccountPlanningRecordResource/Pages/EditAccountPlanningRecord.php) · [ListAccountPlanningRecords.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning-filament/src/Resources/AccountPlanningRecordResource/Pages/ListAccountPlanningRecords.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AccountPlanningQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning/src/Queries/AccountPlanningQuery.php) | `public function records(int $teamId, ?string $kind = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [TransitionRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning/src/Actions/TransitionRecord.php) | `public function execute(int $teamId, int $id, string $status): AccountPlanningRecord` |
| [UpsertRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning/src/Actions/UpsertRecord.php) | `public function execute(int $teamId, array $attributes, ?int $id = null): AccountPlanningRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccountPlanningRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning/src/Models/AccountPlanningRecord.php) | `team_id`, `kind`, `name`, `status`, `account_id`, `owner_id`, `payload`, `starts_at`, `ends_at`, `completed_at` |
<!-- layer-implementation-plan:end -->
