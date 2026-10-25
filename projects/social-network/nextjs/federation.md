# Federation: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-social-network-federation`.

**Proposed design identifier:** `module-social-network-federation-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/federation.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-social-network-federation](../../../modules/source/liberusoftware--module-social-network-federation.md) |
| API | [liberusoftware/module-social-network-federation-api](../../../modules/source/liberusoftware--module-social-network-federation-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| ActivityPub identities | A focused authorized view or workflow section for activitypub identities; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Inbox/outbox | A focused authorized view or workflow section for inbox/outbox; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Signatures | A focused authorized view or workflow section for signatures; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Delivery | A focused authorized view or workflow section for delivery; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Mapping | A focused authorized view or workflow section for mapping; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Moderation | A focused authorized view or workflow section for moderation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Reconciliation | A focused authorized view or workflow section for reconciliation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [PublishActivity.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation/src/Actions/PublishActivity.php) | `public function handle(string $type, array $payload): FederationMessage` |
| [QueueDelivery.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation/src/Actions/QueueDelivery.php) | `public function handle(FederationMessage $message, string $inboxUrl): FederationDelivery` |
| [ReceiveActivity.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation/src/Actions/ReceiveActivity.php) | `public function handle(array $payload, ?string $signature = null): FederationMessage` |
| [ReconcileMapping.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation/src/Actions/ReconcileMapping.php) | `public function handle(string $remoteType, string $remoteId, string $localType, string $localId, array $metadata = []): FederationMapping` |
| [RegisterActor.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation/src/Actions/RegisterActor.php) | `public function handle(Profile $profile, array $data): FederationActor` |
| [VerifyActivitySignature.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation/src/Actions/VerifyActivitySignature.php) | `public function handle(string $payload, string $signature, string $publicKey): bool` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [FederationActor.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation/src/Models/FederationActor.php) | No literal fillable array detected; inspect the model and API schema. |
| [FederationDelivery.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation/src/Models/FederationDelivery.php) | No literal fillable array detected; inspect the model and API schema. |
| [FederationMapping.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation/src/Models/FederationMapping.php) | No literal fillable array detected; inspect the model and API schema. |
| [FederationMessage.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation/src/Models/FederationMessage.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/social-network-federation-api/routes/api.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/federation')->middleware('api')->group(function (): void {
Route::post('/inbox', [FederationController::class, 'inbox'])->name('social-network.federation.inbox');
Route::get('/outbox', [FederationController::class, 'outbox'])->name('social-network.federation.outbox');
Route::middleware(['auth:sanctum', 'throttle:60,1'])->post('/actors', [FederationController::class, 'actor'])->name('social-network.federation.actors');
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
