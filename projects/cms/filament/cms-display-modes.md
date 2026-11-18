# CMS: Cms Display Modes Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-display-modes). Observed identity: [`liberusoftware/module-cms-display-modes-filament`](../../../modules/source/liberusoftware--module-cms-display-modes-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-cms-display-modes-filament`  
**Matching domain module:** `cms-display-modes`  
**Application:** CMS  
**Source feature:** [Cms Display Modes](../features/cms-display-modes.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-display-modes` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Named view/form modes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Field formatters:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Per-type display configuration:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Responsive variants:** resource/table/form/action or page behavior for this module's authorized workflow.
- **API projections:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-cms-display-modes-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `named-view-form-modes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `field-formatters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `per-type-display-configuration`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `responsive-variants`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `api-projections`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-display-modes` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-display-modes-filament`](https://github.com/liberusoftware/module-cms-display-modes-filament) (`liberusoftware/cms-display-modes-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-display-modes.md) · [API plan](../api/cms-display-modes.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Named view/form modes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `named view/form modes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Field formatters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `field formatters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Per-type display configuration** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `per-type display configuration`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Responsive variants** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `responsive variants`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **API projections** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `api projections`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [DisplayModesFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-display-modes-filament/src/DisplayModesFilamentServiceProvider.php) · [DisplayModeResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-display-modes-filament/src/Resources/DisplayModeResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [DisplayModesService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-display-modes/src/Services/DisplayModesService.php) | `public function modes(?int $teamId, ?string $contentType = null, int $perPage = 25): LengthAwarePaginator`<br>`public function create(array $data, ?int $teamId = null): DisplayMode`<br>`public function select(string $contentType, ?int $teamId, string $slug = 'default', ?string $variant = null): ?DisplayMode` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DisplayMode.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-display-modes/src/Models/DisplayMode.php) | `team_id`, `name`, `slug`, `content_type`, `mode_type`, `formatters`, `configuration`, `responsive_variants`, `projection`, `active` |
<!-- layer-implementation-plan:end -->
