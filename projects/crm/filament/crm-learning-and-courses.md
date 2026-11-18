# CRM: Crm Learning And Courses Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-learning-and-courses). Observed identity: [`liberusoftware/module-crm-learning-and-courses-filament`](../../../modules/source/liberusoftware--module-crm-learning-and-courses-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-learning-and-courses-filament`  
**Matching domain module:** `crm-learning-and-courses`  
**Application:** CRM  
**Source feature:** [Crm Learning And Courses](../features/crm-learning-and-courses.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-learning-and-courses` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Courses:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Lessons:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Media:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cohorts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Enrollment:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Access:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Progress:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Assessments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Certificates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Drip schedules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Product/contract entitlements:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-learning-and-courses-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `courses`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `lessons`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `media`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cohorts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `enrollment`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `access`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `progress`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `assessments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `certificates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `drip-schedules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `product-contract-entitlements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-learning-and-courses` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-learning-and-courses-filament`](https://github.com/liberusoftware/module-crm-learning-and-courses-filament) (`liberusoftware/crm-learning-and-courses-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-learning-and-courses.md) · [API plan](../api/crm-learning-and-courses.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Courses** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `courses`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Lessons** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lessons`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Media** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `media`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cohorts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cohorts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Enrollment** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `enrollment`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Access** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `access`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Progress** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `progress`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Assessments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `assessments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Certificates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `certificates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Drip schedules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `drip schedules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Product/contract entitlements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `product/contract entitlements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [LearningAndCoursesFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses-filament/src/LearningAndCoursesFilamentServiceProvider.php) · [LearningCourseResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses-filament/src/Resources/LearningCourseResource.php) · [CreateLearningCourse.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses-filament/src/Resources/Pages/CreateLearningCourse.php) · [EditLearningCourse.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses-filament/src/Resources/Pages/EditLearningCourse.php) · [ListLearningCourses.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses-filament/src/Resources/Pages/ListLearningCourses.php).

| Observed core query | Public method signatures |
| --- | --- |
| [LearningQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Queries/LearningQuery.php) | `public function forTeam(int $teamId)`<br>`public function records(int $teamId, int $enrollmentId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCourse.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Actions/CreateCourse.php) | `public function __construct(private readonly LearningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): LearningCourse` |
| [EnrollLearner.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Actions/EnrollLearner.php) | `public function __construct(private readonly LearningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, LearningCourse $course, array $input): LearningEnrollment` |
| [RecordLearningProgress.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Actions/RecordLearningProgress.php) | `public function __construct(private readonly LearningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, LearningEnrollment $enrollment, array $input): LearningRecord` |
| [LearningPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Services/LearningPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [LearningCourse.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Models/LearningCourse.php) | No literal fillable array detected; inspect the model and API schema. |
| [LearningEnrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Models/LearningEnrollment.php) | No literal fillable array detected; inspect the model and API schema. |
| [LearningLesson.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Models/LearningLesson.php) | No literal fillable array detected; inspect the model and API schema. |
| [LearningRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses/src/Models/LearningRecord.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
