# CRM: Crm Memberships Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-memberships). Observed identity: [`liberusoftware/module-crm-memberships-filament`](../../../modules/source/liberusoftware--module-crm-memberships-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-memberships-filament`  
**Matching domain module:** `crm-memberships`  
**Application:** CRM  
**Source feature:** [Crm Memberships](../features/crm-memberships.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-memberships` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Membership plans:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Gated resources:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Lifecycle:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Access grants:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Renewal references:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Community/course bundles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Member portal:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-memberships-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `membership-plans`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `gated-resources`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `lifecycle`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `access-grants`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `renewal-references`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `community-course-bundles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `member-portal`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-memberships` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-memberships-filament`](https://github.com/liberusoftware/module-crm-memberships-filament) (`liberusoftware/crm-memberships-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-memberships.md) · [API plan](../api/crm-memberships.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Membership plans** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `membership plans`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Gated resources** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `gated resources`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Lifecycle** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lifecycle`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Access grants** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `access grants`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Renewal references** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `renewal references`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Community/course bundles** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `community/course bundles`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Member portal** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `member portal`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [MembershipsFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships-filament/src/MembershipsFilamentServiceProvider.php) · [MembershipPlanResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships-filament/src/Resources/MembershipPlanResource.php) · [CreateMembershipPlan.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships-filament/src/Resources/Pages/CreateMembershipPlan.php) · [EditMembershipPlan.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships-filament/src/Resources/Pages/EditMembershipPlan.php) · [ListMembershipPlans.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships-filament/src/Resources/Pages/ListMembershipPlans.php).

| Observed core query | Public method signatures |
| --- | --- |
| [MembershipQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships/src/Queries/MembershipQuery.php) | `public function forTeam(int $teamId)`<br>`public function memberGrants(int $teamId, int $memberId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ChangeGrantStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships/src/Actions/ChangeGrantStatus.php) | `public function __construct(private readonly MembershipPolicy $policy)`<br>`public function execute(int $teamId, int $userId, MembershipGrant $grant, array $input): MembershipGrant` |
| [CreatePlan.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships/src/Actions/CreatePlan.php) | `public function __construct(private readonly MembershipPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): MembershipPlan` |
| [GrantAccess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships/src/Actions/GrantAccess.php) | `public function __construct(private readonly MembershipPolicy $policy)`<br>`public function execute(int $teamId, int $userId, MembershipPlan $plan, array $input): MembershipGrant` |
| [MembershipPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships/src/Services/MembershipPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MembershipBundle.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships/src/Models/MembershipBundle.php) | No literal fillable array detected; inspect the model and API schema. |
| [MembershipGrant.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships/src/Models/MembershipGrant.php) | No literal fillable array detected; inspect the model and API schema. |
| [MembershipPlan.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships/src/Models/MembershipPlan.php) | No literal fillable array detected; inspect the model and API schema. |
| [MembershipResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships/src/Models/MembershipResource.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
