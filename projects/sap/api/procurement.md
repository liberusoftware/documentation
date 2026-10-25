# Procurement: enterprise API design

**Status:** proposed composition contract. The [observed SAP source](../SOURCE-APPLICATION.md) establishes a foundation host, not these enterprise business endpoints. The paths, schemas and examples below require implementation/adoption review before any client uses them.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#procurement). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## 1. Purpose and ownership

Reuse supplier/master-data contracts, Maintenance purchasing where compatible, and Accounting receipt/payable contracts. Enterprise owns cross-entity sourcing, approval and matching orchestration only where those are genuine gaps.

The primary enterprise workflow record is a **purchase requisition**. A façade can coordinate owning product APIs and an enterprise read model, while the original product retains write authority for its records. `module-sap-procurement-api` is a design identifier; it does not establish a published Composer package or another authoritative business implementation.

Read the [detailed domain design](../design/procurement.md), [composition guide](../COMPOSITION.md), and [API architecture](../../../architecture/API.md) for the surrounding boundaries.

## 2. Contract design

The resource DTO exposes a stable identifier/type, workflow state, record version, authorized source/evidence references and permitted actions. Its domain fields are **`legal_entity_id`, `supplier_reference`, `requester_id`, `cost_center_id`, `currency`, `lines`, `budget_reference`, `approval_policy_version`, `required_by`**. The [domain field table](../design/procurement.md#records-and-required-context) defines their responsibilities; complete types, limits, sensitivity and required/nullable behavior must be reviewed with the actual owners.

Separate input from output schemas. Resolve actor/service, tenant membership and permitted legal entities from trusted authentication; submitted IDs select records but grant no authority. Resource state, audit fields, source results and permitted actions are server-owned. Paginated reads allowlist filters/sorts/includes and apply field/entity policy before serialization.

The proposed command protocol uses an actor/tenant-scoped `Idempotency-Key` and a documented record-version precondition such as `If-Match`. Scope a stored command result by operation and subject as well as identity; reusing a key with a different request is a conflict. Implement this storage/checking explicitly: passing a header alone does not make a downstream API idempotent.

## 3. Endpoint examples

These routes come from the detailed enterprise design. They are not a discovered runtime route list. Record creation/ingestion follows the owning workflow contract; there is no invented generic create/delete operation for an entire business group.

| Method | Proposed path | Responsibility |
| --- | --- | --- |
| GET | `/api/v1/enterprise/purchase-requisitions` | Authorized filtered/paginated workflow records |
| GET | `/api/v1/enterprise/purchase-requisitions/{id}` | Workflow detail, source references, state/version and permitted evidence |
| POST | `/api/v1/enterprise/purchase-requisitions/{id}/submit` | Explicit `submit` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/purchase-requisitions/{id}/approve` | Explicit `approve` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/purchase-requisitions/{id}/issue-order` | Explicit `issue-order` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/purchase-requisitions/{id}/record-receipt` | Explicit `record-receipt` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/purchase-requisitions/{id}/match` | Explicit `match` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/purchase-requisitions/{id}/close` | Explicit `close` command; validate transition, scope and command-specific inputs |

### record-receipt command

Proposed operation ID: `enterprise.procurement.record-receipt`. Scenario: `ordered` → `partially_received` after the business action is confirmed. The example IDs are illustrative; obtain actual identifiers from authorized records.

```http
POST /api/v1/enterprise/purchase-requisitions/requisition-example-001/record-receipt HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer YOUR_AUTHORIZED_TOKEN
If-Match: "record-v12"
Idempotency-Key: procurement-example-command-001
```

```json
{
  "order_reference": "purchase-order-example-001",
  "receipt_reference": "receipt-example-001",
  "received_at": "2026-10-25T10:00:00Z",
  "lines": [
    {
      "order_line_reference": "order-line-example-001",
      "received_quantity": "4.000",
      "unit": "each",
      "condition": "accepted"
    }
  ]
}
```

Validate the receiving actor/location, order line, units and quantity/tolerance policy. The owning stock/receipt service records physical movements; reject duplicate receipt identities.

Link the receipt and outstanding quantities. A partial receipt does not close the order or release an unmatched supplier invoice for payment.

Proposed acceptance response: `202 Accepted`, with `Location: /api/v1/operations/operation-example-001`. Authorization applies when polling the operation and retrieving its result. The returned queue state is not the final business state.

```json
{
  "data": {
    "id": "operation-example-001",
    "type": "operation",
    "attributes": {
      "status": "queued",
      "operation_id": "enterprise.procurement.record-receipt",
      "subject_reference": "requisition-example-001"
    },
    "links": {
      "self": "/api/v1/operations/operation-example-001"
    }
  },
  "meta": {
    "request_id": "request-example-001"
  }
}
```

## 4. OpenAPI schema

The reviewed fragment should define the resource and collection schemas, separate command bodies, operation/result schemas, scopes, version preconditions, idempotency semantics, errors and pagination. Use stable operation IDs for each explicit action and include the owning product/enterprise boundary. Validate/bundle the specification and compare it against supported contracts before generating clients.

This document includes a machine-readable **draft schema for the illustrated `record-receipt` request only**: [request schema](contracts/procurement.request.schema.json) and [matching example](contracts/procurement.request.example.json). Other command bodies and the complete response/OpenAPI bundle still require their own reviewed schemas. The specimen is not a full implemented service contract.

The specimen makes the illustrated business fields required and rejects unknown properties. Required fields, units, effective-date constraints, value ranges, enum sets and cross-record rules must be confirmed against the selected owner before a release; JSON type validation cannot establish authorization or business validity.

Reference: [JSON Schema 2020-12](https://json-schema.org/draft/2020-12) and [OpenAPI 3.1](https://spec.openapis.org/oas/v3.1.0).

## 5. Audience and operation matrix

Requesters manage own drafts; approvers act within delegated limits; receivers record quantities; AP handles invoice disputes.

| Audience | Exposure decision |
| --- | --- |
| Anonymous/public | Disabled for these workflow commands |
| Employee or approved external delegate | Only explicitly granted records, fields and actions; enforce source/evidence policy independently |
| Approver/operator | Domain authority and segregation/delegation policy apply to each action and bulk record |
| Service integration | Narrow service identity, permitted entities/operations, correlation and durable command identity |

An authenticated role name alone is insufficient where a record, value threshold, legal entity, time window or independent approval constrains the operation. Recheck permissions in jobs and evidence downloads.

## 6. Implementation strategy

Physical stock owners record inventory movements; Accounting owns payable and journal results. Match order, receipt, and supplier invoice references without creating another payable ledger.

Persist only enterprise-owned workflow/operation state and source references. Use local transactions for its invariants, then durable outbox/inbox or an equivalent owner-supported handoff. Confirm an existing source operation before retrying a timeout; do not repeat a side effect under a fresh identity. Product adapters translate schemas/errors without accessing another owner's private tables.

Presentations use explicit domain commands rather than a generic state patch. Filament/Livewire can invoke the reviewed public application boundary, while React/Inertia, Next.js, Vue/Nuxt and mobile use their appropriate authorized transport. Preserve one domain invariant and recovery contract across all surfaces.

## 7. Security, resilience, and observability

Hold unmatched or over-tolerance invoices with actionable discrepancies. A supplier timeout leaves an order handoff pending; query/retry by identity before issuing another order.

| Response condition | Proposed handling |
| --- | --- |
| 401 / 403 / scoped 404 | Authenticate or deny/conceal consistently; never retry under a broader identity |
| 409 conflict | Invalid transition, duplicate identity with another payload, or owner uniqueness conflict; expose an actionable current outcome |
| 412 precondition failed | Reload/review the changed record version; preserve safe draft inputs |
| 422 validation failed | Return field/domain errors without leaking hidden source records |
| 429 / 503 | Apply documented retry/backoff and preserve operation identity; reconcile uncertain outcomes before reissuing writes |

Use the shared Problem Details envelope, request/correlation IDs and scoped operator diagnostics. Redact protected data and credentials. Record source acknowledgements, last error, attempt count and recovery owner; an unavailable dependency must not silently advance the final state.

## 8. Verification strategy

- A requester cannot approve their own requisition under separation policy; partial receipts do not close the order; an over-tolerance invoice remains held.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

Also verify the illustrated command body against its draft request schema, allowed/denied/wrong-entity requests, stale versions, changed-payload key reuse, uncertain outcomes, job authorization changes and result/evidence downloads. Test real owner adapters and the selected presentations against the same accepted/rejected transitions. Document which checks ran; the presence of a schema or test file is not a passing-run claim.

## 9. Definition of done

Implementation/adoption is complete only after the selected owner contracts, full request/response/OpenAPI schemas, API/security/version tests, affected data transitions, UI parity and operational recovery are verified. Publish actual identities/compatibility and migration guidance through the owning package process. This document supplies a concrete proposed workflow contract; it does not certify that release gate.
