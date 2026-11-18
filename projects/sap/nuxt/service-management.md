# Service management: Nuxt design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/service-management.md) and [API plan](../api/service-management.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#service-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

Reuse CRM case management, knowledge, SLA/entitlements, and Control Panel monitoring. Enterprise adds cross-product service context, major-incident coordination, and controlled change orchestration where missing.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** triage inbox, incident timeline, sla clock explanation, service impact map, change/knowledge links.

**Business lifecycle:** new → triaged → assigned → investigating → resolved → closed; reopened incidents retain the prior resolution.

Version the priority and SLA basis, define pause conditions and business calendars, and preserve customer-visible communication separately from internal technical notes. Change approval is distinct from incident urgency.

The illustrated `resolve` command takes `resolution_code`, `resolution_summary`, `evidence_references`, `change_reference`, with a documented record-version precondition and scoped operation identity. It starts from `investigating` and reaches `resolved` only after its defined business outcome. The [API example](../api/service-management.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/service-management.request.schema.json).

Require resolution authority and evidence for the selected service/entitlement. Keep customer-visible resolution text separate from restricted internal notes; validate any linked change authority.

Record the resolution and SLA outcome. Closure and any later reopening preserve the earlier resolution evidence and are separate lifecycle actions.

## Layer implementation

The Nuxt application owns its workspace routes, session integration and deployment. The module contributes typed components/composables and an API adapter, with server-only secrets kept out of public runtime configuration and browser payloads.

The proposed API family is `/api/v1/enterprise/service-incidents`. Review actual deployed schemas before generating clients. Server/browser transport validates the authorized DTO and invokes explicit actions such as `resolve` rather than a generic status update.

Start protected reads without shared caching until tenant/entity/permission keys and invalidation are reviewed. Resolve authenticated context per request and never keep request-specific scope in shared SSR state. A client-provided target URL or tenant value cannot select a privileged upstream origin or grant access.

The command form preserves `resolution_code`, `resolution_summary`, `evidence_references`, `change_reference`, field errors and current record version. On timeout/conflict, query the operation/current subject under the same authorization and show recovery guidance before another write. Separate Vue UI primitives from Nuxt-specific navigation and server transport so they can be reused with Inertia.

## Authorization, recovery and operations

Agents see entitled customer records; incident commanders coordinate; change approvers authorize production changes independently.

Deduplicate repeated alerts into an incident correlation policy. Escalate missed acknowledgements and failed automation visibly; a failed run never marks the incident resolved automatically.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- A pause reason affects only permitted SLA clocks; repeated alerts follow correlation policy; restricted internal notes never appear in customer/mobile projections.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `resolve` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `resolved` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-enterprise-sap-nuxt-vue`](https://github.com/liberusoftware/project-enterprise-sap-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-enterprise-sap-laravel-api`](https://github.com/liberusoftware/project-enterprise-sap-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/service-management.md)) |
| Capability Nuxt module skeleton | [`module-sap-service-management-nuxt`](https://github.com/liberusoftware/module-sap-service-management-nuxt) (`@liberusoftware/module-sap-service-management-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Catalog** | Expose composable and Vue 3 component for `catalog` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/service-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **Requests** | Expose composable and Vue 3 component for `requests` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/service-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **Incidents** | Expose composable and Vue 3 component for `incidents` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/service-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **Problems** | Expose composable and Vue 3 component for `problems` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/service-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **Changes** | Expose composable and Vue 3 component for `changes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/service-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **Knowledge** | Expose composable and Vue 3 component for `knowledge` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/service-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **CMDB** | Expose composable and Vue 3 component for `cmdb` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/service-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **SLA** | Expose composable and Vue 3 component for `sla` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/service-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **Field service** | Expose composable and Vue 3 component for `field service` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/service-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
