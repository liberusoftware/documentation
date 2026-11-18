# CRM: Crm Learning And Courses Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-learning-and-courses). Observed identity: [`liberusoftware/module-crm-learning-and-courses-livewire`](../../../modules/source/liberusoftware--module-crm-learning-and-courses-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-learning-and-courses-livewire`  
**Matching domain module:** `crm-learning-and-courses`  
**Application:** CRM  
**Source feature:** [Crm Learning And Courses](../features/crm-learning-and-courses.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Courses:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Lessons:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Media:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cohorts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Enrollment:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Access:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Progress:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Assessments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Certificates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Drip schedules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Product/contract entitlements:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-learning-and-courses-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmLearningAndCourses::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `courses`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `lessons`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `media`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cohorts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `enrollment`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `access`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `progress`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `assessments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `certificates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `drip-schedules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `product-contract-entitlements`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-learning-and-courses` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-learning-and-courses.md) · [API plan](../api/crm-learning-and-courses.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Courses** | Expose a focused Livewire 4 component and namespaced Blade default view for `courses` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Lessons** | Expose a focused Livewire 4 component and namespaced Blade default view for `lessons` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Media** | Expose a focused Livewire 4 component and namespaced Blade default view for `media` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cohorts** | Expose a focused Livewire 4 component and namespaced Blade default view for `cohorts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Enrollment** | Expose a focused Livewire 4 component and namespaced Blade default view for `enrollment` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Access** | Expose a focused Livewire 4 component and namespaced Blade default view for `access` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Progress** | Expose a focused Livewire 4 component and namespaced Blade default view for `progress` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Assessments** | Expose a focused Livewire 4 component and namespaced Blade default view for `assessments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Certificates** | Expose a focused Livewire 4 component and namespaced Blade default view for `certificates` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Drip schedules** | Expose a focused Livewire 4 component and namespaced Blade default view for `drip schedules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Product/contract entitlements** | Expose a focused Livewire 4 component and namespaced Blade default view for `product/contract entitlements` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [LearningPortal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses-livewire/src/Components/LearningPortal.php) · [LearningAndCoursesLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-learning-and-courses-livewire/src/LearningAndCoursesLivewireServiceProvider.php).

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
