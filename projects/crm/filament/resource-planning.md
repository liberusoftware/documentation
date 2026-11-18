# CRM: Resource Planning Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#resource-planning). Observed identity: [`liberusoftware/module-crm-resource-planning-filament`](../../../modules/source/liberusoftware--module-crm-resource-planning-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-resource-planning-filament`  
**Matching domain module:** `crm-resource-planning`  
**Application:** CRM  
**Source feature:** [Resource Planning](../features/resource-planning.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-resource-planning` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Skills:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Capacity:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Allocation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Utilization:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tentative/confirmed bookings:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Conflicts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Staffing forecasts:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-resource-planning-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `skills`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `capacity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `allocation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `utilization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tentative-confirmed-bookings`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `conflicts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `staffing-forecasts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-resource-planning` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-resource-planning-filament`](https://github.com/liberusoftware/module-crm-resource-planning-filament) (`liberusoftware/crm-resource-planning-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/resource-planning.md) · [API plan](../api/resource-planning.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Skills** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `skills`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Capacity** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `capacity`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Allocation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `allocation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Utilization** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `utilization`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tentative/confirmed bookings** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tentative/confirmed bookings`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Conflicts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `conflicts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Staffing forecasts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `staffing forecasts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ResourcePlanningFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning-filament/src/ResourcePlanningFilamentPlugin.php) · [ResourcePlanningFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning-filament/src/ResourcePlanningFilamentServiceProvider.php) · [PlanningResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning-filament/src/Resources/PlanningResource.php) · [CreateBooking.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning-filament/src/Resources/PlanningResource/Pages/CreateBooking.php) · [ListBookings.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning-filament/src/Resources/PlanningResource/Pages/ListBookings.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ResourcePlanningQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Queries/ResourcePlanningQuery.php) | `public function skills(int $teamId)`<br>`public function capacity(int $teamId)`<br>`public function bookings(int $teamId)`<br>`public function forecasts(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateBooking.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Actions/CreateBooking.php) | `public function __construct(private readonly ResourcePlanningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ResourceBooking` |
| [RecordForecast.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Actions/RecordForecast.php) | `public function __construct(private readonly ResourcePlanningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ResourceForecast` |
| [SetCapacity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Actions/SetCapacity.php) | `public function __construct(private readonly ResourcePlanningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ResourceCapacity` |
| [SetRate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Actions/SetRate.php) | `public function __construct(private readonly ResourcePlanningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ResourceRate` |
| [UpsertSkill.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Actions/UpsertSkill.php) | `public function __construct(private readonly ResourcePlanningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ResourceSkill` |
| [ResourcePlanningPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Services/ResourcePlanningPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ResourceBooking.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Models/ResourceBooking.php) | No literal fillable array detected; inspect the model and API schema. |
| [ResourceCapacity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Models/ResourceCapacity.php) | No literal fillable array detected; inspect the model and API schema. |
| [ResourceForecast.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Models/ResourceForecast.php) | No literal fillable array detected; inspect the model and API schema. |
| [ResourceRate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Models/ResourceRate.php) | No literal fillable array detected; inspect the model and API schema. |
| [ResourceSkill.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Models/ResourceSkill.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
