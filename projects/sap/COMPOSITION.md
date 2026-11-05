# Enterprise suite composition and delivery design

**Status:** target enterprise design over an observed foundation host. The complete organization scan includes [`project-enterprise-sap-laravel-filament`](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament); read its [current source/foundation map](SOURCE-APPLICATION.md). The host does not by itself establish implementation of the business-domain contracts below, and this design does not certify production readiness.

The [enterprise scope](SAP.md) describes outcomes and capability groups. Those groups are solution workspaces, not instructions to duplicate every underlying domain in a new `sap-*` package. Reuse the owning product package, then add enterprise orchestration or missing capabilities only when its public contracts cannot meet the requirement.

## Domain ownership and reuse

| Enterprise capability | Existing source candidates | Enterprise-specific responsibility |
| --- | --- | --- |
| Identity, tenancy, policy, audit, files, notifications | Shared `identity-core`, `organizations-teams`, `roles-permissions`, `audit`, `files-media`, and `notifications` in multiple source applications | Map legal entities and delegated roles to tenant membership; preserve isolation and segregation of duties |
| Financial posting, close, consolidation | Accounting `accounting-general-ledger`, `accounting-periods`, `accounting-intercompany`, `accounting-consolidation`, `accounting-close-management` | Coordinate cross-product posting requests, close prerequisites, and reconciliation; do not create a second ledger |
| Leads, customers, opportunities, contracts | CRM `crm-customer-data-model`, `crm-sales-pipelines`, `crm-contracts`, `crm-proposals-and-quotes` | Define master customer identifiers and handoff contracts with billing and fulfillment |
| Subscriptions, invoicing, usage, collections | Billing source directories `module-billing-subscriptions`, `module-billing-invoicing`, `module-billing-usage`, `module-billing-collections` | Define billing-to-accounting posting and enterprise account hierarchies; avoid overlapping receivable write owners |
| Hosting, provisioning, infrastructure | Billing `module-billing-provisioning`; Control Panel `control-panel-containers`, `control-panel-kubernetes`, `control-panel-monitoring` | Coordinate approved service orders with infrastructure jobs, usage attribution, and operational evidence |
| Asset work, schedules, inspections | Maintenance `module-maintenance-assets`, `module-maintenance-work-orders`, `module-maintenance-inspections` | Connect operational assets to financial capitalization and cost dimensions using stable references |
| Procurement, inventory, logistics | Accounting receipt and inventory-accounting packages; Maintenance procurement/inventory candidates | Define commercial purchasing and physical stock ownership separately from financial valuation; review missing enterprise warehouse functions |
| Cross-domain reporting | Product reporting contracts and governed read models | Compose authorized metrics with lineage and reconciliation; never write operational records through reporting tables |
| People, treasury, regulatory packs, enterprise master data | Evaluate relevant accounting, CRM, and foundation contracts first | Add narrowly owned capabilities where the inventory and behavior review establish a real gap |

Candidate names above are source directory names. Look up exact Composer identities and pinned code in the [Accounting](../accounting/SOURCE-MODULES.md), [CRM](../crm/SOURCE-MODULES.md), [Billing](../billing/SOURCE-MODULES.md), [Control Panel](../control-panel/SOURCE-MODULES.md), and [Maintenance](../maintenance/SOURCE-MODULES.md) inventories. Source presence is insufficient to pass an adoption gate. Ecommerce also implements capabilities outside `modules/`; use its [application capability map](../ecommerce/SOURCE-APPLICATION.md) when reviewing inventory, orders, checkout, and integration reuse. Preserve its full documented catalogue while reviewing extraction and compatibility.

## Resolve duplicate capabilities before implementation

Choose one authoritative writer for each record and state transition. For example, billing may own the commercial invoice while Accounting owns the resulting receivable and ledger entries. They are linked records with different responsibilities, not competing invoice stores. Document which service assigns the invoice number, finalizes tax, collects payment, and authorizes correction. Integrate through versioned commands and events; never allow two packages to update the same lifecycle independently.

For each repeated identity in the [shared inventory](../../architecture/SOURCE-INVENTORY.md), compare files and migrations at pinned commits. Record dependencies, schema differences, test coverage, consuming applications, and public API differences. Pick a canonical source and maintainer; extract shared contracts only when they represent actual common behavior. Preserve product-specific policy through supported extension points. Migrate one consumer at a time with data reconciliation and explicit compatibility tests. Do not rename or delete live packages solely because their descriptions look similar.

New enterprise packages should own orchestration, legal-entity mappings, consolidation policy, cross-domain controls, or a documented capability gap. A `sap-finance` design group may compose many accounting packages without becoming another finance implementation. Apply the same rule to every presentation layer: a workspace can compose several existing adapters without copying their forms and actions.

## Example: order to cash

1. CRM approves a quote and sends a versioned order handoff with tenant, legal entity, currency, customer reference, product references, and an idempotency key.
2. The commercial order owner validates current prices and tax policy. Billing creates the appropriate order or subscription. Persist handoff status and the accepted source version.
3. A provisioning or delivery owner records fulfillment and returns its reference. A timeout produces a pending or failed handoff, not an unverified delivered state.
4. Billing finalizes an invoice according to its contract. An outbox record is committed with the local transition; a retryable delivery worker sends the posting request.
5. Accounting validates period, dimensions, currency treatment, and source uniqueness before posting. It returns the posting reference, or a structured rejection requiring correction.
6. Payment processing and reconciliation update their owned records. The workspace joins their published states into a read model and flags unmatched amounts or references.

