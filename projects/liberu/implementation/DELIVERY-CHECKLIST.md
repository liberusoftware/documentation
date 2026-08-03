# Liberu implementation and documentation checklist

## Before coding

- [ ] Select the exact project modules and record exclusions in an ADR.
- [ ] Assign source-of-truth owner, data classification, tenant/brand scope, roles, consent purpose, retention, and escalation owner.
- [ ] Define DTOs, commands, queries, events, webhooks, operation states, idempotency, concurrency, and versioning.
- [ ] Add the module/site/mobile entry to the relevant manifest and this documentation index.

## While coding

- [ ] Keep domain rules in core actions/policies; keep API transport in the API package; keep UI state in adapters.
- [ ] Add migrations, constraints, indexes, seed/configuration, feature flags, audit events, permissions, and provider sandbox adapters.
- [ ] Implement loading, empty, success, queued, offline, conflict, denied, rate-limit, and failure states in web and mobile where applicable.
- [ ] Add observability: correlation ID, structured logs, metrics, traces, queue/provider health, reconciliation status, and alerts.
- [ ] Add accessible responsive web UI, keyboard/focus behavior, localization, RTL, dynamic type, touch targets, and safe notification copy.

## Before release

- [ ] Run unit, feature, contract, architecture, authorization, tenant/brand isolation, migration, failure/recovery, accessibility, performance, and mobile lifecycle tests.
- [ ] Validate OpenAPI, generated clients, deep links, public SSR/cache boundaries, consent analytics, SEO/redirects, and provider webhook replay.
- [ ] Write user journey, API changelog, migration/cutover, rollback, incident, backup/restore, provider-outage, and support runbooks.
- [ ] Demonstrate the vertical slice with source records, references, queued/failure recovery, audit trail, and business-owner sign-off.
- [ ] Record freshness, formula, permission, and drill-through for every dashboard/insight; AI outputs include prompt/version, confidence, cost, and approval evidence.

## Definition of done

The feature is complete when a user can understand and finish the journey on its supported surface, a staff member can recover from interruption or provider failure, an operator can trace the action to its owner and correlation ID, and a developer can install, configure, test, document, release, and roll back it without tribal knowledge.
