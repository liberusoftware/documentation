# CMS Flutter + Dart implementations

**Scope:** [CMS](../CMS.md)
**Architecture:** [Mobile](../../../architecture/MOBILE.md) · [API](../api/README.md) · [Core](../core/README.md)
**Technology:** [Flutter technology](../../../technologies/FLUTTER.md) · [Flutter standard](../../../standards/FLUTTER.md)

This index defines the optional Flutter + Dart adapter boundary for the CMS project. Each future module adapter must map one-to-one to an existing core/API capability, preserve the server contract, and remain independently testable. Product-specific domain behavior stays in the project feature and core documentation.

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

The following 81 adapters map one-to-one to the project core and API indexes. Each module document is the implementation plan for this surface.

| Module                                                                | Package                                            | Core                                               | API                                              |
| --------------------------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------ |
| [Accessibility Assistant](accessibility-assistant.md)                 | module-cms-accessibility-assistant-flutter         | [Core](../core/accessibility-assistant.md)         | [API](../api/accessibility-assistant.md)         |
| [Analytics Integration](analytics-integration.md)                     | module-cms-analytics-integration-flutter           | [Core](../core/analytics-integration.md)           | [API](../api/analytics-integration.md)           |
| [Audit And History](audit-and-history.md)                             | module-cms-audit-and-history-flutter               | [Core](../core/audit-and-history.md)               | [API](../api/audit-and-history.md)               |
| [Backup And Restore](backup-and-restore.md)                           | module-cms-backup-and-restore-flutter              | [Core](../core/backup-and-restore.md)              | [API](../api/backup-and-restore.md)              |
| [Block Editor](block-editor.md)                                       | module-cms-block-editor-flutter                    | [Core](../core/block-editor.md)                    | [API](../api/block-editor.md)                    |
| [Cache And Performance](cache-and-performance.md)                     | module-cms-cache-and-performance-flutter           | [Core](../core/cache-and-performance.md)           | [API](../api/cache-and-performance.md)           |
| [Cms Copilot](cms-copilot.md)                                         | module-cms-cms-copilot-flutter                     | [Core](../core/cms-copilot.md)                     | [API](../api/cms-copilot.md)                     |
| [Cms Core](cms-core.md)                                               | module-cms-cms-core-flutter                        | [Core](../core/cms-core.md)                        | [API](../api/cms-core.md)                        |
| [Comments And Discussion](comments-and-discussion.md)                 | module-cms-comments-and-discussion-flutter         | [Core](../core/comments-and-discussion.md)         | [API](../api/comments-and-discussion.md)         |
| [Configuration Management](configuration-management.md)               | module-cms-configuration-management-flutter        | [Core](../core/configuration-management.md)        | [API](../api/configuration-management.md)        |
| [Contact Directory](contact-directory.md)                             | module-cms-contact-directory-flutter               | [Core](../core/contact-directory.md)               | [API](../api/contact-directory.md)               |
| [Content Access](content-access.md)                                   | module-cms-content-access-flutter                  | [Core](../core/content-access.md)                  | [API](../api/content-access.md)                  |
| [Content Calendar](content-calendar.md)                               | module-cms-content-calendar-flutter                | [Core](../core/content-calendar.md)                | [API](../api/content-calendar.md)                |
| [Content Entities](content-entities.md)                               | module-cms-content-entities-flutter                | [Core](../core/content-entities.md)                | [API](../api/content-entities.md)                |
| [Content Federation](content-federation.md)                           | module-cms-content-federation-flutter              | [Core](../core/content-federation.md)              | [API](../api/content-federation.md)              |
| [Content Governance](content-governance.md)                           | module-cms-content-governance-flutter              | [Core](../core/content-governance.md)              | [API](../api/content-governance.md)              |
| [Content Integrity](content-integrity.md)                             | module-cms-content-integrity-flutter               | [Core](../core/content-integrity.md)               | [API](../api/content-integrity.md)               |
| [Content Intelligence](content-intelligence.md)                       | module-cms-content-intelligence-flutter            | [Core](../core/content-intelligence.md)            | [API](../api/content-intelligence.md)            |
| [Content Locking](content-locking.md)                                 | module-cms-content-locking-flutter                 | [Core](../core/content-locking.md)                 | [API](../api/content-locking.md)                 |
| [Content Search](content-search.md)                                   | module-cms-content-search-flutter                  | [Core](../core/content-search.md)                  | [API](../api/content-search.md)                  |
| [Content Templates](content-templates.md)                             | module-cms-content-templates-flutter               | [Core](../core/content-templates.md)               | [API](../api/content-templates.md)               |
| [Digital Asset Management](digital-asset-management.md)               | module-cms-digital-asset-management-flutter        | [Core](../core/digital-asset-management.md)        | [API](../api/digital-asset-management.md)        |
| [Display Modes](display-modes.md)                                     | module-cms-display-modes-flutter                   | [Core](../core/display-modes.md)                   | [API](../api/display-modes.md)                   |
| [Document Management](document-management.md)                         | module-cms-document-management-flutter             | [Core](../core/document-management.md)             | [API](../api/document-management.md)             |
| [Drupal Migration](drupal-migration.md)                               | module-cms-drupal-migration-flutter                | [Core](../core/drupal-migration.md)                | [API](../api/drupal-migration.md)                |
| [Editorial Content](editorial-content.md)                             | module-cms-editorial-content-flutter               | [Core](../core/editorial-content.md)               | [API](../api/editorial-content.md)               |
| [Editorial Workflow](editorial-workflow.md)                           | module-cms-editorial-workflow-flutter              | [Core](../core/editorial-workflow.md)              | [API](../api/editorial-workflow.md)              |
| [Embeds](embeds.md)                                                   | module-cms-embeds-flutter                          | [Core](../core/embeds.md)                          | [API](../api/embeds.md)                          |
| [Events Content](events-content.md)                                   | module-cms-events-content-flutter                  | [Core](../core/events-content.md)                  | [API](../api/events-content.md)                  |
| [Experience Assistant](experience-assistant.md)                       | module-cms-experience-assistant-flutter            | [Core](../core/experience-assistant.md)            | [API](../api/experience-assistant.md)            |
| [Experimentation](experimentation.md)                                 | module-cms-experimentation-flutter                 | [Core](../core/experimentation.md)                 | [API](../api/experimentation.md)                 |
| [Extension Manager](extension-manager.md)                             | module-cms-extension-manager-flutter               | [Core](../core/extension-manager.md)               | [API](../api/extension-manager.md)               |
| [Extension Marketplace](extension-marketplace.md)                     | module-cms-extension-marketplace-flutter           | [Core](../core/extension-marketplace.md)           | [API](../api/extension-marketplace.md)           |
| [Field System](field-system.md)                                       | module-cms-field-system-flutter                    | [Core](../core/field-system.md)                    | [API](../api/field-system.md)                    |
| [Form Builder](form-builder.md)                                       | module-cms-form-builder-flutter                    | [Core](../core/form-builder.md)                    | [API](../api/form-builder.md)                    |
| [Form Operations](form-operations.md)                                 | module-cms-form-operations-flutter                 | [Core](../core/form-operations.md)                 | [API](../api/form-operations.md)                 |
| [Forums Integration](forums-integration.md)                           | module-cms-forums-integration-flutter              | [Core](../core/forums-integration.md)              | [API](../api/forums-integration.md)              |
| [Headless Api](headless-api.md)                                       | module-cms-headless-api-flutter                    | [Core](../core/headless-api.md)                    | [API](../api/headless-api.md)                    |
| [Hook And Event Sdk](hook-and-event-sdk.md)                           | module-cms-hook-and-event-sdk-flutter              | [Core](../core/hook-and-event-sdk.md)              | [API](../api/hook-and-event-sdk.md)              |
| [Image Processing](image-processing.md)                               | module-cms-image-processing-flutter                | [Core](../core/image-processing.md)                | [API](../api/image-processing.md)                |
| [Integration Directory](integration-directory.md)                     | module-cms-integration-directory-flutter           | [Core](../core/integration-directory.md)           | [API](../api/integration-directory.md)           |
| [Joomla Migration](joomla-migration.md)                               | module-cms-joomla-migration-flutter                | [Core](../core/joomla-migration.md)                | [API](../api/joomla-migration.md)                |
| [Knowledge Base](knowledge-base.md)                                   | module-cms-knowledge-base-flutter                  | [Core](../core/knowledge-base.md)                  | [API](../api/knowledge-base.md)                  |
| [Layout Builder](layout-builder.md)                                   | module-cms-layout-builder-flutter                  | [Core](../core/layout-builder.md)                  | [API](../api/layout-builder.md)                  |
| [Localization](localization.md)                                       | module-cms-localization-flutter                    | [Core](../core/localization.md)                    | [API](../api/localization.md)                    |
| [Media Assistant](media-assistant.md)                                 | module-cms-media-assistant-flutter                 | [Core](../core/media-assistant.md)                 | [API](../api/media-assistant.md)                 |
| [Media Library](media-library.md)                                     | module-cms-media-library-flutter                   | [Core](../core/media-library.md)                   | [API](../api/media-library.md)                   |
| [Membership Content](membership-content.md)                           | module-cms-membership-content-flutter              | [Core](../core/membership-content.md)              | [API](../api/membership-content.md)              |
| [Metadata](metadata.md)                                               | module-cms-metadata-flutter                        | [Core](../core/metadata.md)                        | [API](../api/metadata.md)                        |
| [Migration Framework](migration-framework.md)                         | module-cms-migration-framework-flutter             | [Core](../core/migration-framework.md)             | [API](../api/migration-framework.md)             |
| [Multisite](multisite.md)                                             | module-cms-multisite-flutter                       | [Core](../core/multisite.md)                       | [API](../api/multisite.md)                       |
| [Navigation](navigation.md)                                           | module-cms-navigation-flutter                      | [Core](../core/navigation.md)                      | [API](../api/navigation.md)                      |
| [Notifications And Subscriptions](notifications-and-subscriptions.md) | module-cms-notifications-and-subscriptions-flutter | [Core](../core/notifications-and-subscriptions.md) | [API](../api/notifications-and-subscriptions.md) |
| [Offline And Pwa](offline-and-pwa.md)                                 | module-cms-offline-and-pwa-flutter                 | [Core](../core/offline-and-pwa.md)                 | [API](../api/offline-and-pwa.md)                 |
| [Pages](pages.md)                                                     | module-cms-pages-flutter                           | [Core](../core/pages.md)                           | [API](../api/pages.md)                           |
| [Personalization](personalization.md)                                 | module-cms-personalization-flutter                 | [Core](../core/personalization.md)                 | [API](../api/personalization.md)                 |
| [Polls And Surveys](polls-and-surveys.md)                             | module-cms-polls-and-surveys-flutter               | [Core](../core/polls-and-surveys.md)               | [API](../api/polls-and-surveys.md)               |
| [Publishing](publishing.md)                                           | module-cms-publishing-flutter                      | [Core](../core/publishing.md)                      | [API](../api/publishing.md)                      |
| [Recommendations](recommendations.md)                                 | module-cms-recommendations-flutter                 | [Core](../core/recommendations.md)                 | [API](../api/recommendations.md)                 |
| [Redirects](redirects.md)                                             | module-cms-redirects-flutter                       | [Core](../core/redirects.md)                       | [API](../api/redirects.md)                       |
| [Regions And Widgets](regions-and-widgets.md)                         | module-cms-regions-and-widgets-flutter             | [Core](../core/regions-and-widgets.md)             | [API](../api/regions-and-widgets.md)             |
| [Related Content](related-content.md)                                 | module-cms-related-content-flutter                 | [Core](../core/related-content.md)                 | [API](../api/related-content.md)                 |
| [Revisions](revisions.md)                                             | module-cms-revisions-flutter                       | [Core](../core/revisions.md)                       | [API](../api/revisions.md)                       |
| [Rich Text Editor](rich-text-editor.md)                               | module-cms-rich-text-editor-flutter                | [Core](../core/rich-text-editor.md)                | [API](../api/rich-text-editor.md)                |
| [Security Operations](security-operations.md)                         | module-cms-security-operations-flutter             | [Core](../core/security-operations.md)             | [API](../api/security-operations.md)             |
| [Seo](seo.md)                                                         | module-cms-seo-flutter                             | [Core](../core/seo.md)                             | [API](../api/seo.md)                             |
| [Site Factory](site-factory.md)                                       | module-cms-site-factory-flutter                    | [Core](../core/site-factory.md)                    | [API](../api/site-factory.md)                    |
| [Site Recipes](site-recipes.md)                                       | module-cms-site-recipes-flutter                    | [Core](../core/site-recipes.md)                    | [API](../api/site-recipes.md)                    |
| [Sitemaps](sitemaps.md)                                               | module-cms-sitemaps-flutter                        | [Core](../core/sitemaps.md)                        | [API](../api/sitemaps.md)                        |
| [Static Publishing](static-publishing.md)                             | module-cms-static-publishing-flutter               | [Core](../core/static-publishing.md)               | [API](../api/static-publishing.md)               |
| [Structured Collections](structured-collections.md)                   | module-cms-structured-collections-flutter          | [Core](../core/structured-collections.md)          | [API](../api/structured-collections.md)          |
| [Syndication And Feeds](syndication-and-feeds.md)                     | module-cms-syndication-and-feeds-flutter           | [Core](../core/syndication-and-feeds.md)           | [API](../api/syndication-and-feeds.md)           |
| [Taxonomy](taxonomy.md)                                               | module-cms-taxonomy-flutter                        | [Core](../core/taxonomy.md)                        | [API](../api/taxonomy.md)                        |
| [Theme Integration](theme-integration.md)                             | module-cms-theme-integration-flutter               | [Core](../core/theme-integration.md)               | [API](../api/theme-integration.md)               |
| [Theme Marketplace](theme-marketplace.md)                             | module-cms-theme-marketplace-flutter               | [Core](../core/theme-marketplace.md)               | [API](../api/theme-marketplace.md)               |
| [Translation Assistant](translation-assistant.md)                     | module-cms-translation-assistant-flutter           | [Core](../core/translation-assistant.md)           | [API](../api/translation-assistant.md)           |
| [Translation Management](translation-management.md)                   | module-cms-translation-management-flutter          | [Core](../core/translation-management.md)          | [API](../api/translation-management.md)          |
| [Video And Audio](video-and-audio.md)                                 | module-cms-video-and-audio-flutter                 | [Core](../core/video-and-audio.md)                 | [API](../api/video-and-audio.md)                 |
| [Views And Query Builder](views-and-query-builder.md)                 | module-cms-views-and-query-builder-flutter         | [Core](../core/views-and-query-builder.md)         | [API](../api/views-and-query-builder.md)         |
| [Web Delivery](web-delivery.md)                                       | module-cms-web-delivery-flutter                    | [Core](../core/web-delivery.md)                    | [API](../api/web-delivery.md)                    |
| [Wordpress Migration](wordpress-migration.md)                         | module-cms-wordpress-migration-flutter             | [Core](../core/wordpress-migration.md)             | [API](../api/wordpress-migration.md)             |
