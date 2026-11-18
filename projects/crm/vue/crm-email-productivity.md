# CRM: Crm Email Productivity Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-email-productivity). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-crm-crm-email-productivity-vue-inertia`
**Matching domain module:** `crm-email-productivity`
**Application:** CRM
**Source feature:** [Crm Email Productivity](../features/crm-email-productivity.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-email-productivity.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Mailbox sync:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Send/log:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Templates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Snippets:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Scheduling:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Open/click/reply tracking policy:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Shared/team inbox:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Signatures:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Sidebars:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Gmail/Outlook adapters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-crm-crm-email-productivity-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `mailbox-sync`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `send-log`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `templates`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `snippets`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `scheduling`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `open-click-reply-tracking-policy`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `shared-team-inbox`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `signatures`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `sidebars`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `gmail-outlook-adapters`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `crm-email-productivity` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-crm-laravel-inertia-vue`](https://github.com/liberusoftware/project-crm-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-crm-email-productivity-vue-inertia`](https://github.com/liberusoftware/module-crm-email-productivity-vue-inertia) (`@liberusoftware/module-crm-email-productivity-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/crm-email-productivity.md) · [Core plan](../core/crm-email-productivity.md) · [API plan](../api/crm-email-productivity.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Mailbox sync** | Render `mailbox sync` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Send/log** | Render `send/log` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Templates** | Render `templates` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Snippets** | Render `snippets` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Scheduling** | Render `scheduling` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Open/click/reply tracking policy** | Render `open/click/reply tracking policy` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Shared/team inbox** | Render `shared/team inbox` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Signatures** | Render `signatures` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Sidebars** | Render `sidebars` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Gmail/Outlook adapters** | Render `gmail/outlook adapters` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
