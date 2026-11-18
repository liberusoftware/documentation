# Accounting: Xero Migration Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#xero-migration). Observed identity: [`liberusoftware/module-accounting-xero-migration-livewire`](../../../modules/source/liberusoftware--module-accounting-xero-migration-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-xero-migration-livewire`  
**Matching domain module:** `accounting-xero-migration`  
**Application:** Accounting  
**Source feature:** [Xero Migration](../features/xero-migration.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Chart/tracking categories:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Contacts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Items:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Invoices/bills/credits/payments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Bank:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Tax:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Assets:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Projects:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Expense claims:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Attachments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Source IDs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-xero-migration-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-xero-migration::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `chart-tracking-categories`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `contacts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `items`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `invoices-bills-credits-payments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `bank`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `tax`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `assets`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `projects`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `expense-claims`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `attachments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `source-ids`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-xero-migration` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/xero-migration.md) · [API plan](../api/xero-migration.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Chart/tracking categories** | Expose a focused Livewire 4 component and namespaced Blade default view for `chart/tracking categories` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Contacts** | Expose a focused Livewire 4 component and namespaced Blade default view for `contacts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Items** | Expose a focused Livewire 4 component and namespaced Blade default view for `items` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Invoices/bills/credits/payments** | Expose a focused Livewire 4 component and namespaced Blade default view for `invoices/bills/credits/payments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Bank** | Expose a focused Livewire 4 component and namespaced Blade default view for `bank` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Tax** | Expose a focused Livewire 4 component and namespaced Blade default view for `tax` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Assets** | Expose a focused Livewire 4 component and namespaced Blade default view for `assets` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Projects** | Expose a focused Livewire 4 component and namespaced Blade default view for `projects` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Expense claims** | Expose a focused Livewire 4 component and namespaced Blade default view for `expense claims` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Attachments** | Expose a focused Livewire 4 component and namespaced Blade default view for `attachments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Source IDs** | Expose a focused Livewire 4 component and namespaced Blade default view for `source ids` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [XeroConnections.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration-livewire/src/Livewire/XeroConnections.php) · [XeroMigrationLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration-livewire/src/XeroMigrationLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConnectXeroTenant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration/src/Actions/ConnectXeroTenant.php) | `public function handle(array $attributes): XeroConnection` |
| [RecordMigration.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration/src/Actions/RecordMigration.php) | `public function handle(XeroConnection $connection, array $attributes): XeroMigrationRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [XeroConnection.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration/src/Models/XeroConnection.php) | `team_id`, `tenant_ref`, `access_token`, `refresh_token`, `token_expires_at`, `status`, `last_synced_at`, `metadata` |
| [XeroMigrationRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration/src/Models/XeroMigrationRecord.php) | `team_id`, `connection_id`, `source_type`, `source_id`, `target_type`, `target_id`, `status`, `error`, `payload` |
<!-- layer-implementation-plan:end -->
