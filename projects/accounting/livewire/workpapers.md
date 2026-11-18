# Accounting: Workpapers Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#workpapers). Observed identity: [`liberusoftware/module-accounting-workpapers-livewire`](../../../modules/source/liberusoftware--module-accounting-workpapers-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-workpapers-livewire`  
**Matching domain module:** `accounting-workpapers`  
**Application:** Accounting  
**Source feature:** [Workpapers](../features/workpapers.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Lead schedules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **References:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Attachments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Procedures:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Conclusions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Preparer/reviewer:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Rollover:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Export:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-workpapers-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-workpapers::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `lead-schedules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `references`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `attachments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `procedures`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `conclusions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `preparer-reviewer`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `rollover`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `export`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-workpapers` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/workpapers.md) · [API plan](../api/workpapers.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Lead schedules** | Expose a focused Livewire 4 component and namespaced Blade default view for `lead schedules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **References** | Expose a focused Livewire 4 component and namespaced Blade default view for `references` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Attachments** | Expose a focused Livewire 4 component and namespaced Blade default view for `attachments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Procedures** | Expose a focused Livewire 4 component and namespaced Blade default view for `procedures` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Conclusions** | Expose a focused Livewire 4 component and namespaced Blade default view for `conclusions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Preparer/reviewer** | Expose a focused Livewire 4 component and namespaced Blade default view for `preparer/reviewer` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Rollover** | Expose a focused Livewire 4 component and namespaced Blade default view for `rollover` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Export** | Expose a focused Livewire 4 component and namespaced Blade default view for `export` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Workpapers.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers-livewire/src/Livewire/Workpapers.php) · [WorkpapersLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers-livewire/src/WorkpapersLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddWorkpaperAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/AddWorkpaperAttachment.php) | `public function handle(Workpaper $workpaper, array $attributes): WorkpaperAttachment` |
| [AddWorkpaperProcedure.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/AddWorkpaperProcedure.php) | `public function handle(Workpaper $workpaper, array $attributes): WorkpaperProcedure` |
| [AddWorkpaperReference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/AddWorkpaperReference.php) | `public function handle(Workpaper $workpaper, array $attributes): WorkpaperReference` |
| [AssignWorkpaperReviewer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/AssignWorkpaperReviewer.php) | `public function handle(Workpaper $workpaper, int $reviewerId): Workpaper` |
| [ConcludeWorkpaper.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/ConcludeWorkpaper.php) | `public function handle(Workpaper $workpaper, string $conclusion): Workpaper` |
| [CreateWorkpaper.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/CreateWorkpaper.php) | `public function handle(array $attributes): Workpaper` |
| [RequestWorkpaperExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/RequestWorkpaperExport.php) | `public function handle(Workpaper $workpaper, string $format): WorkpaperExport` |
| [RolloverWorkpaper.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/RolloverWorkpaper.php) | `public function handle(Workpaper $source, array $attributes = []): Workpaper` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Workpaper.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/Workpaper.php) | `team_id`, `title`, `reference`, `status`, `period_start`, `period_end`, `preparer_id`, `reviewer_id`, `conclusion`, `metadata` |
| [WorkpaperAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/WorkpaperAttachment.php) | `workpaper_id`, `name`, `disk`, `path`, `mime_type`, `size` |
| [WorkpaperExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/WorkpaperExport.php) | `workpaper_id`, `format`, `status`, `path`, `error` |
| [WorkpaperProcedure.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/WorkpaperProcedure.php) | `workpaper_id`, `description`, `status`, `performed_by`, `performed_at`, `evidence` |
| [WorkpaperReference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/WorkpaperReference.php) | `workpaper_id`, `label`, `target_type`, `target_id`, `notes` |
<!-- layer-implementation-plan:end -->
