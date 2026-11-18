# Billing: Module Billing Billing Core Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-billing-core). Observed identity: [`liberusoftware/module-billing-core-livewire`](../../../modules/source/liberusoftware--module-billing-core-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-billing-module-billing-billing-core-livewire`  
**Matching domain module:** `module-billing-billing-core`  
**Application:** Billing  
**Source feature:** [Module Billing Billing Core](../features/module-billing-billing-core.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Accounts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Contacts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Currencies:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Tax profiles:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Sequences:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Terms:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Billing settings:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-billing-module-billing-billing-core-livewire` component namespace and service provider; use explicit aliases such as `<livewire:billingModuleBillingBillingCore::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `accounts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `contacts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `currencies`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `tax-profiles`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sequences`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `terms`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `billing-settings`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-billing-billing-core` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-billing-billing-core.md) · [API plan](../api/module-billing-billing-core.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Accounts** | Expose a focused Livewire 4 component and namespaced Blade default view for `accounts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Contacts** | Expose a focused Livewire 4 component and namespaced Blade default view for `contacts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Currencies** | Expose a focused Livewire 4 component and namespaced Blade default view for `currencies` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Tax profiles** | Expose a focused Livewire 4 component and namespaced Blade default view for `tax profiles` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Sequences** | Expose a focused Livewire 4 component and namespaced Blade default view for `sequences` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Terms** | Expose a focused Livewire 4 component and namespaced Blade default view for `terms` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Billing settings** | Expose a focused Livewire 4 component and namespaced Blade default view for `billing settings` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [BillingCoreLivewireServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-livewire/src/BillingCoreLivewireServiceProvider.php) · [BillingAccounts.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-livewire/src/Components/BillingAccounts.php) · [BillingCoreRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-livewire/src/Components/BillingCoreRecords.php) · [CurrencyConverter.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-livewire/src/Components/CurrencyConverter.php) · [TaxCalculator.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-livewire/src/Components/TaxCalculator.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListBillingAccounts.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Queries/ListBillingAccounts.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ListBillingRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Queries/ListBillingRecords.php) | `public function execute(string $modelClass, ?int $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CalculateTax.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/CalculateTax.php) | `public function execute(int $teamId, float $amount, ?string $jurisdiction = null, ?int $customerId = null): array` |
| [ConvertCurrency.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/ConvertCurrency.php) | `public function execute(int $teamId, float $amount, string $from, string $to): array` |
| [CreateBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/CreateBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): BillingAccount` |
| [CreateBillingRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/CreateBillingRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(string $modelClass, array $attributes): Model` |
| [DeleteBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/DeleteBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(BillingAccount $account): void` |
| [DeleteBillingRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/DeleteBillingRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Model $record, string $recordType): void` |
| [TransitionBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/TransitionBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(BillingAccount $account, BillingAccountStatus $status): BillingAccount` |
| [UpdateBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/UpdateBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(BillingAccount $account, array $attributes): BillingAccount` |
| [UpdateBillingRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/UpdateBillingRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Model $record, array $attributes): Model` |
| [BillingAccountPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Policies/BillingAccountPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, BillingAccount $account): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, BillingAccount $account): bool`<br>`public function delete(object $user, BillingAccount $account): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingAccount.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingContact.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingContact.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingCurrency.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingCurrency.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingSequence.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingSequence.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingSetting.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingSetting.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingTaxExemption.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingTaxExemption.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingTaxProfile.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingTaxProfile.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingTerm.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingTerm.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
