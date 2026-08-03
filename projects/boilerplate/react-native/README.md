# Boilerplate foundation React Native + Expo implementations

**Scope:** [Boilerplate foundation](../BOILERPLATE.md)
**Architecture:** [Mobile](../../../architecture/MOBILE.md) · [API](../api/README.md) · [Core](../core/README.md)
**Technology:** [React Native technology](../../../technologies/REACT-NATIVE.md) · [React Native standard](../../../standards/REACT-NATIVE.md)

This index defines the optional React Native + Expo adapter boundary for the Boilerplate foundation project. Each future module adapter must map one-to-one to an existing core/API capability, preserve the server contract, and remain independently testable. Product-specific domain behavior stays in the project feature and core documentation.

## Implementation plan

- Consume the matching versioned API contract; do not query private tables or duplicate Laravel authorization, tenant resolution, audit, or business rules.
- Provide platform-appropriate navigation, screens/widgets, forms, validation feedback, loading/empty/denied/offline/conflict/recovery states, and localization.
- Document native permissions, secure credential storage, deep links, push notifications, cache classification, offline mutation policy, and supported OS/device matrix.
- Test API schemas and authorization, state transitions, accessibility, localization, lifecycle interruptions, permission denial, offline recovery, and signed release builds.
- Keep package naming consistent: `module-{independent-module-name}-react-native`; host applications choose only the adapters they need.

## Related module indexes

- [Core domain modules](../core/README.md)
- [API modules](../api/README.md)
- [All mobile project indexes](../../../modules/mobile/README.md)
- [React Native + Expo module standard](../../../modules/react-native/README.md)

This project may ship no mobile client, one mobile client, or both. A missing adapter is an explicit product decision and must not be interpreted as permission to move domain behavior into the client.

## Complete module index

The following 28 adapters map one-to-one to the project core and API indexes. Each module document is the implementation plan for this surface.

| Module                                                                    | Package                                       | Core                                         | API                                        |
| ------------------------------------------------------------------------- | --------------------------------------------- | -------------------------------------------- | ------------------------------------------ |
| [Activity and Comments domain packages](activity-and-comments.md)         | module-activity-and-comments-react-native     | [Core](../core/activity-and-comments.md)     | [API](../api/activity-and-comments.md)     |
| [Analytics Core domain packages](analytics-core.md)                       | module-analytics-core-react-native            | [Core](../core/analytics-core.md)            | [API](../api/analytics-core.md)            |
| [API Access domain packages](api-access.md)                               | module-api-access-react-native                | [Core](../core/api-access.md)                | [API](../api/api-access.md)                |
| [Application Core domain packages](application-core.md)                   | module-application-core-react-native          | [Core](../core/application-core.md)          | [API](../api/application-core.md)          |
| [Audit domain packages](audit.md)                                         | module-audit-react-native                     | [Core](../core/audit.md)                     | [API](../api/audit.md)                     |
| [Currency Context domain packages](currency-context.md)                   | module-currency-context-react-native          | [Core](../core/currency-context.md)          | [API](../api/currency-context.md)          |
| [Developer Experience domain packages](developer-experience.md)           | module-developer-experience-react-native      | [Core](../core/developer-experience.md)      | [API](../api/developer-experience.md)      |
| [Feature Flags domain packages](feature-flags.md)                         | module-feature-flags-react-native             | [Core](../core/feature-flags.md)             | [API](../api/feature-flags.md)             |
| [Files and Media domain packages](files-and-media.md)                     | module-files-and-media-react-native           | [Core](../core/files-and-media.md)           | [API](../api/files-and-media.md)           |
| [Google Analytics domain packages](google-analytics.md)                   | module-google-analytics-react-native          | [Core](../core/google-analytics.md)          | [API](../api/google-analytics.md)          |
| [Identity domain packages](identity.md)                                   | module-identity-react-native                  | [Core](../core/identity.md)                  | [API](../api/identity.md)                  |
| [Import and Export domain packages](import-and-export.md)                 | module-import-and-export-react-native         | [Core](../core/import-and-export.md)         | [API](../api/import-and-export.md)         |
| [Integrations domain packages](integrations.md)                           | module-integrations-react-native              | [Core](../core/integrations.md)              | [API](../api/integrations.md)              |
| [Jetstream Bridge domain packages](jetstream-bridge.md)                   | module-jetstream-bridge-react-native          | [Core](../core/jetstream-bridge.md)          | [API](../api/jetstream-bridge.md)          |
| [Localization domain packages](localization.md)                           | module-localization-react-native              | [Core](../core/localization.md)              | [API](../api/localization.md)              |
| [Meta Server-Side Tracking domain packages](meta-server-side-tracking.md) | module-meta-server-side-tracking-react-native | [Core](../core/meta-server-side-tracking.md) | [API](../api/meta-server-side-tracking.md) |
| [Module Manager domain packages](module-manager.md)                       | module-module-manager-react-native            | [Core](../core/module-manager.md)            | [API](../api/module-manager.md)            |
| [Notifications domain packages](notifications.md)                         | module-notifications-react-native             | [Core](../core/notifications.md)             | [API](../api/notifications.md)             |
| [Observability domain packages](observability.md)                         | module-observability-react-native             | [Core](../core/observability.md)             | [API](../api/observability.md)             |
| [Organizations and Teams domain packages](organizations-and-teams.md)     | module-organizations-and-teams-react-native   | [Core](../core/organizations-and-teams.md)   | [API](../api/organizations-and-teams.md)   |
| [Profiles domain packages](profiles.md)                                   | module-profiles-react-native                  | [Core](../core/profiles.md)                  | [API](../api/profiles.md)                  |
| [Roles and Permissions domain packages](roles-and-permissions.md)         | module-roles-and-permissions-react-native     | [Core](../core/roles-and-permissions.md)     | [API](../api/roles-and-permissions.md)     |
| [Scheduler and Queues domain packages](scheduler-and-queues.md)           | module-scheduler-and-queues-react-native      | [Core](../core/scheduler-and-queues.md)      | [API](../api/scheduler-and-queues.md)      |
| [Search domain packages](search.md)                                       | module-search-react-native                    | [Core](../core/search.md)                    | [API](../api/search.md)                    |
| [Sessions and Devices domain packages](sessions-and-devices.md)           | module-sessions-and-devices-react-native      | [Core](../core/sessions-and-devices.md)      | [API](../api/sessions-and-devices.md)      |
| [Settings domain packages](settings.md)                                   | module-settings-react-native                  | [Core](../core/settings.md)                  | [API](../api/settings.md)                  |
| [Two-Factor Authentication domain packages](two-factor-authentication.md) | module-two-factor-authentication-react-native | [Core](../core/two-factor-authentication.md) | [API](../api/two-factor-authentication.md) |
| [Webhooks domain packages](webhooks.md)                                   | module-webhooks-react-native                  | [Core](../core/webhooks.md)                  | [API](../api/webhooks.md)                  |
