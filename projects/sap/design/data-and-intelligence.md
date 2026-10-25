# Data and intelligence: detailed enterprise design

**Status:** proposed design. Operation names, resource fields, permissions and routes below are target contracts to review with the selected owning packages. They are not claims of an implemented SAP API or published package.

## Boundary and reuse

Operational products own transactional records and domain metrics. Enterprise owns governed semantic definitions, cross-product projections, lineage and report delivery where needed.

Read the [composition design](../COMPOSITION.md) and [shared-source comparison](../../../architecture/SHARED-MODULE-COMPARISON.md) before selecting dependencies. The group may compose multiple existing domain/API/UI packages; a `module-sap-data-and-intelligence` identifier does not justify another implementation of their owned business rules.

## Records and required context

The primary workflow record is **governed report run**. Its proposed contract includes:

| Field | Contract responsibility |
| --- | --- |
| `report_definition_version` | Immutable version or source snapshot used by the decision; reject stale input according to the operation contract. |
| `legal_entity_scope` | Selected organizational scope; independently authorize every referenced entity through authenticated membership and policy. |
| `parameter_snapshot` | Explicitly typed domain input or snapshot; define units, required/nullable behavior, limits, sensitivity and examples in the owning API schema. |
| `source_watermarks` | Immutable version or source snapshot used by the decision; reject stale input according to the operation contract. |
| `metric_definition_versions` | Immutable version or source snapshot used by the decision; reject stale input according to the operation contract. |
| `requested_by` | Explicitly typed domain input or snapshot; define units, required/nullable behavior, limits, sensitivity and examples in the owning API schema. |
| `output_policy` | Explicitly typed domain input or snapshot; define units, required/nullable behavior, limits, sensitivity and examples in the owning API schema. |
| `expires_at` | Explicitly typed domain input or snapshot; define units, required/nullable behavior, limits, sensitivity and examples in the owning API schema. |

Every command also carries authenticated actor/service context, tenant scope, correlation ID, and an operation identity. Use server-resolved context; browser fields cannot grant authority. The record stores source references and decision evidence without duplicating every upstream record.

## Lifecycle and invariants

requested → authorized → queued → running → ready → expired; failed and cancelled preserve execution evidence.

Apply row/field policy to every source and output; record freshness and lineage. Define currency/timezone and period semantics. Published metrics need an accountable definition owner; AI suggestions do not become authoritative transactions.

Define each transition as an application use case, with typed validation/conflict outcomes and durable audit evidence. Use local transactions for the owner state; publish downstream work through a durable outbox or equivalent owner-supported mechanism. Preserve completed results under retries. Do not permit a generic status update to bypass a domain action.

## Proposed API operations

Use the owning product API where it already expresses the operation. The following façade is a proposed enterprise composition contract, to be exposed only after ownership and compatibility review:

| Method | Route | Purpose |
| --- | --- | --- |
| GET | `/api/v1/enterprise/report-runs` | Authorized filtered/paginated workflow records |
| GET | `/api/v1/enterprise/report-runs/{id}` | Workflow detail, source references, state/version and permitted evidence |
| POST | `/api/v1/enterprise/report-runs/{id}/validate` | Explicit `validate` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/report-runs/{id}/run` | Explicit `run` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/report-runs/{id}/cancel` | Explicit `cancel` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/report-runs/{id}/refresh` | Explicit `refresh` command; validate transition, scope and command-specific inputs |
| POST | `/api/v1/enterprise/report-runs/{id}/download` | Explicit `download` command; validate transition, scope and command-specific inputs |

Publish separate request/response schemas and stable operation IDs. Return the current record version, permitted actions, field errors, and a durable operation reference for asynchronous work. Document `Idempotency-Key` semantics and concurrency preconditions; never imply they are already supported by a source package. A version mismatch requires review/reload, not blind overwrite. An accepted asynchronous command is not proof that downstream work completed.

## Permissions and integrations

Authors define reports within approved sources; data owners approve sensitive fields; viewers can run/export only their permitted entity and purpose scope.

Build projections from published APIs/events or approved analytical feeds, with source watermarks and reconciliation. Keep report execution read-only against transactional domains.

Recheck authorization on reads, commands, job execution, evidence exports and downloads. Job context must distinguish the original requester's authority from an integration service's permissions and record which authority allowed the operation.

## Failure and recovery

A stale or incomplete feed must be visible in output metadata and may block governed reports. Retry failed partitions with the same run identity; recheck authorization at download time.

Classify validation failures, permission denial, stale versions, duplicate commands, upstream rejection and temporary unavailability separately. Store last error, owner, attempt count, correlation/source references and next action. Operators need a scoped recovery action and evidence of the outcome. Sensitive payloads and credentials do not belong in UI error details or logs.

## Presentation design across layers

The workspace surfaces are **report catalogue, filter/freshness preview, run progress, lineage drill-down, governed metric explanations**.

| Layer | Module-specific delivery |
| --- | --- |
| Core | Model the lifecycle above in typed use cases; delegate existing record writes to their canonical owner and persist only enterprise-owned orchestration state. |
| API | Publish the reviewed `report-runs` read model and explicit commands above, or map directly to existing product operations with documented differences. |
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

- A report cannot leak a hidden entity through totals or cache reuse; revoked access blocks download; source totals and declared watermark reconciliation agree.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

Verify actual package behavior, migrations, supported upgrades and clean-consumer installation before promoting dependencies as stable. This design is a reviewable implementation target; test execution and source adoption evidence must be recorded separately.
