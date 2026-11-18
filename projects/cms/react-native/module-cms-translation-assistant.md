# Module Cms Translation Assistant React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-translation-assistant). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-module-cms-translation-assistant-react-native
**Matching core package:** module-cms-module-cms-translation-assistant ([implementation](../core/module-cms-translation-assistant.md))
**Matching API package:** module-cms-module-cms-translation-assistant-api ([contract](../api/module-cms-translation-assistant.md))

## Implementation plan

This adapter presents Module Cms Translation Assistant for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Cms Translation Assistant API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/module-cms-translation-assistant.md), and [API module](../api/module-cms-translation-assistant.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `module-cms-translation-assistant`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-cms-mobile-react`](https://github.com/liberusoftware/project-cms-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-cms-translation-assistant.md)) |
| Capability React Native module skeleton | [`module-cms-translation-assistant-react-native`](https://github.com/liberusoftware/module-cms-translation-assistant-react-native) (`@liberusoftware/module-cms-translation-assistant-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Draft translations** | Progressive mobile list/detail/sheet flow for `draft translations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Glossary/style enforcement** | Progressive mobile list/detail/sheet flow for `glossary/style enforcement` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Confidence** | Progressive mobile list/detail/sheet flow for `confidence` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Review** | Progressive mobile list/detail/sheet flow for `review` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Provider/model provenance** | Progressive mobile list/detail/sheet flow for `provider/model provenance` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-cms-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
