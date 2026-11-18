# CRM: Crm Telephony Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-telephony). Observed identity: [`liberusoftware/module-crm-telephony-filament`](../../../modules/source/liberusoftware--module-crm-telephony-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-telephony-filament`  
**Matching domain module:** `crm-telephony`  
**Application:** CRM  
**Source feature:** [Crm Telephony](../features/crm-telephony.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-telephony` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Numbers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Caller ID:** resource/table/form/action or page behavior for this module's authorized workflow.
- **IVR:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Queues:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Business hours:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Skills:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recording:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Voicemail:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Transfers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dispositions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Click-to-call:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Call logging:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Provider adapters:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-telephony-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `numbers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `caller-id`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ivr`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `queues`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `business-hours`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `skills`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recording`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `voicemail`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `transfers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dispositions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `click-to-call`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `call-logging`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `provider-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-telephony` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-telephony-filament`](https://github.com/liberusoftware/module-crm-telephony-filament) (`liberusoftware/crm-telephony-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-telephony.md) · [API plan](../api/crm-telephony.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Numbers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `numbers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Caller ID** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `caller id`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **IVR** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ivr`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Queues** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `queues`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Business hours** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `business hours`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Skills** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `skills`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recording** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recording`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Voicemail** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `voicemail`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Transfers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `transfers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dispositions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dispositions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Click-to-call** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `click-to-call`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Call logging** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `call logging`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Provider adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provider adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [TelephonyCallResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony-filament/src/Resources/TelephonyCallResource.php) · [ListTelephonyCalls.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony-filament/src/Resources/TelephonyCallResource/Pages/ListTelephonyCalls.php) · [TelephonyNumberResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony-filament/src/Resources/TelephonyNumberResource.php) · [CreateTelephonyNumber.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony-filament/src/Resources/TelephonyNumberResource/Pages/CreateTelephonyNumber.php) · [ListTelephonyNumbers.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony-filament/src/Resources/TelephonyNumberResource/Pages/ListTelephonyNumbers.php) · [TelephonyQueueResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony-filament/src/Resources/TelephonyQueueResource.php) · [ListTelephonyQueues.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony-filament/src/Resources/TelephonyQueueResource/Pages/ListTelephonyQueues.php) · [TelephonyFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony-filament/src/TelephonyFilamentPlugin.php) · [TelephonyFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony-filament/src/TelephonyFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [TelephonyQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Queries/TelephonyQuery.php) | `public function numbers(int $teamId)`<br>`public function queues(int $teamId)`<br>`public function calls(int $teamId)`<br>`public function settings(int $teamId): ?TelephonySettings` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfigureTelephony.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Actions/ConfigureTelephony.php) | `public function execute(int $teamId, int $actorId, array $data): TelephonySettings` |
| [CreateTelephonyQueue.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Actions/CreateTelephonyQueue.php) | `public function execute(int $teamId, int $actorId, array $data): TelephonyQueue` |
| [LogTelephonyCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Actions/LogTelephonyCall.php) | `public function execute(int $teamId, int $actorId, array $data): TelephonyCall` |
| [UpdateCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Actions/UpdateCall.php) | `public function execute(int $teamId, int $actorId, int $callId, array $data): TelephonyCall` |
| [UpsertTelephonyNumber.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Actions/UpsertTelephonyNumber.php) | `public function execute(int $teamId, int $actorId, array $data, ?int $id = null): TelephonyNumber` |
| [TelephonyAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Services/TelephonyAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): Audit` |
| [TelephonyPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Services/TelephonyPolicy.php) | `public function canManage(int $teamId, int $userId): bool`<br>`public function isTeamMember(int $teamId, int $userId, array $roles = [], bool $includeOwner = false): bool` |
| [TenantTwilioService.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Services/TenantTwilioService.php) | `public function client(int $teamId): Client`<br>`public function sendMessage(int $teamId, string $to, string $body): object`<br>`public function usage(int $teamId, array $filters = []): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TelephonyAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Models/TelephonyAudit.php) | No literal fillable array detected; inspect the model and API schema. |
| [TelephonyCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Models/TelephonyCall.php) | No literal fillable array detected; inspect the model and API schema. |
| [TelephonyNumber.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Models/TelephonyNumber.php) | No literal fillable array detected; inspect the model and API schema. |
| [TelephonyQueue.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Models/TelephonyQueue.php) | No literal fillable array detected; inspect the model and API schema. |
| [TelephonySettings.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Models/TelephonySettings.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
