# CRM: Channel Sales Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#channel-sales). Observed identity: [`liberusoftware/module-crm-channel-sales-livewire`](../../../modules/source/liberusoftware--module-crm-channel-sales-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-channel-sales-livewire`  
**Matching domain module:** `crm-channel-sales`  
**Application:** CRM  
**Source feature:** [Channel Sales](../features/channel-sales.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Partner opportunities:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Shared pipelines:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Referrals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reseller pricing references:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Quotes/orders handoff:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Commissions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Forecasts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Partner portal:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-channel-sales-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-channel-sales::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `partner-opportunities`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `shared-pipelines`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `referrals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reseller-pricing-references`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `quotes-orders-handoff`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `commissions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `forecasts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `partner-portal`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-channel-sales` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/channel-sales.md) · [API plan](../api/channel-sales.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Partner opportunities** | Expose a focused Livewire 4 component and namespaced Blade default view for `partner opportunities` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Shared pipelines** | Expose a focused Livewire 4 component and namespaced Blade default view for `shared pipelines` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Referrals** | Expose a focused Livewire 4 component and namespaced Blade default view for `referrals` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reseller pricing references** | Expose a focused Livewire 4 component and namespaced Blade default view for `reseller pricing references` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Quotes/orders handoff** | Expose a focused Livewire 4 component and namespaced Blade default view for `quotes/orders handoff` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Commissions** | Expose a focused Livewire 4 component and namespaced Blade default view for `commissions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Forecasts** | Expose a focused Livewire 4 component and namespaced Blade default view for `forecasts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Partner portal** | Expose a focused Livewire 4 component and namespaced Blade default view for `partner portal` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ChannelSalesLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales-livewire/src/ChannelSalesLivewireServiceProvider.php) · [OpportunityBrowser.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales-livewire/src/Components/OpportunityBrowser.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ChannelSalesQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales/src/Queries/ChannelSalesQuery.php) | `public function opportunities(int $teamId): Builder`<br>`public function forecast(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AdvanceChannelOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales/src/Actions/AdvanceChannelOpportunity.php) | `public function execute(int $teamId, int $actorId, ChannelOpportunity $opportunity, string $stage, string $handoffStatus = 'pending'): ChannelEvent` |
| [RegisterChannelOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales/src/Actions/RegisterChannelOpportunity.php) | `public function execute(int $teamId, int $ownerId, string $partnerKey, string $opportunityKey, float $amount, float $commissionRate, array $pricingReference = []): ChannelOpportunity` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ChannelEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales/src/Models/ChannelEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ChannelOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales/src/Models/ChannelOpportunity.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
