# Genealogy: Timeline Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#timeline). Observed identity: [`liberusoftware/module-genealogy-timeline-filament`](../../../modules/source/liberusoftware--module-genealogy-timeline-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-genealogy-timeline-filament`  
**Matching domain module:** `genealogy-timeline`  
**Application:** Genealogy  
**Source feature:** [Timeline](../features/timeline.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `genealogy-timeline` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Personal/family timelines:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Historical context:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Conflicts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Chronological navigation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-genealogy-timeline-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `personal-family-timelines`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `historical-context`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `conflicts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `chronological-navigation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `genealogy-timeline` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-genealogy-timeline-filament`](https://github.com/liberusoftware/module-genealogy-timeline-filament) (`liberusoftware/genealogy-timeline-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/timeline.md) · [API plan](../api/timeline.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Personal/family timelines** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `personal/family timelines`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Historical context** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `historical context`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Conflicts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `conflicts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Chronological navigation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `chronological navigation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [TimelineEventResource.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline-filament/src/Resources/TimelineEventResource.php) · [CreateTimelineEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline-filament/src/Resources/TimelineEventResource/Pages/CreateTimelineEvent.php) · [EditTimelineEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline-filament/src/Resources/TimelineEventResource/Pages/EditTimelineEvent.php) · [ListTimelineEvents.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline-filament/src/Resources/TimelineEventResource/Pages/ListTimelineEvents.php) · [TimelineFilamentServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline-filament/src/TimelineFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ChronologicalTimeline.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline/src/Queries/ChronologicalTimeline.php) | `public function execute(?string $subjectPersonId = null, ?string $familyKey = null, ?string $from = null, ?string $to = null, bool $includePrivate = false): array` |
| [ConflictingTimelineEvents.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline/src/Queries/ConflictingTimelineEvents.php) | `public function execute(?string $subjectPersonId = null, bool $includePrivate = false): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateTimelineEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline/src/Actions/CreateTimelineEvent.php) | `public function __construct(private readonly ?PersonReferenceResolver $personReference = null)`<br>`public function execute(array $attributes): TimelineEvent`<br>`public function validate(array $values): void` |
| [DeleteTimelineEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline/src/Actions/DeleteTimelineEvent.php) | `public function execute(TimelineEvent $event): void` |
| [UpdateTimelineEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline/src/Actions/UpdateTimelineEvent.php) | `public function __construct(private readonly ?PersonReferenceResolver $personReference = null)`<br>`public function execute(TimelineEvent $event, array $attributes): TimelineEvent` |
| [HistoricalEventService.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline/src/Services/HistoricalEventService.php) | `public function fetchForPeriod(string\|\DateTimeInterface $start, string\|\DateTimeInterface $end, ?string $country = null): Collection`<br>`public function fetchForPerson(Model $person, int $bufferYears = 5): Collection` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [HistoricalEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline/src/Models/HistoricalEvent.php) | `title`, `description`, `event_date`, `year`, `month`, `day`, `place`, `country`, `latitude`, `longitude`, `source_url` |
| [TimelineEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline/src/Models/TimelineEvent.php) | `team_id`, `kind`, `name`, `subject_person_id`, `family_key`, `event_date`, `date_start`, `date_end`, `date_precision`, `place_id`, `description`, `historical_context`, `conflict_group`, `confidence`, `source_reference`, `is_private`, `status`, `metadata` |
<!-- layer-implementation-plan:end -->
