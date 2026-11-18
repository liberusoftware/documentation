# Accounting: Coding Suggestions Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#coding-suggestions). Observed identity: [`liberusoftware/module-accounting-coding-suggestions-filament`](../../../modules/source/liberusoftware--module-accounting-coding-suggestions-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-coding-suggestions-filament`  
**Matching domain module:** `accounting-coding-suggestions`  
**Application:** Accounting  
**Source feature:** [Coding Suggestions](../features/coding-suggestions.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-coding-suggestions` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Account/tax/dimension/payee suggestions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Confidence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Explanations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **User feedback:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Policy thresholds:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Review:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-coding-suggestions-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `account-tax-dimension-payee-suggestions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `confidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `explanations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `user-feedback`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `policy-thresholds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `review`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-coding-suggestions` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-coding-suggestions-filament`](https://github.com/liberusoftware/module-accounting-coding-suggestions-filament) (`liberusoftware/accounting-coding-suggestions-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/coding-suggestions.md) · [API plan](../api/coding-suggestions.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Account/tax/dimension/payee suggestions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `account/tax/dimension/payee suggestions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Confidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `confidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Explanations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `explanations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **User feedback** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `user feedback`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Policy thresholds** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `policy thresholds`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Review** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `review`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CodingSuggestionsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions-filament/src/CodingSuggestionsFilamentPlugin.php) · [CodingSuggestionsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions-filament/src/CodingSuggestionsFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CodingSuggestionQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Queries/CodingSuggestionQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApplySuggestionFeedback.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Actions/ApplySuggestionFeedback.php) | `public function handle(CodingSuggestion $suggestion, array $feedback): CodingSuggestion` |
| [CreateCodingSuggestion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Actions/CreateCodingSuggestion.php) | `public function handle(array $attributes): CodingSuggestion` |
| [ReviewCodingSuggestion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Actions/ReviewCodingSuggestion.php) | `public function handle(CodingSuggestion $suggestion, array $review): CodingSuggestion` |
| [SetSuggestionPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Actions/SetSuggestionPolicy.php) | `public function handle(CodingSuggestion $suggestion, array $policy): CodingSuggestion` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CodingSuggestion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Models/CodingSuggestion.php) | `team_id`, `source_ref`, `target_type`, `target_ref`, `confidence`, `explanation`, `status`, `feedback`, `policy`, `review` |
<!-- layer-implementation-plan:end -->
