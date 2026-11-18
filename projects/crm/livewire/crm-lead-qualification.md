# CRM: Crm Lead Qualification Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-lead-qualification). Observed identity: [`liberusoftware/module-crm-lead-qualification-livewire`](../../../modules/source/liberusoftware--module-crm-lead-qualification-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-lead-qualification-livewire`  
**Matching domain module:** `crm-lead-qualification`  
**Application:** CRM  
**Source feature:** [Crm Lead Qualification](../features/crm-lead-qualification.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Lifecycle stages:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Fit/engagement scoring:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **MQL/PQL/SQL/service-qualified rules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Qualification frameworks:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Disqualification:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Nurture:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Conversion:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-lead-qualification-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmLeadQualification::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `lifecycle-stages`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `fit-engagement-scoring`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `mql-pql-sql-service-qualified-rules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `qualification-frameworks`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `disqualification`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `nurture`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `conversion`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-lead-qualification` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-lead-qualification.md) · [API plan](../api/crm-lead-qualification.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Lifecycle stages** | Expose a focused Livewire 4 component and namespaced Blade default view for `lifecycle stages` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Fit/engagement scoring** | Expose a focused Livewire 4 component and namespaced Blade default view for `fit/engagement scoring` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **MQL/PQL/SQL/service-qualified rules** | Expose a focused Livewire 4 component and namespaced Blade default view for `mql/pql/sql/service-qualified rules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Qualification frameworks** | Expose a focused Livewire 4 component and namespaced Blade default view for `qualification frameworks` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Disqualification** | Expose a focused Livewire 4 component and namespaced Blade default view for `disqualification` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Nurture** | Expose a focused Livewire 4 component and namespaced Blade default view for `nurture` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Conversion** | Expose a focused Livewire 4 component and namespaced Blade default view for `conversion` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [QualificationBrowser.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification-livewire/src/Components/QualificationBrowser.php) · [QualificationDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification-livewire/src/Components/QualificationDashboard.php) · [QualificationForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification-livewire/src/Components/QualificationForm.php) · [LeadQualificationLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification-livewire/src/LeadQualificationLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [LeadQualificationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Queries/LeadQualificationQuery.php) | `public function forTeam(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConvertQualification.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/ConvertQualification.php) | `public function execute(LeadQualification $qualification, ?int $actorId, ?string $reason = null): LeadQualification` |
| [CreateFramework.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/CreateFramework.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): QualificationFramework` |
| [CreateQualification.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/CreateQualification.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): LeadQualification` |
| [DisqualifyQualification.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/DisqualifyQualification.php) | `public function execute(LeadQualification $qualification, ?int $actorId, string $reason): LeadQualification` |
| [EnrollNurture.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/EnrollNurture.php) | `public function execute(LeadQualification $qualification, ?int $actorId, array $attributes): NurtureEnrollment` |
| [EvaluateQualification.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/EvaluateQualification.php) | `public function execute(LeadQualification $qualification, ?int $actorId): LeadQualification` |
| [RecordQualificationEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/RecordQualificationEvent.php) | `public function __construct(private readonly LeadQualificationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, QualifiedLead $lead, array $input): QualificationEvent` |
| [ScoreLead.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/ScoreLead.php) | `public function __construct(private readonly LeadQualificationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, QualifiedLead $lead, array $input): QualifiedLead` |
| [TransitionLifecycle.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/TransitionLifecycle.php) | `public function execute(LeadQualification $qualification, ?int $actorId, string $stage, ?string $reason = null): LeadQualification` |
| [UpdateScores.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/UpdateScores.php) | `public function execute(LeadQualification $qualification, ?int $actorId, array $scores): LeadQualification` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [LeadQualification.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/LeadQualification.php) | `team_id`, `actor_id`, `subject_type`, `subject_id`, `framework_id`, `lifecycle_stage`, `fit_score`, `engagement_score`, `total_score`, `qualification_status`, `disqualification_reason`, `nurture_until`, `converted_at`, `version`, `metadata` |
| [NurtureEnrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/NurtureEnrollment.php) | `team_id`, `qualification_id`, `actor_id`, `status`, `sequence`, `starts_at`, `ends_at`, `metadata` |
| [QualificationEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/QualificationEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [QualificationFramework.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/QualificationFramework.php) | `team_id`, `actor_id`, `name`, `status`, `mql_threshold`, `pql_threshold`, `sql_threshold`, `service_qualified_threshold`, `rules`, `settings` |
| [QualificationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/QualificationRule.php) | No literal fillable array detected; inspect the model and API schema. |
| [QualifiedLead.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/QualifiedLead.php) | No literal fillable array detected; inspect the model and API schema. |
| [StageHistory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/StageHistory.php) | `team_id`, `qualification_id`, `actor_id`, `from_stage`, `to_stage`, `reason` |
<!-- layer-implementation-plan:end -->
