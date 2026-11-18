# CRM: Campaigns Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#campaigns). Observed identity: [`liberusoftware/module-crm-campaigns-livewire`](../../../modules/source/liberusoftware--module-crm-campaigns-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-campaigns-livewire`  
**Matching domain module:** `crm-campaigns`  
**Application:** CRM  
**Source feature:** [Campaigns](../features/campaigns.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Campaign hierarchy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Briefs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Objectives:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Budget:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Assets:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Channels:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Audience:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Owners:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Calendar:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Tasks:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Costs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Responses:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Influence:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **ROI:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-campaigns-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-campaigns::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `campaign-hierarchy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `briefs`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `objectives`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `budget`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `assets`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `channels`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `audience`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `owners`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `calendar`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `tasks`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `costs`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `responses`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `influence`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `roi`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-campaigns` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/campaigns.md) · [API plan](../api/campaigns.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Campaign hierarchy** | Expose a focused Livewire 4 component and namespaced Blade default view for `campaign hierarchy` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Briefs** | Expose a focused Livewire 4 component and namespaced Blade default view for `briefs` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Objectives** | Expose a focused Livewire 4 component and namespaced Blade default view for `objectives` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Budget** | Expose a focused Livewire 4 component and namespaced Blade default view for `budget` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Assets** | Expose a focused Livewire 4 component and namespaced Blade default view for `assets` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Channels** | Expose a focused Livewire 4 component and namespaced Blade default view for `channels` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Audience** | Expose a focused Livewire 4 component and namespaced Blade default view for `audience` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Owners** | Expose a focused Livewire 4 component and namespaced Blade default view for `owners` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Calendar** | Expose a focused Livewire 4 component and namespaced Blade default view for `calendar` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Tasks** | Expose a focused Livewire 4 component and namespaced Blade default view for `tasks` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Costs** | Expose a focused Livewire 4 component and namespaced Blade default view for `costs` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Responses** | Expose a focused Livewire 4 component and namespaced Blade default view for `responses` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Influence** | Expose a focused Livewire 4 component and namespaced Blade default view for `influence` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **ROI** | Expose a focused Livewire 4 component and namespaced Blade default view for `roi` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CampaignsLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns-livewire/src/CampaignsLivewireServiceProvider.php) · [CampaignBrowser.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns-livewire/src/Components/CampaignBrowser.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CampaignQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns/src/Queries/CampaignQuery.php) | `public function campaigns(int $teamId): Builder`<br>`public function roi(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns/src/Actions/CreateCampaign.php) | `public function execute(int $teamId, int $ownerId, array $input): Campaign` |
| [RecordCampaignEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns/src/Actions/RecordCampaignEvent.php) | `public function execute(int $teamId, int $actorId, Campaign $campaign, string $type, float $value = 0, array $payload = []): CampaignEvent` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Campaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns/src/Models/Campaign.php) | No literal fillable array detected; inspect the model and API schema. |
| [CampaignEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns/src/Models/CampaignEvent.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
