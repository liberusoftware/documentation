# CRM: Crm Events And Webinars Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-events-and-webinars). Observed identity: [`liberusoftware/module-crm-events-and-webinars-filament`](../../../modules/source/liberusoftware--module-crm-events-and-webinars-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-events-and-webinars-filament`  
**Matching domain module:** `crm-events-and-webinars`  
**Application:** CRM  
**Source feature:** [Crm Events And Webinars](../features/crm-events-and-webinars.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-events-and-webinars` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Physical/virtual events:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Registration:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Capacity:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tickets/attendance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sessions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Speakers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reminders:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Check-in:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recording links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Follow-up:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Provider adapters:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-events-and-webinars-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `physical-virtual-events`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `registration`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `capacity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tickets-attendance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sessions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `speakers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reminders`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `check-in`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recording-links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `follow-up`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `provider-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-events-and-webinars` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-events-and-webinars-filament`](https://github.com/liberusoftware/module-crm-events-and-webinars-filament) (`liberusoftware/crm-events-and-webinars-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-events-and-webinars.md) · [API plan](../api/crm-events-and-webinars.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Physical/virtual events** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `physical/virtual events`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Registration** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `registration`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Capacity** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `capacity`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tickets/attendance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tickets/attendance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sessions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sessions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Speakers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `speakers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reminders** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reminders`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Check-in** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `check-in`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recording links** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recording links`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Follow-up** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `follow-up`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Provider adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provider adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [EventsAndWebinarsFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars-filament/src/EventsAndWebinarsFilamentServiceProvider.php) · [CrmEventResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars-filament/src/Resources/CrmEventResource.php) · [CreateCrmEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars-filament/src/Resources/Pages/CreateCrmEvent.php) · [EditCrmEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars-filament/src/Resources/Pages/EditCrmEvent.php) · [ListCrmEvents.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars-filament/src/Resources/Pages/ListCrmEvents.php).

| Observed core query | Public method signatures |
| --- | --- |
| [EventQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Queries/EventQuery.php) | `public function events(int $teamId)`<br>`public function sessions(int $teamId, int $eventId)`<br>`public function attendance(int $teamId, int $eventId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CheckInAttendee.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Actions/CheckInAttendee.php) | `public function execute(int $teamId, EventRegistration $registration): EventRegistration` |
| [CreateEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Actions/CreateEvent.php) | `public function __construct(private readonly EventPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CrmEvent` |
| [RecordEventFollowUp.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Actions/RecordEventFollowUp.php) | `public function __construct(private readonly EventPolicy $policy)`<br>`public function execute(int $teamId, int $userId, CrmEvent $event, array $input): EventFollowUp` |
| [RegisterAttendee.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Actions/RegisterAttendee.php) | `public function execute(int $teamId, CrmEvent $event, array $input): EventRegistration` |
| [EventPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Services/EventPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CrmEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Models/CrmEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [EventFollowUp.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Models/EventFollowUp.php) | No literal fillable array detected; inspect the model and API schema. |
| [EventRegistration.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Models/EventRegistration.php) | No literal fillable array detected; inspect the model and API schema. |
| [EventSession.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Models/EventSession.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
