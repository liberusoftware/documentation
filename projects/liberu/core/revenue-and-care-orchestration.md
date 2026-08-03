# Liberu: Revenue and Care Orchestration Core

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
