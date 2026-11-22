# Boilerplate: Integrations domain packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#integrations). Observed identity: [`liberusoftware/integrations`](../../../modules/source/liberusoftware--integrations.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-integrations`
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Provider credentials, capabilities, OAuth callbacks, secret rotation, connection tests, and sync.

## Ownership and implementation plan

This package is the authoritative, presentation-neutral implementation of Integrations. It owns the domain language, invariants, application actions, read models, policies, persistence, events, jobs, contracts, lifecycle, recovery, data classification, and upgrade behavior for this capability.

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
| **Provider credentials** | Model `provider credentials` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Capabilities** | Model `capabilities` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **OAuth callbacks** | Model `oauth callbacks` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Secret rotation** | Model `secret rotation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Connection tests** | Model `connection tests` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Sync** | Model `sync` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_01_030100_create_integration_connections_table.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/integrations/database/migrations/2026_08_01_030100_create_integration_connections_table.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [IntegrationAdapter.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/integrations/src/Contracts/IntegrationAdapter.php) | `public function name(): string`<br>`public function capabilities(): array`<br>`public function test(array $credentials): bool` |

### Consuming adapter specifications

- [HTTP API contract](../api/integrations.md) · [Filament 5](../filament/integrations.md) · [Livewire 4](../livewire/integrations.md) · [React + Inertia](../react/integrations.md) · [Vue + Inertia](../vue/integrations.md) · [Nuxt 4](../nuxt/integrations.md) · [Next.js](../nextjs/integrations.md) · [React Native](../react-native/integrations.md) · [Flutter & Dart](../flutter/integrations.md)
<!-- core-implementation-plan:end -->

## Contracts and modular provider adapters

`liberusoftware/integrations` defines provider-neutral contracts and registries (`IntegrationAdapter`, `OAuthIntegrationAdapter`, `PaymentProviderAdapter`, `CalendarService`, `CredentialVault`, `IntegrationRegistry`, `SsrfGuard`), while provider-specific implementations live in independently installable adapter modules:

- [`liberusoftware/integrations-google`](integrations-google.md) — Google Ads, Google Calendar, Gmail, YouTube
- [`liberusoftware/integrations-imap-pop3`](integrations-imap-pop3.md) — IMAP and POP3 inbound mail
- [`liberusoftware/integrations-linkedin`](integrations-linkedin.md) — LinkedIn organic and Ads
- [`liberusoftware/integrations-mailchimp`](integrations-mailchimp.md) — MailChimp marketing lists and campaigns
- [`liberusoftware/integrations-meta`](integrations-meta.md) — Facebook, Facebook Ads, Messenger, Instagram, WhatsApp Business
- [`liberusoftware/integrations-microsoft`](integrations-microsoft.md) — Outlook Mail and Outlook Calendar
- [`liberusoftware/integrations-sso`](integrations-sso.md) — OIDC and SAML 2.0 SSO with JIT provisioning and enforcement
- [`liberusoftware/integrations-stripe`](integrations-stripe.md) — Stripe billing and subscription integration
- [`liberusoftware/integrations-twilio`](integrations-twilio.md) — Twilio voice, SMS, OAuth, and call settings
- [`liberusoftware/integrations-twitter`](integrations-twitter.md) — Twitter / X publishing
- [`liberusoftware/integrations-zernio`](integrations-zernio.md) — Zernio publishing, advertising, webhooks, and tenant provisioning
