# CRM: Crm Scheduling Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-scheduling). Observed identity: [`liberusoftware/module-crm-scheduling-filament`](../../../modules/source/liberusoftware--module-crm-scheduling-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-scheduling-filament`  
**Matching domain module:** `crm-scheduling`  
**Application:** CRM  
**Source feature:** [Crm Scheduling](../features/crm-scheduling.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-scheduling` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Personal/team/round-robin links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Availability:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Buffers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Minimum notice:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Questions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reminders:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reschedule/cancel:** resource/table/form/action or page behavior for this module's authorized workflow.
- **No-show:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Routing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Calendar adapters:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-scheduling-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `personal-team-round-robin-links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `availability`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `buffers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `minimum-notice`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `questions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reminders`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reschedule-cancel`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `no-show`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `routing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `calendar-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-scheduling` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-scheduling-filament`](https://github.com/liberusoftware/module-crm-scheduling-filament) (`liberusoftware/crm-scheduling-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-scheduling.md) · [API plan](../api/crm-scheduling.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Personal/team/round-robin links** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `personal/team/round-robin links`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Availability** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `availability`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Buffers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `buffers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Minimum notice** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `minimum notice`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Questions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `questions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reminders** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reminders`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reschedule/cancel** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reschedule/cancel`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **No-show** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `no-show`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Routing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `routing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Calendar adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `calendar adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [BookingResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling-filament/src/Resources/BookingResource.php) · [ListBookings.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling-filament/src/Resources/BookingResource/Pages/ListBookings.php) · [SchedulingFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling-filament/src/SchedulingFilamentPlugin.php) · [SchedulingFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling-filament/src/SchedulingFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [SchedulingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Queries/SchedulingQuery.php) | `public function links(int $teamId)`<br>`public function bookings(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ChangeBookingStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Actions/ChangeBookingStatus.php) | `public function execute(int $teamId, int $actorId, int $bookingId, string $status, array $data = []): Booking` |
| [CreateBooking.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Actions/CreateBooking.php) | `public function execute(int $teamId, int $actorId, array $data): Booking` |
| [CreateSchedulingLink.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Actions/CreateSchedulingLink.php) | `public function execute(int $teamId, int $actorId, array $data): SchedulingLink` |
| [SchedulingAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Services/SchedulingAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): Audit` |
| [SchedulingPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Services/SchedulingPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Booking.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Models/Booking.php) | No literal fillable array detected; inspect the model and API schema. |
| [SchedulingAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Models/SchedulingAudit.php) | No literal fillable array detected; inspect the model and API schema. |
| [SchedulingLink.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Models/SchedulingLink.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
