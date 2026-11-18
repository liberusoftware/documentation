# CMS: Translation Assistant Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#translation-assistant). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-translation-assistant-nuxt`
**Matching domain module:** `cms-translation-assistant`
**Application:** CMS
**Source feature:** [Translation Assistant](../features/translation-assistant.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/translation-assistant.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `cms-translation-assistant` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Draft translations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Glossary/style enforcement:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Confidence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Review:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Provider/model provenance:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-translation-assistant-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `draft-translations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `glossary-style-enforcement`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `confidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `review`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `provider-model-provenance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `cms-translation-assistant` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/translation-assistant.md)) |
| Capability Nuxt module skeleton | [`module-cms-translation-assistant-nuxt`](https://github.com/liberusoftware/module-cms-translation-assistant-nuxt) (`@liberusoftware/module-cms-translation-assistant-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Draft translations** | Expose composable and Vue 3 component for `draft translations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/translation-assistant.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Glossary/style enforcement** | Expose composable and Vue 3 component for `glossary/style enforcement` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/translation-assistant.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Confidence** | Expose composable and Vue 3 component for `confidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/translation-assistant.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Review** | Expose composable and Vue 3 component for `review` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/translation-assistant.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Provider/model provenance** | Expose composable and Vue 3 component for `provider/model provenance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/translation-assistant.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [TranslationAssistantQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-assistant/src/Queries/TranslationAssistantQuery.php) | `public function __construct(private TenantContextInterface $tenant)`<br>`public function drafts(array $filters = [], int $perPage = 25, ?int $teamId = null): LengthAwarePaginator`<br>`public function draft(int\|string $id, ?int $teamId = null): ?TranslationDraft`<br>`public function glossary(?string $sourceLocale = null, ?string $targetLocale = null, ?int $teamId = null): array`<br>`public function styleRules(?string $locale = null, ?int $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [TranslationProviderInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-assistant/src/Contracts/TranslationProviderInterface.php) | `public function translate(string $text, string $sourceLocale, string $targetLocale, array $context = []): array` |
| [TranslationAssistantService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-assistant/src/Services/TranslationAssistantService.php) | `public function draft(string $subjectType, int\|string $subjectId, string $sourceLocale, string $targetLocale, string $sourceText, string $translatedText, float $confidence, string $provider, string $model, array $provenance = [], ?int $teamId = null): TranslationDraft`<br>`public function check(TranslationDraft $draft): TranslationDraft`<br>`public function review(TranslationDraft $draft, string $decision, string $reviewerType, int\|string $reviewerId): TranslationDraft`<br>`public function updateDraft(TranslationDraft $draft, array $attributes): TranslationDraft`<br>`public function removeDraft(TranslationDraft $draft): void`<br>`public function addGlossary(string $sourceLocale, string $targetLocale, string $sourceTerm, string $preferredTerm, array $forbiddenTerms = [], ?int $teamId = null): GlossaryEntry`<br>`public function addStyleRule(string $locale, string $name, string $pattern, string $message, string $severity = 'warning', ?int $teamId = null): StyleRule` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [GlossaryEntry.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-assistant/src/Models/GlossaryEntry.php) | `source_locale`, `target_locale`, `source_term`, `preferred_term`, `forbidden_terms`, `team_id` |
| [StyleRule.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-assistant/src/Models/StyleRule.php) | `locale`, `name`, `pattern`, `message`, `severity`, `team_id` |
| [TranslationDraft.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-translation-assistant/src/Models/TranslationDraft.php) | `subject_type`, `subject_id`, `source_locale`, `target_locale`, `source_text`, `translated_text`, `confidence`, `status`, `provider`, `model`, `provenance`, `violations`, `reviewer_type`, `reviewer_id`, `reviewed_at`, `team_id` |
<!-- layer-implementation-plan:end -->
