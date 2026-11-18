# CRM: Crm Forms And Surveys Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-forms-and-surveys). Observed identity: [`liberusoftware/module-crm-forms-and-surveys-livewire`](../../../modules/source/liberusoftware--module-crm-forms-and-surveys-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-forms-and-surveys-livewire`  
**Matching domain module:** `crm-forms-and-surveys`  
**Application:** CRM  
**Source feature:** [Crm Forms And Surveys](../features/crm-forms-and-surveys.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Drag-and-drop schemas:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Conditional fields:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Progressive profiling:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Validation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Spam controls:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Consent:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Hidden attribution:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Embedding:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Submissions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Follow-up:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-forms-and-surveys-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmFormsAndSurveys::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `drag-and-drop-schemas`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `conditional-fields`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `progressive-profiling`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `validation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `spam-controls`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `consent`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `hidden-attribution`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `embedding`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `submissions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `follow-up`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-forms-and-surveys` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-forms-and-surveys.md) · [API plan](../api/crm-forms-and-surveys.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Drag-and-drop schemas** | Expose a focused Livewire 4 component and namespaced Blade default view for `drag-and-drop schemas` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Conditional fields** | Expose a focused Livewire 4 component and namespaced Blade default view for `conditional fields` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Progressive profiling** | Expose a focused Livewire 4 component and namespaced Blade default view for `progressive profiling` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Validation** | Expose a focused Livewire 4 component and namespaced Blade default view for `validation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Spam controls** | Expose a focused Livewire 4 component and namespaced Blade default view for `spam controls` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Consent** | Expose a focused Livewire 4 component and namespaced Blade default view for `consent` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Hidden attribution** | Expose a focused Livewire 4 component and namespaced Blade default view for `hidden attribution` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Embedding** | Expose a focused Livewire 4 component and namespaced Blade default view for `embedding` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Submissions** | Expose a focused Livewire 4 component and namespaced Blade default view for `submissions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Follow-up** | Expose a focused Livewire 4 component and namespaced Blade default view for `follow-up` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [FormDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys-livewire/src/Components/FormDashboard.php) · [FormsAndSurveysLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys-livewire/src/FormsAndSurveysLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [FormQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Queries/FormQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateSurveyForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Actions/CreateSurveyForm.php) | `public function __construct(private readonly FormPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): SurveyForm` |
| [RecordFollowUp.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Actions/RecordFollowUp.php) | `public function __construct(private readonly FormPolicy $policy)`<br>`public function execute(int $teamId, int $userId, FormSubmission $submission, array $input): FormFollowUp` |
| [SubmitForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Actions/SubmitForm.php) | `public function __construct(private readonly FormPolicy $policy)`<br>`public function execute(int $teamId, int $userId, SurveyForm $form, array $input): FormSubmission` |
| [FormPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Services/FormPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FormFollowUp.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Models/FormFollowUp.php) | No literal fillable array detected; inspect the model and API schema. |
| [FormSubmission.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Models/FormSubmission.php) | No literal fillable array detected; inspect the model and API schema. |
| [SurveyForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forms-and-surveys/src/Models/SurveyForm.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
