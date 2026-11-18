# CRM: Crm Feedback And Voice Of Customer Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-feedback-and-voice-of-customer). Observed identity: [`liberusoftware/module-crm-feedback-and-voice-of-customer`](../../../modules/source/liberusoftware--module-crm-feedback-and-voice-of-customer.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-crm-crm-feedback-and-voice-of-customer`
**Domain specification:** [Crm Feedback And Voice Of Customer](../features/crm-feedback-and-voice-of-customer.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Crm Feedback And Voice Of Customer. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **CSAT** | Model `csat` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **NPS** | Model `nps` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **CES** | Model `ces` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Custom surveys** | Model `custom surveys` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Sampling** | Model `sampling` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Delivery** | Model `delivery` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Responses** | Model `responses` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Text analysis** | Model `text analysis` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Alerts** | Model `alerts` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Close-the-loop cases** | Model `close-the-loop cases` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Trend reporting** | Model `trend reporting` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_27_030000_create_crm_feedback_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/database/migrations/2026_08_27_030000_create_crm_feedback_tables.php).

| Observed core query | Public method signatures |
| --- | --- |
| [FeedbackQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Queries/FeedbackQuery.php) | `public function surveys(int $teamId)`<br>`public function responses(int $teamId, int $surveyId)`<br>`public function trend(int $teamId, int $surveyId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateFeedbackSurvey.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/CreateFeedbackSurvey.php) | `public function __construct(private readonly FeedbackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): FeedbackSurvey` |
| [DeliverFeedbackSurvey.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/DeliverFeedbackSurvey.php) | `public function __construct(private readonly FeedbackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, FeedbackSurvey $survey, ?int $recipientId, string $channel = 'email'): FeedbackDelivery` |
| [OpenFeedbackCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/OpenFeedbackCase.php) | `public function __construct(private readonly FeedbackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, FeedbackResponse $response, ?int $ownerId = null): FeedbackCase` |
| [RecordFeedbackResponse.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/RecordFeedbackResponse.php) | `public function execute(int $teamId, FeedbackDelivery $delivery, array $input): FeedbackResponse` |
| [ResolveFeedbackAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/ResolveFeedbackAlert.php) | `public function __construct(private readonly FeedbackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, FeedbackAlert $alert): FeedbackAlert` |
| [FeedbackPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Services/FeedbackPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FeedbackAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackAlert.php) | No literal fillable array detected; inspect the model and API schema. |
| [FeedbackCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackCase.php) | No literal fillable array detected; inspect the model and API schema. |
| [FeedbackDelivery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackDelivery.php) | No literal fillable array detected; inspect the model and API schema. |
| [FeedbackResponse.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackResponse.php) | No literal fillable array detected; inspect the model and API schema. |
| [FeedbackSurvey.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackSurvey.php) | No literal fillable array detected; inspect the model and API schema. |

### Consuming adapter specifications

- [HTTP API contract](../api/crm-feedback-and-voice-of-customer.md) · [Filament 5](../filament/crm-feedback-and-voice-of-customer.md) · [Livewire 4](../livewire/crm-feedback-and-voice-of-customer.md) · [React + Inertia](../react/crm-feedback-and-voice-of-customer.md) · [Vue + Inertia](../vue/crm-feedback-and-voice-of-customer.md) · [Nuxt 4](../nuxt/crm-feedback-and-voice-of-customer.md) · [Next.js](../nextjs/crm-feedback-and-voice-of-customer.md) · [React Native](../react-native/crm-feedback-and-voice-of-customer.md) · [Flutter & Dart](../flutter/crm-feedback-and-voice-of-customer.md)
<!-- core-implementation-plan:end -->
