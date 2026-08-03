# Liberu: Revenue and Care Orchestration API

**Package:** `module-liberu-revenue-and-care-orchestration-api`
**Core:** [Revenue and Care Orchestration](../core/revenue-and-care-orchestration.md)
**Feature:** [Revenue and Care Orchestration](../features/revenue-and-care-orchestration.md)

## Contract

Base path: `/api/v1/liberu/revenue-and-care-orchestration`. Use versioned OpenAPI 3.1 resources, explicit DTOs, Sanctum/service scopes, tenant/brand policy, RFC 9457 errors, bounded pagination, and `Idempotency-Key` for mutations.

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET` | `/health?customer_id={id}` | Read authorized health constellation and evidence links |
| `GET` | `/care-queue` | List prioritized sales/support/on-call work with safe reason codes |
| `GET` | `/outreach-eligibility?contact_id={id}&channel=voice` | Explain whether contact is eligible and return `next_contact_at` |
| `POST` | `/recovery-requests` | Request an owning CRM case from an incident/provisioning signal |
| `POST` | `/ai-recommendations/{id}/accept` | Accept an approved recommendation as a typed action |

The API never accepts a caller-supplied bypass or tenant context as authority. Response fields include source references, freshness, policy version, and non-sensitive reason codes; protected consent, infrastructure, and financial details are field-authorized. Slow projection rebuilds and provider-dependent actions return an operation resource with retry/reconciliation status.
