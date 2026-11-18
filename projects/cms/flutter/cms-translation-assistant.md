# Cms Translation Assistant Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-translation-assistant). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-cms-cms-translation-assistant-flutter
**Matching core package:** module-cms-cms-translation-assistant ([implementation](../core/cms-translation-assistant.md))
**Matching API package:** module-cms-cms-translation-assistant-api ([contract](../api/cms-translation-assistant.md))

## Implementation plan

This adapter presents Cms Translation Assistant for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Cms Translation Assistant API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/cms-translation-assistant.md), and [API module](../api/cms-translation-assistant.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `cms-translation-assistant`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-cms-mobile-flutter`](https://github.com/liberusoftware/project-cms-mobile-flutter) | [`module-cms-translation-assistant-flutter`](https://github.com/liberusoftware/module-cms-translation-assistant-flutter) (`module_cms_translation_assistant_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-cms-dart-mobile`](https://github.com/liberusoftware/project-cms-dart-mobile) | [`module-cms-translation-assistant-dart-mobile`](https://github.com/liberusoftware/module-cms-translation-assistant-dart-mobile) (`module_cms_translation_assistant_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-cms-dart-desktop`](https://github.com/liberusoftware/project-cms-dart-desktop) | [`module-cms-translation-assistant-dart-desktop`](https://github.com/liberusoftware/module-cms-translation-assistant-dart-desktop) (`module_cms_translation_assistant_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | [API plan](../api/cms-translation-assistant.md) · [Core plan](../core/cms-translation-assistant.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Draft translations** | Adaptive mobile cards/sheets for `draft translations` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `draft translations` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Glossary/style enforcement** | Adaptive mobile cards/sheets for `glossary/style enforcement` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `glossary/style enforcement` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Confidence** | Adaptive mobile cards/sheets for `confidence` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `confidence` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Review** | Adaptive mobile cards/sheets for `review` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `review` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Provider/model provenance** | Adaptive mobile cards/sheets for `provider/model provenance` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `provider/model provenance` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-cms-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
