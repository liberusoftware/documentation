# CRM: Goals and Performance Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#goals-and-performance). Observed identity: [`liberusoftware/module-crm-goals-and-performance-filament`](../../../modules/source/liberusoftware--module-crm-goals-and-performance-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-goals-and-performance-filament`  
**Matching domain module:** `crm-goals-and-performance`  
**Application:** CRM  
**Source feature:** [Goals and Performance](../features/goals-and-performance.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-goals-and-performance` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Individual/team/company goals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Activity/outcome targets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Scorecards:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Leaderboards:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reviews:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Coaching plans:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Performance history:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-goals-and-performance-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `individual-team-company-goals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `activity-outcome-targets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `scorecards`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `leaderboards`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reviews`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `coaching-plans`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `performance-history`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-goals-and-performance` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-goals-and-performance-filament`](https://github.com/liberusoftware/module-crm-goals-and-performance-filament) (`liberusoftware/crm-goals-and-performance-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/goals-and-performance.md) · [API plan](../api/goals-and-performance.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Individual/team/company goals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `individual/team/company goals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Activity/outcome targets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `activity/outcome targets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Scorecards** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `scorecards`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Leaderboards** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `leaderboards`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reviews** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reviews`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Coaching plans** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `coaching plans`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Performance history** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `performance history`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [GoalsAndPerformanceFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance-filament/src/GoalsAndPerformanceFilamentServiceProvider.php) · [CreatePerformanceGoal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance-filament/src/Resources/Pages/CreatePerformanceGoal.php) · [EditPerformanceGoal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance-filament/src/Resources/Pages/EditPerformanceGoal.php) · [ListPerformanceGoals.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance-filament/src/Resources/Pages/ListPerformanceGoals.php) · [PerformanceGoalResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance-filament/src/Resources/PerformanceGoalResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [PerformanceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Queries/PerformanceQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateGoal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Actions/CreateGoal.php) | `public function __construct(private readonly PerformancePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PerformanceGoal` |
| [RecordReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Actions/RecordReview.php) | `public function __construct(private readonly PerformancePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PerformanceReview` |
| [UpdateGoalActual.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Actions/UpdateGoalActual.php) | `public function __construct(private readonly PerformancePolicy $policy)`<br>`public function execute(int $teamId, int $userId, PerformanceGoal $goal, array $input): PerformanceEvent` |
| [PerformancePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Services/PerformancePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PerformanceEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Models/PerformanceEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [PerformanceGoal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Models/PerformanceGoal.php) | No literal fillable array detected; inspect the model and API schema. |
| [PerformanceReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-goals-and-performance/src/Models/PerformanceReview.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
