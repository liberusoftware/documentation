# Backup and Restore: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-cms-backup-and-restore`.

**Proposed design identifier:** `module-cms-backup-and-restore-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/backup-and-restore.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **3 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-cms-backup-and-restore](../../../modules/source/liberusoftware--module-cms-backup-and-restore.md) |
| API | [liberusoftware/module-cms-backup-and-restore-api](../../../modules/source/liberusoftware--module-cms-backup-and-restore-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Content/configuration/database/file backup contracts | A focused authorized view or workflow section for content/configuration/database/file backup contracts; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Schedules | A focused authorized view or workflow section for schedules; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Encryption | A focused authorized view or workflow section for encryption; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Retention | A focused authorized view or workflow section for retention; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Verification | A focused authorized view or workflow section for verification; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Restore preview | A focused authorized view or workflow section for restore preview; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Evidence | A focused authorized view or workflow section for evidence; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [BackupAndRestoreService.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-backup-and-restore/src/Services/BackupAndRestoreService.php) | `public function createArtifact(?int $teamId, array $data): BackupArtifact`<br>`public function verify(BackupArtifact $artifact): BackupArtifact`<br>`public function restorePreview(BackupArtifact $artifact): array`<br>`public function schedule(?int $teamId, array $data): BackupSchedule` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [BackupArtifact.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-backup-and-restore/src/Models/BackupArtifact.php) | `team_id`, `name`, `artifact_type`, `status`, `disk`, `path`, `size`, `checksum`, `encrypted`, `metadata`, `verified_at`, `expires_at` |
| [BackupSchedule.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-backup-and-restore/src/Models/BackupSchedule.php) | `team_id`, `name`, `frequency`, `artifact_types`, `retention_days`, `enabled`, `next_run_at`, `last_run_at` |

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
