# CMS: Cms Content Calendar Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-content-calendar). Observed identity: [`liberusoftware/module-cms-content-calendar-filament`](../../../modules/source/liberusoftware--module-cms-content-calendar-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-cms-content-calendar-filament`  
**Matching domain module:** `cms-content-calendar`  
**Application:** CMS  
**Source feature:** [Cms Content Calendar](../features/cms-content-calendar.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-content-calendar` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Editorial calendar:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Campaigns:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Deadlines:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Assignments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Conflicts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Drag/drop rescheduling:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Channel/site filters:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-cms-content-calendar-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `editorial-calendar`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `campaigns`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `deadlines`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `assignments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `conflicts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `drag-drop-rescheduling`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `channel-site-filters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-content-calendar` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-content-calendar-filament`](https://github.com/liberusoftware/module-cms-content-calendar-filament) (`liberusoftware/cms-content-calendar-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-content-calendar.md) · [API plan](../api/cms-content-calendar.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Editorial calendar** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `editorial calendar`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Campaigns** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `campaigns`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Deadlines** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `deadlines`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Assignments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `assignments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Conflicts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `conflicts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Drag/drop rescheduling** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `drag/drop rescheduling`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Channel/site filters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `channel/site filters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ContentCalendarFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-calendar-filament/src/ContentCalendarFilamentServiceProvider.php) · [CalendarItemResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-calendar-filament/src/Resources/CalendarItemResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ContentCalendarService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-calendar/src/Services/ContentCalendarService.php) | `public function items(?int $teamId, ?string $channel = null, ?string $site = null, int $perPage = 25): LengthAwarePaginator`<br>`public function campaign(array $data, ?int $teamId = null): CalendarCampaign`<br>`public function schedule(array $data, ?int $teamId = null): CalendarItem`<br>`public function reschedule(CalendarItem $item, string $startsAt, ?string $deadlineAt = null): CalendarItem` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CalendarCampaign.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-calendar/src/Models/CalendarCampaign.php) | `team_id`, `name`, `slug`, `description`, `status` |
| [CalendarItem.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-calendar/src/Models/CalendarItem.php) | `team_id`, `campaign_id`, `title`, `content_type`, `subject_key`, `channel`, `site`, `status`, `starts_at`, `deadline_at`, `assigned_to` |
<!-- layer-implementation-plan:end -->
