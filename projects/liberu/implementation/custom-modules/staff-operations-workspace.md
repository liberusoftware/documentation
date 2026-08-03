# Staff Operations Workspace

**Package:** `module-liberu-staff-operations-workspace`

Owns role-based work-center composition, task cards, saved queues, priority/freshness display, cross-product context links, and acknowledgment/read state. It consumes CRM, Billing, Control Panel, Accounting, Maintenance, Automation, and Liberu projection contracts; it is not a second workflow engine or record owner.

**Public contract:** work item type/source reference, allowed action links, priority/reason, freshness, owner/team, due/SLA time, and operation status. Each action delegates to the source module with its policy and idempotency rules.

**Acceptance:** least-privilege queues, no cross-tenant leakage, stale data warnings, responsive web/mobile cards, offline notes, conflict recovery, accessible live updates, and audit-visible handoffs.
