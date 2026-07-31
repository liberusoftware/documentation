# Liberu Module Architecture

## Canonical Implementation Specification

**Status:** Source of truth
**Applies to:** All Liberu Laravel applications and reusable packages
**Target stack:** Laravel 13, PHP 8.5, Filament 5, Livewire 4

## 1. Purpose

This document defines how Liberu modules are named, structured, discovered, installed, configured, integrated, tested, versioned, and removed. Product scopes define *what* to build; this document defines *how functional boundaries are packaged*.

A module is a self-contained business or platform capability with explicit ownership, public contracts, dependencies, lifecycle, resources, and tests. The module manager discovers and boots modules but does not contain domain-specific behavior.

## 2. Architectural rules

1. One module owns each business capability and its authoritative writes.
2. Modules communicate through public contracts, commands, queries, and versioned domain events.
3. A module must not query or mutate another module's tables directly.
4. Dependencies must be declared, directional, and free of cycles.
5. Optional integrations are implemented through adapters and capability checks.
6. Framework-facing code stays at module edges; domain rules remain usable without Filament or HTTP.
7. All tenant-owned queries and uniqueness rules include tenant scope.
8. Side effects are authorized, auditable, retry-safe, and observable.
9. Disabling or uninstalling a module must be explicit; data is never silently deleted.
10. Themes may render module output but must not own domain logic.

## 3. Standard module layout

```text
modules/
└── Blog/
    ├── composer.json
    ├── module.json
    ├── README.md
    ├── CHANGELOG.md
    ├── config/blog.php
    ├── database/
    │   ├── factories/
    │   ├── migrations/
    │   └── seeders/
    ├── resources/
    │   ├── lang/
    │   └── views/
    ├── routes/
    │   ├── api.php
    │   ├── console.php
    │   └── web.php
    ├── src/
    │   ├── Actions/
    │   ├── Contracts/
    │   ├── Data/
    │   ├── Domain/
    │   ├── Events/
    │   ├── Exceptions/
    │   ├── Filament/
    │   │   ├── Clusters/
    │   │   ├── Pages/
    │   │   ├── Resources/
    │   │   └── Widgets/
    │   ├── Http/
    │   │   ├── Controllers/
    │   │   ├── Middleware/
    │   │   ├── Requests/
    │   │   └── Resources/
    │   ├── Jobs/
    │   ├── Listeners/
    │   ├── Livewire/
    │   ├── Models/
    │   ├── Notifications/
    │   ├── Policies/
    │   ├── Providers/
    │   ├── Queries/
    │   ├── Services/
    │   └── BlogServiceProvider.php
    └── tests/
        ├── Architecture/
        ├── Feature/
        └── Unit/
```

Only create directories a module uses. `src/` is the PSR-4 root. Database, configuration, routes, translations, and views are module-owned resources outside that root.

## 4. Naming conventions

| Item | Convention | Example |
|---|---|---|
| Directory and PHP module name | Singular PascalCase | `Billing`, `Media` |
| Composer package | `liberu/{kebab-name}` | `liberu/order-management` |
| Namespace | `Liberu\\Modules\\{Name}` | `Liberu\\Modules\\Billing` |
| Manifest name | Stable kebab-case | `order-management` |
| Configuration key | snake_case or short lowercase | `order_management` |
| Database tables | module-prefixed snake_case | `billing_invoices` |
| Routes | module-prefixed names | `billing.invoices.show` |
| Permissions | `{module}.{resource}.{action}` | `billing.invoices.refund` |
| Events | Past-tense domain fact | `InvoiceIssued` |
| Commands/actions | Imperative intent | `IssueInvoice` |

Names are public contracts after release. Renaming requires aliases or a documented migration.

## 5. Manifest contract

Every module contains `module.json` with this minimum shape:

```json
{
  "$schema": "https://schemas.liberu.dev/module/v1.json",
  "name": "blog",
  "display_name": "Blog",
  "description": "Editorial posts and publication workflows.",
  "version": "1.0.0",
  "provider": "Liberu\\Modules\\Blog\\BlogServiceProvider",
  "requires": {
    "php": "^8.5",
    "laravel": "^13.0",
    "modules": { "identity": "^1.0" }
  },
  "suggests": { "media": "^1.0" },
  "capabilities": ["blog.posts", "blog.publication"],
  "default_enabled": false
}
```

