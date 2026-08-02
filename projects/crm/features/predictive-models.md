# CRM: Predictive Models

## Canonical independent module specification

**Domain module:** `crm-predictive-models`  
**Application:** CRM  
**Capability group:** Intelligence and AI modules  
**Source scope:** [CRM.md](../CRM.md)  
**Architecture:** [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md) · [API.md](../CRM.md) · [FILAMENT.md](../CRM.md) · [LIVEWIRE.md](../CRM.md)

## 1. Purpose

The Predictive Models module owns Lead/opportunity scoring, churn/renewal risk, next action/product, forecast, routing, model registry, evaluation, drift, and explanations. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Lead/opportunity scoring:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Churn/renewal risk:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Next action/product:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Forecast:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Routing:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Model registry:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Evaluation:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Drift:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Explanations:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.

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

- Provide matching optional presentation packages only when required: `module-crm-predictive-models-filament`, `module-crm-predictive-models-livewire`, and `module-crm-predictive-models-api`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify lead/opportunity scoring across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify churn/renewal risk across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify next action/product across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify forecast across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify routing across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify model registry across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify evaluation across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify drift across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify explanations across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
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
