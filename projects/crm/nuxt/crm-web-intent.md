# CRM: Crm Web Intent Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-web-intent). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-web-intent-nuxt`
**Matching domain module:** `crm-web-intent`
**Application:** CRM
**Source feature:** [Crm Web Intent](../features/crm-web-intent.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-web-intent.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-web-intent` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **First-party visits:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Account identification adapters:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Page/content engagement:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Scoring signals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Alerts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Buyer intent:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Consent:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Lead/account conversion:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-web-intent-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `first-party-visits`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `account-identification-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `page-content-engagement`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `scoring-signals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `alerts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `buyer-intent`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `consent`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `lead-account-conversion`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-web-intent` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-web-intent.md)) |
| Capability Nuxt module skeleton | [`module-crm-web-intent-nuxt`](https://github.com/liberusoftware/module-crm-web-intent-nuxt) (`@liberusoftware/module-crm-web-intent-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **First-party visits** | Expose composable and Vue 3 component for `first-party visits` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-web-intent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Account identification adapters** | Expose composable and Vue 3 component for `account identification adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-web-intent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Page/content engagement** | Expose composable and Vue 3 component for `page/content engagement` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-web-intent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Scoring signals** | Expose composable and Vue 3 component for `scoring signals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-web-intent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Alerts** | Expose composable and Vue 3 component for `alerts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-web-intent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Buyer intent** | Expose composable and Vue 3 component for `buyer intent` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-web-intent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Consent** | Expose composable and Vue 3 component for `consent` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-web-intent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Lead/account conversion** | Expose composable and Vue 3 component for `lead/account conversion` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-web-intent.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [WebIntentQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Queries/WebIntentQuery.php) | `public function visits(int $teamId): Builder`<br>`public function alerts(int $teamId): Builder`<br>`public function summary(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConvertIntent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/ConvertIntent.php) | `public function execute(int $teamId, int $actorId, string $visitorKey, string $targetType, int $targetId, ?int $visitId, array $metadata, WebIntentPolicy $policy): WebIntentConversion` |
| [CreateAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/CreateAlert.php) | `public function execute(int $teamId, int $actorId, string $visitorKey, string $title, string $severity, ?int $visitId, ?string $details, WebIntentPolicy $policy): WebIntentAlert` |
| [IdentifyAccount.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/IdentifyAccount.php) | `public function execute(int $teamId, int $actorId, string $visitorKey, string $adapter, ?string $accountName, ?string $accountDomain, int $confidence, array $metadata, WebIntentPolicy $policy): WebIntentIdentification` |
| [RecordEngagement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/RecordEngagement.php) | `public function execute(WebIntentVisit $visit, array $attributes, WebIntentScorer $scorer): WebIntentEngagement` |
| [RecordVisit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/RecordVisit.php) | `public function execute(int $teamId, string $visitorKey, array $attributes = []): WebIntentVisit` |
| [ResolveAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/ResolveAlert.php) | `public function execute(WebIntentAlert $alert, int $actorId, WebIntentPolicy $policy): WebIntentAlert` |
| [SetConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/SetConsent.php) | `public function execute(int $teamId, string $visitorKey, string $purpose, string $status, ?string $policyVersion = null): WebIntentConsent` |
| [WebIntentAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Services/WebIntentAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $data = []): void` |
| [WebIntentPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Services/WebIntentPolicy.php) | `public function canManage(int $teamId, int $actorId): bool` |
| [WebIntentScorer.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Services/WebIntentScorer.php) | `public function points(string $eventType, ?int $durationSeconds = null): int`<br>`public function level(int $score): string` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WebIntentAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentAlert.php) | `team_id`, `visitor_key`, `visit_id`, `severity`, `title`, `details`, `status`, `triggered_at`, `resolved_at`, `resolved_by` |
| [WebIntentConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentConsent.php) | `team_id`, `visitor_key`, `purpose`, `status`, `policy_version`, `granted_at`, `revoked_at` |
| [WebIntentConversion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentConversion.php) | `team_id`, `visitor_key`, `visit_id`, `target_type`, `target_id`, `actor_id`, `status`, `metadata` |
| [WebIntentEngagement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentEngagement.php) | `team_id`, `visit_id`, `visitor_key`, `event_type`, `page_url`, `content_type`, `content_id`, `points`, `duration_seconds`, `dedupe_key`, `metadata`, `occurred_at` |
| [WebIntentIdentification.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentIdentification.php) | `team_id`, `visitor_key`, `adapter`, `account_name`, `account_domain`, `confidence`, `status`, `metadata` |
| [WebIntentSignal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentSignal.php) | `team_id`, `visit_id`, `visitor_key`, `signal`, `points`, `metadata`, `occurred_at` |
| [WebIntentVisit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentVisit.php) | `team_id`, `visitor_key`, `session_key`, `ip_hash`, `user_agent_hash`, `landing_url`, `referrer`, `consent_status`, `score`, `intent_level`, `status`, `started_at`, `ended_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [WebIntentController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent-api/src/Http/Controllers/WebIntentController.php) | `public function index(Request $request, WebIntentQuery $query): JsonResponse`<br>`public function store(Request $request, RecordVisit $record): JsonResponse`<br>`public function show(Request $request, int $visit): JsonResponse`<br>`public function engagement(Request $request, int $visit, RecordEngagement $record, WebIntentScorer $scorer): JsonResponse`<br>`public function consent(Request $request, SetConsent $set): JsonResponse`<br>`public function identification(Request $request, IdentifyAccount $identify, WebIntentPolicy $policy): JsonResponse`<br>`public function alerts(Request $request, WebIntentQuery $query): JsonResponse`<br>`public function createAlert(Request $request, CreateAlert $create, WebIntentPolicy $policy): JsonResponse`<br>`public function resolveAlert(Request $request, int $alert, ResolveAlert $resolve, WebIntentPolicy $policy): JsonResponse`<br>`public function convert(Request $request, ConvertIntent $convert, WebIntentPolicy $policy): JsonResponse`<br>`public function summary(Request $request, WebIntentQuery $query): JsonResponse` |

**Observed route declarations:**

[modules/crm-web-intent-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/web-intent')->group(function (): void {
Route::get('/summary', [WebIntentController::class, 'summary'])->name('crm.web-intent.summary');
Route::get('/alerts', [WebIntentController::class, 'alerts'])->name('crm.web-intent.alerts');
Route::get('/visits', [WebIntentController::class, 'index'])->name('crm.web-intent.visits.index');
Route::post('/visits', [WebIntentController::class, 'store'])->name('crm.web-intent.visits.store');
Route::get('/visits/{visit}', [WebIntentController::class, 'show'])->name('crm.web-intent.visits.show');
Route::post('/visits/{visit}/engagements', [WebIntentController::class, 'engagement'])->name('crm.web-intent.engagements.store');
Route::post('/consents', [WebIntentController::class, 'consent'])->name('crm.web-intent.consents.store');
Route::post('/identifications', [WebIntentController::class, 'identification'])->name('crm.web-intent.identifications.store');
Route::post('/alerts', [WebIntentController::class, 'createAlert'])->name('crm.web-intent.alerts.store');
Route::post('/alerts/{alert}/resolve', [WebIntentController::class, 'resolveAlert'])->name('crm.web-intent.alerts.resolve');
Route::post('/conversions', [WebIntentController::class, 'convert'])->name('crm.web-intent.conversions.store');
```
<!-- layer-implementation-plan:end -->
