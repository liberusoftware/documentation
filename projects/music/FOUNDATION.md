# Liberu Music foundation adoption

Music composes shared platform capabilities from the [Boilerplate foundation](../boilerplate/BOILERPLATE.md). Exact packages and install commands must come from verified manifests; these adoption requirements do not assert package availability.

| Shared capability | Music use and required boundary |
| --- | --- |
| Identity, social sign-in and two-factor authentication | Account/session lifecycle and optional account connection; local recording remains usable offline under the declared authorization policy |
| Organizations/teams and roles/permissions | Workspace membership, project owner/editor/reviewer roles and share revocation |
| Files/media and import/export | Private asset storage and portable archives; Music owns audio metadata, revisions and referenced-asset semantics |
| Settings, localization and themes | Device/user preferences, units, shortcuts, translated UI and accessible visual adapters |
| Audit and activity/comments | Administrative and revision audit trail; Music owns musical-position review anchors |
| Notifications and webhooks | Share invitations, review updates and render completion; scoped, retryable delivery |
| Scheduler/queues and observability | Waveform/index/render jobs, retries, quotas and diagnostics; excluded from real-time audio execution |
| Search | Authorized sample, preset and project discovery with workspace-scoped results |
| API access and sessions/devices | Tokens, paired controller sessions, device revocation and scoped API permissions |
| Module manager and feature flags | Capability discovery, compatible engine/schema checks and staged rollout |
| Billing/subscriptions, if sold | Account entitlements and resource limits; define offline entitlement grace without interrupting capture |

Each consuming host chooses only the required foundation adapters. Do not generate parallel Music identity, authorization, storage or payment authorities. Foundation API/web/mobile plans remain canonical in their original indexes; Music adapters integrate their public contracts. Validate tenant isolation and revocation across the combined application.
