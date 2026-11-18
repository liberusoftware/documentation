# CRM: Usage Wallet and Rebilling Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#usage-wallet-and-rebilling). Observed identity: [`liberusoftware/module-crm-usage-wallet-and-rebilling-livewire`](../../../modules/source/liberusoftware--module-crm-usage-wallet-and-rebilling-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-usage-wallet-and-rebilling-livewire`  
**Matching domain module:** `crm-usage-wallet-and-rebilling`  
**Application:** CRM  
**Source feature:** [Usage Wallet and Rebilling](../features/usage-wallet-and-rebilling.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Provider usage imports:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Wallets/credits:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Threshold reloads:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cost/markup rules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Client charges:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Exceptions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reconciliation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Billing/Accounting handoff:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-usage-wallet-and-rebilling-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-usage-wallet-and-rebilling::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `provider-usage-imports`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `wallets-credits`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `threshold-reloads`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cost-markup-rules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `client-charges`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `exceptions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reconciliation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `billing-accounting-handoff`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-usage-wallet-and-rebilling` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/usage-wallet-and-rebilling.md) · [API plan](../api/usage-wallet-and-rebilling.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Provider usage imports** | Expose a focused Livewire 4 component and namespaced Blade default view for `provider usage imports` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Wallets/credits** | Expose a focused Livewire 4 component and namespaced Blade default view for `wallets/credits` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Threshold reloads** | Expose a focused Livewire 4 component and namespaced Blade default view for `threshold reloads` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cost/markup rules** | Expose a focused Livewire 4 component and namespaced Blade default view for `cost/markup rules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Client charges** | Expose a focused Livewire 4 component and namespaced Blade default view for `client charges` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Exceptions** | Expose a focused Livewire 4 component and namespaced Blade default view for `exceptions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reconciliation** | Expose a focused Livewire 4 component and namespaced Blade default view for `reconciliation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Billing/Accounting handoff** | Expose a focused Livewire 4 component and namespaced Blade default view for `billing/accounting handoff` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [UsageWalletDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling-livewire/src/Components/UsageWalletDashboard.php) · [UsageWalletAndRebillingLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling-livewire/src/UsageWalletAndRebillingLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [UsageWalletQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Queries/UsageWalletQuery.php) | `public function wallet(int $teamId): ?UsageWallet`<br>`public function imports(int $teamId)`<br>`public function charges(int $teamId)`<br>`public function summary(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCharge.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Actions/CreateCharge.php) | `public function execute(int $teamId, int $actorId, array $data): UsageCharge` |
| [ImportProviderUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Actions/ImportProviderUsage.php) | `public function execute(int $teamId, int $actorId, array $data): UsageImport` |
| [ResolveUsageException.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Actions/ResolveUsageException.php) | `public function execute(int $teamId, int $actorId, int $exceptionId): void` |
| [UpsertWallet.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Actions/UpsertWallet.php) | `public function execute(int $teamId, int $actorId, array $data): UsageWallet` |
| [UsageAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Services/UsageAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): void` |
| [UsagePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Services/UsagePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [UsageAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Models/UsageAudit.php) | `team_id`, `actor_id`, `event`, `details`, `request_id` |
| [UsageCharge.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Models/UsageCharge.php) | `team_id`, `usage_import_id`, `wallet_id`, `client_reference`, `cost`, `charge`, `currency`, `status` |
| [UsageImport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Models/UsageImport.php) | `team_id`, `provider`, `external_id`, `amount`, `currency`, `status`, `failure_reason`, `payload` |
| [UsageWallet.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-usage-wallet-and-rebilling/src/Models/UsageWallet.php) | `team_id`, `currency`, `balance`, `threshold`, `reload_amount`, `status`, `version` |
<!-- layer-implementation-plan:end -->
