# Social Network Flutter + Dart implementations

**Scope:** [Social Network](../SOCIAL-NETWORK.md)
**Architecture:** [Mobile](../../../architecture/MOBILE.md) · [API](../api/README.md) · [Core](../core/README.md)
**Technology:** [Flutter technology](../../../technologies/FLUTTER.md) · [Flutter standard](../../../standards/FLUTTER.md)

This index defines the optional Flutter + Dart adapter boundary for the Social Network project. Each future module adapter must map one-to-one to an existing core/API capability, preserve the server contract, and remain independently testable. Product-specific domain behavior stays in the project feature and core documentation.

## Implementation plan

- Consume the matching versioned API contract; do not query private tables or duplicate Laravel authorization, tenant resolution, audit, or business rules.
- Provide platform-appropriate navigation, screens/widgets, forms, validation feedback, loading/empty/denied/offline/conflict/recovery states, and localization.
- Document native permissions, secure credential storage, deep links, push notifications, cache classification, offline mutation policy, and supported OS/device matrix.
- Test API schemas and authorization, state transitions, accessibility, localization, lifecycle interruptions, permission denial, offline recovery, and signed release builds.
- Keep package naming consistent: `module-{independent-module-name}-flutter`; host applications choose only the adapters they need.

## Related module indexes

- [Core domain modules](../core/README.md)
- [API modules](../api/README.md)
- [All mobile project indexes](../../../modules/mobile/README.md)
- [Flutter + Dart module standard](../../../modules/flutter/README.md)

This project may ship no mobile client, one mobile client, or both. A missing adapter is an explicit product decision and must not be interpreted as permission to move domain behavior into the client.

## Complete module index

The following 15 adapters map one-to-one to the project core and API indexes. Each module document is the implementation plan for this surface.

| Module                            | Package                                     | Core                             | API                            |
| --------------------------------- | ------------------------------------------- | -------------------------------- | ------------------------------ |
| [Analytics](analytics.md)         | module-social-network-analytics-flutter     | [Core](../core/analytics.md)     | [API](../api/analytics.md)     |
| [Communities](communities.md)     | module-social-network-communities-flutter   | [Core](../core/communities.md)   | [API](../api/communities.md)   |
| [Discovery](discovery.md)         | module-social-network-discovery-flutter     | [Core](../core/discovery.md)     | [API](../api/discovery.md)     |
| [Engagement](engagement.md)       | module-social-network-engagement-flutter    | [Core](../core/engagement.md)    | [API](../api/engagement.md)    |
| [Events](events.md)               | module-social-network-events-flutter        | [Core](../core/events.md)        | [API](../api/events.md)        |
| [Federation](federation.md)       | module-social-network-federation-flutter    | [Core](../core/federation.md)    | [API](../api/federation.md)    |
| [Feed](feed.md)                   | module-social-network-feed-flutter          | [Core](../core/feed.md)          | [API](../api/feed.md)          |
| [Media](media.md)                 | module-social-network-media-flutter         | [Core](../core/media.md)         | [API](../api/media.md)         |
| [Messaging](messaging.md)         | module-social-network-messaging-flutter     | [Core](../core/messaging.md)     | [API](../api/messaging.md)     |
| [Moderation](moderation.md)       | module-social-network-moderation-flutter    | [Core](../core/moderation.md)    | [API](../api/moderation.md)    |
| [Notifications](notifications.md) | module-social-network-notifications-flutter | [Core](../core/notifications.md) | [API](../api/notifications.md) |
| [Profiles](profiles.md)           | module-social-network-profiles-flutter      | [Core](../core/profiles.md)      | [API](../api/profiles.md)      |
| [Publishing](publishing.md)       | module-social-network-publishing-flutter    | [Core](../core/publishing.md)    | [API](../api/publishing.md)    |
| [Social Core](social-core.md)     | module-social-network-social-core-flutter   | [Core](../core/social-core.md)   | [API](../api/social-core.md)   |
| [Social Graph](social-graph.md)   | module-social-network-social-graph-flutter  | [Core](../core/social-graph.md)  | [API](../api/social-graph.md)  |