The same message may arrive more than once: consumers deduplicate using the source operation identity. Do not hold a distributed database transaction across products. Capture correlation IDs, retry count, last error, and ownership of recovery. Financial corrections use explicit reversals or credit workflows under the owning package's rules. Reconcile counts and amounts by entity, currency, and posting period before closing a batch.

## Core and API delivery contracts

Core use cases accept an explicit actor/context, tenant and legal entity, domain inputs, and operation identity. Validate entity relationships and permissions before state changes. Use transactions within the owning database boundary; maintain event delivery state durably. Amounts use an agreed precise representation and currency, never ambiguous floating-point totals. Define effective dates, period closure, exchange-rate references, and rounding ownership for financial operations.

Publish query and command schemas, permissions, pagination, error bodies, idempotency behavior, concurrency rules, and compatibility guarantees in each API owner. Cross-domain commands return durable operation references when asynchronous. Document job polling, cancellation policy, expiry, and recovery rights. Bulk import supports validation reports and controlled application; exports enforce field-level and entity-level access at generation and download time.

Service-to-service credentials carry only required rights and are scoped to the integration's entity/tenant model. Never accept an arbitrary tenant header as authorization. Public read models must apply permissions when joining product data; database access alone is not a published integration contract.

## Presentation responsibilities

All layers display the same owned business transitions and audit references. Select adapters for the actual audience instead of implementing every technology for every deployment.

| Layer | Workspace implementation | Acceptance focus |
| --- | --- | --- |
| Core | Commands, policies, events, persistence, reconciliation | Invariants, isolation, idempotency, closed periods, recovery |
| API | Versioned authorized DTOs and operations over core contracts | Contract compatibility, validation, replay, concurrency, bulk operation authorization |
| Filament | Administrative resources, approval queues, reconciliation tables, controlled batch actions | Policy coverage on every action, restricted exports, entity switching, durable batch outcomes |
| Livewire | Server-owned task screens, step forms, approval details, operational status polling | Reauthorize actions and hydrated record IDs, preserve validation, prevent duplicate submissions |
| React + Inertia | Laravel-owned workspace routes and props, interactive module components | Prop visibility, route policies, redirects and errors, session expiry, navigation recovery |
| Vue + Inertia | Equivalent Laravel-owned workflows with Vue adapters | Same API/domain contracts; permission and validation parity with other web layers |
| Next.js | API-consuming role workspaces with application-owned routes and server integration | Tenant-aware cache isolation, secret exclusion, authorized server actions, API deployment compatibility |
| Nuxt | API-consuming Vue workspaces with explicit server/browser transport boundaries | Session forwarding, SSR isolation, cache policy, hydration and error recovery |
| React Native / Flutter | Focused approval, service, inspection, and field workflows | Secure credentials, attachment recovery, scoped offline data, conflict resolution and revocation |

Use shared design tokens, accessible controls, locale-aware money/date rendering, and consistent error terminology. Display active tenant and legal entity clearly before sensitive operations. For bulk actions show eligible records and denied/skipped counts; require a review step where the domain policy calls for approval. Preserve filters and record links so users can reconcile outcomes after long-running jobs.

See the existing layer indexes under [Core](core/README.md), [API](api/README.md), [Filament](filament/README.md), [Livewire](livewire/README.md), [React](react/README.md), [Vue](vue/README.md), [Next.js](nextjs/README.md), [Nuxt](nuxt/README.md), [React Native](react-native/README.md), and [Flutter](flutter/README.md).

## Adoption and rollout gates

A candidate is eligible for enterprise composition after its owner, supported versions, license, migration history, security boundaries, automated checks, operational recovery, and clean-consumer installation are verified. Record evidence per package and per consuming workflow. Packages with only placeholder behavior remain planned dependencies, even when their manifest declares a stable-looking version.

Start with one legal entity and one complete workflow in a non-production environment. Reconcile imported balances and source identifiers, test denied access and failed handoffs, rehearse replay and rollback, and compare workspace totals with authoritative product reports. Add entities and capabilities only after the acceptance evidence is repeatable. Deploy additive API changes first, consumers second, and remove obsolete contracts after the documented compatibility window.

Run dedicated scenarios for wrong-entity access, changed permissions during a job, duplicate payment notifications, closed-period postings, stale approvals, partial provisioning, failed exports, and offline mobile conflicts. Assign an operator and runbook to each asynchronous handoff; include queue lag, failed operation counts, reconciliation discrepancies, and escalation expectations in service monitoring.


## Shared source review evidence

The [shared module comparison](../../architecture/SHARED-MODULE-COMPARISON.md) distinguishes matching copies from runtime and manifest drift. Use the [consolidation procedure](../../architecture/SHARED-MODULES.md) before selecting a foundation dependency or replacing an enterprise reuse candidate.

Read the [16 detailed enterprise domain designs](design/README.md) for records, lifecycle, API operations, permissions, integration recovery, and per-layer delivery requirements.

The [shared-package adoption profiles](../../architecture/shared-adoption/README.md) document concrete foundation/platform variant differences that must be resolved before a shared dependency is treated as stable for enterprise composition.
