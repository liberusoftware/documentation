# CRM: Email Productivity Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#email-productivity). Observed identity: [`liberusoftware/module-crm-email-productivity-livewire`](../../../modules/source/liberusoftware--module-crm-email-productivity-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-email-productivity-livewire`  
**Matching domain module:** `crm-email-productivity`  
**Application:** CRM  
**Source feature:** [Email Productivity](../features/email-productivity.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Mailbox sync:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Send/log:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Templates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Snippets:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Scheduling:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Open/click/reply tracking policy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Shared/team inbox:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Signatures:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Sidebars:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Gmail/Outlook adapters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-email-productivity-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-email-productivity::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `mailbox-sync`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `send-log`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `templates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `snippets`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `scheduling`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `open-click-reply-tracking-policy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `shared-team-inbox`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `signatures`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sidebars`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `gmail-outlook-adapters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-email-productivity` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/email-productivity.md) · [API plan](../api/email-productivity.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Mailbox sync** | Expose a focused Livewire 4 component and namespaced Blade default view for `mailbox sync` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Send/log** | Expose a focused Livewire 4 component and namespaced Blade default view for `send/log` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Templates** | Expose a focused Livewire 4 component and namespaced Blade default view for `templates` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Snippets** | Expose a focused Livewire 4 component and namespaced Blade default view for `snippets` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Scheduling** | Expose a focused Livewire 4 component and namespaced Blade default view for `scheduling` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Open/click/reply tracking policy** | Expose a focused Livewire 4 component and namespaced Blade default view for `open/click/reply tracking policy` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Shared/team inbox** | Expose a focused Livewire 4 component and namespaced Blade default view for `shared/team inbox` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Signatures** | Expose a focused Livewire 4 component and namespaced Blade default view for `signatures` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Sidebars** | Expose a focused Livewire 4 component and namespaced Blade default view for `sidebars` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Gmail/Outlook adapters** | Expose a focused Livewire 4 component and namespaced Blade default view for `gmail/outlook adapters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [EmailDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity-livewire/src/Livewire/EmailDashboard.php) · [EmailProductivityLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity-livewire/src/EmailProductivityLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [EmailProductivityQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Queries/EmailProductivityQuery.php) | `public function mailboxes(int $teamId)`<br>`public function templates(int $teamId)`<br>`public function messages(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConnectMailbox.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Actions/ConnectMailbox.php) | `public function __construct(private readonly EmailProductivityPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): EmailMailbox` |
| [CreateEmailTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Actions/CreateEmailTemplate.php) | `public function __construct(private readonly EmailProductivityPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): EmailTemplate` |
| [RecordEmailEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Actions/RecordEmailEvent.php) | `public function execute(int $teamId, EmailMessage $message, array $input): EmailEvent` |
| [SendEmail.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Actions/SendEmail.php) | `public function __construct(private readonly EmailProductivityPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): EmailMessage` |
| [EmailProductivityPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Services/EmailProductivityPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EmailEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Models/EmailEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [EmailMailbox.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Models/EmailMailbox.php) | No literal fillable array detected; inspect the model and API schema. |
| [EmailMessage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Models/EmailMessage.php) | No literal fillable array detected; inspect the model and API schema. |
| [EmailTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Models/EmailTemplate.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
