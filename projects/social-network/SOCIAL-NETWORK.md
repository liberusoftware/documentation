# Liberu Social Network

## Product Scope

**Purpose:** Configurable private, public, and federated communities with profiles, content, groups, messaging, discovery, and moderation.
**Architecture:** Modules follow [MODULES.md](../../architecture/MODULES.md); public, application, moderation, and federation APIs follow [API.md](../../architecture/API.md); community experiences and branding follow [THEMES.md](../../standards/THEMES.md).

**Foundation:** Consume relevant modules from [BOILERPLATE.md](../boilerplate/BOILERPLATE.md); this scope defines social-network behavior only.

## Outcomes

- Enable safe identity, connection, publishing, conversation, community, and event experiences.
- Give users understandable control over audience, privacy, notifications, data, and safety.
- Operate transparent moderation and optional federation at scale.

## Module plan

| Module        | Responsibilities                                                                                    |
| ------------- | --------------------------------------------------------------------------------------------------- |
| Social Core   | Network settings, deployment mode, terminology, feature policy, shared IDs, and events              |
| Profiles      | Handles, bios, attributes, avatars, verification, visibility, blocking, and profile lifecycle       |
| Social Graph  | Follow/friend models, requests, lists, suggestions, blocks, and relationship visibility             |
| Publishing    | Posts, articles, drafts, audiences, edits, mentions, hashtags, polls, links, and schedules          |
| Feed          | Candidate generation, ranking, chronological mode, filters, pagination, explanations, and controls  |
| Engagement    | Reactions, comments, replies, sharing, bookmarks, counters, and abuse limits                        |
| Media         | Images, video, audio, files, processing, alt text, captions, rights, and delivery                   |
| Communities   | Groups/pages, memberships, roles, rules, feeds, files, questions, and moderation                    |
| Events        | Events, invitations, attendance, capacity, schedules, locations, reminders, and updates             |
| Messaging     | Conversations, membership, delivery/read state, attachments, requests, safety, and retention        |
| Notifications | Preferences, in-app/email/push delivery, grouping, digests, quiet hours, and read state             |
| Discovery     | Search, hashtags, trends, recommendations, directories, and privacy-aware indexing                  |
| Moderation    | Reports, queues, policy/rules, evidence, actions, appeals, sanctions, and transparency              |
| Federation    | ActivityPub identities, inbox/outbox, signatures, delivery, mapping, moderation, and reconciliation |
| Analytics     | Growth, engagement, retention, health, moderation, delivery, and privacy-governed insights          |

## Required workflows

1. **Publish:** compose → select audience → validate media/policy → publish → distribute/index/notify → edit or delete with propagation.
2. **Connect:** request/follow → privacy and block checks → accept where required → update graph/feed permissions.
3. **Report and appeal:** report content/account → preserve evidence → triage → decide/action → notify → appeal → independent review.
4. **Message:** request or open conversation → enforce membership/block policy → deliver → report/leave/delete according to retention policy.
5. **Federate:** receive signed activity → validate/deduplicate/map/moderate → apply locally → deliver responses with retry and domain controls.

## Product requirements

- Support invite-only private, organization/community, public registration, and optionally federated modes.
- Evaluate audience and block rules on every read, feed, search, notification, export, and API path.
- Provide chronological feeds and explain/control recommendation inputs; do not make ranking a theme concern.
- Handle post/comment edit history according to policy and consistently update counters, indexes, and federation state.
- Provide account download, deactivation, deletion, memorialization where enabled, consent, and retention workflows.
- Design for accessibility, localization, RTL, responsive media, low bandwidth, and progressive enhancement.
- Treat offline/local sharing and external-network import as optional modules with explicit consent and threat models.

## Integrations

Email/SMS/push, storage/CDN, media processing, search, antivirus, link metadata, maps, calendar, identity/SSO, CMS, and optional federation/import providers use replaceable drivers.

## Trust, safety, and quality gates

- Protect against spam, impersonation, harassment, scraping, malicious uploads, link abuse, credential attacks, and moderation misuse.
- Test audience leakage, blocks, deleted/edited content, graph races, counter consistency, feed pagination, notification fanout, and federation replay.
- Require role separation and audit for moderator actions; minimize exposure of reporter identity and sensitive evidence.
- Load-test fanout, feeds, comments, messaging, media, search, and federation queues with degraded-mode behavior.

## Delivery phases

1. Core, Profiles, Social Graph, Publishing, Feed, Engagement, Media, Notifications, and baseline moderation.
2. Communities, Messaging, Discovery, Events, analytics, richer safety tools, and mobile/PWA refinement.
3. Federation, advanced recommendations, pages/articles/files, and external imports.
4. Optional offline sharing, monetization, and specialized community modules.

## Definition of done

Users can control identity, audience, relationships, content, messaging, and account lifecycle; moderators have fair, auditable workflows; privacy rules hold across every projection and integration. Each module becomes a GitHub epic.

