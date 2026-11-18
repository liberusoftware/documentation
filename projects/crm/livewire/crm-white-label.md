# CRM: Crm White Label Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-white-label). Observed identity: [`liberusoftware/module-crm-white-label-livewire`](../../../modules/source/liberusoftware--module-crm-white-label-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-white-label-livewire`  
**Matching domain module:** `crm-white-label`  
**Application:** CRM  
**Source feature:** [Crm White Label](../features/crm-white-label.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Brand/domain/email/application settings:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Theme selection:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Custom client experience:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Provider abstraction:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Safe platform attribution policy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-white-label-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmWhiteLabel::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `brand-domain-email-application-settings`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `theme-selection`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `custom-client-experience`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `provider-abstraction`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `safe-platform-attribution-policy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-white-label` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-white-label.md) · [API plan](../api/crm-white-label.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Brand/domain/email/application settings** | Expose a focused Livewire 4 component and namespaced Blade default view for `brand/domain/email/application settings` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Theme selection** | Expose a focused Livewire 4 component and namespaced Blade default view for `theme selection` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Custom client experience** | Expose a focused Livewire 4 component and namespaced Blade default view for `custom client experience` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Provider abstraction** | Expose a focused Livewire 4 component and namespaced Blade default view for `provider abstraction` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Safe platform attribution policy** | Expose a focused Livewire 4 component and namespaced Blade default view for `safe platform attribution policy` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [WhiteLabelSettings.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label-livewire/src/Components/WhiteLabelSettings.php) · [WhiteLabelLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label-livewire/src/WhiteLabelLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [WhiteLabelSettingsQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label/src/Queries/WhiteLabelSettingsQuery.php) | `public function forTeam(int $teamId): WhiteLabelSettings` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [UpdateWhiteLabelSettings.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label/src/Actions/UpdateWhiteLabelSettings.php) | `public function execute(int $teamId, int $actorId, array $attributes, ?int $expectedVersion = null): WhiteLabelSettings` |
| [WhiteLabelAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label/src/Services/WhiteLabelAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $changes): void` |
| [WhiteLabelPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label/src/Services/WhiteLabelPolicy.php) | `public function canManage(int $teamId, int $actorId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WhiteLabelAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label/src/Models/WhiteLabelAudit.php) | `team_id`, `actor_id`, `event`, `changes`, `request_id` |
| [WhiteLabelSettings.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label/src/Models/WhiteLabelSettings.php) | `team_id`, `brand_name`, `custom_domain`, `theme`, `email_settings`, `application_settings`, `client_experience`, `provider`, `show_platform_attribution`, `version` |
<!-- layer-implementation-plan:end -->
