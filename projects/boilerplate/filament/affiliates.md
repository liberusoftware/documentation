# Boilerplate: Affiliates and Partner Programs Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-affiliates-filament`  
**Matching domain module:** `affiliates`  
**Matching core package:** [`module-affiliates`](../core/affiliates.md) (`liberusoftware/affiliate-core`)  
**Application:** Boilerplate  
**Source feature:** [Affiliates and Partner Programs](../features/affiliates.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `affiliates` public contract boundary (`liberusoftware/affiliate-contracts (AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, ConversionRecorderContract, CommissionCalculatorContract, PayoutSettlementContract)`). It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Affiliate program and commission tier rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Partner applications, KYC/tax readiness, and approval:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tracking links, campaign parameters, and promo codes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Authoritative conversion ingestion and hold ledger:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Automated refund, cancellation, and dispute clawbacks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Self-referral, velocity, and fraud screening:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payout approval batches and settlement handoff:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-affiliates-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `affiliate-program-and-commission-tier-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `partner-applications-kyc-tax-readiness-and-approval`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tracking-links-campaign-parameters-and-promo-codes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `authoritative-conversion-ingestion-and-hold-ledger`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `automated-refund-cancellation-and-dispute-clawbacks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `self-referral-velocity-and-fraud-screening`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payout-approval-batches-and-settlement-handoff`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | `module-boilerplate-affiliates-filament` | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/affiliates.md) · [API plan](../api/affiliates.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Affiliate program and commission tier rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `affiliate program and commission tier rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Partner applications, KYC/tax readiness, and approval** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `partner applications, kyc/tax readiness, and approval`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tracking links, campaign parameters, and promo codes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tracking links, campaign parameters, and promo codes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Authoritative conversion ingestion and hold ledger** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `authoritative conversion ingestion and hold ledger`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Automated refund, cancellation, and dispute clawbacks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `automated refund, cancellation, and dispute clawbacks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Self-referral, velocity, and fraud screening** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `self-referral, velocity, and fraud screening`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Payout approval batches and settlement handoff** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payout approval batches and settlement handoff`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
