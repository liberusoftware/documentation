# CRM React Native + Expo implementations

**Scope:** [CRM](../CRM.md)
**Architecture:** [Mobile](../../../architecture/MOBILE.md) · [API](../api/README.md) · [Core](../core/README.md)
**Technology:** [React Native technology](../../../technologies/REACT-NATIVE.md) · [React Native standard](../../../standards/REACT-NATIVE.md)

This index defines the optional React Native + Expo adapter boundary for the CRM project. Each future module adapter must map one-to-one to an existing core/API capability, preserve the server contract, and remain independently testable. Product-specific domain behavior stays in the project feature and core documentation.

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

The following 95 adapters map one-to-one to the project core and API indexes. Each module document is the implementation plan for this surface.

| Module                                                                | Package                                                 | Core                                               | API                                              |
| --------------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------ |
| [Account Based Marketing](account-based-marketing.md)                 | module-crm-account-based-marketing-react-native         | [Core](../core/account-based-marketing.md)         | [API](../api/account-based-marketing.md)         |
| [Account Planning](account-planning.md)                               | module-crm-account-planning-react-native                | [Core](../core/account-planning.md)                | [API](../api/account-planning.md)                |
| [Activities](activities.md)                                           | module-crm-activities-react-native                      | [Core](../core/activities.md)                      | [API](../api/activities.md)                      |
| [Advertising](advertising.md)                                         | module-crm-advertising-react-native                     | [Core](../core/advertising.md)                     | [API](../api/advertising.md)                     |
| [Advocacy](advocacy.md)                                               | module-crm-advocacy-react-native                        | [Core](../core/advocacy.md)                        | [API](../api/advocacy.md)                        |
| [Affiliate Management](affiliate-management.md)                       | module-crm-affiliate-management-react-native            | [Core](../core/affiliate-management.md)            | [API](../api/affiliate-management.md)            |
| [Agency Workspace](agency-workspace.md)                               | module-crm-agency-workspace-react-native                | [Core](../core/agency-workspace.md)                | [API](../api/agency-workspace.md)                |
| [Ai Reception And Conversation](ai-reception-and-conversation.md)     | module-crm-ai-reception-and-conversation-react-native   | [Core](../core/ai-reception-and-conversation.md)   | [API](../api/ai-reception-and-conversation.md)   |
| [Attribution](attribution.md)                                         | module-crm-attribution-react-native                     | [Core](../core/attribution.md)                     | [API](../api/attribution.md)                     |
| [Business Process Management](business-process-management.md)         | module-crm-business-process-management-react-native     | [Core](../core/business-process-management.md)     | [API](../api/business-process-management.md)     |
| [Campaigns](campaigns.md)                                             | module-crm-campaigns-react-native                       | [Core](../core/campaigns.md)                       | [API](../api/campaigns.md)                       |
| [Case Management](case-management.md)                                 | module-crm-case-management-react-native                 | [Core](../core/case-management.md)                 | [API](../api/case-management.md)                 |
| [Channel Gateway](channel-gateway.md)                                 | module-crm-channel-gateway-react-native                 | [Core](../core/channel-gateway.md)                 | [API](../api/channel-gateway.md)                 |
| [Channel Sales](channel-sales.md)                                     | module-crm-channel-sales-react-native                   | [Core](../core/channel-sales.md)                   | [API](../api/channel-sales.md)                   |
| [Chat And Bots](chat-and-bots.md)                                     | module-crm-chat-and-bots-react-native                   | [Core](../core/chat-and-bots.md)                   | [API](../api/chat-and-bots.md)                   |
| [Client Onboarding](client-onboarding.md)                             | module-crm-client-onboarding-react-native               | [Core](../core/client-onboarding.md)               | [API](../api/client-onboarding.md)               |
| [Collaboration](collaboration.md)                                     | module-crm-collaboration-react-native                   | [Core](../core/collaboration.md)                   | [API](../api/collaboration.md)                   |
| [Communities](communities.md)                                         | module-crm-communities-react-native                     | [Core](../core/communities.md)                     | [API](../api/communities.md)                     |
| [Consent And Preferences](consent-and-preferences.md)                 | module-crm-consent-and-preferences-react-native         | [Core](../core/consent-and-preferences.md)         | [API](../api/consent-and-preferences.md)         |
| [Contact Center](contact-center.md)                                   | module-crm-contact-center-react-native                  | [Core](../core/contact-center.md)                  | [API](../api/contact-center.md)                  |
| [Contracts](contracts.md)                                             | module-crm-contracts-react-native                       | [Core](../core/contracts.md)                       | [API](../api/contracts.md)                       |
| [Conversation Analytics](conversation-analytics.md)                   | module-crm-conversation-analytics-react-native          | [Core](../core/conversation-analytics.md)          | [API](../api/conversation-analytics.md)          |
| [Conversation Intelligence](conversation-intelligence.md)             | module-crm-conversation-intelligence-react-native       | [Core](../core/conversation-intelligence.md)       | [API](../api/conversation-intelligence.md)       |
| [Conversion Optimization](conversion-optimization.md)                 | module-crm-conversion-optimization-react-native         | [Core](../core/conversion-optimization.md)         | [API](../api/conversion-optimization.md)         |
| [Cpq](cpq.md)                                                         | module-crm-cpq-react-native                             | [Core](../core/cpq.md)                             | [API](../api/cpq.md)                             |
| [Crm Analytics](crm-analytics.md)                                     | module-crm-crm-analytics-react-native                   | [Core](../core/crm-analytics.md)                   | [API](../api/crm-analytics.md)                   |
| [Crm Automation Pack](crm-automation-pack.md)                         | module-crm-crm-automation-pack-react-native             | [Core](../core/crm-automation-pack.md)             | [API](../api/crm-automation-pack.md)             |
| [Crm Copilot](crm-copilot.md)                                         | module-crm-crm-copilot-react-native                     | [Core](../core/crm-copilot.md)                     | [API](../api/crm-copilot.md)                     |
| [Crm Core](crm-core.md)                                               | module-crm-crm-core-react-native                        | [Core](../core/crm-core.md)                        | [API](../api/crm-core.md)                        |
| [Crm Documents](crm-documents.md)                                     | module-crm-crm-documents-react-native                   | [Core](../core/crm-documents.md)                   | [API](../api/crm-documents.md)                   |
| [Crm Product Workspace](crm-product-workspace.md)                     | module-crm-crm-product-workspace-react-native           | [Core](../core/crm-product-workspace.md)           | [API](../api/crm-product-workspace.md)           |
| [Crm Search](crm-search.md)                                           | module-crm-crm-search-react-native                      | [Core](../core/crm-search.md)                      | [API](../api/crm-search.md)                      |
| [Customer Data Model](customer-data-model.md)                         | module-crm-customer-data-model-react-native             | [Core](../core/customer-data-model.md)             | [API](../api/customer-data-model.md)             |
| [Customer Data Platform](customer-data-platform.md)                   | module-crm-customer-data-platform-react-native          | [Core](../core/customer-data-platform.md)          | [API](../api/customer-data-platform.md)          |
| [Customer Self Service](customer-self-service.md)                     | module-crm-customer-self-service-react-native           | [Core](../core/customer-self-service.md)           | [API](../api/customer-self-service.md)           |
| [Customer Success](customer-success.md)                               | module-crm-customer-success-react-native                | [Core](../core/customer-success.md)                | [API](../api/customer-success.md)                |
| [Data Operations](data-operations.md)                                 | module-crm-data-operations-react-native                 | [Core](../core/data-operations.md)                 | [API](../api/data-operations.md)                 |
| [Deal Registration](deal-registration.md)                             | module-crm-deal-registration-react-native               | [Core](../core/deal-registration.md)               | [API](../api/deal-registration.md)               |
| [Dialer And Outreach](dialer-and-outreach.md)                         | module-crm-dialer-and-outreach-react-native             | [Core](../core/dialer-and-outreach.md)             | [API](../api/dialer-and-outreach.md)             |
| [Email Marketing](email-marketing.md)                                 | module-crm-email-marketing-react-native                 | [Core](../core/email-marketing.md)                 | [API](../api/email-marketing.md)                 |
| [Email Productivity](email-productivity.md)                           | module-crm-email-productivity-react-native              | [Core](../core/email-productivity.md)              | [API](../api/email-productivity.md)              |
| [Enrichment](enrichment.md)                                           | module-crm-enrichment-react-native                      | [Core](../core/enrichment.md)                      | [API](../api/enrichment.md)                      |
| [Events And Webinars](events-and-webinars.md)                         | module-crm-events-and-webinars-react-native             | [Core](../core/events-and-webinars.md)             | [API](../api/events-and-webinars.md)             |
| [Feedback And Voice Of Customer](feedback-and-voice-of-customer.md)   | module-crm-feedback-and-voice-of-customer-react-native  | [Core](../core/feedback-and-voice-of-customer.md)  | [API](../api/feedback-and-voice-of-customer.md)  |
| [Field Service Coordination](field-service-coordination.md)           | module-crm-field-service-coordination-react-native      | [Core](../core/field-service-coordination.md)      | [API](../api/field-service-coordination.md)      |
| [Forecasting](forecasting.md)                                         | module-crm-forecasting-react-native                     | [Core](../core/forecasting.md)                     | [API](../api/forecasting.md)                     |
| [Forms And Surveys](forms-and-surveys.md)                             | module-crm-forms-and-surveys-react-native               | [Core](../core/forms-and-surveys.md)               | [API](../api/forms-and-surveys.md)               |
| [Goals And Performance](goals-and-performance.md)                     | module-crm-goals-and-performance-react-native           | [Core](../core/goals-and-performance.md)           | [API](../api/goals-and-performance.md)           |
| [Journey Orchestration](journey-orchestration.md)                     | module-crm-journey-orchestration-react-native           | [Core](../core/journey-orchestration.md)           | [API](../api/journey-orchestration.md)           |
| [Knowledge](knowledge.md)                                             | module-crm-knowledge-react-native                       | [Core](../core/knowledge.md)                       | [API](../api/knowledge.md)                       |
| [Landing Pages And Funnels](landing-pages-and-funnels.md)             | module-crm-landing-pages-and-funnels-react-native       | [Core](../core/landing-pages-and-funnels.md)       | [API](../api/landing-pages-and-funnels.md)       |
| [Lead Capture](lead-capture.md)                                       | module-crm-lead-capture-react-native                    | [Core](../core/lead-capture.md)                    | [API](../api/lead-capture.md)                    |
| [Lead Qualification](lead-qualification.md)                           | module-crm-lead-qualification-react-native              | [Core](../core/lead-qualification.md)              | [API](../api/lead-qualification.md)              |
| [Learning And Courses](learning-and-courses.md)                       | module-crm-learning-and-courses-react-native            | [Core](../core/learning-and-courses.md)            | [API](../api/learning-and-courses.md)            |
| [Loyalty](loyalty.md)                                                 | module-crm-loyalty-react-native                         | [Core](../core/loyalty.md)                         | [API](../api/loyalty.md)                         |
| [Marketing Agent](marketing-agent.md)                                 | module-crm-marketing-agent-react-native                 | [Core](../core/marketing-agent.md)                 | [API](../api/marketing-agent.md)                 |
| [Marketing Development Funds](marketing-development-funds.md)         | module-crm-marketing-development-funds-react-native     | [Core](../core/marketing-development-funds.md)     | [API](../api/marketing-development-funds.md)     |
| [Marketing Resources](marketing-resources.md)                         | module-crm-marketing-resources-react-native             | [Core](../core/marketing-resources.md)             | [API](../api/marketing-resources.md)             |
| [Memberships](memberships.md)                                         | module-crm-memberships-react-native                     | [Core](../core/memberships.md)                     | [API](../api/memberships.md)                     |
| [Mobile Messaging](mobile-messaging.md)                               | module-crm-mobile-messaging-react-native                | [Core](../core/mobile-messaging.md)                | [API](../api/mobile-messaging.md)                |
| [Omnichannel Service](omnichannel-service.md)                         | module-crm-omnichannel-service-react-native             | [Core](../core/omnichannel-service.md)             | [API](../api/omnichannel-service.md)             |
| [Orders And Payments Workspace](orders-and-payments-workspace.md)     | module-crm-orders-and-payments-workspace-react-native   | [Core](../core/orders-and-payments-workspace.md)   | [API](../api/orders-and-payments-workspace.md)   |
| [Partner Relationship Management](partner-relationship-management.md) | module-crm-partner-relationship-management-react-native | [Core](../core/partner-relationship-management.md) | [API](../api/partner-relationship-management.md) |
| [Personalization](personalization.md)                                 | module-crm-personalization-react-native                 | [Core](../core/personalization.md)                 | [API](../api/personalization.md)                 |
| [Playbooks And Enablement](playbooks-and-enablement.md)               | module-crm-playbooks-and-enablement-react-native        | [Core](../core/playbooks-and-enablement.md)        | [API](../api/playbooks-and-enablement.md)        |
| [Predictive Models](predictive-models.md)                             | module-crm-predictive-models-react-native               | [Core](../core/predictive-models.md)               | [API](../api/predictive-models.md)               |
| [Projects](projects.md)                                               | module-crm-projects-react-native                        | [Core](../core/projects.md)                        | [API](../api/projects.md)                        |
| [Proposals And Quotes](proposals-and-quotes.md)                       | module-crm-proposals-and-quotes-react-native            | [Core](../core/proposals-and-quotes.md)            | [API](../api/proposals-and-quotes.md)            |
| [Prospecting Agent](prospecting-agent.md)                             | module-crm-prospecting-agent-react-native               | [Core](../core/prospecting-agent.md)               | [API](../api/prospecting-agent.md)               |
| [Prospecting](prospecting.md)                                         | module-crm-prospecting-react-native                     | [Core](../core/prospecting.md)                     | [API](../api/prospecting.md)                     |
| [Quotas And Incentives](quotas-and-incentives.md)                     | module-crm-quotas-and-incentives-react-native           | [Core](../core/quotas-and-incentives.md)           | [API](../api/quotas-and-incentives.md)           |
| [Referrals](referrals.md)                                             | module-crm-referrals-react-native                       | [Core](../core/referrals.md)                       | [API](../api/referrals.md)                       |
| [Reputation Management](reputation-management.md)                     | module-crm-reputation-management-react-native           | [Core](../core/reputation-management.md)           | [API](../api/reputation-management.md)           |
| [Resource Planning](resource-planning.md)                             | module-crm-resource-planning-react-native               | [Core](../core/resource-planning.md)               | [API](../api/resource-planning.md)               |
| [Revenue Intelligence](revenue-intelligence.md)                       | module-crm-revenue-intelligence-react-native            | [Core](../core/revenue-intelligence.md)            | [API](../api/revenue-intelligence.md)            |
| [Revenue Lifecycle](revenue-lifecycle.md)                             | module-crm-revenue-lifecycle-react-native               | [Core](../core/revenue-lifecycle.md)               | [API](../api/revenue-lifecycle.md)               |
| [Routing](routing.md)                                                 | module-crm-routing-react-native                         | [Core](../core/routing.md)                         | [API](../api/routing.md)                         |
| [Saas Packaging](saas-packaging.md)                                   | module-crm-saas-packaging-react-native                  | [Core](../core/saas-packaging.md)                  | [API](../api/saas-packaging.md)                  |
| [Sales Engagement](sales-engagement.md)                               | module-crm-sales-engagement-react-native                | [Core](../core/sales-engagement.md)                | [API](../api/sales-engagement.md)                |
| [Sales Pipelines](sales-pipelines.md)                                 | module-crm-sales-pipelines-react-native                 | [Core](../core/sales-pipelines.md)                 | [API](../api/sales-pipelines.md)                 |
| [Sales Workspace](sales-workspace.md)                                 | module-crm-sales-workspace-react-native                 | [Core](../core/sales-workspace.md)                 | [API](../api/sales-workspace.md)                 |
| [Sandbox And Release Management](sandbox-and-release-management.md)   | module-crm-sandbox-and-release-management-react-native  | [Core](../core/sandbox-and-release-management.md)  | [API](../api/sandbox-and-release-management.md)  |
| [Scheduling](scheduling.md)                                           | module-crm-scheduling-react-native                      | [Core](../core/scheduling.md)                      | [API](../api/scheduling.md)                      |
| [Segmentation](segmentation.md)                                       | module-crm-segmentation-react-native                    | [Core](../core/segmentation.md)                    | [API](../api/segmentation.md)                    |
| [Service Agent](service-agent.md)                                     | module-crm-service-agent-react-native                   | [Core](../core/service-agent.md)                   | [API](../api/service-agent.md)                   |
| [Service Analytics](service-analytics.md)                             | module-crm-service-analytics-react-native               | [Core](../core/service-analytics.md)               | [API](../api/service-analytics.md)               |
| [Sla And Entitlements](sla-and-entitlements.md)                       | module-crm-sla-and-entitlements-react-native            | [Core](../core/sla-and-entitlements.md)            | [API](../api/sla-and-entitlements.md)            |
| [Telephony](telephony.md)                                             | module-crm-telephony-react-native                       | [Core](../core/telephony.md)                       | [API](../api/telephony.md)                       |
| [Templates And Snapshots](templates-and-snapshots.md)                 | module-crm-templates-and-snapshots-react-native         | [Core](../core/templates-and-snapshots.md)         | [API](../api/templates-and-snapshots.md)         |
| [Territories And Ownership](territories-and-ownership.md)             | module-crm-territories-and-ownership-react-native       | [Core](../core/territories-and-ownership.md)       | [API](../api/territories-and-ownership.md)       |
| [Unified Conversations](unified-conversations.md)                     | module-crm-unified-conversations-react-native           | [Core](../core/unified-conversations.md)           | [API](../api/unified-conversations.md)           |
| [Usage Wallet And Rebilling](usage-wallet-and-rebilling.md)           | module-crm-usage-wallet-and-rebilling-react-native      | [Core](../core/usage-wallet-and-rebilling.md)      | [API](../api/usage-wallet-and-rebilling.md)      |
| [Web Intent](web-intent.md)                                           | module-crm-web-intent-react-native                      | [Core](../core/web-intent.md)                      | [API](../api/web-intent.md)                      |
| [White Label](white-label.md)                                         | module-crm-white-label-react-native                     | [Core](../core/white-label.md)                     | [API](../api/white-label.md)                     |
| [Work Management](work-management.md)                                 | module-crm-work-management-react-native                 | [Core](../core/work-management.md)                 | [API](../api/work-management.md)                 |
