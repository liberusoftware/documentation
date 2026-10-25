# Mail: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-control-panel-mail`.

**Proposed design identifier:** `module-control-panel-mail-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/mail.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-control-panel-mail](../../../modules/source/liberusoftware--module-control-panel-mail.md) |
| API | [liberusoftware/module-control-panel-mail-api](../../../modules/source/liberusoftware--module-control-panel-mail-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Domains | A focused authorized view or workflow section for domains; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Mailboxes | A focused authorized view or workflow section for mailboxes; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Aliases | A focused authorized view or workflow section for aliases; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Routing | A focused authorized view or workflow section for routing; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Quotas | A focused authorized view or workflow section for quotas; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Spam/virus controls | A focused authorized view or workflow section for spam/virus controls; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| DKIM | A focused authorized view or workflow section for dkim; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Delivery diagnostics | A focused authorized view or workflow section for delivery diagnostics; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ListMailAccounts.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Queries/ListMailAccounts.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [ConfigureMailAuthentication.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/ConfigureMailAuthentication.php) | `public function execute(MailDomain $domain, array $attributes = []): MailDomain` |
| [ConfigureMailControls.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/ConfigureMailControls.php) | `public function execute(array $a): MailControl` |
| [CreateMailAccount.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/CreateMailAccount.php) | `public function execute(array $attributes): MailAccount` |
| [CreateMailAlias.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/CreateMailAlias.php) | `public function execute(array $a): MailAlias` |
| [CreateMailRoute.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/CreateMailRoute.php) | `public function execute(array $attributes): MailRoute` |
| [DeleteMailAccount.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/DeleteMailAccount.php) | `public function execute(MailAccount $account): void` |
| [DeleteMailAlias.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/DeleteMailAlias.php) | `public function execute(MailAlias $alias): void` |
| [DeleteMailRoute.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/DeleteMailRoute.php) | `public function execute(MailRoute $route): void` |
| [RecordDeliveryDiagnostic.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/RecordDeliveryDiagnostic.php) | `public function execute(array $a): DeliveryDiagnostic` |
| [RecordMailOperation.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/RecordMailOperation.php) | `public function execute(array $a): MailOperation` |
| [RegisterMailDomain.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/RegisterMailDomain.php) | `public function execute(array $attributes): MailDomain` |
| [RotateDkimKey.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/RotateDkimKey.php) | `public function execute(string $teamId, string $domain, string $selector = 'default'): DkimKey` |
| [UpdateMailAccount.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/UpdateMailAccount.php) | `public function execute(MailAccount $account, array $attributes): MailAccount` |
| [UpdateMailAlias.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/UpdateMailAlias.php) | `public function execute(MailAlias $alias, array $attributes): MailAlias` |
| [UpdateMailRoute.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/UpdateMailRoute.php) | `public function execute(MailRoute $route, array $attributes): MailRoute` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [DeliveryDiagnostic.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/DeliveryDiagnostic.php) | `id`, `team_id`, `mail_account_id`, `message_id`, `recipient`, `status`, `response`, `checked_at` |
| [DkimKey.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/DkimKey.php) | `id`, `team_id`, `domain`, `selector`, `public_key`, `private_key`, `active`, `rotated_at` |
| [MailAccount.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailAccount.php) | `team_id`, `domain`, `address`, `status`, `quota_bytes`, `settings` |
| [MailAlias.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailAlias.php) | `id`, `team_id`, `domain`, `address`, `destinations`, `active` |
| [MailControl.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailControl.php) | `id`, `team_id`, `mail_account_id`, `spam_filter_enabled`, `spam_threshold`, `spam_action`, `virus_scan_enabled`, `autoresponder_enabled`, `autoresponder_subject`, `autoresponder_message`, `autoresponder_start_at`, `autoresponder_end_at`, `keep_copy_on_server` |
| [MailDomain.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailDomain.php) | `id`, `team_id`, `domain`, `status`, `dkim`, `spf`, `dmarc` |
| [MailOperation.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailOperation.php) | `id`, `team_id`, `mail_account_id`, `operation`, `status`, `details` |
| [MailRoute.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailRoute.php) | `id`, `team_id`, `domain`, `source_pattern`, `destination`, `priority`, `active` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/control-panel-mail-api/routes/api.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/mail')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [MailAccountController::class, 'index'])->name('control-panel.mail.index');
Route::post('/', [MailAccountController::class, 'store'])->name('control-panel.mail.store');
Route::post('/operations', [MailAccountController::class, 'operation'])->name('control-panel.mail.operations.store');
Route::post('/aliases', [MailAccountController::class, 'alias'])->name('control-panel.mail.aliases.store');
Route::patch('/aliases/{alias}', [MailAccountController::class, 'updateAlias'])->name('control-panel.mail.aliases.update');
Route::delete('/aliases/{alias}', [MailAccountController::class, 'deleteAlias'])->name('control-panel.mail.aliases.delete');
Route::post('/routes', [MailAccountController::class, 'route'])->name('control-panel.mail.routes.store');
Route::patch('/routes/{route}', [MailAccountController::class, 'updateRoute'])->name('control-panel.mail.routes.update');
Route::delete('/routes/{route}', [MailAccountController::class, 'deleteRoute'])->name('control-panel.mail.routes.delete');
Route::post('/controls', [MailAccountController::class, 'controls'])->name('control-panel.mail.controls.store');
Route::post('/delivery-diagnostics', [MailAccountController::class, 'diagnostic'])->name('control-panel.mail.delivery-diagnostics.store');
Route::post('/dkim/rotate', [MailAccountController::class, 'rotateDkim'])->name('control-panel.mail.dkim.rotate');
Route::post('/authentication/configure', [MailAccountController::class, 'authentication'])->name('control-panel.mail.authentication.configure');
Route::post('/domains', [MailAccountController::class, 'domain'])->name('control-panel.mail.domains.store');
Route::patch('/{mailAccount}', [MailAccountController::class, 'update'])->name('control-panel.mail.update');
Route::delete('/{mailAccount}', [MailAccountController::class, 'delete'])->name('control-panel.mail.delete');
Route::get('/{mailAccount}', [MailAccountController::class, 'show'])->name('control-panel.mail.show');
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
