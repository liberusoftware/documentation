# CRM: Crm Saas Packaging Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-saas-packaging). Observed identity: [`liberusoftware/module-crm-saas-packaging-filament`](../../../modules/source/liberusoftware--module-crm-saas-packaging-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-saas-packaging-filament`  
**Matching domain module:** `crm-saas-packaging`  
**Application:** CRM  
**Source feature:** [Crm Saas Packaging](../features/crm-saas-packaging.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-saas-packaging` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Plans:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Feature/module entitlements:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Limits:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Trials:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Signup provisioning:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Upgrade/downgrade:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Suspension:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cancellation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Billing integration:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-saas-packaging-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `plans`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `feature-module-entitlements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `limits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `trials`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `signup-provisioning`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `upgrade-downgrade`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `suspension`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cancellation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `billing-integration`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-saas-packaging` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-saas-packaging-filament`](https://github.com/liberusoftware/module-crm-saas-packaging-filament) (`liberusoftware/crm-saas-packaging-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-saas-packaging.md) · [API plan](../api/crm-saas-packaging.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Plans** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `plans`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Feature/module entitlements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `feature/module entitlements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Limits** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `limits`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Trials** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `trials`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Signup provisioning** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `signup provisioning`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Upgrade/downgrade** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `upgrade/downgrade`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Suspension** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `suspension`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cancellation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cancellation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Billing integration** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `billing integration`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [SubscriptionResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging-filament/src/Resources/SubscriptionResource.php) · [CreateSubscription.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging-filament/src/Resources/SubscriptionResource/Pages/CreateSubscription.php) · [EditSubscription.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging-filament/src/Resources/SubscriptionResource/Pages/EditSubscription.php) · [ListSubscriptions.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging-filament/src/Resources/SubscriptionResource/Pages/ListSubscriptions.php) · [SaasPackagingFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging-filament/src/SaasPackagingFilamentPlugin.php) · [SaasPackagingFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging-filament/src/SaasPackagingFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [SaasQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Queries/SaasQuery.php) | `public function plans()`<br>`public function subscription(int $teamId): ?SaasSubscription`<br>`public function usage(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ChangeSubscriptionStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Actions/ChangeSubscriptionStatus.php) | `public function execute(int $teamId, int $actorId, string $status): SaasSubscription` |
| [ProvisionSubscription.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Actions/ProvisionSubscription.php) | `public function execute(int $teamId, int $actorId, array $data): SaasSubscription` |
| [RecordUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Actions/RecordUsage.php) | `public function execute(int $teamId, int $actorId, array $data): SaasUsage` |
| [UpdateSubscription.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Actions/UpdateSubscription.php) | `public function execute(int $teamId, int $actorId, array $data): SaasSubscription` |
| [SaasPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Services/SaasPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SaasPlan.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Models/SaasPlan.php) | No literal fillable array detected; inspect the model and API schema. |
| [SaasSubscription.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Models/SaasSubscription.php) | No literal fillable array detected; inspect the model and API schema. |
| [SaasUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Models/SaasUsage.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
