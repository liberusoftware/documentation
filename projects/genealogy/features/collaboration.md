# Genealogy: Collaboration

## Canonical independent module specification

**Domain module:** `genealogy-collaboration`
**Application:** Genealogy
**Capability group:** Module plan
**Source scope:** [GENEALOGY.md](../GENEALOGY.md)
**Architecture:** [MODULES.md](../GENEALOGY.md) · [TESTING.md](../GENEALOGY.md) · [API.md](../GENEALOGY.md) · [FILAMENT.md](../GENEALOGY.md) · [LIVEWIRE.md](../GENEALOGY.md)

## 1. Purpose

The Collaboration module owns Invitations, roles, branch/change proposals, review, discussions, watch lists, and attribution. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Invitations:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Roles:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Branch/change proposals:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Review:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Discussions:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Watch lists:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Attribution:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.

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

- Provide matching optional presentation packages only when required: `module-genealogy-collaboration-filament`, `module-genealogy-collaboration-livewire`, and `module-genealogy-collaboration-api`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify invitations across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify roles across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify branch/change proposals across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify review across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify discussions across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify watch lists across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify attribution across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
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
- README, changelog, migration guidance, runbook, CI evidence, a…65731 tokens truncated…nt-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `genealogy-places` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

## Canonical independent module specification

**Domain module:** `genealogy-collaboration`  
**Application:** Genealogy  
**Capability group:** Module plan  
**Source scope:** [GENEALOGY.md](../GENEALOGY.md)  
**Architecture:** [MODULES.md](../GENEALOGY.md) · [TESTING.md](../GENEALOGY.md) · [API.md](../GENEALOGY.md) · [FILAMENT.md](../GENEALOGY.md) · [LIVEWIRE.md](../GENEALOGY.md)

## 1. Purpose

The Collaboration module owns Invitations, roles, branch/change proposals, review, discussions, watch lists, and attribution. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Invitations:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Roles:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Branch/change proposals:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Review:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Discussions:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Watch lists:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Attribution:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.

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

- Provide matching optional presentation packages only when required: `module-genealogy-collaboration-filament`, `module-genealogy-collaboration-livewire`, and `module-genealogy-collaboration-api`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify invitations across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify roles across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify branch/change proposals across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify review across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify discussions across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify watch lists across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify attribution across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
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
