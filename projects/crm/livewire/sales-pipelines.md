# CRM: Sales Pipelines Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sales-pipelines). Observed identity: [`liberusoftware/module-crm-sales-pipelines-livewire`](../../../modules/source/liberusoftware--module-crm-sales-pipelines-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-sales-pipelines-livewire`  
**Matching domain module:** `crm-sales-pipelines`  
**Application:** CRM  
**Source feature:** [Sales Pipelines](../features/sales-pipelines.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Multiple pipelines:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Stages:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Opportunities:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Products:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Values:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Probabilities:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Close dates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Competitors:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Dependencies:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Stage history:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Rotting:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Loss reasons:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-sales-pipelines-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-sales-pipelines::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `multiple-pipelines`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `stages`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `opportunities`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `products`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `values`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `probabilities`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `close-dates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `competitors`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `dependencies`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `stage-history`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `rotting`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `loss-reasons`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-sales-pipelines` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

Read the [source-backed sales-pipeline walkthrough](../guides/SALES-PIPELINES.md) for actual actions, routes, permissions, UI behavior and differences from the target design.
