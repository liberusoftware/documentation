# Hosting and cloud: Nuxt design

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

The Nuxt application owns its workspace routes, session integration and deployment. The module contributes typed components/composables and an API adapter, with server-only secrets kept out of public runtime configuration and browser payloads.

The proposed API family is `/api/v1/enterprise/provisioning-requests`. Review actual deployed schemas before generating clients. Server/browser transport validates the authorized DTO and invokes explicit actions such as `provision` rather than a generic status update.

Start protected reads without shared caching until tenant/entity/permission keys and invalidation are reviewed. Resolve authenticated context per request and never keep request-specific scope in shared SSR state. A client-provided target URL or tenant value cannot select a privileged upstream origin or grant access.

The command form preserves `service_template_version`, `region`, `capacity_request`, `approved_change_reference`, `target_platform`, field errors and current record version. On timeout/conflict, query the operation/current subject under the same authorization and show recovery guidance before another write. Separate Vue UI primitives from Nuxt-specific navigation and server transport so they can be reused with Inertia.

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

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-enterprise-sap-nuxt-vue`](https://github.com/liberusoftware/project-enterprise-sap-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-enterprise-sap-laravel-api`](https://github.com/liberusoftware/project-enterprise-sap-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/hosting-and-cloud.md)) |
| Capability Nuxt module skeleton | [`module-sap-hosting-and-cloud-nuxt`](https://github.com/liberusoftware/module-sap-hosting-and-cloud-nuxt) (`@liberusoftware/module-sap-hosting-and-cloud-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Services** | Expose composable and Vue 3 component for `services` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/hosting-and-cloud.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **Subscriptions** | Expose composable and Vue 3 component for `subscriptions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/hosting-and-cloud.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **Provisioning** | Expose composable and Vue 3 component for `provisioning` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/hosting-and-cloud.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **Infrastructure inventory** | Expose composable and Vue 3 component for `infrastructure inventory` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/hosting-and-cloud.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **Domains/DNS** | Expose composable and Vue 3 component for `domains/dns` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/hosting-and-cloud.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **Capacity** | Expose composable and Vue 3 component for `capacity` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/hosting-and-cloud.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **Usage** | Expose composable and Vue 3 component for `usage` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/hosting-and-cloud.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **Operations** | Expose composable and Vue 3 component for `operations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/hosting-and-cloud.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
