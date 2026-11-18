# CRM: Crm Referrals Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-referrals). Observed identity: [`liberusoftware/module-crm-referrals-filament`](../../../modules/source/liberusoftware--module-crm-referrals-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-referrals-filament`  
**Matching domain module:** `crm-referrals`  
**Application:** CRM  
**Source feature:** [Crm Referrals](../features/crm-referrals.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-referrals` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Referral programs and links/codes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Advocates, prospects, and qualification:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rewards, fraud/duplicate controls, status, and attribution:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-referrals-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `referral-programs-and-links-codes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `advocates-prospects-and-qualification`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rewards-fraud-duplicate-controls-status-and-attribution`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-referrals` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-referrals-filament`](https://github.com/liberusoftware/module-crm-referrals-filament) (`liberusoftware/crm-referrals-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-referrals.md) · [API plan](../api/crm-referrals.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Referral programs and links/codes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `referral programs and links/codes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Advocates, prospects, and qualification** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `advocates, prospects, and qualification`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rewards, fraud/duplicate controls, status, and attribution** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rewards, fraud/duplicate controls, status, and attribution`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ReferralsFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals-filament/src/ReferralsFilamentPlugin.php) · [ReferralsFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals-filament/src/ReferralsFilamentServiceProvider.php) · [ReferralResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals-filament/src/Resources/ReferralResource.php) · [CreateReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals-filament/src/Resources/ReferralResource/Pages/CreateReferral.php) · [EditReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals-filament/src/Resources/ReferralResource/Pages/EditReferral.php) · [ListReferrals.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals-filament/src/Resources/ReferralResource/Pages/ListReferrals.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ReferralQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Queries/ReferralQuery.php) | `public function programs(int $teamId)`<br>`public function referrals(int $teamId)`<br>`public function rewards(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateProgram.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Actions/CreateProgram.php) | `public function __construct(private readonly ReferralPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReferralProgram` |
| [CreateReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Actions/CreateReferral.php) | `public function __construct(private readonly ReferralPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Referral` |
| [IssueReward.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Actions/IssueReward.php) | `public function __construct(private readonly ReferralPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReferralReward` |
| [QualifyReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Actions/QualifyReferral.php) | `public function __construct(private readonly ReferralPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $referralId, string $status): Referral` |
| [UpdateReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Actions/UpdateReferral.php) | `public function __construct(private readonly ReferralPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $referralId, array $input): Referral` |
| [ReferralPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Services/ReferralPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Referral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Models/Referral.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReferralProgram.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Models/ReferralProgram.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReferralReward.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-referrals/src/Models/ReferralReward.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
