# Liberu staff mobile implementation

Mobile is a focused staff companion for sales, support, delivery, on-call, finance approvals, and managers. It consumes the same versioned API as web; it does not duplicate core rules, private storage, authorization, or provider integrations.

## First-release navigation

```text
Home (priority queue) · Work (assigned tasks) · Customers (authorized search)
Alerts (SLA/incident/approval) · More (profile, team, settings, help)
```

Every detail screen presents context, freshness, one next action, evidence, and a safe recovery route. Use the [shared mobile shell](../../../user-guides/WEB-AND-MOBILE.md).

## Staff journeys

| Role | Mobile-first tasks | Required controls |
| --- | --- | --- |
| Sales | view prioritized leads/deals, guarded click-to-call, log outcome, schedule next action | CRM policy, consent/contact cooling-off, no force-contact path |
| Support | claim case, read knowledge, reply/escalate, view SLA, link incident | field sensitivity, recording/communication consent, audit |
| Delivery | view project/work item, update status, add note/evidence, request help | team/project authorization, offline draft, conflict review |
| On-call | inspect alert, acknowledge, open runbook, request recovery, communicate status | Control Panel action scopes, recent auth, approval/break-glass audit |
| Finance/manager | approve queued work, inspect governed insight, review exception | approval policy, masked financial fields, idempotency |

## Device and data policy

- Store only short-lived credentials in Keychain/Keystore or platform-secure storage.
- Cache identifiers, labels, and non-sensitive read data only when classified and encrypted; never cache raw credentials, full payment data, protected consent evidence, or infrastructure secrets.
- Offline writes become local drafts with explicit “not synced” state. Retry through idempotent API actions; show conflicts instead of overwriting.
- Request microphone, contacts, camera, notifications, or location only at the moment of need with a purpose explanation and a denied-permission fallback.
- Push notifications contain minimal data and deep-link to an authorized screen; revocation and logout invalidate routes and cached data.

## Release matrix

Ship React Native/Expo and Flutter only after API contract tests, authorization tests, accessibility checks, lifecycle interruption, offline/retry/conflict tests, signed builds, crash reporting, remote disable/feature flags, and a support runbook pass. Web staff access remains the fallback for unsupported devices or disabled mobile capability.
