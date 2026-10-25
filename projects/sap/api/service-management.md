# Service management: enterprise API design

**Status:** proposed composition contract. The [observed SAP source](../SOURCE-APPLICATION.md) establishes a foundation host, not these enterprise business endpoints. The paths, schemas and examples below require implementation/adoption review before any client uses them.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#service-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## 1. Purpose and ownership

Reuse CRM case management, knowledge, SLA/entitlements, and Control Panel monitoring. Enterprise adds cross-product service context, major-incident coordination, and controlled change orchestration where missing.

The primary enterprise workflow record is a **service incident**. A façade can coordinate owning product APIs and an enterprise read model, while the original product retains write authority for its records. `module-sap-service-management-api` is a design identifier; it does not establish a published Composer package or another authoritative business implementation.

Read the [detailed domain design](../design/service-management.md), [composition guide](../COMPOSITION.md), and [API architecture](../../../architecture/API.md) for the surrounding boundaries.

## 2. Contract design

The resource DTO exposes a stable identifier/type, workflow state, record version, authorized source/evidence references and permitted actions. Its domain fields are **`service_reference`, `affected_entity_ids`, `customer_reference`, `priority`, `entitlement_snapshot`, `business_calendar_version`, `detected_at`, `correlation_reference`**. The [domain field table](../design/service-management.md#records-and-required-context) defines their responsibilities; complete types, limits, sensitivity and required/nullable behavior must be reviewed with the actual owners.

Separate input from output schemas. Resolve actor/service, tenant membership and permitted legal entities from trusted authentication; submitted IDs select records but grant no authority. Resource state, audit fields, source results and permitted actions are server-owned. Paginated reads allowlist filters/sorts/includes and apply field/entity policy before serialization.

The proposed command protocol uses an actor/tenant-scoped `Idempotency-Key` and a documented record-version precondition such as `If-Match`. Scope a stored command result by operation and subject as well as identity; reusing a key with a different request is a conflict. Implement this storage/checking explicitly: passing a header alone does not make a downstream API idempotent.

## 3. Endpoint examples

These routes come from the detailed enterprise design. They are not a discovered runtime route list. Record creation/ingestion follows the owning workflow contract; there is no invented generic create/delete operation for an entire business group.

| Method | Proposed path | Responsibility |
| --- | --- | --- |
| GET | `/api/v1/enterprise/service-incidents` | Authorized filtered/paginated workflow records |
| GET | `/api/v1/enterprise/service-incidents/{id}` | Workflow detail, source references, state/version and permitted evidence |
| POST | `/api/v1/enterprise/service-incidents/{id}/triage` | Explicit `triage` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/service-incidents/{id}/assign` | Explicit `assign` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/service-incidents/{id}/escalate` | Explicit `escalate` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/service-incidents/{id}/resolve` | Explicit `resolve` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/service-incidents/{id}/reopen` | Explicit `reopen` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/service-incidents/{id}/close` | Explicit `close` command; validate transition, scope and command-specific inputs |

### resolve command

Proposed operation ID: `enterprise.service-management.resolve`. Scenario: `investigating` → `resolved` after the business action is confirmed. The example IDs are illustrative; obtain actual identifiers from authorized records.

```http
POST /api/v1/enterprise/service-incidents/incident-example-001/resolve HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer YOUR_AUTHORIZED_TOKEN
If-Match: "record-v12"
Idempotency-Key: service-management-example-command-001
```

```json
{
  "resolution_code": "service-restored",
  "resolution_summary": "Approved recovery completed and service checks passed.",
  "evidence_references": [
    "service-check-example-001"
  ],
  "change_reference": "change-example-001"
}
```

Require resolution authority and evidence for the selected service/entitlement. Keep customer-visible resolution text separate from restricted internal notes; validate any linked change authority.

Record the resolution and SLA outcome. Closure and any later reopening preserve the earlier resolution evidence and are separate lifecycle actions.

Proposed synchronous response: `200 OK` only after the local authorized decision is recorded, with the new record version. Any resulting downstream handoffs remain separately observable; local success is not proof of their completion.

```json
{
  "data": {
    "id": "incident-example-001",
    "type": "service-incidents",
    "attributes": {
      "state": "resolved",
      "version": "record-v13"
    }
  },
  "meta": {
    "request_id": "request-example-001"
  }
}
```

## 4. OpenAPI schema

The reviewed fragment should define the resource and collection schemas, separate command bodies, operation/result schemas, scopes, version preconditions, idempotency semantics, errors and pagination. Use stable operation IDs for each explicit action and include the owning product/enterprise boundary. Validate/bundle the specification and compare it against supported contracts before generating clients.

This document includes a machine-readable **draft schema for the illustrated `resolve` request only**: [request schema](contracts/service-management.request.schema.json) and [matching example](contracts/service-management.request.example.json). Other command bodies and the complete response/OpenAPI bundle still require their own reviewed schemas. The specimen is not a full implemented service contract.

The specimen makes the illustrated business fields required and rejects unknown properties. Required fields, units, effective-date constraints, value ranges, enum sets and cross-record rules must be confirmed against the selected owner before a release; JSON type validation cannot establish authorization or business validity.

Reference: [JSON Schema 2020-12](https://json-schema.org/draft/2020-12) and [OpenAPI 3.1](https://spec.openapis.org/oas/v3.1.0).

## 5. Audience and operation matrix

Agents see entitled customer records; incident commanders coordinate; change approvers authorize production changes independently.

| Audience | Exposure decision |
| --- | --- |
| Anonymous/public | Disabled for these workflow commands |
| Employee or approved external delegate | Only explicitly granted records, fields and actions; enforce source/evidence policy independently |
| Approver/operator | Domain authority and segregation/delegation policy apply to each action and bulk record |
| Service integration | Narrow service identity, permitted entities/operations, correlation and durable command identity |

An authenticated role name alone is insufficient where a record, value threshold, legal entity, time window or independent approval constrains the operation. Recheck permissions in jobs and evidence downloads.

## 6. Implementation strategy

Monitoring emits alerts; service owners create/associate incidents; approved changes invoke infrastructure or delivery contracts. Knowledge publication uses the owning content contract.

Persist only enterprise-owned workflow/operation state and source references. Use local transactions for its invariants, then durable outbox/inbox or an equivalent owner-supported handoff. Confirm an existing source operation before retrying a timeout; do not repeat a side effect under a fresh identity. Product adapters translate schemas/errors without accessing another owner's private tables.

Presentations use explicit domain commands rather than a generic state patch. Filament/Livewire can invoke the reviewed public application boundary, while React/Inertia, Next.js, Vue/Nuxt and mobile use their appropriate authorized transport. Preserve one domain invariant and recovery contract across all surfaces.

## 7. Security, resilience, and observability

Deduplicate repeated alerts into an incident correlation policy. Escalate missed acknowledgements and failed automation visibly; a failed run never marks the incident resolved automatically.

| Response condition | Proposed handling |
| --- | --- |
| 401 / 403 / scoped 404 | Authenticate or deny/conceal consistently; never retry under a broader identity |
| 409 conflict | Invalid transition, duplicate identity with another payload, or owner uniqueness conflict; expose an actionable current outcome |
| 412 precondition failed | Reload/review the changed record version; preserve safe draft inputs |
| 422 validation failed | Return field/domain errors without leaking hidden source records |
| 429 / 503 | Apply documented retry/backoff and preserve operation identity; reconcile uncertain outcomes before reissuing writes |

Use the shared Problem Details envelope, request/correlation IDs and scoped operator diagnostics. Redact protected data and credentials. Record source acknowledgements, last error, attempt count and recovery owner; an unavailable dependency must not silently advance the final state.

## 8. Verification strategy

- A pause reason affects only permitted SLA clocks; repeated alerts follow correlation policy; restricted internal notes never appear in customer/mobile projections.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

Also verify the illustrated command body against its draft request schema, allowed/denied/wrong-entity requests, stale versions, changed-payload key reuse, uncertain outcomes, job authorization changes and result/evidence downloads. Test real owner adapters and the selected presentations against the same accepted/rejected transitions. Document which checks ran; the presence of a schema or test file is not a passing-run claim.

## 9. Definition of done

Implementation/adoption is complete only after the selected owner contracts, full request/response/OpenAPI schemas, API/security/version tests, affected data transitions, UI parity and operational recovery are verified. Publish actual identities/compatibility and migration guidance through the owning package process. This document supplies a concrete proposed workflow contract; it does not certify that release gate.
