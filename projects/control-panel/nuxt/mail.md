# Control Panel: Mail Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#mail). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-control-panel-mail-nuxt`
**Matching domain module:** `control-panel-mail`
**Application:** Control Panel
**Source feature:** [Mail](../features/mail.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/mail.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `control-panel-mail` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Domains:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Mailboxes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Aliases:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Routing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Quotas:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Spam/virus controls:** page/component/composable/API-action behavior for this module's authorized workflow.
- **DKIM:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Delivery diagnostics:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-control-panel-mail-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `domains`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `mailboxes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `aliases`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `routing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `quotas`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `spam-virus-controls`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dkim`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `delivery-diagnostics`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `control-panel-mail` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-control-panel-nuxt-vue`](https://github.com/liberusoftware/project-control-panel-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/mail.md)) |
| Capability Nuxt module skeleton | [`module-control-panel-mail-nuxt`](https://github.com/liberusoftware/module-control-panel-mail-nuxt) (`@liberusoftware/module-control-panel-mail-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Domains** | Expose composable and Vue 3 component for `domains` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mail.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Mailboxes** | Expose composable and Vue 3 component for `mailboxes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mail.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Aliases** | Expose composable and Vue 3 component for `aliases` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mail.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Routing** | Expose composable and Vue 3 component for `routing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mail.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Quotas** | Expose composable and Vue 3 component for `quotas` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mail.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Spam/virus controls** | Expose composable and Vue 3 component for `spam/virus controls` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mail.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **DKIM** | Expose composable and Vue 3 component for `dkim` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mail.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Delivery diagnostics** | Expose composable and Vue 3 component for `delivery diagnostics` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mail.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListMailAccounts.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Queries/ListMailAccounts.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfigureMailAuthentication.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/ConfigureMailAuthentication.php) | `public function __construct(private readonly RotateDkimKey $rotateDkimKey)`<br>`public function execute(MailDomain $domain, array $attributes = []): MailDomain` |
| [ConfigureMailControls.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/ConfigureMailControls.php) | `public function execute(array $a): MailControl` |
| [CreateMailAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/CreateMailAccount.php) | `public function execute(array $attributes): MailAccount` |
| [CreateMailAlias.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/CreateMailAlias.php) | `public function execute(array $a): MailAlias` |
| [CreateMailRoute.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/CreateMailRoute.php) | `public function execute(array $attributes): MailRoute` |
| [DeleteMailAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/DeleteMailAccount.php) | `public function execute(MailAccount $account): void` |
| [DeleteMailAlias.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/DeleteMailAlias.php) | `public function execute(MailAlias $alias): void` |
| [DeleteMailRoute.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/DeleteMailRoute.php) | `public function execute(MailRoute $route): void` |
| [RecordDeliveryDiagnostic.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/RecordDeliveryDiagnostic.php) | `public function execute(array $a): DeliveryDiagnostic` |
| [RecordMailOperation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Actions/RecordMailOperation.php) | `public function execute(array $a): MailOperation` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DeliveryDiagnostic.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/DeliveryDiagnostic.php) | `id`, `team_id`, `mail_account_id`, `message_id`, `recipient`, `status`, `response`, `checked_at` |
| [DkimKey.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/DkimKey.php) | `id`, `team_id`, `domain`, `selector`, `public_key`, `private_key`, `active`, `rotated_at` |
| [MailAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailAccount.php) | `team_id`, `domain`, `address`, `status`, `quota_bytes`, `settings` |
| [MailAlias.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailAlias.php) | `id`, `team_id`, `domain`, `address`, `destinations`, `active` |
| [MailControl.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailControl.php) | `id`, `team_id`, `mail_account_id`, `spam_filter_enabled`, `spam_threshold`, `spam_action`, `virus_scan_enabled`, `autoresponder_enabled`, `autoresponder_subject`, `autoresponder_message`, `autoresponder_start_at`, `autoresponder_end_at`, `keep_copy_on_server` |
| [MailDomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailDomain.php) | `id`, `team_id`, `domain`, `status`, `dkim`, `spf`, `dmarc` |
| [MailOperation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailOperation.php) | `id`, `team_id`, `mail_account_id`, `operation`, `status`, `details` |
| [MailRoute.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail/src/Models/MailRoute.php) | `id`, `team_id`, `domain`, `source_pattern`, `destination`, `priority`, `active` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MailAccountController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-api/src/Http/Controllers/MailAccountController.php) | `public function index(Request $request, ListMailAccounts $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function store(Request $request, CreateMailAccount $create): JsonResponse`<br>`public function update(Request $request, string $id, UpdateMailAccount $update): JsonResponse`<br>`public function delete(Request $request, string $id, DeleteMailAccount $delete): JsonResponse`<br>`public function operation(Request $request, RecordMailOperation $record): JsonResponse`<br>`public function alias(Request $request, CreateMailAlias $create): JsonResponse`<br>`public function updateAlias(Request $request, string $id, UpdateMailAlias $update): JsonResponse`<br>`public function deleteAlias(Request $request, string $id, DeleteMailAlias $delete): JsonResponse`<br>`public function updateRoute(Request $request, string $id, UpdateMailRoute $update): JsonResponse`<br>`public function deleteRoute(Request $request, string $id, DeleteMailRoute $delete): JsonResponse`<br>`public function route(Request $request, CreateMailRoute $create): JsonResponse`<br>`public function controls(Request $request, ConfigureMailControls $configure): JsonResponse`<br>`public function diagnostic(Request $request, RecordDeliveryDiagnostic $record): JsonResponse`<br>`public function rotateDkim(Request $request, RotateDkimKey $rotate): JsonResponse`<br>`public function authentication(Request $request, ConfigureMailAuthentication $configure): JsonResponse`<br>`public function domain(Request $request, RegisterMailDomain $register): JsonResponse` |

**Observed route declarations:**

[modules/control-panel-mail-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-api/routes/api.php)

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
<!-- layer-implementation-plan:end -->
