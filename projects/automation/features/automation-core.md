# Automation: Automation Core\n\n## Canonical independent module specification\n\n**Domain module:** `automation-core` \n**Application:** Automation \n**Capability group:** Module plan \n**Source scope:** [AUTOMATION.md](../AUTOMATION.md) \n**Architecture:** [MODULES.md](../AUTOMATION.md) · [TESTING.md](../AUTOMATION.md) · [API.md](../AUTOMATION.md) · [FILAMENT.md](../AUTOMATION.md) · [LIVEWIRE.md](../AUTOMATION.md)\n\n## 1. Purpose\n\nThe Automation Core module owns Workflow definitions, versions, triggers, state, runs, variables, schedules, retries, cancellation, and compensation. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.\n\n## 2. Full feature scope\n\n- **Workflow definitions:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.\n- **Versions:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.\n- **Triggers:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.\n- **State:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.\n- **Runs:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.\n- **Variables:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.\n- **Schedules:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.\n- **Retries:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.\n- **Cancellation:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.\n- **Compensation:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.\n\n## 3. Ownership and boundaries\n\n- Own the capability's domain rules, policies, actions, queries, events, persistence, migrations, configuration, audit semantics, and failure recovery.\n- Expose stable contracts, immutable DTOs/read models, commands, queries, and past-tense domain events where other modules have a legitimate integration need.\n- Consume identity, organizations/teams, authorization, settings, files, notifications, queues, localization, currency, and observability from the shared foundation rather than duplicating them.\n- Never depend on an application's `App\` classes, another module's private tables/models, a provider SDK in provider-neutral code, or an optional presentation framework.\n- Keep Filament, Livewire, and HTTP API logic in matching one-to-one presentation packages when those surfaces are required.\n\n## 4. Implementation strategy\n\n### Domain model\n\n- Define aggregates, entities, value objects, enums, invariants, lifecycle states, and transition rules using the terminology in this specification.\n- Make invalid states unrepresentable where practical and enforce remaining invariants at every mutation boundary.\n- Use opaque stable identifiers and explicit actor, tenant, locale, timezone, and currency context where relevant.\n\n### Application layer\n\n- Implement one application action per mutation/use case and purpose-built queries for reads.\n- Authorize before accessing or mutating protected data; navigation or UI visibility never substitutes for a policy.\n- Execute local invariant changes transactionally, dispatch events after commit, and make retryable commands idempotent.\n- Model long-running or cross-module work through queued jobs, outbox/inbox delivery, sagas, compensation, and operator-visible recovery.\n\n### Persistence and integrations\n\n- Store only module-owned data in module-owned tables with documented indexes, constraints, retention, export, deletion, and migration behavior.\n- Integrate other capabilities through contracts/events and external systems through independent provider adapters with timeouts, retries, rate limits, reconciliation, and sandbox support.\n- Treat imports, webhooks, provider callbacks, files, and generated content as untrusted inputs with provenance and deduplication.\n\n### Presentation\n\n- Provide matching optional presentation packages only when required: `module-automation-core-filament`, `module-automation-core-livewire`, and `module-automation-core-api`.\n- Each presentation package depends on this module's public boundary and presents no other independent module.\n- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.\n\n## 5. Security, privacy, and operations\n\n- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.\n- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.\n- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.\n- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.\n\n## 6. Verification strategy\n\n- Verify workflow definitions across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.\n- Verify versions across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.\n- Verify triggers across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.\n- Verify state across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.\n- Verify runs across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.\n- Verify variables across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.\n- Verify schedules across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.\n- Verify retries across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.\n- Verify cancellation across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.\n- Verify compensation across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.\n- Add unit tests for pure rules/value objects and feature tests for actions, policies, validation, persistence, events, jobs, and module lifecycle.\n- Add architecture tests for forbidden dependencies, `App\` coupling, provider leakage, private cross-module access, and presentation dependencies.\n- Add migration/upgrade, contract, compatibility, security, performance, failure/recovery, and minimal-host installation tests as risk requires.\n- Run the independent Pest 5 suite through repository-owned Composer scripts and the shared package testbench; meaningful owned PHP targets 100% line coverage without excluding difficult code.\n- Run composition tests in representative host applications while keeping this repository's suite authoritative for module behavior.\n\n## 7. Definition of done\n\n- Every feature in scope has explicit acceptance criteria, permissions, tenant behavior, persistence ownership, events, failure handling, telemetry, and tests.\n- Public contracts and presentation extension points are versioned and documented.\n- Install, enable, disable, upgrade, retry/recovery, and uninstall/retention behavior is verified.\n- Security, accessibility where presented, compatibility, architecture, and 100% meaningful-PHP coverage gates pass.\n- README, changelog, migration guidance, runbook, CI evidence, and tagged release are available from the independent repository.

## Canonical independent module specification

**Domain module:** `automation-core`  
**Application:** Automation  
**Capability group:** Module plan  
**Source scope:** [AUTOMATION.md](../AUTOMATION.md)  
**Architecture:** [MODULES.md](../AUTOMATION.md) · [TESTING.md](../AUTOMATION.md) · [API.md](../AUTOMATION.md) · [FILAMENT.md](../AUTOMATION.md) · [LIVEWIRE.md](../AUTOMATION.md)

## 1. Purpose

The Automation Core module owns Workflow definitions, versions, triggers, state, runs, variables, schedules, retries, cancellation, and compensation. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Workflow definitions:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Versions:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Triggers:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **State:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Runs:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Variables:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Schedules:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Retries:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Cancellation:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Compensation:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.

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

- Provide matching optional presentation packages only when required: `module-automation-core-filament`, `module-automation-core-livewire`, and `module-automation-core-api`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify workflow definitions across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify versions across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify triggers across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify state across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify runs across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify variables across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify schedules across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify retries across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify cancellation across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify compensation across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
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
