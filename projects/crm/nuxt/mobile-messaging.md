# CRM: Mobile Messaging Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#mobile-messaging). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-mobile-messaging-nuxt`
**Matching domain module:** `crm-mobile-messaging`
**Application:** CRM
**Source feature:** [Mobile Messaging](../features/mobile-messaging.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/mobile-messaging.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-mobile-messaging` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Consent-aware SMS/MMS/WhatsApp/push campaigns:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Templates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Short links:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Keywords:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Opt-in/out:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Quiet hours:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Sender governance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Delivery/reply handling:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-mobile-messaging-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `consent-aware-sms-mms-whatsapp-push-campaigns`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `templates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `short-links`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `keywords`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `opt-in-out`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `quiet-hours`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sender-governance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `delivery-reply-handling`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-mobile-messaging` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/mobile-messaging.md)) |
| Capability Nuxt module skeleton | [`module-crm-mobile-messaging-nuxt`](https://github.com/liberusoftware/module-crm-mobile-messaging-nuxt) (`@liberusoftware/module-crm-mobile-messaging-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Consent-aware SMS/MMS/WhatsApp/push campaigns** | Expose composable and Vue 3 component for `consent-aware sms/mms/whatsapp/push campaigns` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mobile-messaging.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Templates** | Expose composable and Vue 3 component for `templates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mobile-messaging.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Short links** | Expose composable and Vue 3 component for `short links` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mobile-messaging.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Keywords** | Expose composable and Vue 3 component for `keywords` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mobile-messaging.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Opt-in/out** | Expose composable and Vue 3 component for `opt-in/out` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mobile-messaging.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Quiet hours** | Expose composable and Vue 3 component for `quiet hours` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mobile-messaging.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Sender governance** | Expose composable and Vue 3 component for `sender governance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mobile-messaging.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Delivery/reply handling** | Expose composable and Vue 3 component for `delivery/reply handling` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/mobile-messaging.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CampaignQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Queries/CampaignQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Actions/CreateCampaign.php) | `public function __construct(private readonly MobileMessagingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): MessagingCampaign` |
| [RecordMessage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Actions/RecordMessage.php) | `public function __construct(private readonly MobileMessagingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, MessagingCampaign $campaign, array $input): MessagingMessage` |
| [UpsertContactConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Actions/UpsertContactConsent.php) | `public function __construct(private readonly MobileMessagingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): MessagingContact` |
| [MobileMessagingPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Services/MobileMessagingPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MessagingCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Models/MessagingCampaign.php) | No literal fillable array detected; inspect the model and API schema. |
| [MessagingContact.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Models/MessagingContact.php) | No literal fillable array detected; inspect the model and API schema. |
| [MessagingMessage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Models/MessagingMessage.php) | No literal fillable array detected; inspect the model and API schema. |
| [MessagingTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging/src/Models/MessagingTemplate.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [MobileMessagingController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-mobile-messaging-api/src/Http/Controllers/MobileMessagingController.php) | `public function index(Request $r, CampaignQuery $q): JsonResponse`<br>`public function consent(Request $r, UpsertContactConsent $a): JsonResponse`<br>`public function store(Request $r, CreateCampaign $a): JsonResponse`<br>`public function message(Request $r, MessagingCampaign $campaign, RecordMessage $a): JsonResponse` |
<!-- layer-implementation-plan:end -->
