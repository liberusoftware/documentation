# Liberu Ecommerce — end-user guide

**Experience area:** Commerce
**Canonical developer scope:** [ECOMMERCE.md](../../../projects/ecommerce/ECOMMERCE.md)
**All module journeys:** [Module guides](modules/README.md)

## What users should feel

Shoppers see discovery, product detail, cart, checkout, order tracking, returns, account, and relevant reassurance at every step.

## Primary journey

```mermaid
flowchart LR
  A[Arrive or sign in] --> B[See relevant context]
  B --> C[Choose the next useful action]
  C --> D[Receive clear result]
  D --> E[Return, continue, or get help]
```

## Web experience

The web surface should support discovery, deep links, keyboard access, shareable URLs where safe, responsive layouts, readable tables/cards, and clear public-to-authenticated handoff. Preserve the same terminology and status meanings across public pages, portals, and staff views.

## Mobile experience

The mobile surface should focus on the frequent task: show essential context first, keep the primary action thumb-reachable, support push/deep links only with consent, preserve drafts, show sync freshness, and recover safely from interruption or offline use. It may simplify navigation but must not weaken authorization, audit, validation, or policy.

## Visual acceptance

Use the shared [responsive shell and state contract](../../WEB-AND-MOBILE.md). A user must be able to identify where they are, what changed, what needs attention, and how to recover without reading developer documentation.

## Module map

See [all commerce module experiences](modules/README.md).
