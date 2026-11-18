# Ecommerce: Catering — Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#catering). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Delivery boundary

Staff resources for meals, private recipes/yields, packages and event requests. Use policies for resource visibility and every action; show immutable quote/menu infolists and a recoverable conversion queue. Host panels register the adapter; package views provide defaults under the theme resolver.

## Shared workflow and security

Use the [core lifecycle](../core/catering.md) and [approved API contract](../api/catering.md). Show event requirements (date, timezone, venue, guests, dietary/service needs), menu quantities and revision, quote currency/expiry/revision and a clear acceptance confirmation. Show availability, accepted quote, order creation and payment as separate statuses. A changed menu or stale/expired quotation requires refresh/re-quote; never optimistically claim acceptance or payment success.

Staff-only capabilities maintain meals, recipes/yields and packages and investigate pending conversion. Customer-facing DTOs, caches, exports, notifications and error messages exclude recipes, preparation instructions and ingredient costs. Scope all caches and queries by actor/Team/Store; clear private state on sign-out or account/store switch. The server rechecks every policy and transition. Disable unavailable integrations with an actionable explanation.

Provide loading, empty, validation, permission-denied, conflict, offline, unavailable-capacity, expired-quote and pending-conversion states. Retrying uses the same conversion idempotency key and reconciles with the server. Quote acceptance/order conversion requires online confirmation and must never silently replay a stale offline action.

## Completion evidence

Test customer and staff journeys, keyboard/screen-reader or native semantics, timezone/currency formatting, stale revision recovery, duplicate taps, interrupted network, privacy after account switch and absence of sensitive fields in client storage/logs. Contract tests use approved schemas and a host integration test proves quote-to-order behavior. Keep all business rules in the owning domain; templates/widgets/components only present approved projections.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-ecommerce-laravel-filament`](https://github.com/liberusoftware/project-ecommerce-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | `module-ecommerce-catering-filament` | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/catering.md) · [API plan](../api/catering.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Meals and ingredient composition** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `meals and ingredient composition`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recipes and preparation yields** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recipes and preparation yields`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Staff-managed catering packages** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `staff-managed catering packages`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Event requirements and venue context** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `event requirements and venue context`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Immutable menu revisions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `immutable menu revisions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reproducible quotation context** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reproducible quotation context`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Availability confirmation and order conversion** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `availability confirmation and order conversion`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
