# CMS: Cms Field System Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-field-system). Observed identity: [`liberusoftware/module-cms-field-system-filament`](../../../modules/source/liberusoftware--module-cms-field-system-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-cms-field-system-filament`  
**Matching domain module:** `cms-field-system`  
**Application:** CMS  
**Source feature:** [Cms Field System](../features/cms-field-system.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-field-system` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Reusable typed fields:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cardinality:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Defaults:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Validation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Computed fields:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Conditional fields:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Field groups:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Schema migrations:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-cms-field-system-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `reusable-typed-fields`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cardinality`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `defaults`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `validation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `computed-fields`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `conditional-fields`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `field-groups`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `schema-migrations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-field-system` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-field-system-filament`](https://github.com/liberusoftware/module-cms-field-system-filament) (`liberusoftware/cms-field-system-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-field-system.md) · [API plan](../api/cms-field-system.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Reusable typed fields** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reusable typed fields`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cardinality** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cardinality`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Defaults** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `defaults`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Validation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `validation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Computed fields** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `computed fields`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Conditional fields** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `conditional fields`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Field groups** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `field groups`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Schema migrations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `schema migrations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [FieldSystemFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-field-system-filament/src/FieldSystemFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [FieldSystemService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-field-system/src/Services/FieldSystemService.php) | `public function __construct(private FieldTypeRegistryInterface $types)`<br>`public function saveSchema(?int $teamId, string $key, string $name, array $fields, ?string $reason = null): FieldSchema`<br>`public function validateData(FieldSchema $schema, array $data): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FieldSchema.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-field-system/src/Models/FieldSchema.php) | `team_id`, `key`, `name`, `version`, `fields`, `history` |
<!-- layer-implementation-plan:end -->
