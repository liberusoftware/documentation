# Accounting: Bank Feeds Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#bank-feeds). Observed identity: [`liberusoftware/module-accounting-bank-feeds-livewire`](../../../modules/source/liberusoftware--module-accounting-bank-feeds-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-bank-feeds-livewire`  
**Matching domain module:** `accounting-bank-feeds`  
**Application:** Accounting  
**Source feature:** [Bank Feeds](../features/bank-feeds.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Consent/connections:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Institutions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Account mapping:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cursors:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Imports:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Duplicates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Pending/posted state:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Health:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Provider adapters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-bank-feeds-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-bank-feeds::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `consent-connections`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `institutions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `account-mapping`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cursors`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `imports`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `duplicates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `pending-posted-state`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `health`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `provider-adapters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-bank-feeds` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/bank-feeds.md) · [API plan](../api/bank-feeds.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Consent/connections** | Expose a focused Livewire 4 component and namespaced Blade default view for `consent/connections` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Institutions** | Expose a focused Livewire 4 component and namespaced Blade default view for `institutions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Account mapping** | Expose a focused Livewire 4 component and namespaced Blade default view for `account mapping` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cursors** | Expose a focused Livewire 4 component and namespaced Blade default view for `cursors` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Imports** | Expose a focused Livewire 4 component and namespaced Blade default view for `imports` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Duplicates** | Expose a focused Livewire 4 component and namespaced Blade default view for `duplicates` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Pending/posted state** | Expose a focused Livewire 4 component and namespaced Blade default view for `pending/posted state` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Health** | Expose a focused Livewire 4 component and namespaced Blade default view for `health` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Provider adapters** | Expose a focused Livewire 4 component and namespaced Blade default view for `provider adapters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Connections.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds-livewire/src/Livewire/Connections.php) · [BankFeedsLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds-livewire/src/BankFeedsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [BankFeedQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Queries/BankFeedQuery.php) | `public function connections(?int $teamId = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateBankFeedConnection.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/CreateBankFeedConnection.php) | `public function handle(array $attributes): BankFeedConnection` |
| [ImportBankFeedTransactions.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/ImportBankFeedTransactions.php) | `public function handle(BankFeedConnection $connection, array $batch): array` |
| [MapBankFeedAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/MapBankFeedAccount.php) | `public function handle(BankFeedConnection $connection, array $attributes): BankFeedAccountMapping` |
| [SetBankFeedTransactionStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/SetBankFeedTransactionStatus.php) | `public function handle(BankFeedTransaction $transaction, FeedTransactionStatus $status): BankFeedTransaction` |
| [UpdateBankFeedHealth.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/UpdateBankFeedHealth.php) | `public function handle(BankFeedConnection $connection, ?string $error = null): BankFeedConnection` |
| [UpsertBankFeedInstitution.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/UpsertBankFeedInstitution.php) | `public function handle(array $attributes): BankFeedInstitution` |
| [BankFeedAdapter.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Contracts/BankFeedAdapter.php) | `public function fetch(BankFeedConnection $connection): array` |
| [BankFeedsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds-api/src/Policies/BankFeedsPolicy.php) | `public function viewAny(?object $user = null): bool`<br>`public function view(?object $user, object $connection): bool`<br>`public function create(?object $user = null): bool`<br>`public function update(?object $user, object $connection): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BankFeedAccountMapping.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Models/BankFeedAccountMapping.php) | `team_id`, `connection_id`, `bank_account_id`, `external_account_id`, `name`, `currency`, `metadata` |
| [BankFeedConnection.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Models/BankFeedConnection.php) | `team_id`, `user_id`, `institution_id`, `provider`, `name`, `external_reference`, `access_token`, `credentials`, `cursor`, `status`, `last_synced_at`, `last_error`, `last_error_at`, `metadata` |
| [BankFeedInstitution.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Models/BankFeedInstitution.php) | `provider`, `external_id`, `name`, `country`, `logo_url`, `metadata` |
| [BankFeedTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Models/BankFeedTransaction.php) | `team_id`, `connection_id`, `mapping_id`, `external_id`, `transaction_date`, `posted_date`, `description`, `amount`, `currency`, `status`, `category`, `raw_data`, `metadata` |
<!-- layer-implementation-plan:end -->
