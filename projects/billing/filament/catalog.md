# Billing: Catalog Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#catalog). Observed identity: [`liberusoftware/module-billing-catalog-filament`](../../../modules/source/liberusoftware--module-billing-catalog-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-billing-catalog-filament`  
**Matching domain module:** `billing-catalog`  
**Application:** Billing  
**Source feature:** [Catalog](../features/catalog.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `billing-catalog` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Products:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Plans:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Add-ons:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bundles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Configurable options:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Eligibility:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Channels:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Lifecycle:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-billing-catalog-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `products`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `plans`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `add-ons`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bundles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `configurable-options`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `eligibility`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `channels`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `lifecycle`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `billing-catalog` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-billing-catalog-filament`](https://github.com/liberusoftware/module-billing-catalog-filament) (`liberusoftware/billing-catalog-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/catalog.md) · [API plan](../api/catalog.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Products** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `products`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Plans** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `plans`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Add-ons** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `add-ons`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bundles** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bundles`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Configurable options** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `configurable options`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Eligibility** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `eligibility`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Channels** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `channels`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Lifecycle** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lifecycle`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CatalogFilamentPlugin.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/CatalogFilamentPlugin.php) · [CatalogFilamentServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/CatalogFilamentServiceProvider.php) · [AddonResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/AddonResource.php) · [CreateAddon.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/AddonResource/Pages/CreateAddon.php) · [ListAddons.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/AddonResource/Pages/ListAddons.php) · [BundleResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/BundleResource.php) · [CreateBundle.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/BundleResource/Pages/CreateBundle.php) · [ListBundles.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/BundleResource/Pages/ListBundles.php) · [CatalogRecordResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/CatalogRecordResource.php) · [ChannelResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/ChannelResource.php) · [CreateChannel.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/ChannelResource/Pages/CreateChannel.php) · [ListChannels.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/ChannelResource/Pages/ListChannels.php) · [ConfigurableOptionResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/ConfigurableOptionResource.php) · [CreateConfigurableOption.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-filament/src/Resources/ConfigurableOptionResource/Pages/CreateConfigurableOption.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListCatalogRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Queries/ListCatalogRecords.php) | `public function execute(string $model, ?int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ListProducts.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Queries/ListProducts.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCatalogRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Actions/CreateCatalogRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(string $model, array $attributes): CatalogRecord` |
| [CreateProduct.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Actions/CreateProduct.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): Product` |
| [TransitionCatalogLifecycle.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Actions/TransitionCatalogLifecycle.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CatalogRecord $record, CatalogStatus $status): CatalogRecord` |
| [TransitionProductLifecycle.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Actions/TransitionProductLifecycle.php) | `public function execute(Product $product, ProductStatus $status): Product` |
| [CatalogRecordPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Policies/CatalogRecordPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, CatalogRecord $record): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, CatalogRecord $record): bool` |
| [ProductPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Policies/ProductPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Product $product): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Product $product): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Addon.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Addon.php) | No literal fillable array detected; inspect the model and API schema. |
| [Bundle.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Bundle.php) | No literal fillable array detected; inspect the model and API schema. |
| [CatalogRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/CatalogRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [Channel.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Channel.php) | No literal fillable array detected; inspect the model and API schema. |
| [ConfigurableOption.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/ConfigurableOption.php) | No literal fillable array detected; inspect the model and API schema. |
| [Eligibility.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Eligibility.php) | No literal fillable array detected; inspect the model and API schema. |
| [Plan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Plan.php) | No literal fillable array detected; inspect the model and API schema. |
| [Product.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Product.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
