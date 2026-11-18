# CRM: Crm Web Intent Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-web-intent). Observed identity: [`liberusoftware/module-crm-web-intent`](../../../modules/source/liberusoftware--module-crm-web-intent.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-crm-crm-web-intent`
**Domain specification:** [Crm Web Intent](../features/crm-web-intent.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Crm Web Intent. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

## Domain-driven implementation plan

- Model the capability with small aggregates, entities, value objects, enums, domain services, and explicit lifecycle states. Enforce invariants inside the domain boundary and keep invalid transitions impossible or rejected with typed exceptions.
- Implement one application action per meaningful mutation/use case and purpose-built query/read-model classes for reads. Use typed immutable DTOs and stable identifiers at public boundaries; use repositories only where persistence abstraction adds value.
- Publish past-tense domain events after a successful local transaction. Use an outbox/inbox, idempotent handlers, sagas, or compensating actions for cross-module and distributed work; never mutate another module's private tables.

## Laravel and persistence plan

- Use PHP 8.5 strict types, PSR-compatible names, constructor injection, Laravel contracts, service providers, configuration, policies, validation, and route-independent application services. Format with the repository's Pint rules and keep static analysis clean.
- Keep Eloquent models as persistence mappings, not domain aggregates or API resources. The module owns migrations, constraints, indexes, casts, factories, seeders, retention, export, deletion, and upgrade behavior. Released migrations are immutable; production-safe follow-up migrations document locks, backfills, deployment order, and rollback limits.
- Queue work that exceeds the request budget or depends on external systems. Jobs carry authorized tenant/actor context, have explicit retry/backoff/timeout/idempotency rules, and emit structured logs, metrics, traces, correlation IDs, and operator-visible failure state.

## Security and user outcomes

- Apply policies consistently to HTTP, UI, console, queue, export, search, notification, and bulk paths. Enforce tenant/team/resource ownership, field sensitivity, consent, entitlement, and break-glass auditing; scopes never override domain authorization.
- Treat imports, files, webhooks, provider responses, and user input as untrusted. Redact credentials and protected data from logs, exceptions, events, snapshots, metrics, and test artifacts.
- Make normal workflows understandable for SMEs and personal users: actionable validation, safe defaults, reversible or previewable operations, clear status and recovery guidance, localization/timezone/currency support where relevant, accessibility in adapters, low operational overhead, and export/retention controls.

## Public boundary and adapters

Expose only stable contracts, actions, queries, events, resource data, and capability metadata needed by consumers. Keep provider SDKs, credentials, webhook mappings, and provider identifiers in separate adapter packages. Presentation packages may add validation at their boundary, but the core revalidates invariants and authorization and remains free of presentation dependencies.

## Verification and delivery plan

- Use unit tests for value objects, entities, aggregates, policies, and pure rules; feature/integration tests for actions, persistence, validation, tenancy, events, jobs, commands, migrations, upgrades, and recovery; and shared contract tests for adapters.
- Add architecture tests for forbidden App classes, private cross-module access, provider leakage, presentation dependencies, and dependency cycles. Test empty installs, supported upgrades, rollback policy, representative host composition, and compatibility across the declared Laravel/PHP/database matrix.
- Run the independent repository's Pest 5 suite through Composer scripts and the shared package testbench. Generate meaningful coverage, static-analysis, security, documentation/link, and performance evidence; coverage complements risk-based assertions and never replaces them.
- Release with Composer metadata, module manifest, service provider, changelog, migration notes, README, compatibility matrix, runbook, and safe install/enable/disable/upgrade/uninstall behavior. Disabling or removal never silently deletes user data.

<!-- core-implementation-plan:start -->
## Module features, domain aspects, and source architecture

### Feature and domain aspect implementation matrix

| Feature / aspect | Domain model & invariant ownership | Application action, query, persistence & event contract |
| --- | --- | --- |
| **First-party visits** | Model `first-party visits` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Account identification adapters** | Model `account identification adapters` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Page/content engagement** | Model `page/content engagement` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Scoring signals** | Model `scoring signals` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Alerts** | Model `alerts` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Buyer intent** | Model `buyer intent` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Consent** | Model `consent` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Lead/account conversion** | Model `lead/account conversion` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_25_030000_create_crm_web_intent_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/database/migrations/2026_08_25_030000_create_crm_web_intent_tables.php).

