# CRM: Affiliate Management Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#affiliate-management). Observed identity: [`liberusoftware/module-crm-affiliate-management-livewire`](../../../modules/source/liberusoftware--module-crm-affiliate-management-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-affiliate-management-livewire`  
**Matching domain module:** `crm-affiliate-management`  
**Application:** CRM  
**Source feature:** [Affiliate Management](../features/affiliate-management.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Affiliates and partner profiles:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Applications and onboarding approval:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Links, promo codes, and campaigns:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Clicks and first-party touch attribution:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Conversions and cross-product clawback ledger:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Commission rules and tiered calculation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Payout approvals/exports via PayoutSettlementContract:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Disputes, fraud controls, assets, and partner portal:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-affiliate-management-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-affiliate-management::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `affiliates-and-partner-profiles`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `applications-and-onboarding-approval`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `links-promo-codes-and-campaigns`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `clicks-and-first-party-touch-attribution`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `conversions-and-cross-product-clawback-ledger`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `commission-rules-and-tiered-calculation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `payout-approvals-exports-via-payoutsettlementcontract`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `disputes-fraud-controls-assets-and-partner-portal`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-affiliate-management` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/affiliate-management.md) · [API plan](../api/affiliate-management.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Affiliates and partner profiles** | Expose a focused Livewire 4 component and namespaced Blade default view for `affiliates and partner profiles` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Applications and onboarding approval** | Expose a focused Livewire 4 component and namespaced Blade default view for `applications and onboarding approval` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Links, promo codes, and campaigns** | Expose a focused Livewire 4 component and namespaced Blade default view for `links, promo codes, and campaigns` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Clicks and first-party touch attribution** | Expose a focused Livewire 4 component and namespaced Blade default view for `clicks and first-party touch attribution` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Conversions and cross-product clawback ledger** | Expose a focused Livewire 4 component and namespaced Blade default view for `conversions and cross-product clawback ledger` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Commission rules and tiered calculation** | Expose a focused Livewire 4 component and namespaced Blade default view for `commission rules and tiered calculation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Payout approvals/exports via PayoutSettlementContract** | Expose a focused Livewire 4 component and namespaced Blade default view for `payout approvals/exports via payoutsettlementcontract` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Disputes, fraud controls, assets, and partner portal** | Expose a focused Livewire 4 component and namespaced Blade default view for `disputes, fraud controls, assets, and partner portal` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [AffiliateManagementLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management-livewire/src/AffiliateManagementLivewireServiceProvider.php) · [AffiliateBrowser.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management-livewire/src/Components/AffiliateBrowser.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AffiliateQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Queries/AffiliateQuery.php) | `public function affiliates(int $teamId): Builder`<br>`public function events(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApplyAffiliate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/ApplyAffiliate.php) | `public function execute(int $teamId, array $input): Affiliate` |
| [ApproveAffiliate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/ApproveAffiliate.php) | `public function execute(int $teamId, Affiliate $affiliate): Affiliate` |
| [ApproveAffiliatePayout.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/ApproveAffiliatePayout.php) | `public function execute(int $teamId, int $actorId, AffiliatePayout $payout): AffiliatePayout` |
| [CreateAffiliateLink.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/CreateAffiliateLink.php) | `public function execute(int $teamId, Affiliate $affiliate, array $input): AffiliateLink` |
| [RecordAffiliateEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/RecordAffiliateEvent.php) | `public function execute(int $teamId, AffiliateLink $link, array $input): AffiliateEvent` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Affiliate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Models/Affiliate.php) | No literal fillable array detected; inspect the model and API schema. |
| [AffiliateEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Models/AffiliateEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [AffiliateLink.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Models/AffiliateLink.php) | No literal fillable array detected; inspect the model and API schema. |
| [AffiliatePayout.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Models/AffiliatePayout.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
