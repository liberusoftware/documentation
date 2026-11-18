# Ecommerce: Catering core

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#catering). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Status and ownership

Design specification implementing [documentation issue #26](https://github.com/liberusoftware/documentation/issues/26); this page does not assert a released package or approved dependency contract. Proposed repository: `liberusoftware/module-ecommerce-catering`; Composer: `liberusoftware/ecommerce-catering`; module: `ecommerce-catering`; namespace: `Liberu\Ecommerce\Catering\`. Schema and implementation wait for the boundary decisions below. The host is the composition root and commits installed modules in `/modules` and themes in `/themes`.

## User outcome and owned records

A catering operator maintains meals and staff-managed packages, prepares an event-specific menu and reproducible quotation, and converts an accepted, availability-confirmed event to an order exactly once. Catering owns meal/recipe composition, ingredient references and quantities, preparation yields, menu selections and revisions, event date/time/timezone, venue, guest count, dietary/service requirements and catering-specific snapshots. Recipes, preparation instructions and ingredient costs are staff-only. Customer projections contain only approved descriptions, dietary disclosures, quantities, event requirements and quoted prices.

Ingredients and recipes are operational records; they do not establish a competing inventory, allergen certification, tax, scheduling or pricing engine. Record units and yields explicitly, reject incompatible units and nonpositive yields/guest counts, and snapshot revisions used by a quotation. Substitutions or changed guest counts create a new menu/quote revision; never edit an accepted snapshot. Dietary requests are recorded as requests, not a guarantee that cross-contamination is impossible.

## Dependencies and exclusions

| Capability | Direction and contract |
| --- | --- |
| Catalog | Catering consumes public product identifiers/contracts when linking sellable meals/components. Catalog owns variants, publication and visibility. |
| Cart | Optional host composition may seed an event request. A mutable cart is never the authoritative menu snapshot. |
| Pricing | Optional until automatic pricing rules are approved. Read current prices through public contracts and freeze quote snapshots. Staff-entered estimates must record currency, author and assumptions. |
| Negotiated Quotes | Reuse its public negotiation/version/expiry/acceptance contract when approved; Catering owns event/menu context and line meaning, not a second quote engine. |
| Bookings and Appointments | Reuse availability/capacity and booking lifecycle when approved. Catering owns event service requirements. |
| Orders | Consume the approved order-conversion API and store stable references plus accepted snapshot references. No writes into Orders tables. |
| Payments | No direct dependency. Deposits, authorization, capture and reconciliation belong to Payments and host checkout composition. |

No upstream capability depends on Catering. Inspect actual published manifests/contracts before declaring required version constraints; record directional, cycle-free dependencies in the implementation ADR. Integrations remain optional until used and approved. Do not invent contract methods or claim installation works before validation.

## Lifecycle and consistency

1. Staff creates meals/packages and an event request within Team/Store scope. Customers may submit their own event requirements through an approved projection.
2. Validate a menu revision and capture meal, package, quantity, yield and requirement context. Save a stable revision reference.
3. Submit that context to the approved quote workflow; retain immutable menu/quote linkage, currency, price/tax assumptions, author, expiry and negotiated quote version reference.
4. Accept only the current unexpired quoted revision using an atomic version check. Reject stale or changed menus and surface a re-quote action.
5. Confirm availability separately using the booking contract. Quote acceptance, availability, order creation, deposit and payment completion are separate facts.
6. On the approved confirmation transition, request order creation with a durable idempotency key tied to event and accepted revision. Preserve the accepted commercial/menu snapshots. Persist the order reference and emit a past-tense event only after the local commit.
7. Use an outbox and retry-safe integration handler where a remote transaction is involved. A failed or timed-out conversion stays pending/recoverable; reconcile by the same key before retrying. Two workers must never create two orders.

Cancellation, rejected/expired quotation, unavailable capacity and payment failure have distinct statuses and recovery actions. Retain accepted records under the owning retention policy; disabling the module never deletes them. Do not invent cancellation fees, deposit rates or automatic pricing formulas.

## Public boundary, authorization and operations

Define typed commands and read DTOs for meal/package maintenance, event requests, menu revision, quote submission, confirmation and conversion recovery only after checking shared contracts. Enforce authorization and Team/Store ownership inside actions as well as UI/API entry points. Customer event access must check ownership, not just guess-resistant IDs. Staff recipe/cost privileges are distinct from customer quote access. Audit actor, scope, revision, transition, reason and correlation ID; redact dietary/personally identifiable data from logs and events. Specify retention/export/redaction with Customer Accounts and the host privacy workflow.

Monitor pending conversion age, retries, stale revisions, availability rejection and duplicate-key reconciliation. A runbook explains how staff inspects failed confirmation, rechecks capacity, reconciles Orders and safely resumes without editing snapshots or creating duplicate orders.

## Acceptance evidence

- Domain tests cover yields/units, invalid guest counts, menu changes, snapshots, expiry and stale acceptance.
- Tenant/ownership and field-projection tests prevent recipe, cost and preparation leakage across every API/UI/export path.
- Contract tests exercise the actual approved Catalog/Quotes/Bookings/Orders boundaries, with optional integrations disabled as well as enabled.
- Concurrent confirmation, duplicate delivery, timeout-after-order-create and replay create one order and preserve references.
- Independent package install, migrations, architecture checks and applicable coverage gates pass; a host composition test proves the full customer/staff journey.

## Boundary decisions required before schema work

Record owner approval for: (1) immediate versus optional Quotes/Bookings integration, (2) which quote fields/line snapshots live in Negotiated Quotes versus Catering, (3) the authoritative availability/accepted-quote confirmation transition that permits order creation, (4) currency/tax/pricing inputs and retention obligations. Until resolved, implementation issues are planning work and must not prescribe schema or claim these choices are approved.

<!-- core-implementation-plan:start -->
## Module features, domain aspects, and source architecture

### Feature and domain aspect implementation matrix

| Feature / aspect | Domain model & invariant ownership | Application action, query, persistence & event contract |
| --- | --- | --- |
| **Meals and ingredient composition** | Model `meals and ingredient composition` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Recipes and preparation yields** | Model `recipes and preparation yields` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Staff-managed catering packages** | Model `staff-managed catering packages` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Event requirements and venue context** | Model `event requirements and venue context` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Immutable menu revisions** | Model `immutable menu revisions` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Reproducible quotation context** | Model `reproducible quotation context` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Availability confirmation and order conversion** | Model `availability confirmation and order conversion` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.

### Consuming adapter specifications

- [HTTP API contract](../api/catering.md) · [Filament 5](../filament/catering.md) · [Livewire 4](../livewire/catering.md) · [React + Inertia](../react/catering.md) · [Vue + Inertia](../vue/catering.md) · [Nuxt 4](../nuxt/catering.md) · [Next.js](../nextjs/catering.md) · [React Native](../react-native/catering.md) · [Flutter & Dart](../flutter/catering.md)
<!-- core-implementation-plan:end -->
