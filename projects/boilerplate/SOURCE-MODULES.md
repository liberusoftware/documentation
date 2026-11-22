# Boilerplate: observed source modules

Observed repository: [project-boilerplate-laravel-filament](https://github.com/liberusoftware/project-boilerplate-laravel-filament).

This is a manifest inventory of all installed modules in the reference boilerplate application. Use the exact manifest identity for dependency resolution.

Found **56 immediate directories under `modules/`** (0 symlink aliases; zero `Legacy` namespaces). See [inventory method and shared identities](../../architecture/SOURCE-INVENTORY.md).

## Other source locations

Application-owned `app/` contains only thin host composition classes (no domain logic):

| Source root | Role |
| --- | --- |
| `app/` | 5 thin host composition classes (`ModulePlugins`, `User`, `AdminPanelProvider`, `AppPanelProvider`, `ThemeColors`) |
| `routes/` | Host web/api/console route entry points |
| `resources/` | Host views, assets, and translations |
| `database/` | Host factories and seeders |
| `tests/` | Host integration, architecture, and 100% coverage suites |

Other manifest paths: `composer.json`, `package.json`, `scripts/composer.json`, `themes/base/composer.json`, `themes/clear-signal/composer.json`, `themes/dark/composer.json`, `themes/default/composer.json`.

## Immediate module manifests

| Module directory | Composer identity | npm identity | Alias target | Description |
| --- | --- | --- | --- | --- |
| [activity-comments](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/activity-comments) | liberusoftware/activity-comments | — | — | Generic authorized timelines, comments, mentions, subscriptions, attachments, and visibility. |
| [affiliate-contracts](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/affiliate-contracts) | liberusoftware/affiliate-contracts | — | — | Product-neutral affiliate management and referral attribution contracts and DTOs for Liberu. |
| [affiliate-core](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/affiliate-core) | liberusoftware/affiliate-core | — | — | Reusable affiliate program, referral attribution, commission ledger, clawback, and payout engine extending liberusoftware/affiliate-contracts. |
| [analytics-core](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/analytics-core) | liberusoftware/analytics-core | — | — | Consent-aware provider-neutral analytics event routing and durable delivery evidence. |
| [analytics-google](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/analytics-google) | liberusoftware/analytics-google | — | — | Consent-aware Google Analytics event mapping adapter. |
| [analytics-meta](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/analytics-meta) | liberusoftware/analytics-meta | — | — | Consent-aware Meta server-side event mapping and normalized customer-data adapter. |
| [api-access](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/api-access) | liberusoftware/api-access | — | — | API token, scope, version, rate-limit, idempotency, and revocation policy. |
| [application](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/application) | liberusoftware/application | — | — | Required application metadata, health, clocks, identifiers, and secure HTTP defaults. |
| [audit](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/audit) | liberusoftware/audit | — | — | Contextual material-change audit records with correlation and retention boundaries. |
| [currency-context](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/currency-context) | liberusoftware/currency-context | — | — | Precise money values, ISO currency metadata, context, formatting, and exchange-rate contracts. |
| [developer-experience](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/developer-experience) | liberusoftware/developer-experience | — | — | Foundation diagnostics and reproducible development/quality conventions. |
| [feature-flags](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/feature-flags) | liberusoftware/feature-flags | — | — | Typed rollout flags with stable environment, tenant, and actor targeting. |
| [files-media](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/files-media) | liberusoftware/files-media | — | — | Secure upload policy, malware-scanner contract, media metadata, access, and retention foundations. |
| [identity-core](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/identity-core) | liberusoftware/identity-core | — | — | Provider-neutral identity policy, normalization, and versioned security events. |
| [identity-core-filament](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/identity-core-filament) | liberusoftware/identity-core-filament | — | — | Filament administration adapter for the configured Liberu identity model. |
| [identity-socialstream](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/identity-socialstream) | liberusoftware/identity-socialstream | — | — | Socialstream/Socialite identity-linking provider adapter. |
| [import-export](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/import-export) | liberusoftware/import-export | — | — | Versioned transfer schemas, mapping, dry runs, validation, queued progress, reports, and retention. |
| [integrations](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/integrations) | liberusoftware/integrations | — | — | Provider adapter registry and protected connection lifecycle. |
| [integrations-google](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/integrations-google) | liberusoftware/integrations-google | — | — | Google Ads, Google Calendar, Gmail, and YouTube integration services. |
| [integrations-imap-pop3](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/integrations-imap-pop3) | liberusoftware/integrations-imap-pop3 | — | — | IMAP and POP3 email integration services. |
| [integrations-linkedin](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/integrations-linkedin) | liberusoftware/integrations-linkedin | — | — | LinkedIn organic and LinkedIn Ads integration services. |
| [integrations-mailchimp](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/integrations-mailchimp) | liberusoftware/integrations-mailchimp | — | — | MailChimp marketing integration service. |
| [integrations-meta](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/integrations-meta) | liberusoftware/integrations-meta | — | — | Facebook, Facebook Ads, Facebook Messenger, Instagram, and WhatsApp Business integration services. |
| [integrations-microsoft](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/integrations-microsoft) | liberusoftware/integrations-microsoft | — | — | Outlook Mail and Outlook Calendar integration services. |
| [integrations-sso](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/integrations-sso) | liberusoftware/integrations-sso | — | — | OIDC and SAML SSO connections, controllers, middleware, and JIT provisioning. |
| [integrations-stripe](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/integrations-stripe) | liberusoftware/integrations-stripe | — | — | Stripe billing and subscription integration service. |
| [integrations-twilio](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/integrations-twilio) | liberusoftware/integrations-twilio | — | — | Twilio voice, SMS, OAuth provider, and call settings integration. |
| [integrations-twitter](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/integrations-twitter) | liberusoftware/integrations-twitter | — | — | Twitter / X integration service. |
| [integrations-zernio](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/integrations-zernio) | liberusoftware/integrations-zernio | — | — | Zernio publishing, advertising, webhook, and tenant provisioning integration. |
| [jetstream-bridge](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/jetstream-bridge) | liberusoftware/jetstream-bridge | — | — | Fortify and Jetstream-compatible action adapters for Liberu identity capabilities. |
| [localization-core](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/localization-core) | liberusoftware/localization-core | — | — | Locale resolution, preferences, propagation, and UI direction for Liberu applications. |
| [localization-core-livewire](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/localization-core-livewire) | liberusoftware/localization-core-livewire | — | — | Livewire locale-switching presentation adapter for Liberu Localization. |
| [localization-mymemory](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/localization-mymemory) | liberusoftware/localization-mymemory | — | — | MyMemory machine-translation adapter for Liberu Localization. |
| [module-manager](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/module-manager) | liberusoftware/module-manager | — | — | Deterministic manifest discovery and runtime enablement for Liberu modules. |
| [module-manager-filament](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/module-manager-filament) | liberusoftware/module-manager-filament | — | — | Filament page for enabling and disabling Liberu feature modules. |
| [notifications](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/notifications) | liberusoftware/notifications | — | — | Localized notification preferences, channel policy, inbox delivery state, and quiet hours. |
| [observability](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/observability) | liberusoftware/observability | — | — | Structured diagnostics, monitoring dashboards, health signals, and redaction defaults. |
| [organizations-teams](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/organizations-teams) | liberusoftware/organizations-teams | — | — | Organization, team, membership, invitation, ownership, and context foundation. |
| [organizations-teams-filament](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/organizations-teams-filament) | liberusoftware/organizations-teams-filament | — | — | Filament administration adapter for organizations and teams. |
| [passkeys](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/passkeys) | liberusoftware/passkeys | — | — | WebAuthn / FIDO2 passkey registration, discoverable passwordless sign-in, step-up authentication, and clone detection for Liberu. |
| [profiles](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/profiles) | liberusoftware/profiles | — | — | Controlled profile updates and user presentation preferences. |
| [roles-permissions](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/roles-permissions) | liberusoftware/roles-permissions | — | — | Contextual roles, permissions, policies, and authorization safeguards. |
| [roles-permissions-filament](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/roles-permissions-filament) | liberusoftware/roles-permissions-filament | — | — | Filament Shield presentation adapter for Liberu authorization. |
| [scheduler-queues](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/scheduler-queues) | liberusoftware/scheduler-queues | — | — | Queue idempotency, retry, failure, scheduling, locking, and deployment conventions. |
| [search](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/search) | liberusoftware/search | — | — | Provider-neutral authorized search contracts and local Eloquent driver. |
| [search-api](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/search-api) | liberusoftware/search-api | — | — | HTTP API presentation adapter for Liberu Search. |
| [sessions-devices](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/sessions-devices) | liberusoftware/sessions-devices | — | — | Privacy-conscious session inventory and revocation. |
| [sessions-devices-filament](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/sessions-devices-filament) | liberusoftware/sessions-devices-filament | — | — | Filament account-security presentation adapter for Liberu Sessions and Devices. |
| [settings](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/settings) | liberusoftware/settings | — | — | Typed scoped settings foundation for Liberu applications. |
| [settings-filament](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/settings-filament) | liberusoftware/settings-filament | — | — | Filament administration adapter for Liberu Settings. |
| [tenancy](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/tenancy) | liberusoftware/tenancy | — | — | Shared Filament and Jetstream team tenancy with scoped runtime context and Eloquent isolation. |
| [theme-support](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/theme-support) | liberusoftware/theme-support | — | — | Theme discovery and host presentation support for Liberu applications. |
| [theme-support-livewire](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/theme-support-livewire) | liberusoftware/theme-support-livewire | — | — | Livewire theme-switching presentation adapter for Liberu Theme Support. |
| [two-factor-authentication](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/two-factor-authentication) | liberusoftware/two-factor-authentication | — | — | TOTP enforcement policy and one-time recovery-code primitives. |
| [users-roles](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/users-roles) | liberusoftware/users-roles | — | — | Shared users, role lookup, user policies, and user factories. |
| [webhooks](https://github.com/liberusoftware/project-boilerplate-laravel-filament/tree/main/modules/webhooks) | liberusoftware/webhooks | — | — | Signed filtered webhook endpoints, durable delivery attempts, retry, replay, and secret rotation. |
