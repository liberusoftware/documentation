# Sap: observed source modules

Observed repository: [enterprise-sap-laravel](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041).

This is a manifest inventory, not a claim that a module is complete, tested, independently released, or available from a registry. Planned feature specifications may use different names. Use the exact manifest identity for dependency resolution.

Found **40 immediate directories under `modules/`**. This count does not measure capabilities implemented elsewhere in the application. Existing documented modules are preserved independently of their current source location. See [inventory method and shared identities](../../architecture/SOURCE-INVENTORY.md).

Of these, **0 are symlink aliases**, not additional package implementations. Their target directories are recorded below and are counted once in shared-package comparisons.

## Other source locations

Application-owned implementation can precede package extraction. These tracked locations must also be reviewed before making availability or ownership claims.

| Source root | Tracked files |
| --- | ---: |
| [app/](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/app) | 5 |
| [routes/](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/routes) | 5 |
| [resources/](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/resources) | 35 |
| [database/](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/database) | 9 |
| [tests/](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/tests) | 49 |

Other manifest paths: `composer.json`, `package.json`, `scripts/composer.json`, `themes/base/composer.json`, `themes/clear-signal/composer.json`, `themes/dark/composer.json`, `themes/default/composer.json`.

## Immediate module manifests

| Module directory | Composer identity | npm identity | Alias target | Description |
| --- | --- | --- | --- | --- |
| [activity-comments](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/activity-comments) | liberusoftware/activity-comments | — | — | Generic authorized timelines, comments, mentions, subscriptions, attachments, and visibility. |
| [analytics-core](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/analytics-core) | liberusoftware/analytics-core | — | — | Consent-aware provider-neutral analytics event routing and durable delivery evidence. |
| [analytics-google](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/analytics-google) | liberusoftware/analytics-google | — | — | Consent-aware Google Analytics event mapping adapter. |
| [analytics-meta](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/analytics-meta) | liberusoftware/analytics-meta | — | — | Consent-aware Meta server-side event mapping and normalized customer-data adapter. |
| [api-access](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/api-access) | liberusoftware/api-access | — | — | API token, scope, version, rate-limit, idempotency, and revocation policy. |
| [application](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/application) | liberusoftware/application | — | — | Required application metadata, health, clocks, identifiers, and secure HTTP defaults. |
| [audit](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/audit) | liberusoftware/audit | — | — | Contextual material-change audit records with correlation and retention boundaries. |
| [currency-context](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/currency-context) | liberusoftware/currency-context | — | — | Precise money values, ISO currency metadata, context, formatting, and exchange-rate contracts. |
| [developer-experience](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/developer-experience) | liberusoftware/developer-experience | — | — | Foundation diagnostics and reproducible development/quality conventions. |
| [feature-flags](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/feature-flags) | liberusoftware/feature-flags | — | — | Typed rollout flags with stable environment, tenant, and actor targeting. |
| [files-media](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/files-media) | liberusoftware/files-media | — | — | Secure upload policy, malware-scanner contract, media metadata, access, and retention foundations. |
| [identity-core](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/identity-core) | liberusoftware/identity-core | — | — | Provider-neutral identity policy, normalization, and versioned security events. |
| [identity-core-filament](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/identity-core-filament) | liberusoftware/identity-core-filament | — | — | Filament administration adapter for the configured Liberu identity model. |
| [identity-socialstream](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/identity-socialstream) | liberusoftware/identity-socialstream | — | — | Socialstream/Socialite identity-linking provider adapter. |
| [import-export](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/import-export) | liberusoftware/import-export | — | — | Versioned transfer schemas, mapping, dry runs, validation, queued progress, reports, and retention. |
| [integrations](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/integrations) | liberusoftware/integrations | — | — | Provider adapter registry and protected connection lifecycle. |
| [jetstream-bridge](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/jetstream-bridge) | liberusoftware/jetstream-bridge | — | — | Fortify and Jetstream-compatible action adapters for Liberu identity capabilities. |
| [localization-core](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/localization-core) | liberusoftware/localization-core | — | — | Locale resolution, preferences, propagation, and UI direction for Liberu applications. |
| [localization-core-livewire](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/localization-core-livewire) | liberusoftware/localization-core-livewire | — | — | Livewire locale-switching presentation adapter for Liberu Localization. |
| [localization-mymemory](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/localization-mymemory) | liberusoftware/localization-mymemory | — | — | MyMemory machine-translation adapter for Liberu Localization. |
| [module-manager](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/module-manager) | liberusoftware/module-manager | — | — | Deterministic manifest discovery and runtime enablement for Liberu modules. |
| [module-manager-filament](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/module-manager-filament) | liberusoftware/module-manager-filament | — | — | Filament operations presentation adapter for the Liberu Module Manager. |
| [notifications](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/notifications) | liberusoftware/notifications | — | — | Localized notification preferences, channel policy, inbox delivery state, and quiet hours. |
| [observability](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/observability) | liberusoftware/observability | — | — | Structured diagnostics, monitoring dashboards, health signals, and redaction defaults. |
| [organizations-teams](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/organizations-teams) | liberusoftware/organizations-teams | — | — | Organization, team, membership, invitation, ownership, and context foundation. |
| [organizations-teams-filament](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/organizations-teams-filament) | liberusoftware/organizations-teams-filament | — | — | Filament administration adapter for organizations and teams. |
| [profiles](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/profiles) | liberusoftware/profiles | — | — | Controlled profile updates and user presentation preferences. |
| [roles-permissions](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/roles-permissions) | liberusoftware/roles-permissions | — | — | Contextual roles, permissions, policies, and authorization safeguards. |
| [roles-permissions-filament](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/roles-permissions-filament) | liberusoftware/roles-permissions-filament | — | — | Filament Shield presentation adapter for Liberu authorization. |
| [scheduler-queues](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/scheduler-queues) | liberusoftware/scheduler-queues | — | — | Queue idempotency, retry, failure, scheduling, locking, and deployment conventions. |
| [search](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/search) | liberusoftware/search | — | — | Provider-neutral authorized search contracts and local Eloquent driver. |
| [search-api](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/search-api) | liberusoftware/search-api | — | — | HTTP API presentation adapter for Liberu Search. |
| [sessions-devices](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/sessions-devices) | liberusoftware/sessions-devices | — | — | Privacy-conscious session inventory and revocation. |
| [sessions-devices-filament](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/sessions-devices-filament) | liberusoftware/sessions-devices-filament | — | — | Filament account-security presentation adapter for Liberu Sessions and Devices. |
| [settings](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/settings) | liberusoftware/settings | — | — | Typed scoped settings foundation for Liberu applications. |
| [settings-filament](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/settings-filament) | liberusoftware/settings-filament | — | — | Filament administration adapter for Liberu Settings. |
| [theme-support](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/theme-support) | liberusoftware/theme-support | — | — | Theme discovery and host presentation support for Liberu applications. |
| [theme-support-livewire](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/theme-support-livewire) | liberusoftware/theme-support-livewire | — | — | Livewire theme-switching presentation adapter for Liberu Theme Support. |
| [two-factor-authentication](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/two-factor-authentication) | liberusoftware/two-factor-authentication | — | — | TOTP enforcement policy and one-time recovery-code primitives. |
| [webhooks](https://github.com/liberusoftware/enterprise-sap-laravel/tree/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/webhooks) | liberusoftware/webhooks | — | — | Signed filtered webhook endpoints, durable delivery attempts, retry, replay, and secret rotation. |