The JSON schema is versioned. CI rejects unknown required fields, invalid dependency ranges, duplicate names/capabilities, cycles, and providers that cannot be resolved. Deployment configuration—not the manifest—decides whether a module is enabled.

## 6. Discovery and boot process

The module manager performs deterministic startup:

1. Discover configured local and Composer-installed manifests.
2. Validate manifests and application compatibility.
3. Resolve required dependencies and detect cycles.
4. Read enabled state from deployment configuration/cache.
5. Sort enabled modules topologically, then by stable name.
6. Register service providers and bindings.
7. Boot routes, views, translations, policies, commands, schedules, events, and UI extensions.
8. Cache the resolved registry in production and invalidate it on deploy or configuration change.

Discovery must not scan arbitrary classes on every request. A broken optional module must produce an actionable deployment error without corrupting installed state.

## 7. Module lifecycle

| State/action | Required behavior |
|---|---|
| Available | Manifest is discoverable and compatible |
| Install | Validate dependencies, publish/configure resources where needed, run migrations, record version |
| Enable | Confirm installation and dependencies, then expose runtime capability |
| Disable | Stop new entry points and scheduled work without deleting records |
| Upgrade | Run ordered, idempotent migrations and upgrade hooks with rollback guidance |
| Uninstall | Require explicit confirmation and retention/export choice; default to preserving data |

Production lifecycle changes must be deploy-time operations or privileged, audited jobs. They must use locks, report progress, recover safely after interruption, and never run schema changes inside a web request.

## 8. Service provider responsibilities

`register()` binds contracts, merges configuration, and registers other providers without reading request state or performing I/O. `boot()` registers routes, policies, commands, events, schedules, views, translations, and publishable resources.

Providers must be idempotent, safe during config/route caching, and compatible with CLI, queue, scheduler, test, and HTTP runtimes. Application-specific overrides use container bindings or configuration, not edits inside the module.

## 9. Public boundaries

A module may expose:

- contracts for replaceable behavior;
- immutable DTOs for supported input/output;
- command handlers for requested state changes;
- query services or authorized read models;
- versioned events describing completed domain facts;
- routes and API resources documented as public endpoints;
- capabilities that optional consumers can detect.

Models, repositories, internal services, migrations, and tables are private unless explicitly documented. Cross-module foreign keys should reference stable platform identifiers and must not force an optional module to be installed.

## 10. Events, queues, and workflows

- Events contain stable identifiers and necessary facts, not serialized Eloquent models.
- Consumers are idempotent and tolerate duplicate or out-of-order delivery where relevant.
- External calls, bulk work, file processing, and slow projections use queued jobs.
- Jobs define timeout, retry, backoff, uniqueness, and failure handling.
- Multi-step workflows record state and support compensation or operator recovery.
- Transactional event publication uses an outbox or after-commit dispatch.
- Event schemas include a version; breaking changes introduce a new version.

## 11. Persistence and migrations

- Prefix tables by module unless a documented shared-core table is used.
- Use portable migrations supported by the product's declared databases.
- Expand schema before code depends on it; contract only after old code is retired.
- Avoid irreversible data transforms without backup, validation, and recovery instructions.
- Seeders are repeatable; factories generate tenant-correct data.
- Encrypt classified fields and never place secrets in module configuration committed to source control.
- Uninstall migrations do not drop production data automatically.

## 12. Identity, tenancy, and authorization

- Identity and organization modules own users, organizations, memberships, and service principals.
- Domain modules reference stable IDs and own their domain-specific profiles.
- Tenant context is resolved once at a trusted boundary and cannot be selected through unvalidated input.
- Policies authorize every UI, HTTP, API, console, and queued entry point.
- Background jobs carry signed or validated tenant and actor context.
- Permission names follow the module convention and are declared centrally by the owning module.
- Privileged actions support re-authentication, approval, and audit where risk warrants it.

## 13. Web, API, Filament, and Livewire

- Controllers and Livewire components orchestrate validated actions; domain logic resides in actions/services.
- Route names and URLs are module-prefixed and collision-tested.
- APIs use versioned resources, consistent errors, pagination, idempotency keys for retried writes, and explicit rate limits.
- Filament resources use policies and tenant scopes for all pages, actions, relation managers, exports, and global search.
- Modules register Filament components through a plugin or documented panel extension, not by modifying panel providers.
- Blade and Livewire presentation follows `THEMES.md`; module-provided views are functional defaults and publish stable extension points.

