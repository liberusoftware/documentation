# Boilerplate Nuxt 4 module implementations

This index lists the independently installable Nuxt presentation packages for the shared Liberu foundation. Each entry maps one-to-one to the canonical module catalog in [BOILERPLATE.md](../BOILERPLATE.md).

These adapters translate the matching core package into Nuxt 4 conventions. They contain transport or view composition only; authorization and business rules remain in the core package.

| Module                                                    | Composer package                        | Documentation                                       |
| --------------------------------------------------------- | --------------------------------------- | --------------------------------------------------- |
| [Application Core](application-core.md)                   | `module-application-core-nuxt`          | [Implementation plan](application-core.md)          |
| [Module Manager](module-manager.md)                       | `module-module-manager-nuxt`            | [Implementation plan](module-manager.md)            |
| [Identity](identity.md)                                   | `module-identity-nuxt`                  | [Implementation plan](identity.md)                  |
| [Two-Factor Authentication](two-factor-authentication.md) | `module-two-factor-authentication-nuxt` | [Implementation plan](two-factor-authentication.md) |
| [Sessions and Devices](sessions-and-devices.md)           | `module-sessions-and-devices-nuxt`      | [Implementation plan](sessions-and-devices.md)      |
| [Jetstream Bridge](jetstream-bridge.md)                   | `module-jetstream-bridge-nuxt`          | [Implementation plan](jetstream-bridge.md)          |
| [Profiles](profiles.md)                                   | `module-profiles-nuxt`                  | [Implementation plan](profiles.md)                  |
| [Organizations and Teams](organizations-and-teams.md)     | `module-organizations-and-teams-nuxt`   | [Implementation plan](organizations-and-teams.md)   |
| [Roles and Permissions](roles-and-permissions.md)         | `module-roles-and-permissions-nuxt`     | [Implementation plan](roles-and-permissions.md)     |
| [Localization](localization.md)                           | `module-localization-nuxt`              | [Implementation plan](localization.md)              |
| [Currency Context](currency-context.md)                   | `module-currency-context-nuxt`          | [Implementation plan](currency-context.md)          |
| [Notifications](notifications.md)                         | `module-notifications-nuxt`             | [Implementation plan](notifications.md)             |
| [Files and Media](files-and-media.md)                     | `module-files-and-media-nuxt`           | [Implementation plan](files-and-media.md)           |
| [Search](search.md)                                       | `module-search-nuxt`                    | [Implementation plan](search.md)                    |
| [Audit](audit.md)                                         | `module-audit-nuxt`                     | [Implementation plan](audit.md)                     |
| [Feature Flags](feature-flags.md)                         | `module-feature-flags-nuxt`             | [Implementation plan](feature-flags.md)             |
| [API Access](api-access.md)                               | `module-api-access-nuxt`                | [Implementation plan](api-access.md)                |
| [Webhooks](webhooks.md)                                   | `module-webhooks-nuxt`                  | [Implementation plan](webhooks.md)                  |
| [Integrations](integrations.md)                           | `module-integrations-nuxt`              | [Implementation plan](integrations.md)              |
| [Analytics Core](analytics-core.md)                       | `module-analytics-core-nuxt`            | [Implementation plan](analytics-core.md)            |
| [Google Analytics](google-analytics.md)                   | `module-google-analytics-nuxt`          | [Implementation plan](google-analytics.md)          |
| [Meta Server-Side Tracking](meta-server-side-tracking.md) | `module-meta-server-side-tracking-nuxt` | [Implementation plan](meta-server-side-tracking.md) |
| [Import and Export](import-and-export.md)                 | `module-import-and-export-nuxt`         | [Implementation plan](import-and-export.md)         |
| [Activity and Comments](activity-and-comments.md)         | `module-activity-and-comments-nuxt`     | [Implementation plan](activity-and-comments.md)     |
| [Settings](settings.md)                                   | `module-settings-nuxt`                  | [Implementation plan](settings.md)                  |
| [Scheduler and Queues](scheduler-and-queues.md)           | `module-scheduler-and-queues-nuxt`      | [Implementation plan](scheduler-and-queues.md)      |
| [Observability](observability.md)                         | `module-observability-nuxt`             | [Implementation plan](observability.md)             |
| [Developer Experience](developer-experience.md)           | `module-developer-experience-nuxt`      | [Implementation plan](developer-experience.md)      |

## Shared delivery contract

Every package targets Laravel 13 and PHP 8.5, uses strict types and typed public boundaries, documents configuration and permissions, and ships independent tests, migrations, upgrade notes, and a compatibility matrix.

See [modules/nuxt](../../../modules/nuxt/README.md), [API architecture](../../../architecture/API.md), [themes](../../../standards/THEMES.md), and [testing](../../../standards/TESTING.md).
