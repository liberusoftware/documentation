# CMS: Cms Polls And Surveys Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-polls-and-surveys). Observed identity: [`liberusoftware/module-cms-polls-and-surveys-livewire`](../../../modules/source/liberusoftware--module-cms-polls-and-surveys-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-cms-polls-and-surveys-livewire`  
**Matching domain module:** `cms-polls-and-surveys`  
**Application:** CMS  
**Source feature:** [Cms Polls And Surveys](../features/cms-polls-and-surveys.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Questions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Branching:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Anonymous/authenticated response policy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Schedules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Results:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Exports:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Privacy controls:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-cms-polls-and-surveys-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsCmsPollsAndSurveys::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `questions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `branching`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `anonymous-authenticated-response-policy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `schedules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `results`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `exports`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `privacy-controls`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-polls-and-surveys` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/cms-polls-and-surveys.md) · [API plan](../api/cms-polls-and-surveys.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Questions** | Expose a focused Livewire 4 component and namespaced Blade default view for `questions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Branching** | Expose a focused Livewire 4 component and namespaced Blade default view for `branching` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Anonymous/authenticated response policy** | Expose a focused Livewire 4 component and namespaced Blade default view for `anonymous/authenticated response policy` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Schedules** | Expose a focused Livewire 4 component and namespaced Blade default view for `schedules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Results** | Expose a focused Livewire 4 component and namespaced Blade default view for `results` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Exports** | Expose a focused Livewire 4 component and namespaced Blade default view for `exports` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Privacy controls** | Expose a focused Livewire 4 component and namespaced Blade default view for `privacy controls` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [PollForm.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-polls-and-surveys-livewire/src/Livewire/PollForm.php) · [PollsAndSurveysLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-polls-and-surveys-livewire/src/PollsAndSurveysLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [PollService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-polls-and-surveys/src/Services/PollService.php) | `public function create(array $attributes, ?int $teamId = null): Poll`<br>`public function update(Poll $poll, array $attributes): Poll`<br>`public function saveQuestion(Poll $poll, array $attributes, ?Question $question = null): Question`<br>`public function deleteQuestion(Question $question): void`<br>`public function submit(Poll $poll, array $answers, ?int $userId = null, ?string $respondentKey = null): Response`<br>`public function results(Poll $poll): array`<br>`public function export(Poll $poll, bool $includeRespondentIdentity = false): array`<br>`public function eraseResponse(Response $response): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Poll.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-polls-and-surveys/src/Models/Poll.php) | `title`, `key`, `description`, `starts_at`, `ends_at`, `allow_anonymous`, `allow_multiple`, `active`, `results_public`, `team_id` |
| [Question.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-polls-and-surveys/src/Models/Question.php) | `poll_id`, `key`, `type`, `prompt`, `options`, `branching`, `position`, `required` |
| [Response.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-polls-and-surveys/src/Models/Response.php) | `poll_id`, `user_id`, `respondent_hash`, `answers`, `submitted_at`, `team_id` |
<!-- layer-implementation-plan:end -->