## Product Scope

**Purpose:** Configurable private, public, and federated communities with profiles, content, groups, messaging, discovery, and moderation.
**Architecture:** Modules follow [MODULES.md](../../architecture/MODULES.md); public, application, moderation, and federation APIs follow [API.md](../../architecture/API.md); community experiences and branding follow [THEMES.md](../../standards/THEMES.md).

**Foundation:** Consume relevant modules from [BOILERPLATE.md](../boilerplate/BOILERPLATE.md); this scope defines social-network behavior only.

## Outcomes

- Enable safe identity, connection, publishing, conversation, community, and event experiences.
- Give users understandable control over audience, privacy, notifications, data, and safety.
- Operate transparent moderation and optional federation at scale.

## Module plan

| Module        | Responsibilities                                                                                    |
| ------------- | --------------------------------------------------------------------------------------------------- |
| Social Core   | Network settings, deployment mode, terminology, feature policy, shared IDs, and events              |
| Profiles      | Handles, bios, attributes, avatars, verification, visibility, blocking, and profile lifecycle       |
| Social Graph  | Follow/friend models, requests, lists, suggestions, blocks, and relationship visibility             |
| Publishing    | Posts, articles, drafts, audiences, edits, mentions, hashtags, polls, links, and schedules          |
| Feed          | Candidate generation, ranking, chronological mode, filters, pagination, explanations, and controls  |
| Engagement    | Reactions, comments, replies, sharing, bookmarks, counters, and abuse limits                        |
| Media         | Images, video, audio, files, processing, alt text, captions, rights, and delivery                   |
| Communities   | Groups/pages, memberships, roles, rules, feeds, files, questions, and moderation                    |
| Events        | Events, invitations, attendance, capacity, schedules, locations, reminders, and updates             |
| Messaging     | Conversations, membership, delivery/read state, attachments, requests, safety, and retention        |
| Notifications | Preferences, in-app/email/push delivery, grouping, digests, quiet hours, and read state             |
| Discovery     | Search, hashtags, trends, recommendations, directories, and privacy-aware indexing                  |
| Moderation    | Reports, queues, policy/rules, evidence, actions, appeals, sanctions, and transparency              |
| Federation    | ActivityPub identities, inbox/outbox, signatures, delivery, mapping, moderation, and reconciliation |
| Analytics     | Growth, engagement, retention, health, moderation, delivery, and privacy-governed insights          |

## Required workflows

1. **Publish:** compose → select audience → validate media/policy → publish → distribute/index/notify → edit or delete with propagation.
2. **Connect:** request/follow → privacy and block checks → accept where required → update graph/feed permissions.
3. **Report and appeal:** report content/account → preserve evidence → triage → decide/action → notify → appeal → independent review.
4. **Message:** request or open conversation → enforce membership/block policy → deliver → report/leave/delete according to retention policy.
5. **Federate:** receive signed activity → validate/deduplicate/map/moderate → apply locally → deliver responses with retry and domain controls.

## Product requirements

- Support invite-only private, organization/community, public registration, and optionally federated modes.
- Evaluate audience and block rules on every read, feed, search, notification, export, and API path.
- Provide chronological feeds and explain/control recommendation inputs; do not make ranking a theme concern.
- Handle post/comment edit history according to policy and consistently update counters, indexes, and federation state.
- Provide account download, deactivation, deletion, memorialization where enabled, consent, and retention workflows.
- Design for accessibility, localization, RTL, responsive media, low bandwidth, and progressive enhancement.
- Treat offline/local sharing and external-network import as optional modules with explicit consent and threat models.

## Integrations

Email/SMS/push, storage/CDN, media processing, search, antivirus, link metadata, maps, calendar, identity/SSO, CMS, and optional federation/import providers use replaceable drivers.

## Trust, safety, and quality gates

- Protect against spam, impersonation, harassment, scraping, malicious uploads, link abuse, credential attacks, and moderation misuse.
- Test audience leakage, blocks, deleted/edited content, graph races, counter consistency, feed pagination, notification fanout, and federation replay.
- Require role separation and audit for moderator actions; minimize exposure of reporter identity and sensitive evidence.
- Load-test fanout, feeds, comments, messaging, media, search, and federation queues with degraded-mode behavior.

## Delivery phases

1. Core, Profiles, Social Graph, Publishing, Feed, Engagement, Media, Notifications, and baseline moderation.
2. Communities, Messaging, Discovery, Events, analytics, richer safety tools, and mobile/PWA refinement.
3. Federation, advanced recommendations, pages/articles/files, and external imports.
4. Optional offline sharing, monetization, and specialized community modules.

## Definition of done

Users can control identity, audience, relationships, content, messaging, and account lifecycle; moderators have fair, auditable workflows; privacy rules hold across every projection and integration. Each module becomes a GitHub epic.
