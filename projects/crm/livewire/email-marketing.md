# CRM: Email Marketing Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#email-marketing). Observed identity: [`liberusoftware/module-crm-email-marketing-livewire`](../../../modules/source/liberusoftware--module-crm-email-marketing-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-email-marketing-livewire`  
**Matching domain module:** `crm-email-marketing`  
**Application:** CRM  
**Source feature:** [Email Marketing](../features/email-marketing.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Drag-and-drop and code templates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Personalization:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Dynamic content:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Test sends:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Inbox previews:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Deliverability controls:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Scheduling:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Throttling:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Analytics:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-email-marketing-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-email-marketing::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `drag-and-drop-and-code-templates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `personalization`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `dynamic-content`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `test-sends`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `inbox-previews`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `deliverability-controls`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `scheduling`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `throttling`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `analytics`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-email-marketing` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/email-marketing.md) · [API plan](../api/email-marketing.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Drag-and-drop and code templates** | Expose a focused Livewire 4 component and namespaced Blade default view for `drag-and-drop and code templates` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Personalization** | Expose a focused Livewire 4 component and namespaced Blade default view for `personalization` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Dynamic content** | Expose a focused Livewire 4 component and namespaced Blade default view for `dynamic content` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Test sends** | Expose a focused Livewire 4 component and namespaced Blade default view for `test sends` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Inbox previews** | Expose a focused Livewire 4 component and namespaced Blade default view for `inbox previews` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Deliverability controls** | Expose a focused Livewire 4 component and namespaced Blade default view for `deliverability controls` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Scheduling** | Expose a focused Livewire 4 component and namespaced Blade default view for `scheduling` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Throttling** | Expose a focused Livewire 4 component and namespaced Blade default view for `throttling` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Analytics** | Expose a focused Livewire 4 component and namespaced Blade default view for `analytics` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CampaignDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing-livewire/src/Livewire/CampaignDashboard.php) · [EmailMarketingLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing-livewire/src/EmailMarketingLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [EmailMarketingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Queries/EmailMarketingQuery.php) | `public function campaigns(int $teamId)`<br>`public function analytics(int $teamId, int $campaignId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateEmailCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Actions/CreateEmailCampaign.php) | `public function __construct(private readonly EmailMarketingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): EmailCampaign` |
| [RecordMarketingEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Actions/RecordMarketingEvent.php) | `public function execute(int $teamId, EmailCampaign $campaign, array $input): EmailMarketingEvent` |
| [ScheduleCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Actions/ScheduleCampaign.php) | `public function __construct(private readonly EmailMarketingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, EmailCampaign $campaign, array $input): EmailCampaign` |
| [EmailMarketingPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Services/EmailMarketingPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EmailCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Models/EmailCampaign.php) | No literal fillable array detected; inspect the model and API schema. |
| [EmailDelivery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Models/EmailDelivery.php) | No literal fillable array detected; inspect the model and API schema. |
| [EmailMarketingEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Models/EmailMarketingEvent.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
