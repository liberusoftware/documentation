# Accounting: Accounting Matching Intelligence Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-matching-intelligence). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-matching-intelligence-nuxt`
**Matching domain module:** `accounting-matching-intelligence`
**Application:** Accounting
**Source feature:** [Accounting Matching Intelligence](../features/accounting-matching-intelligence.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-matching-intelligence.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-matching-intelligence` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Bank/document/payment/settlement matching suggestions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Confidence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Evidence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Feedback:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Safe automation thresholds:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-matching-intelligence-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `bank-document-payment-settlement-matching-suggestions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `confidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `evidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `feedback`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `safe-automation-thresholds`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-matching-intelligence` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-matching-intelligence.md)) |
| Capability Nuxt module skeleton | [`module-accounting-matching-intelligence-nuxt`](https://github.com/liberusoftware/module-accounting-matching-intelligence-nuxt) (`@liberusoftware/module-accounting-matching-intelligence-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Bank/document/payment/settlement matching suggestions** | Expose composable and Vue 3 component for `bank/document/payment/settlement matching suggestions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-matching-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Confidence** | Expose composable and Vue 3 component for `confidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-matching-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Evidence** | Expose composable and Vue 3 component for `evidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-matching-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Feedback** | Expose composable and Vue 3 component for `feedback` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-matching-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Safe automation thresholds** | Expose composable and Vue 3 component for `safe automation thresholds` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-matching-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [MatchingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Queries/MatchingQuery.php) | `public function suggestions(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function automationEligible(?int $teamId = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfigureThreshold.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Actions/ConfigureThreshold.php) | `public function handle(array $attributes): AutomationThreshold` |
| [CreateSuggestion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Actions/CreateSuggestion.php) | `public function handle(array $attributes, array $evidence = []): MatchingSuggestion` |
| [DecideSuggestion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Actions/DecideSuggestion.php) | `public function handle(MatchingSuggestion $suggestion, string $actor, bool $accept = true, bool $automate = false): MatchingSuggestion` |
| [RecordFeedback.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Actions/RecordFeedback.php) | `public function handle(MatchingSuggestion $suggestion, string $actor, string $type, ?string $comment = null): MatchingFeedback` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AutomationThreshold.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Models/AutomationThreshold.php) | `team_id`, `match_type`, `minimum_confidence`, `maximum_amount`, `require_evidence`, `active`, `metadata` |
| [MatchingEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Models/MatchingEvidence.php) | `suggestion_id`, `kind`, `field`, `source_value`, `target_value`, `weight`, `metadata` |
| [MatchingFeedback.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Models/MatchingFeedback.php) | `suggestion_id`, `actor_ref`, `feedback_type`, `comment`, `features`, `metadata` |
| [MatchingSuggestion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Models/MatchingSuggestion.php) | `team_id`, `suggestion_ref`, `source_type`, `source_id`, `target_type`, `target_id`, `match_type`, `confidence`, `score`, `status`, `automation_threshold`, `explanation`, `algorithm_version`, `expires_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MatchingIntelligenceController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence-api/src/Http/Controllers/MatchingIntelligenceController.php) | `public function index(Request $request, MatchingQuery $query): mixed`<br>`public function store(Request $request, CreateSuggestion $action): MatchingSuggestionResource`<br>`public function show(MatchingSuggestion $suggestion): MatchingSuggestionResource`<br>`public function decide(Request $request, MatchingSuggestion $suggestion, DecideSuggestion $action): MatchingSuggestionResource`<br>`public function feedback(Request $request, MatchingSuggestion $suggestion, RecordFeedback $action): JsonResponse`<br>`public function threshold(Request $request, ConfigureThreshold $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-matching-intelligence-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/matching-intelligence')->group(function (): void {
Route::get('/suggestions', [MatchingIntelligenceController::class, 'index'])->name('accounting.matching-intelligence.list');
Route::post('/suggestions', [MatchingIntelligenceController::class, 'store'])->name('accounting.matching-intelligence.create');
Route::get('/suggestions/{suggestion}', [MatchingIntelligenceController::class, 'show'])->name('accounting.matching-intelligence.show');
Route::post('/suggestions/{suggestion}/decide', [MatchingIntelligenceController::class, 'decide'])->name('accounting.matching-intelligence.decide');
Route::post('/suggestions/{suggestion}/feedback', [MatchingIntelligenceController::class, 'feedback'])->name('accounting.matching-intelligence.feedback');
Route::post('/thresholds', [MatchingIntelligenceController::class, 'threshold'])->name('accounting.matching-intelligence.threshold');
```
<!-- layer-implementation-plan:end -->
