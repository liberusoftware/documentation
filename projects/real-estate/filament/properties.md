# Real Estate: Properties Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#properties). Observed identity: [`liberusoftware/real-estate-properties-filament`](../../../modules/source/liberusoftware--real-estate-properties-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-real-estate-properties-filament`  
**Matching domain module:** `real-estate-properties`  
**Application:** Real Estate  
**Source feature:** [Properties](../features/properties.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `real-estate-properties` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Address/location:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Units:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Characteristics:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tenure:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Utilities:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Features:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Status:** resource/table/form/action or page behavior for this module's authorized workflow.
- **History:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Keys:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-real-estate-properties-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `address-location`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `units`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `characteristics`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tenure`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `utilities`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `features`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `status`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `history`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `keys`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `real-estate-properties` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-real-estate-laravel-filament`](https://github.com/liberusoftware/project-real-estate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-real-estate-properties-filament`](https://github.com/liberusoftware/module-real-estate-properties-filament) (`liberusoftware/real-estate-properties-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/properties.md) · [API plan](../api/properties.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Address/location** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `address/location`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Units** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `units`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Characteristics** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `characteristics`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tenure** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tenure`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Utilities** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `utilities`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Features** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `features`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Status** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `status`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **History** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `history`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Keys** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `keys`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PropertiesFilamentPlugin.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-filament/src/PropertiesFilamentPlugin.php) · [PropertiesFilamentServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-filament/src/PropertiesFilamentServiceProvider.php) · [PropertyCategoryResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-filament/src/Resources/PropertyCategoryResource.php) · [CreatePropertyCategory.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-filament/src/Resources/PropertyCategoryResource/Pages/CreatePropertyCategory.php) · [EditPropertyCategory.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-filament/src/Resources/PropertyCategoryResource/Pages/EditPropertyCategory.php) · [ListPropertyCategories.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-filament/src/Resources/PropertyCategoryResource/Pages/ListPropertyCategories.php) · [PropertyResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-filament/src/Resources/PropertyResource.php) · [CreateProperty.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-filament/src/Resources/PropertyResource/Pages/CreateProperty.php) · [EditProperty.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-filament/src/Resources/PropertyResource/Pages/EditProperty.php) · [ListProperties.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-filament/src/Resources/PropertyResource/Pages/ListProperties.php) · [PropertySavedSearchResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-filament/src/Resources/PropertySavedSearchResource.php) · [CreatePropertySavedSearch.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-filament/src/Resources/PropertySavedSearchResource/Pages/CreatePropertySavedSearch.php) · [EditPropertySavedSearch.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-filament/src/Resources/PropertySavedSearchResource/Pages/EditPropertySavedSearch.php) · [ListPropertySavedSearches.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-filament/src/Resources/PropertySavedSearchResource/Pages/ListPropertySavedSearches.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [PropertyCategoryPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Policies/PropertyCategoryPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function delete(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function forceDelete(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [PropertyPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Policies/PropertyPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Property $property): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Property $property): bool`<br>`public function delete(AuthUser $authUser, Property $property): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Property $property): bool`<br>`public function forceDelete(AuthUser $authUser, Property $property): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Property $property): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [PropertyTemplatePolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Policies/PropertyTemplatePolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function delete(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function forceDelete(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CommunityEvent.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/CommunityEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [Neighborhood.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/Neighborhood.php) | No literal fillable array detected; inspect the model and API schema. |
| [NeighborhoodReview.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/NeighborhoodReview.php) | No literal fillable array detected; inspect the model and API schema. |
| [Property.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/Property.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertyCategory.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertyCategory.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertyFavorite.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertyFavorite.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertyHistory.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertyHistory.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertyKey.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertyKey.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
