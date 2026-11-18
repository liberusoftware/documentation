# Social Network: Events Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#events). Observed identity: [`liberusoftware/module-social-network-events-filament`](../../../modules/source/liberusoftware--module-social-network-events-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-social-network-events-filament`  
**Matching domain module:** `social-network-events`  
**Application:** Social Network  
**Source feature:** [Events](../features/events.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `social-network-events` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Events:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Invitations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Attendance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Capacity:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Schedules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Locations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reminders:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Updates:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-social-network-events-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `events`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `invitations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `attendance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `capacity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `schedules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `locations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reminders`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `updates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `social-network-events` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-social-network-events-filament`](https://github.com/liberusoftware/module-social-network-events-filament) (`liberusoftware/social-network-events-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/events.md) · [API plan](../api/events.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Events** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `events`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Invitations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `invitations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Attendance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `attendance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Capacity** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `capacity`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Schedules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `schedules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Locations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `locations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reminders** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reminders`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Updates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `updates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [EventsFilamentPlugin.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events-filament/src/EventsFilamentPlugin.php) · [EventsFilamentServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events-filament/src/EventsFilamentServiceProvider.php) · [Events.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events-filament/src/Pages/Events.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddEventUpdate.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/AddEventUpdate.php) | `public function __construct( private EventsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(Profile $owner, Event $event, string $body): EventUpdate` |
| [CreateEvent.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/CreateEvent.php) | `public function __construct( private EventsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(Profile $owner, array $data): Event` |
| [InviteProfile.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/InviteProfile.php) | `public function __construct(private EventsAuthorizer $authorizer)`<br>`public function handle(Profile $owner, Event $event, Profile $invitee): Invitation` |
| [ListEvents.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/ListEvents.php) | `public function handle(Profile $viewer, int $limit = 25): Collection` |
| [PublishEvent.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/PublishEvent.php) | `public function __construct( private EventsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(Profile $owner, Event $event): Event` |
| [ScheduleReminder.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/ScheduleReminder.php) | `public function __construct(private EventsAuthorizer $authorizer)`<br>`public function handle(Profile $profile, Event $event, string $sendAt): EventReminder` |
| [SetAttendance.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/SetAttendance.php) | `public function __construct(private EventsAuthorizer $authorizer)`<br>`public function handle(Profile $profile, Event $event, string $state): void` |
| [UpdateEvent.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/UpdateEvent.php) | `public function __construct( private EventsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(Profile $owner, Event $event, array $data): Event` |
| [EventsAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Contracts/EventsAuthorizer.php) | `public function create(Profile $owner): void`<br>`public function manage(Profile $owner, Event $event): void`<br>`public function attend(Profile $profile, Event $event): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Event.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Models/Event.php) | `id`, `owner_profile_id`, `state`, `visibility`, `timezone`, `title`, `description`, `starts_at`, `ends_at`, `capacity`, `location`, `metadata` |
| [EventReminder.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Models/EventReminder.php) | `event_id`, `profile_id`, `send_at`, `sent_at` |
| [EventUpdate.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Models/EventUpdate.php) | `event_id`, `author_profile_id`, `body` |
| [Invitation.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Models/Invitation.php) | `event_id`, `profile_id`, `state` |
<!-- layer-implementation-plan:end -->
