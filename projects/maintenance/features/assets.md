# Maintenance: Assets\n\n## Canonical independent module specification\n\n**Domain module:** `maintenance-assets` \n**Application:** Maintenance \n**Capability group:** Module plan \n**Source scope:** [MAINTENANCE.md](../MAINTENANCE.md) \n**Architecture:** [MODULES.md](../MAINTENANCE.md) · [TESTING.md](../MAINTENANCE.md) · [API.md](../MAINTENANCE.md) · [FILAMENT.md](../MAINTENANCE.md) · [LIVEWIRE.md](../MAINTENANCE.md)\n\n## 1. Purpose\n\nThe Assets module owns Hierarchies, categories, specifications, meters, warranties, condition, QR/barcodes, and history. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.\n\n## 2. Full feature scope\n\n- **Hierarchies:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.\n- **Categories:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.\n- **Specifications:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.\n- **Meters:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.\n- **Warranties:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.\n- **Condition:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.\n- **QR/barcodes:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.\n- **History:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.\n\n## 3. Ownership and boundaries\n\n- Own the capability's domain rules, policies, actions, queries, events, persistence, migrations, configuration, audit semantics, and failure recovery.\n- Expose stable contracts, immutable DTOs/read models, commands, queries, and past-tense domain events where other modules have a legitimate integration need.\n- Consume identity, organizations/teams, authorization, settings, files, notifications, queues, localization, currency, and observability from the shared foundation rather than duplicating them.\n- Never depend on an application's `App\` classes, another module's private tables/models, a provider SDK in provider-neutral code, or an optional presentation framework.\n- Keep Filament, Livewire, and HTTP API logic in matching one-to-one presentation packages when those surfaces are required.\n\n## 4. Implementation strategy\n\n### Domain model\n\n- Define aggregates, entities, value objects, enums, invariants, lifecycle states, and transition rules using the terminology in this specification.\n- Make invalid states unrepresentable where practical and enforce remaining invariants at every mutation boundary.\n- Use opaque stable identifiers and explicit actor, tenant, locale, timezone, and currency context where relevant.\n\n### Application layer\n\n- Implement one application action per mutation/use case and purpose-built queries for reads.\n- Authorize before accessing or mutating protected data; navigation or UI visibility never substitutes for a policy.\n- Execute local invariant changes transactionally, dispatch events after commit, and make retryable commands idempotent.\n- Model long-running or cross-module work through queued jobs, outbox/inbox delivery, sagas, compensation, and operator-visible recovery.\n\n### Persistence and integrations\n\n- Store only module-owned data in module-owned tables with documented indexes, constraints, retention, export, deletion, and migration behavior.\n- Integrate other capabilities through contracts/events and external systems through independent provider adapters with timeouts, retries, rate limits, reconciliation, and sandbox support.\n- Treat imports, webhooks, provider callbacks, files, and generated content as untrusted inputs with provenance and deduplication.\n\n### Presentation\n\n- Provide matching optional presentation packages only when required: `module-maintenance-assets-filament`, `module-maintenance-assets-livewire`, and `module-maintenance-assets-api`.\n- Each presentation package depends on this module's public boundary and presents no other independent module.\n- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.\n\n## 5. Security, privacy, and operations\n\n- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval f…70722 tokens truncated…tional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `maintenance-procurement` public API boundary. It must not contain another module's UI or depend on application `App\` classes.\n\n## 2. Module-specific surfaces\n\n- **Suppliers:** page/component/composable/API-action behavior for this module's authorized workflow.\n- **Requests:** page/component/composable/API-action behavior for this module's authorized workflow.\n- **Approvals:** page/component/composable/API-action behavior for this module's authorized workflow.\n- **Purchase orders:** page/component/composable/API-action behavior for this module's authorized workflow.\n- **Receipts:** page/component/composable/API-action behavior for this module's authorized workflow.\n- **Returns:** page/component/composable/API-action behavior for this module's authorized workflow.\n- **Cost allocation:** page/component/composable/API-action behavior for this module's authorized workflow.\n\n## 3. Nuxt 4 implementation\n\n- Register a stable `module-maintenance-procurement-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.\n- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.\n- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.\n- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.\n\n### Capability mapping\n\n- `suppliers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.\n- `requests`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.\n- `approvals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.\n- `purchase-orders`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.\n- `receipts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.\n- `returns`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.\n- `cost-allocation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.\n\n## 4. API contract and Nuxt consumption\n\n- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.\n- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.\n- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.\n- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.\n- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.\n\n## 5. Security and verification\n\n- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.\n- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.\n- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.\n\n## 6. Definition of done\n\n- Package identity, public exports, API dependency, and module dependency match `maintenance-procurement` one-to-one.\n- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.\n- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

## Canonical independent module specification

**Domain module:** `maintenance-assets`  
**Application:** Maintenance  
**Capability group:** Module plan  
**Source scope:** [MAINTENANCE.md](../MAINTENANCE.md)  
**Architecture:** [MODULES.md](../MAINTENANCE.md) · [TESTING.md](../MAINTENANCE.md) · [API.md](../MAINTENANCE.md) · [FILAMENT.md](../MAINTENANCE.md) · [LIVEWIRE.md](../MAINTENANCE.md)

## 1. Purpose

The Assets module owns Hierarchies, categories, specifications, meters, warranties, condition, QR/barcodes, and history. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Hierarchies:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Categories:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Specifications:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Meters:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Warranties:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Condition:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **QR/barcodes:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **History:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.

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

- Provide matching optional presentation packages only when required: `module-maintenance-assets-filament`, `module-maintenance-assets-livewire`, and `module-maintenance-assets-api`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify hierarchies across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify categories across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify specifications across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify meters across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify warranties across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify condition across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify qR/barcodes across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify history across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
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
