# CMS React Native + Expo implementations

**Scope:** [CMS](../CMS.md)
**Architecture:** [Mobile](../../../architecture/MOBILE.md) · [API](../api/README.md) · [Core](../core/README.md)
**Technology:** [React Native technology](../../../technologies/REACT-NATIVE.md) · [React Native standard](../../../standards/REACT-NATIVE.md)

This index defines the optional React Native + Expo adapter boundary for the CMS project. Each future module adapter must map one-to-one to an existing core/API capability, preserve the server contract, and remain independently testable. Product-specific domain behavior stays in the project feature and core documentation.

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

The following 81 adapters map one-to-one to the project core and API indexes. Each module document is the implementation plan for this surface.

| Module                                                                | Package                                                 | Core                                               | API                                              |
| --------------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------ |
| [Accessibility Assistant](accessibility-assistant.md)                 | module-cms-accessibility-assistant-react-native         | [Core](../core/accessibility-assistant.md)         | [API](../api/accessibility-assistant.md)         |
| [Analytics Integration](analytics-integration.md)                     | module-cms-analytics-integration-react-native           | [Core](../core/analytics-integration.md)           | [API](../api/analytics-integration.md)           |
| [Audit And History](audit-and-history.md)                             | module-cms-audit-and-history-react-native               | [Core](../core/audit-and-history.md)               | [API](../api/audit-and-history.md)               |
| [Backup And Restore](backup-and-restore.md)                           | module-cms-backup-and-restore-react-native              | [Core](../core/backup-and-restore.md)              | [API](../api/backup-and-restore.md)              |
| [Block Editor](block-editor.md)                                       | module-cms-block-editor-react-native                    | [Core](../core/block-editor.md)                    | [API](../api/block-editor.md)                    |
| [Cache And Performance](cache-and-performance.md)                     | module-cms-cache-and-performance-react-native           | [Core](../core/cache-and-performance.md)           | [API](../api/cache-and-performance.md)           |
| [Cms Copilot](cms-copilot.md)                                         | module-cms-cms-copilot-react-native                     | [Core](../core/cms-copilot.md)                     | [API](../api/cms-copilot.md)                     |
| [Cms Core](cms-core.md)                                               | module-cms-cms-core-react-native                        | [Core](../core/cms-core.md)                        | [API](../api/cms-core.md)                        |
| [Comments And Discussion](comments-and-discussion.md)                 | module-cms-comments-and-discussion-react-native         | [Core](../core/comments-and-discussion.md)         | [API](../api/comments-and-discussion.md)         |
| [Configuration Management](configuration-management.md)               | module-cms-configuration-management-react-native        | [Core](../core/configuration-management.md)        | [API](../api/configuration-management.md)        |
| [Contact Directory](contact-directory.md)                             | module-cms-contact-directory-react-native               | [Core](../core/contact-directory.md)               | [API](../api/contact-directory.md)               |
| [Content Access](content-access.md)                                   | module-cms-content-access-react-native                  | [Core](../core/content-access.md)                  | [API](../api/content-access.md)                  |
| [Content Calendar](content-calendar.md)                               | module-cms-content-calendar-react-native                | [Core](../core/content-calendar.md)                | [API](../api/content-calendar.md)                |
| [Content Entities](content-entities.md)                               | module-cms-content-entities-react-native                | [Core](../core/content-entities.md)                | [API](../api/content-entities.md)                |
| [Content Federation](content-federation.md)                           | module-cms-content-federation-react-native              | [Core](../core/content-federation.md)              | [API](../api/content-federation.md)              |
| [Content Governance](content-governance.md)                           | module-cms-content-governance-react-native              | [Core](../core/content-governance.md)              | [API](../api/content-governance.md)              |
| [Content Integrity](content-integrity.md)                             | module-cms-content-integrity-react-native               | [Core](../core/content-integrity.md)               | [API](../api/content-integrity.md)               |
| [Content Intelligence](content-intelligence.md)                       | module-cms-content-intelligence-react-native            | [Core](../core/content-intelligence.md)            | [API](../api/content-intelligence.md)            |
| [Content Locking](content-locking.md)                                 | module-cms-content-locking-react-native                 | [Core](../core/content-locking.md)                 | [API](../api/content-locking.md)                 |
| [Content Search](content-search.md)                                   | module-cms-content-search-react-native                  | [Core](../core/content-search.md)                  | [API](../api/content-search.md)                  |
| [Content Templates](content-templates.md)                             | module-cms-content-templates-react-native               | [Core](../core/content-templates.md)               | [API](../api/content-templates.md)               |
| [Digital Asset Management](digital-asset-management.md)               | module-cms-digital-asset-management-react-native        | [Core](../core/digital-asset-management.md)        | [API](../api/digital-asset-management.md)        |
| [Display Modes](display-modes.md)                                     | module-cms-display-modes-react-native                   | [Core](../core/display-modes.md)                   | [API](../api/display-modes.md)                   |
| [Document Management](document-management.md)                         | module-cms-document-management-react-native             | [Core](../core/document-management.md)             | [API](../api/document-management.md)             |
| [Drupal Migration](drupal-migration.md)                               | module-cms-drupal-migration-react-native                | [Core](../core/drupal-migration.md)                | [API](../api/drupal-migration.md)                |
| [Editorial Content](editorial-content.md)                             | module-cms-editorial-content-react-native               | [Core](../core/editorial-content.md)               | [API](../api/editorial-content.md)               |
| [Editorial Workflow](editorial-workflow.md)                           | module-cms-editorial-workflow-react-native              | [Core](../core/editorial-workflow.md)              | [API](../api/editorial-workflow.md)              |
| [Embeds](embeds.md)                                                   | module-cms-embeds-react-native                          | [Core](../core/embeds.md)                          | [API](../api/embeds.md)                          |
| [Events Content](events-content.md)                                   | module-cms-events-content-react-native                  | [Core](../core/events-content.md)                  | [API](../api/events-content.md)                  |
| [Experience Assistant](experience-assistant.md)                       | module-cms-experience-assistant-react-native            | [Core](../core/experience-assistant.md)            | [API](../api/experience-assistant.md)            |
| [Experimentation](experimentation.md)                                 | module-cms-experimentation-react-native                 | [Core](../core/experimentation.md)                 | [API](../api/experimentation.md)                 |
| [Extension Manager](extension-manager.md)                             | module-cms-extension-manager-react-native               | [Core](../core/extension-manager.md)               | [API](../api/extension-manager.md)               |
| [Extension Marketplace](extension-marketplace.md)                     | module-cms-extension-marketplace-react-native           | [Core](../core/extension-marketplace.md)           | [API](../api/extension-marketplace.md)           |
| [Field System](field-system.md)                                       | module-cms-field-system-react-native                    | [Core](../core/field-system.md)                    | [API](../api/field-system.md)                    |
| [Form Builder](form-builder.md)                                       | module-cms-form-builder-react-native                    | [Core](../core/form-builder.md)                    | [API](../api/form-builder.md)                    |
| [Form Operations](form-operations.md)                                 | module-cms-form-operations-react-native                 | [Core](../core/form-operations.md)                 | [API](../api/form-operations.md)                 |
| [Forums Integration](forums-integration.md)                           | module-cms-forums-integration-react-native              | [Core](../core/forums-integration.md)              | [API](../api/forums-integration.md)              |
| [Headless Api](headless-api.md)                                       | module-cms-headless-api-react-native                    | [Core](../core/headless-api.md)                    | [API](../api/headless-api.md)                    |
| [Hook And Event Sdk](hook-and-event-sdk.md)                           | module-cms-hook-and-event-sdk-react-native              | [Core](../core/hook-and-event-sdk.md)              | [API](../api/hook-and-event-sdk.md)              |
| [Image Processing](image-processing.md)                               | module-cms-image-processing-react-native                | [Core](../core/image-processing.md)                | [API](../api/image-processing.md)                |
| [Integration Directory](integration-directory.md)                     | module-cms-integration-directory-react-native           | [Core](../core/integration-directory.md)           | [API](../api/integration-directory.md)           |
| [Joomla Migration](joomla-migration.md)                               | module-cms-joomla-migration-react-native                | [Core](../core/joomla-migration.md)                | [API](../api/joomla-migration.md)                |
| [Knowledge Base](knowledge-base.md)                                   | module-cms-knowledge-base-react-native                  | [Core](../core/knowledge-base.md)                  | [API](../api/knowledge-base.md)                  |
| [Layout Builder](layout-builder.md)                                   | module-cms-layout-builder-react-native                  | [Core](../core/layout-builder.md)                  | [API](../api/layout-builder.md)                  |
| [Localization](localization.md)                                       | module-cms-localization-react-native                    | [Core](../core/localization.md)                    | [API](../api/localization.md)                    |
| [Media Assistant](media-assistant.md)                                 | module-cms-media-assistant-react-native                 | [Core](../core/media-assistant.md)                 | [API](../api/media-assistant.md)                 |
| [Media Library](media-library.md)                                     | module-cms-media-library-react-native                   | [Core](../core/media-library.md)                   | [API](../api/media-library.md)                   |
| [Membership Content](membership-content.md)                           | module-cms-membership-content-react-native              | [Core](../core/membership-content.md)              | [API](../api/membership-content.md)              |
| [Metadata](metadata.md)                                               | module-cms-metadata-react-native                        | [Core](../core/metadata.md)                        | [API](../api/metadata.md)                        |
| [Migration Framework](migration-framework.md)                         | module-cms-migration-framework-react-native             | [Core](../core/migration-framework.md)             | [API](../api/migration-framework.md)             |
| [Multisite](multisite.md)                                             | module-cms-multisite-react-native                       | [Core](../core/multisite.md)                       | [API](../api/multisite.md)                       |
| [Navigation](navigation.md)                                           | module-cms-navigation-react-native                      | [Core](../core/navigation.md)                      | [API](../api/navigation.md)                      |
| [Notifications And Subscriptions](notifications-and-subscriptions.md) | module-cms-notifications-and-subscriptions-react-native | [Core](../core/notifications-and-subscriptions.md) | [API](../api/notifications-and-subscriptions.md) |
| [Offline And Pwa](offline-and-pwa.md)                                 | module-cms-offline-and-pwa-react-native                 | [Core](../core/offline-and-pwa.md)                 | [API](../api/offline-and-pwa.md)                 |
| [Pages](pages.md)                                                     | module-cms-pages-react-native                           | [Core](../core/pages.md)                           | [API](../api/pages.md)                           |
| [Personalization](personalization.md)                                 | module-cms-personalization-react-native                 | [Core](../core/personalization.md)                 | [API](../api/personalization.md)                 |
| [Polls And Surveys](polls-and-surveys.md)                             | module-cms-polls-and-surveys-react-native               | [Core](../core/polls-and-surveys.md)               | [API](../api/polls-and-surveys.md)               |
| [Publishing](publishing.md)                                           | module-cms-publishing-react-native                      | [Core](../core/publishing.md)                      | [API](../api/publishing.md)                      |
| [Recommendations](recommendations.md)                                 | module-cms-recommendations-react-native                 | [Core](../core/recommendations.md)                 | [API](../api/recommendations.md)                 |
| [Redirects](redirects.md)                                             | module-cms-redirects-react-native                       | [Core](../core/redirects.md)                       | [API](../api/redirects.md)                       |
| [Regions And Widgets](regions-and-widgets.md)                         | module-cms-regions-and-widgets-react-native             | [Core](../core/regions-and-widgets.md)             | [API](../api/regions-and-widgets.md)             |
| [Related Content](related-content.md)                                 | module-cms-related-content-react-native                 | [Core](../core/related-content.md)                 | [API](../api/related-content.md)                 |
| [Revisions](revisions.md)                                             | module-cms-revisions-react-native                       | [Core](../core/revisions.md)                       | [API](../api/revisions.md)                       |
| [Rich Text Editor](rich-text-editor.md)                               | module-cms-rich-text-editor-react-native                | [Core](../core/rich-text-editor.md)                | [API](../api/rich-text-editor.md)                |
| [Security Operations](security-operations.md)                         | module-cms-security-operations-react-native             | [Core](../core/security-operations.md)             | [API](../api/security-operations.md)             |
| [Seo](seo.md)                                                         | module-cms-seo-react-native                             | [Core](../core/seo.md)                             | [API](../api/seo.md)                             |
| [Site Factory](site-factory.md)                                       | module-cms-site-factory-react-native                    | [Core](../core/site-factory.md)                    | [API](../api/site-factory.md)                    |
| [Site Recipes](site-recipes.md)                                       | module-cms-site-recipes-react-native                    | [Core](../core/site-recipes.md)                    | [API](../api/site-recipes.md)                    |
| [Sitemaps](sitemaps.md)                                               | module-cms-sitemaps-react-native                        | [Core](../core/sitemaps.md)                        | [API](../api/sitemaps.md)                        |
| [Static Publishing](static-publishing.md)                             | module-cms-static-publishing-react-native               | [Core](../core/static-publishing.md)               | [API](../api/static-publishing.md)               |
| [Structured Collections](structured-collections.md)                   | module-cms-structured-collections-react-native          | [Core](../core/structured-collections.md)          | [API](../api/structured-collections.md)          |
| [Syndication And Feeds](syndication-and-feeds.md)                     | module-cms-syndication-and-feeds-react-native           | [Core](../core/syndication-and-feeds.md)           | [API](../api/syndication-and-feeds.md)           |
| [Taxonomy](taxonomy.md)                                               | module-cms-taxonomy-react-native                        | [Core](../core/taxonomy.md)                        | [API](../api/taxonomy.md)                        |
| [Theme Integration](theme-integration.md)                             | module-cms-theme-integration-react-native               | [Core](../core/theme-integration.md)               | [API](../api/theme-integration.md)               |
| [Theme Marketplace](theme-marketplace.md)                             | module-cms-theme-marketplace-react-native               | [Core](../core/theme-marketplace.md)               | [API](../api/theme-marketplace.md)               |
| [Translation Assistant](translation-assistant.md)                     | module-cms-translation-assistant-react-native           | [Core](../core/translation-assistant.md)           | [API](../api/translation-assistant.md)           |
| [Translation Management](translation-management.md)                   | module-cms-translation-management-react-native          | [Core](../core/translation-management.md)          | [API](../api/translation-management.md)          |
| [Video And Audio](video-and-audio.md)                                 | module-cms-video-and-audio-react-native                 | [Core](../core/video-and-audio.md)                 | [API](../api/video-and-audio.md)                 |
| [Views And Query Builder](views-and-query-builder.md)                 | module-cms-views-and-query-builder-react-native         | [Core](../core/views-and-query-builder.md)         | [API](../api/views-and-query-builder.md)         |
| [Web Delivery](web-delivery.md)                                       | module-cms-web-delivery-react-native                    | [Core](../core/web-delivery.md)                    | [API](../api/web-delivery.md)                    |
| [Wordpress Migration](wordpress-migration.md)                         | module-cms-wordpress-migration-react-native             | [Core](../core/wordpress-migration.md)             | [API](../api/wordpress-migration.md)             |
