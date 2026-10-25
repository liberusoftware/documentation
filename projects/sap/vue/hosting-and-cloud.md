# Hosting and cloud: Vue + Inertia design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/hosting-and-cloud.md) and [API plan](../api/hosting-and-cloud.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#hosting-and-cloud). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

Billing owns commercial subscriptions and provisioning demand; Control Panel owns infrastructure lifecycle and adapters. Enterprise coordinates approval, tenancy, capacity and reconciliation.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** service request wizard, capacity preview, approval summary, provisioning progress, drift and failed-resource reconciliation.

**Business lifecycle:** requested → validated → approved → queued → provisioning → active; failed, compensating, suspended and retired remain observable.

Check region/capacity policy, tenant ownership, entitlement, and template compatibility. Store secret references rather than credentials in operation payloads. A paid order does not prove a resource is active.

The illustrated `provision` command takes `service_template_version`, `region`, `capacity_request`, `approved_change_reference`, `target_platform`, with a documented record-version precondition and scoped operation identity. It starts from `approved` and reaches `active` only after its defined business outcome. The [API example](../api/hosting-and-cloud.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/hosting-and-cloud.request.schema.json).

Validate entitlement, allowed region, capacity, approved template and change authority. Payloads contain secret references only where required, never provider credentials.

Control Panel returns an observed resource reference and outcome. Partial creation retains created-resource and compensation evidence until reconciled.

## Layer implementation

The Laravel host owns Inertia routes/controllers and passes authorized serializable page props to typed Vue components/composables. Compose a queue, subject/evidence detail and `provision` form for the domain workspace. Props include the record/version, permitted actions, safe draft defaults and operation reference, not an unrestricted model snapshot.

An Inertia visit expects an Inertia page/redirect lifecycle. Use the Laravel controller's reviewed public application boundary or a deliberate API adapter and then return the appropriate Inertia response. Do not point an Inertia page visit at a bare REST JSON endpoint and assume it is an Inertia page.

Keep `service_template_version`, `region`, `capacity_request`, `approved_change_reference`, `target_platform` in a typed command draft and map actual server field errors to the form. Preserve navigation/filter state where safe, focus the actionable error summary, and reload/review a stale record before resubmission. Laravel reauthorizes every command independently of client visibility.

Share framework-independent Vue primitives with Nuxt where the contracts fit. Keep Inertia navigation/forms/page props in its wrapper and Nuxt server/browser transport, routing and runtime configuration in its adapter.

The Vue UI displays business and operation states separately. A queued response preserves a pending status and authorized progress link; it does not manufacture the eventual domain outcome in local state.

## Authorization, recovery and operations

Customers request entitled services; operators act on scoped infrastructure; approvers authorize high-impact or high-cost changes.

On partial infrastructure creation, record every created resource and compensation result. Query provider/control-plane state before retry; a new retry must not allocate another billable resource unintentionally.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- A retry returns the existing resource reference; partial failure is recoverable; secrets are absent from UI/log projections and cross-tenant resource access is denied.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `provision` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `active` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.
