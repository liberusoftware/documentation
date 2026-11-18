# CRM: Activities Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#activities). Observed identity: [`liberusoftware/module-crm-activities-filament`](../../../modules/source/liberusoftware--module-crm-activities-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-activities-filament`  
**Matching domain module:** `crm-activities`  
**Application:** CRM  
**Source feature:** [Activities](../features/activities.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-activities` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Tasks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Calls:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Meetings:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Emails:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Deadlines:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recurrence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Queues:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bulk completion:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reminders:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Outcomes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Goals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Activity reporting:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-activities-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `tasks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `calls`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `meetings`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `emails`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `deadlines`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recurrence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `queues`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bulk-completion`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reminders`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `outcomes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `goals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `activity-reporting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-activities` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-activities-filament`](https://github.com/liberusoftware/module-crm-activities-filament) (`liberusoftware/crm-activities-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/activities.md) · [API plan](../api/activities.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Tasks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tasks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Calls** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `calls`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Meetings** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `meetings`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Emails** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `emails`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Deadlines** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `deadlines`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recurrence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recurrence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Queues** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `queues`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bulk completion** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bulk completion`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reminders** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reminders`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Outcomes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `outcomes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Goals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `goals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Activity reporting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `activity reporting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ActivitiesFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities-filament/src/ActivitiesFilamentPlugin.php) · [ActivitiesFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities-filament/src/ActivitiesFilamentServiceProvider.php) · [ActivityGoalResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities-filament/src/Resources/ActivityGoalResource.php) · [CreateActivityGoal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities-filament/src/Resources/ActivityGoalResource/Pages/CreateActivityGoal.php) · [EditActivityGoal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities-filament/src/Resources/ActivityGoalResource/Pages/EditActivityGoal.php) · [ListActivityGoals.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities-filament/src/Resources/ActivityGoalResource/Pages/ListActivityGoals.php) · [ActivityResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities-filament/src/Resources/ActivityResource.php) · [CreateActivity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities-filament/src/Resources/ActivityResource/Pages/CreateActivity.php) · [EditActivity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities-filament/src/Resources/ActivityResource/Pages/EditActivity.php) · [ListActivities.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities-filament/src/Resources/ActivityResource/Pages/ListActivities.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CancelActivity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Actions/CancelActivity.php) | `public function execute(Activity $activity): Activity` |
| [CompleteActivities.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Actions/CompleteActivities.php) | `public function execute(int $teamId, array $activityIds, ?string $outcome = null, ?string $notes = null): int` |
| [CreateActivity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Actions/CreateActivity.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): Activity` |
| [CreateActivityGoal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Actions/CreateActivityGoal.php) | `public function execute(int $teamId, array $attributes): ActivityGoal` |
| [ActivityReport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Services/ActivityReport.php) | `public function summarize(int $teamId, Carbon $from, Carbon $until): array` |
| [ActivityScheduler.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Services/ActivityScheduler.php) | `public function nextOccurrence(Activity $activity): ?Activity`<br>`public function dueReminders(int $teamId, ?Carbon $at = null): Collection` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Activity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Models/Activity.php) | `team_id`, `actor_id`, `assigned_to`, `kind`, `status`, `title`, `description`, `subject_type`, `subject_id`, `starts_at`, `due_at`, `ends_at`, `recurrence`, `recurrence_until`, `reminder_at`, `queue`, `outcome`, `outcome_notes`, `metadata`, `completed_at` |
| [ActivityEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Models/ActivityEvent.php) | `team_id`, `activity_id`, `actor_id`, `event`, `details` |
| [ActivityGoal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Models/ActivityGoal.php) | `team_id`, `owner_id`, `name`, `kind`, `target`, `progress`, `starts_at`, `ends_at`, `status`, `criteria` |
<!-- layer-implementation-plan:end -->