## 14. Configuration and feature flags

- Configuration files contain safe defaults and document every key.
- Secrets are referenced through environment-backed secret stores, never exposed by config endpoints or logs.
- Runtime feature flags control behavior, not module dependency resolution or schema installation.
- Flags define owner, default, rollout strategy, telemetry, and removal date.
- Configuration is validated during deployment and compatible with Laravel configuration caching.

## 15. External integrations

Integrations use a contract plus one or more provider drivers. Each driver defines authentication, supported capabilities, webhook verification, rate limits, retries, idempotency, sandbox behavior, and reconciliation.

Webhook ingestion must verify authenticity, persist a receipt before processing, deduplicate provider event IDs, return promptly, and process asynchronously. Synchronizations use cursors/checkpoints and provide operator-visible replay and reconciliation tools.

## 16. Observability and operations

Each module supplies:

- structured logs with correlation, tenant, actor, module, and operation identifiers;
- counters and timings for critical workflows and external providers;
- health/readiness checks that distinguish required from optional dependencies;
- failed-job and dead-letter visibility with safe replay;
- runbooks for expected failure modes, recovery, migration, and rollback;
- redaction rules preventing credentials, payment data, or sensitive personal data from entering telemetry.

## 17. Testing requirements

Every module requires:

- unit tests for domain rules and value objects;
- feature tests for actions, policies, validation, tenant isolation, routes, Filament, and Livewire surfaces;
- contract tests for public APIs, events, and provider drivers;
- migration tests from every supported released version;
- architecture tests preventing forbidden namespace and model/table dependencies;
- failure tests covering retries, duplicates, authorization denial, provider errors, and partial workflows;
- a minimal host-application test proving standalone installation and boot.

Tests run with dependencies at minimum and supported-latest versions where practical.

## 18. Security and compliance

- Validate input at every trust boundary and encode output for its context.
- Protect state-changing browser routes with CSRF and APIs with appropriate authentication/scopes.
- Apply least privilege to database, queue, storage, provider, and operator access.
- Audit security-sensitive reads and all privileged mutations.
- Define data classification, purpose, consent, retention, export, deletion, and legal-hold behavior.
- Scan dependencies and assets; establish an update and vulnerability-response policy.
- Threat-model authentication, payments, file upload, webhooks, automation, and infrastructure modules.

## 19. Versioning and compatibility

Modules use semantic versioning. The supported surface includes public PHP contracts, configuration keys, commands, routes, API schemas, events, permissions, extension points, and documented view/component identifiers.

- Patch: compatible fixes.
- Minor: backward-compatible capabilities and deprecations.
- Major: incompatible changes with upgrade documentation.

Deprecations identify a replacement and removal version. A compatibility matrix records supported PHP, Laravel, Filament, Livewire, module, database, and provider versions.

## 20. Documentation requirements

Every module README includes purpose, ownership, dependencies, installation, configuration, permissions, capabilities, public contracts/events, routes/commands, scheduled work, data classification, operational notes, extension points, and examples. Significant design decisions use ADRs; user-visible changes use the changelog.

## 21. Definition of done

A module is complete when:

- its boundary, owner, dependencies, and manifest are approved;
- install, enable, disable, upgrade, and failure paths work;
- domain behavior and all entry points are authorized and tenant-safe;
- public contracts and events are versioned and documented;
- UI extension points comply with `THEMES.md`;
- tests, static analysis, security checks, and compatibility CI pass;
- logs, metrics, health checks, alerts, and runbooks are available;
- migrations, rollback/recovery, retention, and upgrade notes are reviewed.

## 22. GitHub issue mapping

Create one epic per module. Recommended child issues:

1. Define boundary, owner, terminology, manifest, and dependency ADR.
2. Scaffold package, provider, configuration, and lifecycle support.
3. Implement domain model, actions, persistence, policies, and audit events.
4. Implement API, Filament, Livewire, console, and scheduled entry points as applicable.
5. Add integrations, webhooks, queues, reconciliation, and failure recovery.
6. Add complete tests, fixtures, architecture rules, and compatibility matrix.
7. Add telemetry, health checks, operational runbook, and documentation.

Each issue should state user outcome, module owner, dependencies, requirements, acceptance criteria, tests, observability, security/data considerations, and explicit exclusions.
