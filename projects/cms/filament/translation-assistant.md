# CMS: Translation Assistant Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#translation-assistant). Observed identity: [`liberusoftware/module-cms-translation-assistant-filament`](../../../modules/source/liberusoftware--module-cms-translation-assistant-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-translation-assistant-filament`  
**Matching domain module:** `cms-translation-assistant`  
**Application:** CMS  
**Source feature:** [Translation Assistant](../features/translation-assistant.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-translation-assistant` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Draft translations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Glossary/style enforcement:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Confidence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Review:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Provider/model provenance:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-translation-assistant-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `draft-translations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `glossary-style-enforcement`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `confidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `review`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `provider-model-provenance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-translation-assistant` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-translation-assistant-filament`](https://github.com/liberusoftware/module-cms-translation-assistant-filament) (`liberusoftware/cms-translation-assistant-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/translation-assistant.md) · [API plan](../api/translation-assistant.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Draft translations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `draft translations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Glossary/style enforcement** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `glossary/style enforcement`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Confidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `confidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Review** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `review`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Provider/model provenance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provider/model provenance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListTranslationDrafts.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-translation-assistant-filament/src/Resources/Pages/ListTranslationDrafts.php) · [TranslationDraftResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-translation-assistant-filament/src/Resources/TranslationDraftResource.php) · [TranslationAssistantFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-translation-assistant-filament/src/TranslationAssistantFilamentServiceProvider.php).

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
