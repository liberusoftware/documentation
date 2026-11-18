# Maintenance: Module Maintenance Inspections Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-maintenance-inspections). Observed identity: [`liberusoftware/module-maintenance-inspections-filament`](../../../modules/source/liberusoftware--module-maintenance-inspections-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-maintenance-module-maintenance-inspections-filament`  
**Matching domain module:** `module-maintenance-inspections`  
**Application:** Maintenance  
**Source feature:** [Module Maintenance Inspections](../features/module-maintenance-inspections.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-maintenance-inspections` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Templates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Conditional checklists:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Readings:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Failures:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Signatures:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Certificates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Follow-up:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-maintenance-module-maintenance-inspections-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `templates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `conditional-checklists`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `readings`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `failures`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `signatures`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `certificates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `follow-up`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-maintenance-inspections` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-maintenance-laravel-filament`](https://github.com/liberusoftware/project-maintenance-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-maintenance-inspections-filament`](https://github.com/liberusoftware/module-maintenance-inspections-filament) (`liberusoftware/maintenance-inspections-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-maintenance-inspections.md) · [API plan](../api/module-maintenance-inspections.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Templates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `templates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Conditional checklists** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `conditional checklists`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Readings** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `readings`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Failures** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `failures`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Signatures** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `signatures`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Certificates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `certificates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Follow-up** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `follow-up`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [InspectionsFilamentPlugin.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections-filament/src/InspectionsFilamentPlugin.php) · [InspectionsFilamentServiceProvider.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections-filament/src/InspectionsFilamentServiceProvider.php) · [InspectionResource.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections-filament/src/Resources/InspectionResource.php) · [CreateInspection.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections-filament/src/Resources/InspectionResource/Pages/CreateInspection.php) · [EditInspection.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections-filament/src/Resources/InspectionResource/Pages/EditInspection.php) · [ListInspections.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections-filament/src/Resources/InspectionResource/Pages/ListInspections.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CompleteInspection.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/src/Actions/CompleteInspection.php) | `public function handle(int $teamId, Inspection $inspection, string $outcome): Inspection` |
| [CreateInspection.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/src/Actions/CreateInspection.php) | `public function handle(int $teamId, array $attributes): Inspection` |
| [DeleteInspection.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/src/Actions/DeleteInspection.php) | `public function handle(int $teamId, Inspection $inspection): void` |
| [UpdateInspection.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/src/Actions/UpdateInspection.php) | `public function handle(int $teamId, Inspection $inspection, array $attributes): Inspection` |
| [InspectionPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/src/Policies/InspectionPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Inspection $inspection): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Inspection $inspection): bool`<br>`public function delete(object $user, Inspection $inspection): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Inspection.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/src/Models/Inspection.php) | `team_id`, `title`, `template_key`, `status`, `outcome`, `inspected_at`, `inspector_id`, `readings`, `failures`, `signature`, `certificate`, `follow_up` |
<!-- layer-implementation-plan:end -->
