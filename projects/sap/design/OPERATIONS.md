# Shared enterprise command and operation design

**Status:** proposed shared infrastructure within the enterprise foundation. The current SAP foundation host does not establish implementation of this protocol. Reuse a verified existing operation/outbox contract where it meets these requirements; do not create a separate job framework or operation ledger for each enterprise domain.

## Ownership and records

The business owner decides whether a transition is valid and commits its authoritative record. Enterprise orchestration stores its own command delivery and acknowledgements plus source references. A posting batch must not become another general ledger; a procurement handoff must not become another inventory or payable ledger.

The common operation record needs an opaque ID, tenant/entity scope, authenticated requester/service reference, subject owner/type/ID, command name, request contract version, expected subject version, payload hash, scoped idempotency identity, lifecycle timestamps, attempts, last error, recovery owner and source acknowledgement/result references. Store only the payload needed for controlled execution and retention; protected source data, secrets and unrestricted record snapshots do not belong in generic diagnostic tables.

Enforce command uniqueness with a database constraint over the documented identity scope, not a cache check alone. That scope includes tenant, effective principal/integration identity, subject owner/reference and operation. Document the key retention window. A repeated key with the same canonical request returns the recorded outcome; a different canonical request under that key is a conflict. Canonicalization must preserve business-significant values and contract versions.

## Two distinct state machines

| Operation delivery state | Meaning |
| --- | --- |
| Accepted/queued | The request was recorded durably; downstream business work is not confirmed |
| Running | A worker owns a bounded execution attempt |
| Waiting for acknowledgement | The owner may have accepted work; poll/query/reconcile before retrying |
| Succeeded | The documented owner outcome and required evidence were recorded |
| Failed/review required | The operation cannot progress without a defined retry, correction or review |
| Cancelled | Cancellation was accepted under the operation/owner policy; it does not undo committed business effects automatically |

Keep these separate from the business lifecycle. A queued posting request is not a posted journal. A provisioning operation can be running while the business request is still approved or provisioning. A revoked access grant may still have downstream invalidation acknowledgements pending. Display both states and their meanings rather than inventing one universal status field.

## Admission and concurrency

1. Authenticate the request and resolve permitted tenant/entity/subject context. Submitted identifiers select records; they never grant authority.
2. Validate the command-specific request schema, input classification and domain references. Apply segregation of duties, delegation, effective dates and value limits.
3. Check the subject version according to the documented precondition contract. Perform the version/state check and the local invariant-changing write atomically, or use the owner's equivalent conditional command.
4. Persist the scoped operation identity and required outbox work within the local transaction. Return an existing result for a known equivalent request instead of enqueueing a second command.
5. Return a synchronous result only after its documented local outcome is committed. Otherwise return an authorized operation reference and explain what remains pending.

A transaction around an enterprise projection does not protect an upstream business record. Forward the owner's supported concurrency/identity contract and handle a stale/rejected result explicitly. If an owner offers no idempotency or conditional operation contract, document reconciliation/serialization limits; a gateway header cannot manufacture exactly-once external effects.

## Worker and handoff behavior

Workers carry only the required subject/context and operation identity. Reauthorize according to the chosen requester/service execution policy; record the authority used and what happens after requester permission changes. Enforce tenant and field policy in exports, attachments, notifications and follow-up queries as well as the initial command.

Use bounded timeouts, retries/backoff and a durable inbox/outbox or equivalent. Before retrying an uncertain write, query the owner by operation/source identity when supported. Persist source acknowledgement and result references so recovery survives process restarts. A provider timeout is not proof that the write failed.

Do not hold a distributed database transaction across products. Compensation uses explicit owner-supported actions, such as reversal or cancellation, with its own authorization and evidence. Report compensation failures and retained partial resources; do not hide them behind a final success state.

## HTTP and presentation contract

The shared API design uses an authorized operation resource, such as the architecture's proposed `/api/v1/operations/{operation_id}`. Define status/result fields, progress interpretation, retry timing, expiry, cancellation policy and access rules in its actual schema. Polling a valid operation ID is still subject to tenant/resource authorization.

All presentations need the subject reference/version, business state, operation state, permitted actions, field errors and authorized evidence/result links. They can compose a common status/timeline component, translated into Filament, Livewire, React/Inertia, Next.js, Vue/Nuxt, React Native or Flutter without moving domain decisions into UI code.

Inertia page requests use the Inertia protocol; a bare REST JSON response is not an Inertia page. A Laravel-hosted controller/component may invoke a public application boundary directly. An independently deployed Next.js/Nuxt/mobile client uses the reviewed API transport. Share contracts and framework-independent view primitives while preserving these different lifecycles.

## Bulk actions and downloads

Preview bulk eligibility using actual policy and current versions, then execute each selected record under its own command identity/result. A partial batch reports succeeded, denied, conflicted, skipped and failed items with safe explanations. Retrying the batch must not repeat completed external effects.

Exports and evidence downloads recheck access at generation and retrieval. Bind artifacts to permitted tenant/entity/field scope, expiry and retention policy. Avoid public cache keys for protected results; report source freshness and watermark limitations when the artifact is a governed cross-product report.

## Verification and operation

Verify concurrent equivalent submissions, changed-payload key reuse, stale versions, crash boundaries, permission revocation, owner rejection, lost acknowledgements, duplicate deliveries, partial compensation, operation/result access and download expiry. Check database constraints and real owner integrations, not only a mocked queue.

Operators need the correlation and source references, last attempt/error, next eligible retry time, accountable recovery role and a scoped recovery action. Monitor queue age, acknowledgement lag, failed/review-required operations and reconciliation discrepancies. Retain evidence according to data/hold policy without logging protected payloads.

Each domain's [detailed design](README.md) and [API plan](../api/README.md) supplies its business-specific rules. Shared mechanics belong here so the domains and presentation layers do not grow competing operation implementations.
