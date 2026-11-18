# CRM: CRM Product Workspace Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-product-workspace). Observed identity: [`liberusoftware/module-crm-product-workspace-filament`](../../../modules/source/liberusoftware--module-crm-product-workspace-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-product-workspace-filament`  
**Matching domain module:** `crm-product-workspace`  
**Application:** CRM  
**Source feature:** [CRM Product Workspace](../features/crm-product-workspace.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-product-workspace` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Sales-facing catalog projections:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bundles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Entitlements:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Price-book references:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Product eligibility:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Governed Billing/Ecommerce synchronization:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-product-workspace-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `sales-facing-catalog-projections`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bundles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `entitlements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `price-book-references`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `product-eligibility`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `governed-billing-ecommerce-synchronization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-product-workspace` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-product-workspace-filament`](https://github.com/liberusoftware/module-crm-product-workspace-filament) (`liberusoftware/crm-product-workspace-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-product-workspace.md) · [API plan](../api/crm-product-workspace.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Sales-facing catalog projections** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sales-facing catalog projections`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bundles** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bundles`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Entitlements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `entitlements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Price-book references** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `price-book references`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Product eligibility** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `product eligibility`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Governed Billing/Ecommerce synchronization** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `governed billing/ecommerce synchronization`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ProductWorkspaceFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace-filament/src/ProductWorkspaceFilamentServiceProvider.php) · [CreateWorkspaceProduct.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace-filament/src/Resources/Pages/CreateWorkspaceProduct.php) · [EditWorkspaceProduct.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace-filament/src/Resources/Pages/EditWorkspaceProduct.php) · [ListWorkspaceProducts.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace-filament/src/Resources/Pages/ListWorkspaceProducts.php) · [WorkspaceProductResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace-filament/src/Resources/WorkspaceProductResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ProductWorkspaceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Queries/ProductWorkspaceQuery.php) | `public function products(int $teamId)`<br>`public function entitlements(int $teamId, int $customerId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [GrantEntitlement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Actions/GrantEntitlement.php) | `public function __construct(private readonly ProductWorkspacePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProductEntitlement` |
| [RecordProductSync.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Actions/RecordProductSync.php) | `public function __construct(private readonly ProductWorkspacePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProductSync` |
| [UpsertWorkspaceProduct.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Actions/UpsertWorkspaceProduct.php) | `public function __construct(private readonly ProductWorkspacePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): WorkspaceProduct` |
| [ProductWorkspacePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Services/ProductWorkspacePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ProductBundle.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Models/ProductBundle.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProductEntitlement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Models/ProductEntitlement.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProductSync.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Models/ProductSync.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkspaceProduct.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Models/WorkspaceProduct.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
