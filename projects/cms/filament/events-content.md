# CMS: Events Content Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#events-content). Observed identity: [`liberusoftware/module-cms-events-content-filament`](../../../modules/source/liberusoftware--module-cms-events-content-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-events-content-filament`  
**Matching domain module:** `cms-events-content`  
**Application:** CMS  
**Source feature:** [Events Content](../features/events-content.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-events-content` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Event/session/speaker/venue content:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Calendars:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Registration-provider references:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Archives:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Structured data:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-events-content-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `event-session-speaker-venue-content`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `calendars`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `registration-provider-references`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `archives`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `structured-data`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-events-content` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-events-content-filament`](https://github.com/liberusoftware/module-cms-events-content-filament) (`liberusoftware/cms-events-content-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/events-content.md) · [API plan](../api/events-content.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Event/session/speaker/venue content** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `event/session/speaker/venue content`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Calendars** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `calendars`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Registration-provider references** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `registration-provider references`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Archives** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `archives`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Structured data** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `structured data`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [EventsContentFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-events-content-filament/src/EventsContentFilamentServiceProvider.php) · [EventResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-events-content-filament/src/Resources/EventResource.php) · [ListEvents.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-events-content-filament/src/Resources/Pages/ListEvents.php).

| Observed core query | Public method signatures |
| --- | --- |
| [EventsContentQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-events-content/src/Queries/EventsContentQuery.php) | `public function calendar(int $perPage = 15, string $search = '', bool $includeArchived = false): LengthAwarePaginator`<br>`public function find(string $key): ?Event` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [EventsContentService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-events-content/src/Services/EventsContentService.php) | `public function speaker(array $attributes, ?int $teamId = null): Speaker`<br>`public function venue(array $attributes, ?int $teamId = null): Venue`<br>`public function event(array $attributes, ?int $teamId = null): Event`<br>`public function session(Event $event, array $attributes): Session`<br>`public function registration(Event $event, array $attributes): RegistrationReference`<br>`public function publish(Event $event): Event`<br>`public function archive(Event $event): Event`<br>`public function structuredData(Event $event): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Event.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-events-content/src/Models/Event.php) | `key`, `title`, `description`, `status`, `timezone`, `starts_at`, `ends_at`, `archived_at`, `structured_data`, `venue_id`, `team_id` |
| [RegistrationReference.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-events-content/src/Models/RegistrationReference.php) | `event_id`, `provider`, `external_key`, `url`, `status`, `metadata` |
| [Session.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-events-content/src/Models/Session.php) | `event_id`, `key`, `title`, `description`, `starts_at`, `ends_at`, `room` |
| [Speaker.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-events-content/src/Models/Speaker.php) | `name`, `bio`, `email`, `metadata`, `team_id` |
| [Venue.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-events-content/src/Models/Venue.php) | `name`, `address`, `timezone`, `latitude`, `longitude`, `team_id` |
<!-- layer-implementation-plan:end -->
