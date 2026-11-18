# Liberu: Revenue and Care Orchestration Filament

**Existing cross-project implementations:** the [platform reuse guide](../REUSE.md) identifies the observed prefixed/unprefixed package families, namespaces, tables and adoption constraints. This scope is their composition/design home; it does not require a third independent implementation.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#revenue-and-care-orchestration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** `module-liberu-revenue-and-care-orchestration-filament`
**Core/API:** [Core](../core/revenue-and-care-orchestration.md) · [API](../api/revenue-and-care-orchestration.md)

Provide a responsive operator panel for customer health, care queue, signal evidence, outreach eligibility, recovery requests, AI recommendations, and projection/reconciliation exceptions. Use read-only source links, policy-aware actions, safe reason codes, visible freshness, and explicit approval dialogs. Never edit CRM, Billing, Control Panel, or Automation records from this resource; dispatch their public actions and show the resulting operation status.

Test tenant/brand isolation, field visibility, authorization, stale/empty/error/queued states, confirmation, keyboard access, responsive tables, and audit entries.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-liberu-official-laravel-filament`](https://github.com/liberusoftware/project-liberu-official-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-planned-liberu-revenue-and-care-orchestration-40451d50-filament`](https://github.com/liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-filament) (`liberusoftware/planned-liberu-revenue-and-care-orchestration-40451d50-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/revenue-and-care-orchestration.md) · [API plan](../api/revenue-and-care-orchestration.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Customer health constellation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `customer health constellation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Revenue-aware service recovery** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `revenue-aware service recovery`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Contact-protection ledger** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `contact-protection ledger`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cross-brand consent and quiet-hour evaluation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cross-brand consent and quiet-hour evaluation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approval-gated AI recommendations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approval-gated ai recommendations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Mobile-ready daily queues** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `mobile-ready daily queues`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
