# Billing: Customer Portal Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#customer-portal). Observed identity: [`liberusoftware/module-billing-customer-portal-livewire`](../../../modules/source/liberusoftware--module-billing-customer-portal-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-billing-customer-portal-livewire`  
**Matching domain module:** `billing-customer-portal`  
**Application:** Billing  
**Source feature:** [Customer Portal](../features/customer-portal.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Profile:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Orders:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Services:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Usage:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Invoices:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Payments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Tickets:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Changes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cancellation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-billing-customer-portal-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-billing-customer-portal::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `profile`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `orders`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `services`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `usage`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `invoices`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `payments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `tickets`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `changes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cancellation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `billing-customer-portal` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/customer-portal.md) · [API plan](../api/customer-portal.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Profile** | Expose a focused Livewire 4 component and namespaced Blade default view for `profile` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Orders** | Expose a focused Livewire 4 component and namespaced Blade default view for `orders` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Services** | Expose a focused Livewire 4 component and namespaced Blade default view for `services` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Usage** | Expose a focused Livewire 4 component and namespaced Blade default view for `usage` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Invoices** | Expose a focused Livewire 4 component and namespaced Blade default view for `invoices` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Payments** | Expose a focused Livewire 4 component and namespaced Blade default view for `payments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Tickets** | Expose a focused Livewire 4 component and namespaced Blade default view for `tickets` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Changes** | Expose a focused Livewire 4 component and namespaced Blade default view for `changes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cancellation** | Expose a focused Livewire 4 component and namespaced Blade default view for `cancellation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [PortalBilling.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-livewire/src/Components/PortalBilling.php) · [PortalDashboard.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-livewire/src/Components/PortalDashboard.php) · [PortalItems.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-livewire/src/Components/PortalItems.php) · [PortalRequests.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-livewire/src/Components/PortalRequests.php) · [CustomerPortalLivewireServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-livewire/src/CustomerPortalLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [GetCustomerBillingSummary.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Queries/GetCustomerBillingSummary.php) | `public function __construct(private DatabaseManager $database)`<br>`public function handle(int $teamId, int $customerId, ?CarbonInterface $startAt = null, ?CarbonInterface $endAt = null): array` |
| [ListCustomerPortalRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Queries/ListCustomerPortalRecords.php) | `public function handle(int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ListPortalItems.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Queries/ListPortalItems.php) | `public function handle(int $teamId, ?string $type = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePortalItem.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Actions/CreatePortalItem.php) | `public function handle(int $teamId, array $attributes): PortalItem` |
| [CreatePortalRequest.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Actions/CreatePortalRequest.php) | `public function handle(int $teamId, array $attributes): PortalRequest` |
| [TransitionPortalItem.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Actions/TransitionPortalItem.php) | `public function handle(PortalItem $item, string $status): PortalItem` |
| [TransitionPortalRequest.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Actions/TransitionPortalRequest.php) | `public function handle(PortalRequest $request, string $status): PortalRequest` |
| [PortalItemPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Policies/PortalItemPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function update(?object $user, object $item): bool`<br>`public function view(?object $user, object $item): bool` |
| [PortalRequestPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Policies/PortalRequestPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, PortalRequest $record): bool`<br>`public function update(?Authenticatable $user, PortalRequest $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PortalItem.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Models/PortalItem.php) | No literal fillable array detected; inspect the model and API schema. |
| [PortalRequest.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Models/PortalRequest.php) | No literal fillable array detected; inspect the model and API schema. |
| [Customer.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-api/src/Models/Customer.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
