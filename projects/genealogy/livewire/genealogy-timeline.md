# Genealogy: Genealogy Timeline Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-timeline). Observed identity: [`liberusoftware/module-genealogy-timeline-livewire`](../../../modules/source/liberusoftware--module-genealogy-timeline-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-genealogy-genealogy-timeline-livewire`  
**Matching domain module:** `genealogy-timeline`  
**Application:** Genealogy  
**Source feature:** [Genealogy Timeline](../features/genealogy-timeline.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Personal/family timelines:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Historical context:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Conflicts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Chronological navigation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-genealogy-genealogy-timeline-livewire` component namespace and service provider; use explicit aliases such as `<livewire:genealogyGenealogyTimeline::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `personal-family-timelines`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `historical-context`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `conflicts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `chronological-navigation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `genealogy-timeline` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/genealogy-timeline.md) · [API plan](../api/genealogy-timeline.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Personal/family timelines** | Expose a focused Livewire 4 component and namespaced Blade default view for `personal/family timelines` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Historical context** | Expose a focused Livewire 4 component and namespaced Blade default view for `historical context` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Conflicts** | Expose a focused Livewire 4 component and namespaced Blade default view for `conflicts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Chronological navigation** | Expose a focused Livewire 4 component and namespaced Blade default view for `chronological navigation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [TimelineLivewireServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline-livewire/src/TimelineLivewireServiceProvider.php).

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
