# Accounting: Accounting Matching Intelligence Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-matching-intelligence). Observed identity: [`liberusoftware/module-accounting-matching-intelligence-filament`](../../../modules/source/liberusoftware--module-accounting-matching-intelligence-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-matching-intelligence-filament`  
**Matching domain module:** `accounting-matching-intelligence`  
**Application:** Accounting  
**Source feature:** [Accounting Matching Intelligence](../features/accounting-matching-intelligence.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-matching-intelligence` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Bank/document/payment/settlement matching suggestions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Confidence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Evidence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Feedback:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Safe automation thresholds:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-matching-intelligence-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `bank-document-payment-settlement-matching-suggestions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `confidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `evidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `feedback`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `safe-automation-thresholds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-matching-intelligence` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-matching-intelligence-filament`](https://github.com/liberusoftware/module-accounting-matching-intelligence-filament) (`liberusoftware/accounting-matching-intelligence-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-matching-intelligence.md) · [API plan](../api/accounting-matching-intelligence.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Bank/document/payment/settlement matching suggestions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bank/document/payment/settlement matching suggestions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Confidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `confidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Evidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `evidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Feedback** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `feedback`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Safe automation thresholds** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `safe automation thresholds`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [MatchingIntelligenceFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence-filament/src/MatchingIntelligenceFilamentPlugin.php) · [MatchingIntelligenceFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence-filament/src/MatchingIntelligenceFilamentServiceProvider.php) · [MatchingSuggestionResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence-filament/src/Resources/MatchingSuggestionResource.php) · [ListMatchingSuggestions.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence-filament/src/Resources/Pages/ListMatchingSuggestions.php).

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
<!-- layer-implementation-plan:end -->
