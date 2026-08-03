# Boilerplate Filament 5 module implementations

This index lists the independently installable Filament presentation packages for the shared Liberu foundation. Each entry maps one-to-one to the canonical module catalog in [BOILERPLATE.md](../BOILERPLATE.md).

These adapters translate the matching core package into Filament 5 conventions. They contain transport or view composition only; authorization and business rules remain in the core package.

| Module                                                    | Composer package                            | Documentation                                       |
| --------------------------------------------------------- | ------------------------------------------- | --------------------------------------------------- |
| [Application Core](application-core.md)                   | `module-application-core-filament`          | [Implementation plan](application-core.md)          |
| [Module Manager](module-manager.md)                       | `module-module-manager-filament`            | [Implementation plan](module-manager.md)            |
| [Identity](identity.md)                                   | `module-identity-filament`                  | [Implementation plan](identity.md)                  |
| [Two-Factor Authentication](two-factor-authentication.md) | `module-two-factor-authentication-filament` | [Implementation plan](two-factor-authentication.md) |
| [Sessions and Devices](sessions-and-devices.md)           | `module-sessions-and-devices-filament`      | [Implementation plan](sessions-and-devices.md)      |
| [Jetstream Bridge](jetstream-bridge.md)                   | `module-jetstream-bridge-filament`          | [Implementation plan](jetstream-bridge.md)          |
| [Profiles](profiles.md)                                   | `module-profiles-filament`                  | [Implementation plan](profiles.md)                  |
| [Organizations and Teams](organizations-and-teams.md)     | `module-organizations-and-teams-filament`   | [Implementation plan](organizations-and-teams.md)   |
| [Roles and Permissions](roles-and-permissions.md)         | `module-roles-and-permissions-filament`     | [Implementation plan](roles-and-permissions.md)     |
| [Localization](localization.md)                           | `module-localization-filament`              | [Implementation plan](localization.md)              |
| [Currency Context](currency-context.md)                   | `module-currency-context-filament`          | [Implementation plan](currency-context.md)          |
| [Notifications](notifications.md)                         | `module-notifications-filament`             | [Implementation plan](notifications.md)             |
| [Files and Media](files-and-media.md)                     | `module-files-and-media-filament`           | [Implementation plan](files-and-media.md)           |
| [Search](search.md)                                       | `module-search-filament`                    | [Implementation plan](search.md)                    |
| [Audit](audit.md)                                         | `module-audit-filament`                     | [Implementation plan](audit.md)                     |
| [Feature Flags](feature-flags.md)                         | `module-feature-flags-filament`             | [Implementation plan](feature-flags.md)             |
| [API Access](api-access.md)                               | `module-api-access-filament`                | [Implementation plan](api-access.md)                |
| [Webhooks](webhooks.md)                                   | `module-webhooks-filament`                  | [Implementation plan](webhooks.md)                  |
| [Integrations](integrations.md)                           | `module-integrations-filament`              | [Implementation plan](integrations.md)              |
| [Analytics Core](analytics-core.md)                       | `module-analytics-core-filament`            | [Implementation plan](analytics-core.md)            |
| [Google Analytics](google-analytics.md)                   | `module-google-analytics-filament`          | [Implementation plan](google-analytics.md)          |
| [Meta Server-Side Tracking](meta-server-side-tracking.md) | `module-meta-server-side-tracking-filament` | [Implementation plan](meta-server-side-tracking.md) |
| [Import and Export](import-and-export.md)                 | `module-import-and-export-filament`         | [Implementation plan](import-and-export.md)         |
| [Activity and Comments](activity-and-comments.md)         | `module-activity-and-comments-filament`     | [Implementation plan](activity-and-comments.md)     |
| [Settings](settings.md)                                   | `module-settings-filament`                  | [Implementation plan](settings.md)                  |
| [Scheduler and Queues](scheduler-and-queues.md)           | `module-scheduler-and-queues-filament`      | [Implementation plan](scheduler-and-queues.md)      |
| [Observability](observability.md)                         | `module-observability-filament`             | [Implementation plan](observability.md)             |
| [Developer Experience](developer-experience.md)           | `module-developer-experience-filament`      | [Implementation plan](developer-experience.md)      |

## Shared delivery contract

Every package targets Laravel 13 and PHP 8.5, uses strict types and typed public boundaries, documents configuration and permissions, and ships independent tests, migrations, upgrade notes, and a compatibility matrix.

See [modules/filament](../../../modules/filament/README.md), [API architecture](../../../architecture/API.md), [themes](../../../standards/THEMES.md), and [testing](../../../standards/TESTING.md).
