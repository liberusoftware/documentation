# Boilerplate: Affiliate Contracts Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-affiliate-contracts-filament`  
**Matching domain module:** `affiliate-contracts`  
**Matching core package:** [`module-affiliate-contracts`](../core/affiliate-contracts.md) (`liberusoftware/affiliate-contracts`)  
**Application:** Boilerplate  
**Source feature:** [Affiliate Contracts](../features/affiliate-contracts.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `affiliate-contracts` public contract boundary (`AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, FraudAndSelfReferralPolicyContract, ConversionRecorderContract, CommissionCalculatorContract, PayoutSettlementContract, RewardFulfillmentContract`). It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **AffiliateProgramContract and attribution window DTOs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **ReferralAttributionContract and signed touch tokens:** resource/table/form/action or page behavior for this module's authorized workflow.
- **ConversionRecorderContract and idempotent clawbacks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **CommissionCalculatorContract and tiered rate rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **FraudAndSelfReferralPolicyContract:** resource/table/form/action or page behavior for this module's authorized workflow.
- **PayoutSettlementContract and RewardFulfillmentContract:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-affiliate-contracts-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `affiliateprogramcontract-and-attribution-window-dtos`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `referralattributioncontract-and-signed-touch-tokens`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `conversionrecordercontract-and-idempotent-clawbacks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `commissioncalculatorcontract-and-tiered-rate-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `fraudandselfreferralpolicycontract`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payoutsettlementcontract-and-rewardfulfillmentcontract`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | `module-boilerplate-affiliate-contracts-filament` | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/affiliate-contracts.md) · [API plan](../api/affiliate-contracts.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **AffiliateProgramContract and attribution window DTOs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `affiliateprogramcontract and attribution window dtos`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **ReferralAttributionContract and signed touch tokens** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `referralattributioncontract and signed touch tokens`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **ConversionRecorderContract and idempotent clawbacks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `conversionrecordercontract and idempotent clawbacks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **CommissionCalculatorContract and tiered rate rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `commissioncalculatorcontract and tiered rate rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **FraudAndSelfReferralPolicyContract** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `fraudandselfreferralpolicycontract`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **PayoutSettlementContract and RewardFulfillmentContract** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payoutsettlementcontract and rewardfulfillmentcontract`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
