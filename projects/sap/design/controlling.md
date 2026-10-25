# Controlling: detailed enterprise design

**Status:** proposed design. Operation names, resource fields, permissions and routes below are target contracts to review with the selected owning packages. They are not claims of an implemented SAP API or published package.

## Boundary and reuse

Reuse Accounting dimensions, budgets, periods, and posted balances. Enterprise controlling owns documented allocation rules, scenario versions, and cross-unit profitability projections where missing.

Read the [composition design](../COMPOSITION.md) and [shared-source comparison](../../../architecture/SHARED-MODULE-COMPARISON.md) before selecting dependencies. The group may compose multiple existing domain/API/UI packages; a `module-sap-controlling` identifier does not justify another implementation of their owned business rules.

## Records and required context

The primary workflow record is **allocation run**. Its proposed contract includes:

| Field | Contract responsibility |
| --- | --- |
| `legal_entity_ids` | Selected organizational scope; independently authorize every referenced entity through authenticated membership and policy. |
| `period_id` | Stable owning-system identifier; resolve through its public boundary and verify actor access and relationship consistency. |
| `rule_version` | Immutable version or source snapshot used by the decision; reject stale input according to the operation contract. |
| `source_balance_snapshot_id` | Stable owning-system identifier; resolve through its public boundary and verify actor access and relationship consistency. |
| `driver_snapshot_id` | Stable owning-system identifier; resolve through its public boundary and verify actor access and relationship consistency. |
| `scenario_id` | Stable owning-system identifier; resolve through its public boundary and verify actor access and relationship consistency. |
| `rounding_policy` | Explicitly typed domain input or snapshot; define units, required/nullable behavior, limits, sensitivity and examples in the owning API schema. |

Every command also carries authenticated actor/service context, tenant scope, correlation ID, and an operation identity. Use server-resolved context; browser fields cannot grant authority. The record stores source references and decision evidence without duplicating every upstream record.

## Lifecycle and invariants

draft → simulated → approved → executing → reconciled; failed and cancelled runs retain their input snapshots.

Freeze source balances and drivers for a run. Require complete allocation weights, defined zero-driver behavior, conserved totals after rounding, and a clear distinction between simulations and posted adjustments.

Define each transition as an application use case, with typed validation/conflict outcomes and durable audit evidence. Use local transactions for the owner state; publish downstream work through a durable outbox or equivalent owner-supported mechanism. Preserve completed results under retries. Do not permit a generic status update to bypass a domain action.

## Proposed API operations

Use the owning product API where it already expresses the operation. The following façade is a proposed enterprise composition contract, to be exposed only after ownership and compatibility review:

| Method | Route | Purpose |
| --- | --- | --- |
| GET | `/api/v1/enterprise/allocation-runs` | Authorized filtered/paginated workflow records |
| GET | `/api/v1/enterprise/allocation-runs/{id}` | Workflow detail, source references, state/version and permitted evidence |
| POST | `/api/v1/enterprise/allocation-runs/{id}/simulate` | Explicit `simulate` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/allocation-runs/{id}/approve` | Explicit `approve` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/allocation-runs/{id}/execute` | Explicit `execute` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/allocation-runs/{id}/reconcile` | Explicit `reconcile` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/allocation-runs/{id}/cancel` | Explicit `cancel` command; validate transition, scope and command-specific inputs |

Publish separate request/response schemas and stable operation IDs. Return the current record version, permitted actions, field errors, and a durable operation reference for asynchronous work. Document `Idempotency-Key` semantics and concurrency preconditions; never imply they are already supported by a source package. A version mismatch requires review/reload, not blind overwrite. An accepted asynchronous command is not proof that downstream work completed.

## Permissions and integrations

Analysts simulate; controllers approve rules; posting authority remains with Accounting and the relevant entities.

Submit approved actual adjustment requests to Accounting; scenario results remain planning data until explicitly promoted through the posting boundary.

Recheck authorization on reads, commands, job execution, evidence exports and downloads. Job context must distinguish the original requester's authority from an integration service's permissions and record which authority allowed the operation.

## Failure and recovery

Partition runs by durable operation IDs. Resume incomplete partitions without reposting completed ones; route unexplained residuals to reconciliation rather than absorbing them silently.

Classify validation failures, permission denial, stale versions, duplicate commands, upstream rejection and temporary unavailability separately. Store last error, owner, attempt count, correlation/source references and next action. Operators need a scoped recovery action and evidence of the outcome. Sensitive payloads and credentials do not belong in UI error details or logs.

## Presentation design across layers

The workspace surfaces are **rule editor, driver completeness report, allocation preview, variance drill-down, run reconciliation**.

| Layer | Module-specific delivery |
| --- | --- |
| Core | Model the lifecycle above in typed use cases; delegate existing record writes to their canonical owner and persist only enterprise-owned orchestration state. |
| API | Publish the reviewed `allocation-runs` read model and explicit commands above, or map directly to existing product operations with documented differences. |
| Filament | Build a scoped work queue and record/evidence detail view. Expose only the permitted domain actions; preview bulk eligibility and show skipped/failed record outcomes. |
| Livewire | Keep filters, selected record/version and draft command input in component state. Reauthorize on every action and hydrate no private model data into public state. |
| React + Inertia | Laravel owns workspace routes and authorized props. Shared React UI renders the record/evidence; Inertia wrappers handle visits, command errors and redirect state. |
| Vue + Inertia | Use the same record/action contract in Vue components; preserve Laravel validation and policy outcomes through the Inertia wrapper. |
| Next.js | Application-owned routes compose authorized API reads and command adapters. Separate server integration from interactive components; disable shared caching until tenant/permission keys are reviewed. |
| Nuxt | Compose authorized API reads with an explicit server/browser transport. Keep credentials in server configuration and isolate SSR state/cache by scope. |
| React Native | Provide focused review/detail screens with secure session handling and bounded evidence uploads. Queue only approved draft capture offline; consequential transitions require fresh server validation. |
| Flutter | Use typed DTOs and explicit loading/error/conflict widgets. Show stale/offline state, protect local evidence, and require server acknowledgment before displaying a command as complete. |

All presentations display active entity, source reference, record version, current state, evidence access and recovery guidance. Format dates/amounts with the actual locale and units. Use keyboard/focus support and announced field/action errors. Permission-sensitive fields must be removed at the server boundary, not hidden only by CSS or client logic.

## Acceptance scenarios

- Zero or missing drivers produce a defined error; rerunning an execution key does not duplicate allocations; rounded destinations reconcile to the source total.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

Verify actual package behavior, migrations, supported upgrades and clean-consumer installation before promoting dependencies as stable. This design is a reviewable implementation target; test execution and source adoption evidence must be recorded separately.