| Observed core query | Public method signatures |
| --- | --- |
| [WebIntentQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Queries/WebIntentQuery.php) | `public function visits(int $teamId): Builder`<br>`public function alerts(int $teamId): Builder`<br>`public function summary(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConvertIntent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/ConvertIntent.php) | `public function execute(int $teamId, int $actorId, string $visitorKey, string $targetType, int $targetId, ?int $visitId, array $metadata, WebIntentPolicy $policy): WebIntentConversion` |
| [CreateAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/CreateAlert.php) | `public function execute(int $teamId, int $actorId, string $visitorKey, string $title, string $severity, ?int $visitId, ?string $details, WebIntentPolicy $policy): WebIntentAlert` |
| [IdentifyAccount.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/IdentifyAccount.php) | `public function execute(int $teamId, int $actorId, string $visitorKey, string $adapter, ?string $accountName, ?string $accountDomain, int $confidence, array $metadata, WebIntentPolicy $policy): WebIntentIdentification` |
| [RecordEngagement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/RecordEngagement.php) | `public function execute(WebIntentVisit $visit, array $attributes, WebIntentScorer $scorer): WebIntentEngagement` |
| [RecordVisit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/RecordVisit.php) | `public function execute(int $teamId, string $visitorKey, array $attributes = []): WebIntentVisit` |
| [ResolveAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/ResolveAlert.php) | `public function execute(WebIntentAlert $alert, int $actorId, WebIntentPolicy $policy): WebIntentAlert` |
| [SetConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/SetConsent.php) | `public function execute(int $teamId, string $visitorKey, string $purpose, string $status, ?string $policyVersion = null): WebIntentConsent` |
| [WebIntentAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Services/WebIntentAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $data = []): void` |
| [WebIntentPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Services/WebIntentPolicy.php) | `public function canManage(int $teamId, int $actorId): bool` |
| [WebIntentScorer.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Services/WebIntentScorer.php) | `public function points(string $eventType, ?int $durationSeconds = null): int`<br>`public function level(int $score): string` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WebIntentAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentAlert.php) | `team_id`, `visitor_key`, `visit_id`, `severity`, `title`, `details`, `status`, `triggered_at`, `resolved_at`, `resolved_by` |
| [WebIntentConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentConsent.php) | `team_id`, `visitor_key`, `purpose`, `status`, `policy_version`, `granted_at`, `revoked_at` |
| [WebIntentConversion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentConversion.php) | `team_id`, `visitor_key`, `visit_id`, `target_type`, `target_id`, `actor_id`, `status`, `metadata` |
| [WebIntentEngagement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentEngagement.php) | `team_id`, `visit_id`, `visitor_key`, `event_type`, `page_url`, `content_type`, `content_id`, `points`, `duration_seconds`, `dedupe_key`, `metadata`, `occurred_at` |
| [WebIntentIdentification.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentIdentification.php) | `team_id`, `visitor_key`, `adapter`, `account_name`, `account_domain`, `confidence`, `status`, `metadata` |
| [WebIntentSignal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentSignal.php) | `team_id`, `visit_id`, `visitor_key`, `signal`, `points`, `metadata`, `occurred_at` |
| [WebIntentVisit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentVisit.php) | `team_id`, `visitor_key`, `session_key`, `ip_hash`, `user_agent_hash`, `landing_url`, `referrer`, `consent_status`, `score`, `intent_level`, `status`, `started_at`, `ended_at`, `metadata` |

### Consuming adapter specifications

- [HTTP API contract](../api/crm-web-intent.md) · [Filament 5](../filament/crm-web-intent.md) · [Livewire 4](../livewire/crm-web-intent.md) · [React + Inertia](../react/crm-web-intent.md) · [Vue + Inertia](../vue/crm-web-intent.md) · [Nuxt 4](../nuxt/crm-web-intent.md) · [Next.js](../nextjs/crm-web-intent.md) · [React Native](../react-native/crm-web-intent.md) · [Flutter & Dart](../flutter/crm-web-intent.md)
<!-- core-implementation-plan:end -->
