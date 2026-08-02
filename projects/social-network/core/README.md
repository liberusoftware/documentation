# Social Network Core Modules

This index covers the Laravel 13/PHP 8.5 core Composer packages for the Social Network domain. Each module is independently installable, testable, versioned, and usable by enterprise applications, small businesses, and personal users. Presentation adapters consume the core package; they do not own its business rules.

| Module                            | Core package                        | Domain specification                    |
| --------------------------------- | ----------------------------------- | --------------------------------------- |
| [Analytics](analytics.md)         | module-social-network-analytics     | [Feature](../features/analytics.md)     |
| [Communities](communities.md)     | module-social-network-communities   | [Feature](../features/communities.md)   |
| [Discovery](discovery.md)         | module-social-network-discovery     | [Feature](../features/discovery.md)     |
| [Engagement](engagement.md)       | module-social-network-engagement    | [Feature](../features/engagement.md)    |
| [Events](events.md)               | module-social-network-events        | [Feature](../features/events.md)        |
| [Federation](federation.md)       | module-social-network-federation    | [Feature](../features/federation.md)    |
| [Feed](feed.md)                   | module-social-network-feed          | [Feature](../features/feed.md)          |
| [Media](media.md)                 | module-social-network-media         | [Feature](../features/media.md)         |
| [Messaging](messaging.md)         | module-social-network-messaging     | [Feature](../features/messaging.md)     |
| [Moderation](moderation.md)       | module-social-network-moderation    | [Feature](../features/moderation.md)    |
| [Notifications](notifications.md) | module-social-network-notifications | [Feature](../features/notifications.md) |
| [Profiles](profiles.md)           | module-social-network-profiles      | [Feature](../features/profiles.md)      |
| [Publishing](publishing.md)       | module-social-network-publishing    | [Feature](../features/publishing.md)    |
| [Social Core](social-core.md)     | module-social-network-social-core   | [Feature](../features/social-core.md)   |
| [Social Graph](social-graph.md)   | module-social-network-social-graph  | [Feature](../features/social-graph.md)  |

## Shared implementation contract

Every core package applies the DDD, Laravel, PHP, database, security, services, jobs, documentation, and testing standards linked from [MODULES.md](../../../architecture/MODULES.md), [Laravel 13](../../../standards/LARAVEL.md), [PHP 8.5](../../../standards/PHP.md), [domain-driven design](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), and [testing](../../../standards/TESTING.md). It owns its domain model, application use cases, policies, persistence, events, jobs, contracts, lifecycle, recovery, and user-safe operational behavior. API, Filament, Livewire, React, Vue, and Nuxt packages depend on the public core boundary and never reimplement it.
