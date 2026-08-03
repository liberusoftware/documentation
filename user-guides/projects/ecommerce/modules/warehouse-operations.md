# Warehouse Operations — end-user guide

**Project:** [Liberu Ecommerce](../README.md)
**Feature specification:** [warehouse-operations.md](../../../../projects/ecommerce/features/warehouse-operations.md)
**Shared experience standard:** [Web and mobile](../../../WEB-AND-MOBILE.md)

## What users see

See product/context reassurance, the primary purchase action, and order progress. The module should explain its purpose in the page heading, keep related evidence close to the decision, and never require users to understand internal package names.

## Primary journey

```mermaid
flowchart LR
  A[Open module] --> B[Understand context]
  B --> C[Take primary action]
  C --> D[See result or queued status]
  D --> E[Continue or recover]
```

## Web behavior

Use a responsive page with a clear title, status/freshness, primary action, related context, and helpful empty/error states. Deep links should reopen the same safe context. Forms preserve entered data after validation errors; destructive or externally visible actions explain their impact before confirmation.

## Mobile behavior

Prioritize the frequent task and essential context. Keep the primary action reachable, use readable cards instead of dense tables, expose sync freshness, preserve drafts, and handle offline, interrupted, denied, and conflict states without claiming success prematurely. Notifications and deep links must respect permission and privacy.

## Visible states

- **Empty:** explain what is missing and the next useful setup or discovery step.
- **Success:** confirm what changed, when, and what the user can do next.
- **Queued:** show that processing continues, who owns it, and where progress appears.
- **Failure/conflict:** explain the problem in plain language and provide retry, review, or support recovery.
- **Denied:** explain the safe reason and an appropriate request/access path.

## Developer expectation

An installed surface is ready when this journey is represented in the relevant web/mobile navigation, authorization is enforced by the server, API errors map to accessible UI, loading and interruption are tested, and the module's terminology is consistent across web, mobile, email, and notifications.
