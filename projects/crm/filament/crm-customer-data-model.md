# CRM: Crm Customer Data Model Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-customer-data-model). Observed identity: [`liberusoftware/module-crm-customer-data-model-filament`](../../../modules/source/liberusoftware--module-crm-customer-data-model-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-customer-data-model-filament`  
**Matching domain module:** `crm-customer-data-model`  
**Application:** CRM  
**Source feature:** [Crm Customer Data Model](../features/crm-customer-data-model.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-customer-data-model` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Standard/custom objects:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Fields:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Relationships:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Layouts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Validation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Calculated fields:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Required-by-stage fields:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Schema versioning:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-customer-data-model-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `standard-custom-objects`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `fields`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `relationships`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `layouts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `validation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `calculated-fields`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `required-by-stage-fields`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `schema-versioning`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-customer-data-model` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-customer-data-model-filament`](https://github.com/liberusoftware/module-crm-customer-data-model-filament) (`liberusoftware/crm-customer-data-model-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-customer-data-model.md) · [API plan](../api/crm-customer-data-model.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Standard/custom objects** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `standard/custom objects`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Fields** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `fields`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Relationships** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `relationships`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Layouts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `layouts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Validation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `validation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Calculated fields** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `calculated fields`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Required-by-stage fields** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `required-by-stage fields`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Schema versioning** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `schema versioning`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CustomerDataModelFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model-filament/src/CustomerDataModelFilamentPlugin.php) · [CustomerDataModelFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model-filament/src/CustomerDataModelFilamentServiceProvider.php) · [FieldDefinitionResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model-filament/src/Resources/FieldDefinitionResource.php) · [CreateFieldDefinition.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model-filament/src/Resources/FieldDefinitionResource/Pages/CreateFieldDefinition.php) · [EditFieldDefinition.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model-filament/src/Resources/FieldDefinitionResource/Pages/EditFieldDefinition.php) · [ListFieldDefinitions.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model-filament/src/Resources/FieldDefinitionResource/Pages/ListFieldDefinitions.php) · [LayoutDefinitionResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model-filament/src/Resources/LayoutDefinitionResource.php) · [CreateLayoutDefinition.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model-filament/src/Resources/LayoutDefinitionResource/Pages/CreateLayoutDefinition.php) · [EditLayoutDefinition.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model-filament/src/Resources/LayoutDefinitionResource/Pages/EditLayoutDefinition.php) · [ListLayoutDefinitions.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model-filament/src/Resources/LayoutDefinitionResource/Pages/ListLayoutDefinitions.php) · [ObjectDefinitionResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model-filament/src/Resources/ObjectDefinitionResource.php) · [CreateObjectDefinition.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model-filament/src/Resources/ObjectDefinitionResource/Pages/CreateObjectDefinition.php) · [EditObjectDefinition.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model-filament/src/Resources/ObjectDefinitionResource/Pages/EditObjectDefinition.php) · [ListObjectDefinitions.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model-filament/src/Resources/ObjectDefinitionResource/Pages/ListObjectDefinitions.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateObject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Actions/CreateObject.php) | `public function execute(int $teamId, array $attributes): ObjectDefinition` |
| [PublishSchema.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Actions/PublishSchema.php) | `public function execute(ObjectDefinition $object, ?int $actorId = null): SchemaVersion` |
| [SchemaValidator.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Contracts/SchemaValidator.php) | `public function validate(ObjectDefinition $object, array $values, ?string $stage = null): array` |
| [SchemaValidationService.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Services/SchemaValidationService.php) | `public function validate(ObjectDefinition $object, array $values, ?string $stage = null): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FieldDefinition.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Models/FieldDefinition.php) | `object_id`, `key`, `label`, `type`, `description`, `config`, `is_required`, `is_calculated`, `calculation`, `required_stages`, `position` |
| [LayoutDefinition.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Models/LayoutDefinition.php) | `object_id`, `key`, `label`, `sections`, `is_default` |
| [ObjectDefinition.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Models/ObjectDefinition.php) | `team_id`, `key`, `label`, `description`, `is_standard`, `status`, `current_version` |
| [RelationshipDefinition.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Models/RelationshipDefinition.php) | `team_id`, `from_object_id`, `to_object_id`, `key`, `label`, `cardinality`, `config` |
| [SchemaVersion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Models/SchemaVersion.php) | `object_id`, `version`, `status`, `snapshot`, `published_by`, `published_at` |
<!-- layer-implementation-plan:end -->
