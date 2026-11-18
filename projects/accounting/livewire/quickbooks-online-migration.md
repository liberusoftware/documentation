# Accounting: QuickBooks Online Migration Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#quickbooks-online-migration). Observed identity: [`liberusoftware/module-accounting-quickbooks-online-migration-livewire`](../../../modules/source/liberusoftware--module-accounting-quickbooks-online-migration-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-quickbooks-online-migration-livewire`  
**Matching domain module:** `accounting-quickbooks-online-migration`  
**Application:** Accounting  
**Source feature:** [QuickBooks Online Migration](../features/quickbooks-online-migration.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Chart:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Classes/locations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Contacts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Items:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Invoices/bills/credits/payments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Journals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Bank data:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Projects:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Tax:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Attachments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Source IDs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-quickbooks-online-migration-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-quickbooks-online-migration::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `chart`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `classes-locations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `contacts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `items`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `invoices-bills-credits-payments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `journals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `bank-data`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `projects`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `tax`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `attachments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `source-ids`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-quickbooks-online-migration` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/quickbooks-online-migration.md) · [API plan](../api/quickbooks-online-migration.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Chart** | Expose a focused Livewire 4 component and namespaced Blade default view for `chart` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Classes/locations** | Expose a focused Livewire 4 component and namespaced Blade default view for `classes/locations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Contacts** | Expose a focused Livewire 4 component and namespaced Blade default view for `contacts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Items** | Expose a focused Livewire 4 component and namespaced Blade default view for `items` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Invoices/bills/credits/payments** | Expose a focused Livewire 4 component and namespaced Blade default view for `invoices/bills/credits/payments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Journals** | Expose a focused Livewire 4 component and namespaced Blade default view for `journals` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Bank data** | Expose a focused Livewire 4 component and namespaced Blade default view for `bank data` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Projects** | Expose a focused Livewire 4 component and namespaced Blade default view for `projects` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Tax** | Expose a focused Livewire 4 component and namespaced Blade default view for `tax` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Attachments** | Expose a focused Livewire 4 component and namespaced Blade default view for `attachments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Source IDs** | Expose a focused Livewire 4 component and namespaced Blade default view for `source ids` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [QuickBooksOnlineMigrationLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration-livewire/src/QuickBooksOnlineMigrationLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateMigrationRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Actions/CreateMigrationRun.php) | `public function handle(?int $connectionId, array $metadata = []): QboMigrationRun` |
| [ImportMigrationRecords.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Actions/ImportMigrationRecords.php) | `public function handle(QboMigrationRun $run, array $records): QboMigrationRun` |
| [ReconcileMigration.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Actions/ReconcileMigration.php) | `public function handle(QboMigrationRun $run): QboMigrationRun` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [QboMigrationConnection.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Models/QboMigrationConnection.php) | `team_id`, `realm_id`, `access_token`, `refresh_token`, `token_expires_at`, `status`, `last_synced_at` |
| [QboMigrationRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Models/QboMigrationRecord.php) | `run_id`, `entity_type`, `source_id`, `status`, `payload`, `payload_hash`, `error_message`, `metadata` |
| [QboMigrationRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Models/QboMigrationRun.php) | `connection_id`, `status`, `total_records`, `imported_records`, `failed_records`, `errors`, `metadata`, `started_at`, `finished_at` |
<!-- layer-implementation-plan:end -->
