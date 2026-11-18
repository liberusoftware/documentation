# Timeline React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#timeline). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-genealogy-timeline-react-native
**Matching core package:** module-genealogy-timeline ([implementation](../core/timeline.md))
**Matching API package:** module-genealogy-timeline-api ([contract](../api/timeline.md))

## Implementation plan

This adapter presents Timeline for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Timeline API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/timeline.md), and [API module](../api/timeline.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `timeline`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-genealogy-mobile-react`](https://github.com/liberusoftware/project-genealogy-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/timeline.md)) |
| Capability React Native module skeleton | [`module-genealogy-timeline-react-native`](https://github.com/liberusoftware/module-genealogy-timeline-react-native) (`@liberusoftware/module-genealogy-timeline-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Personal/family timelines** | Progressive mobile list/detail/sheet flow for `personal/family timelines` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Historical context** | Progressive mobile list/detail/sheet flow for `historical context` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Conflicts** | Progressive mobile list/detail/sheet flow for `conflicts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Chronological navigation** | Progressive mobile list/detail/sheet flow for `chronological navigation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-genealogy-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

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
