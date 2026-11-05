# Events: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-social-network-events`.

**Proposed design identifier:** `module-social-network-events-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/events.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-social-network-events](../../../modules/source/liberusoftware--module-social-network-events.md) |
| API | [liberusoftware/module-social-network-events-api](../../../modules/source/liberusoftware--module-social-network-events-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Events | A focused authorized view or workflow section for events; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Invitations | A focused authorized view or workflow section for invitations; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Attendance | A focused authorized view or workflow section for attendance; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Capacity | A focused authorized view or workflow section for capacity; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Schedules | A focused authorized view or workflow section for schedules; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Locations | A focused authorized view or workflow section for locations; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Reminders | A focused authorized view or workflow section for reminders; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Updates | A focused authorized view or workflow section for updates; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [AddEventUpdate.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/AddEventUpdate.php) | `public function handle(Profile $owner, Event $event, string $body): EventUpdate` |
| [CreateEvent.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/CreateEvent.php) | `public function handle(Profile $owner, array $data): Event` |
| [InviteProfile.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/InviteProfile.php) | `public function handle(Profile $owner, Event $event, Profile $invitee): Invitation` |
| [ListEvents.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/ListEvents.php) | `public function handle(Profile $viewer, int $limit = 25): Collection` |
| [PublishEvent.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/PublishEvent.php) | `public function handle(Profile $owner, Event $event): Event` |
| [ScheduleReminder.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/ScheduleReminder.php) | `public function handle(Profile $profile, Event $event, string $sendAt): EventReminder` |
| [SetAttendance.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/SetAttendance.php) | `public function handle(Profile $profile, Event $event, string $state): void` |
| [UpdateEvent.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/UpdateEvent.php) | `public function handle(Profile $owner, Event $event, array $data): Event` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [Event.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Models/Event.php) | `id`, `owner_profile_id`, `state`, `visibility`, `timezone`, `title`, `description`, `starts_at`, `ends_at`, `capacity`, `location`, `metadata` |
| [EventReminder.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Models/EventReminder.php) | `event_id`, `profile_id`, `send_at`, `sent_at` |
| [EventUpdate.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Models/EventUpdate.php) | `event_id`, `author_profile_id`, `body` |
| [Invitation.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Models/Invitation.php) | `event_id`, `profile_id`, `state` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/social-network-events-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/events')
Route::get('/', [EventsController::class, 'index'])->name('index');
Route::post('/', [EventsController::class, 'store'])->name('store');
Route::patch('/{event}', [EventsController::class, 'update'])->name('update');
Route::post('/{event}/publish', [EventsController::class, 'publish'])->name('publish');
Route::post('/{event}/invitations', [EventsController::class, 'invite'])->name('invite');
Route::post('/{event}/attendance', [EventsController::class, 'attendance'])->name('attendance');
Route::post('/{event}/updates', [EventsController::class, 'updateLog'])->name('updates.store');
Route::post('/{event}/reminders', [EventsController::class, 'reminder'])->name('reminders.store');
```

## Server/client and React reuse

Keep API credentials and session forwarding in server-only exports. A Server Component may load authorized serializable data and compose a Client Component for interaction. Put ordinary event callbacks inside the client boundary; server-to-client props must follow the framework serialization/action rules.

Share framework-independent React cards, tables, labels, formatting and field primitives with Inertia. Keep `next/link`, Next.js navigation, server actions and cache invalidation in this adapter, and Inertia visits, page props and redirects in its wrapper. Reuse domain/API DTOs without importing PHP models or another application's private frontend state.

## State, failures and verification

| Situation | User-facing behavior and integration requirement |
| --- | --- |
| Loading or empty authorized query | Accessible progress/empty copy; preserve filters and avoid displaying stale records from another scope |
| Expired session or denied permission | Reauthenticate or show a scoped denial; discard protected cached data and do not retry as a broader service identity |
| Invalid command input | Preserve safe draft values, announce field errors and use the authoritative API validation outcome |
| Stale record / concurrent change | Reload/review the current version; do not overwrite silently or invent an ETag contract the API does not support |
| Timeout after a write | Query the operation/current record when supported before retrying; an idempotency key works only if the owning API actually stores/enforces it |
| Long-running or partly failed operation | Show a durable operation reference, progress, last error and a permitted retry/recovery action |

Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware caching policy exists. Refresh affected read models after confirmed mutations; pending transport acceptance is not a completed business transition. Recheck access for evidence/export downloads.

Verify the actual supported query/command journeys, invalid and denied paths, tenant switching, stale state, retry recovery, keyboard/focus behavior and secret exclusion from browser bundles. Build/test the packed adapter in a clean consuming Next.js application using its declared versions and API contract. No npm package or application suite was executed by this plan generator.

See the [Next.js standard](../../../standards/NEXTJS.md), [npm lifecycle guide](../../../guides/NPM.md), [API architecture](../../../architecture/API.md), and [shared ownership guide](../../../architecture/SHARED-MODULES.md).
