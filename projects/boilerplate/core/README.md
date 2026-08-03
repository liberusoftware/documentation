# Boilerplate Core module implementations

This index lists the independently installable domain packages for the shared Liberu foundation. Each entry maps one-to-one to the canonical module catalog in [BOILERPLATE.md](../BOILERPLATE.md).

Core packages own domain behavior, persistence, policies, events, jobs, contracts, lifecycle, recovery, and tests. They never depend on a presentation layer.

| Module                                                    | Composer package                   | Documentation                                       |
| --------------------------------------------------------- | ---------------------------------- | --------------------------------------------------- |
| [Application Core](application-core.md)                   | `module-application-core`          | [Implementation plan](application-core.md)          |
| [Module Manager](module-manager.md)                       | `module-module-manager`            | [Implementation plan](module-manager.md)            |
| [Identity](identity.md)                                   | `module-identity`                  | [Implementation plan](identity.md)                  |
| [Two-Factor Authentication](two-factor-authentication.md) | `module-two-factor-authentication` | [Implementation plan](two-factor-authentication.md) |
| [Sessions and Devices](sessions-and-devices.md)           | `module-sessions-and-devices`      | [Implementation plan](sessions-and-devices.md)      |
| [Jetstream Bridge](jetstream-bridge.md)                   | `module-jetstream-bridge`          | [Implementation plan](jetstream-bridge.md)          |
| [Profiles](profiles.md)                                   | `module-profiles`                  | [Implementation plan](profiles.md)                  |
| [Organizations and Teams](organizations-and-teams.md)     | `module-organizations-and-teams`   | [Implementation plan](organizations-and-teams.md)   |
| [Roles and Permissions](roles-and-permissions.md)         | `module-roles-and-permissions`     | [Implementation plan](roles-and-permissions.md)     |
| [Localization](localization.md)                           | `module-localization`              | [Implementation plan](localization.md)              |
| [Currency Context](currency-context.md)                   | `module-currency-context`          | [Implementation plan](currency-context.md)          |
| [Notifications](notifications.md)                         | `module-notifications`             | [Implementation plan](notifications.md)             |
| [Files and Media](files-and-media.md)                     | `module-files-and-media`           | [Implementation plan](files-and-media.md)           |
| [Search](search.md)                                       | `module-search`                    | [Implementation plan](search.md)                    |
| [Audit](audit.md)                                         | `module-audit`                     | [Implementation plan](audit.md)                     |
| [Feature Flags](feature-flags.md)                         | `module-feature-flags`             | [Implementation plan](feature-flags.md)             |
| [API Access](api-access.md)                               | `module-api-access`                | [Implementation plan](api-access.md)                |
| [Webhooks](webhooks.md)                                   | `module-webhooks`                  | [Implementation plan](webhooks.md)                  |
| [Integrations](integrations.md)                           | `module-integrations`              | [Implementation plan](integrations.md)              |
| [Analytics Core](analytics-core.md)                       | `module-analytics-core`            | [Implementation plan](analytics-core.md)            |
| [Google Analytics](google-analytics.md)                   | `module-google-analytics`          | [Implementation plan](google-analytics.md)          |
| [Meta Server-Side Tracking](meta-server-side-tracking.md) | `module-meta-server-side-tracking` | [Implementation plan](meta-server-side-tracking.md) |
| [Import and Export](import-and-export.md)                 | `module-import-and-export`         | [Implementation plan](import-and-export.md)         |
| [Activity and Comments](activity-and-comments.md)         | `module-activity-and-comments`     | [Implementation plan](activity-and-comments.md)     |
| [Settings](settings.md)                                   | `module-settings`                  | [Implementation plan](settings.md)                  |
| [Scheduler and Queues](scheduler-and-queues.md)           | `module-scheduler-and-queues`      | [Implementation plan](scheduler-and-queues.md)      |
| [Observability](observability.md)                         | `module-observability`             | [Implementation plan](observability.md)             |
| [Developer Experience](developer-experience.md)           | `module-developer-experience`      | [Implementation plan](developer-experience.md)      |

## Shared delivery contract

Every package targets Laravel 13 and PHP 8.5, uses strict types and typed public boundaries, documents configuration and permissions, and ships independent tests, migrations, upgrade notes, and a compatibility matrix.

See [modules/core](../../../modules/core/README.md), [MODULES.md](../../../architecture/MODULES.md), [DDD patterns](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), [security](../../../architecture/SECURITY.md), and [testing](../../../standards/TESTING.md).
