# Genealogy: Research Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#research). Observed identity: [`liberusoftware/module-genealogy-research-livewire`](../../../modules/source/liberusoftware--module-genealogy-research-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-genealogy-research-livewire`  
**Matching domain module:** `genealogy-research`  
**Application:** Genealogy  
**Source feature:** [Research](../features/research.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Questions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Plans:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Tasks:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Logs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Correspondence:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Negative searches:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Findings:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-genealogy-research-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-genealogy-research::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `questions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `plans`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `tasks`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `logs`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `correspondence`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `negative-searches`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `findings`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `genealogy-research` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/research.md) · [API plan](../api/research.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Questions** | Expose a focused Livewire 4 component and namespaced Blade default view for `questions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Plans** | Expose a focused Livewire 4 component and namespaced Blade default view for `plans` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Tasks** | Expose a focused Livewire 4 component and namespaced Blade default view for `tasks` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Logs** | Expose a focused Livewire 4 component and namespaced Blade default view for `logs` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Correspondence** | Expose a focused Livewire 4 component and namespaced Blade default view for `correspondence` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Negative searches** | Expose a focused Livewire 4 component and namespaced Blade default view for `negative searches` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Findings** | Expose a focused Livewire 4 component and namespaced Blade default view for `findings` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ResearchLivewireServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research-livewire/src/ResearchLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateChecklist.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/CreateChecklist.php) | `public function execute(Model $user, string $name, ?ChecklistTemplate $template = null, array $attributes = []): UserChecklist` |
| [CreateResearchEntry.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/CreateResearchEntry.php) | `public function execute(array $attributes): ResearchEntry`<br>`public function validate(array $values): void` |
| [CreateResearchProject.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/CreateResearchProject.php) | `public function execute(array $attributes): ResearchProject`<br>`public function validate(array $values): void` |
| [DeleteResearchEntry.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/DeleteResearchEntry.php) | `public function execute(ResearchEntry $entry): void` |
| [DeleteResearchProject.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/DeleteResearchProject.php) | `public function execute(ResearchProject $project): void` |
| [UpdateResearchEntry.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/UpdateResearchEntry.php) | `public function execute(ResearchEntry $entry, array $attributes): ResearchEntry` |
| [UpdateResearchProject.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Actions/UpdateResearchProject.php) | `public function execute(ResearchProject $project, array $attributes): ResearchProject` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ChecklistTemplate.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Models/ChecklistTemplate.php) | `team_id`, `created_by`, `name`, `description`, `category`, `is_public`, `is_default`, `tags`, `difficulty_level`, `estimated_time` |
| [ChecklistTemplateItem.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Models/ChecklistTemplateItem.php) | `checklist_template_id`, `title`, `description`, `sort_order`, `category`, `is_required`, `estimated_time`, `resources`, `tips` |
| [ResearchEntry.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Models/ResearchEntry.php) | `team_id`, `research_project_id`, `kind`, `title`, `body`, `status`, `due_date`, `completed_at`, `metadata` |
| [ResearchProject.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Models/ResearchProject.php) | `team_id`, `name`, `status`, `metadata` |
| [UserChecklist.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Models/UserChecklist.php) | `team_id`, `user_id`, `checklist_template_id`, `name`, `description`, `subject_type`, `subject_id`, `status`, `started_at`, `completed_at`, `notes`, `priority`, `due_date` |
| [UserChecklistItem.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-research/src/Models/UserChecklistItem.php) | `checklist_id`, `template_item_id`, `title`, `description`, `sort_order`, `is_completed`, `completed_at`, `notes`, `estimated_time`, `actual_time`, `resources`, `tips` |
<!-- layer-implementation-plan:end -->
