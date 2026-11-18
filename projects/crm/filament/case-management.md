# CRM: Case Management Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#case-management). Observed identity: [`liberusoftware/module-crm-case-management-filament`](../../../modules/source/liberusoftware--module-crm-case-management-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-case-management-filament`  
**Matching domain module:** `crm-case-management`  
**Application:** CRM  
**Source feature:** [Case Management](../features/case-management.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-case-management` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Tickets/cases:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Types:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Pipelines:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Statuses:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Priorities:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Ownership:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Parent/child cases:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Related assets/orders:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Entitlements:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Escalation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Audit:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-case-management-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `tickets-cases`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `types`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `pipelines`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `statuses`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `priorities`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ownership`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `parent-child-cases`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `related-assets-orders`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `entitlements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `escalation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `audit`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-case-management` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-case-management-filament`](https://github.com/liberusoftware/module-crm-case-management-filament) (`liberusoftware/crm-case-management-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/case-management.md) · [API plan](../api/case-management.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Tickets/cases** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tickets/cases`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Types** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `types`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Pipelines** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `pipelines`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Statuses** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `statuses`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Priorities** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `priorities`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Ownership** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ownership`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Parent/child cases** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `parent/child cases`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Related assets/orders** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `related assets/orders`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Entitlements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `entitlements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Escalation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `escalation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Audit** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `audit`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CaseManagementFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-case-management-filament/src/CaseManagementFilamentPlugin.php) · [CaseManagementFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-case-management-filament/src/CaseManagementFilamentServiceProvider.php) · [CaseResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-case-management-filament/src/Resources/CaseResource.php) · [CreateCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-case-management-filament/src/Resources/CaseResource/Pages/CreateCase.php) · [EditCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-case-management-filament/src/Resources/CaseResource/Pages/EditCase.php) · [ListCases.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-case-management-filament/src/Resources/CaseResource/Pages/ListCases.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CaseQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-case-management/src/Queries/CaseQuery.php) | `public function cases(int $teamId): Builder`<br>`public function queue(int $teamId, string $status = 'open'): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [OpenCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-case-management/src/Actions/OpenCase.php) | `public function execute(int $teamId, int $ownerId, array $input): CaseRecord` |
| [TransitionCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-case-management/src/Actions/TransitionCase.php) | `public function execute(int $teamId, int $actorId, CaseRecord $case, string $status, ?int $ownerId = null): CaseRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CaseAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-case-management/src/Models/CaseAudit.php) | No literal fillable array detected; inspect the model and API schema. |
| [CaseRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-case-management/src/Models/CaseRecord.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
