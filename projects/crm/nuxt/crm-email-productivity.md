# CRM: Crm Email Productivity Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-email-productivity). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-email-productivity-nuxt`
**Matching domain module:** `crm-email-productivity`
**Application:** CRM
**Source feature:** [Crm Email Productivity](../features/crm-email-productivity.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-email-productivity.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-email-productivity` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Mailbox sync:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Send/log:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Templates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Snippets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Scheduling:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Open/click/reply tracking policy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Shared/team inbox:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Signatures:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Sidebars:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Gmail/Outlook adapters:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-email-productivity-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `mailbox-sync`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `send-log`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `templates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `snippets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `scheduling`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `open-click-reply-tracking-policy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `shared-team-inbox`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `signatures`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sidebars`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `gmail-outlook-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-email-productivity` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-email-productivity.md)) |
| Capability Nuxt module skeleton | [`module-crm-email-productivity-nuxt`](https://github.com/liberusoftware/module-crm-email-productivity-nuxt) (`@liberusoftware/module-crm-email-productivity-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Mailbox sync** | Expose composable and Vue 3 component for `mailbox sync` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-email-productivity.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Send/log** | Expose composable and Vue 3 component for `send/log` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-email-productivity.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Templates** | Expose composable and Vue 3 component for `templates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-email-productivity.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Snippets** | Expose composable and Vue 3 component for `snippets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-email-productivity.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Scheduling** | Expose composable and Vue 3 component for `scheduling` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-email-productivity.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Open/click/reply tracking policy** | Expose composable and Vue 3 component for `open/click/reply tracking policy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-email-productivity.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Shared/team inbox** | Expose composable and Vue 3 component for `shared/team inbox` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-email-productivity.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Signatures** | Expose composable and Vue 3 component for `signatures` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-email-productivity.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Sidebars** | Expose composable and Vue 3 component for `sidebars` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-email-productivity.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Gmail/Outlook adapters** | Expose composable and Vue 3 component for `gmail/outlook adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-email-productivity.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EmailProductivityQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Queries/EmailProductivityQuery.php) | `public function mailboxes(int $teamId)`<br>`public function templates(int $teamId)`<br>`public function messages(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConnectMailbox.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Actions/ConnectMailbox.php) | `public function __construct(private readonly EmailProductivityPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): EmailMailbox` |
| [CreateEmailTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Actions/CreateEmailTemplate.php) | `public function __construct(private readonly EmailProductivityPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): EmailTemplate` |
| [RecordEmailEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Actions/RecordEmailEvent.php) | `public function execute(int $teamId, EmailMessage $message, array $input): EmailEvent` |
| [SendEmail.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Actions/SendEmail.php) | `public function __construct(private readonly EmailProductivityPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): EmailMessage` |
| [EmailProductivityPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Services/EmailProductivityPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EmailEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Models/EmailEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [EmailMailbox.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Models/EmailMailbox.php) | No literal fillable array detected; inspect the model and API schema. |
| [EmailMessage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Models/EmailMessage.php) | No literal fillable array detected; inspect the model and API schema. |
| [EmailTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Models/EmailTemplate.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [EmailProductivityController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity-api/src/Http/Controllers/EmailProductivityController.php) | `public function __construct(private readonly EmailProductivityQuery $query)`<br>`public function mailboxes(): JsonResponse`<br>`public function templates(): JsonResponse`<br>`public function messages(): JsonResponse`<br>`public function connect(ConnectMailbox $action): JsonResponse`<br>`public function template(CreateEmailTemplate $action): JsonResponse`<br>`public function send(SendEmail $action): JsonResponse`<br>`public function event(EmailMessage $message, RecordEmailEvent $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-email-productivity-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/email-productivity')->group(function (): void {
Route::get('mailboxes', [EmailProductivityController::class, 'mailboxes']);
Route::get('templates', [EmailProductivityController::class, 'templates']);
Route::get('messages', [EmailProductivityController::class, 'messages']);
Route::post('mailboxes', [EmailProductivityController::class, 'connect']);
Route::post('templates', [EmailProductivityController::class, 'template']);
Route::post('messages', [EmailProductivityController::class, 'send']);
Route::post('messages/{message}/events', [EmailProductivityController::class, 'event']);
```
<!-- layer-implementation-plan:end -->
