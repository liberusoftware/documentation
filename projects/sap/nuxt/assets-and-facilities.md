# Assets and facilities: Nuxt design

**Status:** proposed enterprise implementation. The [current SAP foundation](../SOURCE-APPLICATION.md) does not establish these business workflows or this presentation as implemented. Use the [detailed domain contract](../design/assets-and-facilities.md) and [API plan](../api/assets-and-facilities.md) as the review target.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#assets-and-facilities). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Ownership and delivery scope

Maintenance owns operational assets, inspections and work orders; Accounting owns capitalization, depreciation and disposal postings. Enterprise coordinates custody, locations, facilities and cross-domain evidence.

Reuse the [shared enterprise operation design](../design/OPERATIONS.md) for command identities, concurrency, handoffs and recovery. This capability group adds only its own orchestration/projection and genuine missing behavior; it does not create another owner for existing product records.

## Workflow and command contract

**Workspace surfaces:** asset/custody search, handover checklist, inspection evidence, discrepancy queue, operational-to-financial reconciliation.

**Business lifecycle:** draft → approved → in_transit → accepted → reconciled; rejected and lost_or_damaged preserve custody evidence.

Keep physical asset identity distinct from its financial record. Require explicit custody acceptance, valid location/entity mappings, inspection evidence where needed, and a separate disposal authorization.

The illustrated `accept` command takes `to_custodian_reference`, `location_reference`, `condition_snapshot_id`, `acceptance_evidence_id`, with a documented record-version precondition and scoped operation identity. It starts from `in_transit` and reaches `accepted` only after its defined business outcome. The [API example](../api/assets-and-facilities.md#3-endpoint-examples) provides the proposed body and [draft request schema](../api/contracts/assets-and-facilities.request.schema.json).

Validate the receiving custodian, authorized location, required inspection and current custody version. Conflicting concurrent acceptance must not create two current custodians.

Record the accepted custody transition. Damage/discrepancy and financial capitalization/disposal stay with their respective owner workflows.

## Layer implementation

The Nuxt application owns its workspace routes, session integration and deployment. The module contributes typed components/composables and an API adapter, with server-only secrets kept out of public runtime configuration and browser payloads.

The proposed API family is `/api/v1/enterprise/asset-handovers`. Review actual deployed schemas before generating clients. Server/browser transport validates the authorized DTO and invokes explicit actions such as `accept` rather than a generic status update.

Start protected reads without shared caching until tenant/entity/permission keys and invalidation are reviewed. Resolve authenticated context per request and never keep request-specific scope in shared SSR state. A client-provided target URL or tenant value cannot select a privileged upstream origin or grant access.

The command form preserves `to_custodian_reference`, `location_reference`, `condition_snapshot_id`, `acceptance_evidence_id`, field errors and current record version. On timeout/conflict, query the operation/current subject under the same authorization and show recovery guidance before another write. Separate Vue UI primitives from Nuxt-specific navigation and server transport so they can be reused with Inertia.

## Authorization, recovery and operations

Custodians acknowledge receipt; asset managers approve changes; finance authorizes capitalization/disposal financial effects.

Unaccepted or damaged handovers stay in a discrepancy queue. Never complete offboarding by deleting an assigned asset or clearing its custody history.

Show the selected entity, source/subject reference, current business state and separate operation progress. Preserve safe drafts on validation/conflict. Reauthenticate on expiry and discard protected cached data after scope/permission changes. A network timeout never establishes whether an external write succeeded; use the durable operation/source reference for reconciliation.

## Module-specific acceptance

- The same asset cannot be concurrently accepted by two custodians; damaged receipts remain unresolved; disposal retains financial and custody references.
- Repeated commands return the documented existing result or a clear conflict; they cannot duplicate a completed external side effect.
- A tenant/entity switch, permission revocation or expired session cannot reuse another scope's cached record, attachment or exported file.
- A downstream failure remains observable with a valid owner/recovery path across every enabled presentation.

- Exercise the `accept` example with allowed, denied, invalid, stale, duplicate and uncertain-result paths; confirm `accepted` only from its authoritative outcome.
- Verify the enabled layer uses the same domain/operation contract as other surfaces and cannot bypass it through generic saves, hydrated state, direct JSON fields or offline replay.
- Check scope changes, revoked permissions, evidence/result access, accessible errors and recovery in a representative consuming host. Record actual commands/results before describing the implementation as verified.

Use [testing](../../../standards/TESTING.md), [API architecture](../../../architecture/API.md), [shared operations](../design/OPERATIONS.md), and the [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) lifecycle guides for the remaining delivery requirements.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-enterprise-sap-nuxt-vue`](https://github.com/liberusoftware/project-enterprise-sap-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-enterprise-sap-laravel-api`](https://github.com/liberusoftware/project-enterprise-sap-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/assets-and-facilities.md)) |
| Capability Nuxt module skeleton | [`module-sap-assets-and-facilities-nuxt`](https://github.com/liberusoftware/module-sap-assets-and-facilities-nuxt) (`@liberusoftware/module-sap-assets-and-facilities-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Asset lifecycle** | Expose composable and Vue 3 component for `asset lifecycle` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/assets-and-facilities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **Maintenance** | Expose composable and Vue 3 component for `maintenance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/assets-and-facilities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **Leases** | Expose composable and Vue 3 component for `leases` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/assets-and-facilities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **Locations** | Expose composable and Vue 3 component for `locations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/assets-and-facilities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **Facilities** | Expose composable and Vue 3 component for `facilities` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/assets-and-facilities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **Energy** | Expose composable and Vue 3 component for `energy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/assets-and-facilities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **Safety** | Expose composable and Vue 3 component for `safety` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/assets-and-facilities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |
| **Disposal** | Expose composable and Vue 3 component for `disposal` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/assets-and-facilities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-enterprise-sap-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
