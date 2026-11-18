# Liberu: Revenue and Care Orchestration Core

**Existing cross-project implementations:** the [platform reuse guide](../REUSE.md) identifies the observed prefixed/unprefixed package families, namespaces, tables and adoption constraints. This scope is their composition/design home; it does not require a third independent implementation.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#revenue-and-care-orchestration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** `module-liberu-revenue-and-care-orchestration`
**Feature:** [Revenue and Care Orchestration](../features/revenue-and-care-orchestration.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

## Contract

Own the health-signal projection, care-risk decision, contact-protection decision, recovery handoff, AI approval envelope, and operational read models. Consume only public contracts/events from source modules; never read their private tables or recreate their aggregates.

## Implementation

- Use immutable signal records, typed value objects for source/reference/confidence/expiry, and a tenant/brand-aware projection keyed by customer and service relationship.
- Make event handlers idempotent with inbox keys; rebuild projections from retained events or a documented replay source. Stale or conflicting observations become visible exceptions, not silent overwrites.
- Implement `EvaluateCareRisk`, `EvaluateOutreachEligibility`, `RequestServiceRecovery`, and `AcceptAiRecommendation` as authorized actions. The outreach action must recheck consent, quiet hours, `next_contact_at`, and suppression under a lock.
- Dispatch domain events after commit through an outbox. Cross-module case creation, status publishing, and notifications use retries, correlation IDs, compensation, and operator-visible failure state.
- Store only references and minimal snapshots needed for explainability. Apply retention, export, deletion, field sensitivity, and audit rules to every projection.

## Verification

Cover event replay, duplicate delivery, expiry, source correction, wrong brand/tenant, cooling-off boundaries, concurrent dispatch, consent changes, provider failures, approval rejection, migration/rebuild, and accessibility-facing read models. Add architecture tests for private-table access and provider/framework coupling.

<!-- core-implementation-plan:start -->
## Module features, domain aspects, and source architecture

### Feature and domain aspect implementation matrix

| Feature / aspect | Domain model & invariant ownership | Application action, query, persistence & event contract |
| --- | --- | --- |
| **Customer health constellation** | Model `customer health constellation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Revenue-aware service recovery** | Model `revenue-aware service recovery` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Contact-protection ledger** | Model `contact-protection ledger` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Cross-brand consent and quiet-hour evaluation** | Model `cross-brand consent and quiet-hour evaluation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Approval-gated AI recommendations** | Model `approval-gated ai recommendations` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Mobile-ready daily queues** | Model `mobile-ready daily queues` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.

### Consuming adapter specifications

- [HTTP API contract](../api/revenue-and-care-orchestration.md) · [Filament 5](../filament/revenue-and-care-orchestration.md) · [Livewire 4](../livewire/revenue-and-care-orchestration.md) · [React + Inertia](../react/revenue-and-care-orchestration.md) · [Vue + Inertia](../vue/revenue-and-care-orchestration.md) · [Nuxt 4](../nuxt/revenue-and-care-orchestration.md) · [Next.js](../nextjs/revenue-and-care-orchestration.md) · [React Native](../react-native/revenue-and-care-orchestration.md) · [Flutter & Dart](../flutter/revenue-and-care-orchestration.md)
<!-- core-implementation-plan:end -->
