# CRM: SLA and Entitlements Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sla-and-entitlements). Observed identity: [`liberusoftware/module-crm-sla-and-entitlements-filament`](../../../modules/source/liberusoftware--module-crm-sla-and-entitlements-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-sla-and-entitlements-filament`  
**Matching domain module:** `crm-sla-and-entitlements`  
**Application:** CRM  
**Source feature:** [SLA and Entitlements](../features/sla-and-entitlements.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-sla-and-entitlements` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Service contracts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Coverage:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Business calendars:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Response/resolution targets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Milestones:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Pauses:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Warnings:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Breaches:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Escalations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Exceptions:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-sla-and-entitlements-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `service-contracts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `coverage`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `business-calendars`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `response-resolution-targets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `milestones`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `pauses`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `warnings`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `breaches`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `escalations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `exceptions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-sla-and-entitlements` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-sla-and-entitlements-filament`](https://github.com/liberusoftware/module-crm-sla-and-entitlements-filament) (`liberusoftware/crm-sla-and-entitlements-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/sla-and-entitlements.md) · [API plan](../api/sla-and-entitlements.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Service contracts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `service contracts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Coverage** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `coverage`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Business calendars** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `business calendars`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Response/resolution targets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `response/resolution targets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Milestones** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `milestones`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Pauses** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `pauses`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Warnings** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `warnings`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Breaches** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `breaches`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Escalations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `escalations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Exceptions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exceptions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [SlaCaseResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements-filament/src/Resources/SlaCaseResource.php) · [ListSlaCases.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements-filament/src/Resources/SlaCaseResource/Pages/ListSlaCases.php) · [SlaContractResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements-filament/src/Resources/SlaContractResource.php) · [CreateSlaContract.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements-filament/src/Resources/SlaContractResource/Pages/CreateSlaContract.php) · [ListSlaContracts.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements-filament/src/Resources/SlaContractResource/Pages/ListSlaContracts.php) · [SlaAndEntitlementsFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements-filament/src/SlaAndEntitlementsFilamentPlugin.php) · [SlaAndEntitlementsFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements-filament/src/SlaAndEntitlementsFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [SlaQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Queries/SlaQuery.php) | `public function contracts(int $teamId)`<br>`public function calendars(int $teamId)`<br>`public function entitlements(int $teamId)`<br>`public function cases(int $teamId)`<br>`public function escalations(int $teamId)`<br>`public function exceptions(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCalendar.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/CreateCalendar.php) | `public function execute(int $teamId, int $actorId, array $data): SlaCalendar` |
| [CreateContract.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/CreateContract.php) | `public function execute(int $teamId, int $actorId, array $data): SlaContract` |
| [EvaluateCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/EvaluateCase.php) | `public function execute(int $teamId, int $actorId, int $caseId): array` |
| [OpenCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/OpenCase.php) | `public function execute(int $teamId, int $actorId, array $data): SlaCase` |
| [RequestException.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/RequestException.php) | `public function execute(int $teamId, int $actorId, array $data): SlaException` |
| [SetEntitlement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/SetEntitlement.php) | `public function execute(int $teamId, int $actorId, array $data): SlaEntitlement` |
| [TransitionCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/TransitionCase.php) | `public function execute(int $teamId, int $actorId, int $caseId, string $transition, array $data = []): SlaCase` |
| [SlaAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Services/SlaAudit.php) | `public function record(int $teamId, ?int $actorId, int $caseId, string $type, array $payload = []): SlaCaseEvent` |
| [SlaPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Services/SlaPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SlaCalendar.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaCalendar.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaCase.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaCaseEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaCaseEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaContract.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaContract.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaEntitlement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaEntitlement.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaEscalation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaEscalation.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaException.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaException.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
