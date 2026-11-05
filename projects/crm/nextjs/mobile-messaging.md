# Mobile Messaging: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-crm-mobile-messaging`.

**Proposed design identifier:** `module-crm-mobile-messaging-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/mobile-messaging.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-crm-mobile-messaging](../../../modules/source/liberusoftware--module-crm-mobile-messaging.md) |
| API | [liberusoftware/module-crm-mobile-messaging-api](../../../modules/source/liberusoftware--module-crm-mobile-messaging-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Consent-aware SMS/MMS/WhatsApp/push campaigns | A focused authorized view or workflow section for consent-aware sms/mms/whatsapp/push campaigns; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Templates | A focused authorized view or workflow section for templates; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Short links | A focused authorized view or workflow section for short links; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Keywords | A focused authorized view or workflow section for keywords; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Opt-in/out | A focused authorized view or workflow section for opt-in/out; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Quiet hours | A focused authorized view or workflow section for quiet hours; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Sender governance | A focused authorized view or workflow section for sender governance; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Delivery/reply handling | A focused authorized view or workflow section for delivery/reply handling; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [CampaignQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Queries/CampaignQuery.php) | `public function forTeam(int $teamId)` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CreateCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Actions/CreateCampaign.php) | `public function execute(int $teamId, int $userId, array $input): MessagingCampaign` |
| [RecordMessage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Actions/RecordMessage.php) | `public function execute(int $teamId, int $userId, MessagingCampaign $campaign, array $input): MessagingMessage` |
| [UpsertContactConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Actions/UpsertContactConsent.php) | `public function execute(int $teamId, int $userId, array $input): MessagingContact` |
| [MobileMessagingPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Services/MobileMessagingPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [MessagingCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Models/MessagingCampaign.php) | No literal fillable array detected; inspect the model and API schema. |
| [MessagingContact.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Models/MessagingContact.php) | No literal fillable array detected; inspect the model and API schema. |
| [MessagingMessage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Models/MessagingMessage.php) | No literal fillable array detected; inspect the model and API schema. |
| [MessagingTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Models/MessagingTemplate.php) | No literal fillable array detected; inspect the model and API schema. |

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
