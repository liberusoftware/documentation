# Ecommerce: Lots and Serials

## Canonical independent module specification

**Domain module:** `ecommerce-lots-and-serials`  
**Application:** Ecommerce  
**Capability group:** Inventory and availability modules  
**Source scope:** [ECOMMERCE.md](../ECOMMERCE.md)  
**Architecture:** [MODULES.md](../ECOMMERCE.md) · [TESTING.md](../ECOMMERCE.md) · [API.md](../ECOMMERCE.md) · [FILAMENT.md](../ECOMMERCE.md) · [LIVEWIRE.md](../ECOMMERCE.md)

## 1. Purpose

The Lots and Serials module owns Lot/batch/serial identity, expiry, traceability, allocation policy, recall, warranty links, and fulfillment/return capture. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Lot/batch/serial identity:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Expiry:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Traceability:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Allocation policy:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Recall:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Warranty links:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Fulfillment/return capture:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.

## 3. Ownership and boundaries

- Own the capability's domain rules, policies, actions, queries, events, persistence, migrations, configuration, audit semantics, and failure recovery.
- Expose stable contracts, immutable DTOs/read models, commands, queries, and past-tense domain events where other modules have a legitimate integration need.
- Consume identity, organizations/teams, authorization, settings, files, notifications, queues, localization, currency, and observability from the shared foundation rather than duplicating them.
- Never depend on an application's `App\` classes, another module's private tables/models, a provider SDK in provider-neutral code, or an optional presentation framework.
- Keep Filament, Livewire, and HTTP API logic in matching one-to-one presentation packages when those surfaces are required.

## 4. Implementation strategy

### Domain model

- Define aggregates, entities, value objects, enums, invariants, lifecycle states, and transition rules using the terminology in this specification.
- Make invalid states unrepresentable where practical and enforce remaining invariants at every mutation boundary.
- Use opaque stable identifiers and explicit actor, tenant, locale, timezone, and currency context where relevant.

### Application layer

- Implement one application action per mutation/use case and purpose-built queries for reads.
- Authorize before accessing or mutating protected data; navigation or UI visibility never substitutes for a policy.
- Execute local invariant changes transactionally, dispatch events after commit, and make retryable commands idempotent.
- Model long-running or cross-module work through queued jobs, outbox/inbox delivery, sagas, compensation, and operator-visible recovery.

### Persistence and integrations

- Store only module-owned data in module-owned tables with documented indexes, constraints, retention, export, deletion, and migration behavior.
- Integrate other capabilities through contracts/events and external systems through independent provider adapters with timeouts, retries, rate limits, reconciliation, and sandbox support.
- Treat imports, webhooks, provider callbacks, files, and generated content as untrusted inputs with provenance and deduplication.

### Presentation

- Provide matching optional presentation packages only when required: `module-ecommerce-lots-and-serials-filament`, `module-ecommerce-lots-and-serials-livewire`, and `module-ecommerce-lots-and-serials-api`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify lot/batch/serial identity across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify expiry across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify traceability across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify allocation policy across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify recall across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify warranty links across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify fulfillment/return capture across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Add unit tests for pure rules/value objects and feature tests for actions, policies, validation, persistence, events, jobs, and module lifecycle.
- Add architecture tests for forbidden dependencies, `App\` coupling, provider leakage, private cross-module access, and presentation dependencies.
- Add migration/upgrade, contract, compatibility, security, performance, failure/recovery, and minimal-host installation tests as risk requires.
- Run the independent Pest 5 suite through repository-owned Composer scripts and the shared package testbench; meaningful owned PHP targets 100% line coverage without excluding difficult code.
- Run composition tests in representative host applications while keeping this repository's suite authoritative for module behavior.

## 7. Definition of done

- Every feature in scope has explicit acceptance criteria, permissions, tenant behavior, persistence ownership, events, failure handling, telemetry, and tests.
- Public contracts and presentation extension points are versioned and documented.
- Install, enable, disable, upgrade, retry/recovery, and uninstall/retention behavior is verified.
- Security, accessibility where presented, compatibility, architecture, and 100% meaningful-PHP coverage gates pass.
- README, changelog, migration guidance, runbook, CI evidence, and tagged release are available from the independent repository.
