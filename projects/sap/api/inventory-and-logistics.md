# Inventory and logistics: enterprise API design

**Status:** proposed composition contract. The [observed SAP source](../SOURCE-APPLICATION.md) establishes a foundation host, not these enterprise business endpoints. The paths, schemas and examples below require implementation/adoption review before any client uses them.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#inventory-and-logistics). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## 1. Purpose and ownership

Review Ecommerce inventory/reservation and Maintenance stock contracts before adding another physical ledger. Accounting retains valuation and financial posting ownership.

The primary enterprise workflow record is a **stock transfer**. A façade can coordinate owning product APIs and an enterprise read model, while the original product retains write authority for its records. `module-sap-inventory-and-logistics-api` is a design identifier; it does not establish a published Composer package or another authoritative business implementation.

Read the [detailed domain design](../design/inventory-and-logistics.md), [composition guide](../COMPOSITION.md), and [API architecture](../../../architecture/API.md) for the surrounding boundaries.

## 2. Contract design

The resource DTO exposes a stable identifier/type, workflow state, record version, authorized source/evidence references and permitted actions. Its domain fields are **`legal_entity_id`, `item_reference`, `source_location_id`, `destination_location_id`, `quantity`, `unit`, `lot_reference`, `serial_references`, `expected_version`**. The [domain field table](../design/inventory-and-logistics.md#records-and-required-context) defines their responsibilities; complete types, limits, sensitivity and required/nullable behavior must be reviewed with the actual owners.

Separate input from output schemas. Resolve actor/service, tenant membership and permitted legal entities from trusted authentication; submitted IDs select records but grant no authority. Resource state, audit fields, source results and permitted actions are server-owned. Paginated reads allowlist filters/sorts/includes and apply field/entity policy before serialization.

The proposed command protocol uses an actor/tenant-scoped `Idempotency-Key` and a documented record-version precondition such as `If-Match`. Scope a stored command result by operation and subject as well as identity; reusing a key with a different request is a conflict. Implement this storage/checking explicitly: passing a header alone does not make a downstream API idempotent.

## 3. Endpoint examples

These routes come from the detailed enterprise design. They are not a discovered runtime route list. Record creation/ingestion follows the owning workflow contract; there is no invented generic create/delete operation for an entire business group.

| Method | Proposed path | Responsibility |
| --- | --- | --- |
| GET | `/api/v1/enterprise/stock-transfers` | Authorized filtered/paginated workflow records |
| GET | `/api/v1/enterprise/stock-transfers/{id}` | Workflow detail, source references, state/version and permitted evidence |
| POST | `/api/v1/enterprise/stock-transfers/{id}/reserve` | Explicit `reserve` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/stock-transfers/{id}/dispatch` | Explicit `dispatch` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/stock-transfers/{id}/receive` | Explicit `receive` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/stock-transfers/{id}/reconcile` | Explicit `reconcile` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/stock-transfers/{id}/cancel` | Explicit `cancel` command; validate transition, scope and command-specific inputs |

### receive command

Proposed operation ID: `enterprise.inventory-and-logistics.receive`. Scenario: `dispatched` → `partially_received` after the business action is confirmed. The example IDs are illustrative; obtain actual identifiers from authorized records.

```http
POST /api/v1/enterprise/stock-transfers/transfer-example-001/receive HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer YOUR_AUTHORIZED_TOKEN
If-Match: "record-v12"
Idempotency-Key: inventory-and-logistics-example-command-001
```

```json
{
  "receipt_reference": "transfer-receipt-example-001",
  "destination_location_id": "warehouse-example-002",
  "received_at": "2026-10-25T10:30:00Z",
  "lines": [
    {
      "item_reference": "item-example-001",
      "quantity": "3.000",
      "unit": "each",
      "lot_reference": "lot-example-001",
      "condition": "accepted"
    }
  ]
}
```

Require authorized destination custody, correct units and lot/serial policy, and conserved dispatched/received/in-transit quantities. Validate the movement identity at the selected stock owner.

Record received quantities and discrepancies separately. Financial valuation is a linked Accounting event, not a direct write from the receiving UI.

Proposed acceptance response: `202 Accepted`, with `Location: /api/v1/operations/operation-example-001`. Authorization applies when polling the operation and retrieving its result. The returned queue state is not the final business state.

```json
{
  "data": {
    "id": "operation-example-001",
    "type": "operation",
    "attributes": {
      "status": "queued",
      "operation_id": "enterprise.inventory-and-logistics.receive",
      "subject_reference": "transfer-example-001"
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

This document includes a machine-readable **draft schema for the illustrated `receive` request only**: [request schema](contracts/inventory-and-logistics.request.schema.json) and [matching example](contracts/inventory-and-logistics.request.example.json). Other command bodies and the complete response/OpenAPI bundle still require their own reviewed schemas. The specimen is not a full implemented service contract.

The specimen makes the illustrated business fields required and rejects unknown properties. Required fields, units, effective-date constraints, value ranges, enum sets and cross-record rules must be confirmed against the selected owner before a release; JSON type validation cannot establish authorization or business validity.

Reference: [JSON Schema 2020-12](https://json-schema.org/draft/2020-12) and [OpenAPI 3.1](https://spec.openapis.org/oas/v3.1.0).

## 5. Audience and operation matrix

Warehouse staff act only on assigned locations; supervisors approve adjustments and discrepancy resolution; valuation authority is separate.

| Audience | Exposure decision |
| --- | --- |
| Anonymous/public | Disabled for these workflow commands |
| Employee or approved external delegate | Only explicitly granted records, fields and actions; enforce source/evidence policy independently |
| Approver/operator | Domain authority and segregation/delegation policy apply to each action and bulk record |
| Service integration | Narrow service identity, permitted entities/operations, correlation and durable command identity |

An authenticated role name alone is insufficient where a record, value threshold, legal entity, time window or independent approval constrains the operation. Recheck permissions in jobs and evidence downloads.

## 6. Implementation strategy

The selected stock owner writes physical movements; Accounting receives valuation events. Order and work-order owners hold reservation references and request release through public contracts.

Persist only enterprise-owned workflow/operation state and source references. Use local transactions for its invariants, then durable outbox/inbox or an equivalent owner-supported handoff. Confirm an existing source operation before retrying a timeout; do not repeat a side effect under a fresh identity. Product adapters translate schemas/errors without accessing another owner's private tables.

Presentations use explicit domain commands rather than a generic state patch. Filament/Livewire can invoke the reviewed public application boundary, while React/Inertia, Next.js, Vue/Nuxt and mobile use their appropriate authorized transport. Preserve one domain invariant and recovery contract across all surfaces.

## 7. Security, resilience, and observability

Record short/over/damaged receipt discrepancies separately. Retry a scanner submission under its original movement identity; do not repair discrepancies by editing stock balances directly.

| Response condition | Proposed handling |
| --- | --- |
| 401 / 403 / scoped 404 | Authenticate or deny/conceal consistently; never retry under a broader identity |
| 409 conflict | Invalid transition, duplicate identity with another payload, or owner uniqueness conflict; expose an actionable current outcome |
| 412 precondition failed | Reload/review the changed record version; preserve safe draft inputs |
| 422 validation failed | Return field/domain errors without leaking hidden source records |
| 429 / 503 | Apply documented retry/backoff and preserve operation identity; reconcile uncertain outcomes before reissuing writes |

Use the shared Problem Details envelope, request/correlation IDs and scoped operator diagnostics. Redact protected data and credentials. Record source acknowledgements, last error, attempt count and recovery owner; an unavailable dependency must not silently advance the final state.

## 8. Verification strategy

- Concurrent reservations cannot oversell controlled stock; duplicate scans do not double-receive; source plus transit plus destination quantities reconcile.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

Also verify the illustrated command body against its draft request schema, allowed/denied/wrong-entity requests, stale versions, changed-payload key reuse, uncertain outcomes, job authorization changes and result/evidence downloads. Test real owner adapters and the selected presentations against the same accepted/rejected transitions. Document which checks ran; the presence of a schema or test file is not a passing-run claim.

## 9. Definition of done

Implementation/adoption is complete only after the selected owner contracts, full request/response/OpenAPI schemas, API/security/version tests, affected data transitions, UI parity and operational recovery are verified. Publish actual identities/compatibility and migration guidance through the owning package process. This document supplies a concrete proposed workflow contract; it does not certify that release gate.
