# Boilerplate: Activity and Comments domain packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#activity-and-comments). Observed identity: [`liberusoftware/activity-comments`](../../../modules/source/liberusoftware--activity-comments.md). This retained spelling maps to `activity-comments`; it is not another independent module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-activity-and-comments`
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Activity timelines, mentions, subscriptions, internal comments, attachments, and visibility.

## Ownership and implementation plan

This package is the authoritative, presentation-neutral implementation of Activity and Comments. It owns the domain language, invariants, application actions, read models, policies, persistence, events, jobs, contracts, lifecycle, recovery, data classification, and upgrade behavior for this capability.

- Model the bounded context with explicit aggregates, entities, value objects, enums, and lifecycle states; reject invalid transitions inside the domain boundary.
- Expose typed actions for mutations and purpose-built queries for reads. Keep Eloquent models as persistence mappings and never expose private tables to other modules.
- Enforce authorization, tenant/team context, ownership, consent, and field sensitivity consistently across HTTP, UI, console, queue, export, search, notification, and bulk paths.
- Own migrations, constraints, indexes, factories, seeders, retention, export, deletion, configuration, events, jobs, and safe enable/disable/upgrade behavior.
- Make asynchronous work idempotent, retryable, observable, and safe to replay; dispatch local events after commit and document compensation for distributed work.

## Verification and consumer contract

Test domain rules, actions, policies, validation, persistence, tenancy, events, jobs, commands, migrations, upgrades, security, failure recovery, and representative host composition. Add architecture tests for presentation coupling, provider leakage, private cross-module access, and dependency cycles.

API, Filament, Livewire, React, Vue, and Nuxt consumers use only this package's public contracts. See [DDD patterns](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md) and [testing](../../../standards/TESTING.md).

<!-- core-implementation-plan:start -->
## Module features, domain aspects, and source architecture

### Feature and domain aspect implementation matrix

| Feature / aspect | Domain model & invariant ownership | Application action, query, persistence & event contract |
| --- | --- | --- |
| **Activity timelines** | Model `activity timelines` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Mentions** | Model `mentions` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Subscriptions** | Model `subscriptions` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Internal comments** | Model `internal comments` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Attachments** | Model `attachments` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Visibility** | Model `visibility` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_01_050100_create_activity_comment_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/activity-comments/database/migrations/2026_08_01_050100_create_activity_comment_tables.php) · [2026_08_01_065000_create_mentions_and_attachments.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/activity-comments/database/migrations/2026_08_01_065000_create_mentions_and_attachments.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivityAuthorizer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/activity-comments/src/Contracts/ActivityAuthorizer.php) | `public function allowed(string\|int $actorId, string $subjectType, string\|int $subjectId, string $operation): bool` |

### Consuming adapter specifications

- [HTTP API contract](../api/activity-and-comments.md) · [Filament 5](../filament/activity-and-comments.md) · [Livewire 4](../livewire/activity-and-comments.md) · [React + Inertia](../react/activity-and-comments.md) · [Vue + Inertia](../vue/activity-and-comments.md) · [Nuxt 4](../nuxt/activity-and-comments.md) · [Next.js](../nextjs/activity-and-comments.md) · [React Native](../react-native/activity-and-comments.md) · [Flutter & Dart](../flutter/activity-and-comments.md)
<!-- core-implementation-plan:end -->
