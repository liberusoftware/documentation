# CRM: Crm Revenue Lifecycle Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-revenue-lifecycle). Observed identity: [`liberusoftware/module-crm-revenue-lifecycle-filament`](../../../modules/source/liberusoftware--module-crm-revenue-lifecycle-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-revenue-lifecycle-filament`  
**Matching domain module:** `crm-revenue-lifecycle`  
**Application:** CRM  
**Source feature:** [Crm Revenue Lifecycle](../features/crm-revenue-lifecycle.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-revenue-lifecycle` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Opportunity-to-order orchestration:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Assets/installed products:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Entitlements:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Renewals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Upgrades:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Downgrades:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cancellation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Usage signals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Fallout queues:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-revenue-lifecycle-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `opportunity-to-order-orchestration`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `assets-installed-products`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `entitlements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `renewals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `upgrades`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `downgrades`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cancellation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `usage-signals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `fallout-queues`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-revenue-lifecycle` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-revenue-lifecycle-filament`](https://github.com/liberusoftware/module-crm-revenue-lifecycle-filament) (`liberusoftware/crm-revenue-lifecycle-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-revenue-lifecycle.md) · [API plan](../api/crm-revenue-lifecycle.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Opportunity-to-order orchestration** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `opportunity-to-order orchestration`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Assets/installed products** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `assets/installed products`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Entitlements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `entitlements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Renewals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `renewals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Upgrades** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `upgrades`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Downgrades** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `downgrades`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cancellation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cancellation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Usage signals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `usage signals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Fallout queues** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `fallout queues`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AssetResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle-filament/src/Resources/AssetResource.php) · [CreateAsset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle-filament/src/Resources/AssetResource/Pages/CreateAsset.php) · [EditAsset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle-filament/src/Resources/AssetResource/Pages/EditAsset.php) · [ListAssets.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle-filament/src/Resources/AssetResource/Pages/ListAssets.php) · [RevenueLifecycleFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle-filament/src/RevenueLifecycleFilamentPlugin.php) · [RevenueLifecycleFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle-filament/src/RevenueLifecycleFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [RevenueQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Queries/RevenueQuery.php) | `public function assets(int $teamId)`<br>`public function orders(int $teamId)`<br>`public function fallout(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateOrder.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Actions/CreateOrder.php) | `public function __construct(private readonly RevenuePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): RevenueOrder` |
| [ManageAsset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Actions/ManageAsset.php) | `public function __construct(private readonly RevenuePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): RevenueAsset` |
| [RecordUsageSignal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Actions/RecordUsageSignal.php) | `public function __construct(private readonly RevenuePolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $assetId, array $input): RevenueAsset` |
| [ResolveFallout.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Actions/ResolveFallout.php) | `public function __construct(private readonly RevenuePolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $falloutId, array $input): RevenueFallout` |
| [RevenuePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Services/RevenuePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RevenueAsset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Models/RevenueAsset.php) | No literal fillable array detected; inspect the model and API schema. |
| [RevenueFallout.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Models/RevenueFallout.php) | No literal fillable array detected; inspect the model and API schema. |
| [RevenueOrder.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Models/RevenueOrder.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
