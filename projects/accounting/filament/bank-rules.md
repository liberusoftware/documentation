# Accounting: Bank Rules Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#bank-rules). Observed identity: [`liberusoftware/module-accounting-bank-rules-filament`](../../../modules/source/liberusoftware--module-accounting-bank-rules-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-bank-rules-filament`  
**Matching domain module:** `accounting-bank-rules`  
**Application:** Accounting  
**Source feature:** [Bank Rules](../features/bank-rules.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-bank-rules` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Payee/text/amount/account conditions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Split/category/tax/dimension actions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Priority:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Suggestions/automation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Testing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **History:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-bank-rules-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `payee-text-amount-account-conditions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `split-category-tax-dimension-actions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `priority`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `suggestions-automation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `testing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `history`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-bank-rules` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-bank-rules-filament`](https://github.com/liberusoftware/module-accounting-bank-rules-filament) (`liberusoftware/accounting-bank-rules-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/bank-rules.md) · [API plan](../api/bank-rules.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Payee/text/amount/account conditions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payee/text/amount/account conditions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Split/category/tax/dimension actions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `split/category/tax/dimension actions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Priority** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `priority`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Suggestions/automation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `suggestions/automation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Testing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `testing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **History** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `history`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [BankRulesFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules-filament/src/BankRulesFilamentPlugin.php) · [BankRulesFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules-filament/src/BankRulesFilamentServiceProvider.php) · [BankRuleResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules-filament/src/Resources/BankRuleResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [BankRuleQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Queries/BankRuleQuery.php) | `public function forTeam(int $teamId): Builder`<br>`public function matching(int $teamId, array $transaction): array`<br>`public function matches(array $conditions, array $transaction): bool` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordBankRuleDecision.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Actions/RecordBankRuleDecision.php) | `public function handle(BankRule $rule, string $transactionReference, bool $matched, string $outcome, array $actionsApplied = [], ?string $actorReference = null): BankRuleHistory` |
| [SaveBankRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Actions/SaveBankRule.php) | `public function handle(array $attributes, ?BankRule $rule = null): BankRule` |
| [TestBankRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Actions/TestBankRule.php) | `public function __construct(private readonly BankRuleQuery $query)`<br>`public function handle(BankRule $rule, array $transaction): array` |
| [BankRulesPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules-api/src/Policies/BankRulesPolicy.php) | `public function viewAny($user): bool`<br>`public function view($user, BankRule $rule): bool`<br>`public function create($user): bool`<br>`public function update($user, BankRule $rule): bool`<br>`public function delete($user, BankRule $rule): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BankRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Models/BankRule.php) | `team_id`, `name`, `priority`, `enabled`, `conditions`, `actions`, `automation_mode`, `metadata` |
| [BankRuleHistory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Models/BankRuleHistory.php) | `team_id`, `rule_id`, `transaction_reference`, `outcome`, `matched`, `actions_applied`, `actor_reference`, `created_at` |
<!-- layer-implementation-plan:end -->
