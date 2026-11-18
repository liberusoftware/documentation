# CRM: Loyalty Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#loyalty). Observed identity: [`liberusoftware/module-crm-loyalty-filament`](../../../modules/source/liberusoftware--module-crm-loyalty-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-loyalty-filament`  
**Matching domain module:** `crm-loyalty`  
**Application:** CRM  
**Source feature:** [Loyalty](../features/loyalty.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-loyalty` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Programs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tiers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Points ledger:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Earning/redemption rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rewards:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Expiry:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Partner activity:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Liabilities export:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Fraud controls:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Member statements:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-loyalty-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `programs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tiers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `points-ledger`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `earning-redemption-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rewards`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `expiry`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `partner-activity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `liabilities-export`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `fraud-controls`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `member-statements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-loyalty` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-loyalty-filament`](https://github.com/liberusoftware/module-crm-loyalty-filament) (`liberusoftware/crm-loyalty-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/loyalty.md) · [API plan](../api/loyalty.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Programs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `programs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tiers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tiers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Points ledger** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `points ledger`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Earning/redemption rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `earning/redemption rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rewards** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rewards`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Expiry** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `expiry`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Partner activity** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `partner activity`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Liabilities export** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `liabilities export`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Fraud controls** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `fraud controls`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Member statements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `member statements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [LoyaltyFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty-filament/src/LoyaltyFilamentServiceProvider.php) · [LoyaltyProgramResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty-filament/src/Resources/LoyaltyProgramResource.php) · [CreateLoyaltyProgram.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty-filament/src/Resources/Pages/CreateLoyaltyProgram.php) · [EditLoyaltyProgram.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty-filament/src/Resources/Pages/EditLoyaltyProgram.php) · [ListLoyaltyPrograms.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty-filament/src/Resources/Pages/ListLoyaltyPrograms.php).

| Observed core query | Public method signatures |
| --- | --- |
| [LoyaltyQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Queries/LoyaltyQuery.php) | `public function forTeam(int $teamId)`<br>`public function statement(int $teamId, int $memberId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateProgram.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Actions/CreateProgram.php) | `public function __construct(private readonly LoyaltyPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): LoyaltyProgram` |
| [EnrollMember.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Actions/EnrollMember.php) | `public function __construct(private readonly LoyaltyPolicy $policy)`<br>`public function execute(int $teamId, int $userId, LoyaltyProgram $program, array $input): LoyaltyMember` |
| [RecordPoints.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Actions/RecordPoints.php) | `public function __construct(private readonly LoyaltyPolicy $policy)`<br>`public function execute(int $teamId, int $userId, LoyaltyMember $member, array $input): LoyaltyLedgerEntry` |
| [SetFraudControl.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Actions/SetFraudControl.php) | `public function __construct(private readonly LoyaltyPolicy $policy)`<br>`public function execute(int $teamId, int $userId, LoyaltyMember $member, array $input): LoyaltyControl` |
| [LoyaltyPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Services/LoyaltyPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [LoyaltyControl.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Models/LoyaltyControl.php) | No literal fillable array detected; inspect the model and API schema. |
| [LoyaltyLedgerEntry.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Models/LoyaltyLedgerEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [LoyaltyMember.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Models/LoyaltyMember.php) | No literal fillable array detected; inspect the model and API schema. |
| [LoyaltyProgram.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Models/LoyaltyProgram.php) | No literal fillable array detected; inspect the model and API schema. |
| [LoyaltyRuleReward.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-loyalty/src/Models/LoyaltyRuleReward.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
