# Billing: Referrals and Advocate Rewards Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#referrals). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-billing-referrals-filament`  
**Matching domain module:** `referrals`  
**Matching core package:** [`module-billing-referrals`](../core/referrals.md) (`liberusoftware/billing-referrals`)  
**Application:** Billing  
**Source feature:** [Referrals and Advocate Rewards](../features/referrals.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `referrals` public contract boundary (`liberusoftware/affiliate-contracts (ReferralAttributionContract, ConversionRecorderContract, FraudAndSelfReferralPolicyContract, RewardFulfillmentContract)`). It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Referral programs and two-sided reward rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Advocate share links and referral codes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Referred signup and subscription qualification:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Duplicate, household, and self-referral prevention:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Automated reward fulfillment and clawback handling:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-billing-referrals-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `referral-programs-and-two-sided-reward-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `advocate-share-links-and-referral-codes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `referred-signup-and-subscription-qualification`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `duplicate-household-and-self-referral-prevention`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `automated-reward-fulfillment-and-clawback-handling`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | `module-billing-referrals-filament` | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/referrals.md) · [API plan](../api/referrals.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Referral programs and two-sided reward rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `referral programs and two-sided reward rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Advocate share links and referral codes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `advocate share links and referral codes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Referred signup and subscription qualification** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `referred signup and subscription qualification`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Duplicate, household, and self-referral prevention** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `duplicate, household, and self-referral prevention`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Automated reward fulfillment and clawback handling** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `automated reward fulfillment and clawback handling`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
