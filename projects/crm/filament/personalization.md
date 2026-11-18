# CRM: Personalization Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#personalization). Observed identity: [`liberusoftware/module-crm-personalization-filament`](../../../modules/source/liberusoftware--module-crm-personalization-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-personalization-filament`  
**Matching domain module:** `crm-personalization`  
**Application:** CRM  
**Source feature:** [Personalization](../features/personalization.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-personalization` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Rules and decisioning for content:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Offer:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Channel:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Send time:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Locale:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Lifecycle:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Customer attributes with holdouts and fallback:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-personalization-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `rules-and-decisioning-for-content`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `offer`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `channel`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `send-time`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `locale`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `lifecycle`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `customer-attributes-with-holdouts-and-fallback`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-personalization` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-personalization-filament`](https://github.com/liberusoftware/module-crm-personalization-filament) (`liberusoftware/crm-personalization-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/personalization.md) · [API plan](../api/personalization.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Rules and decisioning for content** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rules and decisioning for content`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Offer** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `offer`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Channel** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `channel`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Send time** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `send time`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Locale** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `locale`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Lifecycle** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lifecycle`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Customer attributes with holdouts and fallback** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `customer attributes with holdouts and fallback`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PersonalizationFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization-filament/src/PersonalizationFilamentPlugin.php) · [PersonalizationFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization-filament/src/PersonalizationFilamentServiceProvider.php) · [PersonalizationRuleResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization-filament/src/Resources/PersonalizationRuleResource.php) · [CreatePersonalizationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization-filament/src/Resources/PersonalizationRuleResource/Pages/CreatePersonalizationRule.php) · [EditPersonalizationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization-filament/src/Resources/PersonalizationRuleResource/Pages/EditPersonalizationRule.php) · [ListPersonalizationRules.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization-filament/src/Resources/PersonalizationRuleResource/Pages/ListPersonalizationRules.php).

| Observed core query | Public method signatures |
| --- | --- |
| [PersonalizationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Queries/PersonalizationQuery.php) | `public function rules(int $teamId)`<br>`public function decisions(int $teamId)`<br>`public function outcomes(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePersonalizationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Actions/CreatePersonalizationRule.php) | `public function __construct(private readonly PersonalizationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PersonalizationRule` |
| [DecidePersonalization.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Actions/DecidePersonalization.php) | `public function __construct(private readonly PersonalizationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PersonalizationDecision` |
| [RecordPersonalizationOutcome.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Actions/RecordPersonalizationOutcome.php) | `public function __construct(private readonly PersonalizationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PersonalizationOutcome` |
| [UpdatePersonalizationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Actions/UpdatePersonalizationRule.php) | `public function __construct(private readonly PersonalizationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $ruleId, array $input): PersonalizationRule` |
| [PersonalizationPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Services/PersonalizationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PersonalizationDecision.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Models/PersonalizationDecision.php) | No literal fillable array detected; inspect the model and API schema. |
| [PersonalizationOutcome.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Models/PersonalizationOutcome.php) | No literal fillable array detected; inspect the model and API schema. |
| [PersonalizationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Models/PersonalizationRule.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
